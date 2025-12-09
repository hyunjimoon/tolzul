search questions with qq


**### critical review

No Country for old Men, boundary is not to be fixed. However, as we release a constant to vary, it creates exploding complexity interacting with other variables, perhaps making our two body to three body problem. However, this synergy is the essense as it fuels the escape from local optima, which we must capture. This dilema of controlling complexity in the context of "re-optimize upstream" has been frustrating to me.

Engineering details of innovative research was often muted from the paper, but thanks to author's recorded lecture, I was able to feel how the final quantifiable improvements from large scale online routing optimization was built up from SSO-VCC, MSO-VCC, VRP-VCC, DAR-VCC. The principled application of functional logics, dynamic programming, modularized design, tightening formulations, convergence guarantee to quantify the benefit of seeing the bigger picture attracted me. Hence I wish to use this paper critique to fully digest its logic, modularize it, and "let Alex help me" for my future research.

(i) outline the problem; 
-  reduce the singlestop optimization problem to a problem in only one dimension.
- In addition, the optimal solution to this problem would not have the vehicle wait for the passenger for any amount of time because the vehicle moves faster. 
- solve the multistop problem by solving a sequence of the single-stop optimization problems as a dynamic program if the norm used was differentiable or the L1 norm. 
- how these techniques would cause a large increase in profits for ridesharing companies, who could then pass some of these profits along to the consumer. 

(ii) summarize methodology/results


(iii) suggest avenues for further work
Downside of modular approach is, it prohibits interaction between different blackboxes' components. For instance, what is called upstream (which custmer to serve and in what sequence) and downstream decision does not necessarily have to be made in that order. Ultimately it is supply (vehicle) and demand (customer) matching so perhaps we could first decide where to met then assign vehicle and customer to that location.


The spirit re-optimizing upstream and subpath-based approach, one heading outside while the other seeking tradeoff within, are widely applicable. Relay logistics, column generation 

- Alex said: Number one is that right now the platforms have a very good understanding of who is more price sensitive versus who is more service quality sensitive in their user base.

- After listening to his talk, some points were left unclear to me. The topic of the distance that riders are willing to walk was addressed at the beginning of the talk, but it is unclear to me whether a large portion of riders would be willing to share a ride in the first place. Having too small a pool of riders could clearly cause some issues, and this is one possible effect of having too many riders be unwilling to share a ride. Lastly, when Professor Jacquillat presented his slide on the comparison of solutions between the standard CPLEX solution and his new algorithm, I noticed that many of the objective values were strictly better with his new algorithm than with the CPLEX solution.

## A. why ideal?
instead of asking why the problem is non-ideal, let's investigate what ideal assumptions we've made for those known to be ideal? assignment,   with relaxation,  every formulation can be ideal after relaxing its constraints one by one. tsp can be assignment, symmetric tsp can be solved by 
- nonbipartite to bipartite
- variable to fixed (cx + fy is easy if x is fixed)
- disaggregated to aggregated

## B. switching gear from theory to algorithm
disaggregated variables and decomposition algorithm co-evolve. Block matrix for knapsack of different machine motivated relaxing linking machine capacity constraint way of column generation algorithm, two stage decision led to the invention of benders decompostion where 
[[../../../../../../ref/alg_space2time.png]]  made dp applicable (re-optimized from start)
3. convex and continuous optimization 
	- where epigraph formulation, strong duality, continuous second stage from BD, euclidean (3d to 1d)
4. discrete, discretized (piecewise linear)
	- technique: dp and lagrangian dual 
	- using manhattan distance we can reduce to linear equations
	- linearize nonlinear optimization to use branch and bound module
	- tsp subgradient via lagrangian dual (c.p.329)

## C. closing the algorithm and theory loop: certificate of optimality 

[[../../../../../../ref/papa_pd_alg.png]]
1.  primal dual algorithm; 1 is optimality guarantee, 2 is for column / row generation 3 is for cutting plane (qq.why adjusting pi is easier than x? is this methodology restricted to col generation? although they are the same)
``` 
chp.5 primal, dual algorithm
“combinatorialized” the cost. We can also look at matters from the point of view of the dual. In going from D to DRP, we combinatoriali?e the right-hand side. Schematicall?, we can write In the shortest-path problem, the right-hand side of P is essentiall? trivial, and all the numerical problem data enters through the cost vector.
Therefore, RP and its dual do not depend e?plicitl? on the numerical problem data at all, but onl? on the admissible setJ, and we produce a purel? combinatorial subprob-lem, which we identified in this case as a reachabilit? problem.
The technique of starting with one problem, and iterativel? solving subprob-lems that are “more combinatorial” b? appl?ing the primal-dual algorithm is central to combinatorial optimi?ation
```

1.  primal-dual algorithm reduces the shortest-path problem to repeated solution of the simpler problem of finding the set of nodes reachable from a given node. Papadimitrioui named this as combinatorialized cost:
. [[../../../../../../ref/reopt_upstream_seq.jpeg]]
2. 
	a. bdd from finite cg rank, extreme ray and points are finite in convexified nice constraint 
	b. lexicographic, primal-dual algorithm 
	-  sp (ui-uj + pi_ij >=0), mf, (dual formulation)
	- 
## c. reformulation
5. lift and project
	- col gen tightens (by nulling part of variables (y) among (x,y) VS row gen. lifts from x to lambda and mu space
6. . principle of optimality
	- dynamic programming (sp, uls, ks, cs) 
	-  flow balance constraint forms route space
	- knapsack constraint forms pattern: cutting stock

## d.
7. when is reoptimization possible 
	- routing before coordination
8. 

## e. everything, everywhere, all at once
9. list of modules
	- knapsack (dp both min, max formulation with network flow - W5)
	- GA, GT, fixed charge min_(c_ij - ui)^+, - f_j

table need color coding - using google sheet
| no.main title (handy name)                                         | angie digest                                                                             | alex's comment, slide                                                  | class (A) and textbook comment (W,c,B,P,S)  | testable assumption                           | connection to lec. |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------- | --------------------------------------------- | ------------------ |
| A. proving thm (end well, in time)                                 | 1(deduct). matroid                                                                       | 1.                       | [[../../../../../../ref/thmalg_bender.png]] |                                               |                    |
|                                                                    | 2(induct). a.finite candidate, b.strict improvement                                      | 2.                                                                     |                                             |                                               |                    |
| B. swiching gears from theory to algorithm                         | 3(deduct).  convex, continuous .dp (continuous and discretize variable) and cvx.opt view | a.bd-outer apx, ?? b.lpj: theory(conv(P and xj=0,1)=pj) and cut (cglp) |                                             | benders has two (epigraph or )                |                    |
|                                                                    | 4(induct).  dynamic programming                                                          |                                                                        |                                             |                                               |                    |
| c. reformulation: lift, project, aggregate, tighten  (outsourcing) | 5(deduct).                                   |                                                                        |                                             |                                               |                    |
|                                                                    | 6(induct). some constraints form tightened space                                         | 6.                                    |                                             |                                               |                    |
| D. reoptimize upstream                                             | 7(deduct).                                                                               | 7.                                                                     |                                             |                                               |                    |
|                                                                    | 8(induct).                                                                               | 8.                                                                     |                                             |                                               |                    |
| E. module                                                          | 9(abduct).                                                                               | 9.                                                                     |                                             | is there a faster algorithmic time embedding? |                    |
|                                                                    |                                                                                          |                                                                        |                                             |                                               |                    |

   
principle of optimality (SP, ULS, KS, CS example from wolsey ch.5 dp) testable, modularized 
## questions

	1. conn:
2. modularize

4. 30% compared to 5% improvement came from re-optimizing the upstream route

## glossary
OG: o

[^1]: why continuous var reformulation (from discrete var, which keeps us from using dp) needed?