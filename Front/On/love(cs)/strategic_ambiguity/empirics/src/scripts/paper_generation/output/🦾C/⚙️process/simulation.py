#!/usr/bin/env python3
"""
P2: Competency Trap - When Success Kills Options
Simulation Module - 나대용 🐅 (Builder)

Bayesian update simulation for belief lock-in.

Variables:
- prior: (μ₀, σ₀) - initial beliefs
- evidence_strength: strength of disconfirming signal
- believer_ratio: proportion of like-minded investors
- switching_threshold: evidence threshold for pivot

Outputs:
- Pivot probability vs σ curve
- Threshold dynamics over time
"""

import numpy as np
import pandas as pd
from scipy import stats
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Any, Optional
from enum import Enum

# Reproducibility
SEED = 42
np.random.seed(SEED)


class InvestorType(Enum):
    """Investor types for cap table composition"""
    BELIEVER = "believer"  # Same-thesis, reinforces current path
    DOUBTER = "doubter"    # Different-thesis, challenges assumptions
    NEUTRAL = "neutral"    # No strong prior


@dataclass
class Prior:
    """Bayesian prior belief about current strategy value"""
    mu: float  # Mean belief
    sigma: float  # Uncertainty (std dev)

    def pdf(self, x: np.ndarray) -> np.ndarray:
        """Probability density function"""
        return stats.norm.pdf(x, self.mu, self.sigma)

    def update(self, evidence: float, evidence_sigma: float) -> 'Prior':
        """Bayesian update with new evidence"""
        # Posterior mean
        mu_post = (evidence_sigma**2 * self.mu + self.sigma**2 * evidence) / \
                  (self.sigma**2 + evidence_sigma**2)
        # Posterior variance
        sigma_post = np.sqrt((self.sigma**2 * evidence_sigma**2) /
                            (self.sigma**2 + evidence_sigma**2))
        return Prior(mu_post, sigma_post)


@dataclass
class Investor:
    """Individual investor with beliefs"""
    type: InvestorType
    prior: Prior
    weight: float = 1.0  # Voting weight (e.g., board seats)


@dataclass
class CapTable:
    """Capital table / Board composition"""
    investors: List[Investor] = field(default_factory=list)

    @property
    def believer_ratio(self) -> float:
        """Proportion of believers by weight"""
        total = sum(inv.weight for inv in self.investors)
        believers = sum(inv.weight for inv in self.investors
                       if inv.type == InvestorType.BELIEVER)
        return believers / total if total > 0 else 0

    def aggregate_prior(self) -> Prior:
        """Weighted average of investor priors"""
        total_weight = sum(inv.weight for inv in self.investors)
        mu_agg = sum(inv.weight * inv.prior.mu for inv in self.investors) / total_weight
        # Variance: use inverse-variance weighting
        var_inv_sum = sum(inv.weight / inv.prior.sigma**2 for inv in self.investors)
        sigma_agg = np.sqrt(total_weight / var_inv_sum)
        return Prior(mu_agg, sigma_agg)


@dataclass
class P2Config:
    """Configuration for P2 simulation"""
    # Prior settings
    high_commitment_mu: float = 0.8  # Confident in current path
    high_commitment_sigma: float = 0.1  # Low uncertainty
    low_commitment_mu: float = 0.5  # Neutral
    low_commitment_sigma: float = 0.3  # High uncertainty

    # Evidence settings
    evidence_sigma: float = 0.2  # Noise in evidence

    # Threshold settings
    base_threshold: float = 0.3  # Base evidence for pivot
    believer_amplifier: float = 0.5  # How much believers raise threshold

    # Simulation settings
    n_periods: int = 20
    n_simulations: int = 1000


def compute_switching_threshold(sigma: float, believer_ratio: float,
                                config: P2Config = P2Config()) -> float:
    """
    Compute the switching threshold given prior uncertainty and believer ratio.

    Lower σ (more confident) → Higher threshold
    Higher believer_ratio → Higher threshold

    τ = base + (1 - σ) * believer_amplifier * believer_ratio
    """
    # Normalize sigma to [0,1] range (assuming sigma in [0.05, 0.5])
    sigma_normalized = np.clip((sigma - 0.05) / 0.45, 0, 1)

    # Threshold increases with confidence (low sigma) and believer composition
    threshold = config.base_threshold + \
                (1 - sigma_normalized) * config.believer_amplifier * believer_ratio

    return np.clip(threshold, 0.1, 0.9)


def simulate_belief_trajectory(
    initial_prior: Prior,
    cap_table: CapTable,
    true_value: float,  # True value of alternative path
    config: P2Config = P2Config()
) -> Dict[str, Any]:
    """
    Simulate belief evolution over time with evidence arrival.

    Returns trajectory of beliefs and pivot decision.
    """
    prior = initial_prior
    trajectory = {
        'mu': [prior.mu],
        'sigma': [prior.sigma],
        'threshold': [],
        'evidence': [],
        'pivot_triggered': False,
        'pivot_period': None
    }

    for t in range(config.n_periods):
        # Generate evidence (noisy signal of true value)
        evidence = true_value + np.random.normal(0, config.evidence_sigma)

        # Compute current threshold
        threshold = compute_switching_threshold(
            prior.sigma, cap_table.believer_ratio, config
        )

        # Check if evidence exceeds threshold to trigger pivot consideration
        # Evidence against current path = low value signal
        evidence_against = 1 - evidence  # Higher when true value is low

        trajectory['evidence'].append(evidence)
        trajectory['threshold'].append(threshold)

        # Update beliefs
        prior = prior.update(evidence, config.evidence_sigma)
        trajectory['mu'].append(prior.mu)
        trajectory['sigma'].append(prior.sigma)

        # Check for pivot trigger
        if prior.mu < (1 - threshold) and not trajectory['pivot_triggered']:
            trajectory['pivot_triggered'] = True
            trajectory['pivot_period'] = t

    return trajectory


def run_monte_carlo_simulation(config: P2Config = P2Config()) -> pd.DataFrame:
    """
    Run Monte Carlo simulation across different commitment levels and believer ratios.
    """
    results = []

    sigma_range = np.linspace(0.05, 0.4, 15)
    believer_range = np.linspace(0.1, 0.9, 9)
    true_value = 0.3  # Alternative path is actually better

    for sigma in sigma_range:
        for believer_ratio in believer_range:
            # Create prior and cap table
            prior = Prior(mu=0.7, sigma=sigma)
            cap_table = CapTable([
                Investor(InvestorType.BELIEVER, Prior(0.8, 0.1), weight=believer_ratio),
                Investor(InvestorType.DOUBTER, Prior(0.4, 0.3), weight=1-believer_ratio)
            ])

            # Run multiple simulations
            pivot_count = 0
            pivot_periods = []

            for _ in range(config.n_simulations):
                traj = simulate_belief_trajectory(prior, cap_table, true_value, config)
                if traj['pivot_triggered']:
                    pivot_count += 1
                    pivot_periods.append(traj['pivot_period'])

            pivot_prob = pivot_count / config.n_simulations
            avg_pivot_period = np.mean(pivot_periods) if pivot_periods else np.nan

            results.append({
                'sigma': sigma,
                'believer_ratio': believer_ratio,
                'pivot_probability': pivot_prob,
                'avg_pivot_period': avg_pivot_period,
                'threshold': compute_switching_threshold(sigma, believer_ratio, config)
            })

    return pd.DataFrame(results)


def analyze_threshold_dynamics(config: P2Config = P2Config()) -> pd.DataFrame:
    """
    Analyze how threshold changes with σ for different believer compositions.
    """
    sigma_range = np.linspace(0.05, 0.5, 50)
    believer_levels = [0.2, 0.5, 0.8]

    results = []
    for sigma in sigma_range:
        for br in believer_levels:
            threshold = compute_switching_threshold(sigma, br, config)
            results.append({
                'sigma': sigma,
                'believer_ratio': br,
                'threshold': threshold
            })

    return pd.DataFrame(results)


def case_study_waymo_vs_comma() -> Dict[str, Dict]:
    """
    Simulate Waymo vs Comma.ai case comparison.
    """
    config = P2Config(n_simulations=500)

    # Waymo: High commitment, believer-heavy
    waymo_prior = Prior(mu=0.85, sigma=0.08)
    waymo_cap = CapTable([
        Investor(InvestorType.BELIEVER, Prior(0.9, 0.05), weight=0.9),
        Investor(InvestorType.NEUTRAL, Prior(0.5, 0.2), weight=0.1)
    ])

    # Comma.ai: Low commitment, doubter presence
    comma_prior = Prior(mu=0.6, sigma=0.25)
    comma_cap = CapTable([
        Investor(InvestorType.BELIEVER, Prior(0.6, 0.2), weight=0.4),
        Investor(InvestorType.DOUBTER, Prior(0.4, 0.3), weight=0.4),
        Investor(InvestorType.NEUTRAL, Prior(0.5, 0.25), weight=0.2)
    ])

    # True value (alternative/pivot path turns out better)
    true_alt_value = 0.7

    # Simulate
    waymo_pivots = 0
    comma_pivots = 0

    for _ in range(config.n_simulations):
        waymo_traj = simulate_belief_trajectory(waymo_prior, waymo_cap, true_alt_value, config)
        comma_traj = simulate_belief_trajectory(comma_prior, comma_cap, true_alt_value, config)

        if waymo_traj['pivot_triggered']:
            waymo_pivots += 1
        if comma_traj['pivot_triggered']:
            comma_pivots += 1

    return {
        'Waymo': {
            'prior_mu': waymo_prior.mu,
            'prior_sigma': waymo_prior.sigma,
            'believer_ratio': waymo_cap.believer_ratio,
            'threshold': compute_switching_threshold(waymo_prior.sigma, waymo_cap.believer_ratio, config),
            'pivot_probability': waymo_pivots / config.n_simulations
        },
        'Comma.ai': {
            'prior_mu': comma_prior.mu,
            'prior_sigma': comma_prior.sigma,
            'believer_ratio': comma_cap.believer_ratio,
            'threshold': compute_switching_threshold(comma_prior.sigma, comma_cap.believer_ratio, config),
            'pivot_probability': comma_pivots / config.n_simulations
        }
    }


def main():
    """Main execution for P2 simulation"""
    print("=" * 70)
    print("P2: Competency Trap - Belief Lock-in Simulation")
    print("Builder: 나대용 🐅")
    print("=" * 70)

    config = P2Config()

    # Threshold dynamics
    print("\n📊 Analyzing threshold dynamics...")
    threshold_df = analyze_threshold_dynamics(config)
    print(f"   Generated {len(threshold_df)} threshold data points")

    # Monte Carlo simulation
    print("\n🎲 Running Monte Carlo simulation...")
    mc_results = run_monte_carlo_simulation(config)
    print(f"   Generated {len(mc_results)} simulation results")

    # Summary statistics
    print("\n📈 Key findings:")
    high_sigma = mc_results[mc_results['sigma'] > 0.25]['pivot_probability'].mean()
    low_sigma = mc_results[mc_results['sigma'] < 0.15]['pivot_probability'].mean()
    print(f"   High σ (uncertain) → Pivot prob: {high_sigma:.1%}")
    print(f"   Low σ (confident) → Pivot prob: {low_sigma:.1%}")

    high_believer = mc_results[mc_results['believer_ratio'] > 0.7]['pivot_probability'].mean()
    low_believer = mc_results[mc_results['believer_ratio'] < 0.3]['pivot_probability'].mean()
    print(f"   High believer ratio → Pivot prob: {high_believer:.1%}")
    print(f"   Low believer ratio → Pivot prob: {low_believer:.1%}")

    # Case study
    print("\n🚗 Case Study: Waymo vs Comma.ai")
    case_results = case_study_waymo_vs_comma()
    for company, data in case_results.items():
        print(f"\n   {company}:")
        print(f"      Prior: μ={data['prior_mu']:.2f}, σ={data['prior_sigma']:.2f}")
        print(f"      Believer ratio: {data['believer_ratio']:.1%}")
        print(f"      Switching threshold: {data['threshold']:.2f}")
        print(f"      Pivot probability: {data['pivot_probability']:.1%}")

    print("\n✅ P2 Simulation Complete!")

    return threshold_df, mc_results, case_results


if __name__ == "__main__":
    threshold_df, mc_results, case_results = main()
