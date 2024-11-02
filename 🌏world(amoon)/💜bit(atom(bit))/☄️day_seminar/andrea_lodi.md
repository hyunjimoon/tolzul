17 instances was BB is the best thing to do 
- four strategies: preprocessing, cutting plane, sophisticated branching strategy, primal heuristics

##1 model preprocessing, algorithmic preprocessing
	- ![[Pasted image 20240306163849.png|100]]
- milp vs combinatorial opt: A's structure (yes or no)
##2 valid ineq: uAx >= ub: "u" gomory cut tells us how to read this u from tableau (split cuts)
##3 branching
- simplex is used by software as reoptimization if fast (feasibility; optimality is free)
- two decisions: node (bfs, most promising) and variable (not well studies; variable value closer to .5) selection
##4 solving submilps; large neighborhood search


- andrea don't see yet, cross learning (between different problem types (e.g. set covering and vrp) - for now just branch and bound for each
- solving two lps for every variables for every branching
- representing graph neural netwokrs (node on one side, constraints on the left)
- branching on one variable (local info associated with var)