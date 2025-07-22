# The Promise Vendor: When and Why Entrepreneurs Rationally Overpromise

## Abstract

Do entrepreneurs systematically overpromise? This paper argues that apparent overpromising emerges as optimal strategy from venture creation's temporal structure. We expand the newsvendor framework to a "promise vendor" model where promise level φ becomes the decision variable, creating new conditional probabilities of funding F|φ and delivery D|φ. Three mechanisms drive rational overpromising: (1) temporal asymmetry where immediate underage costs Cu dominate discounted overage costs Co, (2) fundability mediating deliverability through resource provision, and (3) heterogeneous industry clockspeeds affecting cost perception. The model derives optimal promise levels that increase with underage costs and venture value V, explaining why software startups promise more boldly than aerospace ventures. Rather than cognitive bias, overpromising reflects adaptation to environments where failing to launch devastates more than failing after launch.

# 1. Introduction 

## Module 1: The Phenomenon of Entrepreneurial Overpromising

Tesla's 2007 Roadster promised "0-60 in <4 seconds, 236-mile range, zero emissions by 2008." This bold claim secured $45M Series D funding despite obvious production uncertainties. Rather than aberration, such ambitious promises pervade entrepreneurship. SpaceX promised commercial space flight when no private company had reached orbit. Theranos promised revolutionary blood testing with unproven technology. Even successful ventures like Airbnb promised "book rooms with locals" when they had three air mattresses. This pattern suggests systematic forces rather than individual overconfidence.

We argue these apparently excessive promises emerge from rational optimization within entrepreneurship's unique cost-time structure. Unlike established firms optimizing known operations, entrepreneurs create new variables through their promises. The promise level φ generates conditional probabilities—funding given promise F|φ and delivery given promise D|φ—that didn't exist before articulation. This generative aspect separates entrepreneurial promising from operational planning.

## Module 2: Temporal Cost Asymmetry Between Cu and Co

The promise-then-deliver sequence creates fundamental temporal asymmetry. Underage cost Cu strikes immediately when ventures fail to secure funding—for Tesla, $80M in sunk R&D would evaporate without Series D. Overage cost Co arrives later when funded ventures fail delivery—potentially $100M in reputation damage and lawsuits. But time transforms these nominally similar costs. The discount factor δ makes Co × δ < Cu even when raw magnitudes suggest caution.

This temporal structure alone can justify bold promises. Consider an entrepreneur facing Cu = $80M (immediate death) versus Co = $100M (future failure). With standard discount rate δ = 0.9, the effective comparison becomes $80M versus $90M, already tilting toward bolder promises. Add uncertainty about future enforcement—will investors really pursue full damages?—and the calculus shifts further. The sequence matters: promise happens now when Cu looms, while delivery happens later when Co has been discounted by time, uncertainty, and potentially changed circumstances.

## Module 3: Expanding Variables Through φ Creates Society-Entrepreneur Interactions

Promise level φ expands the decision space, creating new variables that mediate entrepreneur-society exchange. Society faces a statistical learning problem: inferring true deliverability p(D|φ) from observed promise distributions p(φ). The required sample size for reliable inference depends critically on industry clockspeed μ₁. Fast clockspeed industries generate more observations per period but may exhibit higher variance σ²(φ), creating a paradox—software's rapid iteration provides more data points yet each contains less information due to heterogeneity.

Social planners must calibrate sample size n ∝ μ₁ × σ²(φ) when optimizing cost coefficients (Co, Cu). A software ecosystem with μ₁ = 3 (3x faster than baseline) and σ²(φ) = 4 (high heterogeneity) requires n = 12x baseline samples for equivalent statistical power. This explains why software VCs rely on pattern recognition across hundreds of pitches while biotech investors deep-dive into few candidates. The learning challenge compounds because p(D|φ) exhibits fat tails—Tesla's 300-mile promise concentrated probability at extreme success or complete failure, eliminating moderate outcomes that aid inference.

Funding F mediates this inference problem by creating endogeneity: p(D|φ,F=1) > p(D|φ) as resources enable delivery. Society cannot simply average observed outcomes but must model the funding-delivery interaction. The entrepreneur exploits this complexity, optimizing φ knowing society learns slowly in high-clockspeed environments. This information asymmetry persists longer when clockspeed-induced heterogeneity overwhelms the increased sampling rate, allowing rational overpromising to persist as equilibrium strategy.

# 2. Literature Review

## Module 4: Promise Attitudes Vary Systematically Across Industries

Traditional manufacturing exhibits systematic underpromising—aerospace contractors pad schedules, pharmaceutical companies extend trial timelines. Software exhibits systematic overpromising—"fail fast" culture encourages ambitious targets. This heterogeneity reflects different cost structures. In aerospace, Co >> Cu because reputation determines future contracts while upfront costs spread across corporate balance sheets. In software, Cu >> Co because missing market windows devastates while users forgive launch bugs.

We model this heterogeneity through environment-specific parameters. Let safety criticality γ ∈ [0,1] scale overage costs as Co(γ) = Co₀(1 + γ). Aerospace with γ ≈ 0.9 faces amplified failure costs. Let market velocity ν ∈ [0,1] scale underage costs as Cu(ν) = Cu₀(1 + ν). Software with ν ≈ 0.8 faces amplified opportunity costs. The optimal promise φ* = f(Cu/Co) increases with market velocity and decreases with safety criticality, generating observed industry patterns.

## Module 5: Promise Vendor Extends Newsvendor Along Two Dimensions

The newsvendor model optimizes inventory Q against uncertain demand D, minimizing expected mismatch costs. The promise vendor optimizes promise level φ against uncertain deliverability, but with crucial differences. First, uncertainty and decision variables swap places. Newsvendor faces uncertain demand D (given by market) and chooses inventory Q (under control). Promise vendor faces uncertain deliverability D|φ (partially under control through effort) and chooses promise φ (signaling device). This reversal means promises partially create the uncertainty they must satisfy.

Second, funding introduces endogeneity absent in newsvendor. Inventory doesn't affect demand—stocking more newspapers doesn't make people want to read more. But promises affect deliverability through funding—promising more attracts resources that enable delivery. The newsvendor's p(D) remains fixed regardless of Q. The promise vendor's p(D|φ) shifts with φ through the mediating p(F|φ). This endogeneity transforms static optimization into dynamic strategy where initial promises cascade through funding to delivery.

## Module 6: Three-Component Optimization With Value Creation

Beyond newsvendor's two-component cost minimization, promise vendor adds value creation V. The objective function expands from min{CoPo + CuPu} to min{CoPo + CuPu - VPm} where Pm represents matching probability (funded and delivered). This third component fundamentally alters optimization. With only costs, minimal promises minimize expected loss. With value, optimal promises balance three probabilities: p(D=0,F=1) for overage cost, p(D=1,F=0) for underage cost, and p(D=F=1) for value creation.

Value magnitude determines optimal boldness. When V << Cu ≈ Co, ventures minimize promises to avoid either failure mode. When V >> Cu, Co, ventures maximize matching probability even at higher individual failure risks. For Tesla, V ≈ $300M from Roadster revenue plus Model S option value exceeded both Cu ≈ $80M and Co ≈ $100M, justifying ambitious promises. The three-component structure explains why entrepreneurs rationally promise beyond what pure cost minimization suggests—they optimize for astronomical upside, not just failure avoidance.

# 3. Model Development: The Rationality of the Entrepreneurial Promise

[Continue with existing Model Development section...]

# 4. Discussion

[Continue with existing Discussion section...]

# 5. Appendix: Model Derivations

[Continue with existing Appendix section...]

# 6. References

[Continue with existing References section...]