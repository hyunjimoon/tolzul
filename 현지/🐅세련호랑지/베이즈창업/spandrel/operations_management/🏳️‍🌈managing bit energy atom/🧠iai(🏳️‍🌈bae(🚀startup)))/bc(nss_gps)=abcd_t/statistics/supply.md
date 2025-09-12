```
module "atom" Supply(beta_f4) {
  transformed data {
    real nu_global = 1;
    real nu_local = 1;
    real slab_scale = 1;
    real slab_df = 100;
  }
  parameters {
    real<lower=0> tau_f4;
    real<lower=0> caux_f4;
    vector<lower=0>[366] lambda_f4;
  }
  model {
    lambda_f4 ~ student_t(nu_local, 0, 1);
    tau_f4 ~ student_t(nu_global, 0, scale_global*2);
    caux_f4 ~ inv_gamma(0.5*slab_df, 0.5*slab_df);
  }
  real c_f4 = slab_scale * sqrt(caux_f4);
  beta_f4 ~ normal(0, sqrt( c_f4^2 * square(lambda_f4) ./ (c_f4^2 + tau_f4^2*square(lambda_f4)))*tau_f4);
}

module "bit" Supply(beta_f4) {
}
```