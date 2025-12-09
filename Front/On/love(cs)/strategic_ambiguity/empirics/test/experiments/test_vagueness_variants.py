#!/usr/bin/env python3
"""
Vagueness Scorer Variant Testing
=================================
Tests different vagueness scoring approaches to find one with better variance.

Problem:
- Current V1 scorer produces 75% of companies with score = 50.0
- This severely limits statistical power for H1/H2 models

This script tests:
1. V1 (current) - StrategicVaguenessScorer
2. V2 (thesis spec) - StrategicVaguenessScorerV2
3. V2 with different normalization
4. Simple concrete feature count
5. Hybrid approaches

Usage:
    python3 experiments/test_vagueness_variants.py
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple
import logging

# Import both scorers
from features import StrategicVaguenessScorer
from vagueness_v2 import StrategicVaguenessScorerV2

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def load_sample_data(n_samples: int = 10000) -> pd.DataFrame:
    """Load a sample of companies from the full dataset."""
    cache_file = Path("data/processed/consolidated_companies.parquet")

    if not cache_file.exists():
        logger.error(f"Cache file not found: {cache_file}")
        logger.error("Run pipeline/01_load_data.py first")
        return None

    logger.info(f"Loading {n_samples:,} sample companies...")
    df = pd.read_parquet(cache_file)

    # Rename columns to lowercase
    df = df.rename(columns={
        'Description': 'description',
        'Keywords': 'keywords',
        'CompanyID': 'company_id'
    })

    # Take a random sample
    df_sample = df.sample(n=min(n_samples, len(df)), random_state=42)

    # Keep only rows with text
    df_sample = df_sample[df_sample['description'].notna() & df_sample['keywords'].notna()].copy()

    logger.info(f"Loaded {len(df_sample):,} companies with text")
    return df_sample


def score_v1(df: pd.DataFrame) -> pd.Series:
    """Score using V1 (current production scorer)."""
    logger.info("\n" + "="*60)
    logger.info("VARIANT 1: V1 Scorer (Current)")
    logger.info("="*60)

    scorer = StrategicVaguenessScorer()

    scores = df.apply(
        lambda row: scorer.score_vagueness(row['description'], row['keywords']),
        axis=1
    )

    return scores


def score_v2_standard(df: pd.DataFrame) -> pd.Series:
    """Score using V2 with standard settings."""
    logger.info("\n" + "="*60)
    logger.info("VARIANT 2: V2 Scorer (Thesis Spec)")
    logger.info("="*60)

    scorer = StrategicVaguenessScorerV2(use_idf=True, random_state=42)

    # Fit on the sample (for IDF weights)
    text_data = df['description'] + ' ' + df['keywords']
    scorer.fit(text_data)

    # Score each company - returns DataFrame with columns: S_cat, S_concdef, V_raw, V_pct, V_minmax
    scores_df = scorer.transform(text_data)

    # Extract V_raw (the main vagueness score before percentile normalization)
    return scores_df['V_raw']


def score_v2_no_idf(df: pd.DataFrame) -> pd.Series:
    """Score using V2 without IDF weighting."""
    logger.info("\n" + "="*60)
    logger.info("VARIANT 3: V2 No IDF (Simpler)")
    logger.info("="*60)

    scorer = StrategicVaguenessScorerV2(use_idf=False, random_state=42)

    text_data = df['description'] + ' ' + df['keywords']
    scorer.fit(text_data)
    scores_df = scorer.transform(text_data)

    return scores_df['V_raw']


def score_v2_minmax(df: pd.DataFrame) -> pd.Series:
    """Score using V2 with min-max normalization instead of percentile."""
    logger.info("\n" + "="*60)
    logger.info("VARIANT 4: V2 Min-Max Normalized")
    logger.info("="*60)

    scorer = StrategicVaguenessScorerV2(use_idf=True, random_state=42)

    text_data = df['description'] + ' ' + df['keywords']
    scorer.fit(text_data)
    scores_df = scorer.transform(text_data)

    # Use V_minmax instead of V_raw
    return scores_df['V_minmax']


def score_concrete_features(df: pd.DataFrame) -> pd.Series:
    """Simple count of concrete features (numbers, dates, metrics)."""
    logger.info("\n" + "="*60)
    logger.info("VARIANT 5: Concrete Feature Count (Inverse)")
    logger.info("="*60)

    def count_concrete_features(text: str) -> float:
        """Count concrete features in text."""
        if pd.isna(text):
            return 0

        text = str(text).lower()
        score = 0

        # Numbers (including percentages, metrics)
        import re
        score += len(re.findall(r'\d+\.?\d*%?', text))

        # Years (2010-2025)
        score += len(re.findall(r'\b20[0-2]\d\b', text))

        # Units (TB, GB, MHz, etc.)
        units = ['tb', 'gb', 'mb', 'kb', 'ghz', 'mhz', 'fps', 'rpm', 'kwh', 'mph', 'kg', 'lbs']
        for unit in units:
            score += text.count(unit)

        # Technical metrics
        metrics = ['latency', 'throughput', 'bandwidth', 'accuracy', 'precision', 'recall']
        for metric in metrics:
            score += text.count(metric)

        return score

    text_data = df['description'] + ' ' + df['keywords']
    concrete_counts = text_data.apply(count_concrete_features)

    # Invert: high concrete = low vagueness
    # Normalize to 0-100 scale
    max_count = concrete_counts.quantile(0.95)  # Cap outliers
    vagueness = 100 - (concrete_counts.clip(0, max_count) / max_count * 100)

    return vagueness


def score_hybrid(df: pd.DataFrame) -> pd.Series:
    """Hybrid: 50% V2 + 50% inverse concrete features."""
    logger.info("\n" + "="*60)
    logger.info("VARIANT 6: Hybrid (V2 + Concrete)")
    logger.info("="*60)

    # Get V2 scores
    scorer = StrategicVaguenessScorerV2(use_idf=True, random_state=42)
    text_data = df['description'] + ' ' + df['keywords']
    scorer.fit(text_data)
    scores_df = scorer.transform(text_data)
    v2_scores = scores_df['V_minmax'].values  # Use V_minmax

    # Get concrete scores
    concrete_scores = score_concrete_features(df).values

    # Combine 50/50
    hybrid = 0.5 * v2_scores + 0.5 * concrete_scores

    return pd.Series(hybrid, index=df.index, name='hybrid')


def analyze_distribution(scores: pd.Series, name: str) -> dict:
    """Analyze score distribution and return statistics."""
    stats = {
        'name': name,
        'mean': scores.mean(),
        'std': scores.std(),
        'min': scores.min(),
        'q25': scores.quantile(0.25),
        'median': scores.median(),
        'q75': scores.quantile(0.75),
        'max': scores.max(),
        'iqr': scores.quantile(0.75) - scores.quantile(0.25),
        'cv': scores.std() / scores.mean() if scores.mean() > 0 else 0,  # Coefficient of variation
        'spike_at_50': (scores == 50.0).sum() / len(scores) * 100,  # % at exactly 50.0
        'spike_at_median': (scores == scores.median()).sum() / len(scores) * 100,  # % at median
    }

    return stats


def print_comparison_table(results: List[dict]):
    """Print comparison table of all variants."""
    logger.info("\n" + "="*80)
    logger.info("COMPARISON TABLE - Vagueness Score Distributions")
    logger.info("="*80)

    header = f"{'Variant':<20} {'Mean':<8} {'Std':<8} {'IQR':<8} {'CV':<8} {'@50%':<8} {'@Med%':<8}"
    logger.info(header)
    logger.info("-"*80)

    for r in results:
        row = (f"{r['name']:<20} "
               f"{r['mean']:>7.2f} "
               f"{r['std']:>7.2f} "
               f"{r['iqr']:>7.2f} "
               f"{r['cv']:>7.3f} "
               f"{r['spike_at_50']:>7.1f} "
               f"{r['spike_at_median']:>7.1f}")
        logger.info(row)

    logger.info("\n📊 Metrics:")
    logger.info("  IQR = Interquartile Range (higher = more spread)")
    logger.info("  CV  = Coefficient of Variation (std/mean, higher = more relative variance)")
    logger.info("  @50% = Percentage of scores exactly at 50.0 (lower is better)")
    logger.info("  @Med% = Percentage at median value (lower = less concentrated)")

    # Recommend best
    logger.info("\n🎯 Recommendation:")
    best_cv = max(results, key=lambda x: x['cv'])
    best_iqr = max(results, key=lambda x: x['iqr'])

    logger.info(f"  Highest variance (CV): {best_cv['name']} (CV={best_cv['cv']:.3f})")
    logger.info(f"  Highest spread (IQR): {best_iqr['name']} (IQR={best_iqr['iqr']:.2f})")

    # Find lowest spike at 50
    least_spike = min(results, key=lambda x: x['spike_at_50'])
    logger.info(f"  Least concentrated: {least_spike['name']} ({least_spike['spike_at_50']:.1f}% at 50.0)")


def plot_distributions(df_scores: pd.DataFrame, output_dir: Path):
    """Plot distribution comparison."""
    output_dir.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    axes = axes.flatten()

    for idx, col in enumerate(df_scores.columns):
        ax = axes[idx]

        # Histogram
        ax.hist(df_scores[col], bins=50, alpha=0.7, color='steelblue', edgecolor='black')

        # Add median line
        median = df_scores[col].median()
        ax.axvline(median, color='red', linestyle='--', linewidth=2, label=f'Median: {median:.1f}')

        # Styling
        ax.set_xlabel('Vagueness Score', fontsize=12)
        ax.set_ylabel('Frequency', fontsize=12)
        ax.set_title(f'{col}\nMean: {df_scores[col].mean():.1f}, Std: {df_scores[col].std():.1f}',
                     fontsize=13, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)

    plt.tight_layout()

    # Save
    output_file = output_dir / 'vagueness_distributions_comparison.png'
    fig.savefig(output_file, dpi=300, bbox_inches='tight')
    logger.info(f"\n📊 Distribution plot saved: {output_file}")

    plt.close(fig)


def main():
    """Run all variant tests."""
    logger.info("="*80)
    logger.info("VAGUENESS SCORER VARIANT TESTING")
    logger.info("="*80)

    # Load sample data
    df = load_sample_data(n_samples=10000)
    if df is None:
        return 1

    # Test all variants
    variants = [
        ('V1 (Current)', score_v1),
        ('V2 Standard (IDF)', score_v2_standard),
        ('V2 No IDF', score_v2_no_idf),
        ('V2 MinMax', score_v2_minmax),
        ('Concrete Features', score_concrete_features),
        ('Hybrid V2+Concrete', score_hybrid),
    ]

    df_scores = pd.DataFrame(index=df.index)
    results = []

    for name, scorer_func in variants:
        try:
            scores = scorer_func(df)
            df_scores[name] = scores

            # Analyze
            stats = analyze_distribution(scores, name)
            results.append(stats)

            # Print quick stats
            logger.info(f"  Mean: {stats['mean']:.2f}, Std: {stats['std']:.2f}, "
                       f"IQR: {stats['iqr']:.2f}, Spike@50: {stats['spike_at_50']:.1f}%")

        except Exception as e:
            logger.error(f"❌ {name} failed: {e}")
            import traceback
            traceback.print_exc()

    # Print comparison table
    print_comparison_table(results)

    # Plot distributions
    output_dir = Path("experiments/outputs")
    plot_distributions(df_scores, output_dir)

    # Save detailed results
    output_file = output_dir / 'vagueness_variants_sample.csv'
    df_scores.to_csv(output_file, index=False)
    logger.info(f"\n💾 Sample scores saved: {output_file}")

    stats_file = output_dir / 'vagueness_variants_stats.csv'
    pd.DataFrame(results).to_csv(stats_file, index=False)
    logger.info(f"💾 Statistics saved: {stats_file}")

    logger.info("\n" + "="*80)
    logger.info("✓ TESTING COMPLETE")
    logger.info("="*80)

    return 0


if __name__ == '__main__':
    sys.exit(main())
