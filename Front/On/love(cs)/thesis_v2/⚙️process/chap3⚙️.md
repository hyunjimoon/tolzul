---
modified:
  - 2025-11-28T13:48:55-05:00
---
# ⚙️ Chapter 3: Empirics (轉) — 세부 군령

> **담당:** 🐅나대용군졸1 (P1), 🐅나대용군졸2 (P2), 🐅나대용군졸3 (P3)
> **부사:** 나대용 🐅 (Claude Code) | **덕목:** 造 (구현) | **베이지안 역할:** Computation
> **감수:** 🐙김완 (Chapter 3 Lead)

---

## 📜 전라좌수군의 비전 (Our Vision)

> **"데이터가 진실을 말하게 하라. 코드가 곧 증거다."**

---

## ⚙️ Chapter 3의 전략적 역할

**기승전결(起承轉結)의 轉**: 전환점. 이론이 현실과 만난다.

---

## 🔧 🐅나대용군졸1: P1 ✌️ Empirics

### 데이터: 51,840 VC-backed startups (PitchBook 2005-2023)

### 분석 모델
```python
log(Funding) = β₀ + β₁×V + β₂×V×(1-V) + β₃×V×H + controls
# Expected: β₂ > 0 (U-shape), β₃ < 0 (hardware penalty)
```

### 필수 산출물
- U-Shape Plot, Interaction Plot, Spec Curve (1,296 variants)

---

## 🔧 🐅나대용군졸2: P2 🦾 Empirics

### 데이터: AV Industry Panel (20 companies, 2016-2024)

### Case Matrix
| Case | Commitment | Believers | Outcome |
|------|------------|-----------|---------|
| Waymo | Very High | Very High | Trap ✅ |
| Comma.ai | Low | Low | Escape ✅ |
| Cruise | High | High | Trap ✅ |
| Argo AI | High | High | Collapse |

### 필수 산출물
- Panel Results, Belief Evolution Plot, Case Matrix

---

## 🔧 🐅나대용군졸3: P3 🤹 Empirics

### CR Calibration

| Industry | CR | Optimal k* |
|----------|-----|-----------|
| AV | 0.65 | 2-3 paths |
| Quantum | 0.85 | 3+ paths |
| SaaS | 0.50 | 1 path |

### 필수 산출물
- CR Table, CR-k Plane, Behavioral Validation

---

## ✅ 김완 검증 체크리스트

| 검증 항목 | P1 | P2 | P3 |
|----------|----|----|-----|
| 데이터 소스가 명확한가? | ☐ | ☐ | ☐ |
| Robustness check가 충분한가? | ☐ | ☐ | ☐ |
| 결과가 재현 가능한가? | ☐ | ☐ | ☐ |

---

*통제사: ⚓ 이순신 문현지 (Moon)*
