[[🌙amoon()/⚡️generate(tolzul)/management/project proposal]]
## Course Summary

This course explores computational approaches to understanding human cognition, with a focus on Bayesian inference, probabilistic programming, and rational models of cognition. Topics include inductive learning, concept formation, language of thought, graphical models, and applications to everyday reasoning.

## Reading List

links are for marginenote (with  [[🌏world(amoon)]] syntax)

| Topic                                                                                    | Year | Author                | Link                                                                                                                                                            | takeaway |
| ---------------------------------------------------------------------------------------- | ---- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Week 2: Foundations of Inductive Learning, Bayesian Inference, Bayesian Concept Learning | 1982 | Marr                  | [Vision, Chapter 1](marginnote_link)                                                                                                                            |          |
|                                                                                          | 2000 | Tenenbaum             | [Bayesian modeling of human concept learning]()                                                                                                                 |          |
|                                                                                          | 2001 | Tenenbaum             | [Rules and similarity in concept learning](marginnote_link)                                                                                                     |          |
| Week 3: Human Cognition as Rational Statistical Inference w/ Bayes, Number Game          | 2006 | Sivia                 | [Bayesian tutorial](marginnote_link)                                                                                                                            |          |
|                                                                                          | 2010 | Russell & Norvig      | [AIMA chpt. 13 Uncertainty](marginnote_link)                                                                                                                    |          |
|                                                                                          | 2014 | Sanborn               | [Bayesian brains](marginnote_link)                                                                                                                              |          |
|                                                                                          | 1974 | Tversky & Kahneman    | [Heuristics and biases](marginnote_link)                                                                                                                        |          |
|                                                                                          | -    | Mitchell              | [MitchellCh6 - Bayesian learning](marginnote_link)                                                                                                              |          |
|                                                                                          | 2021 | Thaker et al.         | [Learning symbolic concepts](marginnote_link)                                                                                                                   |          |
|                                                                                          | 2007 | Xu & Tenenbaum        | [Word Learning](marginnote_link)                                                                                                                                |          |
| Week 4: Scaling to Structured Hypothesis Spaces, Intro to Probabilistic Programming      | 2016 | Piantadosi et al.     | [The logical primitives of thought](marginnote_link)                                                                                                            |          |
|                                                                                          |      |                       |                                                                                                                                                                 |          |
| Week 5: Everyday Bayesian Perception and Cognition, Intro to Language of Thought         | 2010 | Russell & Norvig      | [AIMA Ch.14 Bayesian networks](marginnote_link)                                                                                                                 |          |
|                                                                                          | 2008 | Chater & Oaksford     | [Rational analysis](marginnote_link)                                                                                                                            |          |
|                                                                                          | 2006 | Griffiths & Tenenbaum | [Optimal Predictions in Everyday Cognition](marginnote_link)                                                                                                    |          |
|                                                                                          | 2023 | Ellis                 | [Human-like Few-Shot Learning via Bayesian Reasoning over Natural Language](marginnote_link)                                                                    |          |
| Week 6: Graphical Models and Probabilistic Programming                                   |      |                       |                                                                                                                                                                 |          |
|                                                                                          |      |                       |                                                                                                                                                                 |          |
| Week 7: Explaining Away, Neural Networks for Inference                                   |      |                       |                                                                                                                                                                 |          |
|                                                                                          |      |                       |                                                                                                                                                                 |          |
| W8: Word to World model, intro to MCMC                                                   |      |                       | <br>Wong et al. (2023) From Word Models to World Models.pdf                                                                                                     |          |
|                                                                                          |      |                       | [Gershman et al. - Computational Rationality.pdf](https://canvas.mit.edu/courses/28357/modules/items/1176311 "Gershman et al. - Computational Rationality.pdf") |          |
|                                                                                          |      |                       |                                                                                                                                                                 |          |


## Course Structure

1. Foundations of inductive learning and Bayesian inference
2. Human cognition as rational statistical inference
3. Structured hypothesis spaces and probabilistic programming
4. Everyday Bayesian perception and cognition
5. Language of thought and symbolic concepts
6. Graphical models and advanced probabilistic programming

## Tools and Techniques

- Probability theory and Bayesian statistics
- WebPPL (probabilistic programming language)
- Computational modeling of cognitive processes
- Analysis of human behavioral data

## Applications

- Concept learning and categorization
- Language acquisition and processing
- Perceptual inference and decision-making
- Reasoning under uncertainty
- Cognitive development and learning

----
2024-10-24
- mcmc as metaphor and cognitive theory 
- calculate stationary dist. from transition matrix (eigen vacecture; convergence rate - how long it takes to reach); posterior dist is stationary (state as latent variable or hypothesis; approximate p(h|D) interesting intuitive easy to set up local dynamics)
- when metropolis hastings? p(data|h) and p(h), but 
- suppose wew can compute likelihood and prior but not the sum over h needed for posterior
- relation btw sampling and density evaluation  (dan roy, cameron)
- T(h_t+1|h_t) is function of proposal (inner loop) and acceptance distribution (outerloop) - outerloop is tabular ; moving around (latent variables; hypothesis as "choices of prog" then "trace of the program to evaluate any one sample program") - don't accept every proposal
- new hypothesis explains the data better, we're accepting it
- proposal is asymmetric (esp. when hyopthesis is more structured)
- two classes of complicated vs simple hypothesis ()
- detailed balance: have transtiontion kernel with pi_i (if for all hypothesis ); overall time (all the hypothesis to the other), twice the prob. on state i than state j, whatever acceptance (rate lambda); the way webppl initialize is empirical bayes "initialization right, or just to initialize with some with basically a program trace that does evaluate the data or with some reasonable probability."
- burnin: doesn't matter where you start, once the two chains cross from different initial points
-
- mixing: luckily unlucky (go down alley) then luckily lucky (go up in a lower mountain)


----
2024-10-30
ideas of mcmc
generate data (fits avg of data)
lots of samples and choose median for the answer (no convergence going on within one person's head)
don't wait like statistian; across different settings -> collect ppl's -> posterior predictive dist.
posterior from one expression?
graded behavior as symbolic process