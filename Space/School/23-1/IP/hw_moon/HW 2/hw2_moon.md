## 1 
set: 
- D: days 1..35
- T: time 1..72 
- J: job shift types indexed from 1 to 99 with sub-indexed as follows:
	- $J_{c}$ 1..18
	- $J_{p}$ 19..33
	- $J_{f}$ 34..99 (without and with overshift = (18-7)+...+(18-17))
	
parameter
- $A_{t,j} = I_{\text{shift j activated in time t}}$
- $B_{t,j,d} = I_{\text{shift j activated in day d, time t}}$
- $c_j$ = cost of having an employee for shift j
- $w_{d,t}$: hourly demand at day d, time t (take max from the raw data)

decision variables
- $x_{j,d}$  number of employee working for job shift j at time d
- $x_{j,t}$  number of employee working for job shift j at time t
- $x_{j,d,t}$ number of employee working for job shift j at day d at time t




$\sum_j{A_{j,t}}

## 2. 
a. maximizing over matroid (as will be proved in b) where objective is a sum of scores of chosen locations in each county. 

b. 
- N = {0, .., 150} locations 
- independece system $\mathcal{I}$ is selecting at most two from each county.
- First, this (N, $\mathcal{I}$) is an independence system as empty set is included in $\mathcal{I}$ and $A \subseteq B, B \in \mathcal{I} \rightarrow A \in \mathcal{I}$ (as A would select less than equal to the number of locations chosen in B, it cannot exceed two from each county).
- Second, (N, $\mathcal{I}$) is a matroid as it is an independence system such that, for all F ⊆ N, every maximal independent set in F has the same cardinality r(F). For any set of location (F), if we choose locations from each county to the maximal (iterate over 12 counties as: two if there are more than or equal to two locations from specific county from in F, one if one location from specific county is in F, zero if there no location from specific county is in F. This procedure will make maximal cardinality same i.e. set can be represented by rank (a scalar).

c. greedy algorithm is defined as:
1. Arrange order such that cj1≥ cj2≥ · · · ≥ cjn. Initialize J = ∅.
2. For k = 1, · · · , n, if J ∪ {$j_k$} is an independent set, let J ← J ∪ {$j_k$}.
3. Return

The manager "ranked the 150 locations" (component 1 i.e. sort), and "select the top 2 in each of the 12 counties" (component 2 i.e. maintain independence, as we defined i.e. no cycle) which makes it greedy algorithm. Since greedy algorithm is optimal iff matroid (lecture note), and as the system is matroid, the solution of chose top two from each county is optimal.

d. (I'm not perfectly sure what the question is asking, but)
Alex explained matroid as "uncoupled between each choices" structure. This is why packing solution (with different weigts) is not a matroid as the first choices affects the following choices in terms of remaining capacity leading to suboptimal greedy solution. In the problem, we assume scores are pre-computed and doesn't depend on what other locations are chosen before. In reality, when the campaign locations are chosen, having campaigned before in a near enough location may make the spot less desirable thereby lowering the score. This creates a coupling situation, which our problem assmes to not have. Having nearby campaigns, which is not penalized according to our assumption, can make our solution suboptimal when that assumption is violated.