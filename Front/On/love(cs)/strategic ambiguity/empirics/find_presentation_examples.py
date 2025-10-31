#!/usr/bin/env python3
"""
Presentation Examples Finder
=============================
논문 발표용 4개사 대표 예시를 추출하는 스크립트.

기존 features.py 모듈의 함수들을 활용하여:
- Vagueness 계산
- Hardware/Software 분류
- Series A(2021) → Series B+ 또는 M&A 결과 추적

목표: 다음 조건을 만족하는 정확히 4개 회사 추출
- 도메인: AI Software(1), Autonomous Vehicles(1), Quantum Computing(2)
- Series A: 2021년 (M&A는 2022-2023 허용)
- 결과 다양성: Rapid B+(L=1), Slow B+(L=0), M&A(Censored)
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
import re
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Import features.py functions
sys.path.insert(0, str(Path(__file__).parent))
from modules.features import (
    compute_vagueness_vectorized,
    classify_hardware_vectorized
)

# Column mapping (adjust based on actual PitchBook export)
COLUMN_MAP = {
    'id': 'CompanyID',
    'name': 'CompanyName',
    'desc': 'Description',
    'keys': 'Keywords',
    'status': 'BusinessStatus',
    # Deal-related columns
    'deal_type': 'FinancingType',
    'deal_date': 'FinancingDate',
    'deal_size': 'FinancingSize'
}

# Deal type patterns (matching features.py logic)
B_PLUS_PAT = r"(?i)series\s*[b-z]|later\s*stage"
MA_PAT = r"(?i)acquired|acquisition|merger"

def classify_domain_custom(keywords: str, description: str) -> str:
    """
    도메인을 3가지로 분류: AI Software, Autonomous Vehicles, Quantum Computing

    Args:
        keywords: 회사 키워드
        description: 회사 설명

    Returns:
        도메인 문자열
    """
    if pd.isna(keywords):
        keywords = ""
    if pd.isna(description):
        description = ""

    text = f"{keywords} {description}".lower()

    # Quantum Computing (highest priority)
    if any(k in text for k in ["quantum", "qbit", "qubit"]):
        return "Quantum Computing"

    # Autonomous Vehicles
    if any(k in text for k in ["autonomous vehicle", "self-driving", "av ", "adas", "autonomous driving"]):
        return "Autonomous Vehicles"

    # AI Software
    if any(k in text for k in ["artificial intelligence", "ai ", "machine learning", "ml ",
                                "deep learning", "neural network", "nlp", "computer vision",
                                "natural language"]):
        return "AI Software"

    return "Other"


def parse_deals_from_company_row(row, deal_type_col='FinancingType', deal_date_col='FinancingDate'):
    """
    회사 행에서 딜 정보 파싱 (PitchBook 데이터 구조에 따라 조정 필요)

    이 함수는 PitchBook 데이터 구조에 맞게 수정이 필요할 수 있습니다.
    일반적으로 PitchBook 데이터는:
    1. 각 딜이 별도의 행으로 있거나
    2. 회사당 하나의 행에 여러 딜 정보가 컬럼으로 있거나
    3. JSON/리스트 형태로 딜 정보가 포함되어 있음

    Returns:
        list of dict: [{'type': 'Series B', 'date': pd.Timestamp(...)}, ...]
    """
    deals = []

    # Method 1: 각 행이 하나의 딜 (가장 일반적)
    if deal_type_col in row and pd.notna(row[deal_type_col]):
        deals.append({
            'type': str(row[deal_type_col]),
            'date': pd.to_datetime(row[deal_date_col], errors='coerce')
        })

    return deals


def find_example_outcomes(company_id, df_all_deals, series_a_date):
    """
    Series A 이후 첫 번째 Series B+ 또는 M&A 딜을 찾음

    Args:
        company_id: 회사 ID
        df_all_deals: 전체 딜 데이터프레임 (각 행이 하나의 딜)
        series_a_date: Series A 날짜 (기준점 t_0)

    Returns:
        dict: {
            'outcome_type': str,
            'outcome_date': pd.Timestamp,
            'months_to_outcome': float
        }
    """
    # 해당 회사의 딜만 필터링
    company_deals = df_all_deals[df_all_deals[COLUMN_MAP['id']] == company_id].copy()

    # Series A 이후 딜만
    company_deals['deal_date_parsed'] = pd.to_datetime(company_deals[COLUMN_MAP['deal_date']], errors='coerce')
    post_a_deals = company_deals[company_deals['deal_date_parsed'] > series_a_date].copy()

    if len(post_a_deals) == 0:
        return {
            'outcome_type': 'No B+/M&A',
            'outcome_date': pd.NaT,
            'months_to_outcome': np.nan
        }

    # 날짜순 정렬
    post_a_deals = post_a_deals.sort_values('deal_date_parsed')

    # 첫 번째 B+ 또는 M&A 찾기
    for _, deal in post_a_deals.iterrows():
        deal_type = str(deal[COLUMN_MAP['deal_type']])
        deal_date = deal['deal_date_parsed']

        # M&A 체크 (우선순위 높음)
        if re.search(MA_PAT, deal_type):
            months = (deal_date - series_a_date).days / 30.44
            return {
                'outcome_type': 'M&A',
                'outcome_date': deal_date,
                'months_to_outcome': months
            }

        # Series B+ 체크
        if re.search(B_PLUS_PAT, deal_type):
            months = (deal_date - series_a_date).days / 30.44
            return {
                'outcome_type': 'Series B+',
                'outcome_date': deal_date,
                'months_to_outcome': months
            }

    # B+/M&A 없음
    return {
        'outcome_type': 'No B+/M&A',
        'outcome_date': pd.NaT,
        'months_to_outcome': np.nan
    }


def assign_l_code(outcome_type: str, months_to_outcome: float, window_months: int = 17) -> str:
    """
    L-Code 할당: '1' (Rapid B+), '0' (Slow/No B+), 'Censored' (M&A)

    Args:
        outcome_type: 결과 타입
        months_to_outcome: Series A로부터 경과 개월
        window_months: 기준 기간 (기본 17개월)

    Returns:
        L-Code 문자열
    """
    if "M&A" in outcome_type:
        return "Censored"

    if pd.isna(months_to_outcome) or outcome_type == 'No B+/M&A':
        return "0"

    if months_to_outcome <= window_months:
        return "1"  # Rapid B+
    else:
        return "0"  # Slow B+


def find_presentation_cohort(df_raw: pd.DataFrame, output_path: Path = None) -> pd.DataFrame:
    """
    메인 함수: 발표용 4개사 코호트 추출

    Args:
        df_raw: PitchBook 원본 데이터
        output_path: 결과 저장 경로 (optional)

    Returns:
        4개사 DataFrame
    """
    print("="*80)
    print("PRESENTATION EXAMPLES FINDER")
    print("="*80)
    print(f"\n📊 Input data: {len(df_raw):,} rows\n")

    # Step 1: 기본 정제
    df = df_raw.copy()

    # CompanyID가 있는지 확인
    id_col = COLUMN_MAP['id']
    if id_col not in df.columns:
        print(f"❌ ERROR: Column '{id_col}' not found in data")
        print(f"Available columns: {list(df.columns)[:10]}...")
        raise KeyError(f"Column '{id_col}' not found")

    # Step 2: features.py 함수 활용
    print("🔧 Applying features.py functions...")

    # Vagueness 계산
    desc_col = COLUMN_MAP['desc']
    keys_col = COLUMN_MAP['keys']

    if desc_col in df.columns and keys_col in df.columns:
        print(f"  Computing vagueness...")
        df['vagueness'] = compute_vagueness_vectorized(
            df[desc_col].fillna(""),
            df[keys_col].fillna("")
        )
        print(f"  ✓ Vagueness computed: mean={df['vagueness'].mean():.3f}")
    else:
        print(f"  ⚠️  Missing description/keywords columns - vagueness set to NaN")
        df['vagueness'] = np.nan

    # Hardware 분류
    if keys_col in df.columns:
        print(f"  Computing is_hardware...")
        df['is_hardware'] = classify_hardware_vectorized(
            df[keys_col].fillna(""),
            df[desc_col].fillna("") if desc_col in df.columns else None
        )
        print(f"  ✓ Hardware classified: {df['is_hardware'].sum():,} hardware companies")
    else:
        df['is_hardware'] = 0

    # Domain 분류 (맞춤형)
    print(f"  Computing domain classification...")
    df['domain'] = df.apply(
        lambda row: classify_domain_custom(
            row.get(keys_col, ""),
            row.get(desc_col, "")
        ),
        axis=1
    )
    domain_counts = df['domain'].value_counts()
    print(f"  ✓ Domains classified:")
    for domain, count in domain_counts.items():
        print(f"    - {domain}: {count:,}")

    # Step 3: Series A 코호트 필터링 (2021년)
    print(f"\n🔍 Filtering Series A cohort (2021)...")

    # Series A 정보 찾기
    deal_type_col = COLUMN_MAP['deal_type']
    deal_date_col = COLUMN_MAP['deal_date']

    if deal_type_col not in df.columns or deal_date_col not in df.columns:
        print(f"❌ ERROR: Deal columns not found")
        print(f"Available columns: {list(df.columns)[:20]}...")
        raise KeyError("Deal columns not found")

    # Series A 필터링
    df['is_series_a'] = df[deal_type_col].fillna("").str.contains(r"(?i)series\s*a(?![b-z])", regex=True)
    df['deal_year'] = pd.to_datetime(df[deal_date_col], errors='coerce').dt.year

    df_series_a = df[df['is_series_a'] & (df['deal_year'] == 2021)].copy()
    print(f"  ✓ Found {len(df_series_a):,} Series A deals in 2021")

    # Step 4: 각 회사의 Outcome 계산
    print(f"\n📈 Computing outcomes for each company...")

    df_series_a['series_a_date'] = pd.to_datetime(df_series_a[deal_date_col], errors='coerce')

    outcomes = []
    for idx, row in df_series_a.iterrows():
        outcome = find_example_outcomes(
            row[id_col],
            df,  # 전체 데이터에서 딜 찾기
            row['series_a_date']
        )
        outcome['company_id'] = row[id_col]
        outcomes.append(outcome)

    df_outcomes = pd.DataFrame(outcomes)
    df_series_a = df_series_a.merge(df_outcomes, left_on=id_col, right_on='company_id', how='left')

    # L-Code 할당
    df_series_a['l_code'] = df_series_a.apply(
        lambda row: assign_l_code(row['outcome_type'], row['months_to_outcome']),
        axis=1
    )

    print(f"  ✓ Outcomes computed:")
    outcome_counts = df_series_a['outcome_type'].value_counts()
    for outcome, count in outcome_counts.items():
        print(f"    - {outcome}: {count:,}")

    l_code_counts = df_series_a['l_code'].value_counts()
    print(f"  ✓ L-Codes:")
    for code, count in l_code_counts.items():
        print(f"    - {code}: {count:,}")

    # Step 5: 조건에 맞는 4개사 선택
    print(f"\n🎯 Selecting 4 representative companies...")

    target_domains = {
        'AI Software': 1,
        'Autonomous Vehicles': 1,
        'Quantum Computing': 2
    }

    selected = []

    for domain, target_count in target_domains.items():
        domain_companies = df_series_a[df_series_a['domain'] == domain].copy()
        print(f"\n  {domain}: {len(domain_companies)} candidates")

        if len(domain_companies) == 0:
            print(f"    ⚠️  No companies found in {domain}")
            continue

        # 결과 다양성 확보
        l_codes_needed = ['1', '0', 'Censored']
        for l_code in l_codes_needed[:target_count]:
            candidates = domain_companies[domain_companies['l_code'] == l_code]
            if len(candidates) > 0:
                # Vagueness가 높은 순으로 선택 (더 흥미로운 예시)
                best = candidates.nlargest(1, 'vagueness', keep='first')
                selected.append(best)
                print(f"    ✓ Selected 1 company with L={l_code}")
                domain_companies = domain_companies[domain_companies[id_col] != best[id_col].values[0]]
            else:
                # 대체: 아무거나 선택
                if len(domain_companies) > 0:
                    best = domain_companies.nlargest(1, 'vagueness', keep='first')
                    selected.append(best)
                    print(f"    ✓ Selected 1 company (fallback)")
                    domain_companies = domain_companies[domain_companies[id_col] != best[id_col].values[0]]

    if len(selected) == 0:
        print(f"\n❌ ERROR: No companies selected!")
        return pd.DataFrame()

    df_final = pd.concat(selected, ignore_index=True)

    # Step 6: 최종 스키마로 정제
    print(f"\n📋 Final cohort: {len(df_final)} companies")

    output_columns = [
        'company_name',
        'domain',
        'promise_text',
        'keywords',
        'vagueness',
        'series_a_date',
        'outcome_type',
        'outcome_date',
        'months_to_outcome',
        'l_code'
    ]

    # 컬럼 이름 매핑
    df_export = pd.DataFrame()
    df_export['company_name'] = df_final[COLUMN_MAP['name']]
    df_export['domain'] = df_final['domain']
    df_export['promise_text'] = df_final[COLUMN_MAP['desc']].str[:200] + "..."  # 200자로 제한
    df_export['keywords'] = df_final[COLUMN_MAP['keys']]
    df_export['vagueness'] = df_final['vagueness'].round(3)
    df_export['series_a_date'] = df_final['series_a_date']
    df_export['outcome_type'] = df_final['outcome_type']
    df_export['outcome_date'] = df_final['outcome_date']
    df_export['months_to_outcome'] = df_final['months_to_outcome'].round(1)
    df_export['l_code'] = df_final['l_code']

    # 결과 출력
    print("\n" + "="*80)
    print("SELECTED COMPANIES")
    print("="*80)
    for idx, row in df_export.iterrows():
        print(f"\n{idx+1}. {row['company_name']}")
        print(f"   Domain: {row['domain']}")
        print(f"   Vagueness: {row['vagueness']:.3f}")
        print(f"   Series A: {row['series_a_date'].strftime('%Y-%m-%d')}")
        print(f"   Outcome: {row['outcome_type']} (L={row['l_code']})")
        if pd.notna(row['outcome_date']):
            print(f"   Outcome Date: {row['outcome_date'].strftime('%Y-%m-%d')} ({row['months_to_outcome']:.1f} months)")

    # 저장
    if output_path:
        df_export.to_csv(output_path, index=False)
        print(f"\n✅ Saved to: {output_path}")

    return df_export


def main():
    """메인 실행 함수"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Find 4 representative companies for presentation"
    )
    parser.add_argument(
        '--input',
        type=str,
        default='data/raw/Company20211201.dat',
        help='Input PitchBook data file'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='outputs/presentation_examples.csv',
        help='Output CSV file'
    )

    args = parser.parse_args()

    # 데이터 로드
    print(f"\n📂 Loading data from: {args.input}")
    try:
        df = pd.read_csv(args.input, sep='|', encoding='utf-8', low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(args.input, sep='|', encoding='latin-1', low_memory=False)

    print(f"✓ Loaded {len(df):,} rows, {len(df.columns)} columns")

    # 4개사 찾기
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df_examples = find_presentation_cohort(df, output_path)

    if len(df_examples) < 4:
        print(f"\n⚠️  WARNING: Only found {len(df_examples)} companies (target: 4)")
        print("Consider:")
        print("  - Relaxing Series A year constraint")
        print("  - Expanding domain definitions")
        print("  - Using different L-code distribution")

    print("\n✅ Done!")
    return df_examples


if __name__ == "__main__":
    main()
