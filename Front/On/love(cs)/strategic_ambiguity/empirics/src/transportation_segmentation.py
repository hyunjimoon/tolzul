#!/usr/bin/env python3
"""
Transportation Segmentation by Customer & Technology
=====================================================
Systematically categorizes transportation companies by:
1. Customer Heterogeneity: B2C, B2B, B2G
2. Pivoting Cost / Experiment Cost: Software, Fleet, Infrastructure

This operationalizes Modules 1 & 2 of the 4-Modules Framework.

Usage:
    from src.transportation_segmentation import categorize_transportation_companies

    df_transport = load_dataframe('data/outputs/transportation/dataset.nc')
    df_segmented = categorize_transportation_companies(df_transport)
"""

import pandas as pd
import numpy as np
from typing import Tuple


def detect_customer_type(description: str, keywords: str = '', promise: str = '') -> str:
    """
    Classify customer type based on text analysis.

    Returns:
        'B2C', 'B2B', 'B2G', or 'Mixed'
    """
    text = f"{description} {keywords} {promise}".lower()

    # B2G indicators (strongest signal)
    b2g_keywords = [
        'government', 'municipal', 'public transit', 'city contract',
        'federal', 'state agency', 'public sector', 'transit authority',
        'dot ', 'department of transportation'
    ]

    # B2B indicators
    b2b_keywords = [
        'enterprise', 'fleet management', 'logistics', 'supply chain',
        'b2b', 'business customer', 'commercial', 'freight',
        'trucking', 'last-mile delivery', 'corporate'
    ]

    # B2C indicators
    b2c_keywords = [
        'consumer', 'rider', 'passenger', 'user', 'commuter',
        'b2c', 'personal transportation', 'ride-sharing', 'ride sharing',
        'on-demand', 'app-based', 'marketplace'
    ]

    # Count matches
    b2g_count = sum(1 for kw in b2g_keywords if kw in text)
    b2b_count = sum(1 for kw in b2b_keywords if kw in text)
    b2c_count = sum(1 for kw in b2c_keywords if kw in text)

    # Decision logic
    total = b2g_count + b2b_count + b2c_count

    if total == 0:
        return 'Unknown'

    # If multiple types detected
    if sum([b2g_count > 0, b2b_count > 0, b2c_count > 0]) >= 2:
        return 'Mixed'

    # Single dominant type
    if b2g_count > 0:
        return 'B2G'
    elif b2b_count > 0:
        return 'B2B'
    elif b2c_count > 0:
        return 'B2C'
    else:
        return 'Unknown'


def detect_tech_stack(description: str, keywords: str = '', promise: str = '') -> str:
    """
    Classify technology stack based on pivoting cost.

    Returns:
        'Software', 'Fleet', 'Infrastructure', or 'Mixed'
    """
    text = f"{description} {keywords} {promise}".lower()

    # Software (low pivoting cost)
    software_keywords = [
        'saas', 'software', 'app', 'application', 'platform',
        'api', 'cloud', 'algorithm', 'ai', 'machine learning',
        'data analytics', 'routing', 'optimization software',
        'mobile app', 'web platform', 'ota update'
    ]

    # Fleet (medium pivoting cost)
    fleet_keywords = [
        'vehicle', 'car', 'truck', 'bus', 'scooter', 'bike',
        'autonomous vehicle', 'self-driving', 'electric vehicle',
        'fleet', 'ride-sharing vehicle', 'micromobility',
        'drone delivery', 'delivery robot'
    ]

    # Infrastructure (high pivoting cost)
    infra_keywords = [
        'infrastructure', 'charging station', 'charging network',
        'highway', 'rail', 'track', 'station', 'terminal',
        'parking', 'garage', 'depot', 'hub', 'facility',
        'hyperloop', 'tunnel', 'bridge', 'port'
    ]

    # Count matches
    software_count = sum(1 for kw in software_keywords if kw in text)
    fleet_count = sum(1 for kw in fleet_keywords if kw in text)
    infra_count = sum(1 for kw in infra_keywords if kw in text)

    # Decision logic
    total = software_count + fleet_count + infra_count

    if total == 0:
        return 'Unknown'

    # If multiple types detected
    if sum([software_count > 0, fleet_count > 0, infra_count > 0]) >= 2:
        return 'Mixed'

    # Single dominant type
    if infra_count > 0:
        return 'Infrastructure'
    elif fleet_count > 0:
        return 'Fleet'
    elif software_count > 0:
        return 'Software'
    else:
        return 'Unknown'


def calculate_customer_heterogeneity_score(customer_type: str) -> float:
    """
    Convert customer type to heterogeneity score (0-1).

    Higher score = more heterogeneous customer base
    """
    scores = {
        'B2C': 1.0,    # Highest heterogeneity (diverse individual needs)
        'Mixed': 0.75,  # Mixed customer base
        'B2B': 0.5,    # Medium heterogeneity (different business needs)
        'B2G': 0.25,   # Low heterogeneity (standardized requirements)
        'Unknown': 0.5  # Default to medium
    }
    return scores.get(customer_type, 0.5)


def calculate_pivoting_cost_score(tech_stack: str) -> float:
    """
    Convert tech stack to pivoting cost score (0-1).

    Higher score = higher pivoting cost (less flexible)
    """
    scores = {
        'Software': 0.0,        # Lowest cost (OTA updates)
        'Mixed': 0.5,           # Mixed tech
        'Fleet': 0.75,          # Medium-high cost (vehicle replacement)
        'Infrastructure': 1.0,  # Highest cost (physical assets)
        'Unknown': 0.5          # Default to medium
    }
    return scores.get(tech_stack, 0.5)


def categorize_transportation_companies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add customer and technology categorization to transportation dataset.

    Args:
        df: Transportation companies DataFrame

    Returns:
        DataFrame with added columns:
        - customer_type: B2C, B2B, B2G, Mixed, Unknown
        - tech_stack: Software, Fleet, Infrastructure, Mixed, Unknown
        - customer_heterogeneity: 0-1 score
        - pivoting_cost: 0-1 score
        - segment: Combined label (e.g., "B2C_Software")
    """
    df = df.copy()

    # Get text columns (handle different naming conventions)
    desc_col = 'Description' if 'Description' in df.columns else 'description'
    kw_col = 'Keywords' if 'Keywords' in df.columns else 'keywords'
    prom_col = 'Promise' if 'Promise' in df.columns else 'promise'

    # Apply categorization
    df['customer_type'] = df.apply(
        lambda row: detect_customer_type(
            str(row.get(desc_col, '')),
            str(row.get(kw_col, '')),
            str(row.get(prom_col, ''))
        ),
        axis=1
    )

    df['tech_stack'] = df.apply(
        lambda row: detect_tech_stack(
            str(row.get(desc_col, '')),
            str(row.get(kw_col, '')),
            str(row.get(prom_col, ''))
        ),
        axis=1
    )

    # Calculate continuous scores
    df['customer_heterogeneity'] = df['customer_type'].apply(calculate_customer_heterogeneity_score)
    df['pivoting_cost'] = df['tech_stack'].apply(calculate_pivoting_cost_score)

    # Create combined segment label
    df['segment'] = df['customer_type'] + '_' + df['tech_stack']

    return df


def get_segment_summary(df_segmented: pd.DataFrame) -> pd.DataFrame:
    """
    Generate summary statistics by segment.

    Returns:
        DataFrame with columns: segment, n, mean_vagueness, survival_rate
    """
    summary = df_segmented.groupby('segment').agg({
        'vagueness': ['count', 'mean', 'std'],
        'growth': 'mean'
    }).round(3)

    summary.columns = ['n', 'mean_vagueness', 'std_vagueness', 'survival_rate']
    summary['survival_rate'] = summary['survival_rate'] * 100  # Convert to percentage
    summary = summary.reset_index()

    return summary.sort_values('n', ascending=False)


# Example usage
if __name__ == '__main__':
    """
    Example: Categorize transportation companies
    """
    from src.data_io import load_dataframe

    # Load transportation dataset
    df_transport = load_dataframe('data/outputs/transportation/dataset.nc')

    print(f"Loaded {len(df_transport):,} transportation companies")

    # Categorize
    df_segmented = categorize_transportation_companies(df_transport)

    # Show distribution
    print("\nCustomer Type Distribution:")
    print(df_segmented['customer_type'].value_counts())

    print("\nTech Stack Distribution:")
    print(df_segmented['tech_stack'].value_counts())

    print("\nSegment Summary:")
    summary = get_segment_summary(df_segmented)
    print(summary)

    # Save segmented dataset
    from src.data_io import save_dataframe
    save_dataframe(df_segmented, 'data/outputs/transportation/dataset_segmented.nc')
    print("\nSaved to data/outputs/transportation/dataset_segmented.nc")
