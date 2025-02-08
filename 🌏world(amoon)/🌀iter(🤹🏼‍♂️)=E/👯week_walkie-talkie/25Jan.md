
2025-01-24 Jeff

For "Decoding Venture Capital Decisions":

1. Data and Methods:
- Need to collect VC content from: Peter Thiel (Zero to One book), Bill Gurley (blog posts), Paul Graham, Mark Andreessen (P-Market blog archive)
- Already have experimental design grid with sectors, venture stage, team characteristics, traction indicators
- Using GPT for generating company descriptions and embedding analysis
- Plan to validate stimuli and run estimation routine

2. Key Research Direction:
- Hypothesis: The more VCs understand technology, the less value they assign to patents
- Framework maps observable startup characteristics → perceptual dimensions → investment decisions
- Need to explore relationship between patents and founding team characteristics

3. Implementation Next Steps:
- Collect and format VC content as text/PDF for LLM input
- Validate design grid including IP/patent features
- Run hierarchical multinomial logit model after data collection
- Use CDL (Creative Destruction Lab) data for validation

For "Venturing into Complexity":

1. Theoretical Framework:
- Focus on computational irreducibility vs "pockets of reducibility" 
- Individual startup trajectories are irreducible but patterns emerge across firms
- Connection to Bayesian calibration theory (Andrew's theorem 2)
- Hierarchical model allows partial exchangeability

2. Data Sources:
- TechStars accelerator data (tracking initial conditions and outcomes)
- CDL data showing granular mentor-startup interactions
- MIT delta V cohort data with Crunchbase/LinkedIn tracking

3. Research Direction:
- Study how startups sequence activities (analysis, experimentation, implementation)
- Identify systematic patterns while acknowledging individual unpredictability
- Use hierarchical models to find "pockets of reducibility" across ventures


2025-01-14 Jeff

# 🗄️👁️🧠🤜table BSA                
Belief/Observation → Understanding → State → Judging → Action

| Component              | Definition                                                     | Mathematical Representation                             | Example from Patent/Investment Context                                                                                                                                                                 |
| ---------------------- | -------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 👁️ Belief/Observation | Raw information or data perceived from environment             | O = {o₁, o₂, ..., oₙ} where oᵢ are observable features  | From transcript: "Those who understand IT and how this works don't give much value to patents" - Raw observation of technical experts' view of patents                                                 |
| Understanding          | Interpretation layer that maps observations to internal states | U: O → S (mapping from observations to internal states) | From transcript: How investors make sense of patents varies based on their understanding of technology - some see it as valuable signal, others as mere formality                                      |
| 🧠 State               | Internal representation of knowledge/understanding             | S = {s₁, s₂, ..., sₘ} where sᵢ are latent states        | From transcript: Jeff discusses how different investors have different mental models about patent value - some believe patents indicate technological capability, others see them as less meaningful   |
| Judging                | Decision function that converts states to actions              | J: S → A (mapping from states to actions)               | From transcript: Investors evaluate investment decisions differently based on their state of belief about patents' value - technical experts may discount patents while others may see them as crucial |
| 🤜 Action              | Observable behavior or choice                                  | A = {a₁, a₂, ..., aₖ} where aᵢ are possible actions     | From transcript: Investment decisions - whether to invest in companies based on their patent portfolio, with different actions emerging from different sense-making processes                          |

