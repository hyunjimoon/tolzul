#!/bin/bash

# Configuration
BASE_DIR="/Users/hyunjimoon/tolzul"
LOG_FILE="$BASE_DIR/mission_control.log"
PYTHON_EXEC=$(which python3)

# Start Log
echo "========================================" >> "$LOG_FILE"
echo "🚀 Mission Start: $(date)" >> "$LOG_FILE"

# Navigate to directory
cd "$BASE_DIR"

# Run Operation (Analysis + Dashboard Generation)
echo "⚙️ Running operate_spaceship.py..." >> "$LOG_FILE"
"$PYTHON_EXEC" operate_spaceship.py >> "$LOG_FILE" 2>&1

# Check Status
if [ $? -eq 0 ]; then
    echo "✅ Mission Success: $(date)" >> "$LOG_FILE"
else
    echo "❌ Mission Failed: $(date)" >> "$LOG_FILE"
fi
echo "========================================" >> "$LOG_FILE"
