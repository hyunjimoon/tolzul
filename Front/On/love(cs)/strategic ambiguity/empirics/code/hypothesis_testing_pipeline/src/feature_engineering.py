"""
Feature Engineering Module for Hypothesis Testing Pipeline

This module provides functions for computing vagueness, integration cost,
and other derived features from company and deal data.
"""

import pandas as pd
import numpy as np
import re
from typing import Union, List


# =============================================================================
# VAGUENESS COMPUTATION
# =============================================================================

def compute_vagueness(text: str) -> float:
    """
    Compute textual vagueness using LIWC-style keyword approach.

    Measures the frequency of hedge words vs precise words.
    Higher scores indicate more vague language.

    Args:
        text: Description or text to analyze

    Returns:
        Vagueness score (0-100 scale), or np.nan if text is invalid
        Formula: 50 + 10 * (vague_count - precise_count), capped at [0, 100]

    Examples:
        >>> compute_vagueness("We maybe provide approximately scalable solutions")
        70  # 2 vague words, 0 precise words
        >>> compute_vagueness("We provide precise guaranteed machine learning APIs")
        30  # 0 vague words, 2 precise words
    """
    if not isinstance(text, str) or pd.isna(text):
        return np.nan

    # Vague/hedge words indicating uncertainty
    vague_words = [
        "maybe", "approximately", "somewhat", "likely", "possibly",
        "potential", "around", "roughly", "flexible", "scalable",
        "adaptive", "designed to", "enables", "allows", "offering",
        "providing", "can be", "may be", "could be", "about", "nearly"
    ]

    # Precise words indicating certainty
    precise_words = [
        "exactly", "precisely", "guaranteed", "specific", "certified",
        "proprietary", "patented", "proven", "definite", "concrete",
        "measurable", "quantifiable"
    ]

    # Tokenize and count
    text_lower = text.lower()

    if len(text_lower) == 0:
        return np.nan

    # Count word occurrences
    vague_count = sum(text_lower.count(word) for word in vague_words)
    precise_count = sum(text_lower.count(word) for word in precise_words)

    # Formula from Family 1: 50 + 10*(vague - precise), capped at [0, 100]
    score = 50 + 10 * (vague_count - precise_count)
    return max(0, min(100, score))


def compute_vagueness_vectorized(descriptions: pd.Series) -> pd.Series:
    """
    Vectorized version of vagueness computation for pandas Series.

    Args:
        descriptions: Series of text descriptions

    Returns:
        Series of vagueness scores (0-100 scale)
    """
    return descriptions.apply(compute_vagueness)


# =============================================================================
# INTEGRATION COST CLASSIFICATION
# =============================================================================

def classify_integration_cost(keywords: str, description: str = "") -> int:
    """
    Classify sector integration cost based on keywords and description.

    High integration cost (1): hardware, robotics, chips, biotech, devices
    Low integration cost (0): software, APIs, SaaS, cloud platforms

    Args:
        keywords: Sector/industry keywords
        description: Optional company description

    Returns:
        1 for high integration cost, 0 for low integration cost

    Examples:
        >>> classify_integration_cost("robotics, hardware, chip design")
        1
        >>> classify_integration_cost("SaaS, API, cloud software")
        0
    """
    # Keywords indicating high integration cost
    high_integrated = [
        "hardware", "robotics", "robot", "chip", "asic", "semiconductor",
        "biotech", "device", "quantum", "fpga", "silicon", "sensor",
        "distributed systems", "gpu clusters"
    ]

    # Keywords indicating low integration cost (modular)
    low_integrated = [
        "software", "saas", "api", "cloud", "platform", "web",
        "application", "service", "interface", "wrapper", "sdk"
    ]

    # Combine text sources
    text = f"{keywords} {description}".lower() if isinstance(keywords, str) else ""

    if not text:
        return 0  # Default to low integration cost if no info

    # Count matches
    high_count = sum(1 for keyword in high_integrated if keyword in text)
    low_count = sum(1 for keyword in low_integrated if keyword in text)

    # Classify based on dominant signal
    if high_count > low_count:
        return 1
    else:
        return 0


def classify_integration_cost_vectorized(
    keywords: pd.Series,
    descriptions: pd.Series = None
) -> pd.Series:
    """
    Vectorized classification of integration cost for pandas DataFrames.

    Args:
        keywords: Series of keyword strings
        descriptions: Optional series of descriptions

    Returns:
        Series of integration cost classifications (0 or 1)
    """
    if descriptions is None:
        descriptions = pd.Series([""] * len(keywords))

    return pd.Series([
        classify_integration_cost(k, d)
        for k, d in zip(keywords, descriptions)
    ])


# =============================================================================
# FUNDING VARIABLES
# =============================================================================

def derive_early_funding(first_financing_size: pd.Series) -> pd.Series:
    """
    Derive early funding amount in millions USD.

    Args:
        first_financing_size: Series of first financing amounts (in USD)

    Returns:
        Series of early funding amounts in millions USD
    """
    return first_financing_size / 1e6


def derive_later_success(last_deal_type: pd.Series, threshold: str = "Series B") -> pd.Series:
    """
    Derive binary later success indicator.

    Success is defined as reaching Series B or later funding rounds.

    Args:
        last_deal_type: Series of last deal type strings
        threshold: Funding round threshold for success (default: "Series B")

    Returns:
        Binary series (1 = success, 0 = no success)
    """
    # Series progression: Seed -> Series A -> Series B -> Series C -> ...
    success_rounds = [
        "Series B", "Series C", "Series D", "Series E",
        "Series F", "Series G", "Late Stage", "IPO", "Acquisition"
    ]

    def is_success(deal_type):
        if pd.isna(deal_type):
            return 0
        deal_str = str(deal_type)
        return int(any(round_type in deal_str for round_type in success_rounds))

    return last_deal_type.apply(is_success)


# =============================================================================
# SURVIVAL VARIABLE (3-SNAPSHOT LOGIC)
# =============================================================================

def create_survival_from_snapshots(
    snapshot_20230501: pd.DataFrame,
    deal_data: pd.DataFrame,
    cutoff_date: str = "2021-11-01"
) -> pd.DataFrame:
    """
    Create survival variable from 3-snapshot data.

    Survival definition:
        survival = 1 if (company in 20230501 snapshot) AND
                       (LastFinancingDate >= cutoff_date)
        survival = 0 otherwise

    This captures companies that:
    1. Still exist as of May 2023
    2. Received funding within 18 months before snapshot (2021-11-01 onwards)

    Args:
        snapshot_20230501: DataFrame with companies in May 2023 snapshot
        deal_data: DataFrame with all deal data including LastFinancingDate
        cutoff_date: Date threshold for recent funding (default: 2021-11-01)

    Returns:
        DataFrame with company_id and survival binary indicator

    Examples:
        >>> snapshot = pd.DataFrame({'company_id': [1, 2, 3]})
        >>> deals = pd.DataFrame({
        ...     'company_id': [1, 2, 3],
        ...     'LastFinancingDate': ['2022-05-01', '2020-01-01', '2023-01-01']
        ... })
        >>> result = create_survival_from_snapshots(snapshot, deals)
        >>> result['survival'].tolist()
        [1, 0, 1]  # Company 2 funded too early
    """
    # Ensure company_id column exists
    if 'company_id' not in snapshot_20230501.columns:
        if 'CompanyID' in snapshot_20230501.columns:
            snapshot_20230501 = snapshot_20230501.rename(columns={'CompanyID': 'company_id'})
        else:
            raise ValueError("snapshot_20230501 must have 'company_id' or 'CompanyID' column")

    if 'company_id' not in deal_data.columns:
        if 'CompanyID' in deal_data.columns:
            deal_data = deal_data.rename(columns={'CompanyID': 'company_id'})
        else:
            raise ValueError("deal_data must have 'company_id' or 'CompanyID' column")

    # Get companies in May 2023 snapshot
    companies_in_snapshot = set(snapshot_20230501['company_id'].unique())

    # Get latest financing date for each company
    last_financing = deal_data.groupby('company_id').agg({
        'LastFinancingDate': 'max'
    }).reset_index()

    # Convert date column to datetime
    last_financing['LastFinancingDate'] = pd.to_datetime(
        last_financing['LastFinancingDate'],
        errors='coerce'
    )
    cutoff_datetime = pd.to_datetime(cutoff_date)

    # Create survival indicator
    def compute_survival(row):
        company_id = row['company_id']
        last_date = row['LastFinancingDate']

        # Check both conditions
        in_snapshot = company_id in companies_in_snapshot
        recent_funding = pd.notna(last_date) and last_date >= cutoff_datetime

        return 1 if (in_snapshot and recent_funding) else 0

    last_financing['survival'] = last_financing.apply(compute_survival, axis=1)

    return last_financing[['company_id', 'survival']]


def create_survival_from_company_snapshots(
    baseline_df: pd.DataFrame,
    followup_df: pd.DataFrame,
    baseline_date: str = "2022-01-01",
    followup_date: str = "2023-05-01"
) -> pd.DataFrame:
    """
    Create survival variable from two Company snapshots (NO Deal data needed).

    Survival definition:
        survival = 1 if company appears in BOTH baseline and follow-up snapshots
        survival = 0 if company only in baseline (disappeared by follow-up)

    This is a simpler presence-based survival measure that tracks whether
    companies persist across time periods.

    Args:
        baseline_df: DataFrame from baseline snapshot (e.g., 2022-01-01)
        followup_df: DataFrame from follow-up snapshot (e.g., 2023-05-01)
        baseline_date: Date of baseline snapshot (for documentation)
        followup_date: Date of follow-up snapshot (for documentation)

    Returns:
        DataFrame with company_id and survival binary indicator

    Examples:
        >>> baseline = pd.DataFrame({'CompanyID': [1, 2, 3, 4]})
        >>> followup = pd.DataFrame({'CompanyID': [1, 3, 4, 5]})
        >>> result = create_survival_from_company_snapshots(baseline, followup)
        >>> result['survival'].tolist()
        [1, 0, 1, 1]  # Company 2 disappeared, others survived
    """
    # Standardize company ID column name
    baseline_id_col = 'CompanyID' if 'CompanyID' in baseline_df.columns else 'company_id'
    followup_id_col = 'CompanyID' if 'CompanyID' in followup_df.columns else 'company_id'

    if baseline_id_col not in baseline_df.columns:
        raise ValueError("Baseline must have 'CompanyID' or 'company_id' column")
    if followup_id_col not in followup_df.columns:
        raise ValueError("Follow-up must have 'CompanyID' or 'company_id' column")

    # Get company IDs from both snapshots
    baseline_companies = set(baseline_df[baseline_id_col].dropna().unique())
    followup_companies = set(followup_df[followup_id_col].dropna().unique())

    print(f"\n  📊 Survival Analysis:")
    print(f"     Baseline ({baseline_date}): {len(baseline_companies):,} companies")
    print(f"     Follow-up ({followup_date}): {len(followup_companies):,} companies")

    # Calculate survival
    survived = baseline_companies & followup_companies  # Intersection
    disappeared = baseline_companies - followup_companies  # In baseline but not follow-up

    survival_rate = len(survived) / len(baseline_companies) if len(baseline_companies) > 0 else 0

    print(f"     Survived: {len(survived):,} ({survival_rate:.1%})")
    print(f"     Disappeared: {len(disappeared):,} ({1-survival_rate:.1%})")

    # Create survival DataFrame
    survival_df = pd.DataFrame({
        'company_id': list(baseline_companies),
        'survival': [1 if cid in survived else 0 for cid in baseline_companies]
    })

    return survival_df


# =============================================================================
# SECTOR FIXED EFFECTS
# =============================================================================

def extract_sector_fe(keywords: pd.Series) -> pd.Series:
    """
    Extract sector fixed effects from Keywords column.

    Maps companies to 5-10 broad sector categories based on keyword matching.

    Categories:
        - AI/ML Software
        - Hardware/Robotics
        - Biotech/Healthcare
        - FinTech
        - Enterprise Software
        - Consumer Software
        - Data/Analytics
        - Other

    Args:
        keywords: Series of keyword strings

    Returns:
        Series of sector category labels

    Examples:
        >>> keywords = pd.Series([
        ...     "AI, machine learning, NLP",
        ...     "robotics, hardware, sensors",
        ...     "biotech, drug discovery"
        ... ])
        >>> extract_sector_fe(keywords)
        0    AI/ML Software
        1    Hardware/Robotics
        2    Biotech/Healthcare
        dtype: object
    """
    def classify_sector(keyword_str):
        if pd.isna(keyword_str):
            return "Other"

        kw_lower = str(keyword_str).lower()

        # Priority order matters (hardware before software to catch hardware-AI)
        if any(word in kw_lower for word in ['biotech', 'pharma', 'drug', 'health', 'medical', 'therapeutics']):
            return "Biotech/Healthcare"
        elif any(word in kw_lower for word in ['hardware', 'robotics', 'robot', 'chip', 'semiconductor', 'sensor', 'device']):
            return "Hardware/Robotics"
        elif any(word in kw_lower for word in ['ai', 'machine learning', 'ml', 'artificial intelligence', 'nlp', 'computer vision', 'deep learning']):
            return "AI/ML Software"
        elif any(word in kw_lower for word in ['fintech', 'finance', 'payment', 'banking', 'crypto', 'blockchain']):
            return "FinTech"
        elif any(word in kw_lower for word in ['data analytics', 'big data', 'data science', 'business intelligence']):
            return "Data/Analytics"
        elif any(word in kw_lower for word in ['enterprise', 'b2b', 'saas', 'cloud']):
            return "Enterprise Software"
        elif any(word in kw_lower for word in ['consumer', 'b2c', 'mobile app', 'gaming', 'social']):
            return "Consumer Software"
        else:
            return "Other"

    return keywords.apply(classify_sector)


# =============================================================================
# DOWN ROUNDS DETECTION
# =============================================================================

def detect_down_rounds(deal_data: pd.DataFrame) -> pd.DataFrame:
    """
    Detect down rounds (when post-valuation decreases from previous round).

    Down round: PostValuation_t < PostValuation_{t-1}

    Args:
        deal_data: DataFrame with company_id, deal_date, post_valuation columns

    Returns:
        DataFrame with is_down_round binary indicator added

    Note:
        Down rounds are flagged but NOT excluded from analysis per user specs.
        Used in H2 robustness test only.
    """
    # Ensure required columns exist
    required_cols = ['company_id', 'deal_date', 'post_valuation']
    missing = [col for col in required_cols if col not in deal_data.columns]
    if missing:
        print(f"Warning: Missing columns for down round detection: {missing}")
        deal_data['is_down_round'] = 0
        return deal_data

    # Sort by company and date
    deal_sorted = deal_data.sort_values(['company_id', 'deal_date']).copy()

    # Get previous valuation per company
    deal_sorted['prev_valuation'] = deal_sorted.groupby('company_id')['post_valuation'].shift(1)

    # Flag down rounds
    deal_sorted['is_down_round'] = (
        (deal_sorted['post_valuation'] < deal_sorted['prev_valuation']) &
        (deal_sorted['prev_valuation'].notna())
    ).astype(int)

    return deal_sorted


# =============================================================================
# CONTROL VARIABLES
# =============================================================================

def compute_log_employees(employees: pd.Series) -> pd.Series:
    """
    Compute log-transformed employee count.

    Uses log1p (log(x+1)) to handle zero values gracefully.

    Args:
        employees: Series of employee counts

    Returns:
        Log-transformed employee counts
    """
    return np.log1p(pd.to_numeric(employees, errors='coerce').fillna(0))


def compute_firm_age(year_founded: pd.Series, current_year: int = 2024) -> pd.Series:
    """
    Compute firm age from founding year.

    Args:
        year_founded: Series of founding years
        current_year: Reference year for age calculation

    Returns:
        Series of firm ages in years
    """
    years = pd.to_numeric(year_founded, errors='coerce')
    return current_year - years


def compute_founder_credibility(df: pd.DataFrame) -> pd.Series:
    """
    Compute founder credibility indicator.

    Uses serial founder status as primary measure (binary: 0 or 1).

    Implementation options (auto-detected):
    1. If 'NumberOfFounders' column exists:
       - Serial founder = 1 if founded 2+ companies (proxy: total_raised in top quartile)
    2. If 'FoundingTeam' or similar text field exists:
       - Parse for serial founder indicators
    3. Fallback: Use proxy based on firm characteristics:
       - Serial founder = 1 if (firm_age < 5 years) AND (total_raised > median)
       - Rationale: Young companies with high funding = experienced founders

    Args:
        df: DataFrame with company data

    Returns:
        Series of founder credibility (0 or 1)

    Examples:
        >>> df = pd.DataFrame({
        ...     'TotalRaised': [1e6, 1e7, 1e8],
        ...     'YearFounded': [2020, 2015, 2018]
        ... })
        >>> compute_founder_credibility(df)
        0    0  # Low funding, recent
        1    1  # High funding, experienced
        2    1  # Very high funding
        dtype: int64
    """
    n = len(df)

    # Option 1: Check for direct founder columns
    founder_cols = [col for col in df.columns if 'founder' in col.lower()]

    if 'NumberOfFounders' in df.columns:
        # Use number of founders as proxy (more founders = more experience)
        num_founders = pd.to_numeric(df['NumberOfFounders'], errors='coerce')
        return (num_founders >= 2).astype(int)  # 2+ founders = more credible

    elif any('founding' in col.lower() for col in df.columns):
        # Check for founding team text fields
        founding_col = [col for col in df.columns if 'founding' in col.lower()][0]
        # Look for serial founder indicators in text
        serial_indicators = df[founding_col].str.contains(
            'serial|prior|previous|founded|co-founded',
            case=False,
            na=False
        )
        return serial_indicators.astype(int)

    # Fallback Option: Proxy from firm characteristics
    print("    ℹ️  No founder columns found, using proxy:")
    print("       Serial founder = (young firm + high funding) OR (high funding + high growth)")

    # Calculate proxies
    if 'TotalRaised' in df.columns:
        total_raised = pd.to_numeric(df['TotalRaised'], errors='coerce').fillna(0)
    else:
        total_raised = pd.Series(0, index=df.index)

    if 'YearFounded' in df.columns:
        year_founded = pd.to_numeric(df['YearFounded'], errors='coerce').fillna(2020)
    else:
        year_founded = pd.Series(2020, index=df.index)

    firm_age = 2024 - year_founded

    # High funding threshold (75th percentile)
    if len(total_raised[total_raised > 0]) > 0:
        high_funding_threshold = total_raised[total_raised > 0].quantile(0.75)
    else:
        high_funding_threshold = 0

    # Serial founder proxy logic:
    # 1. Young company (<5 years) + High funding = experienced founder
    # 2. OR: Very high funding (>75th percentile) = successful fundraiser = credible
    serial_founder = (
        ((firm_age < 5) & (total_raised > high_funding_threshold)) |  # Young + high funding
        (total_raised > high_funding_threshold)  # OR just high funding
    ).astype(int)

    return serial_founder


def standardize_variable(series: pd.Series) -> pd.Series:
    """
    Standardize a variable to mean=0, std=1.

    Args:
        series: Series to standardize

    Returns:
        Standardized series
    """
    return (series - series.mean()) / series.std()


# =============================================================================
# FULL FEATURE ENGINEERING PIPELINE
# =============================================================================

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Complete feature engineering pipeline for hypothesis testing.

    Takes raw company/deal data and creates all derived features needed
    for H1 and H2 analysis.

    Args:
        df: DataFrame with raw company and deal data

    Returns:
        DataFrame with engineered features added

    Expected input columns:
        - Description (or description)
        - Keywords (or keywords)
        - FirstFinancingSize (or first_financing_size)
        - LastFinancingDealType (or last_financing_deal_type)
        - Employees (or employees)
        - YearFounded (or year_founded)
    """
    df = df.copy()

    # Normalize column names (handle both PascalCase and snake_case)
    column_mapping = {
        'Description': 'description',
        'Keywords': 'keywords',
        'FirstFinancingSize': 'first_financing_size',
        'LastFinancingDealType': 'last_financing_deal_type',
        'Employees': 'employees',
        'YearFounded': 'year_founded',
        'TotalRaised': 'total_raised'
    }
    df.rename(columns=column_mapping, inplace=True, errors='ignore')

    print("Engineering features...")

    # 1. Vagueness score
    if 'description' in df.columns:
        print("  - Computing vagueness scores...")
        df['vagueness'] = compute_vagueness_vectorized(df['description'])

    # 2. Integration cost
    if 'keywords' in df.columns:
        print("  - Classifying integration cost...")
        desc = df['description'] if 'description' in df.columns else None
        df['high_integration_cost'] = classify_integration_cost_vectorized(
            df['keywords'], desc
        )

    # 3. Funding variables
    if 'first_financing_size' in df.columns:
        print("  - Deriving early funding amounts...")
        df['early_funding_musd'] = derive_early_funding(df['first_financing_size'])

    if 'last_financing_deal_type' in df.columns:
        print("  - Deriving later success indicator...")
        df['later_success'] = derive_later_success(df['last_financing_deal_type'])

    # 4. Control variables
    if 'employees' in df.columns:
        print("  - Computing log employees...")
        df['employees_log'] = compute_log_employees(df['employees'])

    if 'year_founded' in df.columns:
        print("  - Computing firm age...")
        df['firm_age'] = compute_firm_age(df['year_founded'])

    print("  ✓ Feature engineering complete")

    return df


# =============================================================================
# ANALYSIS DATASET CREATION (MAIN ORCHESTRATOR)
# =============================================================================

def create_analysis_dataset(
    company_df: pd.DataFrame,
    deal_df: pd.DataFrame,
    snapshot_20230501_df: pd.DataFrame = None
) -> pd.DataFrame:
    """
    Create complete analysis dataset with all variables for H1, H2 main, and H2 robustness.

    This is the main orchestrator function that calls all feature engineering
    functions to create the final analysis-ready dataset.

    Variables created (Page 13 table):
        - vagueness: LLM-based generality score (0-100)
        - early_funding_musd: First financing amount in millions USD
        - survival: Binary indicator (Main DV for H2)
        - high_integration_cost: Moderator (0=modular, 1=integrated)
        - founder_credibility: Placeholder (TODO: implement)
        - employees_log: log(employees+1)
        - sector_fe: Sector fixed effects (categorical)
        - year_founded: Founding year
        - is_down_round: Down round indicator (for H2 robustness)
        - series_a_funding: Series A amount (for H2 robustness)
        - series_b_funding: Series B amount (for H2 robustness)

    Args:
        company_df: DataFrame with company-level data
        deal_df: DataFrame with deal-level data
        snapshot_20230501_df: Optional DataFrame with May 2023 snapshot
                              (if None, survival not computed)

    Returns:
        DataFrame with all analysis variables

    Usage:
        >>> analysis_data = create_analysis_dataset(companies, deals, snapshot)
        >>> # Ready for hypothesis testing
        >>> run_h1_early_funding(analysis_data)
        >>> run_h2_main_survival(analysis_data)
    """
    print("\n" + "="*80)
    print("CREATING ANALYSIS DATASET")
    print("="*80)

    # Step 1: Engineer features from company data
    print("\n[1/7] Engineering company features...")
    company_features = engineer_features(company_df)

    # Step 2: Extract sector fixed effects
    print("\n[2/7] Extracting sector fixed effects...")
    if 'keywords' in company_features.columns:
        company_features['sector_fe'] = extract_sector_fe(company_features['keywords'])
        print(f"  Sector distribution:\n{company_features['sector_fe'].value_counts()}")
    else:
        print("  Warning: No 'keywords' column found, setting sector_fe to 'Other'")
        company_features['sector_fe'] = "Other"

    # Step 3: Add founder credibility (placeholder)
    print("\n[3/7] Adding founder credibility (placeholder)...")
    company_features['founder_credibility'] = 0
    print("  ⚠️  TODO: Implement founder_credibility calculation")
    print("      (e.g., prior exits, patents, advanced degrees)")

    # Step 4: Create survival variable (if snapshot provided)
    if snapshot_20230501_df is not None:
        print("\n[4/7] Computing survival variable from 3 snapshots...")
        survival_df = create_survival_from_snapshots(
            snapshot_20230501_df,
            deal_df,
            cutoff_date="2021-11-01"
        )
        # Merge with company features
        company_features = company_features.merge(
            survival_df,
            on='company_id',
            how='left'
        )
        survival_rate = company_features['survival'].mean()
        print(f"  Survival rate: {survival_rate:.1%} ({company_features['survival'].sum()}/{len(company_features)})")
    else:
        print("\n[4/7] Skipping survival variable (no snapshot provided)")
        company_features['survival'] = np.nan

    # Step 5: Extract Series A/B funding amounts
    print("\n[5/7] Extracting Series A and Series B funding amounts...")
    series_a = deal_df[deal_df['vc_round'].str.contains('Series A', case=False, na=False)].copy()
    series_b = deal_df[deal_df['vc_round'].str.contains('Series B', case=False, na=False)].copy()

    if len(series_a) > 0:
        series_a_grouped = series_a.groupby('company_id')['deal_size'].first().reset_index()
        series_a_grouped.columns = ['company_id', 'series_a_funding']
        company_features = company_features.merge(series_a_grouped, on='company_id', how='left')
        print(f"  Series A deals found: {len(series_a_grouped)}")
    else:
        company_features['series_a_funding'] = np.nan
        print("  Warning: No Series A deals found")

    if len(series_b) > 0:
        series_b_grouped = series_b.groupby('company_id')['deal_size'].first().reset_index()
        series_b_grouped.columns = ['company_id', 'series_b_funding']
        company_features = company_features.merge(series_b_grouped, on='company_id', how='left')
        print(f"  Series B deals found: {len(series_b_grouped)}")
    else:
        company_features['series_b_funding'] = np.nan
        print("  Warning: No Series B deals found")

    # Step 6: Detect down rounds
    print("\n[6/7] Detecting down rounds...")
    if all(col in deal_df.columns for col in ['company_id', 'deal_date', 'post_valuation']):
        deal_with_down = detect_down_rounds(deal_df)
        # Get down round indicator per company (1 if any down round)
        down_rounds = deal_with_down.groupby('company_id')['is_down_round'].max().reset_index()
        company_features = company_features.merge(down_rounds, on='company_id', how='left')
        company_features['is_down_round'] = company_features['is_down_round'].fillna(0).astype(int)
        n_down = company_features['is_down_round'].sum()
        print(f"  Companies with down rounds: {n_down} ({n_down/len(company_features)*100:.1f}%)")
    else:
        company_features['is_down_round'] = 0
        print("  Warning: Missing columns for down round detection")

    # Step 7: Final variable summary
    print("\n[7/7] Final dataset summary...")
    analysis_vars = [
        'vagueness', 'early_funding_musd', 'survival', 'high_integration_cost',
        'founder_credibility', 'employees_log', 'sector_fe', 'year_founded',
        'series_a_funding', 'series_b_funding', 'is_down_round'
    ]
    available_vars = [var for var in analysis_vars if var in company_features.columns]

    print(f"\n  Total companies: {len(company_features)}")
    print(f"  Variables created: {len(available_vars)}/{len(analysis_vars)}")
    print("\n  Variable missingness:")
    for var in available_vars:
        if company_features[var].dtype == 'object':
            # Categorical variable
            n_valid = company_features[var].notna().sum()
            pct = n_valid / len(company_features) * 100
            print(f"    - {var}: {n_valid}/{len(company_features)} ({pct:.1f}%)")
        else:
            # Numeric variable
            n_valid = company_features[var].notna().sum()
            pct = n_valid / len(company_features) * 100
            mean = company_features[var].mean()
            print(f"    - {var}: {n_valid}/{len(company_features)} ({pct:.1f}%), mean={mean:.2f}")

    print("\n" + "="*80)
    print("✓ ANALYSIS DATASET READY")
    print("="*80)

    return company_features


# =============================================================================
# UTILITIES
# =============================================================================

def get_feature_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate summary statistics for engineered features.

    Args:
        df: DataFrame with engineered features

    Returns:
        DataFrame with summary statistics
    """
    feature_cols = [
        'vagueness', 'high_integration_cost', 'early_funding_musd',
        'later_success', 'employees_log', 'firm_age'
    ]

    available_cols = [col for col in feature_cols if col in df.columns]

    summary = df[available_cols].describe().T
    summary['missing'] = df[available_cols].isna().sum()
    summary['missing_pct'] = (summary['missing'] / len(df) * 100).round(2)

    return summary


if __name__ == "__main__":
    # Example usage and testing
    print("Feature Engineering Module - Example Usage\n")
    print("=" * 80)

    # Create sample data
    sample_data = pd.DataFrame({
        'description': [
            "We provide approximately scalable machine learning APIs",
            "Precision robotics hardware for manufacturing automation",
            "Cloud-based SaaS platform for data analytics"
        ],
        'keywords': [
            "AI, software, cloud",
            "robotics, hardware, manufacturing",
            "SaaS, cloud, platform"
        ],
        'first_financing_size': [5000000, 15000000, 3000000],
        'last_financing_deal_type': ["Series A", "Series B", "Series A"],
        'employees': [50, 150, 25],
        'year_founded': [2020, 2018, 2021]
    })

    print("Sample input data:")
    print(sample_data[['description', 'keywords']])
    print("\n" + "=" * 80)

    # Engineer features
    result = engineer_features(sample_data)

    print("\nEngineered features:")
    feature_cols = [
        'vagueness', 'high_integration_cost', 'early_funding_musd',
        'later_success', 'employees_log', 'firm_age'
    ]
    print(result[feature_cols])

    print("\n" + "=" * 80)
    print("Feature summary:")
    print(get_feature_summary(result))
