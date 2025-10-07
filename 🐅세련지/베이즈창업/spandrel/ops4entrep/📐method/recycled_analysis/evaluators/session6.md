2025-05-01

 After reviewing the transcript about the Creative Destruction Lab (CDL) mentorship system, I'll extract relevant equations and comments, then express my answer as mathematical equations.

### Relevant Equations/Comments from the Transcript:

1. Quality improvement model: "Qj,t+1 = Qj,t + ω1Aj,t + ω2Mj,t + εj,t" (where Q is startup quality, A is advice implementation, M is mentorship received, and ε represents other factors) [From slide ~1:19:27]

2. Mentor learning rate: "They only update their beliefs from actually observing the startup itself, 2.8% most of their new perception is based on their initial perception of the startup plus whatever weight they put on." [1:39:19]

3. Information spillover between mentors: "The information spillover... is 71% so there's a really high degree of information sharing and mentorship interaction informs other mentors in the network." [1:39:30]

4. Impact estimate: "An extra hour of mentoring increases the amount of capital raised by 1.5 percentage points." [1:30:18]

5. Mentor belief updating: "μj,t+1 = α1Qj,t + (1-α1-α2-α3)μj,t + α2Aj,t + α3Mj,t" (where μ is mentor belief about startup quality) [Simplified from belief updating discussion ~1:33:00]

### Three Mathematical Equations Summarizing the Findings:

1. **Quality Evolution Equation**:
   Qj,t+1 = Qj,t + 0.253Aj,t + 0.673Mj,t + εj,t

2. **Mentor Belief Updating Equation**:
   μj,t+1 = 0.028Qj,t + 0.699μj,t + 0.153Aj,t + 0.12Mj,t

3. **Information Sharing Equation**:
   μi,j,t+1 = μi,j,t + 0.71(μk,j,t - μi,j,t)
   
   Where μi,j,t is mentor i's belief about startup j at time t, and μk,j,t is another mentor k's belief who directly observed the startup.

2025-04-30

🧬digesting as influe think of this as selfish gene logic where human's nature is to desire for influence (whether biological or spiritual) and invest money, time, effort to satisfy that desire. i.e. my business model is to create and capture value using optimism of the five professors. several success examples is implementing the advice of mentor/investors have increase the startup quality as measured by one research using creative destruction lab venture accelerator database (description attached). using charlie's advice - you want others to feel excited about your research, and the recipe for others to get excited about something is, first find a shared vision (as you go up the ladder of abstraction, you can find shared vision with everyone e.g. from optimism of small scope like entrepreneurship to bigger scope of world peace). then given the shared vision, help them understand what they can contribute to they would find a "how" themselves.

2025-04-28

using requesting paper titles on [inventors, entrepreneurs, economics cld](https://claude.ai/share/b0b659f4-81ee-47f3-a06d-c592015716d5)
# Bayesian Entrepreneurship Research Curation

|Paper|Expert Curation|Kid-Friendly Explanation|
|---|---|---|
|[📜 Jovanovic (1982). Selection and Evolution of Industry](https://www.jstor.org/stable/2555498)|• Pioneering model connecting Bayesian learning to firm dynamics<br>• Firms update beliefs about their efficiency based on observed profits<br>• Explains empirical patterns of higher growth variability in small firms|• Tesla started making Roadsters without knowing if they'd be successful<br>• Their sales performance taught them they were good at making electric sports cars<br>• This learning shaped Tesla's growth decisions, just like all companies learn from market feedback|
|[📜 Bayesian Modeling of Mentorship in Startup Accelerators (Mohadesh najad, 2025)](https://www.researchgate.net/profile/Mohadess-Najad)|• Examines mentorship through direct effects (advice) and screening (identifying promising startups)<br>• Mentors update beliefs slowly (2.8%) but share information extensively (71% spillover)<br>• Entrepreneurs prefer implementing low-cost advice over capital-intensive recommendations|• Dale Hill mentored Proterra's teams as founder and "chief mentor" while building electric buses<br>• His industry experience from previous ventures helped teams navigate technical challenges<br>• Despite his mentorship, Proterra eventually filed for bankruptcy in 2023 due to manufacturing challenges|
|[📜 Astebro, Jeffrey & Adomdza (2007). Inventor Perseverance After Being Told to Quit: The Role of Cognitive Biases](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=925223)|• Examines why inventors continue projects despite negative feedback<br>• Found 29% keep spending money and 51% keep spending time after being advised to quit<br>• Identifies optimism and sunk-cost bias as key drivers of perseverance|• Some people making electric cars would keep trying even after experts said their designs wouldn't work<br>• Like if Tesla was told the Roadster would fail, but Elon kept building it anyway<br>• They continue because they believe strongly in their idea and have already invested too much to quit|
|[📜 Bernardo & Welch (2001). On the Evolution of Overconfidence and Entrepreneurs](https://onlinelibrary.wiley.com/doi/10.1111/j.1430-9134.2001.00301.x)|• Explains why seemingly irrational overconfident behavior persists<br>• Overconfident entrepreneurs provide valuable information by ignoring the herd<br>• Though they make more mistakes and fail more often, they benefit group success|• When everyone was making gas cars, Tesla boldly made electric sports cars because they were confident they knew better<br>• While many overconfident car startups fail, Tesla's success changed what everyone knows about electric vehicles<br>• Sometimes we need confident entrepreneurs to try new ideas even when most will fail|
|[📜 Nelson & Winter (1982). An Evolutionary Theory of Economic Change](https://www.hup.harvard.edu/books/9780674272286)|• Groundbreaking book challenging mainstream economics using biological concepts<br>• Applied natural selection to business behavior, innovation, and competition<br>• Firms follow routines and search for improvements rather than simply maximizing profits|• Car companies like Tesla evolve like animals in nature - the best ones survive and grow<br>• Instead of perfectly calculating everything, companies follow habits and routines, trying new things when needed<br>• Electric car companies that innovate better ways to make batteries or motors will grow while others disappear|
|[📜 Decker, Haltiwanger, Jarmin & Miranda (2016). Declining Business Dynamism: What We Know and the Way Forward](https://www.aeaweb.org/articles?id=10.1257/aer.p20161050)|• Documents declining rates of job flows, entrepreneurship, and young firm activity<br>• Trend is pervasive across industries, regions, and firm size classes<br>• Examines relationship between productivity and employment growth in changing economy|• There used to be many more new car companies starting up in America than there are today<br>• Before Tesla, it had been decades since a successful new American car company was created<br>• Understanding why fewer people start new companies like Tesla helps us create better policies|
|[📜 Henderson's work bridging evolutionary and mainstream economics approaches](https://www.hbs.edu/faculty/Pages/profile.aspx?facId=6483)|• Successfully connected Nelson & Winter's evolutionary approach with conventional economics<br>• Applied rigorous methods while maintaining focus on dynamics of innovation<br>• Helped evolutionary economics gain acceptance in mainstream academic discourse|• Imagine someone who can speak both Tesla engineers' language and traditional car company language<br>• She helped translate new ideas about how electric car companies evolve into terms old-school economists understood<br>• Her work built bridges between different ways of thinking about how companies like Tesla change over time|

## first paper
homogenous product
time path of demand and price ard deterministic and known
no aggregate product (can't affect the product)

decision1: enter market or not
decision2: observe profit - update my prior based on theta 

update my prior and choose exit or enter and if enter how many to produce

expected sum of disounted profit
theta bar (avergae)

firm's efficiency function x_t is determined by firm type (monot)

product decision

xi is not theta but theta + noise

-c(q)x_t (firm chooses quantity), 
expected sum of discounted 

every firm can't get profit


theta upper bar is theat i need to enter the market, 

given profit and cost function, production cost is lower than expected 

![[session6 2025-04-28-18.svg]]
%%[[session6 2025-04-28-18|🖋 Edit in Excalidraw]]%%

⭐️cost is noisier than profit

recovery cost is less than the (w<k)

after entering the market, every round significantly update their priors leading to large variability inoutputs overtimes

bad type -> lowers (overtime, everything evens out)

don't need cognition if selection pressure is high

disciplining effect of competition 

currently 

what do they know when they enter and what do they learn

----

## second paper

direct effect, screening effect

choose multiple paths to bring idea to market
sales and markeing vs product development

different levels of mentorshipi

charlie asked - 

mentors, startups, sessions, true intital quality

ADJUSTMENT TO OBJECTIVE



[[session7_social planner]]