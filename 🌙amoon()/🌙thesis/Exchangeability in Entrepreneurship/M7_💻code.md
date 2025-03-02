#### mod.stan

```
data {

int<lower=0> n_obs;

int<lower=0> successes;

real<lower=0,upper=1> mu_phi;

real<lower=0> value_multiplier;

}

  

parameters {

real<lower=0,upper=1> phi;

}

  

model {

phi ~ beta(mu_phi * 5, (1 - mu_phi) * 5);

successes ~ binomial(n_obs, phi);

}

  

generated quantities {

real expected_value = phi * value_multiplier;

}
```
#### integ.stan
```
data {

int<lower=0> n_obs;

int<lower=0> successes;

real<lower=0,upper=1> mu_phi;

real<lower=0,upper=1> mu_theta;

real<lower=0> value_multiplier;

}

  

parameters {

real<lower=0,upper=1> phi;

real<lower=0,upper=1> theta;

}

  

model {

phi ~ beta(mu_phi * 5, (1 - mu_phi) * 5);

theta ~ beta(mu_theta * 5, (1 - mu_theta) * 5);

successes ~ binomial(n_obs, phi * theta);

}

  

generated quantities {

real expected_value = phi * theta * value_multiplier;

}
```


#### 🧮optimization

```
def test_hypothesis_1(market_model, impl_model, n_grid=20):

mu_phi_grid = np.linspace(0.1, 0.9, n_grid)

test_cases = [

{"true_phi": 0.1, "case": "Low True Value"}, # More extreme low value

{"true_phi": 0.9, "case": "High True Value"} # More extreme high value

]

results = []

for test_case in test_cases:

print(f"\nProcessing {test_case['case']}...")

for mu_phi in mu_phi_grid:

n_obs = 50 # Increased sample size

true_theta = 0.95 # Higher implementation effectiveness

# More extreme test outcomes

if test_case["case"] == "Low True Value":

market_successes = np.random.binomial(n_obs, test_case["true_phi"] * 0.8) # Pessimistic market test

impl_successes = np.random.binomial(n_obs, test_case["true_phi"] * true_theta * 1.2) # Optimistic implementation

else:

market_successes = np.random.binomial(n_obs, test_case["true_phi"] * 1.2) # Optimistic market test

impl_successes = np.random.binomial(n_obs, test_case["true_phi"] * true_theta * 0.8) # Pessimistic implementation

# Fit market test model

market_data = {

"n_obs": n_obs,

"successes": market_successes,

"mu_phi": mu_phi,

"value_multiplier": 50.0 # Increased value multiplier

}

market_fit = market_model.sample(data=market_data)

# Fit implementation test model

impl_data = {

"n_obs": n_obs,

"successes": impl_successes,

"mu_phi": mu_phi,

"mu_theta": 0.95, # Higher prior on implementation

"value_multiplier": 50.0

}

impl_fit = impl_model.sample(data=impl_data)

# Extract expected values with more extreme cost structure

market_ev = market_fit.draws_pd()['expected_value'].mean()

impl_ev = impl_fit.draws_pd()['expected_value'].mean()

# More dramatic cost difference

c_phi = 2.0 # Lower market test cost

c_phi_theta = 15.0 # Much higher implementation test cost

delta_E_phi = market_ev - c_phi

delta_E_phi_theta = impl_ev - c_phi_theta

results.append({

"case": test_case["case"],

"mu_phi": mu_phi,

"mean_delta_E_phi": delta_E_phi,

"mean_delta_E_phi_theta": delta_E_phi_theta,

"market_ev": market_ev,

"impl_ev": impl_ev

})

return pd.DataFrame(results)

  

# Usage:

mod_model = CmdStanModel(stan_file="/Users/hyunjimoon/Dropbox (MIT)/Tool4Ops4Entrep/product/program/market-model/exchangbl/scott/stan/mod.stan")

integ_model = CmdStanModel(stan_file="/Users/hyunjimoon/Dropbox (MIT)/Tool4Ops4Entrep/product/program/market-model/exchangbl/scott/stan/integ.stan")

results = test_hypothesis_1(mod_model, integ_model)

# Plot results

fig = plot_h1_results(results)

plt.show()

  
# Print summary statistics

print("\nSummary of Results:")

print(results.groupby('case')[['p_test_phi_theta']].describe())
```

