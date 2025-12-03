---
collection:
  - "[[Space/Lab/Papers]]"
author_ids:
  - John Sillince
  - Paula Jarzabkowski
  - Duncan Shaw
field:
  - 👾cog  # Cognition
  - 🎯str  # Strategy
  - 🔬mth  # Methodology
thesisPaper: U
thesisChapter: T
year: 2012
rank: 9  # Critical for measurement
research_stream:
  - Strategic Ambiguity
  - Rhetorical Construction
  - Measurement
tags:
  - rhetoric
  - language-analysis
  - operationalization
  - measurement
  - empirical-qualitative
  - oil-framework
  - qualifying-exam
created: 2025-11-05
modified:
  - 2025-11-05T00:00:00-05:00
connections:
  extends:
    - "[[📜Eisenberg1984_Ambiguity_Communication]]"  # Ambiguity concept
  applied_in:
    - Your empirical measurement strategy
  related_to:
    - "[[📜Abdallah2014_DoubleEdge_Ambiguity]]"  # What they measure
---

# 📜 Shaping Strategic Action Through Rhetorical Construction of Ambiguity

## 🗄️1: Core Framework (Q&A Format)

| Section | 🔐Research Question | 🔑Key Message & Framework | 📐Formal Concept | 🧱Literature Brick |
|---------|-------------------|-------------------------|-----------------|-------------------|
| **Main Thesis** | How is ambiguity actively constructed? | Ambiguity is NOT absence of clarity but ACTIVE RHETORICAL ACHIEVEMENT through specific linguistic devices | τ as measurable linguistic property | • Rhetoric theory<br>• Green (1995) rhetoric strategy |
| **Operationalization** | How to measure τ? | COUNT linguistic features: abstract terms, hedging, modal verbs (→ low τ) vs concrete terms, specifics (→ high τ) | **τ-index**: (Concrete + Specific) / (Abstract + Hedges) | • Computational linguistics<br>• Content analysis methods |
| **Strategic Use** | Why construct ambiguity? | Enable action by allowing multiple stakeholder groups to see their interests while maintaining flexibility | Active construction (not accident) | • Burke (1969) rhetoric<br>• Suddaby & Greenwood (2005) rhetoric |

## 🗄️2: Theoretical Position

### Extends
- [[📜Eisenberg1984_Ambiguity_Communication]]: From "ambiguity exists" → "how it's made"
- **Key Addition**: OPERATIONALIZATION - how to measure ambiguity

### **CRITICAL for Your Empirical Paper**
This paper provides METHOD to measure τ from text

### Related Work
- [[📜Abdallah2014_DoubleEdge_Ambiguity]]: Provides theory of what to measure; Sillince shows HOW

## 🗄️3: Linguistic Devices for Ambiguity

| Device Type | Increases Ambiguity (↓τ) | Decreases Ambiguity (↑τ) |
|-------------|------------------------|-------------------------|
| **Vocabulary** | Abstract nouns ("value", "transformation") | Concrete nouns ("revenue", "product X") |
| **Specificity** | General statements | Specific numbers/metrics |
| **Modality** | "might", "could", "possibly" | "will", "is", "must" |
| **Hedging** | "arguably", "potentially" | Direct assertions |
| **Metaphors** | Rich metaphors (multiple mappings) | Literal language |
| **Quantification** | Vague quantities ("several", "many") | Exact quantities ("12", "50%") |

## 💭 Critical Insights for OIL Framework

### THE Measurement Paper

**Your Challenge**: How to measure τ (promise precision) in venture data?

**Sillince's Answer**: COUNT linguistic features in company descriptions

### Computational Approach

```python
def measure_tau(text):
    """
    Measure promise precision from company description
    Higher score = Higher τ (more precise)
    Lower score = Lower τ (more vague)
    """
    # Precision indicators (increase τ)
    concrete_terms = count_concrete_nouns(text)
    specific_metrics = count_numbers_percentages(text)
    definitive_language = count_modal_certainty(text)  # will, is, must
    
    # Vagueness indicators (decrease τ)
    abstract_terms = count_abstract_nouns(text)
    hedging = count_hedge_words(text)  # potentially, arguably
    modal_uncertainty = count_modal_possibility(text)  # might, could
    metaphors = count_metaphorical_language(text)
    
    # Calculate τ-index
    precision_score = concrete_terms + specific_metrics + definitive_language
    vagueness_score = abstract_terms + hedging + modal_uncertainty + metaphors
    
    tau_index = precision_score / (vagueness_score + 1)  # +1 to avoid division by zero
    
    return tau_index
```

### Example Analysis

**High τ (Precise Promise)**:
> "We will capture 15% market share in cloud storage by delivering 99.99% uptime through our patented compression algorithm."

- Specific metric: "15% market share"
- Concrete deliverable: "99.99% uptime"
- Definitive: "will capture"
- Technical specificity: "patented compression algorithm"
- **τ-index: HIGH**

**Low τ (Vague Promise)**:
> "We're transforming how organizations think about data, potentially enabling new paradigms of information management through innovative approaches."

- Abstract: "transforming", "paradigms"
- Hedging: "potentially"
- Vague: "innovative approaches"
- Metaphorical: "think about data"
- **τ-index: LOW**

## 🎯 Research Implications

### For Your Empirical Paper

**CRITICAL ENABLER**:
Without Sillince's framework, you cannot measure τ
With it, you can process large-scale text data

### Measurement Strategy

```python
# For each venture in dataset
for venture in ventures:
    # Get company descriptions over time
    desc_t0 = venture.description_at_founding
    desc_t1 = venture.description_at_series_a
    desc_t2 = venture.description_at_growth
    
    # Measure τ trajectory
    tau_0 = measure_tau(desc_t0)
    tau_1 = measure_tau(desc_t1)
    tau_2 = measure_tau(desc_t2)
    
    # Calculate evolution
    delta_tau_early = tau_1 - tau_0
    delta_tau_late = tau_2 - tau_1
    
    # Test hypotheses
    # H1: tau_0 → early_funding
    # H2: delta_tau_late → later_success
```

### Validation Approaches

**1. Inter-rater Reliability**:
- Have humans rate sample on "vague" vs "precise"
- Compare with computational τ-index
- Should correlate r > 0.7

**2. Known Cases**:
- Tesla early (expect low τ): "sustainable transportation"
- vs later (expect high τ): "500,000 Model 3s/year"
- Measure τ trajectory matches expected

**3. Cross-sectional Validation**:
- Compare ventures in different industries
- Tech should have lower τ than manufacturing?
- Mission-driven lower τ than profit-focused?

## 🔬 Detailed Operationalization

### Dictionary Development

**Concrete Terms** (increase τ):
- Products: "smartphone", "software", "vehicle"
- Metrics: "units", "revenue", "users"
- Specifications: "algorithm", "patent", "protocol"

**Abstract Terms** (decrease τ):
- Concepts: "innovation", "transformation", "paradigm"
- Values: "sustainability", "empowerment", "impact"
- Processes: "enabling", "facilitating", "disrupting"

**Hedge Words** (decrease τ):
- "potentially", "arguably", "possibly"
- "might", "could", "may"
- "somewhat", "relatively", "partially"

### Contextual Coding

**Important**: Same word can be concrete or abstract

"Platform" in context:
- Concrete: "Our iOS platform handles 1M requests/second"
- Abstract: "We're building a platform for the future of work"

**Solution**: Use NLP to capture context (not just word counting)

## 🖼️ Rhetorical Ambiguity Framework

```
Low τ Construction:           High τ Construction:
                             
Abstract Nouns               Concrete Nouns
    +                            +
Modal Uncertainty            Definitive Statements
    +                            +
Hedging Language             Specific Metrics
    +                            +
Metaphors                    Literal Description
    ↓                            ↓
AMBIGUOUS MESSAGE            PRECISE MESSAGE
    ↓                            ↓
Multiple Interpretations     Single Interpretation
    ↓                            ↓
Unified Diversity            Narrow Focus
```

## ✅ Action Items for 中군님

- [ ] **CRITICAL FOR EMPIRICS**: This paper enables your measurement
- [ ] **Build τ-index**: Implement computational measure
- [ ] **Validate**: Test on known cases (Tesla, Better Place)
- [ ] **Scale**: Apply to all 29 ventures in dataset
- [ ] **Test H1 & H2**: With measured τ values

## 📚 Implementation Sequence

**Week 1**: 
1. Read Sillince carefully (focus on linguistic devices)
2. Build dictionary of concrete/abstract/hedge terms

**Week 2**:
3. Implement τ-index calculator in Python
4. Test on 5 sample ventures
5. Validate against human raters

**Week 3**:
6. Apply to full dataset
7. Check distribution (any outliers?)
8. Run H1 and H2 regressions

---

**핵심 for 필사즉생**: 
이 논문 = Your empirical paper의 핵심 infrastructure
Without Sillince: Cannot measure τ
With Sillince: Can process all 29 ventures + test hypotheses
