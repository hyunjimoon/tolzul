
A coffee startup evaluating entry into the U.S. market faces a fundamental decision: should it first test market demand for premium coffee (**φ**) or proceed directly with an **implementation strategy** (**θ**)? Idea validation (**c_φ**) involves running blind taste tests or consumer surveys to determine whether customers recognize and prefer high-quality coffee. Alternatively, the company can commit to an **implementation strategy**, either selling brewed coffee (Starbucks model) or packaged beans (Peet’s model), incurring an **implemented idea test cost (c_φθ)**. The **realized profitability (y)** is binary, where **y = 1** indicates financial success only if both **φ** (market demand) and **θ** (implementation) are strong. This hierarchical **Beta-Bernoulli model** captures the entrepreneur’s choice between testing and immediate implementation, where learning updates prior beliefs about demand (**a_φ, b_φ**) and implementation effectiveness (**a_θ, b_θ**).

Unlike coffee, where modeling assumption of discrete market validation (good vs. bad) is acceptable, electric vehicle (EV) adoption depends on continuous trade-offs in market demand (**φ**) and implementation effectiveness (**θ**). A car manufacturer like Tesla or Toyota must decide whether to validate demand for EVs before committing to large-scale production. Idea validation (**c_φ**) may involve prototype testing or consumer surveys to estimate willingness to pay, while an **implemented idea test** (**c_φθ**) includes pilot production or limited regional releases. The **realized profitability (y)** is a continuous measure, reflecting financial success based on **φ** (consumer demand) and **θ** (production scalability).

Because profitability outcomes are no longer binary but instead vary across a range of values, a **computational approach becomes essential** for modeling realistic decision-making. A **Normal-Beta model** generalizes implementation effectiveness (**a_θ, b_θ**) across multiple scenarios, requiring Bayesian inference and Monte Carlo simulations to track how **beliefs evolve with each market observation**. Unlike in the coffee example, where discrete testing suffices, **EV adoption involves dynamic adjustments**, such as pricing strategies, technological advancements, and policy shifts. Capturing these **complex interactions necessitates computational modeling**, making a normal distribution a more suitable framework for decision-making.

While coffee quality perception is often discrete (good vs. bad), decision-making in industries like electric vehicles involves continuous trade-offs, such as battery range, cost, and manufacturing efficiency. EV success depends on **gradual variations in both idea quality (market demand) and implementation effectiveness (cost efficiency, supply chain constraints),** requiring a model that captures **incremental improvements, investment trade-offs, and continuous learning from market signals.** This motivates our shift to a normal distribution framework in Section 2.2, allowing for more nuanced updates and strategic adjustments.

### 2.2🚗 EV Context (Normal Distribution Extension)



Table compares **Sec. 2.1 (Coffee: Peet’s vs Starbucks)**, **Sec. 2.2 (EV: Better Place vs Tesla)**, and **Sec. 2.3 (EV: Toyota vs Tesla)**. Each row references the relevant “🔑table titles” from #🗄️scott to highlight how these examples differ in terms of the Four Axioms, Strategy Compass, key uncertainties, etc.

## 1) Fundamental Difference (Sec. 2.2 vs Sec. 2.3) in Scott’s Terms

[](https://github.com/hyunjimoon/tolzul/blob/ca267a6a8873deda2a169c07448af8543ace32a8/%F0%9F%8C%99amoon\(\)/%F0%9F%8C%99thesis/Exchangeability%20in%20Entrepreneurship/form\(ent\(exbl\)\).md#1-fundamental-difference-sec22-vs-sec23-in-scotts-terms)

In **Sec. 2.2 (Better Place vs Tesla)**, both players are _entrants_ attempting to deliver new “system innovations” (to use Table 2’s language) for EV technology. This scenario reflects a _Disruptor or Architectural orientation_—no incumbent is dominating, so each entrant is searching for an advantage in a relatively open market structure. According to Scott’s **Four Axioms** (Table 1), there is significant _Uncertainty_ about which new EV approach (battery-swap vs. integrated battery + charger network) will best create and capture value, and both must manage _Noisy Learning_ about consumer acceptance.

By contrast, **Sec. 2.3 (Toyota vs Tesla)** pits an _incumbent_ (Toyota) against a _disruptive entrant_ (Tesla). The market for “electrified vehicles” is partially established (Toyota’s hybrids), so there is _Constraint_ (Axiom 2) from Toyota’s existing capabilities and brand. Meanwhile, Tesla is embracing a _Disruptor strategy_ (Table 2) and invests heavily in _Execution_ on integrated capabilities. The fundamental difference is that Toyota’s large existing assets and brand shape its risk posture and ability to adapt, while Tesla’s path is riskier but can yield a novel architectural advantage. Thus, from Scott’s perspective, the **core contrast** in Sec. 2.3 is _incumbent vs. disruptor strategies_ under more direct head-to-head competition, whereas Sec. 2.2 is _two entrants_ vying to shape a still-emerging EV market.

Below is one **crisp table** aligning each section’s example (Coffee vs. two EV scenarios) with the “🔑table titles” from #🗄️scott. We highlight how each example maps to the Four Axioms, Strategy Compass, key uncertainties, etc.

| **Section** | **Context & Players** | **Four Axioms (Table 1)** | **Strategy Compass (Table 2)** | **Key Uncertainty (Table 5)** | **Relevance of “Test 2 Choose 1” (Table 7)** |

|--------------------------------|----------------------------------------------------------|----------------------------------------------------------------------|---------------------------------------------------------------------------|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Sec. 2.1**  
_Coffee_  
(Peet’s vs. Starbucks) | Two _alternative_ expansions of a high-quality coffee idea:  
– Peet’s invests in artisanal beans  
– Starbucks invests in café model | 1) **Freedom**: More than one path to create value (retail café or premium beans).  
2) **Constraint**: Couldn’t do both at scale simultaneously. | Both lean toward _Value Chain_ or partial _IP_ (they focus on functional resources— sourcing/roasting vs. cafe ops).  
(See “The Partners” in Table 2 if collaborating with supply chain) | Mostly **Epistemic**— uncertain how American consumers adopt new coffee habits. Historical data were scant for “Italian bar” concept. | Each tested, _to some extent_, a pilot. Starbucks did a “pop-up cafe.” Peet’s stuck with careful expansions. Demonstrates how parallel testing clarifies which route is more viable before committing large resources. |

| **Sec. 2.2**  
_EV: entrant vs. entrant_  
(Better Place vs. Tesla) | Two _newcomers_ in the EV space:  
– Better Place tries battery-swap infrastructure  
– Tesla invests in integrated battery + charging network | 1) **Uncertainty**: No clear track record for pure EV approach  
2) **Noisy Learning**: Pilots reveal viability of swap stations vs. integrated superchargers. | Both are closer to _Disruptor_ or _Architectural_ (Table 2). They are exploring “new users, new system innovations.” They differ in **execution** approach: infrastructure vs. integrated. | Primarily **Epistemic**— no established demand data for large-scale EV, plus partial _Aleatoric_ from unknown consumer tastes & battery tech. | Each must “test 2 choose 1” early. Better Place invests heavily in physical swap stations, Tesla invests in battery R&D + superchargers. In parallel, they validate different system designs to see which best scales. |

| **Sec. 2.3**  
_EV: incumbent vs. entrant_  
(Toyota vs. Tesla) | An established automaker with hybrid success (Toyota)  
vs. a pure-EV disruptor (Tesla) | 1) **Constraint**: Toyota’s existing brand, supply chain, & incremental approach.  
2) **Uncertainty**: Whether Tesla’s radical integrated EV can outpace Toyota’s “hybrid-first” stance. | Toyota may lean _Value Chain_ or _IP_ to protect existing capabilities. Tesla uses a _Disruptor_ strategy, investing in integrated capabilities for new customers. | Mixed **Epistemic** and **Aleatoric**. Toyota has partial data from hybrids. Tesla faces unknown scale-up and competitive response. | Toyota can do “learn while scaling hybrids.” Tesla “goes all-in” on pure EV. Each has to weigh cost of large pilot expansions. Testing multiple approaches is restricted for Toyota by legacy constraints, while Tesla’s approach is a high-stakes single path. |

**Key Takeaway**:

- **Sec. 2.1**: Two _alternative expansions_ from the _same idea_ (quality coffee).
    
- **Sec. 2.2**: Two _entrant_ startups racing to define a new EV approach.
    
- **Sec. 2.3**: Incumbent (Toyota) vs. disruptor (Tesla) contending with legacy constraints and radically new system design.

----

### Many Alternatives

While an important aspect of the process of founding a firm is to conceive of and refine an idea, a separate and equally crucial challenge is to identify and implement a specific approach that will both create and capture value from that idea.

This is a formidable requirement: it is simply not enough to identify a novel, yet plausible plan to apply a new technology to a new market; instead, entrepreneurs must be able to identify a segment of customers willing to pay (or eventually willing to pay) for the idea, and in most cases, be willing to change their existing behavior in order to take advantage of it (e.g., by purchasing a new good, or even undertaking investments or commitments to take advantage of the new good on an ongoing basis). For most entrepreneurs with ideas that are promising enough to contemplate founding a new venture, there are key decision points where the commercialization alternatives to choose from are numerous. These are often critical moments in the founding and scaling of a venture. While many businesses face a choice between alternatives, it is in startup firms that this fact is most salient. With no pre-existing reputation or historical record to infer “best practices” from, startups will have more alternatives to choose from, and also a lot of freedom to pursue any of these paths.

Many founders do not struggle with articulating a single idea to create and capture value. Sometimes, they can even develop multiple ways to do so, and the question is which one of their alternatives is best. When you walk into a Starbucks you are hit with a considerable choice of beverages with many options. A similarly wide set of choices was in front of the founding team of the then-fledgling Starbucks Coffee Company when their new hire, Howard Schultz, suggested an alternative strategy for their idea of introducing high quality coffee to the United States. At that point, the founders had commercialized their idea by selling coffee beans and coffee roasting equipment to home consumers. Schultz, returning from a trip to Milan, proposed an alternative: translating the Italian coffee bar concept to the United States. He even conducted an experiment by transforming their retail store into a pop-up café for a few weeks. This effectively presented the founders with two alternatives for their future focus. Starbucks could continue its focus on coffee bean sales by prioritizing decisions like improving their abilities to select and source coffee beans, and identifying better roasting technologies. Or it could focus on retail coffee bars, which prioritized a much different set of decisions, like building expertise in real estate and retail operations. Another example is Netflix founder Reed Hastings, who considered and tested multiple strategic paths to find value from his plan to deliver videos to consumers without them leaving their homes. First, he built a business based on replicating the video store experience (including late fees), and then he abandoned those fees altogether with a DVD subscription service that focused on less mainstream content. The choice between them arose through extensive experimentation and testing of different models and their impact on consumer retention and the logistics of shipping DVDs. Hastings also actively sought partnerships with Blockbuster and Amazon. At the same time, he never lost sight that in the relatively near future, not even DVDs would be required and there would be direct online movie delivery.

The lesson here is that understanding that there were alternative strategies that could support their ideas, Schultz and Bezos’ approach was superior to prematurely restricting to one path; a path that would have explicitly limited the amount of market-testing they could have undertaken. Having many alternatives paths for a given idea implies an important insights about being an entrepreneur:

First, successful ideas most often have more than one alternative path by which value can potentially be created and captured. Second, and significantly, there is a core distinction between the initial entrepreneurial idea (or opportunity!) and the ways to commercialize that idea.

This was certainly the case for Bezos, who considered a whole range of product categories upon which to start Amazon. It was also part of the plan for Tristan Walker, Founder and CEO of Walker & Company. Walker’s initial insight came from a problem he had faced for years: razor bumps. This common condition – affecting up to 80% of black men and women and 30% of men and women of others races – lacked a simple solution. 2 His first product, the Bevel razor, was an elegant updated design based on the single blade double edge safety razors used a hundred years ago and yet superior in addressing razor bumps than the ubiquitous multiblade systems of today. Yet, having established the opportunity. Walker considered multiple paths to commercialize his idea: this included, building out a company focused on developing solutions to address conditions that affected people of color (including Vitamin D deficiency and hyperpigmentation), building out a “single blade” system and product line for razor bumps, or partnering Bevel with leading consumer products and shaving companies. In considering these alternative routes, Walker realized that leveraging the resources of an established partner would allow him to build the company that best aligned with this vision and passion: an enduring organization making health and beauty simple for people of color across the world. 3 P&G acquired Walker & Company in 2018.

Of course, there are instances where an entrepreneur’s or start-up’s plans will not have many alternatives. For example, in the case of drug development, some drugs are developed for a single, clearly defined patient population from the outset. Here, creating and capturing value from the idea does not require a



https://www.cnbc.com/2015/03/13/tristan-walker-aims-to-change-the-world-starting-with-razors.html https://www.gic.com.sg/thinkspace/enterprise-excellence/tristan-walker-founder-and-ceo-of-walker-and-company/ and https://www.fastcompany.com/90280166/tristan-walker-announces-acquisition-by-procter-gamble-will-remainas-ceo-and-move-company-to-atlanta

meaningful choice (among customer segments) but instead simply requires a willingness to undertake a risky investment in commercializing the drug.

Tight Constraints

Having many options is one thing, but what startups do not possess are the resources to explore several of those options at the same time. Unlike their larger counterparts, startups cannot diversify their approaches and assign multiple teams for exploration. This forces them to both choose between those alternatives and sequence even how they explore and learn about each option.

In the case of Schultz and Starbucks, the difference in direction between an initial focus on coffee beans for the home consumer and a focus on the café experience led to a split. These two alternatives seemed strategically inconsistent: on the one hand, the original coffee bean and equipment sales strategy pitched consumers an elevated home coffee experience by purchasing high-quality beans and brewing equipment themselves; on the other hand, the retail café strategy would require convincing consumers to adopt a different behavior of drinking coffee outside of their home in a community setting. Given its scarce resources at the time, Starbucks could not have achieved both of these visions simultaneously.

After the original founders decided to continue with their original focus on coffee beans rather than retail, Howard Schultz left Starbucks to found the coffee bar Il Giornale. Because the team needed to focus (initially) on only one direction to be successful, they had to break apart when different members of the team felt that strongly about the way to go. In this case both paths ultimately ended up finding success. Eventually, when starting to scale his coffee bars, Schultz purchased the rights to the name Starbucks from the original founders. However, the founding group kept at their plan too, finding success with Peet’s Coffee (See BOX: Starbuck’s Alternative Timeline: Peet’s Coffee).

Caption: The three founders of Starbucks: Zev Siegl, Jerry Baldwin & Gordon Bowker (Howard Schultz is not pictured).

Starbuck’s Alternative Timeline: Peet’s Coffee

Peet’s Coffee was founded by Alfred Peet as a local coffee shop in Berkeley in the 1960s. His fascination with coffee started as a young boy maintaining the equipment in his father’s coffee and tea business in Holland. By the time Peet landed in California, he’d spent years in Indonesia learning about the coffee bean and built a career in the coffee import business. However, he soon found the American market inexperienced and relatively uninterested in the high-quality coffee beans he imported. By opening a coffee shop, Peet’s idea was to bring better coffee to the American market by combining his quality beans with a carefully calibrated blending and roasting process.

By the early 1970s, with locations in Berkeley and Menlo Park, Peet’s Coffee was an established leader in crafting rich blends for the American consumer. Entrepreneurs and coffee enthusiasts alike sought him out to learn the art and business of coffee. Among these was Jerry Baldwin, one of the co-founders of Starbucks, who had been inspired by Peet’s when he founded Starbucks in Seattle in 1971. Interestingly, Starbucks at the time was an outlet for selling coffee beans, not coffee itself, and Peet provided many of those beans. In 1979, Peet sold his then four shops and by 1984, they were in the hands of Baldwin. When, in 1987, Baldwin sold Starbucks to Howard Schultz, who saw it as an opportunity for retailing coffee rather than beans, Baldwin decided to re-focus on Peet’s and his commitment to coffee beans.

While Starbuck’s growth was explosive with tens of thousands of cafes opening across the globe, Peet’s expanded very slowly. Baldwin’s desire was to ensure that only the best coffee beans were used, and the scarcity of that supply also constrained Peet’s. As a result, Peet’s Coffee achieved a more modest level of scale with just over 200 locations by 2018. Throughout this growth, Peet’s continued to build its reputation in the coffee roasting and blending business and expanded to other retail channels, including grocery stores.

It is easy to conclude that Baldwin made the ‘wrong’ choice with Peet’s strategy compared to Schultz with Starbucks. However, Peet’s itself has proven to be a respected venture with locations

--- 
### Test Two Choose One

Facing the choice and learning challenges is, importantly, a sign of a potentially fruitful entrepreneurial opportunity. Imagine if there was only one available alternative open to the entrepreneur to commercialize their idea. What does this tell you about the idea itself? Can an idea really be of high value if there is only one type of, say, customer, or one way of building a working product that can build a profitable venture? This is unlikely. Thus, a choice challenge is something that accompanies ideas that are likely to be of high quality. Evaluating a wide number of alternatives gives a sense for the range of value in an idea. With a really promising idea, a founding team can often determine multiple promising plans. We saw this earlier in the case of Amazon and Starbucks. On the other hand, for a mediocre idea, the team, at best, will be able to identify only a single viable path forward.

Similarly, imagine if it was obvious which path among the available alternatives was the best one to choose. If it is so obvious how you can take a high quality idea and bring it to market, is this the sort of opportunity that will be unique to, you, as an entrepreneur to develop? Probably not. Thus, a learning challenge is something that accompanies ideas whose pursuit and development is non-obvious.

For an entrepreneur, choosing requires dealing with the learning challenge in order to confront the choice challenge. The entrepreneurial choice process forces a team to surface multiple promising options, and gain insight from simply doing so. When the team begins identifying multiple concrete plans that meaningfully realize the potential value of their idea, then they should move beyond search and choose and implement one. We summarize this best practice with the idea of Test Two Choose One.

Test Two Choose One. For a given idea, entrepreneurs should only begin to commit to one strategic path after considering multiple strategic alternatives and identifying at least two that are commercially viable yet difficult to rank. This is a principal you will see used throughout the book and has been used by countless entrepreneurs in choosing their path to translating their idea into reality. We want to show you how to create a procedure that implements Test Two Choose One as a way of confronting the learning and choice challenges you will inevitably face as you consider a venture. We will then return to the process in Chapter 13, walking you through the detailed playbook to translate your idea to reality. First, let’s understand why entrepreneurs need this playbook.


Q. How would you describe the “idea” behind Starbucks (in its original form)? How would you describe the alternative paths pursued by the original founders versus Howard Schultz? What are some of the key choices that each made (and how (if at all) did they differ?


### starbucks choosing scaling
By contrast, Starbucks (which we first encountered in Chapter 4), found itself locally successful with just 11 stores and 100 employees. It was still making losses when Starbuck’s founder Howard Schultz decided to solve a major potential imbalance – retaining good employees. Despite not being profitable, he made the decision to invest heavily in employees with some very (at least in the 1980s) unconventional moves. Specifically, he decided to give all employees health insurance and stock options. And not just full-timers but part-time employees too; a first for the US. With such inducements in place, Starbucks was in a position to rapidly grow. Four decades later it has 28,000 stores in 76 companies. But even then investing in employees continued with a free college tuition program in 2014. In China, to raise the perceived status of working for Starbucks, health insurance benefits were expanded to an employee’s parents.

SurveyMonkey and Starbucks show how startups, once they are gaining traction, can recognize imbalances and put in place countermeasures and efforts to generate further, more rapid growth.




