![[📜andrew24_federated_learning 2025-04-17-14.svg]]
%%[[📜andrew24_federated_learning 2025-04-17-14.md|🖋 Edit in Excalidraw]]%%

[[📜ackerman19_computbl_cond_prob]]


## 🗄️1: Table of Contents (Question-Answer Format)

|Section/Subsection|Question|Answer|🧱Literature Brick|
|---|---|---|---|
|1. Introduction|How can federated learning be reframed as a distributed inference problem?|🧭 Federated learning can be reformulated as a variational inference problem where the goal is to find a global variational posterior that approximates the true posterior, enabling a probabilistic message-passing approach through expectation propagation between server and clients|• McMahan et al. (2017) on canonical formulation of FL as distributed optimization<br>• Al-Shedivat et al. (2021) on Bayesian formulation of FL<br>• Minka (2001) on expectation propagation|
|2. Federated Learning with Expectation Propagation|How can expectation propagation be applied to federated learning?|🧍‍♀️ Each client performs local inference to update its contribution to the global posterior through probabilistic message-passing, where the cavity distribution summarizes the effect of all other clients, enabling efficient distributed inference|• Classic EP literature (Minka, 2001)<br>• Variational inference on streaming/partitioned data (Broderick et al., 2013; Vehtari et al., 2020)|
|3. Scalable Expectation Propagation|What techniques enable scalable expectation propagation for modern federated learning?|🧭 Scalability is achieved through: (1) mean-field Gaussian variational families, (2) diverse approximate client inference techniques, (3) adaptive optimization via damping, and (4) stateless client support with stochastic expectation propagation|• Mean-field Gaussian literature (Graves, 2011; Blundell et al., 2015)<br>• SG-MCMC (Welling & Teh, 2011)<br>• Natural gradient VI (Zhang et al., 2018)|
|4. Experiments|How does FedEP perform compared to existing federated learning approaches?|🌏 FedEP outperforms both FedAvg and FedPA baselines in terms of convergence speed and accuracy across benchmark tasks, with even the simplest scaled-identity covariance approximation showing strong performance|• Benchmark datasets and models from Reddi et al. (2020)<br>• Comparison with FedAvg and FedPA (Al-Shedivat et al., 2021)|
|5. Analysis and Discussion|What factors influence FedEP performance and what are its limitations?|🗺️ Simpler approximations (like scaled identity) perform surprisingly well for large models as covariance estimation becomes difficult in high dimensions; FedEP provides better calibration but has increased memory requirements for stateful clients|• Model uncertainty literature (Guo et al., 2017)<br>• Convergence guarantees literature (Li et al., 2018, 2020b)|

## 🗄️2: Comparison with Existing Theories

|Aspect|FedAvg|FedPA|FedEP|
|---|---|---|---|
|**Theoretical Foundation**|Distributed optimization|Distributed inference|Iterative probabilistic message-passing|
|**Client Computation**|Local SGD steps|Independent local posterior inference|Local inference conditioned on global posterior|
|**Communication Pattern**|Parameter averaging|Posterior parameter aggregation|Iterative refinement through distributed EP|
|**Client Context**|No global context during updates|No global context during inference|Uses current global posterior for local inference|
|**Client Coupling**|Clients coupled only through server averaging|Clients coupled only through posterior aggregation|Clients iteratively influence each other's posteriors|
|**Robustness to Heterogeneity**|Degrades with data heterogeneity|Better handling of heterogeneity than FedAvg|Further improved handling of heterogeneity|
|**Handling Uncertainty**|Point estimates only|Captures parameter uncertainty|Captures parameter uncertainty with calibration|
|**Memory Requirements**|Low (model parameters only)|Low (model parameters only)|Higher for stateful variant (local distribution parameters)|
|**Theoretical Guarantees**|Convergence guarantees under specific conditions|Limited theoretical analysis|Open problem for EP-based approaches|

## 🗄️3: Practical Implications

|Domain|Implication|Example Application|
|---|---|---|
|**Heterogeneous Federated Systems**|Improved convergence in systems with non-IID data distribution|Healthcare applications where patient data varies significantly across hospitals or regions|
|**Privacy-Preserving ML**|Compatible with secure aggregation for enhanced privacy guarantees|Financial institutions collaboratively training models while maintaining client confidentiality|
|**Probabilistic Decision Making**|Better uncertainty quantification through posterior approximation|Medical diagnosis systems providing confidence intervals with predictions|
|**Resource-Constrained Environments**|Flexible inference techniques that can adapt to client capabilities|IoT deployments with varying computational resources across devices|
|**Adaptable Training Systems**|Reduced communication rounds through faster convergence|Mobile device networks with expensive or unreliable communication channels|
|**System Calibration**|Improved expected calibration error compared to point estimate methods|Risk assessment applications requiring well-calibrated probability estimates|
|**Hybrid Architectures**|Ability to combine optimization-based and inference-based approaches|Systems that transition from FedAvg to FedEP during training for better convergence|

## 🖼️1: Need-Solution Mapping

![Need-Solution Mapping](data:image/svg+xml;base64,<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">

<!-- Background --> <rect width="800" height="600" fill="#f8f9fa" /> <!-- Title -->

<text x="400" y="40" font-family="Arial" font-size="24" font-weight="bold" text-anchor="middle">Federated Learning as Variational Inference</text>

<!-- Problem (💜) --> <rect x="80" y="80" width="300" height="180" rx="10" fill="#f0e6ff" stroke="#9370db" stroke-width="2" /> <text x="230" y="110" font-family="Arial" font-size="18" font-weight="bold" text-anchor="middle" fill="#4b0082">Problem (💜)</text> <text x="230" y="145" font-family="Arial" font-size="14" text-anchor="middle">Standard federated learning (FedAvg):</text> <text x="230" y="175" font-family="Arial" font-size="14" text-anchor="middle">• Suffers from client data heterogeneity</text> <text x="230" y="205" font-family="Arial" font-size="14" text-anchor="middle">• Ignores parameter uncertainty</text> <text x="230" y="235" font-family="Arial" font-size="14" text-anchor="middle">• Independent client updates fail to</text> <text x="230" y="255" font-family="Arial" font-size="14" text-anchor="middle"> account for global context</text> <!-- Solution (💚) --> <rect x="420" y="80" width="300" height="180" rx="10" fill="#e6ffe6" stroke="#4caf50" stroke-width="2" /> <text x="570" y="110" font-family="Arial" font-size="18" font-weight="bold" text-anchor="middle" fill="#008000">Solution (💚)</text> <text x="570" y="145" font-family="Arial" font-size="14" text-anchor="middle">Federated Learning with EP (FedEP):</text> <text x="570" y="175" font-family="Arial" font-size="14" text-anchor="middle">• Reformulates FL as variational inference</text> <text x="570" y="205" font-family="Arial" font-size="14" text-anchor="middle">• Uses iterative probabilistic message-passing</text> <text x="570" y="235" font-family="Arial" font-size="14" text-anchor="middle">• Conditions client inference on global</text> <text x="570" y="255" font-family="Arial" font-size="14" text-anchor="middle"> posterior approximation</text> <!-- Arrow connecting problem and solution --> <path d="M 380 170 L 420 170" stroke="#000000" stroke-width="2" fill="none" marker-end="url(#arrowhead)" /> <defs> <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"> <polygon points="0 0, 10 3.5, 0 7" /> </marker> </defs> <!-- Methodology Visualization --> <rect x="80" y="290" width="640" height="280" rx="10" fill="#ffffff" stroke="#cccccc" stroke-width="2" /> <text x="400" y="320" font-family="Arial" font-size="18" font-weight="bold" text-anchor="middle">Expectation Propagation Message Passing Framework</text> <!-- Server --> <rect x="340" y="340" width="120" height="60" rx="5" fill="#e3f2fd" stroke="#2196f3" stroke-width="2" /> <text x="400" y="375" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Server</text> <!-- Clients --> <rect x="140" y="450" width="100" height="50" rx="5" fill="#e8f5e9" stroke="#4caf50" stroke-width="2" /> <text x="190" y="480" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Client 1</text> <rect x="280" y="450" width="100" height="50" rx="5" fill="#e8f5e9" stroke="#4caf50" stroke-width="2" /> <text x="330" y="480" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Client 2</text> <rect x="420" y="450" width="100" height="50" rx="5" fill="#e8f5e9" stroke="#4caf50" stroke-width="2" /> <text x="470" y="480" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Client 3</text> <rect x="560" y="450" width="100" height="50" rx="5" fill="#e8f5e9" stroke="#4caf50" stroke-width="2" /> <text x="610" y="480" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Client K</text> <!-- Messages --> <path d="M 190 450 L 345 400" stroke="#ff9800" stroke-width="2" fill="none" marker-end="url(#messagehead)" /> <path d="M 330 450 L 370 400" stroke="#ff9800" stroke-width="2" fill="none" marker-end="url(#messagehead)" /> <path d="M 470 450 L 430 400" stroke="#ff9800" stroke-width="2" fill="none" marker-end="url(#messagehead)" /> <path d="M 610 450 L 455 400" stroke="#ff9800" stroke-width="2" fill="none" marker-end="url(#messagehead)" /> <path d="M 355 400 L 200 450" stroke="#673ab7" stroke-width="2" fill="none" marker-end="url(#messagehead2)" /> <path d="M 375 400 L 335 450" stroke="#673ab7" stroke-width="2" fill="none" marker-end="url(#messagehead2)" /> <path d="M 425 400 L 465 450" stroke="#673ab7" stroke-width="2" fill="none" marker-end="url(#messagehead2)" /> <path d="M 445 400 L 600 450" stroke="#673ab7" stroke-width="2" fill="none" marker-end="url(#messagehead2)" />

<text x="260" y="410" font-family="Arial" font-size="12" text-anchor="middle" fill="#ff9800">Client updates (Δqk)</text> <text x="540" y="410" font-family="Arial" font-size="12" text-anchor="middle" fill="#673ab7">Global posterior (qglobal)</text>

<!-- Ellipsis -->

<text x="520" y="480" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">...</text>

<defs> <marker id="messagehead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"> <polygon points="0 0, 10 3.5, 0 7" fill="#ff9800" /> </marker> <marker id="messagehead2" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"> <polygon points="0 0, 10 3.5, 0 7" fill="#673ab7" /> </marker> </defs> </svg>)

## 🖼️2: Methodology Visualization

![Methodology Visualization](data:image/svg+xml;base64,<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">

<!-- Background --> <rect width="800" height="600" fill="#f8f9fa" /> <!-- Title -->

<text x="400" y="40" font-family="Arial" font-size="24" font-weight="bold" text-anchor="middle">Efficiency-Accuracy Tradeoffs in FedEP</text>

<!-- FedEP Algorithmic Considerations --> <rect x="80" y="70" width="640" height="240" rx="10" fill="#ffffff" stroke="#cccccc" stroke-width="2" /> <text x="400" y="100" font-family="Arial" font-size="18" font-weight="bold" text-anchor="middle">Approximate Inference Techniques in FedEP</text> <!-- Comparison Table --> <rect x="110" y="120" width="580" height="170" fill="#ffffff" stroke="#dddddd" stroke-width="1" /> <!-- Table Headers --> <rect x="110" y="120" width="190" height="30" fill="#f5f5f5" stroke="#dddddd" stroke-width="1" /> <rect x="300" y="120" width="130" height="30" fill="#f5f5f5" stroke="#dddddd" stroke-width="1" /> <rect x="430" y="120" width="130" height="30" fill="#f5f5f5" stroke="#dddddd" stroke-width="1" /> <rect x="560" y="120" width="130" height="30" fill="#f5f5f5" stroke="#dddddd" stroke-width="1" />

<text x="200" y="140" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Method</text> <text x="365" y="140" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Computation</text> <text x="495" y="140" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Communication</text> <text x="625" y="140" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Performance</text>

<!-- Row 1 --> <rect x="110" y="150" width="190" height="35" fill="#ffffff" stroke="#dddddd" stroke-width="1" /> <rect x="300" y="150" width="130" height="35" fill="#e3f2fd" stroke="#dddddd" stroke-width="1" /> <rect x="430" y="150" width="130" height="35" fill="#e8f5e9" stroke="#dddddd" stroke-width="1" /> <rect x="560" y="150" width="130" height="35" fill="#ede7f6" stroke="#dddddd" stroke-width="1" />

<text x="200" y="172" font-family="Arial" font-size="12" text-anchor="middle">Scaled Identity Covariance</text> <text x="365" y="172" font-family="Arial" font-size="12" text-anchor="middle">Very Low</text> <text x="495" y="172" font-family="Arial" font-size="12" text-anchor="middle">Low</text> <text x="625" y="172" font-family="Arial" font-size="12" text-anchor="middle">High</text>

<!-- Row 2 --> <rect x="110" y="185" width="190" height="35" fill="#ffffff" stroke="#dddddd" stroke-width="1" /> <rect x="300" y="185" width="130" height="35" fill="#e3f2fd" stroke="#dddddd" stroke-width="1" /> <rect x="430" y="185" width="130" height="35" fill="#ffecb3" stroke="#dddddd" stroke-width="1" /> <rect x="560" y="185" width="130" height="35" fill="#e8f5e9" stroke="#dddddd" stroke-width="1" />

<text x="200" y="207" font-family="Arial" font-size="12" text-anchor="middle">SG-MCMC</text> <text x="365" y="207" font-family="Arial" font-size="12" text-anchor="middle">Low</text> <text x="495" y="207" font-family="Arial" font-size="12" text-anchor="middle">Medium</text> <text x="625" y="207" font-family="Arial" font-size="12" text-anchor="middle">High</text>

<!-- Row 3 --> <rect x="110" y="220" width="190" height="35" fill="#ffffff" stroke="#dddddd" stroke-width="1" /> <rect x="300" y="220" width="130" height="35" fill="#ffecb3" stroke="#dddddd" stroke-width="1" /> <rect x="430" y="220" width="130" height="35" fill="#ffecb3" stroke="#dddddd" stroke-width="1" /> <rect x="560" y="220" width="130" height="35" fill="#ede7f6" stroke="#dddddd" stroke-width="1" />

<text x="200" y="242" font-family="Arial" font-size="12" text-anchor="middle">Laplace Approximation</text> <text x="365" y="242" font-family="Arial" font-size="12" text-anchor="middle">Medium</text> <text x="495" y="242" font-family="Arial" font-size="12" text-anchor="middle">Medium</text> <text x="625" y="242" font-family="Arial" font-size="12" text-anchor="middle">Medium</text>

<!-- Row 4 --> <rect x="110" y="255" width="190" height="35" fill="#ffffff" stroke="#dddddd" stroke-width="1" /> <rect x="300" y="255" width="130" height="35" fill="#ffcdd2" stroke="#dddddd" stroke-width="1" /> <rect x="430" y="255" width="130" height="35" fill="#ffecb3" stroke="#dddddd" stroke-width="1" /> <rect x="560" y="255" width="130" height="35" fill="#e8f5e9" stroke="#dddddd" stroke-width="1" />

<text x="200" y="277" font-family="Arial" font-size="12" text-anchor="middle">Natural Gradient VI</text> <text x="365" y="277" font-family="Arial" font-size="12" text-anchor="middle">High</text> <text x="495" y="277" font-family="Arial" font-size="12" text-anchor="middle">Medium</text> <text x="625" y="277" font-family="Arial" font-size="12" text-anchor="middle">High</text>

<!-- Tradeoff Graph --> <rect x="80" y="330" width="640" height="240" rx="10" fill="#ffffff" stroke="#cccccc" stroke-width="2" /> <text x="400" y="360" font-family="Arial" font-size="18" font-weight="bold" text-anchor="middle">Efficient-Accuracy Tradeoff in FedEP</text> <!-- Axes --> <line x1="150" y1="510" x2="650" y2="510" stroke="#000000" stroke-width="2" /> <line x1="150" y1="510" x2="150" y2="390" stroke="#000000" stroke-width="2" /> <!-- Axis Labels -->

<text x="400" y="540" font-family="Arial" font-size="14" text-anchor="middle">Model Size / Client Heterogeneity</text> <text x="105" y="450" font-family="Arial" font-size="14" text-anchor="middle" transform="rotate(-90, 105, 450)">Performance Gain</text>

<!-- Small Model Curve --> <path d="M 150 510 Q 250 450, 400 410 T 650 390" stroke="#3f51b5" stroke-width="3" fill="none" /> <text x="500" y="405" font-family="Arial" font-size="12" fill="#3f51b5">Small Model: Advanced Methods > Simple Methods</text> <!-- Large Model Curve --> <path d="M 150 510 Q 250 490, 400 470 T 650 460" stroke="#e91e63" stroke-width="3" fill="none" /> <text x="500" y="460" font-family="Arial" font-size="12" fill="#e91e63">Large Model: All Methods Similar Performance</text> <!-- Key Insight --> <rect x="160" y="390" width="480" height="40" rx="5" fill="#fff8e1" stroke="#ffc107" stroke-width="1" /> <text x="400" y="415" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle">Key Insight: As model complexity increases, simple methods (scaled identity) approach</text> <text x="400" y="430" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle">the performance of more advanced methods due to challenges in covariance estimation</text> </svg>)

## Additional Key Resources

### Key Insights from the Paper:

1. **Theoretical Connection**: FedEP provides a principled extension of FedPA by accounting for the current global approximation during client inference, leading to better performance with the same computational complexity.
    
2. **Scalability Techniques**: The paper introduces multiple techniques to scale expectation propagation to modern federated learning, including efficient variational families, approximate inference methods, and adaptive optimization.
    
3. **Surprising Effectiveness of Simple Techniques**: For large models, simple approximations like scaled identity covariance perform surprisingly well, which has important implications for practical implementations.
    
4. **Improved Calibration**: FedEP and FedSEP improve both accuracy and expected calibration error, with marginalization over the approximate posterior further enhancing calibration.
    
5. **Stateless Extension**: The stochastic expectation propagation variant (FedSEP) enables a stateless implementation that reduces client memory requirements while maintaining most of the performance benefits.
    

## Conclusion

This analysis shows that reframing federated learning as a variational inference problem with expectation propagation offers significant advantages over traditional distributed optimization approaches. The FedEP framework improves convergence speed and accuracy by enabling iterative refinement of the global posterior through probabilistic message-passing between clients and the server.

The paper makes important contributions to scaling expectation propagation to realistic federated learning scenarios with large models and numerous clients. Particularly noteworthy is the finding that simple approximations like scaled identity covariance perform remarkably well on large models, which has important implications for practical deployments of federated learning systems.

FedEP represents a promising direction for federated learning research that combines the computational efficiency of distributed optimization approaches with the uncertainty quantification benefits of Bayesian methods.