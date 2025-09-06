
```
module "up" IndustryTrend {
  parameters {
    vector[M_f1] beta_f1;         // the basis functions coefficients
    real<lower=0> lengthscale_f1; // lengthscale of f1
    real<lower=0> sigma_f1;       // scale of f1
  }
  transformed parameters {
    vector[M_f1] diagSPD_f1 = diagSPD_EQ(sigma_f1, lengthscale_f1, L_f1, M_f1);
  }
  BasisTransform() {
    real L_f1 = c_f1*max(xn);
    matrix[N,M_f1] PHI_f1 = PHI_EQ(N, M_f1, L_f1, xn);
    return PHI_f1;
  }
  BasisLength() {
    return M_f1;
  }
  Weights() {
    lengthscale_f1 ~ lognormal(log(700/xsd), 1);
    // This is (0, 1) in some original versions
    sigma_f1 ~ normal(0, .5);
    beta_f1 ~ normal(0, 1);
    return diagSPD_f1 .* beta_f1;
  }
  OriginalScaleFunction() {
    return (intercept_offset + PHI_f1 * (diagSPD_f1 .* beta_f1));
  }
}

module "down" IndustryTrend {
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