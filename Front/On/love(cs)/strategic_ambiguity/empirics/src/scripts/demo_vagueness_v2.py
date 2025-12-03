"""
Demo: Strategic Vagueness Scorer V2

Shows the two-component vagueness measure on diverse example texts.
"""

import pandas as pd
from vagueness import StrategicVaguenessScorerV2


def main():
    print("="*80)
    print("Strategic Vagueness Scorer V2 - Demo")
    print("Two-component measure: Categorical Vagueness + Concreteness Deficit")
    print("="*80)

    # Example texts with varying levels of vagueness
    examples = [
        {
            'id': 1,
            'category': 'Highly Abstract (Marketing)',
            'text': (
                "We leverage our innovative platform solution ecosystem to deliver "
                "next-generation digital transformation services with seamless "
                "integration and enterprise-grade infrastructure."
            )
        },
        {
            'id': 2,
            'category': 'Highly Specific (LED Hardware)',
            'text': (
                "Our phosphor materials achieve 6500K CCT, 95% CRI, and 85% efficacy. "
                "Production pilot in Q3 2024 with 100kg/month capacity at 98% yield."
            )
        },
        {
            'id': 3,
            'category': 'Mixed (Quantum Computing)',
            'text': (
                "Superconducting qubit processors with 20μs coherence time and "
                "error rates below 0.1%. QEC milestone scheduled for Q3 2025; v1.2 SDK."
            )
        },
        {
            'id': 4,
            'category': 'Moderate Vagueness (Solar)',
            'text': (
                "Our solar panels utilize advanced silicon technology for improved "
                "efficiency. The innovative design delivers enhanced performance "
                "in various conditions with 25-year warranty."
            )
        },
        {
            'id': 5,
            'category': 'Technical (Semiconductor)',
            'text': (
                "5nm FinFET process node delivering 3GHz clock speed with 150W TDP. "
                "Benchmark: 15000 Geekbench multi-core, published Q1 2024. "
                "Commercial samples available March 2024."
            )
        },
        {
            'id': 6,
            'category': 'Abstract (Business Consulting)',
            'text': (
                "Transformative strategic framework enabling holistic business optimization "
                "through synergistic value-added solutions and best-in-class methodologies "
                "that empower organizations to achieve world-class outcomes."
            )
        },
        {
            'id': 7,
            'category': 'Specific (Battery)',
            'text': (
                "Lithium iron phosphate cells: 3.2V nominal, 280Ah capacity, "
                "5000 cycles at 80% DOD. Operating range -20°C to 60°C. "
                "UL9540A certified, production Q2 2024."
            )
        },
        {
            'id': 8,
            'category': 'Mixed (AI Chip)',
            'text': (
                "Neural processing unit delivering 400TOPS at 7nm node with "
                "innovative architecture for efficient AI workloads. Supports "
                "framework integration with comprehensive SDK v2.0."
            )
        },
        {
            'id': 9,
            'category': 'Vague (Generic Tech)',
            'text': (
                "Cloud-based platform offering scalable solutions with cutting-edge "
                "technology and robust infrastructure for seamless integration "
                "across enterprise environments."
            )
        },
        {
            'id': 10,
            'category': 'Specific (Biotech)',
            'text': (
                "mRNA vaccine candidate targeting spike protein RBD. Phase 2 trial "
                "N=450, 89% efficacy (95% CI: 82-94%). Results published Nature Medicine "
                "Feb 2024. FDA submission Q4 2024."
            )
        },
    ]

    # Extract texts
    texts = [ex['text'] for ex in examples]
    categories = [ex['category'] for ex in examples]
    ids = [ex['id'] for ex in examples]

    # Create scorer and compute scores
    print("\nComputing vagueness scores...\n")
    scorer = StrategicVaguenessScorerV2()
    results = scorer.fit_transform(texts)

    # Combine with metadata
    df = pd.DataFrame({
        'ID': ids,
        'Category': categories,
        'Text': [t[:60] + '...' if len(t) > 60 else t for t in texts],
        'S_cat': results['S_cat'].round(1),
        'S_concdef': results['S_concdef'].round(1),
        'V_raw': results['V_raw'].round(1),
        'V_pct': results['V_pct'].round(1),
    })

    # Display results
    print("Results:")
    print("-" * 80)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 120)
    pd.set_option('display.max_colwidth', 50)
    print(df.to_string(index=False))
    print("-" * 80)

    # Summary statistics
    print("\nSummary Statistics:")
    print("-" * 80)
    summary = df[['S_cat', 'S_concdef', 'V_raw', 'V_pct']].describe()
    print(summary.round(1))
    print("-" * 80)

    # Distribution analysis
    print("\nDistribution Analysis:")
    print(f"  V_raw range: [{df['V_raw'].min():.1f}, {df['V_raw'].max():.1f}]")
    print(f"  V_raw mean: {df['V_raw'].mean():.1f}, std: {df['V_raw'].std():.1f}")
    print(f"  P10: {df['V_raw'].quantile(0.1):.1f}, P90: {df['V_raw'].quantile(0.9):.1f}")
    print(f"  Spread (P90-P10): {df['V_raw'].quantile(0.9) - df['V_raw'].quantile(0.1):.1f}")

    # Show extreme cases
    print("\nExtreme Cases:")
    print("-" * 80)
    print("Most Vague (highest V_raw):")
    top_vague = df.nlargest(3, 'V_raw')[['ID', 'Category', 'V_raw', 'S_cat', 'S_concdef']]
    print(top_vague.to_string(index=False))

    print("\nMost Specific (lowest V_raw):")
    least_vague = df.nsmallest(3, 'V_raw')[['ID', 'Category', 'V_raw', 'S_cat', 'S_concdef']]
    print(least_vague.to_string(index=False))
    print("-" * 80)

    # Component correlation
    print("\nComponent Correlation:")
    corr = df[['S_cat', 'S_concdef', 'V_raw']].corr()
    print(corr.round(2))
    print("-" * 80)

    print("\n✓ Demo completed successfully!")
    print("\nKey Insights:")
    print("  • S_cat captures abstract/categorical language")
    print("  • S_concdef penalizes absence of specifics (numbers, specs, dates)")
    print("  • V_raw = 0.5*max(S_cat,S_concdef) + 0.5*mean(S_cat,S_concdef)")
    print("  • V_pct provides percentile ranking for modeling")
    print("  • Lexical uncertainty component has been REMOVED per research spec")


if __name__ == "__main__":
    main()
