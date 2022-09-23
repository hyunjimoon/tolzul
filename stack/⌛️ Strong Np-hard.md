Thm 2. Solving a real-world problem is NPC as it involves three coinflips: design an "algorithm" to be applied to the "approximated structure" of the system, assuming "axioms". 

This is related to P-NP conjecture.

> If a problem takes polynomial time on a non-deterministic Turing Machine (TM), then one can build a deterministic TM which would solve the same problem also in polynomial time. (P=NP)

model prior N(0,10) strong no, N(0,5) weak yes, N(0,1) strong yes 
Given the model with N(0,10) prior, algorithm A performs

If any thm on our setting is to be true, it should be able to collapse algorithm and model coinflip (once model is frozen, alg result is frozen, coupling 99 and 100th universe) 

m1:  N(0,10) prior + logit-binom likelihood --> optimization always passes sbc (= sbc(m1, opt) gives consistency certificate i.e. strong + weak yes

m2 N(0,5) prior + logit-binom likelihood
m3 N(0,1) prior + logit-binom likelihood

"consistency certificate (cc)"설계방안? -> "thm" VI ("VI 수렴한다"; A 조건 $\hat{
\theta} -> \theta$ contraction)

cc should be designed s.t. it could use the algorithm validation as submodule
조건문 A -> B (A true -> B true)

"cc-alg": 
$\theta =2$ adversarial algorithm (havning no "thm" that collapses three coinflip to two, our cc-alg should classify this as npc, instead of giving out cc)
- Recall theorems are tautology serving as a submodule for problem-solving. Its role is "coinflip-collapsing" i.e. syncing two coinflips into one. Chained coinflip collapsing ending with two coinflips is what is known as solving the problem. For instance, many problems are solved by the theorem "greedy algorithm achieves global optimum on matroid structure" whose role is to equate "algorithm" and "structure" coinflip reducing three coinflips to two. Notice axiom (induction) coinflip is used to sync the other two coinflips. The complexity of compounded choices forces us to divide and conquer; using "induction", we equate matroid structure (:=invariant maximal) with the optimality of "algorithm". This is "conditional coinflip-collapsing".

  (S, I) optimization vs hmc (given the model is normal distribution, optimization alg, hmc alg perform the same)
- Latent assumptions of induction are 1) countable system 2) homogeneity of n and n+1 \forall n 3) correct base case.
- Notice a stark contrast in "solving problem" and "solving real-world problem"; emphasis is added coinflip in approximating the real world which crosses the boundary from two to three making the latter intractable. Another way to understand this is, that the purely theoretical problem only needs a "mathematical" model whereas a real-world problem requires both a "mathematical" and "computation" model.  