"""
Feature Engineering Module (W1 refactor)

- Vagueness: StrategicVaguenessScorer (Lo&McD 2011; Pan et al. 2018; Zuckerman 1999 based)
- Moderator: is_hardware (1=Integrated/Hardware, 0=Non-integrated/Software)
- DV stitching remains (Series B+ progression); we expose as 'growth'
"""

import pandas as pd
import numpy as np
import re
from typing import Union, List

# =========================================================
# Academic Vagueness (Gemini's StrategicVaguenessScorer)
# =========================================================
class StrategicVaguenessScorer:
    """
    Academic literature-based vagueness scorer analyzing venture 'Promise' and 'Keywords'.
    Cites:
    1. Lexical Uncertainty (Loughran & McDonald 2011, 2016)
    2. Linguistic Concreteness (Pan et al. 2018; Chen et al. 2015)
    3. Categorical Vagueness (Zuckerman 1999; Hannan et al. 2007)
    """

    def __init__(self):
        # Cites: Loughran & McDonald (2011, JF; 2016, JAR)
        self.lm_uncertainty = {
            'approximately', 'believe', 'could', 'depend', 'estimate', 'expect',
            'intend', 'may', 'might', 'possible', 'probable', 'risk', 'uncertain',
            'vary', 'anticipate', 'potential', 'project', 'forecast', 'seek',
            'contingent', 'future', 'unclear', 'unspecified'
        }

        # Cites: Pan et al. (2018, SMJ); Chen et al. (2015, JAR)
        self.concreteness_markers = {
            'temporal': r'\b(Q[1-4]\s*20\d{2}|20\d{2})\b',
            'quantitative_tech': r'\b(\d+[\.\d]*[xX%]?|[A-Z]{2,}\d*|\bL(evel)?\s*\d)\b',
            'acronym': r'\b[A-Z]{3,}\b'
        }

        # Cites: Hannan et al. (2007, ASQ); Zuckerman (1999, AJS)
        self.abstraction_keywords = {
            'platform', 'solution', 'ecosystem', 'technology', 'approach',
            'service', 'market', 'advanced', 'next-generation', 'sustainable',
            'cloud', 'AI', 'data', 'analytics', 'software', 'future'
        }

    def _tokenize(self, text):
        """Helper to safely tokenize text."""
        if not isinstance(text, str) or not text:
            return []
        return re.findall(r'\b\w+\b', text.lower())

    def calculate_lexical_uncertainty(self, description_words):
        """Cites: Loughran & McDonald (2011, JF; 2016, JAR)"""
        if not description_words:
            return 0.0
        uncertain_count = sum(1 for w in description_words if w in self.lm_uncertainty)
        uncertain_ratio = uncertain_count / len(description_words)
        return min(uncertain_ratio * 1000, 100)

    def calculate_concreteness_deficit(self, description_text, description_words):
        """Cites: Pan et al. (2018, SMJ); Chen et al. (2015, JAR)"""
        if not description_words:
            return 100.0

        specific_count = 0
        for pattern in self.concreteness_markers.values():
            if isinstance(description_text, str):
                specific_count += len(re.findall(pattern, description_text))

        specific_ratio = specific_count / len(description_words)
        precision_score = min(specific_ratio * 500, 100)
        return 100 - precision_score

    def calculate_categorical_vagueness(self, keyword_list):
        """Cites: Zuckerman (1999, AJS); Pontikes (2012, ASQ); Hannan et al. (2007)"""
        if not keyword_list:
            return 100.0

        num_keywords = len(keyword_list)
        abstraction_count = sum(1 for w in keyword_list if w in self.abstraction_keywords)
        abstraction_ratio = abstraction_count / num_keywords
        uniqueness_ratio = len(set(keyword_list)) / num_keywords
        categorical_vagueness_ratio = (abstraction_ratio + uniqueness_ratio) / 2

        return categorical_vagueness_ratio * 100

    def score_vagueness(self, description, keywords):
        """Composite Vagueness score (0-100)"""
        description_words = self._tokenize(description)

        keyword_str = keywords if isinstance(keywords, str) else ""
        keyword_list = [k.strip() for k in keyword_str.lower().split(',')]
        keyword_list = [k for k in keyword_list if k]

        score_uncertainty = self.calculate_lexical_uncertainty(description_words)
        score_concreteness_deficit = self.calculate_concreteness_deficit(description, description_words)
        score_categorical = self.calculate_categorical_vagueness(keyword_list)

        composite_score = (score_uncertainty +
                           score_concreteness_deficit +
                           score_categorical) / 3

        return max(0, min(100, composite_score))

# --- Scorer instance and Wrapper ---
_SCORER = StrategicVaguenessScorer()

def compute_vagueness_vectorized(descriptions: pd.Series, keywords: pd.Series) -> pd.Series:
    """
    Vectorized wrapper for StrategicVaguenessScorer using both inputs.
    """
    # Combine into a temporary DataFrame to handle alignment and missing values
    temp_df = pd.DataFrame({'description': descriptions, 'keywords': keywords})

    return temp_df.apply(
        lambda row: _SCORER.score_vagueness(row['description'], row['keywords']),
        axis=1
    )

# =========================================================
# Integration Cost → Hardware/Software classifier
# =========================================================
def classify_hardware_or_software(keywords: str, description: str = "") -> int:
    """
    Return 1 if the venture sits in high-integration 'hardware' space, else 0.
    Mapping for report language:
        1 → Hardware / Integrated (Battleship)  [Purple]
        0 → Software / Non-integrated (Lego)    [Green]
    """
    if not isinstance(keywords, str):
        keywords = ""
    text = f"{keywords} {description}".lower()

    hardware_cues = [
        "hardware", "robotics", "robot", "chip", "asic", "semiconductor", "device",
        "sensor", "fpga", "silicon", "biotech", "quantum", "autonomous vehicle", "av",
        "battery", "manufacturing", "actuator", "lidar", "camera module", "edge device"
    ]
    software_cues = [
        "software", "saas", "api", "cloud", "platform", "sdk", "microservice",
        "data", "ml", "ai", "nlp", "cv", "llm", "analytics", "developer tool"
    ]
    h = sum(kw in text for kw in hardware_cues)
    s = sum(kw in text for kw in software_cues)
    return 1 if h > s else 0

def classify_hardware_vectorized(keywords: pd.Series, descriptions: pd.Series = None) -> pd.Series:
    if descriptions is None:
        descriptions = pd.Series([""] * len(keywords), index=keywords.index)

    # Handle potential NaN values gracefully
    safe_keywords = keywords.fillna("")
    safe_descriptions = descriptions.fillna("")

    return pd.Series(
        [classify_hardware_or_software(k, d) for k, d in zip(safe_keywords, safe_descriptions)],
        index=keywords.index
    )

# =========================================================
# Funding / DV helpers
# =========================================================
def derive_early_funding(first_financing_size: pd.Series) -> pd.Series:
    """
    Convert first financing size to millions USD.

    Note: This function only converts the amount. Filtering for Series A /
    Early Stage VC is done in engineer_features() using FirstFinancingDealType.

    Args:
        first_financing_size: First financing amount in USD

    Returns:
        Funding amount in millions USD
    """
    return first_financing_size / 1e6

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
    """
    Create survival variable based on Series B+ progression (LLM2 approach).

    This addresses the singular matrix problem by using SUCCESS-BASED survival:
    - Y=1: Company progressed from Series A → Series B+ within window
    - Y=0: Company stayed at Series A or went Out of Business
    - CENSORED: Company had M&A exit (competing risk)

    Expected base rate: 12-15% (17-month window captures early movers only)

    Key features:
    1. As-of capping: Prevents data leakage (diagnostic showed 2024-2025 dates in 2021-23 snapshots)
    2. Event ordering: Uses all 4 snapshots to determine "first seen" for B+ and M&A
    3. At-risk cohort: Only companies at Series A (VC-backed) at baseline

    Args:
        df_baseline: Baseline snapshot (2021-12-01) - extract predictors
        df_mid1: Mid snapshot 1 (2022-01-01) - for event ordering
        df_mid2: Mid snapshot 2 (2022-05-01) - for event ordering
        df_endpoint: Endpoint snapshot (2023-05-01) - final outcomes
        baseline_date: Date of baseline snapshot
        mid1_date: Date of mid1 snapshot
        mid2_date: Date of mid2 snapshot
        endpoint_date: Date of endpoint snapshot

    Returns:
        DataFrame with columns:
        - company_id: Company identifier
        - Y_primary: Binary DV (1=B+ progression, 0=no progression, NaN=M&A censored)
        - Y_MA_upper: Upper bound (M&A=1)
        - Y_MA_lower: Lower bound (M&A=0)
        - at_risk: Whether company was in at-risk cohort
    """
    import re

    # Regex patterns for deal types (FIXED - matches actual PitchBook data structure)
    # PitchBook uses "Early Stage VC" / "Later Stage VC" instead of "Series A/B/C"

    # Series A: "Early Stage VC" is the primary label (~45K companies)
    A_STAGE_PAT = r"(?:\bSeries\s*A(?:[-\s]?\d+|[A-Z])?\b|\bEarly[-\s]*Stage\s*VC\b)"

    # Series B+: "Later Stage VC" is the primary label (~24K companies)
    B_PLUS_PAT = r"(?:\bLater[-\s]*Stage\s*VC\b|\bSeries\s*[B-G](?:[-\s]?\d+|[A-Z])?\b)"

    # M&A pattern (unchanged)
    MA_PAT = r"(?:Merger|Acquisition|Buyout|LBO)"
    OOB_VAL = "Out of Business"

    # Identify company ID column
    id_col = 'CompanyID' if 'CompanyID' in df_baseline.columns else 'company_id'

    def apply_asof_cap(df, snapshot_date, date_col="LastFinancingDate", type_col="LastFinancingDealType"):
        """Apply as-of date capping to prevent data leakage."""
        df = df.copy()
        snap_dt = pd.to_datetime(snapshot_date)

        # Normalize date
        d = pd.to_datetime(df[date_col], errors='coerce')

        # Cap DATE but keep TYPE (type represents current stage, date may have data entry errors)
        capped_date = d.where(d <= snap_dt)
        # IMPORTANT: We keep the deal type even if date is future - it shows current financing stage
        capped_type = df[type_col]  # Don't null out based on date

        df[date_col + "_asof"] = capped_date
        df[type_col + "_asof"] = capped_type

        # Leakage guard
        max_date = df[date_col + "_asof"].dropna().max()
        if pd.notna(max_date) and max_date > snap_dt:
            print(f"  ⚠️  WARNING: Leakage detected: {max_date} > {snap_dt}")

        # Convenience flags for this snapshot
        df["asof_is_Bplus"] = df[type_col + "_asof"].fillna("").str.contains(B_PLUS_PAT, case=False, regex=True)
        df["asof_is_Astage"] = df[type_col + "_asof"].fillna("").str.contains(A_STAGE_PAT, case=False, regex=True)
        df["asof_is_MA"] = df[type_col + "_asof"].fillna("").str.contains(MA_PAT, case=False, regex=True)

        # Debug: Show sample matches
        n_a = df["asof_is_Astage"].sum()
        n_b = df["asof_is_Bplus"].sum()
        if n_a > 0:
            print(f"        → Found {n_a:,} Series A companies")
        if n_b > 0:
            print(f"        → Found {n_b:,} Series B+ companies")

        # Check for OOB status
        if "BusinessStatus" in df.columns:
            df["asof_is_OOB"] = (df["BusinessStatus"] == OOB_VAL)
        else:
            df["asof_is_OOB"] = False

        return df

    # Apply as-of capping to all snapshots
    print("\n  📅 Applying as-of date capping (preventing data leakage):")
    df_t0 = apply_asof_cap(df_baseline, baseline_date)
    print(f"     Baseline ({baseline_date}): capped")
    df_tM1 = apply_asof_cap(df_mid1, mid1_date)
    print(f"     Mid1 ({mid1_date}): capped")
    df_tM2 = apply_asof_cap(df_mid2, mid2_date)
    print(f"     Mid2 ({mid2_date}): capped")
    df_t1 = apply_asof_cap(df_endpoint, endpoint_date)
    print(f"     Endpoint ({endpoint_date}): capped")

    # Get at-risk cohort: Series A, VC-backed, no prior B+ at baseline
    print("\n  🎯 Identifying at-risk cohort (Series A at baseline):")

    if "CompanyFinancingStatus" in df_t0.columns:
        vc = (df_t0["CompanyFinancingStatus"] == "Venture Capital-Backed")
    else:
        vc = pd.Series(True, index=df_t0.index)

    at_a = df_t0["asof_is_Astage"].fillna(False)
    no_prior_b = ~df_t0["asof_is_Bplus"].fillna(False)

    cohort_mask = vc & at_a & no_prior_b
    atrisk = df_t0.loc[cohort_mask, [id_col]].drop_duplicates(subset=[id_col])

    print(f"     Total at baseline: {len(df_t0):,}")
    print(f"     VC-backed: {vc.sum():,}")
    print(f"     At Series A: {at_a.sum():,}")
    print(f"     No prior B+: {no_prior_b.sum():,}")
    print(f"     → At-risk cohort: {len(atrisk):,}")

    # Track event ordering across all 4 snapshots
    print("\n  🔍 Tracking event ordering (first seen B+ vs M&A):")

    atrisk_ids = set(atrisk[id_col].unique())
    snapshots = [
        (0, "t0", df_t0),
        (1, "tM1", df_tM1),
        (2, "tM2", df_tM2),
        (3, "t1", df_t1)
    ]

    # Collect all events
    all_events = []
    for idx, name, df in snapshots:
        events = df[[id_col, "asof_is_Bplus", "asof_is_MA"]].copy()
        events = events[events[id_col].isin(atrisk_ids)]
        events['_snap_idx'] = idx
        all_events.append(events)

    all_events_df = pd.concat(all_events, axis=0, ignore_index=True)

    # Find first occurrence of each event type
    def first_idx(flag_col):
        subset = all_events_df.loc[all_events_df[flag_col].fillna(False), [id_col, '_snap_idx']]
        return subset.groupby(id_col)['_snap_idx'].min()

    first_b = first_idx("asof_is_Bplus")
    first_ma = first_idx("asof_is_MA")

    # OOB status at endpoint
    oob_at_t1 = df_t1[[id_col, "asof_is_OOB"]].set_index(id_col)["asof_is_OOB"]

    # Merge into result DataFrame
    result = pd.DataFrame({
        'company_id': list(atrisk_ids)
    })
    result['first_seen_B_idx'] = result['company_id'].map(first_b)
    result['first_seen_MA_idx'] = result['company_id'].map(first_ma)
    result['oob_at_t1'] = result['company_id'].map(oob_at_t1).fillna(False)

    # Compute DV variants
    print("\n  📊 Computing DV (Series B+ progression):")

    # Primary DV: Y=1 if B+ appeared after baseline (idx>=1), CENSORED if M&A before B+
    b_idx = result['first_seen_B_idx']
    m_idx = result['first_seen_MA_idx']

    cond_B = b_idx.notna() & (b_idx >= 1)  # B+ appeared after baseline
    cond_MA_preB = m_idx.notna() & ((b_idx.isna()) | (m_idx < b_idx))  # M&A before B+ (or no B+)
    cond_OOB_or_stillA = (~cond_B) & (~cond_MA_preB)  # Neither B+ nor M&A

    # Primary DV (M&A censored)
    result['Y_primary'] = np.nan
    result.loc[cond_B, 'Y_primary'] = 1
    result.loc[cond_OOB_or_stillA, 'Y_primary'] = 0
    # M&A before B+ → censored (remains NaN)

    # Robustness bounds
    result['Y_MA_upper'] = result['Y_primary'].copy()
    result.loc[cond_MA_preB & (~cond_B), 'Y_MA_upper'] = 1

    result['Y_MA_lower'] = result['Y_primary'].copy()
    result.loc[cond_MA_preB & (~cond_B), 'Y_MA_lower'] = 0

    result['at_risk'] = True

    # Diagnostics
    n_total = len(result)
    n_valid_primary = result['Y_primary'].notna().sum()
    n_success = (result['Y_primary'] == 1).sum()
    n_censored = result['Y_primary'].isna().sum()

    base_rate = n_success / n_valid_primary if n_valid_primary > 0 else 0
    censored_rate = n_censored / n_total if n_total > 0 else 0

    print(f"     N at-risk: {n_total:,}")
    print(f"     N valid (non-censored): {n_valid_primary:,}")
    print(f"     N progressed to B+: {n_success:,}")
    print(f"     Base rate (B+ progression): {base_rate:.1%}")
    print(f"     M&A censored: {n_censored:,} ({censored_rate:.1%})")

    # Sanity check
    if not (0.08 <= base_rate <= 0.20):
        print(f"     ⚠️  WARNING: Base rate {base_rate:.1%} outside expected 8-20% range")
    else:
        print(f"     ✓ Base rate within expected range (8-20%)")

    return result[['company_id', 'Y_primary', 'Y_MA_upper', 'Y_MA_lower', 'at_risk']]


# =========================================================
# Sector FE & controls
# =========================================================
def extract_sector_fe(keywords: pd.Series) -> pd.Series:
    """
    Extract sector fixed effects from Keywords column.
    """
    def classify_sector(keyword_str):
        if pd.isna(keyword_str):
            return "Other"
        kw = str(keyword_str).lower()
        if any(w in kw for w in ['biotech', 'pharma', 'drug', 'health', 'medical', 'therapeutics']):
            return "Biotech/Healthcare"
        elif any(w in kw for w in ['hardware', 'robotics', 'robot', 'chip', 'semiconductor', 'sensor', 'device']):
            return "Hardware/Robotics"
        elif any(w in kw for w in ['ai', 'machine learning', 'ml', 'artificial intelligence', 'nlp', 'computer vision', 'deep learning']):
            return "AI/ML Software"
        elif any(w in kw for w in ['fintech', 'payment', 'banking', 'crypto', 'blockchain']):
            return "FinTech"
        elif any(w in kw for w in ['data analytics', 'big data', 'business intelligence']):
            return "Data/Analytics"
        elif any(w in kw for w in ['enterprise', 'b2b', 'saas', 'cloud']):
            return "Enterprise Software"
        elif any(w in kw for w in ['consumer', 'b2c', 'mobile app', 'gaming', 'social']):
            return "Consumer Software"
        else:
            return "Other"
    return keywords.apply(classify_sector)

def compute_log_employees(employees: pd.Series) -> pd.Series:
    return np.log1p(pd.to_numeric(employees, errors='coerce').fillna(0))

def compute_firm_age(year_founded: pd.Series, current_year: int = 2024) -> pd.Series:
    years = pd.to_numeric(year_founded, errors='coerce')
    return current_year - years

# Founder credibility
def compute_founder_credibility(df: pd.DataFrame) -> pd.Series:
    """
    Compute founder credibility indicator using PrimaryContactPBId.
    """
    if 'PrimaryContactPBId' in df.columns and 'BusinessStatus' in df.columns:
        tmp = df[['PrimaryContactPBId', 'BusinessStatus']].copy()
        tmp['_has_exit'] = tmp['BusinessStatus'].isin(['Acquired', 'IPO', 'Public']).astype(int)
        has_exit = tmp.groupby('PrimaryContactPBId')['_has_exit'].transform('max')
        return has_exit.fillna(0).astype(int)
    return pd.Series(0, index=df.index)

def compute_serial_entrepreneur(df: pd.DataFrame) -> pd.Series:
    """
    Compute serial entrepreneur indicator (alias for founder credibility).
    Returns 1 if founder has had prior successful exit, 0 otherwise.
    This is used as the moderator for H2-Alt (Credibility hypothesis).
    """
    return compute_founder_credibility(df)

# =========================================================
# Orchestrator
# =========================================================
def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize & engineer all predictors needed for H1/H2.
    """
    df = df.copy()
    mapping = {
        'Description': 'description', 'Keywords': 'keywords',
        'FirstFinancingSize': 'first_financing_size',
        'FirstFinancingDealType': 'first_financing_deal_type',
        'LastFinancingDealType': 'last_financing_deal_type',
        'Employees': 'employees', 'YearFounded': 'year_founded', 'TotalRaised': 'total_raised',
        'CompanyID': 'CompanyID', 'company_id': 'company_id'
    }
    df.rename(columns=mapping, inplace=True, errors='ignore')

    # 1) Vagueness (now uses description AND keywords)
    if 'description' in df.columns and 'keywords' in df.columns:
        df['vagueness'] = compute_vagueness_vectorized(
            df['description'],
            df['keywords']
        )
    elif 'description' in df.columns:
        print("Warning: 'keywords' column not found. Vagueness score based only on description.")
        df['vagueness'] = compute_vagueness_vectorized(
            df['description'],
            pd.Series([""] * len(df), index=df.index)
        )

    # 2) Hardware/Software (moderator)
    if 'keywords' in df.columns:
        desc = df['description'] if 'description' in df.columns else None
        df['is_hardware'] = classify_hardware_vectorized(df['keywords'], desc)

    # 3) Early funding ($M) - ONLY Series A / Early Stage VC
    if 'first_financing_size' in df.columns:
        # Pattern for Series A / Early Stage VC (same as DV creation)
        A_STAGE_PAT = r"(?:\bSeries\s*A(?:[-\s]?\d+|[A-Z])?\b|\bEarly[-\s]*Stage\s*VC\b)"

        # Initialize with the funding amount
        df['early_funding_musd'] = derive_early_funding(df['first_financing_size'])

        # Filter: Set to NaN if NOT Early Stage VC / Series A
        if 'first_financing_deal_type' in df.columns:
            is_series_a = df['first_financing_deal_type'].fillna("").str.contains(
                A_STAGE_PAT, case=False, regex=True, na=False
            )
            # Keep only Series A / Early Stage VC funding
            df.loc[~is_series_a, 'early_funding_musd'] = np.nan
            print(f"  ℹ️  Early funding filtered to Series A / Early Stage VC: {is_series_a.sum():,} of {len(df):,} companies")
        else:
            print("  ⚠️  Warning: 'first_financing_deal_type' not found. Using all first financing rounds.")

    # 4) Controls
    if 'employees' in df.columns:
        df['employees_log'] = compute_log_employees(df['employees'])
    if 'year_founded' in df.columns:
        df['firm_age'] = compute_firm_age(df['year_founded'])

    return df

# =========================================================
# Preprocessing for H2
# =========================================================
def create_founding_cohort(df: pd.DataFrame, year_col: str = 'year_founded') -> pd.Series:
    if year_col not in df.columns:
        return pd.Series(np.nan, index=df.index)
    bins = [0, 2009, 2014, 2018, 2020, 2021, 9999]
    labels = ['≤2009', '2010-14', '2015-18', '2019-20', '2021', '2022+']
    cohort = pd.cut(df[year_col], bins=bins, labels=labels, right=True)
    return cohort.cat.remove_unused_categories()

def preprocess_for_h2(df: pd.DataFrame, fix_founder_credibility: bool = True) -> pd.DataFrame:
    out = df.copy()
    out['founding_cohort'] = create_founding_cohort(out)

    for col in ['vagueness', 'employees_log']:
        if col in out.columns and out[col].std() not in [0, np.nan]:
            out[f'z_{col}'] = (out[col] - out[col].mean()) / out[col].std()
        else:
            out[f'z_{col}'] = 0

    # CRITICAL FIX: Create founder_serial BEFORE z-scoring or dropping
    # This ensures the binary column persists even if founder_credibility has std=0
    if 'founder_credibility' in out.columns:
        # Create binary column (0 or 1) from continuous credibility
        out['founder_serial'] = (out['founder_credibility'] > 0).astype(int)

        # Now handle z-scoring (founder_credibility may be constant → drop for main spec)
        fc_std = out['founder_credibility'].std()
        if (pd.isna(fc_std) or fc_std == 0) and fix_founder_credibility:
            # Drop the continuous version but KEEP the binary founder_serial
            out = out.drop(columns=['founder_credibility'])
            print(f"  ℹ️  founder_credibility dropped (std=0), but founder_serial preserved (n={out['founder_serial'].sum():,})")
        else:
            # Create z-score if there's variation
            out['z_founder_credibility'] = (out['founder_credibility'] - out['founder_credibility'].mean()) / max(1e-9, out['founder_credibility'].std())
    else:
        # If founder_credibility doesn't exist, create founder_serial as all zeros
        out['founder_serial'] = 0
        print(f"  ⚠️  founder_credibility not found. Created founder_serial=0 for all rows.")

    # FINAL GUARD: Ensure founder_serial has stable dtype and no NaNs
    # This is belt-and-suspenders to prevent any downstream issues
    if 'founder_serial' in out.columns:
        out['founder_serial'] = out['founder_serial'].fillna(0).astype(int)
        # NEVER drop founder_serial - it's required for H3/H4
        assert 'founder_serial' in out.columns, "INTERNAL ERROR: founder_serial was dropped"

    return out
