## 🗄️MT: Map & Terrain (첨부 사진 기반)

|모델|Founder Success Prior|World Success Posterior|Success Value|특징|
|---|---|---|---|---|
|**M1**|P (고정)|X (외생)|X(1)|• 성공확률 = 상수<br>• 학습 없음<br>• 정태적 모델|
|**M2**|X(0) → X(φ)|△ (Posterior 업데이트)|X(1)|• 성공확률 = 확률변수<br>• 베이지안 학습<br>• φ는 변하지만 가치 고정|
|**M2'**|X(0) → X(φ)|△ (Posterior 업데이트)|X(1) → X(φ)△(V)|• 확률과 가치 모두 내생화<br>• 완전 동적 모델<br>• τ 최적화 가능|

### 핵심 메시지

- **Direction Var**: △는 변동하지만 의사결정 변수 아님
- **X**: 고정된 외생변수
- **진화**: M1(외생) → M2(확률 내생화) → M2'(확률+가치 내생화)

## 수정된 1층 구조

### 1.1호 내용 수정

- ~~Tesla vs Better Place 비교~~ (제거)
- **성공확률의 내생화 진화**: M1 → M2 → M2'
- **🗄️MT**: 위 표 구조 적용

### 2.1호 확정

- **🖼️LT**: "Grow τ" 그림 (Nail → Scale)
- 정보 축적에 따른 τ 성장
- Few samples → Large samples
- Loose prior → Tight prior

이제 이론적 진화(MT)와 실제적 성장(LT)이 명확히 구분됩니다!