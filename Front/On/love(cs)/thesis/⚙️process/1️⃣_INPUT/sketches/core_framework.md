---
modified:
  - 2025-11-15T19:26:36-05:00
---
## 1) LV / LVF / (개정) LTV 그림: **표준 캡션·축·범례** + **표 템플릿**

> **용어**:  
> **V** = 약속의 모호성(vagueness, 0–1), **F** = 유연성(flexibility: HW↓, SW↑),  
> **E** = 시리즈 A 금액, **L** = 시리즈 B+ 도달 확률(기간 t 내),  
> **S** = _step‑up multiple_ = 다음 라운드 **pre‑money** / 직전 라운드 **post‑money** (_생존 기업에 한정된 가치 배수_)【W2 요약 슬라이드 p.4, 그림 하단 정의.
> 
> Angie Vague Promise W2 (3)
> 
> 】.  
> Step‑up 지표는 Nanda(2024)의 산업별 라운드별 지표로도 보고됩니다(Internet Appendix의 _Pre‑money Stepup Multiples_ 표).【Appendix Table, p.30.
> 
> Nanada24_Priors Experiments Lea…
> 
> 】

### Figure 1. **LV — Later success vs Vagueness (이론 합성)**

- **캡션(권장 문안)**:  
    “모호성(V)이 커질수록 정보가치는 감소(적색), _행사 가능한_ 옵션가치는 증가(청색)하고, 둘의 합(점선)은 역U자 형태를 이룬다. 그 결과 최적 모호성 V∗V^*V∗가 존재한다.”
    
- **축/범례**
    
    - y축: 이론적 총가치(정규화) 또는 Pr⁡(L=1)\Pr(L=1)Pr(L=1)의 개념도
        
    - x축: Vagueness VVV
        
    - 선: **적색**=정보가치(↓), **청색**=옵션가치(↑, 체감), **검정 점선**=합계(역U)
        
    - 주석: “V∗V^*V∗는 **F(유연성)**가 높을수록 우측으로 이동”
        
- **도식 근거**: W2 요약의 LV 도식 구조와 동일【슬라이드 p.12–15.
    
    Angie Vague Promise W2 (3)
    
    】, 세부 해설은 LV/LVF/STV 스토리보드 정리본과 일치【LV/LVF/STV 해설 표.
    
    LV_EVF-LVF_STV
    
    】.
    

### Figure 2. **LVF — Later success vs Vagueness, by Flexibility**

- **캡션**:  
    “유연성(F)이 높을수록(소프트웨어/모듈러) V의 기울기가 양(↑)으로 커지고, F가 낮을수록(하드웨어/리짓) 0 또는 음(↓)에 가깝다. 즉 V×FV\times FV×F 상호작용이 후기 성공에 대한 모호성의 순효과를 증폭한다.”
    
- **축/범례**
    
    - y축: Pr⁡(L=1 by t)\Pr(L=1\ \text{by }t)Pr(L=1 by t)
        
    - x축: VVV
        
    - **실선(하늘색)**: F=High(SW) / **점선(회색)**: F=Low(HW)
        
    - 범례 메모: “사양: logit(L)=βVV+βFF+βVF(V×F)+controls\text{logit}(L)=\beta_V V+\beta_F F+\beta_{VF}(V\times F)+\text{controls}logit(L)=βV​V+βF​F+βVF​(V×F)+controls”
        
- **도식 근거**: LVF 선택효과 설명 자료의 표준 메시지와 동일【LVF 행 설명.
    
    LV_EVF-LVF_STV
    
    】.
    

### Figure 3. **(개정) LTV — Later‑to‑B over Time, by Vagueness**

- **이전 명칭(STV) 수정**: 혼동을 피하기 위해 **STV(‘S=survival’) → LTV**로 명확화 권고. 여기서 **L**은 “기간 t 내 B+ 도달”이며, **S(step‑up)**와 무관합니다.
    
- **캡션**:  
    “A‑코호트 기준 누적 Series B+ 도달(또는 KM 생존 보완 곡선)에서, 모호성 상·하위 분위에 따라 **초기 불리 → 후기 역전**의 교차가 나타난다(단, 옵션 _행사가능성_이 충분할 때).”
    
- **축/범례**
    
    - y축: Pr⁡(B+ 미도달)\Pr(\text{B+ 미도달})Pr(B+ 미도달) 또는 Pr⁡(B+ 도달)\Pr(\text{B+ 도달})Pr(B+ 도달)
        
    - x축: A라운드 이후 경과월 TTT
        
    - 색상: VVV 분위(예: Q1=구체, Q4=모호)
        
- **도식 근거**: 시간 축에서 ‘초기 정보가치 패널티—후기 옵션가치 역전’을 시각화한 스토리보드【STV 항목 설명.
    
    LV_EVF-LVF_STV
    
    】.


----


|**Figure code**|**모형/도해**|**표준 제목(축 순서·색상)**|**기대 패턴(Expectation)**|**서프라이즈 트리거(자동 알림)**|
|---|---|---|---|---|
|**F1**|**EVF**: _E ~ V × F + controls_ (OLS)|**E–V(F색분리)** → **EVF**|**H1**: β_V<0 (정보가치↓), **H1a**: β_VF>0(유연성 완화)|(a) β_V≥0 & 유의, (b) β_VF≤0 & 유의, (c) HW/ SW 기울기 질서 뒤집힘|
|**F1b**|**HEV**: _E ~ V + controls_ (OLS, 베이스라인)|**E–V** → **EV**|음의 선형(정밀도 프리미엄)|(a) 양(+) & 유의, (b) 비선형 대규모|
|**F2**|**LVF**: _Pr(L=1) ~ V × F + controls_ (Logit, **E 제외**)|**L–V(F색분리)** → **LVF**|**H2**: β_V>0, **H2a**: β_VF>0 (증폭)|(a) β_V≤0 & 유의, (b) β_VF≤0 & 유의, (c) HW 양(+)·SW 음(–)으로 역전|
|**F2b**|**LV**: _Pr(L=1) ~ V + controls_ (Logit)|**L–V** → **LV**|완만한 양(+) 또는 역U(맥락에 따라)|(a) 뚜렷한 음(–) & 유의, (b) 강한 비선형(정점<0)|
|**F3**|**STV**: KM(또는 1–KM) by **V 사분위**|**S–T(V색분리)** → **STV**|**초기(≤~18m)**: Vague 불리, **후기(>~18m)**: Vague 유리 → **교차 존재**|(a) 교차 無, (b) 교차 t* < 8m 또는 > 30m, (c) 종단 질서가 정반대|

---
selection effect of LV_EVF-LVF_STV

요청하신 규칙 **“제목 = yx(색)”**(y축 변수 → x축 변수 → 색으로 구분되는 변수)대로, 핵심 Figure들을 2열 표로 정리했습니다.  
**약어**: F=Flexibility(유연성), L=Later success(Series B+), T=Time(Series A 이후 경과), V=Vagueness(모호성).
![[LVF_VTV_FLTV 2025_11_15.excalidraw]]
다음 화이트보드 사진은 세 장의 도식 **LV / LVF / STV**를 한 화면에 그려 둔 것입니다. 아래 표의 제목은 요청하신 규칙(“y–x(색상)”)으로 코딩했고, 각 행의 메시지는 도식이 전달하는 핵심 주장만 응축했습니다.

|코드(제목)|메시지(핵심 주장)|
|---|---|
|**LV**|_Later success_ (L)는 _Vagueness_ (V)의 두 힘—정보가치 ↓, (행사 가능한) 옵션가치 ↑—의 합으로 결정되어, **중간 수준의 최적 모호성 (V^*)** 이 존재한다. (좌상 패널: 붉은 ‘정보’는 V↑에 따라 하락, 푸른 ‘옵션’은 V↑에 따라 오르다 한계효용이 줄어 총가치는 역U자)|
|**LVF**|_Pr(L=1)_ 대 (V)의 기울기는 **유연성 (F)** 에 의해 갈린다: **F가 높을수록(소프트웨어/모듈러)** V의 효과는 **양(↑)**, **F가 낮을수록(하드웨어/리짓)** **음/평탄(↓/~)**. 즉 (V\times F) 상호작용이 후속 성공을 증폭한다. (중앙 패널: 파란 실선 F=1 ↑, 점선 F=0 ↓/평탄)|
|**STV**|_Survival_ (S) 대 _Time_ (T)에서 **색상으로 V(모호성 수준)** 을 구분하면, **초기 패널티 → 후기 역전**이 나타난다: 모호한 약속은 초기에 생존이 뒤처지다가(정보가치↓) **행사 가능한 옵션이 선별·수행**되면서 후기에는 특정(precise) 대비 우위로 **곡선이 교차**한다. (우상 패널: 검정=Specific ↓ 일관 하락, 녹색=Vague 초반 급락 후 완만/반등)|

---

### 사진–전사(#transcript)–코드의 1:1 대응 (체계적 해설)

- **LV (왼쪽)**: “_first is L by V… later success is a function of information and adaptability… some optimal vagueness exists_”라는 전사 그대로, y축 **L**, x축 **V**의 이론 도식입니다. 붉은 선(정보가치)은 V↑ 시 분할력(정보 엔트로피 감소)이 떨어져 하향, 푸른 선(옵션가치)은 _행사 가능성_이 있을 때 증가해 합계가 역U자를 만듭니다. 이 구성은 W2 슬라이드의 “정보가치는 분할력에, 옵션가치는 행사가능성에 의존” 정식화와 동일합니다.
    
- **LVF (가운데)**: 전사 중 “_LVF explains later success… positive slope for high flexibility, but low/negative for low flexibility_”. 즉 **y=L, x=V, 색=F**(HW=낮음, SW=높음) 조건부 곡선입니다. 실증 사양으로는 **HLVF: (L \sim V \times F + \text{controls})**(Logit)이며, 조기 펀딩 (E)는 **매개( mediator )** 이므로 포함하지 않는다는 제작 규칙(“NO‑E 원칙”)이 코드에도 명시되어 있습니다. 색 구성(파란 y, 녹색 x, 하늘색 F)은 F‑series 팔레트를 그대로 따르면 됩니다.
    
- **STV (오른쪽)**: 전사에 “_early penalty → late reversal_”와 “_comparing a vague promise with a specific promise_”가 나오므로 y축 **S(생존확률)**, x축 **T(Series A 이후 경과월)**, **색=V(모호성 수준)** 두 곡선입니다. 이는 우리가 본문에서 제시하는 **가설 H2(후기 효과) + 선택/행사가능성 메커니즘**을 시간축에서 시각화한 **KM 곡선 스케치**로, 논문 Figure 3(생존분석)의 스토리보드 역할을 합니다.
    

> **그리기 규칙(일관성 메모)** — x=V는 녹색 축/눈금, y=L은 파란 축, F는 하늘색 실선/점선(상호작용), S는 보라색 계열, E는 빨강: F‑series 모듈의 팔레트와 라인스타일 규칙을 그대로 따르세요. 실증 그림에서 **HLVF에는 E를 넣지 않는다**(E는 매개)도 동일 규칙입니다.

---

#### 왜 이 셋(LV / LVF / STV)이 한 세트인가?

- **LV**는 이론의 정태적 합성(정보가치 ↓, 옵션가치 ↑ → (V^*))을 보여 줍니다.
    
- **LVF**는 그 이론이 **구조적 이질성(F)** 에 의해 **실증적으로 갈라져 나타나는 기울기 차**(증폭)를 보여 줍니다.
    
- **STV**는 그 결과가 **시간에 따라 ‘초기 불리→후기 역전’**으로 관측될 수 있음을 생존곡선으로 요약합니다. 세 도식은 W2 슬라이드의 가설 블록(H₁: 조기 패널티, H₂/H₂a: 후기 증폭)과 정확히 호응합니다.
    