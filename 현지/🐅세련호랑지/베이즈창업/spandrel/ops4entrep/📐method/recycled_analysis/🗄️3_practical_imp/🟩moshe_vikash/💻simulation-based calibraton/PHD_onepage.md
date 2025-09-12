
#phd 
**Simulation measures for simplified system design**

goal
1. Define optimality what?
2. Decide optimality test? YesNo [[3 opt version]]
3. Decrease to optimality

application
- digital twin and abstraction of model components
2. Update to optimality
Methodologies (A) criticized for its possibility to be locked in local optimal can be used as a test stone for optimality verification test i.e. A is used for 
- relative: 
	- defensive: min overall risk, prevent cascade (electricity)
	- active: auction, better than others
- objective: 
	- geometry- dim reduction
classify (objective geometry, goal, ) then optimize
mds solution: metric, diagnosis, system

classify the system: #surrogate testing

- #system summary with #preference embedded under  detailed balance 
- stochastic system: more than one members that behaves randomly

| name      | system  | member    | goal          | how.           | interact |
| --------- | ------- | --------- | ------------- | -------------- | -------- |
| HMC       | post.   | param     | higher H(p,q) | lpdf_grad      | no       |
| sync      |         |           | higher S      | coupling ODE   | yes      |
| cascade   |         |           |               |                | yes      |
| entangle  | quantum |           |               | joint/marginal | yes      |
| immune    |         |           |               |                |          |
| mechanism |         | human     |               |                | yes      |
| orbital   |         | electron  |               |                | yes      |
| coupling  |         | sto.proc  |               |                | yes      |
| Diff.Eq   |         | sol.cand. |               |                |          |
| military  |         |           |               |                | sum      | 

## system classification on interaction and goal
### interaction yes (a.k.a interacting particle systems)
| name      | system  | member    | goal          | how.           | interact |
| --------- | ------- | --------- | ------------- | -------------- | -------- |
| HMC       | post.   | param     | higher H(p,q) | lpdf_grad      | no       |
| sync      |         |           | higher S      | coupling ODE   | yes      |
| cascade   |         |           |               |                | yes      |
| entangle  | quantum |           |               | joint/marginal | yes      |
| immune    |         |           |               |                |          |
| mechanism |         | human     |               |                | yes      |
| orbital   |         | electron  |               |                | yes      |
| coupling  |         | sto.proc  |               |                | yes      |
| Diff.Eq   |         | sol.cand. |               |                |          |
| military  |         |           |               |                | sum      | 
cause for interaction types are:
- pure physical: sync-ode, maximum entropy
- relative goal
### interaction no
fixed goal
modeler ->model network
### goal: absolute and relative
parallel chain
communicating chains
- relative 
variable goal
modeler <-> model network
- models competing to be selected
- model selection is the same as portfolio selection (trade-off of variability)
- logN: the number of bins = categorizing the models into subcategory

rel
1. given a number of models and the fixed goal
2. stacking 

variable goal
# Metric
- Metric accouting for the difference between system and individual [[garudiyengar|garud]]
- sample-based #gq easy with no closed form requirement
- #gq computing machine #verification 
- #gq computing machines #modelavg #validate 

system outcome = f(member outcome)
f(member outcome) = pure member + interaction 
do not stay at 1s but at weight average of 1s and 2s orbital

coupling: 
- lifting in space
- sync: react to the same stimulus while interacting between (interaction term)
converge: lifting in space

maximum entropy given constraint - goal is relative vs absolute


	- lpdf of prior and likehood

relation btw natural gradient and coupling?


# characterizing optimal strategy/solution
 
In a flat area, 
### Thm.1. Coupling
if q* is optimal, i.e. $q* = \underset{q}argmax H(p,q)$
meeting time between two process with initial point $x_{q*}, y_{q*} \sim N(q*, \epsilon$ is shorter than any other q

- cvar is a #coherent risk measure
- #mrt rewrite CVaR objective as max problem for adversary who controls the quantile process Q tagainst the decision maker -> continuous-time stochastic game
- 
- sup inf L(x, lambda) = inf sup L(x, lambda) 

### Thm.2. Natural gradient ascent
when all components are orthogonal, component wise descent is optimal and not prone to lock in the local

### Thm.3. Lifting and perspective function
$p -> \phi^{-1}(p) -> p$ tangent bundle
![[inf_proj.png]]

### Thm.4. Iteration
개별 정체성을 주는 idx를 찾아서 복제하면 됨. 현지는 한국에 사는 여자 대학생 $f(a1...an) -> w_i * f(Ea_i, ..)$ 이게 회귀계수지. 
# 
- #q augmentation along running cost and quantile value whereas I suggest augmentation along time. Projecting i.e. substituting each component as its expectation value is equivalent to natural gradient or lifting along the time axis then compose with perspective function
>  $f(\theta_1, \theta_2, \theta_3)$
> 1) lifting $f(\theta_1, \theta_2, \theta_3, t)$
> 2) perspective $f(\theta_1, \theta_2, \theta_3, t)$



#coupling #verification
## Using coupling to test whether x is optimal or a solution
- given a state x, and an objective function H(x) (e.g. energy function; H(p,q) = V(q) + K(p)



#chos

1.  풀려는걸 방정식화 해 원하는걸 방정식해로 기술
2.  해 있는 상황가정 후 해당 상황의 성질 관찰
    

metic <-> laplacian (heat equation의 해가 rw = diffusion operator)
