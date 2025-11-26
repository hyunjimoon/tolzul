#!/usr/bin/env python3
"""
Generate Section 02: Literature Review

Theoretical framework: Information Economics vs Real Options
Output: 02_LiteratureReview.md
"""

from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.scripts.paper_generation import OUTPUT_DIR

# Meta-Prompt approved by General Kim Wan
META_PROMPT = """
You are generating the Literature Review section for an academic paper on strategic vagueness.

TONE: Authoritative but critical. Position existing theories as incomplete, setting up your contribution.

STRUCTURE:
1. Information Economics Perspective (vagueness as information asymmetry - NEGATIVE view)
   - Akerlof (1970): Adverse selection
   - Spence (1973): Costly signaling
   - Shane & Cable (2002): Investor selection
   - Critique: Assumes vagueness is always bad

2. Real Options Perspective (vagueness as flexibility - POSITIVE view)
   - McGrath (1997): Discovery-driven planning
   - Levinthal & Wu (2010): Ambiguity in innovation
   - Gans, Stern & Wu (2019): Startup strategy as real option
   - Critique: Ignores heterogeneity in option value

3. Modularity Theory (SYNTHESIS - conditional view)
   - Baldwin & Clark (2000): Design rules
   - Schilling (2000): Modularity and innovation
   - Ethiraj & Levinthal (2004): Bounded rationality
   - GAP: Nobody connects modularity to communication strategy

4. Hypothesis Development Preview
   - H1: Vagueness → Early Funding (main effect, expected negative)
   - H2: Vagueness × Modularity → Growth (interaction, our contribution)

STYLE GUIDELINES:
- Each subsection: 3-4 paragraphs
- Summarize theory → Cite key papers → Identify limitation
- Use "However" transitions to signal theoretical gaps
- Build tension: "Prior work shows X, but overlooks Y"

CITATION STYLE: (Author, Year) format
"""


def generate_literature_review():
    """Generate Literature Review section"""

    content = """# 2. Literature Review

## 2.1 Information Economics: Vagueness as Adverse Selection

The dominant view in entrepreneurship finance treats vagueness as a signal of low quality. **Akerlof's (1970)** seminal "Market for Lemons" model predicts that information asymmetry between entrepreneurs and investors leads to adverse selection: high-quality ventures credibly signal competence through specific, verifiable claims, while low-quality ventures hide behind vague language. **Spence's (1973)** signaling theory formalizes this: costly signals (patents, prototypes, detailed business models) separate high-types from low-types precisely because vague claims are cheap talk.

Empirical work in entrepreneurship largely confirms this negative view. **Shane & Cable (2002)** find that social capital reduces information asymmetry, increasing funding likelihood. **Hsu (2007)** shows that affiliation signals (prestigious VCs, board members) correlate with higher valuations, implying investors value **specificity** in signals. **Zott & Huy (2007)** demonstrate that symbolic management — including specific narratives about legitimacy — attracts resources. The implicit assumption across this literature: **vagueness = incompetence or deception**.

However, this perspective overlooks a critical dimension: **strategic flexibility**. In highly uncertain environments, early specificity may constitute premature commitment to untested assumptions (Ries, 2011). Information economics treats uncertainty as static (known unknowns), but entrepreneurial contexts often involve **dynamic uncertainty** (unknown unknowns), where learning occurs through experimentation rather than ex-ante planning (Sarasvathy, 2001).

## 2.2 Real Options Reasoning: Vagueness as Strategic Flexibility

Real options theory offers a contrasting view: **vagueness preserves option value**. **McGrath (1997)** introduced discovery-driven planning, advocating for sequential commitments under uncertainty rather than comprehensive upfront plans. By deferring specification, entrepreneurs retain the right but not the obligation to pivot based on market feedback. This logic parallels financial options: vagueness maintains strategic flexibility to "exercise" alternative business models costlessly.

**Levinthal & Wu (2010)** formalize this in their model of opportunity evaluation: moderate ambiguity can be **advantageous** when the cost of gathering information exceeds the expected value of precision. **Gans, Stern & Wu (2019)** extend this to startup strategy, arguing that control rights (equity retention) function as real options to switch strategies without external constraints. Vagueness in initial positioning complements this by avoiding public commitments that would constrain future pivots.

Empirical evidence supports real options logic in R&D contexts (**Kogut & Kulatilaka, 2001**; **Adner & Levinthal, 2004**), but applications to **entrepreneurial communication strategy** remain limited. Moreover, real options theory implicitly assumes **costless switching** — a valid assumption for pure software products (cloud infrastructure scales and pivots easily) but invalid for hardware products (tooling, supply chains, regulatory certifications cannot be rapidly reconfigured).

## 2.3 Modularity Theory: Technological Architecture and Strategic Flexibility

Modularity theory bridges information economics and real options by specifying **when** flexibility is valuable. **Baldwin & Clark (2000)** define modularity as the degree to which a system's components can be separated and recombined. High modularity reduces coordination costs, enables parallel experimentation, and permits localized changes without system-wide redesign. **Schilling (2000)** shows that modularity accelerates innovation by decomposing complex problems into independent modules.

Critically, **Ethiraj & Levinthal (2004)** demonstrate that modularity's benefits depend on **landscape ruggedness**: in smooth landscapes (few interactions between components), modularity permits efficient local search. In rugged landscapes (many interdependencies), premature modularization can trap firms in local optima. This implies heterogeneity in the value of flexibility: modularity determines whether deferring commitment (via vagueness) yields **productive ambiguity** (cheap exploration) or **destructive ambiguity** (unresolved interdependencies).

However, **no prior work connects modularity to entrepreneurial communication strategy**. Existing research focuses on product architecture (Baldwin & Clark, 2000), organizational design (Sanchez & Mahoney, 1996), or industry structure (Schilling, 2000). We extend this logic to **positioning vagueness**: high modularity justifies vague initial claims because pivots are technically feasible; low modularity demands specificity because pivots are prohibitively costly.

## 2.4 Hypothesis Development

Synthesizing these perspectives, we propose:

**H1 (Main Effect - Information Economics)**: Strategic vagueness is **negatively** associated with early-stage funding success. On average, investors interpret vagueness as a signal of low quality or incompetence, consistent with adverse selection logic.

**H2 (Moderation - Real Options × Modularity)**: The negative effect of vagueness on growth outcomes is **attenuated** in high-modularity (software) ventures and **amplified** in low-modularity (hardware) ventures. Specifically:

- **H2a (Software)**: In software ventures, vagueness has a weaker negative effect (or potentially positive effect) on progression to late-stage funding (Series B+), because modularity permits costless pivots.

- **H2b (Hardware)**: In hardware ventures, vagueness has a stronger negative effect on progression, because low modularity renders pivots costly, making early vagueness a credible signal of unresolved technical risk.

This framework reconciles conflicting findings in prior work: vagueness is neither uniformly good nor bad, but **contingent** on underlying technological architecture.

---

**Generated from:** `generate_02_litreview.py`
**Meta-prompt:** See source code for LLM expansion guidance
**Key references to add:** Akerlof (1970), Spence (1973), Shane & Cable (2002), McGrath (1997), Gans et al. (2019), Baldwin & Clark (2000)
"""

    return content


def main():
    """Main execution function"""
    print("=" * 60)
    print("Generating Section 02: Literature Review")
    print("=" * 60)

    content = generate_literature_review()

    output_path = OUTPUT_DIR / "02_LiteratureReview.md"
    output_path.write_text(content)

    print(f"\n✅ Generated: {output_path}")
    print(f"📚 Key theoretical frameworks:")
    print(f"   - Information Economics (Adverse Selection)")
    print(f"   - Real Options Theory (Strategic Flexibility)")
    print(f"   - Modularity Theory (Technological Architecture)")
    print(f"\n📝 Next step: Review and expand with LLM using META_PROMPT")


if __name__ == "__main__":
    main()
