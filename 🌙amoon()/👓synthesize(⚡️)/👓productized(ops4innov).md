- [[#<span style="purple">customer_action(researcher)</span>|customer_action(researcher)]]
- [[#<span style="green">bit_action(researcher)</span>|bit_action(researcher)]]
- [[#<span style="red">atom_action(researcher)</span>|atom_action(researcher)]]
		- [[#⚙️auto(mng())|⚙️auto(mng())]]
		- [[#👓auto(mng(comp(stat()))|👓auto(mng(comp(stat()))]]
		- [[#🧠comp(stat())|🧠comp(stat())]]
- [[#product(researcher)|product(researcher)]]
		- [[#📄paper|📄paper]]
		- [[#🛝slide|🛝slide]]
		- [[#🔐code|🔐code]]

![[theory-experiment-phenomena-desire.png|500]]
## <span style="color:purple">customer_action(researcher)</span>
- value proposition: innovative management of bit, atom, energy with growth-aware exploration
- which audience would need the above value the most?
- can my technology be solutions for the value proposition?

## <span style="color:green">bit_action(researcher)</span>
is ideas behind my research, and covers management, statistics, computation via simulation-based continuous improvement: Dynamic decision from Management (M), supported by dynamic model from Bayesian Statistics (S), supported by scalable Probabilistic Computation (C).

## <span style="color:red">atom_action(researcher)</span>
#### ⚙️auto(mng())
is about how dynamic decision from Management (M), supported by dynamic model from Bayesian Statistics (S), supported by scalable Probablistic Computation (C)
- [[⚙️auto(mng())]] lists my publication on matching data supply with demand and multi-seasonality
- [[nextopt_B2NBC_roadmap]] records how I actively design business based on past experience

#### 👓auto(mng(comp(stat()))
is about how system of different components (M, S, C) can be harmoniously managed
- [[👓auto(mng(comp(stat()))]] lists my publication on two topics: Predictive maintenance (system dynamics simulation, hierarchical modeling, Bayesian averaging) and Simulation-based Calibration (developing statistical theory justifying approximation, constructing updating scheme based on interpretable, diagnosing [[🧠comp(stat())]]

#### 🧠comp(stat())
 [[🧠comp(stat())]] is about how computation and probabilistic model meet
- stats: dynamic high dimensional hierarchical Model
- comp: scalable probabilistic computation
	- Hamiltonian Monte Carlo
		- Clamped HMC: combining Gibbs sampler and HMC
		- embedded Laplace approximation and its adjoint-differentiated version
		- [[startup_prediction]]
	- Sequential Monte Carlo

Relevant diagrams: [[academic_app.png|center]]

## product(researcher)
#### 📄paper
Featured (Book) Gelman, A. et al., (2020) Bayesian data analysis (Moon, H. et al. Translator). Bookcube (Original work published in 2013)
Featured (Paper) Modrak, M., Moon, H., Kim S, P. Burkner, N. Huurre, A. Gelman and A. Vehtari (2022). Simulation-Based Calibration Checking for Bayesian Computation: The Choice of Test Quantities Shapes Sensitivity. (Bayesian Analysis, submitted) [Paper](https://arxiv.org/pdf/2211.02383.pdf) [Code](https://github.com/hyunjimoon/SBC)
Moon, H., & Choi, J. (2021). Hierarchical spline for time series prediction: An application to naval ship engine failure rate. Applied AI Letters, 2(1), e22. [Paper](https://onlinelibrary.wiley.com/doi/full/10.1002/ail2.22)[Code](https://github.com/hyunjimoon/defense-reliability/blob/master/R/2_Theta_bar_Y/spline/navy/Failure%20prediction%20in%20hierarchical%20equipment%20system.ipynb)


Moon, H., Song, B., & Lee H. (2022) Mixed pooling of seasonality for time series forecasting: An application to pallet transport data. Expert Systems with Applications, 201, 117195. [Paper](https://www.sciencedirect.com/science/article/abs/pii/S0957417422005826?casa_token=K8sO8sq5pxQAAAAA:I9bo13yjknP5EAQ5aRgy4p-H3-lHCBP2spzWzfBQi6PsvDHcUBp6S1Tg4l2-15u-TnfRpLQ) [Code](https://github.com/hyunjimoon/Mixed-pooling-paper)
Moon, S., Choi, K., Choi, J., Moon, H. (2022) Inventory Management with System Dynamics / Vensim. Bookcube 
Choi, J, Moon, H., Cho, W. (2020) Preventive Maintenance Interval Optimization based on Lifecycle Failure Prediction. Korean Journal of Logistics, 28(6). [Paper](https://www.researchgate.net/publication/346259943_Preventive_Maintenance_Interval_Optimization_based_on_Lifecycle_Failure_Prediction) 
Moon, H., & Song, B. (2019) Time Unit Clustering Model for Pallet Movement Amount. Korean Journal of Logistics, 27(4), 1-10. [Paper](https://www.researchgate.net/publication/346259742_Time_Unit_Clustering_Model_for_Pallet_Movement_Amount)[Code](https://github.com/hyunjimoon/2018_Paper_Time-Unit-Clustering/tree/master/Tutorial/TUC_Experiment)
Kim, H., Moon, S., & Moon, H. (2017). Parallel military supply chain for resilience. International Journal of Advanced Logistics, 6(2), 80-87. [Paper](https://www.tandfonline.com/doi/abs/10.1080/2287108X.2018.1472966)

#### 🛝slide
- [[Moon18_auto(mng(inven)).pdf]] describes developed application for demand forecasting and inventory management
- [[Moon19_timeseries_stan.pdf]] explains how Stan, open-source bayesian computation library, can be used for time series
- [[Moon20_LetsSBC_GelmanIntern.pdf]]
- [[Moon22_ActionableWorkflow.pdf]]
- [[Rahmandad_Moon22_BayesSD.pdf]] summarizes my collaboration with Hazhir on analytical approach to system dynamics model. I contributed to 15.879 style (Bringing data into dynamic models) with my expertise on Bayesian workflow. Hazhir is the main author of the slide itself.
- [[Moon24_Stone_Gauntlet_Snap1.pdf]], [[Moon24_Stone_Gauntlet_Snap2.pdf]] for [[15s.03]]

2023
- [[MoonFiddaman23_stanify.pdf]]
- [[RFHM_SDConf2023.pdf]] was selected as planetary speech in International System Dynamics Conference 2023
- [[Moon23_ops4entrep.pdf]] introduced operations and innovation management to thirty Hyundai Mobility employees, led by Go Young Suk
- [[FiddamanMoon23_questions to ask given vensim is the answer.pdf]]
- [[23F_M3S_Moon23_proposal_3pg.pdf]]

- [[playbook.canvas]]
#### 🔐code
- maintaining five libraries are in [[def(hacker)]], but themes are largely three:
- Bayesian computation: algorithm (spectrum from optimization to variational inference to hamiltonian monte carlo), regression and time series statistical model
- System dynamics: [[mng(atom)]], [[mng(game)]], [[mng(bit))]], [[mng(city)]], 
- Econometrics: [Dynamic stochastic general equilibrium (DSGE)](https://www.sas.upenn.edu/~schorf/papers/er-final.pdf)

