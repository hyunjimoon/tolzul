# plots.py
"""
W1 Figures (Matplotlib only)
- Fig1: Vagueness distribution (univariate limitation)
- Fig2: Growth by architecture (univariate limitation)
- Fig3: H2 Interaction (Modular↑ green, Hardware↓ purple)
- Fig4: Reversal (H1 negative vs H2 positive)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

GREEN_SW = "#198754"   # Software/Modular
PURPLE_HW = "#6f42c1"  # Hardware/Integrated
GRAY = "#6c757d"
GREEN = "#28a745"

def fig_vagueness_dist(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8,5))
    v = pd.to_numeric(df['vagueness'], errors='coerce').dropna()
    ax.hist(v, bins=30, edgecolor='black', alpha=0.75)
    ax.axvline(v.median(), color='red', linestyle='--', linewidth=2, label=f"Median {v.median():.1f}")
    ax.set_xlabel("Vagueness (0=precise, 100=vague)")
    ax.set_ylabel("Count")
    ax.set_title("Figure 1. Vagueness Distribution (Precision Bias)")
    ax.legend()
    return fig

def fig_growth_by_arch(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8,5))
    tmp = df.dropna(subset=['growth','is_hardware'])
    rates = tmp.groupby('is_hardware')['growth'].mean().reindex([0,1]).fillna(0)
    ax.bar(['Software (Modular)','Hardware (Integrated)'],
           [rates.loc[0], rates.loc[1]],
           color=[GREEN_SW, PURPLE_HW], edgecolor="black")
    ax.set_ylim(0,1); ax.set_ylabel("Growth (Series B+) Rate")
    ax.set_title("Figure 2. Growth by Architecture (Univariate)")
    return fig

def fig_h2_interaction(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(9,6))
    tmp = df.dropna(subset=['growth','vagueness','is_hardware']).copy()
    for is_hw, color, label, style in [
        (0, GREEN_SW, "Software / Modular", '-'),
        (1, PURPLE_HW, "Hardware / Integrated", '--')
    ]:
        sub = tmp[tmp['is_hardware']==is_hw]
        if len(sub)==0: continue
        sub['v_bin'] = pd.qcut(sub['vagueness'], 5, duplicates='drop')
        rates = sub.groupby('v_bin')['growth'].mean()
        ax.plot(range(len(rates)), rates.values, marker='o', linewidth=3,
                color=color, linestyle=style, label=label)
    ax.set_xticks(range(len(rates))); ax.set_xlabel("Vagueness quintile (Low→High)")
    ax.set_ylim(0,1); ax.set_ylabel("Growth (Series B+) Rate")
    ax.set_title("Figure 3. H2 Interaction (Modular↑, Integrated↓)")
    ax.legend()
    return fig

def fig_reversal(df: pd.DataFrame, h1_coef: float, h2_main: float):
    fig, ax = plt.subplots(figsize=(8,5))
    bars = ax.bar(['H1: Early Funding','H2: Growth (avg)'],
                  [h1_coef, h2_main],
                  color=[GRAY, GREEN], edgecolor="black", linewidth=1.5)
    ax.axhline(0, color='black', linewidth=1)
    ax.set_ylabel("Effect (sign/scale comparable)")
    ax.set_title("Figure 4. Reversal: What hurts early helps later")
    for b, val in zip(bars, [h1_coef, h2_main]):
        ax.text(b.get_x()+b.get_width()/2, val + (0.05 if val>=0 else -0.08),
                f"{val:.2f}", ha='center', va='bottom' if val>=0 else 'top')
    return fig
