---
부사: 이순신
modified:
  - 2025-11-15T19:54:16-05:00
  - 2025-11-16T07:06:52-05:00
  - 2025-11-16T21:30:00-05:00
  - 2025-11-19T04:56:16-05:00
---
![[00_TOC 2025_11_19.excalidraw]]
### **논문 구조 요약 (섹션별)**

| No. | 섹션 (Section)                        | 주요 내용 및 역할 (Key Contents & Roles)                                                                      | 담당자 (Person in Charge) | 핵심 지시사항 (Key Instructions)                    | 주요 산출물 (Figures & Tables)                                                      |
| :-: | :---------------------------------- | :----------------------------------------------------------------------------------------------------- | :--------------------- | :-------------------------------------------- | :----------------------------------------------------------------------------- |
|  1  | **01_Introduction**                 | 현상 제시(Hook)부터 연구의 기여까지 논문의 전체적인 개요를 소개. 문제 제기, 연구 질문, 접근법, 핵심 발견 및 기여를 요약합니다.                          | 정운                     | -                                             | -                                                                              |
|  2  | **02_LitReview_Contributions**      | 정보경제학/신호 이론 및 실물옵션/유연성 관련 기존 문헌을 검토하고, 시간 및 아키텍처 차원을 추가하여 본 연구의 차별점을 부각합니다.                            | 정운                     | -                                             | 🗄️차별점 비교표                                                                     |
|  3  | **03_ConceptualModel_DataOverview** | 2x2 개념틀, 형식모형 스케치를 통해 가설(H1/H2/H2a)을 도출하고, 분석에 사용될 데이터(양자컴퓨팅 산업), 표본 구성, 변수를 소개합니다.                    | 권준                     | 변수 소개 순서를 종속변수(E, L) 우선, 이후 독립변수(V, F) 순으로 변경 | 🖼️Fig1_LV, 🗄️표본구성표, 🗄️변수정의·요약통계                                             |
|  4  | **04_EmpiricalMethodology**         | 약속 모호성(V), 유연성(F) 등 주요 변수의 측정 방법을 정의하고, 내생성 문제 해결을 위한 식별 전략과 분석 모형(OLS, Logit)을 설정하며 강건성 검증 계획을 제시합니다. | 권준, 김완                 | -                                             | 🗄️T_DescStats, 🗄️T_MainSpecs                                                 |
|  5  | **05_Results**                      | 실증 분석을 통해 가설(H1:초기 패널티, H2:후기 우위, H2a:상호작용)을 검증하고, 피벗/학습 등 메커니즘을 분석하며, 스펙 커브 분석 등으로 강건성을 확인합니다.        | 김완                     | -                                             | 🖼️Fig2_EVF, 🖼️Fig3_LVF, 🖼️Fig4_STV, 🗄️T1, 🗄️T2, 🗄️T_Mech, 🗄️T_SpecCurve |
|  6  | **06_Discussion_Conclusions**       | 연구 결과의 이론적, 관리적, 정책적 함의를 논의하고, 연구의 한계와 향후 연구 방향을 제시하며 핵심 공헌을 요약하여 결론을 맺습니다.                            | 어영담                    | -                                             | -                                                                              |


---
[[00_TOC 2025_11_16.excalidraw]]# Strategic Ambiguity   — 32 Paragraph Scaffold (6-section layout)

|   # | 역할                                                | 섹션                              | 파일                                          | 부사  | 🚨instruction                                                       | 🖼️fig, 🗄️table             |
| --: | ------------------------------------------------- | ------------------------------- | ------------------------------------------- | --- | ------------------------------------------------------------------- | ---------------------------- |
|   1 | Hook — 현상 제시 및 주목도 높은 사례                          | 01_Introduction                 | [[01-Intro-1_Hook]]                         | 정운  |                                                                     |                              |
|   2 | 실무적 중요성 — 왜 중요한가                                  | 01_Introduction                 | [[02-Intro-2_PracticalImportance]]          | 정운  |                                                                     |                              |
|   3 | 이론적 퍼즐 — 기존 이론의 모순                                | 01_Introduction                 | [[03-Intro-3_TheoreticalPuzzle]]            | 정운  |                                                                     |                              |
|   4 | 연구 질문 — 언제/왜 모호성이 유리한가                            | 01_Introduction                 | [[01-Intro-4_ResearchQuestion.md]]          | 정운  |                                                                     |                              |
|   5 | 접근 방법 — 산업/데이터/텍스트 분석                             | 01_Introduction                 | [[04-Intro-4_Approach_Context]]             | 정운  |                                                                     |                              |
|   6 | 핵심 발견 요약 — 3개 불릿                                  | 01_Introduction                 | [[05-Intro-5_KeyFindings]]                  | 정운  |                                                                     |                              |
|   7 | 기여 — 이론/실증/실무                                     | 01_Introduction                 | [[07-Intro-7_Progression]]                  | 정운  |                                                                     |                              |
|   8 | 문헌: 정보경제학/신호 이론 — 명확성=신뢰=투자                       | 02_LitReview_Contributions      | [[08-LitCon-1_InfoEcon]]                    | 정운  |                                                                     |                              |
|   9 | 문헌: 실물옵션/유연성 — 모호성=옵션=생존                          | 02_LitReview_Contributions      | [[09-LitCon-2_RealOptions]]                 | 정운  |                                                                     |                              |
|  10 | 우리의 위치 — 시간 분해 & 아키텍처 조건부, 차별점 표                  | 02_LitReview_Contributions      | [[10-LitCon-3_OurPositioning]]              | 정운  |                                                                     |                              |
|  11 | 개념틀 — 2×2(시간×레벨) 및 지배 논리                          | 03_ConceptualModel_DataOverview | [[11-Concept-1_Framework_2x2]]              | 권준  |                                                                     | 🖼️Fig1_LV                   |
|  12 | 형식모형 스케치 — max_V E[Opt(V;F)-InfoLoss(V)] - C(V;F) | 03_ConceptualModel_DataOverview | [[12-Concept-2_FormalModel_Sketch]]         | 권준  |                                                                     |                              |
|  13 | 가설 정식화 — H1/H2/H2a                                | 03_ConceptualModel_DataOverview | [[13-Concept-3_Hypotheses]]                 | 권준  |                                                                     | 🖼️Fig1_LV (재참조)             |
|  14 | 데이터 맥락 — 양자컴퓨팅 산업                                 | 03_ConceptualModel_DataOverview | [[14-DataOverview-1_Context_Quantum]]       | 권준  |                                                                     |                              |
|  15 | 표본 구성 — 출처/코호트/필터                                 | 03_ConceptualModel_DataOverview | [[15-DataOverview-2_Sample_Construct]]      | 권준  |                                                                     | 🗄️표본구성표                     |
|  16 | 변수 개관 — E/L/V/F 요약                                | 03_ConceptualModel_DataOverview | [[16-DataOverview-3_Variables_Overview]]    | 권준  | 기존에 v, f, e.l이었는데, E/L/V/F로 dependent then independent 변수 소개로 순서 정정 | 🗄️변수정의·요약통계                 |
|  17 | 측정 — 약속 모호성(V), 유연성(F) 등                          | 04_EmpiricalMethodology         | [[17-Method-1_Measurements]]                | 권준  |                                                                     |                              |
|  18 | 기초통계 — 요약통계/상관                                    | 04_EmpiricalMethodology         | [[18-Method-2_DescriptiveStats]]            | 권준  |                                                                     | 🗄️T_DescStats               |
|  19 | 식별 전략 — 내생성 논의                                    | 04_EmpiricalMethodology         | [[19-Method-3_Identification_Strategy]]     | 김완  |                                                                     |                              |
|  20 | 주요 사양 — E(OLS), L(Logit)                          | 04_EmpiricalMethodology         | [[20-Method-4_MainSpecs]]                   | 김완  |                                                                     | 🗄️T_MainSpecs               |
|  21 | 강건성 — 대체측정/표본제한/윈도우                               | 04_EmpiricalMethodology         | [[21-Method-5_RobustnessPlan]]              | 김완  |                                                                     |                              |
|  22 | 추정력/스케일링 — 해석 단위와 경제적 크기                          | 04_EmpiricalMethodology         | [[22-Method-6_StatPower_Scaling]]           | 김완  |                                                                     |                              |
|  23 | 결과: H1 — 초기 펀딩 패널티                                | 05_Results                      | [[23-Results-1_EarlyFundingPenalty]]        | 김완  |                                                                     | 🖼️Fig2_EVF, 🗄️T1           |
|  24 | 결과: H2 — 후기 성공 우위                                 | 05_Results                      | [[24-Results-2_LaterSuccessBenefit]]        | 김완  |                                                                     | 🖼️Fig3_LVF, Fig4_STV, 🗄️T2 |
|  25 | 결과: H2a — (V×F) 상호작용                              | 05_Results                      | [[25-Results-3_VxF_Interaction]]            | 김완  |                                                                     | 🖼️Fig3_LVF (재참조)            |
|  26 | 메커니즘 — 피벗/학습/행사가능성                                | 05_Results                      | [[26-Results-4_Mechanisms_Pivot]]           | 김완  |                                                                     | Fig4_STV (간접), 🗄️T_Mech     |
|  27 | 강건성 — 스펙 커브/안정성                                   | 05_Results                      | [[27-Results-5_Robustness_SpecCurve]]       | 김완  |                                                                     | 🗄️T_SpecCurve               |
|  28 | 이론적 함의 — Two-Audience, 다층 상호작용                    | 06_Discussion_Conclusions       | [[28-Discuss-1_TheoreticalImplications]]    | 어영담 |                                                                     |                              |
|  29 | 관리적 함의 — 약속 설계 규칙                                 | 06_Discussion_Conclusions       | [[29-Discuss-2_ManagerialImplications]]     | 어영담 |                                                                     |                              |
|  30 | 정책 함의 — 생태계 설계/평가 기준                              | 06_Discussion_Conclusions       | [[30-Discuss-3_PolicyImplications]]         | 어영담 |                                                                     |                              |
|  31 | 한계와 향후 연구                                         | 06_Discussion_Conclusions       | [[31-Discuss-4_Limitations_FutureResearch]] | 어영담 |                                                                     |                              |
|  32 | 결론 — 핵심 공헌 요약                                     | 06_Discussion_Conclusions       | [[32-Conclude-1_Conclusion]]                | 어영담 |                                                                     |                              |
