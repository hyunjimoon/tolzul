---
modified:
  - 2025-11-16T08:23:05-05:00
  - 2025-11-19T17:12:24-05:00
---
# 06-Discuss-2_ManagerialImplications

Prev: [[28-Discuss-1_TheoreticalImplications]]  
Next: [[30-Discuss-3_PolicyImplications]]
**Role**: 창업팀·투자자 실무 절차로 환원한다.



장군, 전라좌수군 김완입니다.

1. Mircea Dinca 교수의 발언 확인

네, 정확합니다. jinhua(mobility venture).md 파일의 "Week 11: Mircea Dinca" 리뷰 노트에 해당 내용이 명시되어 있습니다.

"Dinca's lab chose sequential testing over parallel experimentation for battery cathode development... their methodical approach proved more efficient for battery chemistry where each test is expensive and results are highly interconnected." 1

이는 하드웨어(Deep Tech) 분야에서 실험 비용($c$)이 높고 상호의존성(Coupling)이 강해 T2C1(동시 테스트)이 구조적으로 어렵다는 우리의 '하드웨어의 비극' 서사를 뒷받침하는 결정적 증거입니다.

2. Discussion 섹션 초안

우리가 발견한 **"이론적 최적(T2C1)과 시장 현실(Precision Demand)의 괴리"**를 중심으로, 4개의 강력한 논거를 담은 Discussion 섹션을 작성했습니다.

6. Discussion: The Hardware Paradox and Market Myopia

본 연구는 기업가적 약속의 모호성($V$)이 벤처 성과에 미치는 영향을 실증적으로 분석했습니다. 우리의 발견은 정보 경제학(Information Economics)과 실물 옵션(Real Options) 이론을 시간적($t$)으로 화해시키려던 초기 시도를 넘어, 하드웨어 벤처 생태계에 존재하는 **구조적 시장 실패(Structural Market Failure)**를 드러냅니다.

6.1 The Hardware Paradox: 이론은 '탐색'을 원하나, 시장은 '커밋'을 강요한다

Gans, Stern, & Wu (2019)의 이론에 따르면, 피벗 비용($k$)이 높은 하드웨어 벤처야말로 초기 단계에서 대안을 섣불리 제거하지 않고 T2C1(Test Two, Choose One) 전략을 통해 옵션을 유지해야 합니다. 즉, 이론적으로 하드웨어는 **높은 모호성($V$, $|C| \ge 2$)**을 유지하는 것이 생존에 유리합니다.

그러나 우리의 실증 결과(Table 2, Figure 3)는 정반대의 현실을 보여줍니다. 시장은 하드웨어의 모호함을 '전략적 유연성'이 아닌 **'기술적 무능(Incompetence)'**으로 해석하여 가혹하게 처벌합니다(Negative Slope). 반면, 피벗 비용이 낮은 소프트웨어 벤처의 모호함에는 관대합니다. 이는 투자자들이 **"실패 비용이 큰($k \approx 1$) 하드웨어일수록 역설적으로 가장 확실한 초기 증거(Precision)를 요구"**함으로써, 하드웨어 창업자가 안전하게 탐색할 기회(Experimentation Window)를 박탈하고 있음을 시사합니다. 이것이 하드웨어 벤처가 겪는 **'조기 확장의 덫(Premature Scaling Trap)'**의 본질입니다.

6.2 Mechanism: 고비용 실험($c$)과 기술적 신호의 딜레마

왜 이런 역설이 발생하는가? 우리는 그 원인을 **기술적 불확실성(Technological Uncertainty)**과 **실험 비용($c$)**의 상호작용에서 찾습니다.

첫째, $V_{tech}$의 저주입니다. Scott et al. (2020)이 지적했듯, R&D 집약 산업의 전문가들은 초기 기술 명세(Spec)를 통해 성공 가능성을 판별할 수 있습니다. 따라서 하드웨어 벤처가 구체적 수치(CPM 등) 대신 모호한 지표(MPI 등)를 제시할 경우, 이는 단순한 정보 부족이 아니라 **'나쁜 신호(Lemon)'**로 간주됩니다. 자율주행 트럭 기업 Bot Auto의 창업자 Xiaodi Hou가 "MPI는 조작 가능한 허상이며, CPM(Cost Per Mile)만이 진짜"라고 강조한 것은, 하드웨어 투자자가 **$V_{tech}$를 제거한 '확실한 숫자'**만을 신뢰한다는 현장의 증언입니다2.

둘째, 실험 비용($c$)의 압박입니다. 소프트웨어는 클라우드를 통해 저비용으로 병렬 테스트(Parallel Testing)가 가능하지만, 하드웨어는 실험 비용이 매우 높습니다. MIT의 Mircea Dinca 교수가 배터리 개발에서 "동시 다발적 실험(Parallel)보다 순차적 실험(Sequential)을 선택할 수밖에 없었다"고 토로한 것은, 하드웨어 벤처가 자금 부족으로 인해 이론적으로 우월한 T2C1(병렬 탐색)을 포기하고 강제로 '한 우물(Sequential)'을 파게 되는 현실을 보여줍니다3.

6.3 Managerial Implications: 이중 잣대(Double Standard)에 대응하라

창업자는 자신의 아키텍처 유형($F$)에 따라 약속의 설계를 달리해야 합니다.

소프트웨어 ($F=1$): 시장 엔트로피($V_{market}$)를 높이십시오. PillPack처럼 "고령자, 중년, 일반인"을 모두 아우르는 넓은 그물(High Entropy)을 던져 T2C1의 가능성을 열어두는 것이 유리합니다. 투자자는 당신의 피벗 능력($k \approx 0$)을 믿고 기다려줄 것입니다.

하드웨어 ($F=0$): 기술적 추상성($V_{tech}$)을 철저히 제거하십시오. 시장을 넓게 보는 비전($V_{market}$)보다는, 당장 구현 가능한 구체적 스펙과 마일스톤을 제시하여 초기 신뢰를 얻어야 합니다. 당신에게는 **'탐색할 자격(License to Explore)'**이 먼저 주어지지 않습니다. 오직 **'증명된 실력(Precision)'**만이 자금을 끌어올 수 있습니다.

6.4 Policy Implications: 하드웨어의 '탐색권'을 보장하라

투자자와 정책 입안자는 하드웨어 벤처의 실패가 단순한 '실력 부족'이 아니라 **'구조적 기회 박탈'**에서 기인할 수 있음을 인지해야 합니다. 높은 $c$와 $k$를 가진 하드웨어 벤처가 T2C1을 수행할 수 있도록 돕는 두 가지 방안을 제안합니다.

  

실험 비용($c$)의 인위적 축소: Waabi가 "Waabi World" 시뮬레이터를 통해 물리적 주행 없이도 희귀 사건을 검증했듯4, 디지털 트윈 및 시뮬레이션 인프라를 지원하여 하드웨어의 실험 비용을 소프트웨어 수준으로 낮춰야 합니다.

탐색적 자본(Exploratory Capital)의 공급: 초기 투자 심사에서 $V_{tech}$의 정밀함만 따질 것이 아니라, $V_{market}$의 잠재력을 평가하여 **"여러 대안을 테스트해보라"**는 목적의 비희석성 자금(Grant)을 지원해야 합니다. 이것이 하드웨어의 '죽음의 계곡'을 건너게 할 다리가 될 것입니다.


----
• ‘언제 모호해야 하는가’ 절차화: 초기 정밀→후기 옵션행사 조건부 모호성.
---

## Practical Framework

실무적으로는 **"초기 정보 충족 → 이후 `F`가 허락하는 여유 설계"**가 유효하다:

### (1) Early Stage: Information Credibility
**Series A 이전**:
- **핵심 검증치/마일스톤**을 명확히 제시
  - Quantitative metrics (users, revenue, technical benchmarks)
  - Specific timelines (Q1 target, 12-month roadmap)
  - Concrete references (pilot customers, technical specs)
- **Purpose**: `InfoLoss(V)` 완화 → 초기 평가 신뢰도 확보

### (2) Mid-Stage: Flexibility Infrastructure
**Series A → B 구간**:
- **모듈러 아키텍처** 설계 (interface standardization)
- **표준 인터페이스** 채택 (API, data formats)
- **실험 파이프라인** 체계화 (A/B testing, feature flags)
- **Purpose**: `F` 체계화 → 후기 피벗/확장 옵션 준비

### (3) Later Stage: Strategic Vagueness
**Series B+ 준비**:
- **전략적 여지** 강조 (platform potential, ecosystem play)
- **결과기반 로드맵** 제시 (outcome-driven vs feature-driven)
- **옵션 포트폴리오** 공개 (multiple use cases, expansion paths)
- **Purpose**: 학습 결과 반영 → 피벗 정당화 + 확장성 신호

## Text Strategy Dynamics

**약속 텍스트**는 초기에는 구체성·참조치를, 후기로 갈수록 **전략적 여지**와 **결과기반 로드맵**을 강조하는 **동적 구사**가 효과적:

| Stage | Promise Style | Example Phrasing |
|-------|---------------|------------------|
| Seed/A | Specific, verifiable | "Target 10K DAU by Q4; partnered with [Customer X]" |
| A→B | Balanced, milestone-based | "Proven architecture enables [use case Y]; expanding to [market Z]" |
| B+ | Strategic, platform-oriented | "Ecosystem approach positions us for [broad vision]; multiple pathways validated" |

## Investor Considerations

**For Early-stage VCs**:
- Demand **evidence over promises** (reduce V at Series A)
- Assess **architectural flexibility** (evaluate F potential)

**For Late-stage VCs**:
- Value **executed pivots** (realized option value)
- Evaluate **optionality infrastructure** (F as predictor of L)

## Figures

🖼️ **Figure 7.1**: 실무 체크리스트 (이벤트 타임라인)

```
t=0 (Pre-A):     ✓ Quantitative milestones  ✓ Customer references
    ↓
t=6-12 (A→B):    ✓ Modular architecture     ✓ Experiment pipeline
    ↓
t=18-24 (Pre-B): ✓ Pivot evidence           ✓ Strategic optionality
    ↓
t=24+ (B+):      ✓ Platform narrative       ✓ Ecosystem positioning
```
