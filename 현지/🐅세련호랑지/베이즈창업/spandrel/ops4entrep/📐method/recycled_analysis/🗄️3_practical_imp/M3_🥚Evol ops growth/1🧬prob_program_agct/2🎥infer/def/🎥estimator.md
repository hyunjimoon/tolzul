a.k.a. Inference algorithms

Learning algorithms are rooted from largely five origins (neuroscience, evolutional biology, logic/philosophy, statistics, psychology) each of which has its own posterior approximation (gradient descent, genetic algorithm, decision tree, Bayesian inference, kernel machine) and evaluation target (squared error, fitness, posterior probability, margin  )) according to  [[5 Merging Algorithm Tribes]] are being merged into master algorithm. They merge to create a master equation. 

| approximation composition and error          | Connectionist                    | Evolutionist         | Bayesian                | Analogizer      | symbolist         |
| -------------------------------------------- | -------------------------------- | -------------------- | ----------------------- | --------------- | ----------------- |
| Origin                                       | neuroscience                     | evolutionary biology | statistics              | psychology      | philosophy        |
| [[🏭def(generate)]], approximation error         | neural network                   | genetic programming  | probabilistic inference | kernel machines | inverse deduction |
| Evalutation [[🌲inf(gen)]]), statistical error | squared error                    | fitness              | posterior prob.         | accuracy        |                   |
| [[🎥estimator]], optimization error          | gradient descent,backpropagation | particle filtering   | MCMC                    |                 |                   |

Literature on customized sampling kernel is booming with automized framework such as [Gen](https://www.gen.dev/) (an open-source stack for generative modeling and probabilistic inference) which provides customizable kernel functions. 

[[def(SBC)🌀]] tests the combination of [[def(Prior)]], [[def(generator)🌀]], [[🌀discriminator]], [[def(PosteriorApx)]] but I personally wish to put emphasis on [[def(Prior)]] and [[def(PosteriorApx)]]. This is because there is no clear way to systemize/automate and therefore need much research. For instance, the  use of customized sampling kernel designed using the more automated frameworks like Gen can be justified using SBC and compare with Posteriordb's model answer.
- Posteriordb's [reference posteior](https://github.com/stan-dev/posteriordb#what-is-posteriordb), sample-type posterior inference
- SBC library's two vignettes  
	- [Implementing a new backend (algorithm) + frequentist approximations](https://hyunjimoon.github.io/SBC/articles/implementing_backends.html)  
	- [SBC for ADVI and optimizing in Stan (+HMMs)](https://hyunjimoon.github.io/SBC/articles/computational_algorithm1.html)

- our quantity of interest in our hand; combined effects of [[def(generator)🏭]] and inference algorithms such as below which Domingos [introduces](https://en.wikipedia.org/wiki/The_Master_Algorithm) as five origins of learning algorithms 

$$
\begin{array}{lll}
\text { Tribe } & \text { Origins } & \text { Master Algorithm } \\
\text { Symbolists } & \text { Logic, philosophy } & \text { Inverse deduction } \\
\text { Connectionists } & \text { Neuroscience } & \text { Backpropagation } \\
\text { Evolutionaries } & \text { Evolutionary biology } & \text { Genetic programming } \\
\text { Bayesians } & \text { Statistics } & \text { Probabilistic inference } \\
\text { Analogizers } & \text { Psychology } & \text { Kernel machines }
\end{array}
$$





So How Do Computers Discover New Knowledge?
1. Fill in gaps in existing knowledge
2. Emulate the brain
3. Simulate evolution
4. Systematically reduce uncertainty
5. Notice similarities between old and new

Representation
- Probabilistic logic (e.g., Markov logic networks)
- Weighted formulas $\rightarrow$ Distribution over states
Evaluation
- Posterior probability
- User-defined objective function
Optimization
- Formula discovery: Genetic programming
- Weight learning: Backpropagation


- (weapons): connectionist (neural network), evolutionist (genetic algorithm), Bayesian (Bayes rule), symbolist (decision tree), analogizers (kernel machine)) which are converging.
- summary from  [[Moon17_Domingos15_MasterAlg.pdf]]  
Here's the updated table with eight columns, including the new "Reference" column with three papers for each tribe:

| Tribe          | Representation   | Evaluation            | Optimization             | Origins              | Problem               | Solution                | Scholars                                        | [[alg(master)_ref]]                                               |
| -------------- | ---------------- | --------------------- | ------------------------ | -------------------- | --------------------- | ----------------------- | ----------------------------------------------- | ----------------------------------------------------------------- |
| Symbolists     | Logic            | Accuracy              | Inverse Deduction        | Logic, philosophy    | Knowledge composition | Inverse deduction       | Tom Mitchell; Steve Muggleton; Ross Quinlan     | mitchell1997machine; muggleton1991inductive; quinlan1986induction |
| Connectionists | Neural Networks  | Squared Error         | Gradient Descent         | Neuroscience         | Credit assignment     | Backpropagation         | Yann LeCun; Geoffrey Hinton; Yoshua Bengio      | lecun1998gradient; hinton2006fast; bengio2009learning             |
| Evolutionaries | Genetic Programs | Fitness               | Genetic Search           | Evolutionary biology | Structure discovery   | Genetic programming     | John Koza; John Holland; Hod Lipson             | koza1992genetic; holland1992adaptation; schmidt2009distilling     |
| Bayesians      | Graphical Models | Posterior Probability | Probabilistic Inference  | Statistics           | Uncertainty           | Probabilistic inference | David Heckerman; Judea Pearl; Michael Jordan    | heckerman1998tutorial; pearl2009causality; jordan1999introduction |
| Analogizers    | Support Vectors  | Margin                | Constrained Optimization | Psychology           | Similarity            | Kernel machines         | Peter Hart; Vladimir Vapnik; Douglas Hofstadter | hart1968condensed; vapnik2013nature; hofstadter1979godel          |

| Intersection              | Confusing Instances                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Behavioral x Bayesian     | 1. Ries (2011). The lean startup - While it emphasizes experimentation (Bayesian), it also focuses on entrepreneurial decision-making under uncertainty (Behavioral).<br>2. Eisenmann et al. (2012). Hypothesis-driven entrepreneurship: The lean startup - Similar to Ries (2011), it combines experimental approaches with entrepreneurial cognition.                                                                                                                                                                                    |
| Bayesian x Evolutionary   | 1. Kerr et al. (2014). Entrepreneurship as experimentation - While primarily focused on learning through experiments (Bayesian), it also considers how firms adapt over time (Evolutionary).<br>2. Manso (2016). Experimentation and the Returns to Entrepreneurship - Discusses both experimental learning and how it affects firm survival and growth over time.<br>3. Nanda & Rhodes-Kropf (2016). Financing entrepreneurial experimentation - Combines elements of experimental learning with how financing affects startup evolution. |
| Evolutionary x Behavioral | 1. Lazear (2004). Balanced skills and entrepreneurship - Discusses both individual characteristics (Behavioral) and how they adapt to entrepreneurial roles (Evolutionary).<br>2. Lumpkin & Dess (1996). Clarifying the entrepreneurial orientation construct and linking it to performance - Combines elements of entrepreneurial behavior with how it affects firm performance over time.                                                                                                                                                |
