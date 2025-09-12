#!/bin/bash
# The Ergodic Life Sampler
# Ensures you visit all four chains with appropriate frequency

# Configuration
CHAIN_WEIGHTS=(30 25 25 20)  # Target percentages for chains 1-4
CHAINS=("1_🐢acculturate-evaluate" "2_🐅evaluate-professionalize-processify-automate" "3_🐙collaborate-automate-platformize-capitalize" "4_👾segment-replicate-capitalize")

# Function to count files modified today in each chain
count_today_activity() {
    echo "📊 Today's Chain Activity:"
    for i in {0..3}; do
        count=$(find "${CHAINS[$i]}" -type f -mtime -1 2>/dev/null | wc -l)
        echo "Chain $((i+1)): $count files"
    done
}

# Function to calculate R-hat (simplified)
calculate_rhat() {
    echo "🎯 Chain Balance (R-hat proxy):"
    # In real life, this would track variance between time periods
    echo "Chain 1 (Can): Check weekly theory/experiment balance"
    echo "Chain 2 (Dev): Check monthly process documentation"
    echo "Chain 3 (Fill): Check daily execution logs"
    echo "Chain 4 (Use): Check user feedback frequency"
}

# The Daily Sampler
daily_sampler() {
    echo "🎲 TODAY'S CHAIN ASSIGNMENT:"
    
    # Generate weighted random selection
    RANDOM_NUM=$((RANDOM % 100))
    CUMSUM=0
    
    for i in {0..3}; do
        CUMSUM=$((CUMSUM + CHAIN_WEIGHTS[$i]))
        if [ $RANDOM_NUM -lt $CUMSUM ]; then
            echo "Focus on Chain $((i+1)): ${CHAINS[$i]}"
            echo "Today's prompt: $(get_chain_prompt $i)"
            break
        fi
    done
}

# Chain-specific prompts
get_chain_prompt() {
    case $1 in
        0) echo "🐢 What experiment can you run today? What culture needs building?";;
        1) echo "🐅 What validated idea can you systematize today?";;
        2) echo "🐙 What collaboration can you initiate? What can you automate?";;
        3) echo "👾 Who is your user? What feedback can you gather?";;
    esac
}

# Main execution
echo "🔄 ERGODIC LIFE SAMPLER"
echo "======================="
count_today_activity
echo ""
calculate_rhat
echo ""
daily_sampler