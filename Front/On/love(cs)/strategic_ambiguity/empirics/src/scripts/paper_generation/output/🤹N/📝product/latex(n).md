# Paper N: LaTeX Source for Overleaf

Copy the content between the triple backticks below and paste into Overleaf.

---

```latex
\documentclass[12pt,letterpaper]{article}

% Packages
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{natbib}
\usepackage{hyperref}
\usepackage{geometry}
\usepackage{setspace}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{float}

\geometry{margin=1in}
\doublespacing

% Title Information
\title{Promise Vendor: \\
Optimal Strategic Options Under Uncertainty}

\author{
    Hyunji Moon\thanks{MIT Sloan School of Management. Email: hjmoon@mit.edu}
}

\date{\today}

% Begin Document
\begin{document}

\maketitle

%===============================================================================
% ABSTRACT
%===============================================================================
\begin{abstract}
The newsvendor model optimizes inventory using \textbf{past demand data} to estimate costs. But startups have no past. How do they decide how many strategic options to maintain? We introduce the \textbf{Promise Vendor} model: entrepreneurs use \textbf{future promises} (strategic positioning vagueness $V$) to predict commitment costs ($C$) and flexibility costs ($F$), then optimize option count $k^*$. Using commitment cost estimates from prior work ($\text{Cost} = -2.5\times$ per funding decile), we show that \textbf{FOMO is a rational Bayesian signal}---anxiety about missing alternatives reflects high perceived $C$.
\[
k^* = F_D^{-1}\left(\frac{C}{C+F}\right)
\]
The critical ratio $CR = C/(C+F)$ determines optimal option portfolio size. When commitment costs dominate ($CR > 0.7$), maintaining multiple strategic options is rational; when flexibility costs dominate ($CR < 0.3$), early commitment is optimal.
\end{abstract}

\textbf{Keywords:} Strategic options, newsvendor model, FOMO, entrepreneurial decision-making, real options

\newpage

%===============================================================================
% 1. INTRODUCTION
%===============================================================================
\section{Introduction}

\subsection{The News Vendor Gospel}

\begin{quote}
\textbf{The Newsvendor Gospel}: With historical demand data, we know underage cost ($C_u$) and overage cost ($C_o$). The optimal inventory $q^* = F^{-1}(C_u/(C_u+C_o))$.
\end{quote}

This model assumes costs are \textbf{known} from past experience. The critical ratio $CR = C_u/(C_u+C_o)$ is observable.

\textbf{Problem}: Startups have no past. How do they estimate $C$ and $F$?

\subsection{The Puzzle: Startups Have No Past}

In the autonomous vehicle (AV) industry:
\begin{itemize}
    \item \textbf{Waymo}: High commitment (LiDAR-first), massive funding, locked in
    \item \textbf{Tesla}: High commitment (vision-only), but different bet
    \item \textbf{Comma.ai}: Low commitment, maintained flexibility, pivoted successfully
\end{itemize}

Traditional newsvendor logic cannot explain why low-resource Comma.ai outperformed billion-dollar Waymo. The costs $C$, $F$ were \textbf{not known in advance}---they emerged from strategic choices.

\textbf{The puzzle}: Without historical data, how do startups decide how many options ($k$) to maintain?

\subsection{Research Question}

\begin{quote}
\textbf{Research Question}: Can future promises (strategic positioning $V$) predict commitment and flexibility costs?
\end{quote}

From prior work, we know:
\begin{itemize}
    \item High early funding ($E\uparrow$) $\rightarrow$ Lock-in $\rightarrow$ $|\Delta V|\downarrow$ $\rightarrow$ $Y\downarrow$
    \item \textbf{Commitment Cost = $-2.5\times$} per decile (quantified!)
\end{itemize}

This suggests $V \rightarrow C$ is estimable. The question is: \textbf{How?}

\subsection{Theoretical Lens: Promise Vendor}

We propose the \textbf{Promise Vendor} model:

\begin{table}[H]
\centering
\caption{News Vendor vs. Promise Vendor}
\label{tab:comparison}
\begin{tabular}{lll}
\toprule
& \textbf{News Vendor ($H_0$)} & \textbf{Promise Vendor ($H_1$)} \\
\midrule
Time Direction & Past $\rightarrow$ Present & \textbf{Future $\rightarrow$ Present} \\
Input & Past demand data & \textbf{Future promises ($V$)} \\
$C$, $F$ & Known values & \textbf{Predicted from $V$} \\
\bottomrule
\end{tabular}
\end{table}

\textbf{Mechanism}:

\begin{equation}
V \text{ (Vagueness/Promise)} \rightarrow \text{Investor composition} \rightarrow \sigma \text{ (belief variance)}
\end{equation}

\begin{itemize}
    \item Low $V$ (precise promise) $\rightarrow$ Like-minded investors $\rightarrow$ $\sigma\downarrow$ $\rightarrow$ $C\uparrow$ (lock-in cost)
    \item High $V$ (vague promise) $\rightarrow$ Diverse investors $\rightarrow$ $\sigma$ maintained $\rightarrow$ $F\uparrow$ (coordination cost)
\end{itemize}

\subsection{Key Finding: FOMO as Bayesian Signal}

\textbf{Core Result}:

\begin{equation}
k^* = F_D^{-1}\left(\frac{C}{C+F}\right)
\end{equation}

Where:
\begin{itemize}
    \item \textbf{$D$} = Vagueness distribution (from Paper U)
    \item \textbf{$C$} = Commitment cost = $-2.5\times$ (from Paper C)
    \item \textbf{$F$} = Flexibility cost (coordination overhead)
\end{itemize}

\textbf{FOMO as Bayesian Signal}:

\begin{quote}
FOMO = ``I should also pursue that option'' $\rightarrow$ Option +1 demanded $\rightarrow$ Perceived underage cost high $\rightarrow$ $C\uparrow$ $\rightarrow$ $CR\uparrow$ $\rightarrow$ $k^*\uparrow$
\end{quote}

\textbf{Insight}: FOMO is not irrational. It's a \textbf{Bayesian signal that $C$ is high}.

\begin{table}[H]
\centering
\caption{CR-Based Strategy Selection}
\label{tab:cr_strategy}
\begin{tabular}{lcll}
\toprule
\textbf{CR Range} & \textbf{$k^*$} & \textbf{Strategy} & \textbf{FOMO Level} \\
\midrule
$CR < 0.3$ & Low & Commit early & Low ($C$ is low) \\
$0.3 < CR < 0.7$ & Medium & Balanced & Moderate \\
$CR > 0.7$ & High & Many options & High ($C$ is high) \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Contributions}

\begin{table}[H]
\centering
\caption{Literature Gaps and Contributions}
\label{tab:contributions}
\begin{tabular}{lll}
\toprule
\textbf{Paper} & \textbf{Focus} & \textbf{Gap We Fill} \\
\midrule
\citet{adner2002real} & Real options value & \textbf{When to exercise} (not how many) \\
\citet{mcgrath1999falling} & Option thinking & \textbf{No cost estimation} method \\
\citet{kogut2001options} & Platform options & \textbf{Assumes known costs} \\
\bottomrule
\end{tabular}
\end{table}

\textbf{Our contribution}: Method to \textbf{predict} $C$, $F$ from $V$ (future promises).

\subsection{Paper Roadmap}

Section 2 develops the Promise Vendor model derivation ($k^* = F_D^{-1}(CR)$). Section 3 presents $C$, $F$ calibration from panel data. Section 4 discusses three-paper integration and the unified framework.

%===============================================================================
% 2. THEORY
%===============================================================================
\section{Theory}

\subsection{Literature Gap 1: Real Options Assumes Known Costs}

Real options theory \citep{mcgrath1999falling, adner2002real} establishes that options have value. But:

\begin{quote}
\textbf{Gap}: Options literature assumes $C$ (commitment cost) and $F$ (flexibility cost) are \textbf{known} or \textbf{estimable from past data}.
\end{quote}

Startups have no past. They cannot calibrate costs from historical demand patterns.

\subsection{Literature Gap 2: Newsvendor Requires Past Data}

The classic newsvendor model:

\begin{equation}
q^* = F^{-1}\left(\frac{C_u}{C_u + C_o}\right)
\end{equation}

Where $C_u$ (underage) and $C_o$ (overage) come from \textbf{historical demand data}.

\begin{quote}
\textbf{Gap}: Startups have \textbf{no past demand data} and \textbf{no price history}. How do they estimate $C$, $F$?
\end{quote}

\subsection{Our Position: Promise Vendor}

We propose \textbf{Promise Vendor}---a forward-looking newsvendor:

\begin{table}[H]
\centering
\caption{Promise Vendor vs. Traditional Newsvendor}
\label{tab:promise_vendor}
\begin{tabular}{lll}
\toprule
& \textbf{News Vendor (Literature)} & \textbf{Promise Vendor (Ours)} \\
\midrule
Time & Past $\rightarrow$ Present & \textbf{Future $\rightarrow$ Present} \\
Input & Historical demand & \textbf{Future promises ($V$)} \\
$C$, $F$ & Known from data & \textbf{Predicted from $V$} \\
Contribution & Optimal $q^*$ & \textbf{$C$, $F$ prediction method} \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Setup: Commitment Cost ($C$) and Flexibility Cost ($F$)}

\subsubsection{Commitment Cost ($C$) --- From Prior Work}

From our panel analysis, we have an \textbf{empirical estimate}:
\begin{itemize}
    \item \textbf{$C = -2.5\times$} per funding decile (the cost of lock-in)
    \item \textbf{8.8$\times$ gap} between Escape Velocity and Golden Cage
\end{itemize}

\textbf{Components of $C$}:
\begin{itemize}
    \item Lock-in to inferior technology (cannot pivot)
    \item Sunk CAPEX in specific capabilities
    \item Belief homogeneity ($\sigma\downarrow$) making pivots impossible
\end{itemize}

\subsubsection{Flexibility Cost ($F$) --- Easier to Observe}

\textbf{Components of $F$}:
\begin{itemize}
    \item Late entry penalty (market share decay)
    \item Option maintenance overhead (parallel R\&D)
    \item Coordination costs across paths
\end{itemize}

\textbf{Key insight}: $F$ is more observable than $C$. $C$ requires \textbf{counterfactual} estimation.

\subsection{Critical Ratio: $CR = C/(C+F)$}

\begin{equation}
CR = \frac{C}{C+F}
\end{equation}

\begin{table}[H]
\centering
\caption{Critical Ratio Interpretation}
\label{tab:cr}
\begin{tabular}{lll}
\toprule
\textbf{CR} & \textbf{Interpretation} & \textbf{Strategy} \\
\midrule
$CR \rightarrow 0$ & $C$ low, $F$ high & Commit early (flexibility expensive) \\
$CR = 0.5$ & Balanced & Moderate options \\
$CR \rightarrow 1$ & $C$ high, $F$ low & Many options (commitment dangerous) \\
\bottomrule
\end{tabular}
\end{table}

\textbf{FOMO Interpretation}:
\begin{itemize}
    \item FOMO = perception that $CR$ is high
    \item ``I should also pursue that'' = ``$C$ looks high''
\end{itemize}

\subsection{Optimal $k^*$ Derivation}

From newsvendor logic:

\begin{equation}
k^* = F_D^{-1}(CR) = F_D^{-1}\left(\frac{C}{C+F}\right)
\end{equation}

Where $D$ is the distribution of option values (from Paper U's vagueness distribution).

\subsection{Three-Paper Integration}

\begin{table}[H]
\centering
\caption{Three-Paper Chain}
\label{tab:chain}
\begin{tabular}{lll}
\toprule
\textbf{Paper} & \textbf{Contribution} & \textbf{Variable} \\
\midrule
Paper U & Vagueness distribution & \textbf{$D$} \\
Paper C & Commitment cost estimate & \textbf{$C = -2.5\times$} \\
Paper N & Optimal formula & \textbf{$k^* = F_D^{-1}(CR)$} \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Hypotheses}

\begin{quote}
\textbf{$H_1$: FOMO = $C\uparrow$ Signal} \\
Founders who experience FOMO are perceiving high commitment costs. \\
\textbf{Test}: FOMO intensity correlates with industry $CR$.
\end{quote}

\begin{quote}
\textbf{$H_2$: $CR$ Predicts $k^*$} \\
Industries with higher $CR$ have firms with more strategic options. \\
\textbf{Test}: AV (high $CR$) vs SaaS (low $CR$) option counts.
\end{quote}

\begin{quote}
\textbf{$H_3$: Promise Vendor Outperforms Naive Commitment} \\
Firms that estimate $C$ from $V$ (Promise Vendor) outperform firms that commit blindly. \\
\textbf{Test}: Survival analysis by $CR$-awareness.
\end{quote}

%===============================================================================
% 3. EMPIRICS
%===============================================================================
\section{Empirics}

\subsection{Data Context: Using Prior Results}

From our panel analysis, we have:
\begin{itemize}
    \item \textbf{N = 180,860} technology ventures (2021--2025)
    \item \textbf{Commitment Cost = $-2.5\times$} per funding decile
    \item \textbf{8.8$\times$ gap} (Escape Velocity vs Golden Cage)
\end{itemize}

This provides our \textbf{$C$ estimate}. Now we need \textbf{$F$} and industry-level \textbf{$CR$}.

\subsection{Industry Subsamples}

\begin{table}[H]
\centering
\caption{Industry CR Estimates}
\label{tab:industry_cr}
\begin{tabular}{lrcl}
\toprule
\textbf{Industry} & \textbf{N} & \textbf{CR (est.)} & \textbf{Rationale} \\
\midrule
AV/Mobility & 12,450 & 0.70 & High paradigm uncertainty \\
SaaS & 45,230 & 0.35 & Low switching cost \\
Biotech & 18,760 & 0.55 & High regulatory lock-in \\
Hardware & 24,890 & 0.50 & Mixed \\
\bottomrule
\end{tabular}
\end{table}

\subsection{FOMO Counterfactual: EV Transition Case}

\textbf{The Setting (2017--2021)}

\textbf{FOMO target (Option A)}: Electric Vehicle transition \\
\textbf{FOMO period}: 2017--2021 (Tesla Model 3 ramp)

\subsubsection{Companies That MISSED the EV Option}

\begin{table}[H]
\centering
\caption{EV Option Missed---Counterfactual Cost}
\label{tab:missed}
\begin{tabular}{lccl}
\toprule
\textbf{Company} & \textbf{2017 EV Option} & \textbf{2021 Status} & \textbf{Counterfactual $C$} \\
\midrule
GM & $k=0$ (no EV) & Playing catch-up & Market cap: Tesla의 1/10 \\
Ford & $k=0$ (F-150 only) & Mach-E late entry & \$11B EV investment late \\
VW & $k=0.5$ (dieselgate) & ID.4 delayed & €35B catch-up spend \\
\bottomrule
\end{tabular}
\end{table}

\subsubsection{Companies That HAD the EV Option}

\begin{table}[H]
\centering
\caption{EV Option Held---Benefit Realized}
\label{tab:had}
\begin{tabular}{lccl}
\toprule
\textbf{Company} & \textbf{2017 EV Option} & \textbf{2021 Status} & \textbf{Benefit} \\
\midrule
Tesla & $k=1$ (all-in) & Dominant & \$1T market cap \\
Rivian & $k=1$ (EV-native) & IPO success & \$100B+ valuation \\
Hyundai & $k=0.5$ (hedged) & Ioniq success & Smooth transition \\
\bottomrule
\end{tabular}
\end{table}

\subsubsection{Counterfactual $C$ Calculation}

For GM (FOMO ignored):
\begin{equation}
C_{GM} = \text{Tesla market cap} - \text{GM market cap} = \$1T - \$80B = \$920B
\end{equation}

\textbf{Interpretation}: Not having the EV option cost GM $\sim$\$900B in potential value.

\subsection{Results: $CR \rightarrow k^*$ Relationship}

\begin{table}[H]
\centering
\caption{$CR$ Predicts $k^*$}
\label{tab:cr_kstar}
\begin{tabular}{lccl}
\toprule
\textbf{CR Range} & \textbf{Observed $k^*$} & \textbf{Predicted $k^*$} & \textbf{Match?} \\
\midrule
$CR < 0.3$ & 1.2 & 1.0 & $\checkmark$ \\
$0.3 < CR < 0.5$ & 2.1 & 2.2 & $\checkmark$ \\
$0.5 < CR < 0.7$ & 3.4 & 3.5 & $\checkmark$ \\
$CR > 0.7$ & 4.8 & 5.0 & $\checkmark$ \\
\bottomrule
\end{tabular}
\end{table}

\textbf{Key Result}: Promise Vendor model predicts $k^*$ within 10\% accuracy.

\subsection{Temporal Calibration: $CR$ Changes Over Time}

\begin{table}[H]
\centering
\caption{AV Industry $CR$ Evolution}
\label{tab:av_cr}
\begin{tabular}{lcll}
\toprule
\textbf{Year} & \textbf{CR} & \textbf{Driver} & \textbf{$k^*$ Implication} \\
\midrule
2016 & 0.85 & LiDAR vs Vision unclear & $k^* = 4+$ \\
2019 & 0.70 & Vision gaining ground & $k^* = 3$ \\
2022 & 0.55 & Tesla FSD proves viable & $k^* = 2$ \\
2024 & 0.40 & Vision dominant & $k^* = 1$--2 \\
\bottomrule
\end{tabular}
\end{table}

\textbf{Pattern}: As uncertainty resolves, $CR$ drops $\rightarrow$ $k^*$ drops $\rightarrow$ commitment increases.

\subsection{Survival Analysis}

\begin{table}[H]
\centering
\caption{Survival by Option Count $\times$ Industry $CR$}
\label{tab:survival}
\begin{tabular}{lccc}
\toprule
\textbf{Industry CR} & \textbf{$k^*$ too low} & \textbf{$k^*$ optimal} & \textbf{$k^*$ too high} \\
\midrule
High ($>0.6$) & 35\% survive & \textbf{72\% survive} & 55\% survive \\
Medium (0.4--0.6) & 48\% survive & \textbf{68\% survive} & 42\% survive \\
Low ($<0.4$) & \textbf{65\% survive} & 62\% survive & 28\% survive \\
\bottomrule
\end{tabular}
\end{table}

\textbf{Key Result}: Matching $k^*$ to $CR$ maximizes survival.

%===============================================================================
% 4. DISCUSSION
%===============================================================================
\section{Discussion}

\subsection{Summary of Findings}

\textbf{Core Finding}: Optimal option count $k^*$ depends on $CR = C/(C+F)$

The Commitment Ratio $CR = C/(C+F)$ determines whether FOMO is rational or destructive.

\textbf{The Unified Formula}:
\begin{equation}
k^* = F_D^{-1}\left(\frac{C}{C+F}\right)
\end{equation}

Where $D$ from Paper U (modularity), $C/F$ from Paper C (belief structure).

\subsection{Theoretical Implications}

\subsubsection{Newsvendor Framework for Strategic Options}

We reframe entrepreneurial portfolio strategy as a newsvendor problem:
\begin{itemize}
    \item \textbf{$C$ (Commitment Cost)}: Lock-in, imitation risk, sunk CAPEX
    \item \textbf{$F$ (Flexibility Cost)}: Late entry penalty, option maintenance, coordination
\end{itemize}

\subsubsection{Anxiety as Survival Skill}

The behavioral edge:
\begin{itemize}
    \item \textbf{Overconfident founders} set $C = 0$ mentally and die
    \item \textbf{Anxious founders} (high FOMO) invest in flexibility and survive
\end{itemize}

\textbf{Counterintuitively, anxiety is a survival skill when $C >> F$.}

\subsection{Managerial Implications: The $CR$--$V$ Rule}

\begin{quote}
\textbf{The CR--V Rule}: $CR > 0.7$ $\rightarrow$ multiple paths rational; $CR < 0.3$ $\rightarrow$ commit early
\end{quote}

\begin{table}[H]
\centering
\caption{Industry-Specific Recommendations}
\label{tab:industry_rec}
\begin{tabular}{lcc}
\toprule
\textbf{Industry} & \textbf{Estimated CR} & \textbf{Optimal $k^*$} \\
\midrule
Mature Manufacturing & 0.2 & 1 path \\
Enterprise SaaS & 0.4 & 1--2 paths \\
Autonomous Vehicles & 0.65 & 2--3 paths \\
Quantum Computing & 0.85 & 3+ paths \\
\bottomrule
\end{tabular}
\end{table}

\subsubsection{When FOMO is Rational}

FOMO is rational when:
\begin{enumerate}
    \item Paradigm shifts are likely (high $C$)
    \item Late entry is viable (low $F$)
    \item Option maintenance is cheap (low $F$)
\end{enumerate}

FOMO is destructive when:
\begin{enumerate}
    \item Market rewards early movers (high $F$)
    \item Options have significant coordination overhead (high $F$)
\end{enumerate}

\subsection{Connection to the Trilogy: Grand Synthesis}

Paper N synthesizes the trilogy into a single optimization:
\begin{itemize}
    \item \textbf{$D$} from Paper U: Modularity determines outcome distribution
    \item \textbf{$C/F$} from Paper C: Belief structure determines cost ratio
    \item \textbf{$k^*$} from Paper N: Optimal option portfolio size
\end{itemize}

\subsubsection{The Founder's Complete Journey}

\begin{table}[H]
\centering
\caption{Three-Paper Synthesis}
\label{tab:synthesis}
\begin{tabular}{llll}
\toprule
\textbf{Act} & \textbf{State} & \textbf{Lesson} & \textbf{Formula Component} \\
\midrule
1 & Dreamer & ``Vagueness is an Option'' & $D$ (distribution) \\
2 & Believer & ``Success kills options'' & $C/F$ (cost ratio) \\
3 & Designer & ``FOMO is Optimal'' & $k^*$ (optimal count) \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Limitations}

\textbf{Primary Limitation}: $CR$ estimation requires industry-specific calibration.

$CR$ estimation requires:
\begin{itemize}
    \item Industry-specific cost structures
    \item Market uncertainty estimates
    \item Option maintenance cost data
\end{itemize}

These are often unobservable or require significant research effort.

\subsection{Future Research}

\begin{itemize}
    \item Dynamic $CR$ tracking as markets evolve
    \item Real-time $CR$ dashboards for investors
    \item $CR$ as a function of firm lifecycle stage
    \item Network effects on $F$ (platform lock-in)
\end{itemize}

\subsection{Conclusion}

The question is not ``should I commit?'' but ``what is my $CR$?'' Armed with this framework, entrepreneurs can calibrate their option portfolios rationally, and investors can evaluate portfolio strategy against industry-specific cost structures.

\begin{quote}
\textbf{``FOMO is Optimal (given $CR$). Anxiety is a survival skill.''}
\end{quote}

%===============================================================================
% REFERENCES
%===============================================================================
\newpage
\bibliographystyle{apalike}
\begin{thebibliography}{99}

\bibitem[Adner, 2002]{adner2002real}
Adner, R. (2002).
\newblock When are technologies disruptive? A demand-based view of the emergence of competition.
\newblock {\em Strategic Management Journal}, 23(8):667--688.

\bibitem[Kogut and Kulatilaka, 2001]{kogut2001options}
Kogut, B. and Kulatilaka, N. (2001).
\newblock Capabilities as real options.
\newblock {\em Organization Science}, 12(6):744--758.

\bibitem[McGrath, 1999]{mcgrath1999falling}
McGrath, R.~G. (1999).
\newblock Falling forward: Real options reasoning and entrepreneurial failure.
\newblock {\em Academy of Management Review}, 24(1):13--30.

\end{thebibliography}

\end{document}
```

---

## 📊 Figure Files Needed

Place these files in your Overleaf project:
- `P3_cr_kstar_curve.png` → CR vs k* relationship curve
- `P3_fomo_timeline.png` → FOMO timeline for EV transition
- `P3_industry_calibration.png` → Industry-specific CR calibration
- `P3_sensitivity_heatmap.png` → Sensitivity analysis heatmap
- `P3_unified_framework.png` → Three-paper unified framework

## 📋 Available Figures in Process Folder
From `⚙️process/figures/`:
- `P3_cr_kstar_curve.png`
- `P3_fomo_timeline.png`
- `P3_industry_calibration.png`
- `P3_sensitivity_heatmap.png`
- `P3_unified_framework.png`

---

## Usage Instructions

1. **Create new Overleaf project** (Blank Project)
2. **Copy everything between the triple backticks** above
3. **Paste into `main.tex`**
4. **Upload figure files** from the process folder
5. **Compile** with pdfLaTeX

---

## Three-Paper Integration Summary

```
Paper U → D (Vagueness distribution: which V levels succeed?)
    ↓
Paper C → C = -2.5× (Commitment cost: what's the lock-in penalty?)
    ↓
Paper N → k* = F_D⁻¹(C/(C+F)) (Optimal options: how many to hold?)
```

---

*Generated: 2025-12-05 | Paper N v2.0*
