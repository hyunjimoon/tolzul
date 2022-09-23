![[Pasted image 20220606091058.png]]

|                        | System Dynamics                                                                             | Discrete Event Simulation                           |
| ---------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| clock type             | continuous                                                                                  | interarrival time ~ exp($\lambda$)                  |
| # of variables         | a few                                                                                       | many, Stochastic process                            |
| e.g.                   | fluid flow, strategic                                                                       | longest waiting time, backlog estimate              |
| how                    | global clock                                                                                | simulation clock                                    |
|                        | Relation-based; differential equation i.e. identify structure + relationships within system | Object-based                                        |
|                        | nonlinear                                                                                   | linear                                              |
| direction of inference | deconvolution i.e. what is Y given X + Y = Z, X + Z = 10 (Dirichlet problem)                | convolution i.e. what is Z given X, Y and X + Y = Z |

- Dirichlet problem is finding a function which solves a specified PDE in the interior of a given region which satifies boundary values.
- DES, which looks at the result of random convolution with many variables, it is difficult to discover new facts, whereas in SD, it is easy to discover causal relationships by observing convergence with few variables. DES is Contextual Model (상황적합모델) while SD: Resource-based model (자원기반모델)
- Five types of network: fully connected, random, Watts-Strogatz small world, scale-free, lattice networks
  