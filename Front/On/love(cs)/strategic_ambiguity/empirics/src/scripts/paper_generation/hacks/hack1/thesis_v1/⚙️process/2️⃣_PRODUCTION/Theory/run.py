#!/usr/bin/env python3
"""
Theory/run.py - Generate theoretical figures for Promise Precision paper

Outputs:
- fig1_tradeoff.pdf: VOI vs RO trade-off curve
- fig2_architecture.pdf: Hardware vs Software option exercisability
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent.parent / "3️⃣_OUTPUT" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def generate_voi_ro_tradeoff():
    """
    Figure 1: Trade-off between VOI (early) and RO (later)
    
    Red line: Value of Information (decreases with vagueness)
    Blue line: Real Option value (increases then decreases)
    Total: Sum of both (optimal vagueness at intersection)
    """
    V = np.linspace(0, 1, 100)
    
    # VOI: decreases linearly (clarity → lower uncertainty)
    VOI = 0.8 * (1 - V)
    
    # RO: inverted U (some vagueness good, too much bad)
    RO = 0.5 * V * (1 - V)  
    
    # Total payoff
    Total = VOI + RO
    
    # Plot
    plt.figure(figsize=(8, 6))
    plt.plot(V, VOI, 'r-', linewidth=2, label='VOI(V): clarity payoff')
    plt.plot(V, RO, 'b--', linewidth=2, label='RO(V): flexibility payoff')
    plt.plot(V, Total, 'k:', linewidth=2.5, label='Total payoff')
    
    # Mark optimal point
    optimal_idx = np.argmax(Total)
    plt.plot(V[optimal_idx], Total[optimal_idx], 'ko', markersize=10, 
             label=f'V* ≈ {V[optimal_idx]:.2f}')
    
    plt.xlabel('Promise Variance V (vagueness)', fontsize=12)
    plt.ylabel('Contribution to expected enterprise value', fontsize=12)
    plt.title('Trade-off: VOI (red) vs. RO (purple) → Total (blue)', fontsize=14)
    plt.legend(loc='upper right')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    
    # Save
    output_path = OUTPUT_DIR / "fig1_tradeoff.pdf"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Saved: {output_path}")
    plt.close()

def generate_architecture_comparison():
    """
    Figure 2: Hardware vs Software - RO exercisability
    
    Software: steep positive slope (easy to pivot)
    Hardware: flat/negative slope (hard to pivot)
    """
    V = np.linspace(0, 1, 100)
    
    # Software: RO value increases (easy to exercise options)
    RO_software = 0.4 * V
    
    # Hardware: RO value flat/decreases (hard to exercise, costs dominate)
    RO_hardware = 0.2 - 0.1 * V
    
    plt.figure(figsize=(8, 6))
    plt.plot(V, RO_software, color='skyblue', linewidth=3, label='Software (flexible)')
    plt.plot(V, RO_hardware, color='gray', linewidth=3, label='Hardware (rigid)')
    
    plt.xlabel('Promise Variance V (vagueness)', fontsize=12)
    plt.ylabel('RO contribution to later success', fontsize=12)
    plt.title('H2a/b: Architecture Moderates RO Value', fontsize=14)
    plt.legend(loc='best')
    plt.grid(alpha=0.3)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.tight_layout()
    
    output_path = OUTPUT_DIR / "fig2_architecture.pdf"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Saved: {output_path}")
    plt.close()

if __name__ == "__main__":
    print("🔧 Generating Theory figures...")
    generate_voi_ro_tradeoff()
    generate_architecture_comparison()
    print("✅ Theory section complete.")
