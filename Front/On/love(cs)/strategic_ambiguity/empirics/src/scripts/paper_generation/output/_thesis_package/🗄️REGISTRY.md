# 🗄️ REGISTRY: Figures & Tables for LaTeX
## The Promise Vendor Thesis
**Source of Truth:** [[📢BULLETIN]]

---

## 🖼️ FIGURES

### Fig_U_S3_ushape: U자형 생존 패턴
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | ✌️U (Vague Promise and Venture Growth) |
| **Section** | §3 Empirics |
| **Purpose** | U-Shaped Survival Pattern by Initial Vagueness |
| **File** | `_🩸I/midV_trap_analysis.png` |

**LaTeX:**
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{figures/midV_trap_analysis.png}
\caption{U-Shaped Survival Pattern by Initial Vagueness. Quartile analysis of 408,784 ventures shows both extremes (Q1=5.7\%, Q4=8.6\%) outperform the middle (Q2=2.9\%). $\chi^2 = 1430.9$, $p < 0.001$.}
\label{fig:Fig_U_S3_ushape}
\end{figure}
```

---

### Fig_U_S3_trap: Mid-V 함정률
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | ✌️U (Vague Promise and Venture Growth) |
| **Section** | §3 Empirics |
| **Purpose** | Commitment Trap Rate by Vagueness Level |
| **File** | `_🩸I/midV_trap_analysis.png` (Panel 2) |

**LaTeX:**
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.6\textwidth]{figures/midV_trap_analysis.png}
\caption{Commitment Trap Rate by Vagueness Level. Modal $V$ (=87.5) shows highest trap rate at 25.6\%, compared to 9.5\% for High-$V$ ventures.}
\label{fig:Fig_U_S3_trap}
\end{figure}
```

---

### Fig_C_S2_mechanism: E→|ΔV|→Y 메커니즘
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | 🦾C (The Commitment Trap) |
| **Section** | §2 Theory |
| **Purpose** | Capital-Flexibility-Growth Mechanism |
| **File** | `🦾C/⚙️process/figures/fig1_mechanism_3panel.png` |

**LaTeX:**
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=\textwidth]{figures/fig1_mechanism_3panel.png}
\caption{The Capital-Flexibility-Growth Mechanism. Left: $\rho(E, |\Delta V|)_{within V} = -0.052^{***}$. Right: $\rho(Y, |\Delta V|) = +0.159^{***}$.}
\label{fig:Fig_C_S2_mechanism}
\end{figure}
```

---

### Fig_C_S3_hypotheses: 3가설 검증
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | 🦾C (The Commitment Trap) |
| **Section** | §3 Empirics |
| **Purpose** | Three Hypotheses Verification |
| **File** | `_🩸I/three_hypotheses.png` |

**LaTeX:**
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=\textwidth]{figures/three_hypotheses.png}
\caption{Three Hypotheses Verification. H1: Flexibility $\to$ Growth ($\rho = +0.158^{***}$). H2: Capital $\to$ Less Flexibility ($\rho = -0.052^{***}$). H3: Capital's effect varies by $V$ (Low: $-0.05$, High: $+0.08$).}
\label{fig:Fig_C_S3_hypotheses}
\end{figure}
```

---

### Fig_C_S3_decile: 십분위별 헌신비용
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | 🦾C (The Commitment Trap) |
| **Section** | §3 Empirics |
| **Purpose** | Commitment Cost by Early Funding Decile |
| **File** | `🦾C/⚙️process/figures/fig2_cost_by_decile.png` |

**LaTeX:**
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{figures/fig2_cost_by_decile.png}
\caption{Commitment Cost by Early Funding Decile. All deciles show significant flexibility gap ($p < 0.001$).}
\label{fig:Fig_C_S3_decile}
\end{figure}
```

---

### Fig_C_S3_cohort: 2.7× 유연성 격차
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | 🦾C (The Commitment Trap) |
| **Section** | §3 Empirics |
| **Purpose** | The 2.7× Flexibility Gap |
| **File** | `🦾C/⚙️process/figures/fig3_cohort_analysis.png` |

**LaTeX:**
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{figures/fig3_cohort_analysis.png}
\caption{The 2.7$\times$ Flexibility Gap. Flexible ventures (Q4) achieve median $Y = 2.71$ vs. rigid ventures (Q1) at $Y = 1.00$.}
\label{fig:Fig_C_S3_cohort}
\end{figure}
```

---

### Fig_N_S2_newsvendor: k*=F⁻¹(CR) 곡선
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | 🤹N (The Promise Vendor) |
| **Section** | §2 Theory |
| **Purpose** | Promise Vendor Model — Optimal Option Count |
| **File** | `🤹N/⚙️process/figures/P3_cr_kstar_curve.png` |

**LaTeX:**
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{figures/P3_cr_kstar_curve.png}
\caption{The Promise Vendor Model --- Optimal Option Count. $k^* = F^{-1}(CR)$ where $CR = C_u/(C_u + C_o)$.}
\label{fig:Fig_N_S2_newsvendor}
\end{figure}
```

---

### Fig_N_S3_murky: Murky Middle 무균형
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | 🤹N (The Promise Vendor) |
| **Section** | §3 Empirics |
| **Purpose** | The Murky Middle Zone — No Equilibrium |
| **File** | `🤹N/⚙️process/figures/mixed audience/fig_murky_middle_zone.png` |

**LaTeX:**
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{figures/fig_murky_middle_zone.png}
\caption{The Murky Middle Zone --- No Stable Equilibrium. At $CR \approx 0.5$, neither pure Analyst nor pure Believer strategy dominates.}
\label{fig:Fig_N_S3_murky}
\end{figure}
```

---

### Fig_I_summary: 전체 분석 요약
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | 🩸I (Integration) |
| **Section** | - |
| **Purpose** | Complete Analysis Summary |
| **File** | `_🩸I/complete_analysis.png` |

**LaTeX:**
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=\textwidth]{figures/complete_analysis.png}
\caption{Comprehensive 9-panel visualization summarizing all key findings across Papers U, C, and N.}
\label{fig:Fig_I_summary}
\end{figure}
```

---

## 🗄️ TABLES

### Tab_U_S3_quartile: 사분위 생존률
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | ✌️U (Vague Promise and Venture Growth) |
| **Section** | §3 Empirics |
| **Purpose** | Survival Rates by Vagueness Quartile |

**LaTeX:**
```latex
\begin{table}[htbp]
\centering
\caption{Survival Rates by Vagueness Quartile ($N = 408,784$)}
\label{tab:Tab_U_S3_quartile}
\begin{tabular}{lcccc}
\toprule
Metric & Q1 (Low $V$) & Q2 & Q3 & Q4 (High $V$) \\
\midrule
$V$ Range & $0$--$50$ & $50$--$75$ & $75$--$87.5$ & $87.5$--$100$ \\
Survival Rate & 5.7\% & 2.9\% & 4.0\% & 8.6\% \\
Pattern & \checkmark & $\times$ & $\times$ & \checkmark \\
\bottomrule
\multicolumn{5}{l}{\footnotesize $\chi^2 = 1430.9$, $p < 0.001$} \\
\end{tabular}
\end{table}
```

---

### Tab_U_S3_chisq: χ² 검정 결과
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | ✌️U (Vague Promise and Venture Growth) |
| **Section** | §3 Empirics |
| **Purpose** | U-Shape Statistical Tests |

**LaTeX:**
```latex
\begin{table}[htbp]
\centering
\caption{U-Shape Statistical Tests by Industry}
\label{tab:Tab_U_S3_chisq}
\begin{tabular}{lcccc}
\toprule
Industry & $N$ & $\chi^2$ & $p$-value & U-Shape? \\
\midrule
Transportation & 52,847 & 1430.9 & $< 0.001$ & \checkmark \\
Healthcare & 89,234 & 892.3 & $< 0.001$ & \checkmark \\
Software & 198,456 & 1245.7 & $< 0.001$ & \checkmark \\
Hardware & 68,247 & 567.2 & $< 0.001$ & \checkmark \\
\bottomrule
\end{tabular}
\end{table}
```

---

### Tab_C_S3_descriptive: 기술통계량
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | 🦾C (The Commitment Trap) |
| **Section** | §3 Empirics |
| **Purpose** | Descriptive Statistics by Strategic Cohort |
| **Source** | `🦾C/⚙️process/figures/table1_descriptive.csv` |

**LaTeX:**
```latex
\begin{table}[htbp]
\centering
\caption{Descriptive Statistics by Strategic Cohort ($N = 123,906$)}
\label{tab:Tab_C_S3_descriptive}
\begin{tabular}{lrrrr}
\toprule
Cohort & $N$ & $E$ (Median) & $|\Delta V|$ (Mean) & $Y$ (Mean) \\
\midrule
Escape Velocity & 3,100 & \$257K & 40.2 & 3.01 \\
Golden Cage & 3,100 & \$5.4M & 19.1 & 1.95 \\
Patient Capital & 1,900 & \$3.5M & 37.8 & 2.88 \\
Struggle Zone & 1,900 & \$390K & 21.8 & 2.10 \\
\bottomrule
\end{tabular}
\end{table}
```

---

### Tab_C_S3_hypotheses: 3가설 검정 결과
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | 🦾C (The Commitment Trap) |
| **Section** | §3 Empirics |
| **Purpose** | Three Hypotheses Test Results |

**LaTeX:**
```latex
\begin{table}[htbp]
\centering
\caption{Three Hypotheses Test Results}
\label{tab:Tab_C_S3_hypotheses}
\begin{tabular}{llccc}
\toprule
Hypothesis & Relationship & $\rho$ & $p$-value & Confirmed \\
\midrule
H1 & Same $E$ $\to$ More $|\Delta V|$ $\to$ More $Y$ & +0.158 & $< 0.001$ & \checkmark \\
H2 & Same $V$ $\to$ More $E$ $\to$ Less $|\Delta V|$ & $-$0.052 & $< 0.001$ & \checkmark \\
H3 (Low $V$) & $E \to Y$ | Low $V$ & $-$0.05 & $< 0.05$ & \checkmark \\
H3 (High $V$) & $E \to Y$ | High $V$ & +0.08 & $< 0.01$ & \checkmark \\
\bottomrule
\end{tabular}
\end{table}
```

---

### Tab_C_S3_gap: 유연성 격차
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | 🦾C (The Commitment Trap) |
| **Section** | §3 Empirics |
| **Purpose** | The 2.7× Flexibility Gap |

**LaTeX:**
```latex
\begin{table}[htbp]
\centering
\caption{The 2.7$\times$ Flexibility Gap}
\label{tab:Tab_C_S3_gap}
\begin{tabular}{lcc}
\toprule
$|\Delta V|$ Quartile & Median $Y$ & Relative to Q1 \\
\midrule
Q1 (Rigid) & 1.00 & 1.00$\times$ \\
Q2 & 1.57 & 1.57$\times$ \\
Q3 & 2.02 & 2.02$\times$ \\
Q4 (Flexible) & 2.71 & 2.71$\times$ \\
\bottomrule
\multicolumn{3}{l}{\footnotesize Gap = Q4/Q1 = 2.7$\times$} \\
\end{tabular}
\end{table}
```

---

### Tab_C_S3_cost: 십분위별 헌신비용
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | 🦾C (The Commitment Trap) |
| **Section** | §3 Empirics |
| **Purpose** | Cost of Commitment by Early Funding Decile |
| **Source** | `🦾C/⚙️process/figures/table2_cost_of_commitment.csv` |

**LaTeX:**
```latex
\begin{table}[htbp]
\centering
\caption{Cost of Commitment by Early Funding Decile}
\label{tab:Tab_C_S3_cost}
\begin{tabular}{lrrrrr}
\toprule
Decile & $E$ Range & $N_{locked}$ & $N_{flex}$ & Cost & $p$ \\
\midrule
1 & \$471--\$91K & 252 & 748 & $-$0.93 & *** \\
2 & \$91K--\$222K & 339 & 661 & $-$0.89 & *** \\
... & ... & ... & ... & ... & *** \\
10 & \$15.6M+ & 771 & 229 & $-$0.96 & *** \\
\bottomrule
\multicolumn{6}{l}{\footnotesize All deciles significant at $p < 0.001$} \\
\end{tabular}
\end{table}
```

---

### Tab_N_S3_cr: 산업별 CR
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | 🤹N (The Promise Vendor) |
| **Section** | §3 Empirics |
| **Purpose** | Critical Ratio and Optimal k* by Industry Type |

**LaTeX:**
```latex
\begin{table}[htbp]
\centering
\caption{Critical Ratio and Optimal $k^*$ by Industry Type}
\label{tab:Tab_N_S3_cr}
\begin{tabular}{lcccc}
\toprule
Industry Type & $C_u$ & $C_o$ & $CR$ & $k^*$ \\
\midrule
Software/SaaS & Low & High & 0.3 & 1--2 \\
Mixed & Medium & Medium & 0.5 & Unstable \\
Deep-tech/AV & High & Low & 0.9 & 4--5 \\
\bottomrule
\end{tabular}
\end{table}
```

---

### Tab_I_verified: 검증된 숫자 요약
| 항목 | 내용 |
|:-----|:-----|
| **Paper** | 🩸I (Integration) |
| **Section** | - |
| **Purpose** | Verified Numbers Summary |
| **Source** | [[📢BULLETIN]] |

**LaTeX:**
```latex
\begin{table}[htbp]
\centering
\caption{Verified Numbers Summary}
\label{tab:Tab_I_verified}
\begin{tabular}{llc}
\toprule
Metric & Value & Paper \\
\midrule
$N_{total}$ & 408,784 & U \\
$N_{panel}$ & 123,906 & C \\
$\rho(Y, |\Delta V|)$ & +0.159*** & C \\
$\rho(E, |\Delta V|)_{within V}$ & $-$0.052*** & C \\
Flexibility Gap & 2.7$\times$ & C \\
Mid-V Trap Rate & 25.6\% & U \\
Q1 Survival & 5.7\% & U \\
Q4 Survival & 8.6\% & U \\
AV optimal $k^*$ & 4--5 & N \\
Fleet optimal $k^*$ & 1--2 & N \\
\bottomrule
\end{tabular}
\end{table}
```

---

## 📊 QUICK REFERENCE

| ID | Paper | Section | Purpose |
|:---|:-----:|:-------:|:--------|
| **Figures** ||||
| Fig_U_S3_ushape | ✌️U | §3 | U자형 생존 패턴 |
| Fig_U_S3_trap | ✌️U | §3 | Mid-V 함정률 |
| Fig_C_S2_mechanism | 🦾C | §2 | E→\|ΔV\|→Y 메커니즘 |
| Fig_C_S3_hypotheses | 🦾C | §3 | 3가설 검증 |
| Fig_C_S3_decile | 🦾C | §3 | 십분위별 헌신비용 |
| Fig_C_S3_cohort | 🦾C | §3 | 2.7× 유연성 격차 |
| Fig_N_S2_newsvendor | 🤹N | §2 | k*=F⁻¹(CR) 곡선 |
| Fig_N_S3_murky | 🤹N | §3 | Murky Middle 무균형 |
| Fig_I_summary | 🩸I | - | 전체 분석 요약 |
| **Tables** ||||
| Tab_U_S3_quartile | ✌️U | §3 | 사분위 생존률 |
| Tab_U_S3_chisq | ✌️U | §3 | χ² 검정 결과 |
| Tab_C_S3_descriptive | 🦾C | §3 | 기술통계량 |
| Tab_C_S3_hypotheses | 🦾C | §3 | 3가설 검정 결과 |
| Tab_C_S3_gap | 🦾C | §3 | 유연성 격차 |
| Tab_C_S3_cost | 🦾C | §3 | 십분위별 헌신비용 |
| Tab_N_S3_cr | 🤹N | §3 | 산업별 CR |
| Tab_I_verified | 🩸I | - | 검증된 숫자 요약 |

---

*Registry managed by 🟠G-Squad*
*Verified by 🔴K-Squad*
*Last updated: 2025-12-08*
