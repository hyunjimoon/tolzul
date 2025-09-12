2024-12-29
Angie defines this as: 

$\underset{a_t∈A_t}{argmax} Σ U(a_t, S_t)  \neq \underset{a_t∈A_t}{argmax} Σ U(a_t+1, S_t+1)$  where $s_{n} \sim P(s_n|D_n)$ n= t, t+1, a_t: action, s_t: state, D_t: data


$PathDep$ ⟺ $\underset{a_t∈A_t}{argmax} ; E[Σ_{τ=t}^T U(Env(a_τ,s_τ))|D_t] \neq \underset{a_t∈A_t}{argmax} ; E[Σ_{τ=t}^T U(Env(a_τ,s_τ))|D_{t+1}]$

$\underset{a_t∈A_t}{argmax} Σ U(a_t, s_t) \neq \underset{a_t∈A_t}{argmax} Σ U(a_t+1, s_t+1)$ where $s_{n} \sim P(s_n|D_n)$ n= t, t+1