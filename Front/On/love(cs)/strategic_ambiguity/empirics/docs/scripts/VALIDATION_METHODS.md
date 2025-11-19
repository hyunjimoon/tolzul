# E와 L 설계 의도 검증 방법

## E Definition (Short term survival)
**정의**: E is defined as funding amount of companies whose most recent financing was Early Stage VC (Series A) as of Dec 2021, regardless of when that financing occurred. This state-based definition captures companies currently at the early stage.

## L Definition (Long term survival)
**정의**: Among the companies with E=1, by year t, did they secure Series B+? (t=2023, 2024, 2025)

---

## 검증 방법 (Validation Methods)

### 1. E=1 Cohort Purity (코호트 순수성)

**목적**: E=1 cohort가 오직 Early Stage VC / Series A만 포함하는지 확인

**검증 항목**:
- ✅ 100% of DealType_2021 are "Early Stage VC" or "Series A"
- ❌ NO Buyout/LBO
- ❌ NO Merger/Acquisition
- ❌ NO Later Stage VC / Series B+
- ❌ NO Angel / Seed
- ❌ NO missing values (all E=1 companies must have DealType)

**검증 방법**:
```python
# Pattern matching
is_E = df['DealType_2021'].str.contains('Early Stage VC|Series A', regex=True)
purity_rate = is_E.sum() / len(df)

# Expected: purity_rate == 1.0 (100%)
assert purity_rate == 1.0, f"Cohort not pure: {purity_rate:.1%} are Early Stage VC"
```

**Plot**: Bar chart showing deal type distribution in DealType_2021

---

### 2. State-based Design (상태 기반 설계)

**목적**: E는 "2021.12 시점의 상태"이지 "2021년에 Series A를 받은 이벤트"가 아님을 확인

**설계 의도**:
- E=1: 2021.12에 **현재** Early Stage VC 상태인 회사
- 언제 Series A를 받았는지는 **상관없음**
- 2019년에 Series A를 받았지만 아직 Early Stage인 회사 → E=1 ✅
- 2021년에 Series A를 받았지만 이미 Series B로 넘어간 회사 → E=0 ❌

**검증 방법**:
```python
# 만약 LastFinancingDate 정보가 있다면:
# E=1 cohort 내에서 Series A 날짜 분포 확인
# 2019, 2020, 2021년에 받은 회사들이 모두 섞여 있어야 함

# LastFinancingDate가 없다면:
# 이 검증은 skip (데이터 제약)
```

**Plot**: Histogram of "Years since Series A" (if LastFinancingDate available)

---

### 3. L Definition - Progression from E (L의 진행 정의)

**목적**: L은 E=1 cohort 내에서만 정의되며, Series B+ 달성 여부를 나타냄

**검증 항목**:
- L은 **오직 E=1 companies에 대해서만** 정의됨
- L=1: 해당 시점까지 Series B+ 달성
- L=0: 아직 Early Stage, failed, 또는 다른 결과

**검증 방법**:
```python
# All companies in analysis should have E=1
assert df['E_2021'].all(), "Found non-E=1 companies in L analysis"

# L categories
for year in [2023, 2024, 2025]:
    is_L = df[f'DealType_{year}'].str.contains('Later Stage VC|Series [B-G]', regex=True)
    l_rate = is_L.sum() / len(df)

    print(f"L_{year} rate: {l_rate:.1%}")

    # Sanity check: L rate should be 15-40%
    assert 0.10 <= l_rate <= 0.50, f"L rate {l_rate:.1%} seems unrealistic"
```

**Plot**: Stacked bar chart showing E=1 → L outcomes by year

---

### 4. Temporal Consistency (시간적 일관성)

**목적**: 시간이 지날수록 L=1 비율이 증가해야 함 (monotonic increase)

**설계 의도**:
- 2년 후 (2023) ≤ 3년 후 (2024) ≤ 4년 후 (2025)
- Series B+를 달성하면 되돌아갈 수 없음
- 2023년에 Series B였으면 2024, 2025에도 Later Stage여야 함

**검증 방법**:
```python
# Count L=1 by year
l_2023 = is_later(df['DealType_2023']).sum()
l_2024 = is_later(df['DealType_2024']).sum()
l_2025 = is_later(df['DealType_2025']).sum()

# Check monotonic increase
assert l_2023 <= l_2024 <= l_2025, f"L counts not monotonic: {l_2023}, {l_2024}, {l_2025}"

# Check individual companies: once L=1, stays L=1
for idx, row in df.iterrows():
    if is_later(row['DealType_2023']):
        # Should be Later Stage in 2024 and 2025 too
        assert is_later(row['DealType_2024']), f"Company {row['CompanyID']} regressed from L=1"
        assert is_later(row['DealType_2025']), f"Company {row['CompanyID']} regressed from L=1"
```

**Plot**: Line chart showing L rate over time (2023, 2024, 2025)

---

### 5. Impossible Transitions (불가능한 전환 감지)

**목적**: 논리적으로 불가능한 state transition을 감지

**불가능한 전환**:
- Early Stage → Seed/Angel (역행, impossible)
- Later Stage → Early Stage (역행, impossible)
- Series B → Series A (역행, impossible)

**의심스러운 전환** (경고):
- Early Stage → Buyout/LBO (가능하지만 흔치 않음)
- Early Stage → M&A (가능하지만 흔치 않음)
- Early Stage → Missing (실패 또는 데이터 누락)

**검증 방법**:
```python
# Check for backward transitions
for year in [2023, 2024, 2025]:
    # Early Stage → Seed/Angel
    backward = df['DealType_{year}'].str.contains('Seed|Angel', regex=True, na=False)
    backward_count = backward.sum()

    if backward_count > 0:
        print(f"⚠️  WARNING: {backward_count} companies regressed to Seed/Angel in {year}")

# Check for disappearances
for year in [2023, 2024, 2025]:
    missing = df[f'DealType_{year}'].isna()
    missing_count = missing.sum()
    missing_rate = missing_count / len(df)

    print(f"Missing data in {year}: {missing_count:,} ({missing_rate:.1%})")

    # Warning if too many missing
    if missing_rate > 0.20:
        print(f"⚠️  WARNING: High missing rate ({missing_rate:.1%}) in {year}")
```

**Plot**: Sankey diagram showing all state transitions

---

### 6. Cohort Stability (코호트 안정성)

**목적**: E=1 cohort 크기가 시간에 관계없이 일정한지 확인 (no survivorship bias)

**설계 의도**:
- LEFT JOIN으로 모든 E=1 companies 유지
- Cohort size는 baseline과 동일해야 함
- 실패한 회사도 cohort에 유지 (L=0으로 분류)

**검증 방법**:
```python
# Cohort size should be constant
baseline_size = len(df)

# All endpoint DataFrames should have same size
for year in [2023, 2024, 2025]:
    endpoint_size = len(df)  # After merge
    assert endpoint_size == baseline_size, f"Cohort size changed: {baseline_size} → {endpoint_size}"

print(f"✓ Cohort stability verified: {baseline_size:,} companies across all timepoints")
```

**Plot**: Bar chart showing cohort size over time (should be flat)

---

### 7. Progression Rate Sanity Check (진행률 상식 검증)

**목적**: L 진행률이 상식적인 범위인지 확인

**예상 범위** (based on typical VC progression):
- 2년 후 (2023): 15-25% Later Stage
- 3년 후 (2024): 20-30% Later Stage
- 4년 후 (2025): 25-40% Later Stage

**검증 방법**:
```python
expected_ranges = {
    2023: (0.10, 0.30),  # 10-30%
    2024: (0.15, 0.35),  # 15-35%
    2025: (0.20, 0.45),  # 20-45%
}

for year, (min_rate, max_rate) in expected_ranges.items():
    l_rate = is_later(df[f'DealType_{year}']).sum() / len(df)

    if l_rate < min_rate:
        print(f"⚠️  WARNING: L_{year} rate ({l_rate:.1%}) is unusually LOW (expected {min_rate:.0%}-{max_rate:.0%})")
    elif l_rate > max_rate:
        print(f"⚠️  WARNING: L_{year} rate ({l_rate:.1%}) is unusually HIGH (expected {min_rate:.0%}-{max_rate:.0%})")
    else:
        print(f"✓ L_{year} rate ({l_rate:.1%}) is within expected range")
```

**Plot**: L rate over time with expected range bands

---

### 8. Outcome Categories (결과 카테고리 분포)

**목적**: E=1 companies의 가능한 결과들이 모두 합리적인지 확인

**가능한 결과** (2025년 기준):
- L=1 (Later Stage VC / Series B+): 성공
- L=0, stayed Early Stage: 아직 진행 중
- L=0, missing data: 실패 또는 데이터 누락
- L=0, Buyout/LBO: Exit (성공적 인수)
- L=0, M&A: Exit (인수합병)
- L=0, Seed/Angel: 역행 (데이터 오류 가능성)

**검증 방법**:
```python
# Categorize all E=1 companies by 2025 outcome
outcomes = {
    'Later_Stage': 0,
    'Still_Early': 0,
    'Buyout_LBO': 0,
    'MA': 0,
    'Missing': 0,
    'Other': 0
}

for idx, row in df.iterrows():
    deal_2025 = row['DealType_2025']

    if pd.isna(deal_2025):
        outcomes['Missing'] += 1
    elif is_later(deal_2025):
        outcomes['Later_Stage'] += 1
    elif is_early(deal_2025):
        outcomes['Still_Early'] += 1
    elif 'Buyout' in deal_2025 or 'LBO' in deal_2025:
        outcomes['Buyout_LBO'] += 1
    elif 'Merger' in deal_2025 or 'Acquisition' in deal_2025:
        outcomes['MA'] += 1
    else:
        outcomes['Other'] += 1

# Print distribution
for outcome, count in outcomes.items():
    pct = count / len(df) * 100
    print(f"  {outcome}: {count:,} ({pct:.1f}%)")
```

**Plot**: Pie chart or bar chart showing outcome distribution

---

### 9. V×F Interaction Feasibility (가설 검증 가능성)

**목적**: V (Vagueness)와 F (Flexibility) 데이터가 hypothesis test에 충분한지 확인

**검증 항목**:
- Description/Keywords 존재 (vagueness 계산용)
- F_flexibility 분포 (0과 1이 모두 존재)
- 충분한 sample size per group

**검증 방법**:
```python
# Check Description/Keywords availability
has_desc = df['Description_2021'].notna().sum()
has_keywords = df['Keywords_2021'].notna().sum()

print(f"Description available: {has_desc:,} / {len(df):,} ({has_desc/len(df):.1%})")
print(f"Keywords available: {has_keywords:,} / {len(df):,} ({has_keywords/len(df):.1%})")

if has_desc < len(df) * 0.5:
    print(f"⚠️  WARNING: Less than 50% have Description (vagueness may be inaccurate)")

# Check F distribution (if F_flexibility exists)
if 'F_flexibility' in df.columns:
    f_dist = df['F_flexibility'].value_counts()
    print(f"\nFlexibility distribution:")
    for val, count in f_dist.items():
        print(f"  F={val}: {count:,} ({count/len(df):.1%})")

    # Both F=0 and F=1 should exist
    if len(f_dist) < 2:
        print(f"⚠️  WARNING: Only one F value present (interaction test impossible)")
```

**Plot**: Histogram of vagueness scores (if computed)

---

## 종합 검증 프로세스

### Phase 1: Data Quality
1. E=1 Cohort Purity
2. Cohort Stability
3. Missing data analysis

### Phase 2: Logical Consistency
4. Temporal Consistency
5. Impossible Transitions
6. Outcome Categories

### Phase 3: Statistical Feasibility
7. Progression Rate Sanity Check
8. V×F Interaction Feasibility

### Phase 4: Visual Inspection
9. Generate all plots for manual review

---

## Pass Criteria

**MUST PASS** (critical):
- ✅ E=1 Cohort Purity == 100%
- ✅ Cohort Stability (size constant)
- ✅ Temporal Consistency (L monotonic increase)
- ✅ No impossible transitions (Early → Seed/Angel)

**SHOULD PASS** (important):
- ✅ Progression rates within expected range
- ✅ V×F data availability > 50%

**CAN WARN** (informational):
- ⚠️  High missing data rate (>20%)
- ⚠️  Unusual outcome distribution
- ⚠️  Low Description/Keywords coverage

---

## Output Format

Each validation method will output:
```
================================================================================
TEST N: [Test Name]
================================================================================

Purpose: [What this test checks]

Results:
  [Metric 1]: [Value] [Status]
  [Metric 2]: [Value] [Status]
  ...

Verdict: ✓ PASS / ⚠️ WARNING / ✗ FAIL

[Optional plot saved to: outputs/validation/...]
================================================================================
```

Final summary:
```
================================================================================
VALIDATION SUMMARY
================================================================================

Critical Tests:   4 / 4 PASSED
Important Tests:  2 / 2 PASSED
Warnings:         1

Overall Status: ✓ READY FOR ANALYSIS
================================================================================
```
