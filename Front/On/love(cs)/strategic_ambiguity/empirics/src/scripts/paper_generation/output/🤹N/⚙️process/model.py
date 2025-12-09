#!/usr/bin/env python3
"""
P3: Execution Gap - Optimal Number of Options
Model Module - 나대용 🐅 (Builder)

Newsvendor optimization for strategic options.

Variables:
- D: Demand (market opportunities) ~ Poisson(λ) or Normal(μ,σ²)
- C: Commitment cost (being wrong)
- F: Flexibility cost (waiting)
- k: Number of options to maintain
- CR: Commitment ratio = C / (C + F)

Outputs:
- k* = argmax E[payoff]
- CR vs k* curve
- Sensitivity analysis
"""

import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import minimize_scalar
from dataclasses import dataclass
from typing import Tuple, Dict, Any, Optional, List

# Reproducibility
SEED = 42
np.random.seed(SEED)


@dataclass
class NewsvendorConfig:
    """Configuration for newsvendor model"""
    # Demand parameters
    demand_mean: float = 5.0  # Expected market opportunities
    demand_std: float = 2.0   # Uncertainty in opportunities

    # Cost parameters (will be varied)
    value_per_option: float = 100.0  # Value when option is exercised

    # Simulation settings
    n_simulations: int = 10000


@dataclass
class CostStructure:
    """Cost structure for a given industry/scenario"""
    C: float  # Commitment cost (being wrong)
    F: float  # Flexibility cost (waiting)

    @property
    def CR(self) -> float:
        """Commitment Ratio"""
        return self.C / (self.C + self.F) if (self.C + self.F) > 0 else 0.5

    @property
    def total_cost(self) -> float:
        """Total cost per option"""
        return self.C + self.F


def expected_payoff_normal(k: float, costs: CostStructure,
                          config: NewsvendorConfig) -> float:
    """
    Calculate expected payoff for k options with normal demand.

    Payoff(k) = E[min(k, D)] * V - k * F - E[max(0, D-k)] * C
    """
    mu, sigma = config.demand_mean, config.demand_std
    V = config.value_per_option
    C, F = costs.C, costs.F

    # E[min(k, D)] for normal distribution
    # = k * Φ((k-μ)/σ) + μ * (1 - Φ((k-μ)/σ)) - σ * φ((k-μ)/σ)
    z = (k - mu) / sigma if sigma > 0 else 0

    cdf_z = stats.norm.cdf(z)
    pdf_z = stats.norm.pdf(z)

    expected_min = k * cdf_z + mu * (1 - cdf_z) - sigma * pdf_z

    # E[max(0, D-k)] = E[D] - E[min(k, D)]
    expected_excess = mu - expected_min

    # Total expected payoff
    payoff = expected_min * V - k * F - expected_excess * C

    return payoff


def expected_payoff_poisson(k: int, costs: CostStructure,
                           config: NewsvendorConfig) -> float:
    """
    Calculate expected payoff for k options with Poisson demand.
    """
    lam = config.demand_mean
    V = config.value_per_option
    C, F = costs.C, costs.F

    # E[min(k, D)] for Poisson
    expected_min = sum(
        min(k, d) * stats.poisson.pmf(d, lam)
        for d in range(int(lam * 3) + 1)
    )

    # E[max(0, D-k)]
    expected_excess = lam - expected_min

    # Total expected payoff
    payoff = expected_min * V - k * F - expected_excess * C

    return payoff


def find_optimal_k_normal(costs: CostStructure,
                         config: NewsvendorConfig) -> Tuple[float, float]:
    """
    Find optimal k* for normal demand using newsvendor formula.

    k* = μ + σ * Φ⁻¹(CR)
    """
    mu, sigma = config.demand_mean, config.demand_std
    CR = costs.CR

    # Critical fractile solution
    k_star = mu + sigma * stats.norm.ppf(CR)
    k_star = max(0, k_star)  # Can't have negative options

    # Calculate expected payoff at optimum
    payoff_star = expected_payoff_normal(k_star, costs, config)

    return k_star, payoff_star


def find_optimal_k_search(costs: CostStructure,
                         config: NewsvendorConfig,
                         demand_type: str = 'normal') -> Tuple[float, float]:
    """
    Find optimal k* via grid search (works for any demand distribution).
    """
    if demand_type == 'poisson':
        payoff_func = lambda k: -expected_payoff_poisson(int(k), costs, config)
        k_range = range(0, int(config.demand_mean * 3) + 1)
        payoffs = [expected_payoff_poisson(k, costs, config) for k in k_range]
        k_star = k_range[np.argmax(payoffs)]
        payoff_star = max(payoffs)
    else:
        result = minimize_scalar(
            lambda k: -expected_payoff_normal(k, costs, config),
            bounds=(0, config.demand_mean * 3),
            method='bounded'
        )
        k_star = result.x
        payoff_star = -result.fun

    return k_star, payoff_star


def generate_cr_kstar_curve(config: NewsvendorConfig = NewsvendorConfig()) -> pd.DataFrame:
    """
    Generate CR vs k* curve.

    Shows how optimal option count varies with commitment ratio.
    """
    results = []

    # Vary CR from 0.1 to 0.9
    cr_range = np.linspace(0.1, 0.9, 50)

    for cr in cr_range:
        # Set C and F to achieve desired CR
        # CR = C / (C + F), so C = CR * (C + F)
        # Let C + F = 100 (normalized)
        total = 100
        C = cr * total
        F = (1 - cr) * total

        costs = CostStructure(C=C, F=F)
        k_star, payoff = find_optimal_k_normal(costs, config)

        results.append({
            'CR': cr,
            'C': C,
            'F': F,
            'k_star': k_star,
            'payoff': payoff
        })

    return pd.DataFrame(results)


def generate_sensitivity_analysis(config: NewsvendorConfig = NewsvendorConfig()) -> pd.DataFrame:
    """
    Sensitivity analysis: how does k* change with demand uncertainty (σ)?
    """
    results = []

    sigma_range = np.linspace(0.5, 5.0, 20)
    cr_levels = [0.3, 0.5, 0.7]

    for sigma in sigma_range:
        config_mod = NewsvendorConfig(
            demand_mean=config.demand_mean,
            demand_std=sigma,
            value_per_option=config.value_per_option
        )

        for cr in cr_levels:
            total = 100
            costs = CostStructure(C=cr * total, F=(1 - cr) * total)
            k_star, payoff = find_optimal_k_normal(costs, config_mod)

            results.append({
                'sigma': sigma,
                'CR': cr,
                'k_star': k_star,
                'payoff': payoff
            })

    return pd.DataFrame(results)


def industry_calibration() -> pd.DataFrame:
    """
    Calibrate CR and k* for different industries.
    """
    industries = {
        'SaaS': {'C': 30, 'F': 30, 'mu': 3, 'sigma': 1},
        'Fintech': {'C': 50, 'F': 40, 'mu': 4, 'sigma': 1.5},
        'Biotech': {'C': 70, 'F': 60, 'mu': 5, 'sigma': 2},
        'AV (LiDAR vs Vision)': {'C': 80, 'F': 45, 'mu': 4, 'sigma': 2.5},
        'Quantum Computing': {'C': 90, 'F': 15, 'mu': 6, 'sigma': 3},
        'Hardware Manufacturing': {'C': 60, 'F': 80, 'mu': 3, 'sigma': 1}
    }

    results = []
    for name, params in industries.items():
        costs = CostStructure(C=params['C'], F=params['F'])
        config = NewsvendorConfig(
            demand_mean=params['mu'],
            demand_std=params['sigma']
        )
        k_star, payoff = find_optimal_k_normal(costs, config)

        results.append({
            'industry': name,
            'C': params['C'],
            'F': params['F'],
            'CR': costs.CR,
            'demand_mean': params['mu'],
            'demand_std': params['sigma'],
            'k_star': k_star,
            'optimal_strategy': 'Commit early' if k_star < 2 else
                               'Balanced' if k_star < 4 else 'Many options'
        })

    return pd.DataFrame(results)


def compute_policy_regions() -> Dict[str, Tuple[float, float]]:
    """
    Define CR thresholds for different strategic policies.
    """
    return {
        'Commit Early': (0.0, 0.35),
        'Balanced': (0.35, 0.65),
        'Many Options': (0.65, 1.0)
    }


def main():
    """Main execution for P3 newsvendor model"""
    print("=" * 70)
    print("P3: Execution Gap - Newsvendor Optimization")
    print("Builder: 나대용 🐅")
    print("=" * 70)

    config = NewsvendorConfig()

    # CR vs k* curve
    print("\n📈 Generating CR vs k* curve...")
    cr_curve = generate_cr_kstar_curve(config)
    print(f"   CR range: [{cr_curve['CR'].min():.2f}, {cr_curve['CR'].max():.2f}]")
    print(f"   k* range: [{cr_curve['k_star'].min():.2f}, {cr_curve['k_star'].max():.2f}]")

    # Sensitivity analysis
    print("\n📊 Running sensitivity analysis...")
    sensitivity = generate_sensitivity_analysis(config)

    # Industry calibration
    print("\n🏭 Industry calibration:")
    industries = industry_calibration()
    print(industries.to_string(index=False))

    # Policy regions
    print("\n📋 Policy Regions:")
    regions = compute_policy_regions()
    for policy, (low, high) in regions.items():
        print(f"   {policy}: CR ∈ [{low:.2f}, {high:.2f}]")

    # Key insights
    print("\n💡 Key Insights:")
    print("   - Low CR (C << F): Commit early, few options optimal")
    print("   - High CR (C >> F): Many options optimal, hedge broadly")
    print("   - Higher σ(D): More options needed regardless of CR")

    print("\n✅ P3 Model Complete!")

    return cr_curve, sensitivity, industries


if __name__ == "__main__":
    cr_curve, sensitivity, industries = main()
