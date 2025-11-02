### 1. challenge in interdisciplinary research 
- story and unit of value in different value
- lifecycle of phd
- mentorship from prob.comp perspective


scientific research is objective, research felt more objective when (fool myself it's more objective);  very clear it is story telling ; science vs intuitive conception of it

social epistomology of the field you're in
(subjectivity replaced by awareness of multiple perspectives and context dependence)

attached to research (viable, growth, when tdoes it matter who's doing research lab A vs lab B) - l

CV/ML
- machine learning originated from computer vision
- different 
- BILL FRREMON: in addition to the result, we can have some insight
- performance metric
- external validity of the result
⭐️good implementation of bad idea (external validtity - reason it can appply outside)
CV become so empirical (intrinstic property)

bespoke hadnd crafted data 

gen3d, genLM, (techincal ; concept decreasse model) - conceptualed novel, technically mature, calibrated to market HARD TO DO ALL SAME

specilization X enables soundness A / performance B / automation C

complier problem: problem caputre and  / mechanism to solve prooblems BOTH GENERAL PURPOSE and GOOD PERFOMANCE FOR SPECIAL CASE

database has bunch of structure, 

data and lear problem for it

human can solve better

(career choices they are navigating)


personally so lightly so, so, you know, moving from systems like picture or like clips from Chen's work, which also is evaluated a little bit of this form, which were kind of like slightly bespoke, hand created data sets, to sort of illustrate The point of some new idea, we moved to data sets that were a little bit more standard, might be clean and larger, so like much, much more standard benchmarks that many people have taken shots at, like Gen 3d and in general, that reflects, in some ways, An increase in technical maturity, but I would also say a massive decrease in conceptual novelty. There's sort of an economics to that very hard to be both conceptually novel and technically mature, and like calibrated to some market all at the same time.
in programming languages, we've got other types of stories. I think the ones I feel get the closest to the heart of the discipline actually are specialization X enables systems with soundness property a or performance characteristics B or automation C. The reason why I'm saying that's the part of the discipline is because, in some sense, any method for computing is a specialization over just computing somehow. And so there's some fairly deep metal level where that's like one of the only stories. And in fact, I don't think that's just cute, you know, eventually, right? If we want to have general purpose AI, and understand how we can have general purpose AI that, like, is very broad, but also can specialize itself. Like, in some sense, that's a PL problem applied to probabilistic inference and decision theory. How is it possible to have something which can take any problem, synthesize a model for it, or probabilistic model, an inference process and the decision process, and generate specialized implementations that get better or tuned to workloads over time? And do all of that in any domain, like the extent to which that's possible, that's like kind of a compiler problem, the only technology that lets you have the general purpose method problem capture that still gives high performance specialized instances. Clearly, that's something about what we mean by general intelligence, because that is a mechanism which can solve problems, you know, like a very broad, open ended class of problems, and then specialize itself to get better, so somehow builds a general purpose and competitive in special instances. So


there's a lot of depth to that class of stories. Gen, SQL is one very good, I think, modest example of the story of that form probable programming languages.

But if you consider the context of databases, there's a bunch of structure there, and if you explain that structure, you can relax the constraints on soundness, and you can get better automation and better performance,


something I like about that genre of PL stories, personally is explains what's doing the work. In some sense, it is the knowledge of how and why you're specializing that's getting you the better soundness or performance. As I'd say, it's from some deeper computer science sense that kind of has to be true, unless what you're saying is you're building some general compiler which is still specializing just at some meta level. Another PL story is that there's some domain of problems and it's better handled by some system than some other system, but the methods of evaluation aren't average performance on some benchmark, usually just a richer set of arguments, and often much sparser data, where there's some task and it can be formalized in terms of an approach, a that's perfectly sound, and it may or may not have some empirical benefits be and so you know, some of Alex's loves. Alex loves work on automated differentiator expected value takes that form. There's this task of which is widespread, and computing, which is differentiating expectations, and you can formalize it as a meta program on probable state programs and prove that you can do

Or some process work, which says, like, you might like to take data and learn problem two programs for it. That's a problem paper in 2019,


using [multidisciplinary ai research tools cld](https://claude.ai/chat/4f1b9d73-b663-4b40-96d8-1e4e6108c293)

|Field|Operations Research|Strategy Science|
|---|---|---|
|Summary|Mathematical method A produces provably more optimal solutions than method B for resource allocation problem P under constraints C with efficiency/scalability E|Organizational approach X generates measurably superior outcomes Y compared to traditional approach Z in competitive environment E when facing constraints C|
|Example|Stochastic programming outperforms deterministic models on supply chain optimization under demand uncertainty, reducing costs by 15% while maintaining 99% service levels|Cross-functional team structures drive 40% faster innovation cycles than siloed departments in technology firms facing rapid market changes and disruptive competition|
|Prob. Comp. Tools|Monte Carlo simulation, Linear/Integer programming, Queuing theory, Dynamic programming, Network optimization|Game theory, Agent-based modeling, Causal inference, Network analysis, Bayesian decision theory|

The Operations Research story focuses on mathematical proof of optimality and efficiency under well-defined constraints, while the Strategy Science story emphasizes measurable organizational outcomes in complex competitive environments with less precisely defined constraints.-
# Operations Research & Strategy Science Structured Comparison

## Operations Research: Method A produces provably more optimal solutions than method B for resource allocation problem P under constraints C with efficiency/scalability E

|Problem (P)|Method A|Method B|Constraints (C)|Efficiency/Scalability (E)|
|---|---|---|---|---|
|Airline Crew Scheduling|Mathematical Programming|Greedy Heuristics|Regulatory rest periods, route coverage, crew qualifications|15% cost reduction while maintaining 99.8% schedule reliability|
|Supply Chain Optimization|Stochastic Programming|Deterministic Models|Demand uncertainty, lead time variability, capacity limits|12% inventory reduction with equivalent service levels across 500+ SKUs|
|Vehicle Routing|Column Generation|Local Search Algorithms|Time windows, heterogeneous fleet, multi-depot constraints|Linear scaling to 1000+ delivery points with 98% optimality guarantee|
|Hospital Resource Allocation|Markov Decision Processes|Fixed Staffing Rules|Unpredictable patient arrivals, varying acuity levels, shift constraints|30% reduction in patient wait times with same staffing budget|
|Investment Portfolio Design|Robust Optimization|Traditional Mean-Variance|Return targets, liquidity requirements, regulatory constraints|Consistent performance across stress-test scenarios with 99.5% VaR|

## Strategy Science: Approach X generates measurably superior outcomes Y compared to traditional approach Z in competitive environment E when facing constraints C

| Approach (X)                          | Traditional Approach (Z)        | Outcome (Y)                              | Competitive Environment (E)           | Constraints (C)                                                      |
| ------------------------------------- | ------------------------------- | ---------------------------------------- | ------------------------------------- | -------------------------------------------------------------------- |
| Cross-Functional Innovation Teams     | Siloed R&D Departments          | 40% faster product development cycle     | Rapidly changing technology landscape | Resource limitations, specialized knowledge requirements             |
| Staged Geographic Expansion           | Simultaneous Multi-Market Entry | 65% higher 5-year survival rate          | Emerging market competition           | Cultural differences, regulatory variation, capital constraints      |
| Agile Digital Transformation          | Waterfall Implementation        | 3x higher user adoption rates            | Digital-first competitors             | Legacy systems integration, organizational resistance, talent gaps   |
| Integrated Skills Development         | External Talent Acquisition     | 25% higher retention and productivity    | Talent war industries                 | Specialized skill requirements, training costs, competitive poaching |
| Stakeholder-Integrated Sustainability | Compliance-Focused Approaches   | 28% premium on sustainable product lines | ESG-conscious markets                 | Resource intensity, cost pressures, regulatory complexity            |

work you have (finger exercise) - able to do rigorous work in X and Y very well - 

advisor wants you to take risks (responsible for both of you)

learning how to take larger risk (market, come back on my shield, apprentice to )

you get funded whe ppl already working for you  (formalize this thing that is already happening) - isn't that person already a professor??
1. track1: become CEP
2. track2: joining a larger organization

calibrate your risk (relatively to your own skill and market) - risking the time of the ppl you're talking to?

academic clock (starts from when you graduate)

understand what happens on the other side of the table

move the direcation for ten ppl to move 

5k -> zero to one (nishad, xuan, ); learning funda

deeper hierarchical planning in service of our actual goals

MAKE YOURSELF INDISPENSIBLE

|Time Scale|Activities|
|---|---|
|O(0.01h - 0.1h) ⚡|- TL;DR that hooks attention and establishes credibility, whether it's for 1 paper or $1M or $10M or...|
|O(1h) ⏱️|- Advising meeting / peer office hours<br>- Give feedback on an MVP<br>- PI review of a typical ML paper<br>- Planning O(10h) of work, in writing<br>- O(10) people listening to you for 5min<br>- Preparing a 5min presentation to O(10) people|
|O(10h) 🕙|- Write design doc; sketch solution to "hard but solvable" problem<br>- Test a usable prototype; prepare a test dataset<br>- Implement a simple published idea using a PPL<br>- PI review of a typical PL paper|
|O(100h) 📅|- MVP that derisks a research or engineering idea, given adequate design doc<br>- Camera-ready version of accepted paper<br>- Drafting an hour-long talk<br>- Testing and revising an hour-long talk / VC funding pitch / sales pitch, with the help of your network|
|O(1,000h) 📊|- Leading a top conference paper<br>- Creating a usable programming system prototype<br>- Raising a Seed / Series A VC funding round<br>- Being on the academic job market|
|O(10,000h) 🎓|- A ~5-year PhD / founder journey for a startup / live OSS project<br>- (Learning fundamentals of using Gen + one application domain is ~5,000h)|
|O(100,000h) 👴👵|- A ~50-year career / 10 people working for 5 years / 50 people working for 1 year|

The emojis provide visual anchors for each time scale:

- ⚡ - Quick, lightning-fast activities (minutes)
- ⏱️ - Standard hour-long activities
- 🕙 - Day-length projects (10 hours)
- 📅 - Week to month-long projects (100 hours)
- 📊 - Quarter to half-year projects (1,000 hours)
- 🎓 - Multi-year educational/entrepreneurial journeys (10,000 hours)
- 👴👵 - Career/lifetime achievements (100,000 hours)


sensible person to become a startup () - oten ways to get some funding (not viable for the next stage)
hierarchial planning(backups chaining)

loving advisor and being indispensible - sharing optimism

for me, i share optimism 

bob telling processors are coming

evaluation and performance metric cannot be determined 

experience of exploration through wandering

interdisciplinary - 

⭐️personal (lecturer setting - ) drop prestige (satisfying) - end up considering ; 
prestigage -> interdisciplinary hire (against the physics)

Q. is the person best person in the field for the next five year?

slot is not by one despartment (power structure) - department is paying

choosing whose advice you'd trust, who'd serve as evaluator of you vision takes the most time - loving advisor and being indispensible - sharing optimism

having general view, 

ANALYZE ENTREPRENEURSHIP
## research frontiers