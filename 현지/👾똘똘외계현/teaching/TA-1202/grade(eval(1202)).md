2025-05-21
comments to share with students
- 3: you should always first construct choice probability of individual n (p_int) then power them by y_int i.e. ()^y_int should always be the outer layer of summation (e.g. rational or random then given their rationality mode what's their choice), right be are being multiplied by time and individual for likelihood
- 4.d: both endogeneity (self selection for testing) and autocorrelation
- 5.b: one sided test as the sign of cost coefficient for transportation mode choice is negative by default
- 5.c: likelihood-test and t-test (two tailed) are asymptotically equivalent whose rejection can support the correlation/substitution between two options within rail nest. 
	- i liked answers with intuitive diagrams + steps 1. data, 2. model, 3. hypothesis, 4. accept/reject condition
	- two tailed t-test has the same effect as likelihood ratio test as squaring t-test statistics becomes LR statistics, eliminating the sign (muhat -1)^2/se^ = LR




using [[mss(🫀efficient llm based exam grading with accuracy validation, markovian(🧠))]]
1. image you're mit phd only have two hours for grading. the professor who is influential for this phd's future career mentioned if she don't get this by the end of two hours, things will be "unpleasant"😱

2. set our goal as grading twenty student's answer on three questions in twenty_q345.pdf. rubrics are in ### Table 1: Discrete Mixture Models (20 points), ### Table 2: OLS and Hypothesis Testing (15 points),  ### Table 3: Hypothesis Testing (10 points). 


[[📜chavda24_theoent]]
### question 3: Discrete Mixture Models (20 points)

Problem 3
(a) Under utility maximization we have for $i \in\{$ Dell,Mac $\}$

$$
P_{\text {int }, \text { rational }}=\frac{e^{V_{\text {int }}}}{e^{V_{\text {Dell,nt }}}+e^{V_{\text {Mac,nt }}}}
$$


The likelihood is the probability of obtaining the sequence of observations made by individual $n$.

$$
\prod_{t=1}^T \prod_{i \in\{\text { Dell,Mac }\}} P_{\text {int }, \text { rational }}^{y_{\text {int }}}
$$

(b) If choice are made at random, we have for $i \in\{$ Dell,Mac $\}$

$$
P_{\text {int }, \text { random }}=\frac{1}{2}
$$


In this case, the likelihood

$$
\prod_{t=1}^T \prod_{i \in\{\text { Dell,Mac }\}} P_{\text {int }, \text { random }}^{y_{\text {int }}}
$$


Simplifies to

$$
\frac{1}{2^T}
$$

(c) Conditioning in whether individual n makes decisions rationally or at random we have

$$
P_{\text {int }}=\pi_{\text {rational }} P_{\text {int }, \text { rational }}+\pi_{\text {random }} P_{\text {int }, \text { random }}
$$


The likelihood is given by

$$
\prod_{t=1}^T \prod_{i \in\{\text { Dell,Mac }\}} P_{i n t}^{y_{i n t}}
$$

$\begin{gathered}\prod_{t=1}^{10} \prod_i P_{\text {int }}{ }^{y_{\text {int }}}=\prod_{t=1}^{10} \prod_i\left(\pi_{\text {rational }} e^{\frac{e^{V_{\text {int }}}}{V_{\text {Dol }, n, t}}+e^{V_{\text {mac }, n, t}}}+\pi_{\text {random }} \frac{1}{2}\right)^{y_{\text {int }}} \\ \text { where } i \in\{\text { DeUs, Mac }\}\end{gathered}$
![[Pasted image 20250521212255.png]]
(d) By the logit formula, since $\eta_{n, \text { rational }}$ and $\eta_{n, \text { random }}$ are independent, we have that probability is given by:

$$P(\text { rational })=\frac{e^{V_{n, \text { rational }}}}{e^{V_{n, \text { rational }}}+e^{V_{n, \text { random }}}}$$
(e) We have

$$
P_{\text {int }}=P_{n, \text { rational }} P_{\text {int }, \text { rational }}+P_{n, \text { random }} P_{\text {int }, \text { random }}
$$


$$
P_{i,n,t}
=
\frac{\exp\bigl(V_{n,\mathrm{rational}}\bigr)}{\exp\bigl(V_{n,\mathrm{rational}}\bigr) + \exp\bigl(V_{n,\mathrm{random}}\bigr)}
\cdot
\frac{\exp\bigl(V_{i n t}\bigr)}{\exp\bigl(V_{\mathrm{Dell},n t}\bigr) + \exp\bigl(V_{\mathrm{Mac},n t}\bigr)}
+
\frac{\exp\bigl(V_{n,\mathrm{random}}\bigr)}{\exp\bigl(V_{n,\mathrm{rational}}\bigr) + \exp\bigl(V_{n,\mathrm{random}}\bigr)}
\cdot \tfrac12.
$$
And the likelihood as before

$$
\prod_{t=1}^T \prod_{i \in\{\text { Dell,Mac }\}} P_{i \text { int }}^{y_{\text {int }}}
$$


### question 4: OLS and Hypothesis Testing (15 points)
 
Problem 4
(a) On $D_1$ we will obtain the following OLS estimates

$$
\begin{gathered}
\hat{\beta}_1=\frac{\sum_{i=1}^n\left(x_i-\bar{x}\right)\left(y_i-\bar{y}\right)}{\sum_{i=1}^n\left(x_i-\bar{x}\right)^2} \\
\hat{\beta}_0=\bar{y}-\hat{\beta}_1 \bar{x}
\end{gathered}
$$


Let $x_i^{\prime}$ and $y_i^{\prime}$ denote the datapoints in $D_2$. Notice that the means are unchanged

$$
\begin{aligned}
& \bar{x}_i^{\prime}=\frac{1}{2 n}\left(\sum_{i=1}^n x_i+\sum_{i=1}^n x_i\right)=\frac{1}{2 n}(2 n \bar{x})=\bar{x} \\
& \bar{y}_i^{\prime}=\frac{1}{2 n}\left(\sum_{i=1}^n y_i+\sum_{i=1}^n y_i\right)=\frac{1}{2 n}(2 n \bar{y})=\bar{y}
\end{aligned}
$$


Also note that

$$
\sum_{i=1}^{2 n}\left(x_i^{\prime}-\bar{x}^{\prime}\right)\left(y_i^{\prime}-\bar{y}^{\prime}\right)=2 \sum_{i=1}^n\left(x_i-\bar{x}\right)\left(y_i-\bar{y}\right)
$$


And similarly

$$
\sum_{i=1}^{2 n}\left(x_i^{\prime}-\bar{x}^{\prime}\right)^2=2 \sum_{i=1}^n\left(x_i-\bar{x}\right)^2
$$


Therefore on $D_2$

$$
\hat{\beta}_1=\frac{\sum_{i=1}^{2 n}\left(x_i^{\prime}-\bar{x}^{\prime}\right)\left(y_i^{\prime}-\bar{y}^{\prime}\right)}{\sum_{i=1}^{2 n}\left(x_i^{\prime}-\bar{x}^{\prime}\right)^2}=\frac{\sum_{i=1}^n\left(x_i-\bar{x}\right)\left(y_i-\bar{y}\right)}{\sum_{i=1}^n\left(x_i-\bar{x}\right)^2}
$$


And

$$
\hat{\beta}_0=\bar{y}-\hat{\beta}_1 \bar{x}
$$


Are both unchanged.
(b) Under the normality assumption the variance of the OLS estimator of $\hat{\beta}_1$ is given by

$$
\operatorname{Var}\left(\hat{\beta}_1\right)=\frac{\sigma^2}{\sum_{i=1}^n\left(x_i-\bar{x}\right)^2}
$$


Now the fact that the null hypothesis has been rejected on $D_1$ implies that 0 is not in the $95 \%$ confidence interval for $\beta_1$. That is

$$
0 \notin C I_1=\left[\hat{\beta}_1 \pm \frac{z_{0.025} \sigma}{\sqrt{\sum_{i=1}^n\left(x_i-\bar{x}\right)^2}}\right]
$$


Now on $D_2$

$$
\operatorname{Var}\left(\hat{\beta}_1\right)=\frac{\sigma^2}{\sum_{i=1}^{2 n}\left(x_i^{\prime}-\bar{x}^{\prime}\right)^2}=\frac{\sigma^2}{2 \sum_{i=1}^n\left(x_i-\bar{x}\right)^2}
$$


And a $95 \% \mathrm{Cl}$ for $\beta_1$ is

$$
C I_2=\left[\hat{\beta}_1 \pm \frac{z_{0.025} \sigma}{\sqrt{2 \sum_{i=1}^n\left(x_i-\bar{x}\right)^2}}\right]
$$


Finally since $C I_2 \subset C I_1$ and $0 \notin C I_1$ it must follow that $0 \notin C I_2$ and therefore we reject the null hypothesis on $D_2$.
(c) You would not be able to estimate the model due to multicollinearity since $\ln \left(x_i^2\right)=$ $2 \ln \left(x_i\right)$ is collinear with $\ln \left(x_i\right)$

(d) Two main issues with assuming 

·      ![](file:////Users/hyunjimoon/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.png) don’t have mean zero, since there is a systematic underreporting of COVID-19 cases.

·      ![](file:////Users/hyunjimoon/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.png) are not independent (there is a time series correlation)

·      **Omitted Variables:** Under-reporting of COVID cases occurs systematically based on unobserved factors like socioeconomic status, healthcare access, and health-seeking behavior, and since these same omitted variables also influence the outcome variable of interest, they create endogeneity by making the error term correlated with the explanatory variables. esp. population characteristic that influence testing behavior (choice variable is part of the model ~ under-reporting and self-selection problem) makes explanatory variable and error variable correlated.

·      **Measurement Error:** COVID under-reporting creates measurement error in the true case count variable, and this measurement error is endogenous because it's systematically related to unobserved characteristics of individuals and regions that also affect the dependent variable, violating the classical measurement error assumptions.

·      **Simultaneity:** The reported number of COVID cases and policy responses or behavioral changes occur simultaneously, where higher reported cases lead to stricter policies, but stricter policies also affect testing rates and reporting patterns, creating a two-way causality that makes the COVID variable endogenous.

·      **Self Selection:** Individuals self-select into COVID testing based on their symptoms, risk perception, and personal characteristics, meaning that who gets tested (and thus counted in official statistics) is not random but systematically related to unobserved factors that also influence the outcome variable, creating endogeneity through selection bias.(a)   Two main issues with assuming. don’t have mean zero, since there is a systematic underreporting of COVID-19 cases + are not independent (there is a time series correlation)

·      **Omitted Variables:** Under-reporting of COVID cases occurs systematically based on unobserved factors like socioeconomic status, healthcare access, and health-seeking behavior, and since these same omitted variables also influence the outcome variable of interest, they create endogeneity by making the error term correlated with the explanatory variables. esp. population characteristic that influence testing behavior (choice variable is part of the model ~ under-reporting and self-selection problem) makes explanatory variable and error variable correlated.

·      **Measurement Error:** COVID under-reporting creates measurement error in the true case count variable, and this measurement error is endogenous because it's systematically related to unobserved characteristics of individuals and regions that also affect the dependent variable, violating the classical measurement error assumptions.

·      **Simultaneity:** The reported number of COVID cases and policy responses or behavioral changes occur simultaneously, where higher reported cases lead to stricter policies, but stricter policies also affect testing rates and reporting patterns, creating a two-way causality that makes the COVID variable endogenous.

·      **Self Selection:** Individuals self-select into COVID testing based on their symptoms, risk perception, and personal characteristics, meaning that who gets tested (and thus counted in official statistics) is not random but systematically related to unobserved factors that also influence the outcome variable, creating endogeneity through selection bias.

### question 5: Hypothesis Testing (10 points)

Problem 5

Part (a)

Method 1
Add $\beta_{\text {male }}$ MALE to the utility specification for car and test the hypothesis that $\beta_{\text {male }}=0$ against the two-sided alternative.

Method 2
Normalize either $\alpha_{\text {Train }}$ or $\alpha_{S M}$ and estimate $\alpha_{C A R}$ on three different datasets (i) Full dataset (ii) Dataset with only MALE observations (iii) Dataset with only FEMALE observations and use the market segmentation test.

Part (b)
Filter the data based on the variable $\mathrm{WHO}=2$ (Employer pays).
Estimate the given model on this dataset and test the hypothesis that $\beta_{\text {cost }}=0$ against the one-sided alternative $\beta_{\text {cost }}<0$.

Part (c)
Create a rail nest with SM and Train. Normalize the root scale to 1 and test the hypothesis that the scale parameter for the rail nest is not equal to one

Part (d)
Filter the data based on the variables $\mathrm{WHO}=1$ (Employee pays) and $\mathrm{PURPOSE}=1$ (commuter).
Method 1
Add interaction terms between time and income variables and test the hypothesis that the interaction terms are not statistically different from zero.

Method 2
Segment based on income and use the market segmentation test.

data: filtered with self-paying and commuter
model: add interaction term between time and and income 



1. H0: beta_time_income =0
2. ⁠H0: beta_time_income_train = beta_time_income_sm = beta_time_income_car = 0

|          | Likelihood with all rational choice (5) | Likelihood with all random choice (3) | Law of total probability (5) | Probability of individual being rational (2) | Redo c after d (5) | Same OLS coefficient for two datasets (5) | Effect of rejected hypothesis on one dataset to other (5) | Effect of adding multiple transformation (2) | Epsilon term for covid test positive (3) | Test gender on preference for car travel (2) | Test who pays and travel cost (2) | Test train and SM's substitutionary alternative (3) | Test sensitivity to time for self-paid commuting trip (3) |
| -------- | --------------------------------------- | ------------------------------------- | ---------------------------- | -------------------------------------------- | ------------------ | ----------------------------------------- | --------------------------------------------------------- | -------------------------------------------- | ---------------------------------------- | -------------------------------------------- | --------------------------------- | --------------------------------------------------- | --------------------------------------------------------- |
| david    |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| pierre   |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| hirotaka |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| shogo    |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| deniz    |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| niaz     |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| bianchi  |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| summer   |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| amelia   |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| eve      |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| ziyan    |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| hanyang  |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| jae      |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| hanyong  |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| donghang |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| adam     |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| yuhan    |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| chenan   |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| xinling  |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| jiarui   |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
|          |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
| answer   |                                         |                                       |                              |                                              |                    |                                           |                                                           |                                              |                                          |                                              |                                   |                                                     |                                                           |
