# 1. Partial Equilibrium: Interventions in the Market for Cigarettes

$u_i(c,y) = c + \alpha_i log(y_i)$
each consumer has w endowment in numeraire, common across N consumers; $log(\alpha_i) \sim N(\mu, \sigma^2)$ $c_j(q) = (1+\beta_j) q^2$, $\beta_i \sim U[0, \bar{\beta}]$ technology parameter of firm describing efficiency

## (a) individual consumer i's utility max problem
$max \; c + \alpha_i log(y_i) + w_i \sigma \theta^i (px^Q - c)$ 
using MRS = relative price $y_i = \alpha_i /p$, 
$c = w_i- p x_i + \theta^i p x - c(x)$

## (b) aggregate demand $D_x(p)$
demand is p-linear and there are N consumers so N *$exp(\mu + \sigma^2)/ p$ 

SWITCHING TO HANDWRITING
![[Pasted image 20231114095825.png]]

# 2 welfare and class diff
## (a) equilibrium price and quantity supplied in the market for food.
consider both the demand and supply sides of the market to solve for the equilibrium price and quantity supplied in the market for food, we need to 

## (b)
### Demand Side

Given the utility function $u_i(c, x) = c + \alpha \sqrt{x}$, where \( c \) is the numeraire (with price normalized to 1) and \( x \) is the quantity of food, we can derive the demand function for food.

Since utility is quasilinear, the marginal utility of money (numeraire) is constant and equal to 1. The marginal utility of food is $\frac{\alpha}{2\sqrt{x}}$. In equilibrium, consumers equate the marginal utility per dollar spent on each good to its price. Therefore, for food, we have:

$\frac{\alpha}{2\sqrt{x}} = p$
$\sqrt{x} = \frac{\alpha}{2p}$
$x = \left( \frac{\alpha}{2p} \right)^2$

This is the individual demand function for food. Since there are \( N \) consumers, the total market demand \( Q_D \) for food is: $Q_D = N \left( \frac{\alpha}{2p} \right)^2$
### Supply Side

Each of the  J = $\frac{N}{2}$ factories has a cost function  $c_j(q) = q^2$. Since they supply competitively to the market, they set marginal cost equal to price. The marginal cost for a firm is \( 2q \), so in equilibrium: $2q = p, q = \frac{p}{2}$

This is the supply function for an individual firm. aggregated supply is $Q_S = J \cdot q = \frac{N}{2} \cdot \frac{p}{2} = \frac{Np}{4}$

Note we're multiplying $Q_D$ by N for aggregation whereas multiplying  $Q_S$ by N/2 for aggregation. Now we're solving market clearance condition i.e. $Q_D = Q_S$ $N (\alpha/2p)^2 = Np/4$ gives $p = \alpha^{2/3}$. Plugging it in to aggregated supply and demand, we get $Q_S = \frac{N \alpha^{2/3}}{4}$ = $Q_D$


## (b) revenue neutral transfer

consumer's utility: $c + \alpha \sqrt{x}$ = $(w-p \frac{\alpha^2}{4p^2}) + \alpha \sqrt{x}$ = $w - \alpha^{4/3}/4$ 
capitalist's utility: $c + \alpha \sqrt{x}$ = $w - \alpha^{4/3}/4 + \alpha^{4/3} + \alpha \sqrt{x}$ = $w + \alpha^{4/3}/2$ 

to make the two have the same utility (for rawlsian) capitalist should transfer 3/8$\alpha^{4/3}$ to workers. It's pareto optimal

## (c) Monopoly Price and Quantity

we first need to determine the monopoly price and quantity for the food market, and then we can address the Rawlsian social welfare maximization under this new market structure.
solving $\max _p J pq-J q^2$ we get $q=\frac{\alpha^2}{2 p^2}$
solving $\underset{p}{max} \;\alpha^2/2p - \alpha^4/4p^4$ gives $p = 2^{1/3}\alpha^{2/3}$

$max \; q(p) p - q(p)^2$ where $x=\alpha^2/ 4 p^2, q=\alpha^2/ 2 p^2$ (q = 2x as there are twice as much as consumers than producers)
worker:
$\begin{aligned} & (w-p \cdot x)+\alpha \sqrt{x} \\ & =w-\frac{\alpha^2}{4 p}+\frac{\alpha^2}{2 p}= w - \frac{\alpha^2}{4p} \end{aligned}$

capitalist: 
$\begin{aligned} & (w-p \cdot x + \pi)+\alpha \sqrt{x} \\ & =w-\frac{\alpha^2}{4 p}+\frac{\alpha^2}{2 p} - \frac{\alpha^4}{4 p^4} = w - \frac{\alpha^2}{4p} \end{aligned}$

hence the revenue neutral transfer should be $\frac{\alpha^2}{4p} -\frac{\alpha^2}{8p^4}$ which using $p = 2^{1/3} \alpha^{2/3}$ is $\frac{\alpha^{4 / 3}}{4 \cdot 2^{1 / 3}}-\frac{\alpha^{-2 / 3}}{8 \cdot 2^{4 / 3}}$. 


# 3. Tax Burden in Equilibrium
ad valorem tax of τ%, agg.demand is $A+ \alpha log(p)$, $log(q(p)) = B+ \beta log(p)$  price elas. for demand and supply
## (a) p*, q*
solve for p* $A+ \alpha log(p)$, $log(q(p)) = B+ \beta log(p)$
T% assessed at each purchase -> $p(1+\tau)$
$$
\begin{array}{ll}
\varepsilon_{x_i}=\log (x(p))=A+\alpha \log (p) & \alpha \leq 0-\varepsilon_\alpha \\
\varepsilon_{q i}=\log (q(p))=B+\beta \log (p) & B \geq 0-\varepsilon_s \\
\end{array}
$$
A) solve for $P^*$ and $Q$ *
solve for $p^{\star}$ :
$$
\begin{aligned}
& A+\alpha \log (p(1+r)=b+B \log (p) \\
& A-b=B \log (p)-\alpha \log (p(1+r)) \\
& \frac{A-b+\alpha \log (1+r)}{B-\alpha}=B \log (p)-\alpha \log (p) \\
& p *=\frac{A-b+\alpha \log (1+T)}{B-\alpha}
\end{aligned}
$$

Solve for q*:
$$
\begin{aligned}
& \log (q)=b+B \log \left[\frac{A-D+\alpha \log (1+T)}{B-\alpha}\right] \\
& q^*=\exp \left[b+B \log \left[\frac{A-D+\alpha \log (1+T)}{B-\alpha}\right]\right] \\
& =b+B \log (A-D+\alpha \log (1++))-B \log (B-\alpha) \\
& q^*=e^b\left(A-x+\alpha \log (1+t)-B \log (B-\alpha)^B\right.
\end{aligned}
$$

(b) determine price elasticity of tax
$\frac{\partial}{P(t)(1+t)}\left(\frac{\partial P(t)}{\partial t}(1+t)+1(P(t))\right)=\frac{B}{P(t)} \cdot \frac{\partial P(t)}{\partial t}$

$\begin{aligned} & \frac{\partial P(t)}{\partial t}=\frac{\alpha}{(B-\alpha)(1+T)} \\ & P^{\prime}(0)=\frac{\alpha}{B-\alpha} \\ & \end{aligned}$
(c, d) 
if $\alpha =0$ or $\beta = \infty$, tax burden is on consumers and P'(0) = 0 
if $\alpha =\infty$ or $\beta = 0$, tax burden is on producers and P'(0) = -1
![[Pasted image 20231114102205.png]]


# 4
(a) set aggregate demand equal to aggregate supply when accounting for $p(\tau)$

(b) CS PS and TR
$$
\begin{aligned}
& \text {a) Determine } \frac{d P}{d t} C t=0 \\
& \text { set } D^A=S^A \\
& \frac{d}{d t}\left[x(p(t))=J_d q_d(p(t))+J_f q_f(p(t)-t)\right] \\
& \frac{\partial x(p(t))}{\partial p} \cdot \frac{\partial p}{\partial t}=\frac{\partial(J_d \cdot q_d(p(t)))}{\partial p} \cdot \frac{\partial p}{\partial t}+\frac{\partial\left[J_f q_f(p(t)-t)\right)}{\partial p} \cdot\left[\frac{\partial p}{\partial t}-1\right] \\
& \frac{\partial}{\partial p}\left[J_f q f(p(t)-t)\right]=\frac{\partial p}{d t}\left[\frac{\partial}{\partial p}\left[J_d \cdot q_d(p(t))\right]+\frac{\partial}{\partial p}\left[J_f \; q_f(p(t)-t)\right]-\frac{\partial}{\partial p}[x(p(t))]\right. \\
& \frac{d p}{d t}=\left.\frac{J_f} {q f(p(t)-t)}{J_{d q d}(p(t))+J_f q_f(p(t)-t)-x(p(t))}\right|_{t=0} \\
& =\frac{J_f q_f(p)}{J_{d q}(p)+J_{f q f}(p)-x(p)} \\
&
\end{aligned}
$$