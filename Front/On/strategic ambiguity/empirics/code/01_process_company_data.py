"""
Script 01: Process Company Data from Pitchbook
Input: data/raw/Company*.dat (pipe-delimited files)
Output: data/processed/company_master.csv

Steps:
1. Read Company data files
2. Filter to AI/ML firms based on keywords
3. Score vagueness using keyword counts
4. Classify integration cost from Keywords field
5. Create company master file
"""

import pandas as pd
import os
from pathlib import Path

# Setup paths
BASE_DIR = Path(__file__).parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("SCRIPT 01: PROCESS COMPANY DATA")
print("=" * 80)

# Step 1: Read Company data files
print("\n[Step 1] Reading Company data files...")
company_files = list(RAW_DATA_DIR.glob("Company*.dat"))
print(f"Found {len(company_files)} Company files: {[f.name for f in company_files]}")

dfs = []
for file in company_files:
    df = pd.read_csv(file, sep='|', encoding='utf-8')
    dfs.append(df)
    print(f"  - {file.name}: {len(df)} rows")

company_df = pd.concat(dfs, ignore_index=True)
print(f"\nTotal companies loaded: {len(company_df)}")

# Step 2: Filter to AI/ML firms
print("\n[Step 2] Filtering to AI/ML firms...")
ai_ml_keywords = ['AI', 'ML', 'artificial intelligence', 'machine learning', 'neural', 'deep learning']

def is_ai_ml_firm(row):
    """Check if firm is AI/ML based on Description and Keywords"""
    text = f"{row['Description']} {row['Keywords']}".lower()
    return any(keyword.lower() in text for keyword in ai_ml_keywords)

company_df['is_ai_ml'] = company_df.apply(is_ai_ml_firm, axis=1)
ai_ml_df = company_df[company_df['is_ai_ml']].copy()
print(f"AI/ML firms identified: {len(ai_ml_df)} out of {len(company_df)} ({len(ai_ml_df)/len(company_df)*100:.1f}%)")

# Step 3: Score vagueness using keyword counts
print("\n[Step 3] Scoring vagueness...")

VAGUE_KEYWORDS = ['approximately', 'around', 'roughly', 'flexible', 'scalable', 'adaptive']
PRECISE_KEYWORDS = ['exactly', 'precisely', 'guaranteed', 'specific', 'certified']

def calculate_vagueness(description):
    """
    Calculate vagueness score (0-100) based on keyword counts
    Formula: 50 + 10*(vague_count - precise_count), capped at [0,100]
    """
    text = description.lower()
    vague_count = sum(text.count(keyword) for keyword in VAGUE_KEYWORDS)
    precise_count = sum(text.count(keyword) for keyword in PRECISE_KEYWORDS)

    score = 50 + 10 * (vague_count - precise_count)
    score = max(0, min(100, score))  # Cap at [0, 100]

    return score

ai_ml_df['vagueness'] = ai_ml_df['Description'].apply(calculate_vagueness)
print(f"Vagueness scores: mean={ai_ml_df['vagueness'].mean():.2f}, "
      f"median={ai_ml_df['vagueness'].median():.2f}, "
      f"std={ai_ml_df['vagueness'].std():.2f}")

# Step 4: Classify integration cost
print("\n[Step 4] Classifying integration cost...")

HIGH_I_KEYWORDS = ['chip', 'asic', 'robotics', 'distributed', 'gpu', 'hardware', 'semiconductor']
LOW_I_KEYWORDS = ['api', 'saas', 'software', 'wrapper', 'platform', 'cloud']

def classify_integration_cost(keywords):
    """
    Classify integration cost based on keywords
    High-i (1): hardware, chips, robotics
    Low-i (0): software, APIs, cloud
    """
    keywords_lower = keywords.lower()

    has_high_i = any(keyword in keywords_lower for keyword in HIGH_I_KEYWORDS)
    has_low_i = any(keyword in keywords_lower for keyword in LOW_I_KEYWORDS)

    # If both or neither, classify based on which has more matches
    if has_high_i and not has_low_i:
        return 1
    elif has_low_i and not has_high_i:
        return 0
    else:
        # Count matches for tie-breaking
        high_i_count = sum(keyword in keywords_lower for keyword in HIGH_I_KEYWORDS)
        low_i_count = sum(keyword in keywords_lower for keyword in LOW_I_KEYWORDS)
        return 1 if high_i_count > low_i_count else 0

ai_ml_df['high_integration_cost'] = ai_ml_df['Keywords'].apply(classify_integration_cost)
high_i_count = ai_ml_df['high_integration_cost'].sum()
low_i_count = len(ai_ml_df) - high_i_count
print(f"Integration cost classification: High-i={high_i_count}, Low-i={low_i_count}")

# Step 5: Create company master file
print("\n[Step 5] Creating company master file...")

# Select and rename columns for output
company_master = ai_ml_df[[
    'CompanyID', 'CompanyName', 'Description', 'Keywords',
    'vagueness', 'high_integration_cost',
    'TotalRaised', 'Employees', 'YearFounded'
]].copy()

# Rename for consistency
company_master.columns = [
    'company_id', 'company_name', 'description', 'keywords',
    'vagueness', 'high_integration_cost',
    'total_raised', 'employees', 'year_founded'
]

# Save to CSV
output_file = PROCESSED_DATA_DIR / "company_master.csv"
company_master.to_csv(output_file, index=False)
print(f"✓ Saved to: {output_file}")
print(f"  Rows: {len(company_master)}")
print(f"  Columns: {len(company_master.columns)}")

# Display summary
print("\n" + "=" * 80)
print("SUMMARY STATISTICS")
print("=" * 80)
print(f"\nTotal AI/ML firms: {len(company_master)}")
print(f"\nVagueness distribution:")
print(company_master['vagueness'].describe())
print(f"\nIntegration cost:")
print(f"  High-i (hardware): {company_master['high_integration_cost'].sum()} ({company_master['high_integration_cost'].sum()/len(company_master)*100:.1f}%)")
print(f"  Low-i (software): {(1-company_master['high_integration_cost']).sum()} ({(1-company_master['high_integration_cost']).sum()/len(company_master)*100:.1f}%)")

print("\n" + "=" * 80)
print("FIRST 5 ROWS")
print("=" * 80)
print(company_master[['company_id', 'company_name', 'vagueness', 'high_integration_cost', 'employees']].head())

print("\n" + "=" * 80)
print("✓ SCRIPT 01 COMPLETED SUCCESSFULLY")
print("=" * 80)
