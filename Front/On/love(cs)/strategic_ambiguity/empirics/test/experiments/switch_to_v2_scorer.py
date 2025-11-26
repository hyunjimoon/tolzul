#!/usr/bin/env python3
"""
Switch Feature Engineering to V2 Scorer
========================================
This script updates src/features.py to use StrategicVaguenessScorerV2
instead of the old V1 scorer.

Problem:
- src/features.py currently uses StrategicVaguenessScorer (V1)
- This produces 75% of companies with vagueness = 50.0
- V2 should provide better variance

Solution:
- Replace _SCORER = StrategicVaguenessScorer() with V2
- Update compute_vagueness_vectorized() to use V2's API

Usage:
    python3 experiments/switch_to_v2_scorer.py
"""

import sys
from pathlib import Path

def main():
    features_file = Path("src/features.py")

    if not features_file.exists():
        print(f"❌ File not found: {features_file}")
        return 1

    print("="*80)
    print("SWITCHING TO V2 VAGUENESS SCORER")
    print("="*80)
    print()

    # Read current file
    with open(features_file, 'r') as f:
        content = f.read()

    # Check if already using V2
    if 'StrategicVaguenessScorerV2' in content:
        print("✓ Already using V2 scorer!")
        print()
        return 0

    # Make changes
    changes_made = []

    # 1. Add V2 import at top
    if 'from vagueness_v2 import StrategicVaguenessScorerV2' not in content:
        # Find import section
        import_line = "import numpy as np"
        if import_line in content:
            content = content.replace(
                import_line,
                f"{import_line}\nfrom vagueness_v2 import StrategicVaguenessScorerV2"
            )
            changes_made.append("Added V2 import")

    # 2. Replace scorer instance
    old_scorer = "_SCORER = StrategicVaguenessScorer()"
    new_scorer = (
        "# V2 Scorer: 2-component model (categorical + concreteness deficit)\n"
        "_SCORER_V2 = StrategicVaguenessScorerV2(use_idf=True, random_state=42)\n"
        "_SCORER_V2_FITTED = False  # Track if scorer has been fit"
    )

    if old_scorer in content:
        content = content.replace(old_scorer, new_scorer)
        changes_made.append("Replaced V1 scorer instance with V2")

    # 3. Update compute_vagueness_vectorized function
    old_function = '''def compute_vagueness_vectorized(descriptions: pd.Series, keywords: pd.Series) -> pd.Series:
    """
    Vectorized wrapper for StrategicVaguenessScorer using both inputs.
    """
    # Combine into a temporary DataFrame to handle alignment and missing values
    temp_df = pd.DataFrame({'description': descriptions, 'keywords': keywords})

    return temp_df.apply(
        lambda row: _SCORER.score_vagueness(row['description'], row['keywords']),
        axis=1
    )'''

    new_function = '''def compute_vagueness_vectorized(descriptions: pd.Series, keywords: pd.Series) -> pd.Series:
    """
    Vectorized wrapper for StrategicVaguenessScorerV2 using both inputs.

    V2 Improvements:
    - 2-component model (categorical vagueness + concreteness deficit)
    - IDF weighting for abstract terms
    - Better variance (less concentration at 50.0)
    - Returns V_minmax (min-max normalized 0-100 score)
    """
    global _SCORER_V2_FITTED

    # Combine description and keywords
    text_data = (descriptions.fillna('') + ' ' + keywords.fillna(''))

    # Fit on first call (IDF weights need corpus)
    if not _SCORER_V2_FITTED:
        print("  🔧 Fitting V2 vagueness scorer on corpus (one-time)...")
        _SCORER_V2.fit(text_data)
        _SCORER_V2_FITTED = True
        print("  ✅ V2 scorer fitted")

    # Transform to get scores
    # Returns: [S_cat, S_concdef, V_raw, V_pct, V_minmax]
    scores = _SCORER_V2.transform(text_data)

    # Use V_minmax (column 4) - min-max normalized 0-100
    return pd.Series(scores[:, 4], index=descriptions.index, name='vagueness')'''

    if old_function in content:
        content = content.replace(old_function, new_function)
        changes_made.append("Updated compute_vagueness_vectorized() to use V2 API")

    # Save modified file
    if changes_made:
        # Backup original
        backup_file = features_file.with_suffix('.py.backup')
        print(f"📝 Creating backup: {backup_file}")
        with open(backup_file, 'w') as f:
            # Read original again to backup
            with open(features_file, 'r') as orig:
                f.write(orig.read())

        # Write modified
        with open(features_file, 'w') as f:
            f.write(content)

        print(f"✅ Updated {features_file}")
        print()
        print("Changes made:")
        for change in changes_made:
            print(f"  ✓ {change}")
        print()
        print("⚠️  IMPORTANT: Re-run feature engineering to use V2:")
        print("  rm data/processed/features_all.parquet")
        print("  python3 pipeline/02_engineer_features.py")
        print()
        print("To restore original:")
        print(f"  mv {backup_file} {features_file}")
        print()

    else:
        print("⚠️  No changes needed - file may already be updated")
        print()

    return 0


if __name__ == '__main__':
    sys.exit(main())
