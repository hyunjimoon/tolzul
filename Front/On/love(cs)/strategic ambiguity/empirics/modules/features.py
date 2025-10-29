# features.py
"""
Feature Engineering for W1
- StrategicVaguenessScorer (Description + Keywords)
- Architecture classification: is_hardware (1=Hardware/Integrated, 0=Software/Modular)
- Founder credibility (robust, ID-based when available)
- Survival→growth DV helpers
- Preprocess for W1 (z-scores, cohorts, aliases)
"""

from __future__ import annotations
import pandas as pd
import numpy as np
import re
from typing import Optional, List

# =============================================================================
# 0) Utility
# =============================================================================

def _z(series: pd.Series) -> pd.Series:
    s = pd.to_numeric(series, errors='coerce')
    if s.std(ddof=0) == 0 or np.isnan(s.std(ddof=0)):
        return pd.Series(np.nan, index=s.index)
    return (s - s.mean()) / s.std()

# =============================================================================
# 1) Strategic Vagueness (Description + Keywords)
# =============================================================================

class StrategicVaguenessScorer:
    """
    Three-pillar vagueness for venture texts:
    1) Lexical Uncertainty (Loughran & McDonald 2011/2016)
    2) Concreteness Deficit (Chen et al. 2015; Pan et al. 2018)
    3) Categorical Vagueness (Zuckerman 1999; Hannan et al. 2007)
    Outputs 0–100 (higher = more vague).
    """

    def __init__(self):
        self.lm_uncertainty = {
            'approximately','believe','could','depend','estimate','expect',
            'intend','may','might','possible','probable','risk','uncertain',
            'vary','anticipate','potential','project','forecast','seek',
            'contingent','future','unclear','unspecified'
        }
        self.concreteness_markers = {
            'temporal': r'\b(Q[1-4]\s*20\d{2}|20\d{2})\b',
            'quant_tech': r'\b(\d+[\.\d]*[xX%]?|[A-Z]{2,}\d*|\bL(evel)?\s*\d)\b',
            'acronym': r'\b[A-Z]{3,}\b'
        }
        self.abstraction_keywords = {
            'platform','solution','ecosystem','technology','approach',
            'service','market','advanced','next-generation','sustainable',
            'cloud','ai','data','analytics','software','future'
        }

    def _tok(self, text: str) -> List[str]:
        if not isinstance(text, str) or not text:
            return []
        return re.findall(r'\b\w+\b', text.lower())

    def _lexical_uncertainty(self, words: List[str]) -> float:
        if not words: return 0.0
        cnt = sum(1 for w in words if w in self.lm_uncertainty)
        ratio = cnt / len(words)
        return min(ratio * 1000, 100)

    def _concreteness_deficit(self, raw_text: str, words: List[str]) -> float:
        if not words: return 100.0
        specific = 0
        for p in self.concreteness_markers.values():
            specific += len(re.findall(p, raw_text))
        ratio = specific / len(words)
        precision = min(ratio * 500, 100)  # cap
        return 100 - precision

    def _categorical_vagueness(self, kw_list: List[str]) -> float:
        if not kw_list: return 100.0
        kw = [k.strip().lower() for k in kw_list if k and isinstance(k, str)]
        if not kw: return 100.0
        abstraction = sum(1 for w in kw if w in self.abstraction_keywords) / len(kw)
        uniqueness = len(set(kw)) / len(kw)
        return (abstraction + uniqueness) / 2 * 100

    def score(self, description: str, keywords: str) -> float:
        words = self._tok(description or "")
        kw_list = [k.strip() for k in (keywords or "").split(",")]
        s1 = self._lexical_uncertainty(words)
        s2 = self._concreteness_deficit(description or "", words)
        s3 = self._categorical_vagueness(kw_list)
        composite = (s1 + s2 + s3) / 3.0
        return float(np.clip(composite, 0, 100))

_SCORER = StrategicVaguenessScorer()

def strategic_vagueness_vectorized(desc: pd.Series, kws: pd.Series) -> pd.Series:
    return pd.Series([
        _SCORER.score(d, k) for d, k in zip(desc.fillna(""), kws.fillna(""))
    ], index=desc.index)

# =============================================================================
# 2) Architecture classification (Hardware vs Software)
# =============================================================================

def classify_architecture(keywords: str, description: str = "") -> int:
    """
    Returns is_hardware: 1 = Hardware/Integrated, 0 = Software/Modular
    """
    if not isinstance(keywords, str): keywords = ""
    if not isinstance(description, str): description = ""
    text = f"{keywords} {description}".lower()

    hw = any(w in text for w in [
        "hardware","robotics","robot","chip","asic","semiconductor","device",
        "fpga","silicon","sensor","biotech","quantum","lidar","camera","actuator"
    ])
    sw = any(w in text for w in [
        "software","saas","api","cloud","platform","mlops","sdk","microservice",
        "data platform","etl","wrapper","serverless"
    ])
    if hw and not sw: return 1
    if sw and not hw: return 0
    # tie-break: conservative (HW=1 only if strong)
    return 1 if hw and not sw else 0

def classify_architecture_vectorized(keywords: pd.Series, descriptions: pd.Series) -> pd.Series:
    return pd.Series([classify_architecture(k, d) for k, d in zip(keywords, descriptions)], index=keywords.index)

# =============================================================================
# 3) Funding & DV helpers
# =============================================================================

def derive_early_funding(first_financing_size: pd.Series) -> pd.Series:
    return pd.to_numeric(first_financing_size, errors='coerce') / 1e6

def create_survival_from_company_snapshots(
    baseline_df: pd.DataFrame, followup_df: pd.DataFrame,
    baseline_date: str="2021-12-01", followup_date: str="2023-05-01"
) -> pd.DataFrame:
    # Presence-based survival (simplified presence measure)
    bid = 'CompanyID' if 'CompanyID' in baseline_df.columns else 'company_id'
    fid = 'CompanyID' if 'CompanyID' in followup_df.columns else 'company_id'
    bset = set(baseline_df[bid].dropna().unique())
    fset = set(followup_df[fid].dropna().unique())
    df = pd.DataFrame({'company_id': list(bset)})
    df['survival'] = df['company_id'].apply(lambda x: 1 if x in fset else 0)
    return df

# NOTE: 아래 함수는 기존 리포지토리의 LLM2 방식(SeriesB+ 진행)을 보존합니다.
#       길지만 W1 재현을 위해 포함합니다. (축약 불가)
def create_survival_seriesb_progression(
    df_baseline: pd.DataFrame,
    df_mid1: pd.DataFrame,
    df_mid2: pd.DataFrame,
    df_endpoint: pd.DataFrame,
    baseline_date: str = "2021-12-01",
    mid1_date: str = "2022-01-01",
    mid2_date: str = "2022-05-01",
    endpoint_date: str = "2023-05-01"
) -> pd.DataFrame:
    # (원본 논리 유지; 편집: 변수명 일관화만 반영)
    import pandas as pd, numpy as np
    A_STAGE_PAT = r"(?:\bSeries\s*A(?:[-\s]?\d+|[A-Z])?\b|\bEarly[-\s]*Stage\s*VC\b)"
    B_PLUS_PAT = r"(?:\bLater[-\s]*Stage\s*VC\b|\bSeries\s*[B-G](?:[-\s]?\d+|[A-Z])?\b)"
    MA_PAT = r"(?:Merger|Acquisition|Buyout|LBO)"
    OOB_VAL = "Out of Business"
    id_col = 'CompanyID' if 'CompanyID' in df_baseline.columns else 'company_id'

    def _cap(df, snap_date, date_col="LastFinancingDate", type_col="LastFinancingDealType"):
        d = df.copy()
        snap_dt = pd.to_datetime(snap_date)
        d[date_col+"_asof"] = pd.to_datetime(d[date_col], errors='coerce').where(
            pd.to_datetime(d[date_col], errors='coerce') <= snap_dt
        )
        d[type_col+"_asof"] = d[type_col]
        d["asof_is_Bplus"] = d[type_col+"_asof"].fillna("").str.contains(B_PLUS_PAT, case=False, regex=True)
        d["asof_is_Astage"] = d[type_col+"_asof"].fillna("").str.contains(A_STAGE_PAT, case=False, regex=True)
        d["asof_is_MA"] = d[type_col+"_asof"].fillna("").str.contains(MA_PAT, case=False, regex=True)
        d["asof_is_OOB"] = (d["BusinessStatus"] == OOB_VAL) if "BusinessStatus" in d.columns else False
        return d

    t0  = _cap(df_baseline, baseline_date)
    tm1 = _cap(df_mid1, mid1_date)
    tm2 = _cap(df_mid2, mid2_date)
    t1  = _cap(df_endpoint, endpoint_date)

    # at-risk cohort: Series A, VC-backed, no prior B+
    vc = (t0["CompanyFinancingStatus"] == "Venture Capital-Backed") if "CompanyFinancingStatus" in t0.columns else True
    cohort_mask = vc & t0["asof_is_Astage"].fillna(False) & (~t0["asof_is_Bplus"].fillna(False))
    atrisk = t0.loc[cohort_mask, [id_col]].drop_duplicates(subset=[id_col])
    atrisk_ids = set(atrisk[id_col].unique())

    # event ordering
    snaps = [(0,"t0",t0),(1,"tm1",tm1),(2,"tm2",tm2),(3,"t1",t1)]
    all_e = []
    for idx, nm, d in snaps:
        e = d[[id_col,"asof_is_Bplus","asof_is_MA"]].copy()
        e = e[e[id_col].isin(atrisk_ids)]
        e["_snap_idx"] = idx
        all_e.append(e)
    events = pd.concat(all_e, ignore_index=True)
    def first_idx(flag):
        sub = events.loc[events[flag].fillna(False), [id_col, "_snap_idx"]]
        return sub.groupby(id_col)["_snap_idx"].min()
    fb = first_idx("asof_is_Bplus")
    fm = first_idx("asof_is_MA")
    oob = t1[[id_col, "asof_is_OOB"]].set_index(id_col)["asof_is_OOB"]

    res = pd.DataFrame({'company_id': list(atrisk_ids)})
    res["first_seen_B_idx"] = res["company_id"].map(fb)
    res["first_seen_MA_idx"] = res["company_id"].map(fm)
    res["oob_at_t1"] = res["company_id"].map(oob).fillna(False)

    b = res["first_seen_B_idx"]; m = res["first_seen_MA_idx"]
    cond_B = b.notna() & (b >= 1)
    cond_MA_preB = m.notna() & (b.isna() | (m < b))
    cond_Other = (~cond_B) & (~cond_MA_preB)

    res["Y_primary"] = np.nan
    res.loc[cond_B, "Y_primary"] = 1
    res.loc[cond_Other, "Y_primary"] = 0
    res["Y_MA_upper"] = res["Y_primary"].copy()
    res.loc[cond_MA_preB & (~cond_B), "Y_MA_upper"] = 1
    res["Y_MA_lower"] = res["Y_primary"].copy()
    res.loc[cond_MA_preB & (~cond_B), "Y_MA_lower"] = 0
    res["at_risk"] = True
    return res[["company_id","Y_primary","Y_MA_upper","Y_MA_lower","at_risk"]]

# =============================================================================
# 4) Sector FE and controls
# =============================================================================

def extract_sector_fe(keywords: pd.Series) -> pd.Series:
    def _map(s: str) -> str:
        s = str(s).lower() if isinstance(s, str) else ""
        if any(w in s for w in ['biotech','pharma','drug','health','medical','therapeutics']): return "Biotech/Healthcare"
        if any(w in s for w in ['hardware','robotics','robot','chip','semiconductor','sensor','device']): return "Hardware/Robotics"
        if any(w in s for w in ['ai','machine learning','ml','artificial intelligence','nlp','computer vision','deep learning']): return "AI/ML Software"
        if any(w in s for w in ['fintech','finance','payment','banking','crypto','blockchain']): return "FinTech"
        if any(w in s for w in ['data analytics','big data','data science','business intelligence']): return "Data/Analytics"
        if any(w in s for w in ['enterprise','b2b','saas','cloud']): return "Enterprise Software"
        if any(w in s for w in ['consumer','b2c','mobile app','gaming','social']): return "Consumer Software"
        return "Other"
    return keywords.fillna("").apply(_map)

def compute_log_employees(employees: pd.Series) -> pd.Series:
    return np.log1p(pd.to_numeric(employees, errors='coerce').fillna(0))

def compute_firm_age(year_founded: pd.Series, current_year: int = 2024) -> pd.Series:
    y = pd.to_numeric(year_founded, errors='coerce')
    return current_year - y

# Founder credibility (ID-based when available)
def compute_serial_entrepreneur(df: pd.DataFrame, contact_id_col: str = 'PrimaryContactPBId') -> pd.Series:
    if contact_id_col not in df.columns:
        return pd.Series(0, index=df.index)
    counts = df.groupby(contact_id_col).size()
    return df[contact_id_col].map(counts).fillna(0).ge(2).astype(int)

def compute_has_successful_exit(df: pd.DataFrame, contact_id_col: str='PrimaryContactPBId', status_col: str='BusinessStatus') -> pd.Series:
    if contact_id_col not in df.columns or status_col not in df.columns:
        return pd.Series(0, index=df.index)
    success = ['Acquired','IPO','Public']
    tmp = df.copy()
    tmp['_has_exit'] = tmp[status_col].isin(success).astype(int)
    founder_exit = tmp.groupby(contact_id_col)['_has_exit'].max()
    return df[contact_id_col].map(founder_exit).fillna(0).astype(int)

def compute_founder_credibility(df: pd.DataFrame) -> pd.Series:
    # Priority: prior exit → serial → fallback 0
    has_exit = compute_has_successful_exit(df)
    if has_exit.sum() > 0:
        return has_exit
    serial = compute_serial_entrepreneur(df)
    if serial.sum() > 0:
        return serial
    return pd.Series(0, index=df.index)

# =============================================================================
# 5) Full feature engineering & preprocessing for W1
# =============================================================================

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    colmap = {
        'Description':'description', 'Keywords':'keywords',
        'FirstFinancingSize':'first_financing_size',
        'LastFinancingDealType':'last_financing_deal_type',
        'Employees':'employees', 'YearFounded':'year_founded',
        'TotalRaised':'total_raised'
    }
    df.rename(columns=colmap, inplace=True, errors='ignore')

    # Vagueness
    if 'description' in df.columns:
        if 'keywords' not in df.columns: df['keywords'] = ""
        df['vagueness'] = strategic_vagueness_vectorized(df['description'], df['keywords'])

    # Architecture
    if 'keywords' in df.columns:
        desc = df['description'] if 'description' in df.columns else pd.Series([""]*len(df))
        df['is_hardware'] = classify_architecture_vectorized(df['keywords'], desc)
        # Back-compat alias
        df['high_integration_cost'] = df['is_hardware']

    # Early funding
    if 'first_financing_size' in df.columns:
        df['early_funding_musd'] = derive_early_funding(df['first_financing_size'])

    # Controls
    if 'employees' in df.columns: df['employees_log'] = compute_log_employees(df['employees'])
    if 'year_founded' in df.columns: df['firm_age'] = compute_firm_age(df['year_founded'])

    # Sector FE (optional)
    if 'keywords' in df.columns:
        df['sector_fe'] = extract_sector_fe(df['keywords'])
    else:
        df['sector_fe'] = "Other"

    return df

def create_founding_cohort(df: pd.DataFrame, year_col: str='year_founded') -> pd.Series:
    if year_col not in df.columns:
        return pd.Series(np.nan, index=df.index)
    bins = [0,2009,2014,2018,2020,2021,9999]
    labels = ['≤2009','2010-14','2015-18','2019-20','2021','2022+']
    cohort = pd.cut(pd.to_numeric(df[year_col], errors='coerce'), bins=bins, labels=labels, right=True)
    return cohort.cat.remove_unused_categories()

def preprocess_for_w1(df: pd.DataFrame) -> pd.DataFrame:
    """Create z-variables, cohorts, ic_within; make growth/survival aliases."""
    d = df.copy()

    # Architecture aliases
    if 'is_hardware' not in d.columns and 'high_integration_cost' in d.columns:
        d['is_hardware'] = d['high_integration_cost']
    if 'high_integration_cost' not in d.columns and 'is_hardware' in d.columns:
        d['high_integration_cost'] = d['is_hardware']  # back-compat

    # Cohort
    d['founding_cohort'] = create_founding_cohort(d)

    # z-scores
    if 'vagueness' in d.columns: d['z_vagueness'] = _z(d['vagueness'])
    if 'employees_log' in d.columns: d['z_employees_log'] = _z(d['employees_log'])
    if 'founder_credibility' in d.columns and d['founder_credibility'].std(ddof=0) > 0:
        d['z_founder_credibility'] = _z(d['founder_credibility'])

    # within-sector centered IC (for FE robustness)
    if 'is_hardware' in d.columns and 'sector_fe' in d.columns:
        d['ic_within'] = d['is_hardware'] - d.groupby('sector_fe')['is_hardware'].transform('mean')

    # DV aliases (growth = main)
    if 'Y_primary' in d.columns and 'growth' not in d.columns:
        d['growth'] = d['Y_primary']
    if 'growth' in d.columns and 'survival' not in d.columns:
        d['survival'] = d['growth']

    return d

# Back-compat alias used by run_analysis in 기존 코드
preprocess_for_h2 = preprocess_for_w1
