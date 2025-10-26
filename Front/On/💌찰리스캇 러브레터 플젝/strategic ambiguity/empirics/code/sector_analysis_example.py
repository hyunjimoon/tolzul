"""
Example: Multi-Sector Analysis with xarray

This script demonstrates how to use the multi-sector classification
for analyzing companies across different eras of ferment (AV, 3DP, etc.)

Usage:
    python sector_analysis_example.py
"""

import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from config.sector_keywords import SECTOR_DEFINITIONS, get_all_sectors

# Import pipeline
from pipeline_xarray import StrategicAmbiguityPipeline


def main():
    """Run example sector analyses"""
    
    print("=" * 80)
    print("MULTI-SECTOR ANALYSIS EXAMPLES")
    print("=" * 80)
    
    # Initialize pipeline
    print("\n[1] Loading pipeline data...")
    pipeline = StrategicAmbiguityPipeline()
    ds = pipeline.ds
    
    # Check if data is loaded
    if 'company' not in ds.dims:
        print("\n⚠️  No company data loaded. Please run the pipeline first:")
        print("    python pipeline_xarray.py")
        return
    
    print(f"  ✓ Loaded {len(ds['company'])} companies")
    
    # Display available sectors
    print("\n[2] Available sectors:")
    available_sectors = []
    for sector_id in get_all_sectors():
        col_name = f'company_is_{sector_id}'
        if col_name in ds:
            count = int(ds[col_name].sum().values)
            available_sectors.append(sector_id)
            sector_name = SECTOR_DEFINITIONS[sector_id]['name']
            print(f"  - {sector_id:10s} ({sector_name:30s}): {count:4d} companies")
    
    if not available_sectors:
        print("\n⚠️  No sector data found. Sector classification may not have run yet.")
        return
    
    # Example 1: Filter to single sector
    print("\n" + "=" * 80)
    print("[Example 1] Single Sector Analysis: Autonomous Vehicles")
    print("=" * 80)
    
    if 'company_is_AV' in ds:
        av_companies = ds.where(ds['company_is_AV'], drop=True)
        n_av = len(av_companies['company'])
        
        print(f"\nAutonomous Vehicle companies: {n_av}")
        
        if n_av > 0 and 'company_vagueness' in av_companies:
            av_vagueness_mean = float(av_companies['company_vagueness'].mean().values)
            av_vagueness_std = float(av_companies['company_vagueness'].std().values)
            print(f"Average vagueness: {av_vagueness_mean:.2f} (±{av_vagueness_std:.2f})")
            
            if 'company_high_integration_cost' in av_companies:
                high_i = int(av_companies['company_high_integration_cost'].sum().values)
                pct_high_i = high_i / n_av * 100 if n_av > 0 else 0
                print(f"High integration cost: {high_i} ({pct_high_i:.1f}%)")
            
            # Show a few example companies
            if 'company_company_name' in av_companies:
                print(f"\nExample AV companies:")
                for i, company_id in enumerate(av_companies['company'][:5].values):
                    name = av_companies['company_company_name'].sel(company=company_id).values
                    vague = av_companies['company_vagueness'].sel(company=company_id).values
                    print(f"  {i+1}. {name} (vagueness: {vague:.1f})")
    else:
        print("  ⚠️  AV sector not found in dataset")
    
    # Example 2: Compare multiple sectors
    print("\n" + "=" * 80)
    print("[Example 2] Sector Comparison: AV vs 3DP")
    print("=" * 80)
    
    if 'company_is_AV' in ds and 'company_is_3DP' in ds and 'company_vagueness' in ds:
        av_ds = ds.where(ds['company_is_AV'], drop=True)
        tdp_ds = ds.where(ds['company_is_3DP'], drop=True)
        
        n_av = len(av_ds['company'])
        n_tdp = len(tdp_ds['company'])
        
        print(f"\nAV companies: {n_av}")
        print(f"3DP companies: {n_tdp}")
        
        if n_av > 0:
            av_vague_mean = float(av_ds['company_vagueness'].mean().values)
            print(f"\nAV average vagueness: {av_vague_mean:.2f}")
        
        if n_tdp > 0:
            tdp_vague_mean = float(tdp_ds['company_vagueness'].mean().values)
            print(f"3DP average vagueness: {tdp_vague_mean:.2f}")
        
        if n_av > 0 and n_tdp > 0:
            diff = av_vague_mean - tdp_vague_mean
            print(f"\nDifference: {diff:.2f} (AV - 3DP)")
            if diff > 0:
                print(f"  → AV companies are more vague")
            else:
                print(f"  → 3DP companies are more vague")
    else:
        print("  ⚠️  Required data not found")
    
    # Example 3: Multi-sector companies
    print("\n" + "=" * 80)
    print("[Example 3] Multi-Sector Companies")
    print("=" * 80)
    
    if 'company_sector_count' in ds:
        sector_counts = ds['company_sector_count'].values
        
        print(f"\nSector overlap distribution:")
        unique, counts = np.unique(sector_counts, return_counts=True)
        for n_sectors, count in zip(unique, counts):
            pct = count / len(sector_counts) * 100
            print(f"  {int(n_sectors)} sector(s): {count:5d} companies ({pct:5.1f}%)")
        
        # Find companies in multiple sectors
        multi_sector = ds.where(ds['company_sector_count'] > 1, drop=True)
        n_multi = len(multi_sector['company'])
        
        if n_multi > 0:
            print(f"\nCompanies in multiple sectors: {n_multi}")
            
            # Show some examples
            if 'company_company_name' in multi_sector and 'company_primary_sector' in multi_sector:
                print(f"\nExample multi-sector companies:")
                for i, company_id in enumerate(multi_sector['company'][:5].values):
                    name = multi_sector['company_company_name'].sel(company=company_id).values
                    n_sect = int(multi_sector['company_sector_count'].sel(company=company_id).values)
                    primary = multi_sector['company_primary_sector'].sel(company=company_id).values
                    
                    # Find which sectors
                    sectors = []
                    for sector_id in get_all_sectors():
                        col_name = f'company_is_{sector_id}'
                        if col_name in multi_sector:
                            if bool(multi_sector[col_name].sel(company=company_id).values):
                                sectors.append(sector_id)
                    
                    print(f"  {i+1}. {name}")
                    print(f"     Sectors: {', '.join(sectors)} (primary: {primary})")
    else:
        print("  ⚠️  Sector count data not found")
    
    # Example 4: Intersection analysis (AV + AI)
    print("\n" + "=" * 80)
    print("[Example 4] Intersection Analysis: AV + AI/ML")
    print("=" * 80)
    
    if 'company_is_AV' in ds and 'company_is_AI_ML' in ds:
        av_and_ai = ds.where(
            (ds['company_is_AV']) & (ds['company_is_AI_ML']),
            drop=True
        )
        n_intersection = len(av_and_ai['company'])
        
        n_av = int(ds['company_is_AV'].sum().values)
        n_ai = int(ds['company_is_AI_ML'].sum().values)
        
        print(f"\nAV companies: {n_av}")
        print(f"AI/ML companies: {n_ai}")
        print(f"AV ∩ AI/ML: {n_intersection}")
        
        if n_av > 0:
            pct_av_doing_ai = n_intersection / n_av * 100
            print(f"\nPercentage of AV companies using AI/ML: {pct_av_doing_ai:.1f}%")
        
        if n_intersection > 0 and 'company_company_name' in av_and_ai:
            print(f"\nExample AV+AI companies:")
            for i, company_id in enumerate(av_and_ai['company'][:5].values):
                name = av_and_ai['company_company_name'].sel(company=company_id).values
                print(f"  {i+1}. {name}")
    else:
        print("  ⚠️  Required sectors not found")
    
    # Example 5: Primary sector analysis
    print("\n" + "=" * 80)
    print("[Example 5] Primary Sector Distribution")
    print("=" * 80)
    
    if 'company_primary_sector' in ds:
        primary_sectors = ds['company_primary_sector'].values
        unique_sectors, counts = np.unique(primary_sectors, return_counts=True)
        
        # Sort by count descending
        sorted_indices = np.argsort(counts)[::-1]
        
        print(f"\nPrimary sector distribution:")
        for idx in sorted_indices[:10]:  # Top 10
            sector = unique_sectors[idx]
            count = counts[idx]
            pct = count / len(primary_sectors) * 100
            
            # Get full name if available
            sector_name = sector
            if sector in SECTOR_DEFINITIONS:
                sector_name = SECTOR_DEFINITIONS[sector]['name']
            
            print(f"  {sector_name:30s}: {count:5d} ({pct:5.1f}%)")
    else:
        print("  ⚠️  Primary sector data not found")
    
    # Summary
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)
    print("\nKey xarray filtering patterns used:")
    print("  1. Single sector: ds.where(ds['company_is_AV'], drop=True)")
    print("  2. Multiple sectors (AND): ds.where((ds['company_is_AV']) & (ds['company_is_AI_ML']), drop=True)")
    print("  3. Multiple sectors (OR): ds.where((ds['company_is_AV']) | (ds['company_is_3DP']), drop=True)")
    print("  4. Sector count: ds.where(ds['company_sector_count'] > 1, drop=True)")
    print("  5. Primary sector: ds.where(ds['company_primary_sector'] == 'AV', drop=True)")
    
    print("\n💡 Tip: Use these patterns in your analysis scripts and notebooks!")


if __name__ == "__main__":
    main()
