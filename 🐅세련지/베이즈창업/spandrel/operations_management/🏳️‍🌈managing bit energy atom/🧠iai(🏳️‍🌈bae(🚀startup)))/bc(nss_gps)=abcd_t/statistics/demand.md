```
module "customer_behavior" Demand(beta_f4) {
  parameters {
    real<lower=0> sigma_f4;
  }
  model {
    sigma_f4 ~ normal(0, 0.1);
  }
  beta_f4 ~ normal(0, sigma_f4);
}

module "customer" Demand(beta_f4) {
}
```