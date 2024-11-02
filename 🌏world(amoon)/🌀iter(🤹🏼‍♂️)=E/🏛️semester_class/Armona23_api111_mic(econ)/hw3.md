## 1


a) 
Dollar investment in risky assest if it gives me at least as much as 1. a>=1. So if a<1 is necessary condition.

b) Average income should be at least as much as one dollar to choose x2. i.e. every investment made should satisfy smaller expectation of utility of each outcome than utility of expected outcome:
$$
E V[L]=\pi a+(1-\pi) b>1
$$

c)
$\begin{aligned} & \mathcal{L}\left(x_1, x_2, \lambda\right)=u\left(-x_1+x_1\right)+ \pi u\left(w-x_2+a x_2\right)+(1-\pi) u\left(w-x_2+b x_2\right)+\lambda\left(w-x_1-x_2\right) \\ & =u\left(-x_1+x_1\right)+\pi u\left(w+x_2(a-1)\right)+(1-\pi) u\left(w+x_2(b-1)\right)+\lambda\left(w-x_1-x_2\right) \\ & \frac{\partial \mathcal{L}}{\partial x_2}=\pi u^{\prime}\left(w+x_2(a-1)\right)(a-1)+(1-\pi) u^{\prime}\left(w+x_2(p-1)\right)(p-1)-x=0 \\ & \frac{\partial \mathcal{L}}{\partial x_1}=-\lambda=0 \rightarrow \lambda=0 \\ & \quad \pi u^{\prime}\left(w+x_2(a-1)\right)(1-a)=(1-\pi) u^{\prime}\left(w+x_2(b-1)\right)(b-1) \\ & \frac{\pi(1-a)}{(1-\pi)(p-1)}=\frac{w\left(w+x_2(b-1)\right)}{u^{\prime}\left(w+x_2(a-1)\right)}\end{aligned}$

from 1 we assume: $\pi a+(1-\pi) b>1$ :
$$
\begin{aligned}
& a \pi+b-\pi b>1 \\
& \pi -a \pi<b-\pi b-1+\pi
\end{aligned}
$$
we know that $\pi(a-1)$ is negative as $a<1$. Thus, it must be the case that $-\pi a \cdot \pi<0$, such that $- \pi -1-(1-\pi) b>0$ -> 1 < b*


since $\pi (1-a)$ and $(1-\pi)(b-1)$ are both positive, we know that at optimal values of $x_2$, expected utility of getting the better payoff relevant to loss will be the expected loss relevant to expected benefit of the better payoff

## 2.
a) Maximization problem
$\operatorname{Max}$
$$
\begin{aligned}
& E U_{A_1}=p(\bar{u}-c)+(1-p)(-c) \\
& E U_{A_2}=0
\end{aligned}
$$
b)
$$
\begin{aligned}
E U_{A=1} & =p(\bar{u}-c)+(1-p)(-c) \\
& =p \bar{u}-p c-c+c p>0 \\
& =p \bar{u}-c>0 \\
& -> \mu_p>\frac{c}{\bar{u}}
\end{aligned}
$$
If cost of applying is low relative to pay off, stan should apply. 

(c)
conjugate prior fit outcome to those
$$
a^*(x)=\underset{a \in A}{\operatorname{argmax}} \sum_\delta \operatorname{Pr}(s \mid x) u(a, s)
$$
pl $x_i$ ~ Beta $\left(\alpha+x_1, B+x_0\right)$, where 1 sues and $O=$ failure
when $x_i=1 \rightarrow \frac{a+1}{a+1+B}>\frac{c}{\bar{u}}$
when $x_i=0 \rightarrow \frac{a}{a+B+1}>\frac{C}{\bar{u}}$ 

If Thomas was accepted in early decision $\left(x_i=1\right)$ then Stan should apply if $\frac{a+1}{a+1+B}>\frac{c}{\bar{u}}$. If Thomas is rejected $\left(x_i=0\right)$, then the threshold is has small cost relative to $\bar{u}$ has to be is smaller. Payoff is higher for $x_i=1$

(d)
when x=1: to go from $A=0$ to $A=1: \frac{a}{a+B}<\frac{c}{\bar{u}}<\frac{a+1}{a+1+B}$

when x=0: to go from applying $(A=1)$ to not applying $(A=0): \frac{a}{a+1+B}<\frac{c}{\bar{u}}<\frac{a}{a+B}$

(e)

$$
\begin{aligned}
& 0.03(a+b)=a \\
& b=\frac{0.97}{0.03}, a=\frac{97}{3} \\
& 0.03<\frac{a+1}{a+1+\frac{97}{3} a} \\
& a<\frac{97}{3} \\
& b <\left(\frac{97}{3}\right)^2
\end{aligned}
$$
$$
\begin{aligned}
& \frac{a+1}{a+1+b}<0.031 \\
& \frac{a}{a+1+b} <0.029 
\end{aligned}
$$
To go from $A=1 \rightarrow A=0$, when $\mu_p=36: .0292<\frac{c}{G}<.03$ to go from $A=0 \rightarrow A=1$, wen $u p=31: .03 <\frac{c}{\bar{u}}<.031$

To shift stan's decision from apply to not apply given $x=0$, stars prior on relative cost-utility must be between 2.9-3 %, while persuading to apply, when they were not going to apply, they must put their prior 3% - 3.1%.
