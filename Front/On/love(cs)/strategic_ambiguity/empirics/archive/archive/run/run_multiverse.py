#!/usr/bin/env python3
"""
Multiverse Analysis CLI

Executes complete multiverse analysis across specification grid,
testing vagueness → funding/success hypotheses.

Usage:
    python run_multiverse.py --input data.csv --outdir results/
"""

import argparse
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
from pathlib import Path
from multiverse_engine import (
    filter_window, create_moderators, apply_scaling,
    build_formula, fit_specification, compute_evidence,
    plot_multiverse_heatmap, plot_specification_curve,
    EXPECTED_SIGNS, STAGE_MAP
)

# Set random seed for reproducibility
np.random.seed(42)

# ============================================================================
# SPECIFICATION GRID
# ============================================================================

COORDS = {
    "stage": ["E", "L1", "L2"],
    # E=Early(OLS), L1=Later(Logit,VC-only), L2=Later(Logit,VC+IPO)

    "window": [
        ("2022-06", "2024-12"),
        ("2022-06", "2025-11"),
        ("2021-12", "2024-06")
    ],

    "scaling": ["zscore", "winsor99_z"],
    "moderator": ["isSoftware"],  # Only use moderators present in dataset

    # Control toggles
    "ctrl_employee": [0, 1],
    "ctrl_region": [0, 1],
    "ctrl_founder": [0, 1],
    "ctrl_earlyfund": [0, 1]  # H2 only
}


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def run_multiverse(input_path: str, outdir: str, verbose: bool = True) -> None:
    """
    Execute complete multiverse analysis.

    Parameters
    ----------
    input_path : str
        Path to input CSV file
    outdir : str
        Output directory for results
    verbose : bool
        Print progress messages
    """
    if verbose:
        print(f"🚀 Loading data from {input_path}...")

    df = pd.read_csv(input_path, encoding='utf-8')

    if verbose:
        print(f"   Loaded {len(df)} observations")
        print(f"   Columns: {list(df.columns)}\n")

    results = []
    total_specs = (len(COORDS['stage']) * len(COORDS['window']) *
                   len(COORDS['scaling']) * len(COORDS['moderator']) *
                   len(COORDS['ctrl_employee']) * len(COORDS['ctrl_region']) *
                   len(COORDS['ctrl_founder']) * len(COORDS['ctrl_earlyfund']))

    if verbose:
        print(f"🔬 Running {total_specs} specifications across multiverse...\n")

    spec_count = 0

    for stage in COORDS['stage']:
        for window in COORDS['window']:
            for moderator in COORDS['moderator']:
                for scaling in COORDS['scaling']:
                    for ctrl_emp in COORDS['ctrl_employee']:
                        for ctrl_reg in COORDS['ctrl_region']:
                            for ctrl_fnd in COORDS['ctrl_founder']:
                                for ctrl_efc in COORDS['ctrl_earlyfund']:

                                    spec_count += 1

                                    if verbose and spec_count % 50 == 0:
                                        pct = 100 * spec_count / total_specs
                                        print(f"   Progress: {spec_count}/{total_specs} ({pct:.1f}%)")

                                    # Data pipeline
                                    d = filter_window(df, window)
                                    d = create_moderators(d)
                                    d = apply_scaling(d, scaling)

                                    # Build formula
                                    formula = build_formula(
                                        stage, moderator,
                                        ctrl_emp, ctrl_reg, ctrl_fnd, ctrl_efc, d
                                    )

                                    # Fit model
                                    res = fit_specification(d, stage, formula)

                                    # Expected signs
                                    exp_vag = EXPECTED_SIGNS['vag_main'][stage]
                                    exp_opt = EXPECTED_SIGNS['vagXoption']
                                    exp_sw = EXPECTED_SIGNS['vagXsoftware']

                                    # Compute evidence metrics
                                    ev_vag, cons_vag, surp_vag = compute_evidence(
                                        res['coef_vag_main'], res['p_vag_main'], exp_vag
                                    )
                                    ev_opt, cons_opt, surp_opt = compute_evidence(
                                        res['coef_vagXoption'], res['p_vagXoption'], exp_opt
                                    )
                                    ev_sw, cons_sw, surp_sw = compute_evidence(
                                        res['coef_vagXsoftware'], res['p_vagXsoftware'], exp_sw
                                    )

                                    # Store results
                                    # Convert window tuple to string for NetCDF compatibility
                                    window_str = f"{window[0]}_to_{window[1]}"

                                    results.append({
                                        'stage': stage,
                                        'window': window_str,
                                        'moderator': moderator,
                                        'scaling': scaling,
                                        'ctrl_employee': ctrl_emp,
                                        'ctrl_region': ctrl_reg,
                                        'ctrl_founder': ctrl_fnd,
                                        'ctrl_earlyfund': ctrl_efc,
                                        **res,
                                        'expected_sign_vag_main': exp_vag,
                                        'expected_sign_vagXoption': exp_opt,
                                        'expected_sign_vagXsoftware': exp_sw,
                                        'evidence_score_vag_main': ev_vag,
                                        'evidence_score_vagXoption': ev_opt,
                                        'evidence_score_vagXsoftware': ev_sw,
                                        'is_consistent_vag_main': cons_vag,
                                        'is_consistent_vagXoption': cons_opt,
                                        'is_consistent_vagXsoftware': cons_sw,
                                        'is_surprise_vag_main': surp_vag,
                                        'is_surprise_vagXoption': surp_opt,
                                        'is_surprise_vagXsoftware': surp_sw
                                    })

    if verbose:
        print(f"\n✓ Completed {total_specs} specifications")

    # Convert to xarray Dataset
    if verbose:
        print("\n📊 Building xarray Dataset...")

    df_results = pd.DataFrame(results)

    # Set multi-index and convert to xarray
    ds = df_results.set_index(list(COORDS.keys())).to_xarray()

    # Create output directory
    outdir_path = Path(outdir)
    outdir_path.mkdir(exist_ok=True, parents=True)

    # Save outputs
    if verbose:
        print(f"\n💾 Saving results to {outdir}/")

    # 1. NetCDF file
    nc_path = outdir_path / 'multiverse_results.nc'
    ds.to_netcdf(nc_path)
    if verbose:
        print(f"   ✓ {nc_path.name}")

    # 2. CSV table
    csv_path = outdir_path / 'spec_table.csv'
    df_results.to_csv(csv_path, index=False)
    if verbose:
        print(f"   ✓ {csv_path.name}")

    # 3. Summary statistics
    summary_path = outdir_path / 'summary_stats.txt'
    with open(summary_path, 'w') as f:
        f.write("MULTIVERSE ANALYSIS SUMMARY\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total specifications: {len(df_results)}\n\n")

        for effect in ['vag_main', 'vagXoption', 'vagXsoftware']:
            f.write(f"\n{effect.upper()}:\n")
            f.write("-" * 40 + "\n")

            cons_col = f'is_consistent_{effect}'
            surp_col = f'is_surprise_{effect}'

            n_consistent = df_results[cons_col].sum()
            n_surprise = df_results[surp_col].sum()
            pct_consistent = 100 * n_consistent / len(df_results)
            pct_surprise = 100 * n_surprise / len(df_results)

            f.write(f"Consistent with hypothesis: {n_consistent} ({pct_consistent:.1f}%)\n")
            f.write(f"Significant surprises: {n_surprise} ({pct_surprise:.1f}%)\n")

            # Mean evidence score
            ev_col = f'evidence_score_{effect}'
            mean_ev = df_results[ev_col].mean()
            f.write(f"Mean evidence score: {mean_ev:.2f}\n")

    if verbose:
        print(f"   ✓ {summary_path.name}")

    # 4. Visualizations
    if verbose:
        print("\n📈 Generating visualizations...")

    # Heatmap for H1 (early stage vagueness)
    try:
        fig = plot_multiverse_heatmap(ds, 'evidence_score_vag_main', expected_sign=-1)
        fig.savefig(outdir_path / 'multiverse_h1_heatmap.png', dpi=300, bbox_inches='tight')
        if verbose:
            print("   ✓ multiverse_h1_heatmap.png")
        plt.close(fig)
    except Exception as e:
        if verbose:
            print(f"   ⚠ H1 heatmap failed: {e}")

    # Specification curve for H1
    try:
        fig = plot_specification_curve(ds, 'evidence_score_vag_main', expected_sign=-1)
        fig.savefig(outdir_path / 'spec_curve_h1.png', dpi=300, bbox_inches='tight')
        if verbose:
            print("   ✓ spec_curve_h1.png")
        plt.close(fig)
    except Exception as e:
        if verbose:
            print(f"   ⚠ H1 spec curve failed: {e}")

    # Heatmap for H2 interactions
    try:
        fig = plot_multiverse_heatmap(ds, 'evidence_score_vagXoption', expected_sign=+1)
        fig.savefig(outdir_path / 'multiverse_h2_option_heatmap.png', dpi=300, bbox_inches='tight')
        if verbose:
            print("   ✓ multiverse_h2_option_heatmap.png")
        plt.close(fig)
    except Exception as e:
        if verbose:
            print(f"   ⚠ H2 option heatmap failed: {e}")

    try:
        fig = plot_multiverse_heatmap(ds, 'evidence_score_vagXsoftware', expected_sign=+1)
        fig.savefig(outdir_path / 'multiverse_h2_software_heatmap.png', dpi=300, bbox_inches='tight')
        if verbose:
            print("   ✓ multiverse_h2_software_heatmap.png")
        plt.close(fig)
    except Exception as e:
        if verbose:
            print(f"   ⚠ H2 software heatmap failed: {e}")

    if verbose:
        print(f"\n{'=' * 60}")
        print("✅ MULTIVERSE ANALYSIS COMPLETE")
        print(f"{'=' * 60}")
        print(f"\nResults saved to: {outdir_path.absolute()}\n")
        print("必死則生 🐢🐅\n")


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description='Run multiverse analysis for vagueness → funding/success hypotheses',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python run_multiverse.py --input data/startups.csv --outdir results/
    python run_multiverse.py --input data.csv --outdir output/ --quiet
        """
    )

    parser.add_argument(
        '--input',
        required=True,
        help='Path to input CSV file'
    )

    parser.add_argument(
        '--outdir',
        default='outputs/',
        help='Output directory for results (default: outputs/)'
    )

    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress progress messages'
    )

    args = parser.parse_args()

    run_multiverse(args.input, args.outdir, verbose=not args.quiet)


if __name__ == '__main__':
    main()
