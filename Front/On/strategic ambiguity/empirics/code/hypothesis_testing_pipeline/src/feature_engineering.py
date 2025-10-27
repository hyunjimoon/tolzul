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

    Measures the frequency of hedge words relative to total word count.
    Higher scores indicate more vague language.

    Args:
        text: Description or text to analyze

    Returns:
        Vagueness score (0-1 scale), or np.nan if text is invalid

    Examples:
        >>> compute_vagueness("We maybe provide approximately scalable solutions")
        0.25  # 2 hedge words out of 8 total
        >>> compute_vagueness("We provide precise machine learning APIs")
        0.0   # 0 hedge words
    """
    if not isinstance(text, str) or pd.isna(text):
        return np.nan

    # Hedge words indicating vagueness/uncertainty
    hedge_words = [
        "maybe", "approximately", "somewhat", "likely", "possibly",
        "potential", "around", "roughly", "flexible", "scalable",
        "adaptive", "designed to", "enables", "allows", "offering",
        "providing", "can be", "may be", "could be"
    ]

    # Tokenize and count
    text_lower = text.lower()
    total_words = len(text.split())

    if total_words == 0:
        return np.nan

    # Count hedge word occurrences
    hits = sum(text_lower.count(hedge) for hedge in hedge_words)

    # Return proportion (0-1 scale)
    return hits / total_words


def compute_vagueness_vectorized(descriptions: pd.Series) -> pd.Series:
    """
    Vectorized version of vagueness computation for pandas Series.

    Args:
        descriptions: Series of text descriptions

    Returns:
        Series of vagueness scores (0-1 scale)
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
