#!/usr/bin/env python3
"""
Shared Test Fixtures for Empirics Pipeline
===========================================
Provides reusable test data and fixtures for unit and integration tests.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path


# ============================================
# Path Fixtures
# ============================================

@pytest.fixture(scope='session')
def test_data_dir():
    """Test data directory for storing fixture files."""
    return Path(__file__).parent / 'fixtures'


@pytest.fixture(scope='session')
def project_root():
    """Project root directory."""
    return Path(__file__).parent.parent


# ============================================
# Minimal Valid Company DataFrames
# ============================================

@pytest.fixture
def minimal_company_df():
    """
    Minimal valid company dataset for quick unit tests.

    Contains 20 companies with all required columns for H1/H2 testing.
    No missing values, balanced hardware/software split.
    """
    np.random.seed(42)  # Reproducible

    n = 20

    return pd.DataFrame({
        'company_id': range(1, n + 1),
        'description': [f'Company {i} description' for i in range(1, n + 1)],
        'employees': np.random.randint(5, 200, n),
        'z_employees_log': np.random.randn(n),
        'vagueness': np.random.uniform(20, 80, n),
        'z_vagueness': np.random.randn(n),
        'is_hardware': [0, 1] * (n // 2),  # Alternating
        'early_funding_musd': np.random.uniform(0.5, 10.0, n),
        'growth': [0, 1, 1, 0, 1, 0, 1, 1, 0, 1] * 2,  # 60% growth rate
        'founder_serial': [0, 0, 1, 0, 1, 1, 0, 1, 0, 1] * 2,  # 50% serial
        'z_firm_age': np.random.randn(n),
        'sector_fe': ['Software', 'Hardware', 'Quantum', 'AI'] * (n // 4),
        'founding_cohort': ['2015', '2016', '2017', '2018'] * (n // 4),
    })


@pytest.fixture
def h1_test_df():
    """
    Dataset specifically designed for H1 testing with known properties.

    Features:
    - Strong negative correlation between vagueness and early funding
    - All required columns for full H1 specification
    - No missing values
    """
    np.random.seed(123)

    n = 50

    # Generate vagueness scores
    z_vagueness = np.random.randn(n)

    # Early funding negatively correlated with vagueness (H1 expected effect)
    # early_funding = base - (vagueness effect) + noise
    base_funding = 5.0
    vagueness_effect = 2.0 * z_vagueness
    noise = np.random.randn(n) * 0.5
    early_funding_musd = base_funding - vagueness_effect + noise
    early_funding_musd = np.clip(early_funding_musd, 0.1, 15.0)  # Keep positive

    return pd.DataFrame({
        'company_id': range(1, n + 1),
        'z_vagueness': z_vagueness,
        'z_employees_log': np.random.randn(n),
        'founder_serial': np.random.choice([0, 1], n, p=[0.6, 0.4]),
        'is_hardware': np.random.choice([0, 1], n, p=[0.5, 0.5]),
        'z_firm_age': np.random.randn(n),
        'early_funding_musd': early_funding_musd,
        'sector_fe': np.random.choice(['Software', 'Hardware', 'AI'], n),
        'founding_cohort': np.random.choice(['2015', '2016', '2017'], n),
    })


@pytest.fixture
def h2_test_df():
    """
    Dataset for H2 testing with interaction effect.

    Features:
    - Vagueness beneficial in software (is_hardware=0)
    - Vagueness detrimental in hardware (is_hardware=1)
    - Interaction term should be negative
    """
    np.random.seed(456)

    n = 100

    # Generate predictors
    z_vagueness = np.random.randn(n)
    is_hardware = np.random.choice([0, 1], n, p=[0.6, 0.4])
    z_employees_log = np.random.randn(n)
    founder_serial = np.random.choice([0, 1], n, p=[0.7, 0.3])

    # Growth probability depends on vagueness * is_hardware interaction
    # Software (is_hardware=0): positive vagueness effect
    # Hardware (is_hardware=1): negative vagueness effect
    logit_p = 0.0  # Base rate
    logit_p += 0.5 * z_vagueness  # Main effect (positive in software)
    logit_p -= 1.0 * z_vagueness * is_hardware  # Interaction (negative)
    logit_p += 0.3 * z_employees_log  # Control
    logit_p += 0.2 * founder_serial  # Control

    # Convert logit to probability
    prob_growth = 1 / (1 + np.exp(-logit_p))
    growth = (np.random.rand(n) < prob_growth).astype(int)

    return pd.DataFrame({
        'company_id': range(1, n + 1),
        'z_vagueness': z_vagueness,
        'is_hardware': is_hardware,
        'z_employees_log': z_employees_log,
        'founder_serial': founder_serial,
        'growth': growth,
        'founding_cohort': np.random.choice(['2015', '2016', '2017', '2018'], n),
    })


@pytest.fixture
def constant_founder_serial_df():
    """
    Dataset where founder_serial is constant (for testing formula adjustment).

    This tests the edge case where a variable has no variance and should
    be removed from the regression formula.
    """
    np.random.seed(789)

    n = 30

    return pd.DataFrame({
        'company_id': range(1, n + 1),
        'z_vagueness': np.random.randn(n),
        'z_employees_log': np.random.randn(n),
        'founder_serial': [1] * n,  # CONSTANT - no variance
        'is_hardware': np.random.choice([0, 1], n),
        'z_firm_age': np.random.randn(n),
        'early_funding_musd': np.random.uniform(1.0, 10.0, n),
        'growth': np.random.choice([0, 1], n),
        'sector_fe': ['Software'] * n,  # Single sector
        'founding_cohort': ['2016'] * n,  # Single cohort
    })


@pytest.fixture
def empty_df():
    """Empty DataFrame with correct schema (for testing edge cases)."""
    return pd.DataFrame({
        'company_id': [],
        'z_vagueness': [],
        'z_employees_log': [],
        'founder_serial': [],
        'is_hardware': [],
        'z_firm_age': [],
        'early_funding_musd': [],
        'growth': [],
        'sector_fe': [],
        'founding_cohort': [],
    })


@pytest.fixture
def missing_values_df():
    """
    DataFrame with strategic missing values to test dropna behavior.

    Tests that models correctly handle missing data by dropping rows.
    """
    np.random.seed(999)

    n = 25

    df = pd.DataFrame({
        'company_id': range(1, n + 1),
        'z_vagueness': np.random.randn(n),
        'z_employees_log': np.random.randn(n),
        'founder_serial': np.random.choice([0, 1], n),
        'is_hardware': np.random.choice([0, 1], n),
        'z_firm_age': np.random.randn(n),
        'early_funding_musd': np.random.uniform(1.0, 10.0, n),
        'growth': np.random.choice([0, 1], n),
        'sector_fe': np.random.choice(['Software', 'Hardware'], n),
        'founding_cohort': np.random.choice(['2015', '2016'], n),
    })

    # Introduce missing values
    df.loc[0:4, 'z_vagueness'] = np.nan  # 5 missing vagueness
    df.loc[10:12, 'early_funding_musd'] = np.nan  # 3 missing funding
    df.loc[20:22, 'growth'] = np.nan  # 3 missing growth

    return df


# ============================================
# H3/H4 Fixtures (with founder_credibility)
# ============================================

@pytest.fixture
def h3_test_df():
    """
    Dataset for H3 testing (early funding interaction with founder credibility).

    Features:
    - Log-transformed early funding (handles skew)
    - Interaction between vagueness and founder_serial
    """
    np.random.seed(321)

    n = 60

    z_vagueness = np.random.randn(n)
    founder_serial = np.random.choice([0, 1], n, p=[0.6, 0.4])
    z_employees_log = np.random.randn(n)

    # Early funding with interaction effect
    # Serial founders less affected by vagueness
    log_funding = 1.5  # Base (exp(1.5) ≈ 4.5M)
    log_funding -= 0.4 * z_vagueness  # Vagueness penalty
    log_funding += 0.3 * founder_serial  # Serial founder boost
    log_funding += 0.5 * z_vagueness * founder_serial  # Interaction: serial founders buffer vagueness penalty
    log_funding += np.random.randn(n) * 0.3  # Noise

    early_funding_musd = np.exp(log_funding)
    early_funding_musd = np.clip(early_funding_musd, 0.5, 50.0)

    return pd.DataFrame({
        'company_id': range(1, n + 1),
        'z_vagueness': z_vagueness,
        'founder_serial': founder_serial,
        'z_employees_log': z_employees_log,
        'early_funding_musd': early_funding_musd,
        'sector_fe': np.random.choice(['Software', 'Hardware', 'AI'], n),
        'founding_cohort': np.random.choice(['2015', '2016', '2017'], n),
    })


@pytest.fixture
def h4_test_df():
    """
    Dataset for H4 testing (growth interaction with founder credibility).

    Features:
    - Binary growth outcome
    - Interaction between vagueness and founder_serial
    """
    np.random.seed(654)

    n = 80

    z_vagueness = np.random.randn(n)
    founder_serial = np.random.choice([0, 1], n, p=[0.65, 0.35])
    z_employees_log = np.random.randn(n)

    # Growth probability with interaction
    logit_p = -0.5  # Base rate
    logit_p += 0.4 * z_vagueness  # Vagueness effect
    logit_p += 0.6 * founder_serial  # Serial founder advantage
    logit_p += 0.3 * z_vagueness * founder_serial  # Interaction
    logit_p += 0.2 * z_employees_log  # Size effect

    prob_growth = 1 / (1 + np.exp(-logit_p))
    growth = (np.random.rand(n) < prob_growth).astype(int)

    return pd.DataFrame({
        'company_id': range(1, n + 1),
        'z_vagueness': z_vagueness,
        'founder_serial': founder_serial,
        'z_employees_log': z_employees_log,
        'growth': growth,
        'founding_cohort': np.random.choice(['2015', '2016', '2017'], n),
    })


# ============================================
# Two-Snapshot Mode Fixtures (E/L/S/V/F)
# ============================================

@pytest.fixture
def two_snapshot_df():
    """
    Dataset for two-snapshot validation mode (E, L, S, V, F).

    Variables:
    - E: Early event (1 if Series A at baseline)
    - L: Later success (1 if Series B+ at endpoint)
    - S_stepup_log: Log step-up ratio
    - z_V: Vagueness (z-scored)
    - F_flexibility: 1 - is_hardware
    """
    np.random.seed(111)

    n = 100

    # Generate predictors
    z_V = np.random.randn(n)
    F_flexibility = np.random.choice([0, 1], n, p=[0.3, 0.7])  # 70% flexible (software)

    # E (Early event): negatively affected by vagueness
    prob_E = 1 / (1 + np.exp(-(0.5 - 0.3 * z_V)))
    E = (np.random.rand(n) < prob_E).astype(int)

    # L (Later success): positively affected by vagueness, amplified by flexibility
    logit_L = -0.2  # Base
    logit_L += 0.4 * z_V  # Vagueness main effect
    logit_L += 0.5 * F_flexibility  # Flexibility main effect
    logit_L += 0.3 * z_V * F_flexibility  # Interaction
    prob_L = 1 / (1 + np.exp(-logit_L))
    L = (np.random.rand(n) < prob_L).astype(int)

    # S (Step-up): only for L==1 companies
    # Vagueness increases step-up, especially in flexible sectors
    S_stepup_log = np.full(n, np.nan)
    L_mask = L == 1
    n_survivors = L_mask.sum()
    S_stepup_log[L_mask] = 0.5 + 0.3 * z_V[L_mask] + 0.4 * F_flexibility[L_mask] + \
                           0.2 * z_V[L_mask] * F_flexibility[L_mask] + \
                           np.random.randn(n_survivors) * 0.2

    return pd.DataFrame({
        'company_id': range(1, n + 1),
        'E': E,
        'L': L,
        'S_stepup_log': S_stepup_log,
        'z_V': z_V,
        'F_flexibility': F_flexibility,
        'founding_cohort': np.random.choice(['2015', '2016', '2017'], n),
        'region': np.random.choice(['North America', 'Europe', 'Asia'], n),
    })


# ============================================
# Edge Case Fixtures
# ============================================

@pytest.fixture
def perfect_separation_df():
    """
    Dataset with perfect separation (all Y=0 in one group, all Y=1 in other).

    This should cause logit convergence issues and trigger regularization fallbacks.
    """
    n = 40

    # Create perfect separation: all hardware companies have growth=0, all software have growth=1
    is_hardware = [0] * 20 + [1] * 20
    growth = [1] * 20 + [0] * 20

    return pd.DataFrame({
        'company_id': range(1, n + 1),
        'z_vagueness': np.random.randn(n),
        'is_hardware': is_hardware,
        'z_employees_log': np.random.randn(n),
        'founder_serial': np.random.choice([0, 1], n),
        'growth': growth,
        'founding_cohort': ['2016'] * n,
    })


@pytest.fixture
def single_category_df():
    """
    Dataset with categorical variables having only one level.

    Tests that categorical controls are handled gracefully when they have no variance.
    """
    np.random.seed(222)

    n = 30

    return pd.DataFrame({
        'company_id': range(1, n + 1),
        'z_vagueness': np.random.randn(n),
        'z_employees_log': np.random.randn(n),
        'z_firm_age': np.random.randn(n),
        'founder_serial': np.random.choice([0, 1], n),
        'is_hardware': np.random.choice([0, 1], n),
        'early_funding_musd': np.random.uniform(1.0, 10.0, n),
        'growth': np.random.choice([0, 1], n),
        'sector_fe': ['Software'] * n,  # SINGLE LEVEL
        'founding_cohort': ['2016'] * n,  # SINGLE LEVEL
        'region': ['North America'] * n,  # SINGLE LEVEL
    })


# ============================================
# Marker for Integration Tests
# ============================================

def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )
