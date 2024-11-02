a. 
stndfnl $=\beta_0+\beta_1 \times$ atndrte $+\beta_2 \times$ frosh $+\beta_3 \times \operatorname{soph}+\epsilon$
student ability, motivation, personality, health may affect both attendance and score. 
running an regression returns $\beta_1$ = .008 (pvalue is smaller than .001)  which means one unit of attendance increase would lead to .008 unit increase of score which may not be true. 

you need to have a model of omitted variable to think (capturing some of the things non attendance) 


model of ommitted variable is wrong

correlated with ommitted variable (don't observe ability), sign the bias (under and overestimate)

but with endogeneity bias, 


b. $\hat{\beta_1}$ would be an overestimate due to omitted variables because the model incorrectly attributes the positive effects of these omitted variables (like student ability, study habits, motivation) entirely to attendance.

c. As proxy variables for student ability, add to the regression priGPA (prior cumulative GPA) and ACT (achievement test score). Now what is the estimated effect of atndrate? Discuss how the effect differs from that in part a.

when including $\beta_1$ =.0005 - coefficient dropped, absorbed (variance projected to attendance is absorbed to proxy variable)