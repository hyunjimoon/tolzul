#!/usr/bin/env python3
"""
Life Spaceship Operator
=======================

"Operate the spaceship of life with Strategic Ambiguity."

This script analyzes your daily notes to help you tune the rhythm of:
- Space (Morning/Ear): High Vagueness (Exploration)
- Front (Day/Eye): Low Vagueness (Execution)
- Balance (Evening/Hand): Control

Usage:
    python operate_spaceship.py
"""

import sys
import os
import glob
import re
from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np

# --- Configuration ---
BASE_DIR = Path("/Users/hyunjimoon/tolzul")
DAILY_NOTES_DIR = BASE_DIR / "Balance/Daily_Rhythm"
EMPIRICS_SRC = BASE_DIR / "Front/On/love(cs)/strategic_ambiguity/empirics/src"

# Add empirics source to path to import scorer
sys.path.append(str(EMPIRICS_SRC))

try:
    from vagueness_v2 import StrategicVaguenessScorerV2
except ImportError:
    print(f"Error: Could not import StrategicVaguenessScorerV2 from {EMPIRICS_SRC}")
    print("Please check the path and ensure the file exists.")
    sys.exit(1)

# --- Spaceship Operator ---

class LifeSpaceshipOperator:
    def __init__(self):
        self.scorer = StrategicVaguenessScorerV2(use_idf=False) # No IDF for single user notes usually better, or maybe True if we load many
        # Let's use IDF=False for now as we might not have a huge corpus loaded at once to make IDF meaningful, 
        # or we can load all notes to build IDF. Let's try loading all notes for IDF.
        self.scorer_idf = StrategicVaguenessScorerV2(use_idf=True)
        self.notes = []

    def load_daily_notes(self, limit=30):
        """Load the most recent daily notes."""
        files = sorted(glob.glob(str(DAILY_NOTES_DIR / "*.md")), reverse=True)
        files = files[:limit]
        
        print(f"📂 Loading {len(files)} recent daily notes from {DAILY_NOTES_DIR}...")
        
        data = []
        for f in files:
            path = Path(f)
            try:
                date_str = path.stem.split(' ')[0] # Handle "2025-10-16" or "2025-08-05-..."
                # Try to parse date
                try:
                    date = datetime.strptime(date_str[:10], "%Y-%m-%d").date()
                except ValueError:
                    continue
                
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                data.append({
                    'date': date,
                    'filename': path.name,
                    'content': content
                })
            except Exception as e:
                print(f"  ⚠️ Error reading {path.name}: {e}")
        
        self.notes = pd.DataFrame(data)
        if not self.notes.empty:
            self.notes = self.notes.sort_values('date', ascending=False)
            
            # Fit the scorer on all content to learn IDF (if we want to use it)
            # Combining all content for fitting
            all_texts = self.notes['content'].tolist()
            self.scorer_idf.fit(all_texts)
            
        return self.notes

    def analyze_rhythm(self):
        """Analyze the vagueness of the notes."""
        if self.notes.empty:
            print("No notes to analyze.")
            return

        print("\n🚀 Analyzing Life Spaceship Rhythm...")
        
        # Calculate scores
        texts = self.notes['content'].tolist()
        scores = self.scorer_idf.transform(texts)
        
        # Merge back
        results = pd.concat([self.notes.reset_index(drop=True), scores], axis=1)
        
        # Display Report
        print("\n" + "="*60)
        print(f"🌌 FLIGHT REPORT (Last {len(results)} Days)")
        print("="*60)
        print(f"{'Date':<12} | {'V_raw':<6} | {'S_cat':<6} | {'S_conc':<6} | {'Signal'}")
        print("-" * 60)
        
        for _, row in results.iterrows():
            date_str = row['date'].strftime("%Y-%m-%d")
            v_raw = row['V_raw']
            s_cat = row['S_cat']
            s_conc = row['S_concdef']
            
            # Interpret Signal
            # High V -> Space/Exploration
            # Low V -> Front/Execution
            if v_raw > 60:
                signal = "👂 Space (Exploring)"
            elif v_raw < 40:
                signal = "👁 Front (Executing)"
            else:
                signal = "✋ Balance (Tuning)"
                
            print(f"{date_str:<12} | {v_raw:6.1f} | {s_cat:6.1f} | {s_conc:6.1f} | {signal}")
            
        print("-" * 60)
        
        # Weekly Averages
        print("\n📊 Weekly Averages:")
        results['week'] = pd.to_datetime(results['date']).dt.to_period('W')
        weekly = results.groupby('week')[['V_raw', 'S_cat', 'S_concdef']].mean().sort_index(ascending=False)
        print(weekly)

        # Save to CSV for visualization
        output_path = BASE_DIR / "spaceship_data.csv"
        results.to_csv(output_path, index=False)
        print(f"\n💾 Data saved to {output_path}")

        # Recommendation
        recent_v = results.iloc[0]['V_raw']
        print("\n💡 Pilot Recommendation:")
        if recent_v > 70:
            print("  ⚠️ High Vagueness detected. Ensure you are converging to action (Front).")
            print("     \"Neurons that fire together, wire together.\" - Make it concrete.")
        elif recent_v < 30:
            print("  ⚠️ Low Vagueness detected. Don't forget to listen to the White Space (Space).")
            print("     \"Preserve uncertainty.\" - Expand your options.")
        else:
            print("  ✅ Good Balance. You are tuning the rhythm well.")

        # Trigger Visualization
        print("\n🎨 Updating Dashboard...")
        try:
            import subprocess
            subprocess.run([sys.executable, str(BASE_DIR / "visualize_spaceship.py")], check=True)
        except Exception as e:
            print(f"⚠️ Failed to update dashboard: {e}")

if __name__ == "__main__":
    operator = LifeSpaceshipOperator()
    operator.load_daily_notes(limit=365) # Load more history for visualization
    operator.analyze_rhythm()
