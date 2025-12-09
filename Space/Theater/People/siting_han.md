---
modified:
  - 2025-10-21T09:06:48-04:00
  - 2025-11-21T16:22:05-05:00
  - 2025-11-22T05:19:53-05:00
---

[[Siting AV Commit.txt]]

### Application of the "Vague Promise Pays" Framework to the Autonomous Vehicle (AV) Industry

My research aims to test the hypothesis that the value of a vague promise is moderated by the venture's environment, specifically its "reconfiguration cost." Based on our discussion, the Autonomous Vehicle (AV) industry provides a perfect real-world laboratory for this analysis, superior to the broader EV market because its core architectural debates are still active and directly map to my hardware vs. software dichotomy.

Here is how I will apply the four-dimensional framework to the AV industry:

#### 1. Technology & Reconfiguration Cost

This is the central pillar of the analysis. The primary technological schism in the AV industry—**LiDAR vs. Vision**—serves as an excellent proxy for high and low reconfiguration costs.

- **High Reconfiguration Cost (Hardware-Centric): LiDAR Approach**
    
    - **Description:** Companies building their AV stack around LiDAR and other expensive sensor suites (radar, etc.) are making a significant upfront hardware commitment. As discussed, this hardware is costly, and the process of upgrading or switching to a different type of LiDAR involves significant expense and engineering effort.
    - **Hypothesis:** For these ventures, a vague promise is likely to be detrimental. Investors will demand a high degree of _specificity_ regarding the technology's performance, cost-down roadmap, and target application. Vagueness would signal a lack of technical direction and an inability to manage high capital expenditures. The "option value" of vagueness is low because the chosen hardware path locks them in.
    - **Data Analysis:** I will predict that LiDAR-based companies with higher "vagueness scores" in their descriptions will see lower early-stage funding and a lower probability of later-stage success.
- **Low Reconfiguration Cost (Software-Centric): Vision Approach**
    
    - **Description:** Companies following the vision-only approach (pioneered by Tesla) treat the car as a compute platform. Once the initial hardware (cameras and processing unit) is installed, improvements are delivered via over-the-air (OTA) software updates.
    - **Hypothesis:** This model has a much lower reconfiguration cost. Therefore, a vague promise could "pay" by preserving flexibility. A founder can promise a general goal like "achieving full self-driving" without committing to a specific intermediate feature set or timeline. The ability to pivot and improve through software makes the initial promise's ambiguity an asset, allowing the company to explore and adapt.
    - **Data Analysis:** While vagueness may still negatively impact initial funding (as it can signal risk), the negative effect should be significantly weaker than for LiDAR companies. More importantly, I hypothesize that for these software-centric firms, initial vagueness may show a positive (or less negative) correlation with _long-term_ success, as it allows for the exploration that leads to a better product-market fit. This directly tests the idea that flexibility moderates the value of vagueness.

#### 2. Customer & Market Segmentation

The technology choice directly forces a specific customer and market strategy, providing another clear variable for analysis.

- **LiDAR-based systems** are extremely expensive, making them unviable for the mass consumer market. Their business model must target commercial applications where the high cost can be amortized over constant use.
    
    - **Customer Segment:** Robotaxi services (e.g., Waymo) or commercial logistics (trucking, delivery), where vehicles must run 12-24 hours a day to be profitable.
    - **Application:** A promise from such a company must be specific to this B2B market.
- **Vision-based systems** have a much lower bill-of-materials cost, making them suitable for the private passenger car market.
    
    - **Customer Segment:** Mass-market consumers (private ownership). The business model can even resemble a SaaS model, selling software upgrades (like FSD) to an existing hardware base.
    - **Application:** The promise can be broader, focusing on safety, convenience, and progressive feature enhancement for a large, heterogeneous customer base.

#### 3. Competition & Strategic Disclosure

The AV space is intensely competitive, making strategic communication critical.

- **Insight:** As you noted, while founders may fear that competitors will steal their ideas, true success comes from execution. A founder must be transparent with the _right_ people (investors, key talent) to build a team and secure capital.
- **Application:** My research, based on public PitchBook data, captures the public-facing promise. I hypothesize that successful AV companies, regardless of their technology, are very specific in their private pitches to VCs. However, their public statements may be strategically vague to avoid tipping off competitors. The research can't capture the private conversations, but it can analyze if a pattern of public vagueness combined with strong founder credibility (see next point) leads to funding success.

#### 4. Organization & Founder Credibility

The credibility of the founding team is a major factor, especially in a field requiring deep, specialized expertise like AI and robotics.

- **Insight:** A highly credible founder (e.g., a known expert from Google/Waymo, Tesla, or a top university) can raise capital on a much vaguer promise than an unknown team. You gave the example of Mira Murati raising funds for her new venture without even a product description.
- **Application:** I will incorporate founder/team credibility as a key variable in my model. I predict that the negative effect of vagueness on funding will be significantly dampened or even reversed for teams with high credibility. An investor's bet is on the team's ability to navigate the uncertainty, making the specifics of the initial promise less critical.

### Research Plan Summary

1. **Filter Data:** Isolate companies within the PitchBook dataset that are specifically in the Autonomous Vehicle (AV) space.
2. **Categorize by Technology:** Classify each company based on its core technological approach (LiDAR-centric, Vision-centric, etc.) to create a proxy for "reconfiguration cost."
3. **Measure Vagueness:** Analyze the company descriptions to generate a "vagueness score" based on the number of abstract keywords, lack of specific metrics, etc.
4. **Regress and Analyze:** Run regressions to model the relationship between `vagueness`, `technology category (reconfiguration cost)`, `founder credibility`, and the dependent variables: `early-stage funding amount` and `later-stage funding success`.

By using the AV industry, I can create a clean, compelling test of my core thesis and generate specific insights into how strategic ambiguity functions in a capital-intensive, high-tech industry.
---


사람보고 한다. 실패했는데도 다시 투자하고 싶은 창업가들은
- 그 사람만의 잘못이 아님을 감지
- trust worthy
- specific한 약속 check한다
- 

--

[[10-09|25-10-09]]
[[siting_han2.txt]]

* 텀시트 협상 시, trustable한 조건
   * 돈만은 ᄂᄂ (교환가치가 전부인 사람은 x)
   * 12개 조건 중 3~4개 우선순위가 있는 사람 (책임감)
   * 123은 알고있는데 456도 생각해본 사람 (내 모델 확장해줌)
   * 애틋함이 느껴지는 사람 (현실감, 확률적 사고, 판타지만 팔진 않는 사람)
* sailing단계에선 capex/payroll증가현상 - 탑에게 쏠림 
* one venture per person은 vc가 필요없어지고, layoff스트레스 줄고, 가장 안전한 직업이 될거다

---
## 추가로 관심 가질 만한 내용들

**Angie의 "optimal ignorance" 연구**

- precision을 "earn"해야 한다는 개념 - 스타트업이 초기에 너무 구체적이면(Better Place처럼) 실패할 수 있음
- Tesla는 낮은 precision으로 시작 → 성공 / Better Place는 높은 precision으로 시작(덴마크+이스라엘 동시 진출, 배터리 인프라 등) → 실패
- 정밀도를 높이려면: 정확한 가치 예측 + 낮은 정보 통합 비용(문화가 조직을 묶어줌)

**투자 평가 프로세스**

- 순서: market size → timing → people → valuation (가장 유연한 것)
- 초반 15분 안에 "이 사람이 뭘 하는지 아는가" 판단됨
- founder가 pivot 능력이 있는지가 중요 (특정 아이템보다 본질적 능력)

**장기 목표 alignment의 중요성**

- 장기 목표(IPO 의지 등)가 맞아야 단기 목표(거버넌스 개선, 투명성 등)도 align 가능
- 비상장 minority stake는 liquidity가 없어서 장기 비전 공유가 필수

**문화/조직 관련**

- "nail-scale-sail" 프레임워크 + "nail-in-scale" 개념 (lifecycle에서 다시 nail로 돌아가야 생존)
- 역사 케이스 스터디의 중요성 - "learning history is the best way of looking for future"

**개인적 통찰**

- FOMO도 충분한 동기다 - 코치가 말하길 "어떤 이유든 미치게 만들면 그게 맞는 이유"
- 중국은 exit market이 없어서 zombie (walking dead; go to bank) company 많음 vs 미국은 M&A 활발
- MIT 환경이 "시간 여행기" - 과거를 돌아보며 미래 배울 수 있는 최적의 장소
- 한국 문화 - 열정을 강요하는 문제 ("찜질방처럼 서서히 뜨거워져야지 갑자기 확 열 올리면 안 됨")

**파트너/사랑 기준 (Angie가 분석한 것)**
- 나보다 어떤 면에서 우월하거나 내 모델을 확장시켜주는 사람 (123만 아니라 456도 생각해낸 사람)
- sadness/bittersweet함이 있는 사람 - 현실적이고 확률적 사고를 하는 사람
- "I think the desire to do something grows the intelligence to think probabilistically"

흥미로운 대화였네요! 특히 투자자 관점과 학술 연구 관점이 섞여있는 게 독특합니다.