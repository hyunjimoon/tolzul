#!/bin/bash
################################################################################
# Diagnose Pipeline Outputs
# ==========================
# Check what the pipeline actually created
################################################################################

echo "═══════════════════════════════════════════════════════════════════"
echo "PIPELINE OUTPUT DIAGNOSTICS"
echo "═══════════════════════════════════════════════════════════════════"
echo ""

# Check each dataset
for dataset in all quantum transportation; do
    echo "───────────────────────────────────────────────────────────────────"
    echo "Dataset: $dataset"
    echo "───────────────────────────────────────────────────────────────────"

    base_dir="outputs/$dataset"

    # Check if directory exists
    if [ ! -d "$base_dir" ]; then
        echo "  ❌ Directory doesn't exist: $base_dir"
        continue
    fi

    # Check dataset file
    if [ -f "$base_dir/dataset.parquet" ]; then
        size=$(du -h "$base_dir/dataset.parquet" | cut -f1)
        echo "  ✓ Dataset file: $size"
    else
        echo "  ❌ No dataset.parquet"
    fi

    # Check models directory
    models_dir="$base_dir/models"
    if [ -d "$models_dir" ]; then
        echo "  ✓ Models directory exists"

        # Check H1 outputs
        if [ -f "$models_dir/h1_coefficients.csv" ]; then
            rows=$(wc -l < "$models_dir/h1_coefficients.csv")
            echo "    ✓ H1 coefficients: $rows rows"
        else
            echo "    ❌ No H1 coefficients"
        fi

        # Check H2 outputs
        if [ -f "$models_dir/h2_main_coefficients.csv" ]; then
            rows=$(wc -l < "$models_dir/h2_main_coefficients.csv")
            echo "    ✓ H2 coefficients: $rows rows"
        else
            echo "    ❌ No H2 coefficients"
        fi

        if [ -f "$models_dir/h2_analysis_dataset.csv" ]; then
            rows=$(wc -l < "$models_dir/h2_analysis_dataset.csv")
            echo "    ✓ H2 analysis dataset: $rows rows"
        else
            echo "    ❌ No H2 analysis dataset (needed for plots)"
        fi
    else
        echo "  ❌ No models/ directory"
    fi

    # Check figures directory
    figures_dir="$base_dir/figures"
    if [ -d "$figures_dir" ]; then
        count=$(ls -1 "$figures_dir"/*.png 2>/dev/null | wc -l)
        echo "  ✓ Figures directory exists: $count PNG files"
    else
        echo "  ❌ No figures/ directory"
    fi

    echo ""
done

echo "═══════════════════════════════════════════════════════════════════"
echo "SUMMARY"
echo "═══════════════════════════════════════════════════════════════════"
echo ""
echo "Expected structure for each dataset:"
echo "  outputs/{dataset}/"
echo "    ├── dataset.parquet           ← From Step 3 (filtering)"
echo "    ├── models/"
echo "    │   ├── h1_coefficients.csv   ← From Step 4 (H1 model)"
echo "    │   ├── h2_main_coefficients.csv  ← From Step 4 (H2 model)"
echo "    │   └── h2_analysis_dataset.csv   ← From Step 4 (for plotting)"
echo "    └── figures/"
echo "        └── F3a_interaction.png   ← From Step 5 (plots)"
echo ""
echo "If models/ or figures/ are missing, re-run those steps:"
echo "  python3 pipeline/04_run_models.py all"
echo "  python3 pipeline/05_generate_plots.py all"
echo ""
