# List of Tables
## The Promise Vendor: Strategic Ambiguity and the Capital-Flexibility Paradox
**Source:** `[[🗄️REGISTRY]]`

---

## Introduction

| # | Table | Caption |
|:-:|:------|:--------|
| I.1 | `[[🗄️I_verified]]` | Verified Numbers Summary (2025-12-08) |

---

## Paper U: Vague Promise and Venture Growth

| # | Table | Caption |
|:-:|:------|:--------|
| U.1 | `[[🗄️U_S3_quartile]]` | Survival Rates by Vagueness Quartile |
| U.2 | `[[🗄️U_S3_chisq]]` | U-Shape Statistical Tests |

---

## Paper C: The Commitment Trap

| # | Table | Caption |
|:-:|:------|:--------|
| C.1 | `[[🗄️C_S3_correlations]]` | Key Correlations |
| C.2 | `[[🗄️C_S3_hypotheses]]` | Three Hypotheses Test Results |
| C.3 | `[[🗄️C_S3_gap]]` | The 2.7× Flexibility Gap |

---

## Paper N: The Promise Vendor

| # | Table | Caption |
|:-:|:------|:--------|
| N.1 | `[[🗄️N_S3_cr]]` | Critical Ratio by Industry |

---

## Table Details (from [[🗄️REGISTRY]])

### 🗄️I_verified

| Metric | Value | Source |
|:-------|:------|:-------|
| Total Sample | **408,784** | features_all.parquet |
| Panel Sample | **133,945** | vagueness_timeseries |
| ρ(Y, \|ΔV\|) | **+0.159*** | Spearman |
| ρ(E, \|ΔV\|)_within_V | **-0.052*** | Within-decile |
| Flexibility Gap | **2.7×** | Q4/Q1 |
| Mid-V Trap Rate | **25.6%** | Modal V bin |

### 🗄️U_S3_quartile

| Industry | N | Q1 | Q2 | Q3 | Q4 | χ² |
|:---------|--:|:--:|:--:|:--:|:--:|---:|
| Transportation | 154,148 | 5.7% | 2.9% | 4.0% | 8.6% | 1430.9*** |
| Software | 226,896 | 7.8% | 4.8% | 6.8% | 8.0% | 564.8*** |
| Hardware | 50,390 | 6.0% | 3.7% | 3.9% | 8.7% | 398.6*** |
| Pharma | 56,947 | 8.8% | 5.7% | 6.2% | 10.6% | 305.7*** |

### 🗄️U_S3_chisq

| Test | Result | p-value |
|:-----|:------:|:-------:|
| H₀: Linear | Rejected | > 0.10 |
| H₁: U-shape | Confirmed | < 0.001 |
| Murky Middle Penalty | -3.2pp | — |

### 🗄️C_S3_correlations

| Relationship | ρ | p-value |
|:-------------|:-:|:-------:|
| ρ(Y, \|ΔV\|) | **+0.159** | < 0.001 |
| ρ(E, ΔV) | -0.014 | < 0.001 |
| ρ(E, \|ΔV\|)_within_V | **-0.052** | < 0.001 |

### 🗄️C_S3_hypotheses

| H | Claim | ρ | Status |
|:-:|:------|:-:|:------:|
| H1 | Flexibility → Growth | +0.158*** | ✅ |
| H2 | Capital → Less Flex | -0.052*** | ✅ |
| H3a | Low V: E hurts | -0.05 | ✅ |
| H3b | High V: E helps | +0.08 | ✅ |

### 🗄️C_S3_gap

| \|ΔV\| Quartile | Y Median | Relative |
|:----------------|:--------:|:--------:|
| Q1 (Rigid) | 1.00× | Baseline |
| Q4 (Flexible) | 2.71× | +171% |
| **Gap** | **2.7×** | — |

### 🗄️N_S3_cr

| Industry | CR | Optimal k* |
|:---------|:--:|:----------:|
| Software | 0.3 | 1-2 |
| Hardware | 0.5 | 2-3 |
| AV/Deep-tech | 0.9 | 4-5 |

---

**Total Tables: 7**

*Managed by 🟢J-Squad*
*Registry: [[🗄️REGISTRY]]*
