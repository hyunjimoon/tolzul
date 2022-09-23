a.k.a. Verification, Estimation on bounded range with $\epsilon$- optimality/feasibility (based on weak optimization = weak separation)

### Introducing CAT, reliability verification probablistic programming language
#operator, #hiearchize #regression 
- what: computationally efficient reliability verification of hierarchical model inference

- how: operator-based probabilistic programming language (PPL [[0. Introduction]])

- why: simulation is a weak solution of equations which generated reality and "what" above is needed to verify the closeness of simulation and reality. With "online" flavor added to simulation for digital twins as [this](https://www.ibm.com/topics/what-is-a-digital-twin) IBM report shows, computational efficiency is the key for CAT. By weak solution, I mean just as SDE's weak solution is constructed on a new setting (probability space, sigma algebra, measure, and filtration) and weakly equal to the strong solution, twin is a newly constructed object that is weakly equal to reality. With this view, CAT's main job in catching RAT (:= generative regression modeling languages) becomes searching for counterexamples i.e. a member of determining class $\phi$ breaching the (in)equality. Digitizing this falsifying logic is its aim. An example is finding an counterexample for inequality using a increasing function $\delta_{1} \in \phi$ (determining class for $\geq_{st}$, and n = 2. $\frac{1}{n} \sum_{l=1}^{n} X_{i} \geq_{st} \frac{1}{n+1} \sum_{i=1}^{n+1} X_{i}$  (further check needed!)


Consistency Ability Test, Consistency Analyzing Test, Calibrate and Test are current candidates for the name CAT. Filtering models that are [Accurate, yet inconsistent](https://arxiv.org/pdf/2108.06665.pdf) is CAT's goal based on their potential danger. 

List of verification-type approaches are:
- [Abstract Interpretation in a Nutshell](https://www.di.ens.fr/~cousot/AI/IntroAbsInt.html)
- [An importance sampling approach for reliable and efficient inference in Bayesian ordinary differential equation models](https://arxiv.org/pdf/2205.09059.pdf) 
> "validate the efficiency and reliability of our workflow in experiments using simulated and real data, and different ODE solvers"
- [Detecting Model Misspecification in Amortized Bayesian Inference with Neural Networks](https://arxiv.org/pdf/2112.08866.pd)