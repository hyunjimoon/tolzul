a. 
1a: minimize transportation cost of all travels (for every cost of arc (i,j) multiplied by whether each vehicle cross that arc or not)
1b: every vehicle can only leave the depot at most once (y00k can be 1 so vehicle need not leave)
1c: no self loops at the customer
1d: flow conservation at each node - what comes in, goes out 
1e: every vehicle visits at most one node at a time
1f: subtour elimination
1g: linking constraints that couples vehicle (path) and customer: for every customer (node) and for every vehicle, if a vehicle makes it to that customer, they go together! (I can't be riding vehicle1 and vehicle2)
1h: each custoemre mucst be served
1i: vehicle's capacity constraint i.e. aggregated demand packs supply's capacity
1j: vehicle k's path includes arc(i,j) or not (i,j including depot)
1k: vehicle k's path includes node i or not (i only for customer's depot)

e. total number of iteration is 26 and time for master and subproblem at each iteration, bounds are as follows. 

![[../../../../../../../ref/Pasted image 20230510204946.png]]

![[../../../../../../../ref/Pasted image 20230510205049.png]]
![[../../../../../../../ref/Pasted image 20230510205646.png]]
Objective value is 494.9 and 29 routes generated from the subproblems are as follows among which four of them are selected. For instance, fifth route is selected and therefore we can see from the visualization above green route from 11-7-3-1-11.
![[../../../../../../../ref/Pasted image 20230510205931.png]]