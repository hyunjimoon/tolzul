
Dual is a relation where the pair defines each other while Twin is [[🌅⏱ Weak Copy]]. Example of dual is [[🏭def(generate)]] and [[👁🧠🌲🏭 Digital Twin/deConv(Digital Twin)/👓 Discriminator/def(Discriminator)]] while example of twin is two solutions with the same distribution but with different construction. Might dual be related to twin? Yes. 

> Thm1. $\exists$ symmetry in `operator` $f:X\rightarrow R$ for every symmetry found in `result` random variable $X$.

> Thm2. If the  two `operators` $f, g$ returns C-twin `results`i.e. random variables $X, X'$, then, $f, g$ are in dual relationship. 

C-twin := same in distribution for every function in C; $<X, h> = <X', h> \forall h \in C$

This is the underlying principle behind GAN which can learn any distribution of data in an unsupervised manner. $X =_{D} G(z)$ where $z$ is random noise.

![[Pasted image 20220608082239.png |800]]
Another example where dual relation in operator is Primal-dual algorithm in combinatoric optimization. The algorithm whose framework is as above is designed to converge to unique optimal solution by finding two operators that act as the upper and lower bound for each other.

Given the two operators, each step involves `augmentation` i.e. strictly reducing the gap of objective value between the two operators. With integrality of input data, we can prove that this algorithm terminates. 

![[Pasted image 20220608082418.png | 800]] 
This figure shows steps of primal dual algorithm to solve Shortest Path and Max-Flow.


Reference

- Papadimitriou Chp.4 for a primal dual framework and 5 for its application on Max-Flow and Shortest Path: Ford-Fulkerson and Djjkstra.
