- problems that can solved from map-based compass
- scale-free system dynamics model, computational representation level 
- 
- divided into two depending on bottleneck: 
	- `feasiblity bottleneck`
		- feasibility modeling with set inclusion (conventional operations management and research) is more challenging than optimality modeling with specifying objective function and sometimes its gradient 
		- [[def(sol2.l)]] 
	- `optimality bottleneck`
		- optimality modeling with specifying objective function (cost of decreased gdp  + hospitalization + death in covid modeling) is more challenging than feasibility (discrete set of policy prescriptions e.g. vaccination amount, detail in [[iai3_data_structure]]) range simulation approach (agent based and compartment) where writing down the objective function is more challenging [[def(sol2.g)]] 

from `fx_pcsth` system, external evaluator provides `f: summary/test stat.`, internal evaluator sets `p: parameter (both estimated, fixed), c: component/sector, s: space, t: time, h: hyper-parameter/actionable)` as they adjust these based on `x: observed time series`, whose process can be aided by simulation tool