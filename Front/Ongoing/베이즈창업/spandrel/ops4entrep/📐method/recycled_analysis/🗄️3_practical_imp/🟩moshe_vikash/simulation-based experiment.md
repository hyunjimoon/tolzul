---
tags:
  - vikash
---

### andrew
_Simulation-based experimentation._ Data analysis can be expensive in time and effort, and this can lead to us thinking that if a project took a lot of work then it has to be good. To state that belief is to mock it, yet it persists.

How can we avoid what might be called the “fallacy of effort”? We recommend simulation-based experimentation, which requires the following steps: (1) create a fake world, (2) simulate parameters and data from this world, (3) analyze the simulated data and get inference for the underlying parameters, (4) compare those inferences to the parameter values simulated in step 2. This can be done systematically in a Bayesian context (Modrák et al., 2024) but in practice informal checking can work just fine, in that problems will often show up in a simple simulation.

Creating a fake world is not easy—if analyzing a dataset is like playing Sim City, simulating fake data is like writing Sim City—but this effort can be well worth it, not just for the benefit of uncovering problems and the increased confidence arising from successful recovery, but also because constructing a simulation experiment is a way to clarify our thinking. Indeed, we often recommend simulating fake data before embarking on any real-world data collection process, to get a sense of what can realistically be learned from a proposed design.

- statistical theory will be mostly about gaining a deep understanding of simulation as profitable abstraction of counter-factually repeatable phenomenon" from [here]()