#!/bin/bash

# Auto-commit script for Scale Dashboard
# Runs every hour to commit changes to the dashboard.

while true; do
    echo "⏰ [$(date)] Checking for changes..."
    
    # Check if there are changes to commit
    if [[ -n $(git status -s) ]]; then
        echo "📝 Changes detected. Committing..."
        git add .
        git commit -m "chore(auto): Hourly dashboard update [$(date +'%Y-%m-%d %H:%M')]"
        git push
        echo "✅ Changes pushed to remote."
    else
        echo "💤 No changes to commit."
    fi
    
    # Wait for 1 hour (3600 seconds)
    echo "⏳ Waiting for next cycle (1 hour)..."
    sleep 3600
done
