---
modified:
  - 2025-11-18T15:04:28-05:00
---
# Statement of Objectives: Ph.D. in Operations Research
## Coordinating Resource Partners Under Uncertainty

**Angie Hyunji Moon**  
MIT Operations Research Center Application

---

## I. Opening: Viewing My Life as a Product

**"How should its product management look like?"**

Over the past two years, I treated my doctoral pursuit itself as a venture—a product requiring deliberate design, stakeholder validation, and resource optimization. This wasn't metaphorical. Like any entrepreneur, I faced fundamental uncertainty across three dimensions: Could I build the technical capabilities (feasibility)? Would academic stakeholders value this research (desirability)? Could I secure the resources to sustain this journey (viability)?

The answer emerged through systematic experimentation. I didn't passively discover my calling—I actively designed it through coordinated uncertainty reduction. This process revealed a profound insight: **entrepreneurial success isn't about finding the right answer; it's about designing the right sequence of questions.**

That realization led me to Operations Research.

---

## II. The Evaluation Puzzle

Just as the **source of innovation** puzzled the marketing field in the 1970s and led to the birth of innovation management, the **source of evaluation** perplexes the innovation field in the 2020s. 

Entrepreneurs don't just create new products—they create new ways of evaluating success before standard metrics exist. Consider: how do you evaluate a venture when revenue doesn't exist at birth? You're solving for feasibility first before discovering the objective function:

```
max φ   subject to   φ ∈ {feasible set}
```

Through solving feasibility, you discover new evaluation metrics that become your objective function. This **meta-cognitive problem**—changing objectives during execution—is most emphasized in entrepreneurship due to short clock speeds. Yet existing frameworks lack formal decision rules for when to learn and when to commit.

With Professor Charles Fine, the pioneer of "Operations for Entrepreneurs," I first felt the outline of my calling. His framework identifies ten operational tools (Segment, Collaborate, Acculturate, Processify, Automate, Platformize, Replicate, Capitalize). But it lacked the answer to: **Which tool to deploy next? When to transition from flexibility to commitment? How to coordinate across stakeholders with limited budget?**

The last two years became my field experiment to answer these questions.

---

## III. Three Evaluations: A 2-Year Field Experiment

### The Fundamental Coordination Problem

Entrepreneurs must simultaneously satisfy three evaluations to survive:
1. **Technical Feasibility** (Can we build it?)
2. **Desirability** (Do customers want it?)  
3. **Financial Viability** (Will investors fund it?)

Rather than theorize abstractly, I tested this by pursuing "Operations for Entrepreneurs" as a venture itself. Critically, **the sequence mattered**. I didn't approach these three evaluations in parallel—I orchestrated them strategically, each building on the previous one's validation.

---

### A. Desirability FIRST: Do Customers Want This Research?

**Decision Logic**: Before investing years in technical development or seeking funding, I needed to validate whether academic stakeholders valued this research direction at all.

**Validation Event**: In 2023, Professor Scott Stern—the frontier leader in entrepreneurship research—invited me and Charlie Fine to the **Bayesian Entrepreneurship Conference** in Beijing. I presented my framework on promise precision and stakeholder coordination.

**The Layered Discovery**:  
What I discovered wasn't a simple yes/no validation. I uncovered **layered needs** across different stakeholder segments:

- **Layer 1 (Economists)**: Wanted Bayesian approaches to entrepreneurial decision-making
- **Layer 2 (Practitioners)**: Needed specific solutions like probabilistic programming tools  
- **Layer 3 (Policymakers)**: Required frameworks for ecosystem design

This layered structure revealed something fundamental: desirability isn't binary. It's a **hierarchical optimization problem** where different stakeholders weight dimensions differently. Leaders including Bernardo Camufco, Ramana Nanda, and Daniel Elfenbein called for exactly this kind of research, confirming both the general topic (Bayesian entrepreneurship) and specific technologies (probabilistic decision models).

**OR Insight**: This is multi-objective optimization. I couldn't just maximize value for economists—I needed a weighted objective function:

```
max Σⱼ wⱼ · V_j(research)   subject to   threshold constraints
```

But validation created a new question: was this technically feasible?

---

### B. Technical Feasibility SECOND: Can We Build This?

**Decision Logic**: Having confirmed desirability, I now needed to validate whether the technical approach was viable before committing limited resources.

**The Degeneracy Problem**:  
Entrepreneurial decision-making is special in two ways:
1. **Too many decision variables** (hundreds of possible actions)
2. **Too few constraints** initially (no revenue, no customers, no clear success metrics)

This generates **degeneracy**: most optimization methods fail when the feasible region is poorly defined. Traditional approaches assume:

```
max c^T x   s.t.   Ax ≤ b,  x ≥ 0
```

But for early ventures, the constraint matrix A is rank-deficient. The feasible region is too large, making every solution equally "optimal."

**Technical Validation**:  
I hypothesized that **program synthesis** in probabilistic programming could solve this. By interacting with frontier researchers—Josh Tenenbaum and Vikash Mansinghka at MIT's Probabilistic Computing Project—I collected feedback on technical feasibility.

**The Key Learning**: Resource rationality matters. Entrepreneurs operate under severe computational constraints (limited time, capital). Solutions must be **tractably computable**, not just theoretically optimal. This meant I needed to simplify my initial complex Bayesian models into threshold rules founders could actually use.

**OR Insight**: This validated my research direction while constraining methodology. I needed Operations Research methods that balance rigor with computational tractability—Bayesian models that can run in minutes, not days; optimization rules that practitioners can apply without PhD-level expertise.

---

### C. Layered Pairing: Needs × Solutions

**The Discovery Process**:  
Between desirability validation (summer 2023) and technical validation (fall 2023), I didn't just collect binary yes/no answers. I discovered an **ordered structure** to both needs and solutions.

**Needs Layers** (from customer side):
1. Bayesian approach to entrepreneurial decisions (conceptual)
2. Probabilistic programming for uncertainty (methodological)  
3. Resource-rational heuristics for founders (practical)

**Solution Layers** (from supplier side):
1. Program synthesis theory (from Josh/Vikash)
2. Computational implementation (Stan, Arviz)
3. Operational tools mapping (from Charlie Fine)

**The Pairing Problem**:  
My job became: **sequence the matching** of need-solution pairs to maximize the probability of successful field formation. This is fundamentally an OR problem:

```
max Σᵢⱼ p(match_ij) · V_ij   
s.t.  ordering constraints (some pairs must precede others)
      budget constraints
      time constraints
```

**Experimental Validation**:  
To test this layered pairing, I organized the **Bayesian Entrepreneurship Seminar** in spring 2024, inviting both Josh Tenenbaum (solutions) and Scott Stern (needs) to discuss intuitive game theory with 30+ PhD students. The successful engagement validated that proper pairing of needs and solutions creates field momentum.

**OR Insight**: This isn't just matching—it's **sequenced matching** under constraints. Some need-solution pairs create foundation for others. The order matters.

---

### D. Financial Viability THIRD: Can We Fund This Journey?

**Decision Logic**: Only after validating desirability (stakeholders want this) and technical feasibility (I can build this) did it make sense to address financial viability. Seeking funding before validation would have meant pitching an unvalidated value proposition.

**The Resource Constraint**:  
PhD programs don't provide enough runway for high-uncertainty, high-impact research. I needed **angel investors** who had faith in my process based on observing my style of execution—not just its promised outcomes.

**Solution**: I found three angels:
1. **Professor Charlie Fine** (operational and flexibility)
2. **Professor Scott Stern** (strategic and commitment)  
3. **My parents** (financial buffer + unconditional faith in the path i choose)

They provided runway to pursue this research without forcing premature commitment to safer topics.

**Burn Rate Management**:  
I complemented their investment by lowering my burn rate—adopting a minimalist lifestyle that reduced funding needs by 25%. This extended my runway from ~12 months to 18 months, creating space for iteration and pivot.

**OR Insight**: This is **option pricing** under resource constraints:

```
max E[V_success · 1_{success}] - C_burn_rate · T
s.t.  T ≤ runway_available
```

By reducing burn rate (C), I increased available time (T) to run experiments, which increased success probability.

---

### E. The Meta-Recursive Validation

**"I was doing the problem I'm formalizing."**

The profound realization: my 2-year journey **was itself an instance** of the coordination problem I'm trying to solve. I was:

- Coordinating three resource partners (technical suppliers, commercial customers, financial investors)
- Under fundamental uncertainty (Would this work? Would people care?)
- With constrained resources ($200K over 2 years, limited time)
- Making sequential decisions (which validation to pursue next?)
- Maintaining strategic ambiguity (vague enough to pivot, precise enough to mobilize support)

This recursive structure provides a unique form of validation: **existence proof by construction**. The framework I'm proposing isn't just theoretical—it's the methodology I actually used to get here. This result is well recognized in entreprenuership literature.

---

## IV. Why This Requires Operations Research

Let me be specific about what emerged from coordinating these three evaluations that demands OR methods.

### 1. Multi-Objective Optimization Under Constraints

Each resource partner evaluates my research differently:

**Objective Function**:
```
max  w_tech · V_tech + w_comm · V_comm + w_fin · V_fin
```

**Subject to**:
- Budget constraint: Σⱼ cⱼaⱼ ≤ $200K
- Time constraint: T ≤ 36 months  
- Threshold constraints: Vⱼ ≥ μⱼ for all j

**The Primal-Dual Structure**:  
When I developed my STRAP framework, I discovered that **regulatory certifiers had the highest shadow price (λ)**—counterintuitively, they were the binding constraint, not investors. Only Operations Research provides the formal machinery to identify such non-obvious bottlenecks through dual variable analysis.

### 2. Sequential Decision-Making Under Uncertainty

At each stage, I faced: **Should I invest more in validation (reducing uncertainty) or commitment (executing on current best guess)?**

**Early phase**: Heavy investment in validation—conferences, interviews, feedback. High information cost delayed publication but preserved flexibility to pivot.

**Middle phase**: After confirming desirability and feasibility, I committed to specific hypotheses for "When Vagueness Pays" paper. This locked research direction but enabled completion.

**Current phase**: Transitioning to MIT PhD requires **irreversible commitment**—five years focused on this agenda.

**The Dynamic Programming Formulation**:
```
V_t(state) = max { V_commit(state), -c_info + E[V_{t+1}(state')] }
```

Commit when: `V_commit ≥ E[V_continue] - c_info`

Optimal stopping theory tells me: commit when expected value of additional information falls below option value of preserved flexibility. This is the **4i threshold** from my Optimal Ignorance paper:

```
Commit when V ≥ 4i
```

### 3. Coordination Mechanism Design

The deepest OR contribution comes from formalizing **how** to coordinate partners, not just **that** coordination matters.

**The Revelation Problem**:  
Different partners respond to different signals:
- Technical partners want rigorous proofs and computational efficiency
- Commercial partners want empirical validation and case studies  
- Financial partners want institutional prestige and publication records

**Naive Approach**: Optimize for one audience, hope others follow.  
**Result**: Attract technical partners but lose commercial support (too abstract), or vice versa (not rigorous enough).

**OR Solution**: Multi-stakeholder Bayesian game with incomplete information. I design promises with **strategic vagueness**:
- Precise where precision helps screening
- Vague where vagueness preserves adaptation capacity

The optimal promise vector τ* balances:
- Information costs (partners discount vagueness)  
- Option values (vagueness preserves pivot capability)

This mechanism design problem requires game-theoretic OR methods to derive incentive-compatible revelation mechanisms.

---

## V. Research Example: "When Vagueness Pays"

My dissertation applies these OR methods to a specific question: **When should entrepreneurs make precise commitments versus preserve strategic ambiguity?**

**The OR Formulation**:

**Optimization Objective**:  
```
max E[venture_success] across funding stages (Series A → Series B → Exit)
```

**Decision Variable**: Promise precision τ ∈ [0,1]  
(0 = maximally vague, 1 = maximally precise)

**Constraints**:
- Budget: limited capital for experiments
- Thresholds: minimum investor acceptance, customer adoption, regulatory approval  
- Time: 36-month observation window

**Uncertainty Sources**:
- Market demand unknown at founding
- Technology feasibility uncertain until prototyping
- Investor preferences heterogeneous and partially observable

**Key Finding**:  
Promise vagueness reduces Series A funding by 18% (information cost penalty) but increases Series B probability by 8 percentage points **only for software ventures** with low pivot costs (option value benefit).

This conditional result—negative effects early, positive effects later, but only when exercisability is high—required OR methods to formalize and test.

**Methods Employed**:
- Stochastic modeling: Bayesian belief updating with heterogeneous priors
- Optimization: First-order conditions for optimal precision choice  
- Large-scale empirics: Logit estimation on 137,597 ventures
- Mechanism analysis: Shadow price interpretation revealing that desirability constraints bind before feasibility constraints

Each component draws directly from OR curriculum. The contribution isn't documentation—it's deriving **actionable decision rules** from optimization under uncertainty.

---

## VI. Why MIT Operations Research Center?

MIT ORC provides three unique advantages for this research agenda.

### 1. Methodological Foundation

My research requires simultaneous mastery of:
- **Optimization theory** (deriving closed-form solutions for precision choice)
- **Stochastic modeling** (belief updating under incomplete information)  
- **Empirical methods** (large-scale estimation with computational constraints)
- **Mechanism design** (incentive-compatible stakeholder coordination)

MIT ORC faculty provide world-leading expertise in each domain:
- Dimitris Bertsimas (optimization)
- Patrick Jaillet (stochastic optimization)
- David Simchi-Levi (empirical operations)  
- Vivek Farias (discrete choice and mechanism design)

No other program offers this comprehensive methodological toolkit focused on decision-making under uncertainty.

### 2. Substantive Grounding: Fine + Stern Collaboration

My dissertation bridges operations and strategy through unprecedented collaboration:

**Charles Fine** brings forty years of operational expertise in clockspeed theory, automotive supply chains, and entrepreneurial operations. His "Operations for Entrepreneurs" framework identifies the critical tools. I formalize these tools as discrete actions in an optimization framework, deriving decision rules for sequencing and resource allocation.

**Scott Stern** brings Bayesian entrepreneurship methods and large-scale empirical research. Our co-authored "When Vagueness Pays" paper provides empirical validation. I extend his belief-updating models by endogenizing the precision choice itself—making uncertainty resolution a strategic variable rather than passive process.

This Fine-Stern-Moon collaboration creates something new: **prescriptive analytics for entrepreneurial execution**. Operations (Fine) meets Strategy (Stern) through Operations Research methods (my contribution).

### 3. Real-World Testbed: MIT Mobility Initiative

The MIT Mobility Initiative (MMI) provides the perfect empirical application for validation. Electric vehicle infrastructure deployment faces exactly the coordination problem I'm formalizing:

**Multiple stakeholders**: OEMs, battery suppliers, charging infrastructure operators, utilities, regulators, customers

**Fundamental uncertainty**: Demand elasticity unknown, technology evolution uncertain, policy shifts unpredictable

**Resource constraints**: $50M infrastructure budget, 5-year deployment timeline

**Critical decisions**: Where to locate chargers? When to commit to specific standards? How to coordinate across stakeholders with conflicting objectives?

Working with Charlie Fine and MMI team would provide:
- Real-world problem validation (do my decision rules actually help?)
- Data access (proprietary infrastructure planning data)  
- Stakeholder feedback (utilities and OEMs testing my frameworks)
- Policy impact (influence actual EV transition strategy)

This theory-practice integration defines MIT's "Mens et Manus" philosophy.

---

## VII. Three-Paper Dissertation and Timeline

**Paper 1: "When Vagueness Pays"** (with Scott Stern)  
*Status*: Near completion, presented at Bayesian Entrepreneurship Conference  
*OR methods*: Large-scale logit, heterogeneous treatment effects, specification curves  
*Timeline*: Submit to Management Science by end of Year 1  
*Contribution*: Establishes empirical patterns motivating theoretical development

**Paper 2: "STRAP: Multi-Stakeholder Coordination Framework"** (with Charles Fine)  
*Status*: Conceptual framework complete, beginning formal modeling  
*OR methods*: Primal-dual optimization, shadow price interpretation, dynamic programming  
*Timeline*: Working paper by end of Year 2, test on MMI project  
*Contribution*: Formalizes Fine's operational tools as optimization problem

**Paper 3: "Ecosystem Design for Flexible Innovation"** (policy focus)  
*Status*: Case collection beginning  
*OR methods*: Mechanism design, platform optimization, comparative institutional analysis  
*Timeline*: Complete by end of Year 3, use as job market paper  
*Contribution*: Translates theoretical insights into policy-relevant recommendations

**Timeline**:
- **Year 1**: Complete coursework, finish Paper 1, begin Paper 2 modeling
- **Year 2**: Field research with MMI, complete Paper 2, begin Paper 3 cases  
- **Year 3**: Job market preparation, complete Paper 3, dissertation proposal
- **Year 4**: Revisions, final defense, transition to faculty position

---

## VIII. Long-Term Vision: Establishing OR for Entrepreneurship

After completing my PhD, I want to establish **Operations Research for Entrepreneurship** as a recognized field. Currently, entrepreneurship research is dominated by strategy (what to do) and finance (how to fund). **Operations Research provides the missing piece: how to execute under uncertainty with constrained resources.**

My vision includes:

**Academic contribution**: Publish in top OR journals (Operations Research, Management Science, Production and Operations Management) while reaching entrepreneurship scholars (Strategic Management Journal, Organization Science). Bridge these communities through methodological workshops and special issues.

**Teaching**: Develop "Operations for Entrepreneurs" course that teaches OR methods through entrepreneurial applications. Create open-source software tools (extending my Stan/Arviz development work) that make advanced methods accessible to practitioners.

**Practical impact**: Work with venture capital firms to improve screening using precision-based signals. Advise accelerators on program design that builds exercisability. Consult with policymakers on ecosystem design for flexible innovation.

**Institutional building**: Organize conferences bridging OR and entrepreneurship. Create research centers combining rigorous methods with practical problem-solving. Train next generation of scholar-entrepreneurs who master both theory and execution.

---

## IX. Conclusion: Coordinating Partners Under Uncertainty

The last two years taught me that entrepreneurial success—whether building ventures or building research programs—depends on coordinating multiple resource partners under fundamental uncertainty with constrained resources.

I tested this by pursuing "Operations for Entrepreneurs" itself as a venture:
- **Technical feasibility**: Validated through interactions with MIT Probabilistic Computing  
- **Desirability**: Validated through Bayesian Entrepreneurship Conference engagement
- **Financial viability**: Secured through advisor support and minimalist lifestyle

This experience revealed that the coordination problem requires Operations Research. Not just optimization (though that's necessary). Not just stochastic modeling (though that's critical). But the **integration** of optimization, uncertainty, and constraints into actionable decision rules that work at scale.

"When should entrepreneurs commit versus preserve flexibility?" sounds like a strategy question. But answering it requires:
- Formalizing objectives (maximize expected venture value)
- Quantifying tradeoffs (information cost versus option value)  
- Respecting constraints (budget, time, stakeholder thresholds)
- Deriving decision rules (optimal precision = f(value, cost, exercisability))
- Validating at scale (137,597 ventures, not case studies)

This is Operations Research.

I don't just want to understand entrepreneurial decision-making. I want to **optimize** it. That's why I'm applying to MIT ORC.

Thank you for considering my application.

---

**Word count**: ~4,200 words  
**Contact**: angiemoon@mit.edu  
**Portfolio**: [GitHub](https://github.com/hyunjimoon)
