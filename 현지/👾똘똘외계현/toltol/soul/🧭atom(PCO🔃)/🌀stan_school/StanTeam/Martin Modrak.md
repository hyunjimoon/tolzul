Codeveloping [SBC library](https://hyunjimoon.github.io/SBC)


## Meeting notes
### store in the stack for now
1. discrete instead of continuous
2. posterior instead of prior draws
 (practical; why we need posterior draw 1.dap = prior but sbc will fail (alpha-error (practical; why we need posterior draw 1.dap = prior but sbc will fail (alpha-error

- two priors: scientific and program prior

1. false alarm prior (low specificity)
2. dull prior (low sensitivity) --> rejection sampling

f: posterior and prior
1 compare (theta' and ) for fixed $\delta_{\theta}$
![[Pasted image 20220523115038.png]]
2 compare (, ) for fixed y

p(theta | y) = p(theta' |y)

3 compare (dist_theta', dist_theat) for fixed dist_theat
![[Pasted image 20220523115046.png]]
- allowing canceled difference can be cancelled out each other.

![[Pasted image 20220523115541.png]]

p(theta, y, theta'):  theta-theta' sym
p(theta|theta', y=d) = p(theta'|theta, y=d)
vs
if you follow SBC procedure, p(theta' ㅗ theta| y=d)

p(theta', theta| y=d) 
= p(theta' | y=d) * p(theta | y=d) 
= p(theta | y=d) * p(theta' | y=d) 
= p(theta, theta'| y=d) 

> independence might be stronger

> conditional indep hold but may not have uniform rank
> marginalizing y is practical, but it would be better if y-conditional diagnostic is possible bc it would increase sensitivity


> In the fear of having low sensitivity (fail to detect the actual true), we choose very low specification (rejecting what actually works)

focus-SBC

control prior or y to the interested
> customized prior ~ customized y 

control y with prior vs  control prior with y
which has a better specificity btw f and g modeling?

### replace prior with fake data?

> tight prior is ok; it lowers sensitivity but concentrate on the point we 

### 
- differenct be