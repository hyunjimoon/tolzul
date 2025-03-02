# Module 2: 🟰 4-Step Optimization Formulation

1. Basic formulation with utilities

2. First approximation using empirical distributions

3. Second approximation comparing true vs estimated probabilities

4. Final decision framework with delta EU comparisons

specifically

1. Basic formulation:

```

argmax_{a \in \{a, a_\phi, a_{\phi\theta}\}} \{EU_1 - EU_0 - C(a)\}

```

2. First approximation (with empirical distributions):

```

argmax \sum \color{brown}{U}(\color{green}{\phi}, \color{red}{\theta}) \cdot \color{blue}{\hat{P}}(\color{green}{\phi}\color{red}{\theta}|\color{purple}{D(a)}) - \sum \color{brown}{U}(\color{green}{\phi}, \color{red}{\theta}) \cdot \color{blue}{\hat{P}}

```

1. Second approximation (true vs estimated):

```

argmax \sum \color{brown}{U}(\cdot)\color{blue}{P} - \sum \color{brown}{U}(\cdot)\color{blue}{\hat{P}} - C(a)

```

2. Final decision framework:

```

argmax\{\Delta EU_0, \Delta EU_1, \Delta EU_2\}

```