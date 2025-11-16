#!/bin/bash
# run_all.sh - One-touch execution: INPUT → PRODUCTION → OUTPUT
# Author: 권준/나대용 (中軍)

set -e  # Exit on error

echo "🚀 Starting thesis pipeline..."

# 1. Theory figures
echo "📊 [1/3] Generating Theory figures..."
cd 2️⃣_PRODUCTION/Theory
python3 run.py
cd ../..

# 2. Empirics_Early analysis
echo "📊 [2/3] Running H1 tests..."
cd 2️⃣_PRODUCTION/Empirics_Early
python3 run.py
cd ../..

# 3. Empirics_Later analysis
echo "📊 [3/3] Running H2 tests..."
cd 2️⃣_PRODUCTION/Empirics_Later
python3 run.py
cd ../..

echo "✅ Pipeline complete. Outputs in 3️⃣_OUTPUT/"
ls -lh 3️⃣_OUTPUT/figures/
ls -lh 3️⃣_OUTPUT/tables/
