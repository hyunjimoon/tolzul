```
module "fast" IndustryClockspeed {
  parameters {
    vector[2*J_f2] beta_f2;       // the basis functions coefficients for f2
    real<lower=0> lengthscale_f2; //
    real<lower=0> sigma_f2;       // scale of f2
  }
  transformed parameters {
    vector[2*J_f2] diagSPD_f2 = diagSPD_periodic(sigma_f2, lengthscale_f2, J_f2);
  }
  BasisTransform() {
    real period_year = 365.25/xsd;
    matrix[N,2*J_f2] PHI_f2 = PHI_periodic(N, J_f2, 2*pi()/period_year, xn);
    return PHI_f2;
  }
  BasisLength() {
    return 2*J_f2;
  }
  Weights() {
    lengthscale_f2 ~ normal(0, .1);
    sigma_f2 ~ normal(0, 1);
    beta_f2 ~ normal(0, 1);
    return diagSPD_f2 .* beta_f2;
  }
  OriginalScaleFunction() {
    return (PHI_f2 * (diagSPD_f2 .* beta_f2));
  }
}

module "slow" IndustryClockspeed {
  BasisTransform() {
    return rep_matrix(0, N, 0);
  }
  BasisLength() {
    return 0;
  }
  Weights() {
    return rep_vector(0, 0);
  }
  OriginalScaleFunction() {
    return rep_vector(0, N);
  }
}
```
