1a.  we define valid disjuctions as conditions that are exhaustive.

1b. 
$$
\begin{array}{ll}
\min & \sum_{j=1}^n \sum_{k=1}^{m_j} \lambda_{j k} f\left(s_{j k}\right) \\
\text { s.t. } & \sum_{k=1}^{m_j} \lambda_{j k}=1 \quad \forall j=1 . . n . \\
& \sum_{j=1} \sum_{k=1} \lambda_{j k} a_{i j} s_{j k} \leq L_i \forall_i=1 . . I . \\
& \lambda_{j k} \geq 0 \quad \forall_{j=1} . . n . \quad \forall_{k=1 . . m_j} \\
& \left(\lambda_j \cdots \cdots \lambda_{j m_j}\right) \in Q\left(m_j\right) \quad \forall_{j=1}=. . n_c
\end{array}
$$
2. 
3. 
Using the dual for the flow balance condition (lec.note for maxflow-mincut), we have the following dual for scenario s:
master problem
$$
\begin{align}
min \Sigma c_{ij}x_{ij} +  \Sigma_{s \in S} p_s \Sigma_{i,j \in A} \Sigma_{k \in K}f_{ijk}y_{ijk}^s \\
\end{align}
$$

$$
\begin{align}
min \Sigma c_{ij}x_{ij} +  \Sigma_{s \in S} p_s \theta_s \\
\end{align}
$$
primal sub problem
$$
\begin{align}
(w-Ux) \leq \theta_s \\
\Sigma_{k \in K} y_{ijk}^s \leq u_{ij}x_{ij} \forall{k \in K, s \in S}\\
y_{ijk}^{s} \geq 0
\end{align}
$$
dual sub problem
$$
\begin{align}
max \Sigma u_{ij}x_{ij} \pi_{ij}^s \\
s.t. \mu_{ik}^s - \mu_{jk}^s + \pi_{ijk}^s \geq 0 \\
\mu_{O_kk}^s - \mu_{D_kk}^s =1
\end{align}
$$

## appendix
```julia
feasibility_cut_number = 0
optimality_cut_number = 0
# Define main problem
MP = Model(() -> Gurobi.Optimizer(GRB_ENV));
set_optimizer_attributes(MP, "TimeLimit" => 60, "MIPGap" => 1e-4, "OutputFlag" => 0)
A = size(edge_ind, 1)
S = size(demand, 2)
K = size(demand, 1)
@variable(MP, x[1:A], Bin)
@variable(MP, θ[1:S] >= 0)
@objective(MP, Min, sum(edge_construction_cost[a] * x[a] for a in 1:A) 
                    + sum(prob[s] * θ[s] for s in 1:S))

lower_bound_all = []; upper_bound_all = []
MP_time = []; SP_max_time = []; SP_time = []
while true
    # solve master problem
    push!(MP_time, @elapsed optimize!(MP))
    lower_bound_new = objective_value(MP)
    push!(lower_bound_all, lower_bound_new)
    x_MP = value.(MP[:x])
    # solve S subproblems
    obj_SP = zeros(S)
    SP_time_all = zeros(S)
    for s = 1:S
        SP = Model(() -> Gurobi.Optimizer(GRB_ENV))
        set_optimizer_attributes(SP, "InfUnbdInfo" => 1, "OutputFlag" => 0)
        
        @variable(SP, y[a=1:A, k=1:K] >= 0)
        @constraint(SP, source[k=1:K], sum(y[a,k] for a in edge_start_dict[od_matrix[k,1]])
                    - sum(y[a, k] for a in edge_end_dict[od_matrix[k,1]]) == demand[k,s])
        @constraint(SP, [k=1:K, i in setdiff(node_list, od_matrix[k,:])], sum(y[a,k] for a in edge_start_dict[i])
                    - sum(y[a, k] for a in edge_end_dict[i]) == 0)
        @constraint(SP, sink[k=1:K], sum(y[a,k] for a in edge_start_dict[od_matrix[k,2]])
                    - sum(y[a, k] for a in edge_end_dict[od_matrix[k,2]]) == - demand[k,s])
        @constraint(SP, capacity[a=1:A], - sum(y[a,k] for k in 1:K) >= - edge_capacity[a] * x_MP[a])
        @objective(SP, Min, sum(transport_cost[a,k] * y[a,k] for a in 1:A, k in 1:K))
        
        SP_time_all[s] = @elapsed optimize!(SP)
        SP_obj = objective_value(SP)
        
        α_O_val = dual.(source)
        α_D_val = dual.(sink)
        β_val = dual.(capacity)
        
        if termination_status(SP) == MOI.INFEASIBLE # feasibility cut
            @constraint(MP, sum(demand[k,s]*(α_O_val[k] - α_D_val[k]) for k in 1:K)
                        - sum(edge_capacity[a] * x[a] * β_val[a] for a in 1:A)  <= 0)
            obj_SP[s] = 1e5
            feasibility_cut_number += 1
        elseif termination_status(SP) == MOI.OPTIMAL
            @constraint(MP, θ[s] >= sum(demand[k,s]*(α_O_val[k] - α_D_val[k]) for k in 1:K)
                        - sum(edge_capacity[a] * x[a] * β_val[a] for a in 1:A))
            obj_SP[s] = SP_obj
            optimality_cut_number += 1
        end
    end
    push!(SP_max_time, maximum(SP_time_all))
    push!(SP_time, sum(SP_time_all))
    upper_bound_new = sum(edge_construction_cost[a] * x_MP[a] for a=1:A) + sum(prob[s] * obj_SP[s] for s in 1:S)
    push!(upper_bound_all, upper_bound_new)
    verbose && @printf("Sol: %.2f - Bound: %.2f\n", upper_bound_all[end], lower_bound_all[end])
    if sum(MP_time) + sum(SP_time) >= TIME_LIMIT ||
        (upper_bound_new-lower_bound_new)/lower_bound_new < OPTIMALITY_GAP
        break
    end
end
```


![[../../../../../../../ref/Pasted image 20230415110959.png]]
multi bender's cut
![[../../../../../../../ref/Pasted image 20230416183511.png]]
we have a lower bound for $\theta$ as zero.