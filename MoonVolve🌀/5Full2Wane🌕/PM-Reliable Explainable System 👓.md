## M. Predictive Maintenance

### System Dynamics Simulation
- Moon, S., Ji, W., Moon, H., & Kim, D. (2018). A simulation of order resonance phenomenon in a supply chain triggered by reinforcing loop. International Journal of Simulation Modeling, 17, 231-244. [Paper]

- Kim, H., Moon, S., & Moon, H. (2017). Parallel military supply chain for resilience. International Journal of Advanced Logistics, 6(2), 80-87.



### Hierarchical modeling
- Moon, H., & Choi, J. (2021). Hierarchical spline for time series prediction: An application to naval ship engine failure rate. Applied AI Letters, 2(1), e22.

- Choi, J, Moon, H., Cho, W. (2020) Preventive Maintenance Interval Optimization based on Lifecycle Failure Prediction. Korean Journal of Logistics, 28(6).

- Bayesian Hierarchical ODE: See [[Teaching Goal]] 

### Bayesian Averaging
- Kim, S., Nam, K., Choi, J., Moon, H. (2022) A Study on the Failure Function of Logistics Industrial Equipment Using Bayesian Aggregation: an Application to Electric Forklift Engine Failure Rate

[[Forklift_HBayesAgg.png]]



## S. Simulation-based Calibration 

See https://hyunjimoon.github.io/SBC/.

###  1. develop statistical theory justifying approximation
. Credible interval as a function of sample size and the simulator is the outcome. Based on the interval, graphical test that verifies miscalibration is provided through SBC, an opensource package for simulation-based calibration. [package](https://github.com/hyunjimoon/SBC/) [vignettes](https://hyunjimoon.github.io/SBC/articles/index.html)

### 2. construct updating scheme based on interpretable measures
. Different methodologies from Bayesian optimization to solving stochastic integral differential equation are used to lower learning (statistical, approximation, and optimization) errors.

### 3. diagnose [[CP-Posterior Approximator 🧠]]  
- generic (SBC) and data-specific (PSIS) method and compare their outcomes for different data and models.
