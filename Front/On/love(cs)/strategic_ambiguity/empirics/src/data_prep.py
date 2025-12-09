"""
src/data_prep.py
===================================
Step 06: Measurement & Data Preparation Factory

Transforms raw transaction data into a multi-dimensional Xarray cube (panel_v3.nc).
Key Logic:
  1. Decomposes Vagueness into V_market (Entropy) and V_tech (Abstractness).
  2. Computes Founder Credibility (Serial Entrepreneurship) with caching.
  3. Builds Time-Varying Outcomes (L, S) across horizons [24, 36, 48].
  4. Identifies Moderators (F: is_software, Sector).
"""

from pathlib import Path
import pandas as pd
import numpy as np
import xarray as xr
import logging
import re
from typing import Optional, Tuple, List

# 로컬 모듈 임포트 (src 패키지 내)
from .definitions import (
    MARKET_KEYWORDS, TECH_SPEC_PATTERNS, CONSTANTS,
    ARCH_SOFTWARE_KEYWORDS, ARCH_HARDWARE_KEYWORDS,
    NANDA_SECTOR_TO_CODE
)
from .vagueness_v3 import StrategicVaguenessScorerV3
from .cache_manager import CacheManager

logger = logging.getLogger(__name__)

# =============================================================================
# 1. Helper Functions (Data Cleaning)
# =============================================================================

def _read_raw(input_path: str) -> pd.DataFrame:
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    
    if path.suffix == '.parquet':
        return pd.read_parquet(path)
    return pd.read_csv(path, low_memory=False)

def _standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """PitchBook 등 벤더별 컬럼명을 표준화"""
    rename_map = {
        'CompanyID': 'company_id', 'Description': 'description', 'Keywords': 'keywords',
        'DealDate': 'deal_date', 'DealAmount': 'deal_amount', 
        'PrimaryIndustryCode': 'industry_code', 'PreMoneyValuation': 'premoney',
        'PostMoneyValuation': 'postmoney', 'YearFounded': 'year_founded',
        'PrimaryContactPBId': 'person_id', 'PrimaryContactTitle': 'person_title'
    }
    # 대소문자 무시 매핑을 위해 컬럼명 정규화 로직 추가 가능
    df = df.rename(columns=rename_map)
    
    # 날짜 변환
    if 'deal_date' in df.columns:
        df['deal_date'] = pd.to_datetime(df['deal_date'], errors='coerce')
    
    return df

def _infer_round_type(series: pd.Series) -> pd.Series:
    """라운드 명칭 정규화 (Series A, B...)"""
    s = series.fillna('').astype(str).str.lower()
    out = pd.Series('Other', index=s.index)
    out[s.str.contains('seed|angel')] = 'Seed'
    out[s.str.contains('series a') | (s == 'a')] = 'A'
    out[s.str.contains('series b') | (s == 'b')] = 'B'
    out[s.str.contains(r'series [c-z]')] = 'Late'
    return out

# =============================================================================
# 2. Feature Engineering Logic
# =============================================================================

def _classify_is_software(text: str) -> int:
    """F (Exercisability) 측정: SW 키워드가 HW보다 많으면 1"""
    if not isinstance(text, str): return 0
    text = text.lower()
    sw_count = sum(1 for k in ARCH_SOFTWARE_KEYWORDS if k in text)
    hw_count = sum(1 for k in ARCH_HARDWARE_KEYWORDS if k in text)
    # Tie-breaker: SW 우선 (현대 벤처의 기본 속성)
    return 1 if sw_count >= hw_count else 0

def _compute_founder_credibility(raw_df: pd.DataFrame, cache: CacheManager) -> pd.DataFrame:
    """
    C (Founder Credibility): 인명부 구축 및 캐싱
    """
    step_name = 'founder_features'
    scenario = 'all'
    
    # 1. 캐시 확인
    if cache.is_valid(step=step_name, scenario=scenario):
        logger.info("📜 Founder DB found in cache. Loading...")
        return cache.load_step(step=step_name, scenario=scenario)

    # 2. 캐시 없으면 계산
    logger.info("⚡ Computing Founder Credibility (Expensive Operation)...")
    df = raw_df.copy()
    df['person_id'] = df['person_id'].fillna('UNKNOWN')
    
    # Founder/CEO 필터링
    role_mask = df['person_title'].fillna('Founder').str.contains(
        r'Founder|Co-Founder|CEO|Chief Executive|President', case=False, regex=True
    )
    
    # 창업자 데이터 추출 및 정렬
    founders = df.loc[role_mask & (df['person_id'] != 'UNKNOWN')].copy()
    founders = founders.sort_values(['person_id', 'year_founded'])
    
    # 시점 의존적 Serial Count (이전 창업 횟수)
    founders['serial_count'] = founders.groupby('person_id').cumcount()
    founders['is_serial'] = (founders['serial_count'] >= 1).astype(int)
    
    # 회사별 Max Credibility (공동창업자 중 한 명이라도 경험 있으면 인정)
    founder_db = founders.groupby('company_id')['is_serial'].max().reset_index()
    founder_db.columns = ['company_id', 'founder_credibility']
    
    # 3. 저장
    cache.save_step(step=step_name, data=founder_db, scenario=scenario)
    return founder_db

def _compute_outcomes_and_early_funding(df: pd.DataFrame, horizons: List[int]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    E (Early Funding), L (Later Success), S (Step-up) 계산
    """
    df['norm_round'] = _infer_round_type(df['DealType'] if 'DealType' in df.columns else df['Round'])
    
    # Series A (Early Funding Baseline)
    series_a = df[df['norm_round'] == 'A'].sort_values('deal_date').drop_duplicates('company_id')
    series_a = series_a.set_index('company_id')
    
    # Outcomes (L, S) Dictionary
    outcomes = {
        'L_outcome': {},
        'S_stepup': {}
    }
    
    for h in horizons:
        # Horizon (개월) 이후의 날짜 계산
        cutoff_date = series_a['deal_date'] + pd.to_timedelta(h, unit='D') * 30.5
        
        # Series B 이상이면서 Horizon 이내인 딜 찾기
        later_rounds = df[
            (df['norm_round'].isin(['B', 'Late'])) & 
            (df['company_id'].isin(series_a.index))
        ].copy()
        
        # 각 회사별로 Horizon 이내에 성공했는지 체크
        # (이 부분은 벡터화가 까다로워 로직 설명용으로 간소화함. 실제 구현 시 merge/filter 사용 권장)
        # 여기서는 간단한 플래그 로직 예시:
        success_ids = []
        stepups = {}
        
        # (실제로는 더 최적화된 판다스 연산 필요)
        # ... [생략: 조인 연산으로 L, S 계산] ...
        # 나대용이 구현할 영역. 여기서는 구조만 잡음.
    
    # Placeholder for demonstration (나대용이 채울 로직)
    # 실제로는 Series A 데이터프레임(E)과 Outcome 데이터프레임(L, S)을 리턴
    return series_a, pd.DataFrame() 


# =============================================================================
# 3. Main Pipeline Function
# =============================================================================

def build_panel_v3(
    input_parquet_path: str,
    output_netcdf_path: str = None,
    index_col: Optional[str] = 'company_id'
) -> xr.Dataset:
    """
    Build panel dataset v3: Parquet -> Xarray NetCDF with V-Decomposition.
    """
    # 1. Init Cache & Load Raw
    cache = CacheManager()
    raw = _read_raw(input_parquet_path)
    raw = _standardize_columns(raw)
    logger.info(f"📂 Raw Data Loaded: {len(raw):,} rows")

    # 2. Founder Credibility (Merge Cached DB)
    founder_db = _compute_founder_credibility(raw, cache)
    raw = raw.merge(founder_db, on='company_id', how='left')
    raw['founder_credibility'] = raw['founder_credibility'].fillna(0).astype('int8')

    # 3. Text Processing & V-Scoring (V3)
    logger.info("🧠 Scoring Vagueness (V3: Market Entropy vs Tech Abstractness)...")
    
    # 텍스트 결합
    raw['full_text'] = (raw['description'].fillna('') + ' ' + raw['keywords'].fillna('')).str.lower()
    
    # Scorer 호출
    scorer = StrategicVaguenessScorerV3()
    scorer.fit(raw['full_text']) # Density 분포 학습
    
    # 배치 처리를 위해 Series로 전달
    v_scores = scorer.score_series(raw['full_text']) # DataFrame 반환
    
    # 결과 병합
    raw = pd.concat([raw, v_scores], axis=1)
    
    # 4. Moderators (F, Sector)
    raw['is_software'] = raw['full_text'].apply(_classify_is_software).astype('int8')
    
    # Nanda Sector Mapping (간소화)
    raw['nanda_sector'] = raw['industry_code'].map(lambda x: 0).astype('int8') # TODO: 매핑 로직 연결

    # 5. Outcomes (Time-Varying L, S) & E (Static)
    # 단순화를 위해, 여기서는 Series A가 있는 기업만 필터링하여 패널을 만듭니다.
    # 실제 구현 시 _compute_outcomes_and_early_funding 로직을 정교하게 짜야 함.
    
    # (가정) 이미 벤처 단위로 정리된 데이터라고 칩니다.
    # 실제로는 Transaction -> Venture 변환이 필요함.
    venture_df = raw.drop_duplicates('company_id').set_index('company_id')
    
    # 6. Assemble Xarray Dataset
    logger.info("📦 Assembling Venture Cube (Xarray)...")
    
    venture_ids = venture_df.index.values
    horizons = CONSTANTS['HORIZONS']
    
    # 데이터 배열 생성 (N x H)
    # L_outcome과 S_stepup은 별도 로직으로 채워야 함 (여기서는 0/NaN으로 초기화)
    L_data = np.zeros((len(venture_ids), len(horizons)), dtype='int8')
    S_data = np.full((len(venture_ids), len(horizons)), np.nan, dtype='float32')
    
    ds = xr.Dataset(
        data_vars={
            # Predictors
            'V_market_entropy': (('venture_id'), venture_df['V_market_entropy'].values.astype('float32')),
            'V_tech_abstractness': (('venture_id'), venture_df['V_tech_abstractness'].values.astype('float32')),
            'V_composite': (('venture_id'), venture_df['V_composite'].values.astype('float32')),
            
            # Moderators
            'is_software': (('venture_id'), venture_df['is_software'].values.astype('int8')),
            'founder_credibility': (('venture_id'), venture_df['founder_credibility'].values.astype('int8')),
            'nanda_sector': (('venture_id'), venture_df['nanda_sector'].values.astype('int8')),
            
            # Outcomes (Time-varying)
            'L_outcome': (('venture_id', 'horizon'), L_data),
            'S_stepup': (('venture_id', 'horizon'), S_data),
        },
        coords={
            'venture_id': venture_ids,
            'horizon': horizons
        },
        attrs={
            'description': 'Panel V3: Decomposed Vagueness & Time-varying Outcomes',
            'source_file': str(input_parquet_path),
            'schema_version': '3.0'
        }
    )

    # 7. Save via CacheManager
    logger.info(f"💾 Saving Xarray Panel to Cache...")
    cache.save_xarray(step='panel_v3', dataset=ds, scenario='all')
    
    # 사용자가 요청한 경로에도 저장
    if output_netcdf_path:
        output_path = Path(output_netcdf_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        ds.to_netcdf(output_path)
        logger.info(f"✓ Backup saved to: {output_path}")

    return ds

if __name__ == "__main__":
    # CLI 실행용 (예시)
    import sys
    if len(sys.argv) > 1:
        build_panel_v3(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)