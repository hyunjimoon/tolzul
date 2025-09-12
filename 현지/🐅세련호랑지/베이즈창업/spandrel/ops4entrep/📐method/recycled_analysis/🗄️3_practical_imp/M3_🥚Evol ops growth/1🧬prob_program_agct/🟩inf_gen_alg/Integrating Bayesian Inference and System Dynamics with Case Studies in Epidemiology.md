#### Integrating Bayesian Inference and System Dynamics with Case Studies in Epidemiology
Jair Andrade, Tom Fiddaman, Angie.H Moon (equal contributions)

This talk discusses how integrating Bayesian inference with system dynamics enables an efficient framework for robust inference on reliable dynamic models. This synergy ultimately enhances decision-making processes in various fields, including epidemiology. Our methodology involves a two-step workflow. First, we build models using system dynamics software such as Vensim. Then, we convert these models to probabilistic programs using tools like [Readsdr](https://github.com/jandraor/readsdr) and [Stanify](https://github.com/Data4DM/stanify). This translation allows dynamic modelers to incorporate Hamiltonian Monte Carlo in the inference process, which iteratively refines the models based on data and prior information.

We will present several case studies from epidemiology to illustrate the practical applications and benefits of this integrated approach. For instance, accurate estimates from population-level (reproduction number from transmission models) and within-host (immune response) structures are crucial  for formulating effective strategies to mitigate the impact of infectious diseases (e.g., COVID-19, pandemic influenza, and dengue). Our case studies demonstrate how combining system dynamics with Bayesian inference can improve decisions based on estimates by addressing the inherent uncertainties in data, model structures, and inference algorithms.

The talk will also highlight recent advancements in the Stan ecosystem that facilitate this integration, including diagram-based debugging and unit checks that reduce errors and improve model transparency. By bridging the gap between system dynamics and Bayesian inference, our approach offers a comprehensive toolkit for researchers and practitioners to develop more accurate and actionable models.

Attendees will gain insights into:

1. The workflow for integrating system dynamics and Bayesian inference using Stan.
2. Practical examples of how this integration improves model reliability in epidemiological studies.
3. The advantages of using both code-based and diagram-based representations to enhance model accuracy and transparency.
4. Future directions for expanding this methodology to other fields and improving decision support systems.

Join us to explore how the powerful combination of Stan and system dynamics can lead to more informed and effective decision-making in complex, dynamic environments.

  
![[Pasted image 20240619170813.png | center| 800]]