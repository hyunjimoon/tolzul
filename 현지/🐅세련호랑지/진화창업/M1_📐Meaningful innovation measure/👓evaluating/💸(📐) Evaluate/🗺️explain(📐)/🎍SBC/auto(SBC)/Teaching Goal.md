> If you’re looking for a formula for greatness, the closest we’ll ever get, I think, is this: Consistency driven by a deep love of the work. – Maria Popova

### SD example of Guard and Attack system with Two Stocks: SI vs PP

| -                      | Suceptible-Infected           | Prey-Predator                                |                                                        |
| ---------------------- | ----------------------------- | -------------------------------------------- | ------------------------------------------------------ |
| order                  | stock-flow-stock  (closed system) | flow-stock-flow (open system)                  |                                                        |
| members                | cooperative actors            | competitive actors                           | competition:= heterogeneous goals                      |
| global goal            | guard, allocate within        | attack, match between                        |                                                        |
| relation between boxes | zero sum, relative            | absolute                                     |                                                        |
| # of flow/ # of box    | < 1                           | > 1                                          |                                                        |
| model for              | diffusion                     | competition, M:1 matching                    |                                                        |
| scale of `est.param`   | free (given N, ratio form)    | scale dep. coef. of rate (u-coef vs uv-coef) |                                                        |
| time window            | instant                       | long-term                                    | reason why time-hetero transm. rate is emphasized (HR) |
| equilibrium            | (space-time) locally stable   | locally unstable                             |                                                        |
| reference              | BD ch.9, negative feedback    | BD ch.10, positive feedback                  |                                                        |
| tag                    |       #ZeroSum                         |                                              |                                                        |

## How
### 3D
Three dots to connect: data, draws, demand. We first unite [draws-demand] then add data for a complete sync between 3Ds: [data - [draws-decision]]. The main spirit is, real data comes after calibrating the translation of our mental model to statistical+computational model. For this, we first make the rough mockup from data (in the form of prior-knowledge) to draws to decision then build up from the decision's end. As the saying "Match supply with demand" goes, we recommend pull instead of push system. The model building iteration is divided into three and we assume previous modules are built-in in the next.

### 1. Verify Draws-Demand 
In 879 `Bringing data in dynamic models`, we limit the bounds for data, draws, decision as follows.
```
Given the `generator`,
- data: synthetic data
- data to draws: asymptotically unbiased inference algorithms e.g. HMC (and sequential MC)
- demand: stiff binary
```
Examples are not too very complicated (prey-predator, demand-supply, SIR) and the focus is on adding hierarcy in each of them.

### 2. Validate Data - [Draws - Demand]
The difference with the first iteration is the use of real-world data. With this, we reverse engineer the first iteration by asking, "to make our demand noise-resilient, what form should our demand be, what data is needed, and what algorithm can do this most efficiently"? 
```
Given the `real-world data`,
- demand: flexible binary
- data to demand: Bayes factor simulation-based calibration and indirect inference
- draws: posterior approximators from simulation-based inference e.g. BayesFlow
```
Link to [Bayes factor SBC](https://psycnet.apa.org/record/2022-39838-001) and [BayesFlow](https://github.com/stefanradev93/BayesFlow).

This order is common in Bayesian inference where we first build the generator then do the inference conditional on the data. Working in both directions is the benefit of generative model (e.g. Bayesian) which operates on data-parameter joint space. Using this benefit, we argue the best practice of model building is to first make the rough mockup from data to demand then building up from the demand's end. For instance, the effect of new data on demand can be forwardly-simulated, then compared to inform us the best data. This spirit is similar to [Bayesian optimization](https://www.cs.ox.ac.uk/people/nando.defreitas/publications/BayesOptLoop.pdf). However, unlike their description of "taking human out of the loop", we aim to design human-machine interface. In practice, human's form of demand, or activation function in Bayesian optimization, becomes clearer during the model building iteration.

Parsimoniously constructed graphs with appropriate level of parameter uncertainty (i.e. identifiable structure with tight prior distribution) will facilitate the inverse procedure by preventing degeneracy in posterior space.

The value of real-world data i.e. empirical approach are two folds:
1. prevent fixed value of parameters cross the tipping boundaries
2. remove unrealistic attractor

I will use Jeroen's poster in ISDC 2022, _Sustainable consumption transformations: Should we mobilize the young generation?_ to illustrate the two. Appendix Struben22_SustainTrans.pdf is in `Reading` directory the same folder.

First, the model qualification test outcome (pass/fail) depends on the value `assumed parameter` is conditioned updon. Like a water's boiling point (100 degree at 1 atm), tipping points boundary is unavoidable. The least we can do is to move our demand (mostly binary, at most finite) away from these sensitive borders. The easiest remedy is to adjust the fixed value of `assumed parameter` as this sometimes is modeler's rough assumption. However, changing `estimated parameter`'s prior distribution or prior parmeter can be another remedy, followed by changing model parmaeterization or components. Even collecting more data are possible and recommended if this can make our demand more resilient. 

Jeroen's poster on aging model illustrates two attractors in the phase space; however, this analysis is based on the fixed value of `assumed parameter` (noted as green in his poster, e.g. $\tau_{yo}$ active life duration). Fixing $\tau_{yo}$ can be problematic in two ways: first in calibration then in analysis. Regarding calibration, the model that passed quality test when conditioned on $\tau_{yo}$ at 20 can fail the test at $\tau_{yo}$ = 30. In other words, the same model qualifed in 1900s (or at the time when active life duration was 20 years) becomes outdated as society evolved to the era of longer active life duration. Considering both real data and parameter for calibration is well discussed in the upcoming paper on simulation-based calibration. Second, even if the model passed the quality test, under different conditioning, the analysis (two attractors in phase space) may comepletely change. There may be one or three attractors for instance, affecting the downstream policy proposal.

Assumed-value of nuisance parameter affecting the test result is problematic but unavoidable as we can't afford full-Bayesian model where uncertainty is imbued to every parameter. Like a Pirate Roulette game, we should pray each time that our slice of fixed parameter hyperplane does not cross the tipping points. Inference helps us in this respect as we can alternately focus on different parmeters by switching back and forth between `estimated parameter` and `assumed parameter`. This zig-zag learning like that of Gibbs sampling is suboptimal but can help keep modelers away from borders by providing a more global view of the decision geometnry.

Second, is to argue the state value of a particular attractor is not realistic. Globally it may be the bimodal but if the scale of state for the second mode is out of bounds we may as well consider it unimodal. This allows us to save considerable amount of further analysis (`Analysis of tipping behavior` from the poster) by precluding certain scenarios. However, both known and unknown bias should be acknowledged as data in hand may not be the just representation of population.

![[Struben22_Bimodal.png]]
### 3. nonDiscrete [Data - [Draws - Demand]]
For the final iteration, we invite policy and behavior to calibration framework. Both parameteric and nonparameteric approach exist to address these non-binary and sometimes continuous objects. We visit seminal works by John, Tom, Rogelio, Andrew, Yaman, Erling and dissect their softwares to collect six infinity stones on Python, R, Stan (Bayesian computation opensource) as described in [Supply of SilkRoad project](https://github.com/hyunjimoon/DataInDM#supply-of-silkroad-project).

```
Given SilkRoad and `real-world data`,
- demand: flexible binary
- data to demand: Bayes factor simulation-based calibration and indirect inference
- draws: posterior approximators from simulation-based inference e.g. BayesFlow
```

Specific topics are to be decided but,
- Indirect structure testing: Extreme condition hypothesis testing
- Sensitivity analysis (by behavior pattern space): Behavior pattern sensitivity with respect to parameter changes
- Model calibration: Automated parameter calibration based on input (real) behavior patterns
- Policy analysis and design: Policy parameter(s) specification based on desired behavior patterns
- Discuss similarity and difference in discriminate, cluster, classify, outlier-removal from optimization's three steps viewpoint (recognize, evaluate, optimize)

