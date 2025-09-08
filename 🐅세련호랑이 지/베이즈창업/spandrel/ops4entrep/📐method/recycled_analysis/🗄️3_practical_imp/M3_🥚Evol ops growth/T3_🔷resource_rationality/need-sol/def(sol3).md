- problems that can solved from genome-based map-based compass
- firm agent's approach
- divided into 
	- [[def(sol3.g)]] corporate and dominant in the market e.g. google, amazon, bank of america who need to be keep innovate to sustain itself 
	- [[def(sol3.l)]] entrant who 
		- sense signal from the market constructed by dominant (e.g. zillow, clicks) then detect poorly served need then detect technology for solution

## nine components
![[Pasted image 20240115213756.png|800]]
## camera focus analogy

![[Pasted image 20240115214003.png|500]]
### need-leadership
pure customer pull 
- (fulfill, sol, need) -> (fulfill, sol, $customer_{1..N}(need)$)
- `sol lens` approximates 
- $\underset{{customer_{[n] \in \{1..\infty \}}}}{argmax} p_f(sol, customer_{[n]}(need)|sol=s_1, need), |[n]| = \infty$ as 
	$\underset{{customer_{[n]  \in \{1..\infty \}}}}{argmax} p_f(sol, customer_{[n]}(need)|sol=s_1, need), |[n]| = N$
- the higher demand uncertainty lowering capability is, the more accurate it can construct $p_f$
- develop technology for solution based on identified need

### sol-leadership
pure tech push (sol-leadership):
- (fulfill, sol, need) -> (fulfill, $technology_{1..M}(sol)$, need) 
- `need lens` approximates
-  $\underset{{technology_{[m]  \in \{1..\infty \}}}}{argmax} p_f(technology_{[m]}(sol), need|sol, need=n_1), |[m]| = \infty$ as  
	$\underset{{technology_{[m]  \in \{1..\infty \}}}}{argmax} p_f(technology_{[m]}(sol), need|sol, need=n_1), |[m]| = M$

- the higher technology uncertainty lowering capability is, the more accurate it can construct $p_f$

search need-sol pair (quantified self; several points filled out)
- information in the cell; tradeoff between gun and butter (possibility frontier; spending on national defense or on domestic programs)
- cannot evaluate before using them; 
- no production frontier - labor, automation
### fulfill-leadership
 -  (fulfill, sol, need) -> (fulfill, $technology_{[m]}(sol), customer_{[n]}(need)$)


each leadership may converge differently (e.g. $a_{m n}=\frac{m}{m+n}$may converge to different (need, sol) when row vs col vs diagonal - wise each converge to 0, 1, .5) and we argue criticality of fulfill-leadership

- one sol would be suitable for wide variety 
- private solution
- different clothing outfit (phone - iphone)
- low cost to create variety
- economics `MU_need/p_need = MU_sol/p_sol
define fulfill as balancing m, n uncertainty (can we argue convergence to .5 is the best? in what sense?)