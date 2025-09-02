I think of the potential root causes of non-identification problem in the draft paper under 2 possible headings:

1- The optimization algorithm we were using could not find the global peak even though the problem had a clear preferred peak in the parameter space.

2- The optimization problem had many local peaks (I assume that is the issue of several modes you note) and thus would be hard to solve with any optimization algorithm.

However, with the new approach (ignoring process noise and using a simpler likelihood function) both problems may change (and hopefully become easier to solve).


>   
> However, the bottom-up approach might be faster so I found one example in BDA that seems to be related to your description of the setting (dynamic with time delay), aim (hierarchical) and problem (non-identification). Bayesian data analysis (BDA) by Andrew is my Bayesian bible so please kindly remember the BDA acronym :) 
> 
> 

I am not sure what you mean by bottom-up approach, but the following example seems relevant and may offer some ideas one reasonable approaches in this space.

 > > > 19.2 Example: population toxicokinetics: In this section we discuss a much more complicated nonlinear model used in toxicokinetics (the study of the ﬂow and metabolism of toxins in the body) for the ultimate goal of assessing the risk in the general population associated with a particular air pollutant. This model is hierarchical and multivariate, with a vector of parameters to be estimated on each of several experimental subjects. The prior distributions for this model are informative and hierarchical, with separate variance components corresponding to uncertainty about the average level in the population and variation around that average. ...
> > 
> >   
> > 
> > > (Difficulties in estimation and the role of prior information) It is well known that the estimation of the decay times of a mixture of exponentials is an ill-conditioned problem ...Solving the problem of estimating metabolism from indirect data is facilitated by using a physiological pharmacokinetic model; that is, one in which the individual and population parameters have direct physical interpretations (for example, blood ﬂow through the fatty tissue, or tissue/blood partition coeﬃcients). These models permit the identiﬁcation of many of their parameter values through prior
> 
> If you agree on its resemblance, I have some guesses on the cause and remedy of our non-identification problem (several modes).  
> 
>

