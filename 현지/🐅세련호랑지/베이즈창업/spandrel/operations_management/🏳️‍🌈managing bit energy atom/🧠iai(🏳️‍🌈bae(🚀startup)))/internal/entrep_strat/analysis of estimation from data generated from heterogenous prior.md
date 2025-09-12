what happens to the level of information of merged signal generate from two different priors?
Given the classification of reference modes (likelihood based classification from [this code](https://github.com/Data4DM/BayesSD/blob/3928fceee90fb289d7a5b45d8f13249f723a4600/code/moonshot/factory/wormholes/GeomPrior/aria/aria/models/ists.py#L164), and its [intro in inner_circle](https://github.com/Data4DM/BayesSD/blob/master/code/canon_dynamics/inner_circle.md)as BATS) ![[Pasted image 20230910092214.png]]
## parameter to data
![[Pasted image 20230910091957.png]]

higher the adjustment fraction (lower delay time), more control startup can have.

## information gain from weighted averaging two time series

| -                     | red ![[oscct.png]]                               | yellow ![[gr2db.png]] | blue ![[sshgr.png]] | green ![[Pasted image 20230910084616.png]] |
| --------------------- | ------------------------------------------------ | --------------------- | ------------------- | ------------------------------------------ |
| red ![[oscct.png]]    | up and down ![[Pasted image 20230910084151.png]] |                       |                     |                                            |
| yellow ![[gr2db.png]] |                                                  |                       |                     |                                            |
| blue ![[sshgr.png]]   |                                                  |                       |                     |                                            |
| green ![[nexgr.png]]  |                                                  |                       |                     |                                            |

- red and red: preserved if initial state is matched, not-preserved if not matched
- red and yellow: ?
- red and blue: structure of blue preserved
- red and green: structure of green preserved
- yellow and yellow: preserved
- yellow and blue: ?
- yellow and green: ?
- blue and blue: preserved
- blue and green: either blue or green structure preserved
- green and green: preserved