---
collection:
  - "[[Space/Lab/Papers]]"
author_ids:
  - jan_van_mieghem
field:
  - 🐅ops
year: 1998
journal: Management Science
module: "Real Options in Operations"
tags:
  - flexibility
  - capacity-investment
  - demand-uncertainty
  - newsvendor
created: 2025-11-26
---

```svg
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a1a2e"/>
      <stop offset="100%" style="stop-color:#16213e"/>
    </linearGradient>
    <linearGradient id="orange" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#f39c12"/>
      <stop offset="100%" style="stop-color:#e74c3c"/>
    </linearGradient>
  </defs>
  
  <!-- Background -->
  <rect width="800" height="600" fill="url(#bg1)"/>
  
  <!-- Grid: 2x2 -->
  <line x1="400" y1="80" x2="400" y2="580" stroke="#ffffff20" stroke-width="2"/>
  <line x1="20" y1="330" x2="780" y2="330" stroke="#ffffff20" stroke-width="2"/>
  
  <!-- Title -->
  <text x="400" y="50" fill="url(#orange)" font-size="24" font-weight="bold" text-anchor="middle" font-family="Arial">
    Optimal Investment in Flexible Capacity
  </text>
  <text x="400" y="72" fill="#888" font-size="14" text-anchor="middle" font-family="Arial">
    Van Mieghem (1998) • Management Science
  </text>
  
  <!-- Q1: 기(起) - 현상 제시 -->
  <rect x="30" y="90" width="360" height="230" rx="10" fill="#ffffff08"/>
  <text x="50" y="120" fill="#3498db" font-size="16" font-weight="bold" font-family="Arial">🐢 기(起): The Paradox</text>
  
  <text x="50" y="150" fill="#ecf0f1" font-size="13" font-family="Arial">"When demand is perfectly correlated,</text>
  <text x="50" y="170" fill="#ecf0f1" font-size="13" font-family="Arial">why invest in flexibility?"</text>
  
  <!-- Diagram: Two factories -->
  <rect x="70" y="190" width="60" height="40" fill="#e74c3c" rx="5"/>
  <text x="100" y="215" fill="white" font-size="10" text-anchor="middle">Dedicated A</text>
  <rect x="150" y="190" width="60" height="40" fill="#3498db" rx="5"/>
  <text x="180" y="215" fill="white" font-size="10" text-anchor="middle">Dedicated B</text>
  <text x="230" y="215" fill="#888" font-size="20">vs</text>
  <rect x="260" y="190" width="80" height="40" fill="#9b59b6" rx="5"/>
  <text x="300" y="215" fill="white" font-size="10" text-anchor="middle">Flexible A+B</text>
  
  <text x="50" y="270" fill="#f1c40f" font-size="12" font-family="Arial">📚 Prior: Newsvendor (Arrow 1951), Fine & Freund (1990)</text>
  <text x="50" y="290" fill="#888" font-size="11" font-family="Arial">Traditional view: High correlation → No flexibility value</text>
  
  <!-- Q2: 승(承) - 이론 -->
  <rect x="410" y="90" width="360" height="230" rx="10" fill="#ffffff08"/>
  <text x="430" y="120" fill="#e67e22" font-size="16" font-weight="bold" font-family="Arial">🐅 승(承): The Theory</text>
  
  <text x="430" y="150" fill="#ecf0f1" font-size="13" font-family="Arial">Key Insight: Margin matters more than correlation</text>
  
  <!-- Formula box -->
  <rect x="440" y="165" width="300" height="50" fill="#2c3e50" rx="5"/>
  <text x="590" y="195" fill="#f39c12" font-size="14" text-anchor="middle" font-family="monospace">
    Flex Value = f(Δmargin, cost_ratio)
  </text>
  
  <text x="430" y="240" fill="#ecf0f1" font-size="12" font-family="Arial">• Even ρ = +1 (perfect correlation):</text>
  <text x="445" y="260" fill="#2ecc71" font-size="12" font-family="Arial">→ Flexibility valuable if margin spread exists</text>
  <text x="430" y="285" fill="#ecf0f1" font-size="12" font-family="Arial">• Investment cost vs. operational benefit tradeoff</text>
  
  <text x="430" y="310" fill="#f1c40f" font-size="11" font-family="Arial">H: Flex investment ↑ when |margin_A - margin_B| ↑</text>
  
  <!-- Q3: 전(轉) - 결과 -->
  <rect x="30" y="340" width="360" height="230" rx="10" fill="#ffffff08"/>
  <text x="50" y="370" fill="#e74c3c" font-size="16" font-weight="bold" font-family="Arial">🐙 전(轉): The Evidence</text>
  
  <!-- Result visualization -->
  <text x="50" y="400" fill="#ecf0f1" font-size="12" font-family="Arial">Analytical Optimization Results:</text>
  
  <!-- Bar chart -->
  <rect x="70" y="420" width="120" height="20" fill="#e74c3c"/>
  <text x="200" y="435" fill="#ecf0f1" font-size="11">Low margin spread: Dedicated wins</text>
  <rect x="70" y="450" width="200" height="20" fill="#9b59b6"/>
  <text x="280" y="465" fill="#ecf0f1" font-size="11">High margin spread: Flex wins</text>
  <rect x="70" y="480" width="250" height="20" fill="#2ecc71"/>
  <text x="330" y="495" fill="#ecf0f1" font-size="11">ρ=1 + high spread: Still flex!</text>
  
  <text x="50" y="540" fill="#888" font-size="11" font-family="Arial">Counter-intuitive: Correlation ≠ flexibility killer</text>
  
  <!-- Q4: 결(結) - 함의 -->
  <rect x="410" y="340" width="360" height="230" rx="10" fill="#ffffff08"/>
  <text x="430" y="370" fill="#9b59b6" font-size="16" font-weight="bold" font-family="Arial">👾 결(結): Startup Implications</text>
  
  <text x="430" y="400" fill="#ecf0f1" font-size="13" font-family="Arial">For Your Venture:</text>
  
  <text x="430" y="430" fill="#2ecc71" font-size="12" font-family="Arial">✓ Multi-product portfolio = Real option value</text>
  <text x="430" y="455" fill="#2ecc71" font-size="12" font-family="Arial">✓ Focus on margin differentials, not just demand</text>
  <text x="430" y="480" fill="#2ecc71" font-size="12" font-family="Arial">✓ Flexible capability > Perfect forecasting</text>
  
  <text x="430" y="515" fill="#f1c40f" font-size="12" font-family="Arial">📚 Must Read:</text>
  <text x="430" y="535" fill="#888" font-size="11" font-family="Arial">• Fine & Freund (1990) - Flexible manufacturing</text>
  <text x="430" y="550" fill="#888" font-size="11" font-family="Arial">• Jordan & Graves (1995) - Process flexibility</text>
</svg>
```

# Optimal Investment in Flexible Capacity

## Summary
Van Mieghem (1998) proves that flexible production capacity has value even when product demands are perfectly positively correlated—contradicting the intuition that flexibility only matters when demands move oppositely. The key driver is the **margin spread** between products, not demand correlation.

## Research Question
Under what conditions should firms invest in flexible (multi-product) capacity versus dedicated (single-product) capacity when facing uncertain demand?

## Key Concepts

### Flexibility Premium
The additional value of flexible capacity comes from the ability to shift production toward higher-margin products after demand is revealed, regardless of correlation structure.

### Margin Spread Effect
Even with ρ = +1 correlation, if product A has margin $10 and product B has margin $2, flexible capacity allows capturing the upside of A while avoiding the downside of B.

## Main Results

### Counter-Intuitive Finding
Perfect positive correlation does NOT eliminate flexibility value. The traditional view (flexibility only valuable with negative correlation) is incomplete.

### Optimal Investment Rule
Invest in flexibility when:
- Margin differential between products is high
- Flexibility cost premium is moderate
- Demand uncertainty is substantial

## Critical Insights

> **Scott Stern Application**: This maps directly to entrepreneurial strategy—keeping multiple strategic options open has value even when market outcomes are correlated, because the **value capture** differs across strategies.

> **Charlie Fine Application**: The operational system design (flexible vs. dedicated) must account for margin economics, not just demand pooling.

## Methodology
**Approach**: Analytical optimization (multi-product Newsvendor extension)
**Data**: Theoretical model with closed-form solutions
**Analysis**: Comparative statics on correlation, margins, and costs

## Connections

**Builds on**:
- [[📜arrow51_optimize(inventory, decisions)]] - Newsvendor foundation
- Fine & Freund (1990) - Flexible manufacturing systems

**Relates to**:
- [[📜Gans19_EntrepreneurialStrategy]] - Multiple viable alternatives
- [[📜VassoloAnandFolta04_Portfolios]] - Option portfolio non-additivity

## Startup Strategy Application

| Situation | Implication |
|-----------|-------------|
| Multiple product ideas with different margins | Flexible platform development valuable |
| Correlated market outcomes | Don't abandon optionality prematurely |
| High margin spread | Prioritize capability switching over forecasting |

---

*"Flexibility's value comes not from hedging demand, but from capturing margin differentials."*
