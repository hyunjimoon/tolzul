Jim hynes' three wishes
1. Better tools for model analysis, meaning making it easier to trace a particular aspect of behavior to structure and understanding how the structure generates that aspect of behavior.

2. Automatically increase robustness of a model -- i.e. make the modeled hypothesis robust to parameter changes and simple structural change (e.g. putting in a perception delay).

3. Help creating policy (decision rule) changes.  Perhaps changing a single answer (e.g. introduce a product at this point in time) to a policy answer.



| python function    | purpose                                                                         | in: xarray `data_vars`                                                                               | out: plot                                 | required work (priority)                                               |
| ------------------ | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------------------------------------------- |
| `tf11234_vgcsv2xr` | run vengine and store csv in `xarray`                                           |                                                                                                      |                                           | refactor (1), run vengine for 3x23 csv files (2)                       |
| `tf5_x_ctnt`       | are real and simulated cost component time vector of three main states similar? | cost and vaccine taking population, aggregated over space `x_ct`, `x_nt`                             | ![[Pasted image 20230709113704.png\|300]] | automate vengine-csv (real,sim of gdp,death,hosp.of three states)  (5) |
| `tf6_f1x_cs`       | how does each state's cost component (gdp, death, hosp.) differ?                | last day's cumulative mvv calculation for baseline `f1x_pcst[{'param':'baseline', 'time':time[-1]}]` | ![[marg_vv_by_state2.png\|300]]           | refactor (4)                                                           |
| `tf7_f2x_p`        | which parameter affects cumulative mvv the most?                                | sensitivity of last day's cumulative mvv w.r.t. 22 parameters`f2x_p`                                 | ![[elasticity_marg.png\|300]]             | refactor (4)                                                           |
| `tf8_x_ch2`        | how would vaccine timeshift affect cumulative mvv and its each component?       | `x_ch2`                                                                                              | ![[vv_by_vac_start_offset.png\|300]]      | refactor (3)                                                           |
|                    |                                                                                 |                                                                                                      |                                           |                                                                        |

expected time: 1,3,4: 3hr + 2: 3hr (+alpha)
