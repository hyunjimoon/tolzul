From [Inverse Reward Design](https://papers.nips.cc/paper_files/paper/2017/file/32fdab6559cdfa4f167f8c31b9199643-Paper.pdf)

## 
|  | 1. negative side effect | 2. reward hacking |
| ---- | ---- | ---- |
| time frame | short | long |
| mis-alignment measured as | d(y, $\tilde{y}$)>>0<br>$\tilde{y}$: prior predictive, $y$: observation<br> | d($a^*$, $\tilde{a}^*$)>>0<br>$\tilde{a}^*$: optimal action given prior predictive, $a^*$: optimal action sequence implemented |
| perspective | observation of `env.` from `robot-human`'s | observation of `robot given human-env`  from `human`'s |
| tl;dr | argument: 1, 2 are the same phenomenon viewed in different time frame and perspective | Q.could there exist negative side effect that doesn’t lead to reward hacking given the freedom of scale of some model parameter (e.g. time horizon, discount factor)? i don’t think so.. |

Deep reinforcement learning is fragile to small changes in the setting.


## agents

agents relevant to startup (agent0):
- can we define innovation index based on quality (:= fitness of use) that can serve as proxy reward function (using DIRL)
- how startup journey can be represented as actions to manage spatiotemporal demand, productivity, technological uncertainties
- can building business simulation tools that can help task prioritization alignment (which is dependent on industry and phase of growth) be automated?

agent1. corporate 
- competing or collaborating agent of startup 
- how and when to capitalize in the context of startup operations (<-> agent3 )

agent2. government
- regulations (biotech)
- policies that can incubate innovation e.g. how clusters can be robust to external shocks (mechanism of overcoming core-rigidity with capital)

agent3. risk capital
- how to hedge risk portfolio

agent4. university
- which candidate to send abroad to maximize number of returns from startup 
- need not launch startup right after graduation, case where launched startup after getting industry expertise, which increased startup quality 

- usecase:give guidance to NUS oversea program on interview candidate selection, matching algorithm of student's background with oversea cities (sillicon valley, stockholm, shenzen)

agent5. entrepreneurs
- how to gauge one's comparative advantage