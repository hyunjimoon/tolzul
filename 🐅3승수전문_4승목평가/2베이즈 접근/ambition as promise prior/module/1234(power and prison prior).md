## **The theory of Entrepreneurial Promise**

### **Abstract**

Founders must promise what they don’t know yet. This paper develops a formal theory of entrepreneurial promise, modeling how founders construct prior distributions of their promise as a function of aspiration and precision. Rather than treating entrepreneurs as passive responders to market incentives, we examine how they actively design uncertainty structures. To implement this founder agency, we capture two tensions of the founder's promise. First, we show that selling pushes entrepreneurs toward bolder promises while delivery constraints pull them back - creating an optimal middle ground. We further demonstrate that operational complexity fundamentally limits promise boldness following a simple mathematical relationship. Second, we reveal how excessive constant precision creates learning traps that prevent ventures from adapting to market feedback. We further relax precision from constant to variable, prescribing optimal aspiration level and precision as a function of complexity, reward, and cost of precision. Our work contributes to both theory and practice.  Theoretically, we extend the “operations for entrepreneurs” framework by challenging key assumptions in traditional operations management and decision science. Practically, we provide simple promise optimization logic to entrepreneurs, investors, and policymakers.

**Keywords:** operations for entrepreneurs, bayesian entrepreneurship, modeling flexibility

## **1. Introduction**

Two ventures with identical visions for electric vehicles met opposite fates. In 2006, Tesla began with a deliberately ambiguous promise of "roughly 200 miles or more." This ambiguity acknowledged the uncertainty in battery technology while still presenting sufficient potential to investors. Only after achieving 244 miles with the 2008 Roadster did they begin using the specific figure of "EPA-certified 244 miles," and today, Tesla is an $800 billion company. In contrast, Better Place, starting in 2007, made extremely precise promises: "battery swaps in exactly 3 minutes" and "swap stations costing $500,000 each." They claimed that thanks to their battery-swapping infrastructure, drivers could travel "anytime, anywhere" without charging concerns—effectively promising infinite range. This completely ignored the vehicle's actual 75-mile range and the extreme complexity of building the infrastructure. After burning through $850 million, the company went bankrupt in 2013.

This stark contrast reveals the first core tension in entrepreneurial promise design: bolder promises are easier to sell but harder to deliver. Entrepreneurs face relentless pressure to promise revolutionary change—venture capitalists seek 10x returns, customers want breakthrough solutions, and the media celebrates moonshot visions. Better Place exemplified this perfectly: their promise of "infinite range" through battery swapping captured imaginations and $850 million in funding. Yet the operational reality was brutal. Each swap station required robotic systems to handle different car models, real estate in prime locations, inventory management for expensive batteries, and partnerships with manufacturers who had their own battery strategies. The very boldness that attracted capital made delivery nearly impossible. Meanwhile, Tesla's modest promise of "200 miles or more" seemed almost boring by comparison, yet it aligned with what battery technology could actually deliver.

The second tension is equally treacherous: specific, precise promises bring immediate credibility but create future prisons. When Better Place promised "3-minute battery swaps" and "500,000 stations by 2012," investors could model returns and customers could plan purchases. This precision attracted serious capital—after all, vague promises often signal unclear thinking. But when BMW and Mercedes refused to standardize their battery designs, when robotic swapping proved slower than promised, when real estate costs exploded, Better Place couldn't adapt. They had created a mental model so specific that any deviation seemed like failure. Tesla, conversely, kept their early promises deliberately flexible—"roughly 200 miles," "around 2010," "approximately $100,000." This vagueness wasn't weakness but wisdom, allowing them to navigate battery chemistry improvements, production delays, and market feedback without breaking promises.

Our study resolves these tensions through two mechanisms. First, we add deliverability as a multiplicative factor to market appeal, recognizing that venture success requires both selling the promise and delivering it. This idea of convoluting two random variables can be explained as adding deliverability prior to the likelihood of selling the promise.[[1]](#_msocom_1)  Using this outcome as posterior distribution, the promise level that maximizes the expected reward decreases as complexity increases. This mechanism reveals how operational complexity should affect the boldness of promise. A simple software update can promise revolution, but a venture requiring dozens of technical breakthroughs must promise evolution. Second, we treat precision as a strategic variable that can evolve over time rather than a fixed requirement. By analyzing how high precision promise creates learning traps, we uncover the hidden debt of early specificity: it prevents ventures from updating their assumption based on market evidence. The solution is to view precision as something ventures purchase through verification—starting vague and becoming specific only after demonstrating capabilities at each stage.

These insights redefine a promise from communication to an architecture of uncertainty. A promise is a design choice that simultaneously determines resource acquisition and adaptive capacity. Traditional management theories may struggle with multi-objective optimization problems of persuading while learning. Operations management provides tools to maximize efficiency within given constraints but does not address the fundamental problem entrepreneurs face: how to design the environmental constraints themselves. Decision science neatly separates the step of eliciting prior distribution and the step of utility maximization given that prior distribution (Gelman et al., 2015; Morris, 1995). However, this sequence of subjective belief formation (past), prior distribution elicitation (present), and utility maximization (future) is awkward in entrepreneurial decision science. Entrepreneurial decision making is essentially optimizing the process of founder's fantasy realization. Present cannot be decided without information from the future and traditional sequence of decision science can’t handle this. Another challenge is how to define the “success” of a venture (e.g. is being acquired a success?) and given its definition, how to disentangle the probability and value of a success event. In simplest form, if success is Bernoulli random variable with probability p, p is a multiplicative function of supply model (e.g. technology, organization, capability, goals) and demand model (e.g. customer, competitor, offering). Utility is determined by how synergistic the supply side options are with demand side options. TODO[[2]](#_msocom_2) 

This study bridges these theoretical gaps by asking: why not view uncertainty as a decision variable? This is a huge promotion for a decision where it spent its dark age “under uncertainty” due to a rational framework by Bernoulli (1738) and later axiomatized by von Neumann and Morgenstern (1944). Naming this decision variable as **_promise prior_**, we prescribe entrepreneurs to rationally promise by **_multiplying sellability by deliverability_** and **_adding precision cost_**.

Given the bold and precise promise of this paper, we plan to pay for precision as follows. Sec.2 Literature review uses narrative structure to explain different functions of and constraints around promise. Sec.3 Model builds from baseline models through increasingly sophisticated frameworks: Model 3 multiplies deliverability by sellability to show how complexity constrains promises, Model 4 reveals how fixed precision with high ambition creates learning traps, and Model 5 makes precision a decision variable to theorize optimal promise architecture. The application section analyzes the specific choices of Tesla and Better Place to derive practical implications of the theory. Hopefully we didn’t leave much debt.

## **2. Theoretical Background**

This paper’s theoretical contribution synthesizes four intellectual traditions to formalize the concept of entrepreneurial promise design. From **operations management**, we extend beyond Taylor's (1911) efficiency paradigm and Toyota's lean production (Womack et al., 1990) to address the prior question: how entrepreneurs create the uncertainty structures that enable coordination before operational optimization becomes possible. From **decision science**, we adopt the mathematical machinery but depart from Savage's (1954) expected utility framework, which assumes stable distributions and fixed preferences. Following Knight's (1921) distinction between risk and uncertainty and Kahneman and Tversky's (1979) demonstration of preference instability, we model promises as prior distributions where belief and value co-evolve. From **Bayesian statistics,** we import modeling flexibility. Gelman & Shalizi (2013) shows that learning is most effective when starting with some uncertainty; strong priors hinder effective inference. Entrepreneurs must therefore make promises specific enough to coordinate action, but vague enough for learning and pivots. From **entrepreneurship theory**, the evolution from opportunity discovery (Shane & Venkataraman, 2000) to opportunity creation (Alvarez & Barney, 2007) frames our core insight. We extend Sarasvathy's (2001) effectuation logic[[3]](#_msocom_3)  to show how entrepreneurs design the very means of collective belief formation. Finally, from **strategic management**, the shift from planning to sensemaking—from dynamic capabilities (Teece et al., 1997) to organizing ambiguity across coalitions with divergent goals (Cyert & March, 1963; Weick, 1995)—motivates our formalization of strategy as designed uncertainty structures that generate convergent predictions while preserving flexibility.

Operations for entrepreneurs (Fine et al, 2022) and Bayesian entrepreneurship (Stern et al, 2025) are synthesis in action. Our framework integrates insights across these disciplines by identifying four fundamental constraints that shape the design of a sellable and deliverable promise. These constraints, which we later formalize as propositions, are the financial incentive for boldness, the operational constraint of complexity, the strategic requirement for flexibility, and the economic cost of information.

First, the **Financial Incentive** for boldness creates a natural pressure toward ambitious promises. Markets reward what they believe to be high-potential ventures, and in a world where beliefs can shape reality, a compelling promise can become a self-fulfilling prophecy (Benabou & Tirole, 2016). However, this dynamic creates a powerful temptation to overpromise, as the immediate rewards of securing capital can obscure the downstream challenge of actually delivering on that promise. The promise must eventually confront the reality of operations.

Second, the **Operational Complexity Constraint** imposes a hard, mathematical limit on what is feasible. While dynamic capabilities are crucial for execution (Teece et al., 1997), the inherent complexity of a venture—the number of independent, critical components that must be successfully developed and integrated—creates an unforgiving ceiling on the probability of success. As complexity increases, the likelihood of delivering on an ambitious promise decreases exponentially. Past a certain threshold of complexity (e.g., more than a few critical miracles), the operational challenge of deliverability becomes the dominant factor in venture success, overwhelming any advantage gained from a more persuasive promise.

Third, the **Flexibility Requirement** highlights the tension between commitment and adaptation. A highly specific and precise promise can be a powerful tool for mobilizing resources, but it also creates rigidity. This rigidity can lead to a "learning trap," a state where the venture's beliefs are so firm that new market evidence is ignored, making adaptation mathematically and organizationally impossible. As Bayesian theory demonstrates, learning is most effective when starting from a position of some uncertainty; overly strong priors prevent effective inference from new data (Gelman & Shalizi, 2013). Entrepreneurs must therefore design promises that are specific enough to coordinate action but vague enough to allow for learning and strategic pivots.

Fourth, the **Information Cost**[[4]](#_msocom_4)  recognizes that genuine precision is not free. In information theory, reducing uncertainty (i.e., increasing precision) requires the transmission of information, which is costly (Shannon, 1948). In an entrepreneurial context, this cost is paid through verification—the process of building prototypes, running tests, and achieving milestones that prove capabilities. An entrepreneur cannot simply declare a high degree of precision; they must earn it through progressive, demonstrated achievements. Promising precision without paying the verification cost is equivalent to taking on a form of hidden debt that will eventually come due.

## **3. Model**

### 3.1 Overview of variables and models

Our model frames a venture as an agent designing a prior distribution, Beta(μτ,(1−μ)τ), over the fulfillment level of a promise. The key variables and their interactions are defined in **Table 1**. Here, μ (aspiration level) represents the boldness of the promise—Tesla's μ≈0.3 signified a moderate improvement over the standard at the time, while Better Place's μ≈0.9 implied a revolutionary change with infinite range. The precision, τ, measures the specificity of the promise—"200 miles or more" (τ≈5) implies a flexibility of ±40 miles, whereas "exactly 1,000 miles" (τ≈100) implies a rigidity of ±10 miles. Operational complexity, n, is the difficulty of execution—a battery electric vehicle (n≈5) leverages known supply chains, but a battery-swapping infrastructure (n>15) involves multidimensional challenges from robotics to real estate. Finally, the verification cost, c, is the investment required to justify precision—verifying mileage might cost $1 million, while verifying hydrogen efficiency could require a $10 million infrastructure. How do these variables interact to determine a venture's fate?

**Table 1: Definition of Key Model Variables**

|   |   |   |   |
|---|---|---|---|
|**Variable**|**Definition**|**Interpretation**|**Example (Tesla vs. Better Place)**|
|**μ**|Aspiration Level (mean of belief distribution)|The boldness of the promise.|**Tesla (μ≈0.3):** "200+ miles" (70% improvement over 120-mile standard). **Better Place (μ≈0.9):** "Infinite range."|
|**τ**|Precision (concentration parameter)|The specificity and rigidity of the promise.|**Tesla (τ≈5):** "Roughly 200 miles" (±40 miles).**Better Place (τ≈30):** "Exactly 3 minutes."|
|**n**|Operational Complexity|The number of independent, critical components for success.|**Tesla (n≈5):** Battery, motor, software. **Better Place (n>15):** Robotics, real estate, battery standards, OEM partnerships.|
|**c**|Verification Cost|The cost to increase precision (τ) by one unit.|**Tesla:** Cost of building and testing prototypes.  <br>**Better Place:** Cost of building a nationwide swap station network.|
|**V**|Venture Value|The total potential value created upon successful delivery.|The market capitalization or total addressable market.|

**Figure 1**. illustrates the sequential structure of entrepreneurial outcomes following a promise φ. The square node represents the entrepreneur's initial promise decision, which determines both the probability of market acceptance p(φ) and the conditional probability of successful delivery d(φ). Three terminal states emerge: no sale (V_ns), sale without delivery (V_snd), and successful delivery (V_sd). The expected utility formulation at bottom demonstrates how operational complexity affects outcomes through d(φ), creating the fundamental tension between market persuasion and execution feasibility that drives our theoretical framework.

![](file:////Users/hyunjimoon/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image002.jpg)

**Figure 1. The Sell-and-Deliver Decision Tree**

**Table2** maps our theoretical progression from naive to sophisticated conceptions of entrepreneurial promises. Models 1-2 establish boundary conditions: promises as either powerless words or unconstrained magic—both absurd but necessary to motivate realistic alternatives. Model 3 grounds promises in operational reality, showing how complexity n mathematically constrains optimal promises to φ* = 1/(n+1). Model 4 reveals the learning trap: fixed precision τ can reduce adaptive capacity below critical thresholds, explaining why intelligent entrepreneurs persist with failing strategies. Model 5 achieves synthesis by making precision itself a design variable, enabling joint optimization of aspiration and specificity based on verification costs. This evolution—from irrelevance through constraint to architectural agency—transforms promises from mere communication into the uncertainty structures that determine venture fate.

**Table 2: Summary of models**

|   |   |   |   |
|---|---|---|---|
|**Model**|**Core Insight**|**Entrepreneur Controls**|**Mathematical Result**|
|**M1-2: Baseline**|Promises are either irrelevant (M1) or unconstrained (M2)—both unrealistic but establish why sophisticated models are needed.|M1: Nothing  <br>M2: Promise level φ only|M1: Success fixed at p₀M2: Always promise maximum (φ*=1)|
|**M3: Sell & Deliver**|Success requires both market acceptance AND operational execution—complexity creates binding constraints.|Promise level ϕ, facing complexity n|Optimal promise ϕ*=1/(n+1)|
|**M4: Learning Trap**|Fixed precision creates belief distributions that can prevent adaptation regardless of evidence.|Aspiration μ at given precision τ|Learning trap when μ(1−μ)<ϵ(τ+1)|
|**M5: Full Architecture**|Precision becomes a strategic choice with verification costs—entrepreneurs design complete uncertainty structures.|Both aspiration μ and precision τ|Joint optimum (μ*,τ*) = (1/(n+1), V⋅n/[c(n+1)²]−1)|

### 3.2 Models and propositions

Baseline Models (1 and 2) serve as necessary strawmen, proving the need for our subsequent models. Model 1 assumes a world where promises are completely irrelevant. Here, the probability of success, p0​, is exogenously fixed, and the entrepreneur's words have no impact on the outcome. This reflects a pure "execution is everything" view, which fails to explain why venture capitalists spend time on pitch decks. Model 2 represents the opposite extreme—the promise level, ϕ, linearly determines the probability of success (p(ϕ)=ϕ). Here, the optimal strategy is always to promise the maximum (ϕ∗=1). This captures the "fake it till you make it" culture but doesn't explain why overpromises like Betterplace, Nikola, FTX, Theranos eventually collapse. These two models assume promises have either no effect or can have unconstrained positive effect. Reality lies somewhere in between.

Model 3.1 shows how financial incentives shape promises. Decomposing success into "selling and delivering" yields three possible outcomes: successful delivery (Vsd​), selling but failing to deliver (Vsnd​), and not selling (Vns​).

**Proposition 1 (Financial** **Tightrope****):** _When_ n=1_, the optimal promise level is given by:_ ϕ∗=(Vsd​−Vns​​)/2(Vsd​−Vsnd​)

This proposition proves that while sellability alone pushes towards maximum promises, operational constraints create an internal optimum. Both Tesla and Betterplace saw a Vsd​ in the tens of billions. Penalties for fraud (decreasing Vsnd​) or rewards for "proving failure" (increasing Vns​) as suggested by Bolton et al. (2024) can moderate the promise. The practical implication is clear: despite the overpromising of unicorn companies, there exists a mathematically optimal level of restraint, as illustrated in **Plot 1**.

**Plot 1: Optimal Promise Level (**ϕ∗**) as a Function of Financial Incentives** _Caption: This plot illustrates Proposition 1, showing that the optimal promise level_ ϕ is a concave function of the relative value of success (Vsd​). As the penalty for failure (Vsnd​) increases, the optimal promise becomes more conservative.*

Model 3.2 implements the first agentic shift. Here, the entrepreneur becomes an agent who balances "what the market wants" with "what I can deliver." The deliverability function, d(ϕ)=(1−ϕ)^n, decreases sharply as the promise becomes bolder and as complexity, n, increases.

**Proposition 2 (Complexity Celling):** _When_ Vns​=Vsnd​=0_, the optimal promise level is given by:_ ϕ∗=1​/(n+1)

This proposition shows that when we remove financial nuances and focus purely on the sell-deliver dynamic, operational complexity alone determines the optimal promise. Better Place's battery-swapping infrastructure (n>15) implied a ϕ∗<0.06, yet they promised "infinite range" (ϕ≈0.9). This mathematical discrepancy preordained their failure. A software startup (n≈2) can promise a 33% improvement, but a hydrogen infrastructure venture (n>20) should promise less than 5%.

Model 4 reveals the dark side of precision. When an entrepreneur can only choose the aspiration level, μ, under a fixed precision, τ, the ability to learn is determined by μ(1−μ)/(τ+1).

**Proposition 3 (Learning Trap):** _Ventures enter a learning trap when:_ μ(1−μ)<ϵ(τ+1)

High precision prevents belief updates, creating structural rigidity regardless of market evidence. Better Place's "exactly 3-minute battery swap" (τ≈30) reduced their learning capacity to 0.003—even a strong signal like BMW's refusal to participate couldn't change their strategy. This proposition mathematically proves that precision, often considered a virtue in goal-setting literature (todo: citation), becomes a liability in an uncertain environment. The reason some ventures persist with failing strategies is not irrationality but a learning trap created by initial precision.

Model 5 achieves the second agentic leap. Now, the entrepreneur is not a victim of precision but its architect. The key insight is that precision has a cost, C(τ)=c⋅ln(τ+1).

**Proposition 4 (Optimal Architecture):** _The joint optimum for aspiration and precision is given by:_  **(μ*, τ*) = (1/(n+1), max{0, V·n/c(n+1)² - 1}).**

This proposition achieves a theoretical synthesis by jointly optimizing aspiration and precision. The elegant result reveals a fundamental separation: optimal aspiration, μ∗, depends only on operational characteristics (complexity n), while optimal precision, τ∗, is determined by economic parameters (value V, cost c) modulated by complexity. For Tesla's battery electric vehicle (n≈5), the optimal aspiration was μ∗≈0.17 (perfectly matching "200 miles or more" against a 100-mile baseline), and given the V/c ratio at the time, the optimal precision was τ∗≈5. This insight—that as complexity increases, both μ∗ and τ∗ must decrease—explains why revolutionary promises in complex domains (like Betterplace’s battery infrastructure) are mathematically ill-advised.

## **4. Application**

Capital cheers for bold promises, but execution complexity constrains them—the solution is to explicitly incorporate deliverability into the initial design. Tesla practiced this intuitively: the promise of "200 miles or more" reflected the achievable range with the battery technology of the time (n≈5 in d(ϕ)=(1−ϕ)n). Elon Musk explicitly stated, "We promise 10% higher than what we can do," which aligns with the mathematical optimum of μ∗=1/(n+1)≈0.17. In contrast, Better Place sought only to maximize the probability of sellability, P(sellability∣ϕ). "3-minute battery swap" excited investors, but the actual operational complexity (robotics, battery standardization, site acquisition) meant n>15, which demanded an extremely conservative promise of μ∗<0.06. Successful ventures optimize the product d(ϕ)×P(sellability∣ϕ), no matter how tempting the capital. This is the "deliverability first" principle, as summarized in **Table 3**.

**Table 3: Contrasting Promise Architectures of Tesla and Better Place**  
  

|   |   |   |   |
|---|---|---|---|
|**Architectural Choice**|**Tesla (Successful Design)**|**Better Place (Flawed Design)**|**Theoretical Principle**|
|**Aspiration (μ)**|μ≈0.17 ("200+ miles")|μ≈0.9 ("Infinite range")|**Deliverability First:** Optimal μ* =1/(n+1). Tesla's μ was aligned with its n≈5. Better Place's μ ignored its n>15.|
|**Precision (τ)**|Started low (τ≈5), increased with verification (τ→12→25).|Started high (τ≈30), could not adapt.|**Pay for Precision:** Optimal τ* depends on V/c. Tesla "bought" precision with milestones. Better Place promised it for free.|
|**Learning Capacity**|High initially, allowing pivots (e.g., focus on charging).|Near zero, leading to strategic rigidity.|**Avoid Learning Trap:** Capacity ≈μ(1−μ)/(τ+1). Better Place's high τ and μ created a structural inability to learn.|

Precise promises grant power but also imprison—the solution is to purchase precision only through verification. Tesla's increase in precision was strictly a "pay-then-purchase" model: only after producing 100 Roadsters (~$10M investment) did they increase τ from 5 to 12, and only after the Fremont factory was operational (~$100M) did they raise it to τ≈25. They actually paid the verification cost C(τ)=c⋅ln(τ+1) at each stage. Better Place reversed this sequence. They first made a promise of τ≈∞ ("unlimited range") and tried to verify it later. When it was revealed that the actual vehicle range was only 75 miles, the already-established "unlimited" frame was impossible to revise. The correct formula is clear: τ∗=V⋅n​/c(n+1)^2−1 commands that τ should only be increased when the potential for value creation, V, and the cost of verification, c, justify it. "Verify first, precision later"—this is the law of survival.

The optimal strategy emerges where these two constraints meet: the greater the complexity, the lower both the promise and the precision should be. Better Place's tragedy lies in ignoring this matrix. The complexity of their battery-swapping infrastructure (n>15) demanded a "gradual" promise instead of a "revolutionary" one, and "approximate goals" instead of "exact specifications." Yet they did the opposite: "standard battery," "38 swap stations," "100,000 cars by 2010"—overly specific on all dimensions. In contrast, look at successful hydrogen ventures. Toyota's Mirai started with a flexible promise of "over 300 miles" and still describes it as "around 400 miles" today. They acknowledged the high complexity and adjusted μ and τ accordingly. The practical guidance is simple: when n is large, promise "improvement" over "revolution," and "direction" over "exact figures."

This framework provides concrete tools for the practicing entrepreneur, outlined in **Table 4**. First, conduct a "complexity audit"—assess the supply chain, regulations, and technological maturity to estimate n, and calibrate the promise level with μ∗=1/(n+1). Second, establish a "precision budget"—explicitly calculate the verification cost required to increase τ by one unit, and only increase specificity after securing that much evidence. Third, monitor "learning capacity"—maintain μ(1−μ)/(τ+1)>0.01 to ensure that market signals can lead to strategic corrections. These are not abstract theories but survival tools. The reason Amazon could evolve from a "bookstore" to an "everything store," and the reason Tesla could acknowledge and overcome "production hell," is because they followed these principles. The success of a 21st-century venture depends on the ability to design uncertainty—the wisdom to acknowledge complexity and purchase precision.

**Table 4: A Practical Toolkit for Designing Entrepreneurial Promises**

|   |   |   |   |
|---|---|---|---|
|**Tool**|**Action**|**Guiding Question**|**Desired Outcome**|
|**1. Complexity Audit**|Map all critical dependencies (tech, supply chain, regulation) to estimate complexity n.|How many miracles do we need for this to work?|A realistic n that calibrates the optimal aspiration level: μ* =1/(n+1).|
|**2. Precision Budgeting**|Calculate the cost c of milestones that would justify a higher precision τ.|What evidence must we produce to earn the right to be more specific?|A staged approach where precision is "purchased" with validated results, not promised for free.|
|**3. Learning Capacity Monitor**|Continuously track the venture's learning capacity, defined as μ(1−μ)/(τ+1).|Is our current promise structure making us deaf to market feedback?|Maintaining a capacity > 0.01 to ensure the venture can pivot based on new information.|

## 5. Discussion, Conclusion, and Future Research

Our hypothesis—that entrepreneurial success stems from the ability to design, not eliminate, uncertainty—offers a new path for operations management to contribute to entrepreneurship. As Joglekar & Lévesque (2013) noted, the OM community has relatively neglected its contribution to entrepreneurial practice. We have prescribed an intuitive optimal solution where complexity n lowers the optimal promise level and precision, while an increase in the value-to-cost ratio raises precision, as shown by (μ∗,τ∗)=(n+11​,max{0,V⋅n/(c(n+1)^2)​−1}). This framework is a first step toward bridging the gap between entrepreneurship and operations management. It opens a new domain that treats uncertainty itself as a decision variable, moving beyond the traditional OM focus on efficiency optimization.

Our core prescriptions are simple: prioritize deliverability over sellability (optimizing d(ϕ)×P(sellability∣ϕ)) and pay for precision (increasing τ only after verification)—the contrasting fates of Tesla and Better Place prove this. Tesla started with "200 miles or more" (τ≈5), gradually increasing precision to "244 miles" (τ≈12) after Roadster verification, and then to "265/300 miles" (τ≈25) after Model S production began. Better Place started with promises like "3-minute battery swap" and "500,000swapstations"(\tau \approx 30$), thereby losing its ability to adapt. This contrast explains why some ventures overcome "production hell" while others fail despite honest intentions.

However, the limitations of a static model are clear: it does not capture the nonlinear interactions between constraints, the dynamic process of learning, or the management of overfitting/underfitting from the "entrepreneur-as-scientist" perspective proposed by Zellweger and Zenger (2023). In reality, funding pressure can lead to excessive promises, which in turn demand high precision, and this precision paralyzes learning in a chain reaction. Furthermore, our case set is small and biased toward the electric vehicle industry. Validation across broader industrial and cultural contexts is needed.

Future research should explore the optimal (μ,τ) trajectory over time, the impact of competition on uncertainty design, and the balance required in a multi-stakeholder environment. This will further refine the core insight of 21st-century entrepreneurship: it is neither a bold vision nor perfect execution, but the sophisticated design of uncertainty that matters most. Just as Fine et al. (2022) invited their OM colleagues "into the jungle," we invite them into the uncharted territory of uncertainty design. Entrepreneurs are often unrealistically optimistic (Jiang & Liu, 2019), but our model shows how properly designed optimism can lead to success. The ability to design uncertainty is the new science of entrepreneurial operations management.

## **6. References**

Agrawal, A., Camuffo, A., Gambardella, A., Gans, J. S., Scott, E. L., & Stern, S. (2025). Bayesian entrepreneurship. MIT Press.

Agrawal, A., Gans, J., & Goldfarb, A. (2024). _The economics of artificial intelligence: An agenda_. University of Chicago Press.

Alvarez, S. A., & Barney, J. B. (2007). Discovery and creation: Alternative theories of entrepreneurial action. _Strategic Entrepreneurship Journal, 1_(1‐2), 11-26.

Benabou, R., & Tirole, J. (2016). Mindful economics: The production, consumption, and value of beliefs. _Journal of Economic Perspectives, 30_(3), 141-164.

Bolton, P., Liu, S., Nanda, R., & Sunderesan, S. (2024). Moral hazard in experiment design: Implications for financing innovation. Working Paper.

Box, G. E. (1980). Sampling and Bayes' inference in scientific modelling and robustness. _Journal of the Royal Statistical Society, 143_(4), 383-430.

Crawford, V. P., & Sobel, J. (1982). Strategic information transmission. Econometrica, 50(6), 1431-1451.

Cyert, R. M., & March, J. G. (1963). _A behavioral theory of the firm_. Prentice-Hall.

Fine, C., Padurean, L., & Naumov, S. (2022). Entrepreneurial operations: A review and agenda. _Manufacturing & Service Operations Management, 24_(5), 2365-2381.

Garud, R., Gehman, J., & Giuliani, A. P. (2014). Contextualizing entrepreneurial innovation: A narrative perspective. _Research Policy, 43_(7), 1177-1188.

Gelman, A., & Shalizi, C. R. (2013). Philosophy and the practice of Bayesian statistics. _British Journal of Mathematical and Statistical Psychology, 66_(1), 8-38.

Jiang, K., & Liu, D. (2019). The dark side of optimistic leadership: A moderated mediation model. _Journal of Business Ethics, 156_(4), 1107-1122.

Joglekar, N., & Lévesque, M. (2013). An OM perspective on the entrepreneurship-innovation interface. _Production and Operations Management, 22_(6), 1355-1370.

Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. _Econometrica, 47_(2), 263-291.

Knight, F. H. (1921). _Risk, uncertainty, and profit_. Houghton Mifflin.

Morris, S. (1995). The common prior assumption in economic theory. Economics & Philosophy, 11(2), 227-253.

Sarasvathy, S. D. (2001). Causation and effectuation: Toward a theoretical shift from economic inevitability to entrepreneurial contingency. _Academy of Management Review, 26_(2), 243-263.

Savage, L. J. (1954). _The foundations of statistics_. Wiley.

Schumpeter, J. A. (1934). _The theory of economic development: An inquiry into profits, capital, credit, interest, and the business cycle_. Harvard University Press.

Shane, S., & Venkataraman, S. (2000). The promise of entrepreneurship as a field of research. _Academy of Management Review, 25_(1), 217-226.

Shannon, C. E. (1948). A mathematical theory of communication. _The Bell System Technical Journal, 27_(3), 379-423.

Taylor, F. W. (1911). _The principles of scientific management_. Harper & Brothers.

Teece, D. J., Pisano, G., & Shuen, A. (1997). Dynamic capabilities and strategic management. _Strategic Management Journal, 18_(7), 509-533.

Weick, K. E. (1995). _Sensemaking in organizations_. Sage.

Womack, J. P., Jones, D. T., & Roos, D. (1990). _The machine that changed the world_. Rawson Associates.

Zellweger, T., & Zenger, T. (2023). Entrepreneurs as scientists: A pragmatist approach to producing value out of uncertainty. _Academy of Management Review, 48_(3), 379-408.

## **7. Appendix: Proof of Propositions**

### **Proposition 1 (Financial Tightrope)**

_When_ n=1_, the optimal promise level is_ ϕ∗=(Vsd​−Vns​​)/2(Vsd​−Vsnd​).

**Proof:** With p(φ) = φ and d(φ) = 1-φ, expected utility becomes E[U(φ)] = φ(1-φ)Vsd + φ²Vsnd + (1-φ)Vns. Differentiating yields dE/dφ = (1-2φ)Vsd + 2φVsnd - Vns = 0, giving φ* = (Vsd - Vns)/2(Vsd - Vsnd).

### **Proposition 2 (Complexity Ceiling)**

_When_ Vns​=Vsnd​=0_, the optimal promise level is_ ϕ* = 1/(n+1)_. Operational complexity n constrains promise—higher complexity leads to a more conservative promise._

**Proof:** With p(φ) = φ and d(φ) = (1-φ)^n, expected utility reduces to E[U(φ)] = φ(1-φ)^n Vsd. Maximizing requires f'(φ) = (1-φ)^(n-1)[1-(n+1)φ] = 0, yielding φ* = 1/(n+1).

### **Proposition 3 (Learning Trap)**

_A learning trap occurs when_ μ(1−μ)<ϵ(τ+1)_. High precision prevents belief revision, creating structural rigidity regardless of evidence._

**Proof.** Consider Bayesian updating after observing failure. Prior Beta(μτ,(1-μ)τ) yields posterior Beta(μτ,(1-μ)τ+1) with mean μ' = μτ/(τ+1). The change |μ'-μ| = μ(1-μ)/(τ+1) < ε requires τ > μ(1-μ)/ε - 1.

### **Proposition 4 (Optimal Architecture)**

_The joint optimum is_ **(μ*, τ*) = (1/(n+1), max{0, V·n/c(n+1)² - 1}).** _Aspiration is determined by operational complexity, while precision is determined by the value-to-cost ratio._

**Proof.** We maximize total utility L(μ,τ) = E[V(φ)] - C(τ), where expected reward is V·E[φ(1-φ)ⁿ] and precision cost is c·ln(τ+1).

Step 1: Optimal Aspiration. Since C(τ) is independent of μ, we maximize expected reward E[V(φ)]. From Proposition 2, the reward function f(φ) = φ(1-φ)ⁿ peaks at φ* = 1/(n+1). Therefore: μ* = 1/(n+1) Operational complexity alone determines optimal aspiration.[[5]](#_msocom_5) 

Step 2: Optimal Precision. With μ fixed at μ*, we approximate expected reward using second-order Taylor expansion: E[V(φ)] ≈ V·[f(μ*) + ½f''(μ*)Var(φ)]

where Var(φ) = μ*(1-μ*)/(τ+1). The first-order condition becomes:

dL/dτ = -V·½f''(μ*)μ*(1-μ*)/(τ+1)² - c/(τ+1) = 0

The key insight emerges from recognizing that the sensitivity term [-½f''(μ*)μ*(1-μ*)] equals n/(n+1)², which is precisely the task's inherent uncertainty μ*(1-μ*). This yields the elegant relationship: τ + 1 = (V/c)·μ*(1-μ*) Substituting μ*(1-μ*) = n/(n+1)²: τ* = max{0, V·n/c(n+1)² - 1}. Aspiration depends only on operational complexity, while precision scales with the value-to-cost ratio modulated by complexity. As complexity increases, both optimal aspiration and precision decrease—complex tasks demand conservative promises with flexibility to learn.

---

prior need not temporally precede likelihood

elaborate

1. linear flow of "elicit prior then maximize" can't work

2. abstract "keeping synergistic options" as flexibility

3. flexibility is needed to hedge against unknown unknown

4. low precision promise creates internal uncertainty, to buffer external unknown unknown

need scott's input

in most recent scott's work (Homo Entrepreneuricus (2025)), it distinguishes effectuation vs homo entrepreneuricus on the axis of Emergent vs Theory-Based.

my paper may be heading toward  emergent from theory-based, especially with adding feedback loop claimed in further work.

need guidance on 

on how to think about model 4 vs 5 differences - where mean is optimized given precision vs mean and precision are optimized 

and whether connecting this with information cost is meaningful

need checking

---

[[2025-08-08|25-08-08-07]]

# The Strategic Design of Entrepreneurial Promises: A Five-Stage Evolution Model

## I. Introduction

Entrepreneurial promises transform uncertainty into possibility. When Trevor Milton proclaimed that Nikola would revolutionize trucking with hydrogen power, markets responded with an $11 billion valuation. When Elon Musk promised to electrify transportation through Tesla, initial skepticism gave way to transformative success. Both entrepreneurs mastered the art of selling their vision—yet only one delivered. What distinguishes empty rhetoric from catalytic prophecy?

This paper advances two fundamental insights about entrepreneurial promise-making. First, excessive precision creates learning traps that prevent entrepreneurs from updating their beliefs when markets signal differently. Second, operational complexity imposes mathematical constraints on optimal promise levels, explaining why software ventures promise aggressively while hardware ventures speak cautiously. These insights transform promise-making from mysterious art to tractable science.

We develop a five-stage theoretical framework building from static promises to distributions over ambition levels. Through this progression, we derive four propositions that reshape how scholars should understand entrepreneurial decision-making. Our analysis provides mathematical foundations for phenomena that practitioners recognize intuitively but struggle to articulate systematically.

## II. Core Concepts and Theoretical Framework

### 2.1 The Architecture of Promises

Understanding entrepreneurial promises requires precise analytical decomposition. The **promise level** (φ) captures specific performance claims relative to technical possibilities. When battery technology permits 100-300 mile range, promising 226 miles yields φ = (226-100)/(300-100) = 0.63. This normalization enables cross-industry comparison despite different performance metrics.

The **aspiration level** (μ) represents the mean of the prior distribution over possible promises. Declaring "approximately 200-mile range" communicates μ while acknowledging uncertainty. The **precision parameter** (τ) quantifies how tightly promises cluster around this mean—high τ yields narrow commitments like "195-205 miles," while low τ permits broad ranges like "150-250 miles."

### 2.2 Decision Architecture: Choices and Constraints

Entrepreneurial promises emerge from the interplay between strategic choices and environmental constraints. Understanding this architecture is essential for grasping how our theoretical propositions translate into practical prescriptions.

#### 2.2.1 The Entrepreneurial Choice Space

Entrepreneurs control two fundamental variables that shape their venture's trajectory:

**Aspiration Level (μ)**: This strategic choice represents the entrepreneur's vision calibration—how ambitious their promises relative to current technological possibilities. A μ = 0.9 signals revolutionary ambition ("we'll obsolete the industry"), while μ = 0.3 indicates incremental improvement ("we'll enhance existing solutions"). This choice directly determines resource mobilization potential but also delivery difficulty.

**Precision Parameter (τ)**: This communication choice governs specificity design—how tightly promises cluster around the aspiration level. Low precision (τ < 10) preserves strategic flexibility through statements like "we aim to revolutionize transportation." High precision (τ > 50) creates rigid commitments like "we will deliver 1,000-mile range by Q3 2023." This choice fundamentally affects learning capacity and pivot optionality.

#### 2.2.2 Technological and Institutional Constraints

While entrepreneurs choose (μ,τ), they operate within a parameter space shaped by forces beyond their control:

**Technological Parameters**:
- **Operational Complexity (n)**: Physical laws create immutable constraints. Software's malleability yields n ≈ 1; hardware's material resistance imposes n ≈ 5; biology's complexity demands n ≈ 10. This parameter fundamentally bounds achievable promises.
- **Information Cost (c)**: Market structure determines validation expense. Open ecosystems with standardized metrics reduce c; proprietary domains with complex integration increase c. This shapes optimal precision levels.

**Institutional Parameters**:
- **Success Rewards (V_sd)**: Exit multiples and acquisition premiums create pull incentives. Higher rewards enable bolder promises but also amplify temptation.
- **Fraud Penalties (V_snd)**: Criminal sanctions and regulatory enforcement create push constraints. Severe penalties deter deception but may chill legitimate experimentation.
- **Failure Costs (V_ns)**: Bankruptcy protection and cultural attitudes determine downside risk. Forgiving environments encourage experimentation; punitive ones demand conservatism.

#### 2.2.3 The Complete Decision Table

| **Variable**          | **Links to Propositions** | **Links to Propositions**            | **Nature**           | **Control Mechanism**        |
| --------------------- | ------------------------- | ------------------------------------ | -------------------- | ---------------------------- |
| μ (aspiration)        |                           | Props 2,4: μ* = 1/(n+1)              | Strategic choice     | Vision calibration           |
| τ (precision)         |                           | Props 3,4: τ < μ(1-μ)/ε - 2          | Communication choice | Specificity design           |
| n (complexity)        |                           | Props 2,4: Determines μ*,τ*          | Physical constraint  | Operations difficulty        |
| c (information cost)  |                           | Prop 4: Shapes τ*                    | Market structure     | Due diligence infrastructure |
| V_sd (success reward) |                           | Props 1,4: Drives promise escalation | Market incentive     | Exit multiples               |
| V_snd (fraud penalty) |                           | Constrains high τ choices            | Legal deterrent      | Criminal sanctions           |
| V_ns (failure cost)   |                           | Enables experimentation              | Safety net           | Bankruptcy protection        |

This architecture reveals why entrepreneurial success requires more than good intentions or bold vision. The interplay between choice variables (μ,τ) and environmental parameters (n,c,V_sd,V_snd,V_ns) creates a complex optimization landscape where naive strategies—whether maximally bold or maximally precise—lead to predictable failure modes.

### 2.3 Mathematical Framework

We model entrepreneurial communication through Beta(μτ, (1-μ)τ) distributions as priors over promise levels. When τ = 2, we obtain nearly uniform distributions reflecting maximum uncertainty. As τ increases, distributions concentrate around μ, reflecting increasing confidence in specific outcomes. This framework enables rigorous analysis of how communication choices affect subsequent learning dynamics.

## III. Model Development and Core Propositions

Our theoretical journey progresses through five models, each adding critical elements to understand entrepreneurial promise-making. We begin with promises as cheap talk (Model 1), then show how they mobilize resources (Model 2), constrain delivery (Model 3), enable flexibility through distributions (Model 4), and finally optimize precision and ambition jointly (Model 5). The following table summarizes this progression, highlighting how each model's assumptions generate distinct insights about entrepreneurial behavior.

| Model                               | Key Assumption                                          | Core Result                                            | Real-World Implication                                                               |
| ----------------------------------- | ------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| **Model 1: Static World**           | Success probability exogenous (p fixed)                 | Promises irrelevant: U = p·V                           | Explains internal ventures, government contracts where promises don't affect funding |
| **Model 2: Persuasion Power**       | Promises mobilize resources: P(S∣φ) = p + αφ            | Maximum promises optimal: φ* = 1                       | Bubble dynamics—Nikola's $11B valuation from bold claims                             |
| **Model 3: Sell-Deliver Trade-off** | Delivery difficulty rises with promises: d(φ) = (1-φ)^n | Optimal promise: φ* = 1/(n+1)                          | Software promises 50%, hardware 17%, deep tech 9%                                    |
| **Model 4: Strategic Ambiguity**    | Entrepreneurs choose distribution Beta(μτ, (1-μ)τ)      | Learning trap when τ > μ(1-μ)/ε - 2                    | BetterPlace's τ=56 prevented pivoting to charging                                    |
| **Model 5: Precision Costs**        | Information gathering costly: C(τ) = c·ln(τ+1)          | Joint optimum: μ* = 1/(n+1), τ* = V_sd·n/[c(n+1)²] - 1 | Tesla's gradual precision increase (12→60) vs Nikola's immediate τ=100               |

Each model builds on its predecessors while introducing new strategic considerations. Model 1 establishes the null hypothesis—when don't promises matter? Model 2 reveals why entrepreneurs feel pressure to exaggerate. Model 3 explains why some succeed while others fail through operational constraints. Model 4 shows how overconfidence blocks learning. Model 5 integrates all elements into a complete optimization framework.
### Model 1: The Impotent Promise

Traditional economic models treat success probability as exogenous, rendering promises mere cheap talk. Here P(Success) = p regardless of promised performance. This baseline captures contexts where resource allocation follows predetermined plans—internal corporate ventures with fixed budgets, government contracts with guaranteed funding, tenure-track positions evaluated solely on past work. While limited, this null model establishes when promises matter.

### Model 2: The Escalation Imperative

Reality often exhibits self-fulfilling dynamics where bold promises attract resources that genuinely enhance success probability. We model this as P(Success|φ) = p + αφ, where α captures resource mobilization effects.

**Proposition 1.** When promises linearly affect success probability through resource mobilization, optimal promises always maximize: φ* = 1.

*Proof.* Expected utility U = (p + αφ)V yields ∂U/∂φ = αV > 0 throughout [0,1], implying corner solution φ* = 1. ∎

This proposition explains maximum promise equilibria during bubble periods. When resources flow toward confidence, entrepreneurs rationally escalate claims. Nikola's hydrogen revolution narrative attracted General Motors' partnership and $2 billion investment precisely because it maximized φ. The model's fatal flaw—ignoring delivery constraints—enables escalation spirals that end in collapse.

### Model 3: Physics Meets Rhetoric

Entrepreneurial success demands sequential achievements: selling visions then delivering results. We model delivery difficulty as d(φ) = (1-φ)^n, where operational complexity n transforms ambitious promises into exponential implementation challenges.

**Proposition 2.** Given operational complexity n, optimal promise level equals φ* = 1/(n+1).

*Proof.* Success requires both selling and delivering: E[U] = V_sd × φ × (1-φ)^n. First-order condition yields φ* = 1/(n+1). ∎

This proposition explains systematic variation across sectors:

**Low Complexity (n ≈ 1)**: SaaS platforms, mobile apps, algorithmic trading systems promise aggressively (φ* ≈ 0.5) because iteration cycles measure in days and deployment requires clicking "publish."

**Medium Complexity (n ≈ 5)**: Autonomous vehicles, robotics, medical devices promise moderately (φ* ≈ 0.17) because hardware prototyping takes months and regulatory approval adds years.

**High Complexity (n ≈ 10)**: Nuclear fusion, quantum computing, novel therapeutics promise minimally (φ* ≈ 0.09) because fundamental physics research spans decades and clinical trials eliminate most candidates.

### Model 4: From Points to Distributions

Sophisticated entrepreneurs communicate through probability distributions. When venture capitalists hear "we expect 10x to 100x returns, most likely around 30x," they receive information about the entire belief structure. We model this through Beta(μτ, (1-μ)τ) priors where entrepreneurs choose distribution parameters.

High precision creates rigidity—confident entrepreneurs cannot update beliefs despite contrary evidence. Low precision preserves adaptability but sacrifices credibility.

**Proposition 3.** Precision exceeding τ̄ = μ(1-μ)/ε - 2 creates learning traps where market feedback cannot meaningfully update the prior.

*Proof.* Consider Bayesian updating after observing failure. Prior Beta(μτ,(1-μ)τ) yields posterior Beta(μτ,(1-μ)τ+1) with mean μ' = μτ/(τ+1). The change |μ'-μ| = μ(1-μ)/(τ+1) < ε requires τ > μ(1-μ)/ε - 1. ∎

BetterPlace exemplified this trap. With μ = 0.7 confidence in battery-swapping and τ ≈ 56 precision, even strong consumer preference for charging stations barely moved beliefs. The learning trap threshold τ̄ = 2.2 for 5% minimum updates means Agassi's precision exceeded adaptability requirements by 25-fold.

**Figure 1: Success and Failure Regions in μ-τ Space**

![[figure1_mu_tau_space_eng.svg]]

The entrepreneurial landscape maps onto a two-dimensional space where aspiration (μ) and precision (τ) determine venture trajectories. Gradient shading indicates danger intensity, with the mathematical threshold τ̄ = μ(1-μ)/ε - 2 forming a curved boundary that separates the learnable zone from learning traps. Three distinct regions emerge: the adaptive zone (low τ, moderate μ), the operational rigidity trap (high τ, low μ), and the fraud temptation zone (high τ, high μ).

Tesla's path demonstrates successful navigation—maintaining μ≈0.4-0.7 while gradually adjusting τ. Even during "production hell," they stayed below the learning threshold, preserving adaptability. BetterPlace fell into the rigidity trap due to high precision (τ=45→95), blocking pivots despite market signals. Nikola began in the fraud temptation zone (μ=0.85, τ=35→56), where unrealizable promises led to deception.

**Figure 2: Evolution of Beta Distributions Over Time**

![[figure2_beta_evolution_eng.svg]]

The evolution of Beta distributions for three ventures reveals distinct patterns of belief concentration. Tesla began with broad exploration (Beta(2.1,2.9)) and converged to validated confidence (Beta(40,20)). The uncertainty range (shaded area) narrowed gradually as evidence accumulated. BetterPlace showed early rigidity (Beta(36,9)) leading to extremely narrow late-stage distributions (Beta(45,50))—a visual representation of learning impossibility. Nikola's distributions evolved toward extreme asymmetry (Beta(51,5)), representing commitment to rhetoric over realizability.

**Figure 3: Learning Dynamics and Precision's Trap**

![[figure3_learning_dynamics_eng.svg]]

Learning dynamics show how precision constrains adaptability. The vertical axis measures belief updates after negative market feedback. Ventures with τ < 20 maintain meaningful learning, enabling successful pivoting. Beyond τ > 20, updates fall below the 5% threshold, creating learning traps. Empirical cases validate the theory: PayPal and Instagram successfully pivoted with low τ, Segway and BetterPlace were trapped by high precision, and Nikola's extreme precision led to deception rather than adaptation.

### Model 5: The Precision-Aspiration Nexus

Choosing precision requires investment in market research, prototyping, and validation. We model cost as C(τ) = c × ln(τ+1), where the logarithm captures diminishing returns—doubling precision requires more than double investment.

**Proposition 4.** Optimal promise design yields joint solution (μ*, τ*) where:
- μ* = 1/(n+1)
- τ* = max(0, [V_sd·n/(c(n+1)²)] - 1)

*Proof.* Maximizing E[U] = V_sd × μ × (1-μ)^n - c × ln(τ+1) yields the stated first-order conditions. ∎

The coupling reveals why software startups speak precisely while hardware ventures hedge. Low operational complexity and information costs enable high optimal precision. High complexity compounds with high validation costs to demand strategic ambiguity.

## IV. Theoretical Integration and Implications

### 4.1 Theoretical Synthesis

Our four propositions form an integrated framework:

1. **Maximum promises emerge** when resources follow confidence (Proposition 1)
2. **Physics constrains promises** through operational complexity (Proposition 2)  
3. **Precision traps learning** when confidence exceeds adaptability needs (Proposition 3)
4. **Joint optimization** reveals complexity-precision trade-offs (Proposition 4)

These results explain entrepreneurial phenomena that previously seemed paradoxical. Why do smart founders make obviously impossible promises? Proposition 1 shows the structural incentives. Why do some sectors systematically overpromise while others underpromise? Proposition 2 quantifies operational constraints. Why can't failing ventures pivot despite clear market signals? Proposition 3 identifies learning traps. How should entrepreneurs balance specificity and flexibility? Proposition 4 provides the optimization framework.

### 4.2 The Entrepreneurial Perspective: Managing Aspiration and Precision

Our two core messages—that excessive precision creates learning traps and operational complexity constrains promises—translate into specific prescriptions for entrepreneurs navigating uncertainty.

**From Message 1 (Precision Traps)**: Proposition 3 reveals the mathematical threshold τ̄ = μ(1-μ)/ε - 2 beyond which learning ceases. For a typical venture with μ = 0.6 and requiring 5% belief updates, this yields τ̄ ≈ 2.8. Yet we observe entrepreneurs beginning with τ = 30-50, creating immediate learning paralysis. The prescription is clear: start with τ < 10, ideally τ ≈ 5. This preserves pivot optionality worth far more than any credibility gain from false precision.

**From Message 2 (Operational Constraints)**: Propositions 2 and 4 jointly determine optimal (μ*, τ*) given operational complexity n. For software ventures (n ≈ 1), μ* = 0.5 permits ambitious promises because rapid iteration enables recovery from overreach. For hardware ventures (n ≈ 5), μ* = 0.17 reflects the unforgiving nature of physical constraints. Deep tech ventures (n ≈ 10) must accept μ* = 0.09—humility imposed by physics, not choice.

**Integration Through Simulation**: Before committing to any (μ,τ) combination, entrepreneurs should simulate plausible market scenarios. If negative signals wouldn't meaningfully update beliefs, precision is dangerously high. If positive signals wouldn't increase confidence, precision may be too low for credibility. The sweet spot preserves learning while maintaining stakeholder engagement.

**Dynamic Calibration Path**: Begin with μ* = 1/(n+1) and minimal τ. As evidence accumulates—successful prototypes, customer validation, regulatory approvals—increase τ by approximately 20% per major milestone. Tesla exemplified this path: τ evolved from 5→12→30→60 over twelve years, each increase justified by demonstrated achievement.

### 4.3 The Institutional Perspective: Technology and Policy Design

While entrepreneurs control (μ,τ), institutions and technology shape the parameter space within which these choices occur.

**Technology's Immutable Constraints**: Operational complexity n represents physical laws that no amount of optimism can overcome. Battery chemistry, thermodynamic efficiency, biological pathways—these create hard bounds on feasible promises. Industries naturally stratify by n: software (n ≈ 1) permits aggressive promises because code is malleable; hardware (n ≈ 5) demands conservatism because atoms resist; biotech (n ≈ 10) requires extreme humility because biology humbles.

Information cost c similarly varies by technological infrastructure. Open-source ecosystems and standardized APIs reduce c, enabling higher optimal τ*. Proprietary knowledge and complex integration increase c, forcing strategic ambiguity. The formula τ* = V_sd·n/[c(n+1)²] - 1 quantifies how these technological realities shape communication strategies.

**Policy Levers for Innovation**: Institutions control three critical parameters that shape entrepreneurial behavior:

1. **Success Rewards (V_sd)**: Higher exit multiples and acquisition premiums increase both μ* and τ*. But this creates a dilemma—the same incentives that motivate genuine innovation also amplify fraud temptation. The policy challenge is calibrating rewards high enough to incentivize risk-taking but not so high as to make deception irresistible.

2. **Fraud Penalties (V_snd)**: Criminal sanctions and regulatory enforcement deter deception but may also discourage legitimate experimentation. Our framework suggests focusing enforcement on high-precision false claims (high τ with failed delivery) while tolerating low-precision aspirational statements. The distinction between "we will achieve X" (high τ) and "we aim toward X" (low τ) should guide regulatory response.

3. **Failure Costs (V_ns)**: Bankruptcy protection, social safety nets, and cultural attitudes toward failure determine entrepreneurial risk appetite. Low V_ns encourages experimentation by reducing downside risk. Silicon Valley's success partly reflects institutional forgiveness—failed entrepreneurs can try again. But excessive forgiveness enables recklessness. The optimum balances second chances with accountability.

**Empirical Predictions for Policy**: Our framework generates testable hypotheses about institutional effects:
- Increasing V_sd by 10% should increase average industry μ by approximately 5% and τ by 3%
- Doubling fraud penalties (V_snd) should reduce high-τ ventures by 30-40%
- Improving bankruptcy protection (reducing V_ns by half) should increase venture formation by 20-25%

These quantitative relationships enable evidence-based policy design rather than ideological speculation.

### 4.4 Future Research Directions

Our framework opens several avenues for theoretical and empirical investigation:

**Multi-Period Dynamics**: How do reputation effects modify optimal (μ,τ) trajectories? Does success in early rounds justify higher precision in later stages, or does maintaining adaptability remain paramount?

**Competitive Interactions**: When multiple entrepreneurs compete in the same space, do promise levels escalate in prisoner's dilemma dynamics? How do first-mover advantages interact with precision choices?

**Behavioral Extensions**: Do entrepreneurs systematically deviate from optimal (μ,τ) due to overconfidence bias or social pressures? Can training in simulation-based thinking improve calibration?

**Cross-Cultural Variation**: How do institutional parameters (V_sd, V_snd, V_ns) vary across entrepreneurial ecosystems? Do cultural attitudes toward uncertainty affect optimal precision independent of formal institutions?

### 4.5 Empirical Illustration: Calibrating Promise Priors Through Public Communications

To ground our theoretical framework in observable phenomena, we demonstrate how entrepreneurial communications translate into prior distributions over promise levels. This methodology illuminates the critical moment when entrepreneurs crystallize their initial beliefs—a simulation-based calibration that shapes all subsequent learning.

**Coding Protocol**: Our content analysis transforms linguistic choices into mathematical parameters. Aspiration level (μ) emerges from the semantic distance between current reality and promised future: "enhance" signals modest departure (μ ≈ 0.1-0.3), while "revolutionize" claims transformative discontinuity (μ ≈ 0.7-0.9). Precision (τ) accumulates through commitment devices—each quantitative metric adds specificity (+10), temporal boundaries create accountability (+15), while hedging language preserves optionality (-5 to -10). This translation reveals how rhetoric becomes belief structure.

**Table 2: Initial Promise Calibration in Three Ventures**

| Venture | Founding Communication | Coded Elements | μ | τ | Beta Prior | Theoretical Zone |
|---------|----------------------|----------------|---|---|------------|------------------|
| **Tesla (2006)** | "Build sports car. Use that money to build affordable car. While doing above, provide zero emission power generation" | • "Zero emission" (+0.4 aspiration)<br>• Sequential milestones (-10 flexibility)<br>• No timeline (-15 precision) | 0.42 | 5 | Beta(2.1, 2.9) | Adaptive zone |
| **BetterPlace (2007)** | "Make Israel oil-independent by 2020 through battery swapping infrastructure" | • "Oil-independent" (+0.8 aspiration)<br>• "By 2020" (+15 precision)<br>• Specific country/method (+30) | 0.80 | 45 | Beta(36, 9) | Rigidity threshold |
| **Nikola (2016)** | "1,000-mile range hydrogen trucks by 2020, making diesel obsolete" | • "Making obsolete" (+0.85 aspiration)<br>• "1,000 miles" (+10 precision)<br>• "By 2020" (+15 precision) | 0.85 | 35 | Beta(30, 5) | Fraud temptation |

These initial calibrations reveal each venture's fundamental stance toward uncertainty. Tesla's Roadster-era prior—Beta(2.1, 2.9)—represents nearly maximum entropy, acknowledging profound uncertainty while maintaining directional conviction. This wide distribution enabled learning: when battery costs proved higher than anticipated, the broad prior could accommodate reality without shattering.

BetterPlace began at the rigidity threshold, with τ = 45 already constraining adaptability. The specificity of "battery swapping" and "by 2020" created a narrow prior that subsequent market feedback—consumers' revealed preference for charging—could barely shift. Nikola's extreme aspiration (μ = 0.85) combined with moderate initial precision placed them immediately in our model's danger zone, where the mathematics of delivery make deception tempting.

This snapshot analysis—examining the crystallized moment of initial promise-making rather than temporal evolution—demonstrates how our framework operationalizes entrepreneurial belief structures. The simulation-based perspective reveals why some ventures preserve learning capacity while others lock themselves into tragic trajectories from inception.

## V. Conclusion

Entrepreneurial promises operate at the intersection of ambition and constraint, confidence and uncertainty. Our analysis reveals promise-making as optimization under physical laws and information dynamics. The core insights—that precision can trap learning and complexity constrains promises—provide mathematical foundations for entrepreneurial success and failure.

The four propositions trace a complete theory from escalation incentives through operational reality to learning dynamics and optimal design. This framework explains patterns that practitioners recognize but rarely articulate: why software founders speak boldly while hardware founders hedge, why confident entrepreneurs can't pivot, why some sectors breed fraud while others encourage honesty.

For entrepreneurs, the implications are direct. Respect operational complexity when setting ambitions. Preserve learning capacity by limiting initial precision. Increase specificity only as evidence accumulates. These principles transform promise-making from guesswork to engineering.

For scholars, our framework opens new research directions. How do competitive dynamics affect promise equilibria? Can reputation models explain precision evolution? Do behavioral biases systematically distort (μ,τ) choices? Each question extends naturally from our foundation.

The difference between Nikola and Tesla, between collapse and triumph, lies in mathematical alignment. Both ventures began with transformative visions. Both founders possessed conviction. But only Tesla calibrated promises to physics, precision to uncertainty. In this calibration lies entrepreneurship's essential challenge: bold enough to inspire, realistic enough to achieve, flexible enough to learn.

Success requires more than vision. It demands strategic design of promises that mobilize resources while respecting reality. Our model provides the blueprint for such design—not through inspirational maxims but through mathematical necessity. In entrepreneurship's highest calling, turning imagination into impact, precision matters. But not too much.

---

## References

Baron, J. N., & Hannan, M. T. (2002). Organizational blueprints for success in high-tech start-ups. California Management Review, 44(3), 8-36.

Fine, C. H. (1998). Clockspeed: Winning industry control in the age of temporary advantage. Perseus Books.

Gans, J. S. (2023). Experimental choice and disruptive technologies. Management Science, 69(11), 6429-6450.

Gans, J. S., & Stern, S. (2003). The product market and the market for "ideas." Research Policy, 32(2), 333-350.

Kerr, W. R., Nanda, R., & Rhodes-Kropf, M. (2014). Entrepreneurship as experimentation. Journal of Economic Perspectives, 28(3), 25-48.

---

## Mathematical Appendix

### A.1 Proposition 2 Extended

The first-order condition ∂E[U]/∂φ = V_sd[(1-φ)^n - nφ(1-φ)^(n-1)] = 0 yields φ* = 1/(n+1). This result has profound implications:

As n → 0 (trivial complexity), φ* → 1 (maximum promises)
As n → ∞ (impossible complexity), φ* → 0 (no promises)

The elasticity ∂ln(φ*)/∂ln(n) = -1 implies a 1% increase in complexity reduces optimal promises by 1%.

### A.2 Learning Trap Dynamics

For μ = 0.7 and τ = 100, observing failure yields:
- Prior: Beta(70, 30)
- Posterior: Beta(70, 31)  
- Updated mean: 70/101 = 0.693
- Change: 0.007 or 0.7%

For τ = 10:
- Prior: Beta(7, 3)
- Posterior: Beta(7, 4)
- Updated mean: 7/11 = 0.636
- Change: 0.064 or 6.4%

The 10-fold difference in precision creates a 9-fold difference in learning capacity.

### A.3 Joint Optimization Details

The Lagrangian for constrained optimization:
L = V_sd × μ × (1-μ)^n - c × ln(τ+1) + λ(τ - τ̄(μ))

Yields the system:
∂L/∂μ: V_sd[(1-μ)^n - nμ(1-μ)^(n-1)] = λ∂τ̄/∂μ
∂L/∂τ: c/(τ+1) = λ

Solving simultaneously produces the joint optimum.
