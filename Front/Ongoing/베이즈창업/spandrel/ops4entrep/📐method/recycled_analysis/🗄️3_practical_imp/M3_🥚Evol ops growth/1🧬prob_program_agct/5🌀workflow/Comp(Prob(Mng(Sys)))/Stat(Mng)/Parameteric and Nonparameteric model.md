Estimated ones vs assumed ones from domain knowledge
- Stella has four types: instantaneous C&E, Stock, flow, calculated variables, 
- Vensim has : Constant, auxilary variable, flow, stock

How are these mapped in pysd simulation? Clamping `params` 

> Let's define "works well enough". Assuming hierarchical modeling and its estimation of eq.19 and fig.2 from your good jobs paper is your goal, I listed decisions on your A and C. We could iterate through them.
> 
> a - parametric vs nonparametric model - (if parametric) likelihood of generalized linear model  - (if nonparametric) spline, gaussian process, etc 
> 
> b. prior
>   

I am not sure about what you mean by a and b items you noted as part of defining "works well enough". My definition is: an estimation method that works acceptably on synthetic data generated from our model including reasonable process noise values, following a method like SBC.