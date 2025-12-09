# Translated to .py by Yundi Zhang
# Jan 2017
# Adapted to PandasBiogeme by Michel Bierlaire
# Sun Oct 21 23:01:50 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.expressions import Beta, DefineVariable

df = pd.read_csv("netherlands.dat",'\t')
database = db.Database("netherlands",df)
pd.options.display.float_format = '{:.3g}'.format
globals().update(database.variables)

exclude = sp != 0
database.remove(exclude)


# Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_CAR_MALE		 = Beta('ASC_CAR_MALE',0,None,None,0)
ASC_CAR_FEMALE		 = Beta('ASC_CAR_FEMALE',0,None,None,0)
BETA_COST_MALE	 = Beta('BETA_COST_MALE',0,None,None,0)
BETA_COST_FEMALE	 = Beta('BETA_COST_FEMALE',0,None,None,0)
BETA_TT_CAR_MALE	 = Beta('BETA_TT_CAR_MALE',0,None,None,0)
BETA_TT_CAR_FEMALE	 = Beta('BETA_TT_CAR_FEMALE',0,None,None,0)
BETA_TT_RAIL_MALE = Beta('BETA_TT_RAIL_MALE',0,None,None,0)
BETA_TT_RAIL_FEMALE = Beta('BETA_TT_RAIL_FEMALE',0,None,None,0)

# Define here arithmetic expressions for name that are not directly available from the data
rail_time  = DefineVariable('rail_time',(  rail_ivtt   +  rail_acc_time   ) +  rail_egr_time  ,database)
car_time  = DefineVariable('car_time', car_ivtt   +  car_walk_time  ,database)
rate_G2E = DefineVariable('rate_G2E', 0.44378022,database)
car_cost_euro = DefineVariable('car_cost_euro', car_cost * rate_G2E,database)
rail_cost_euro = DefineVariable('rail_cost_euro', rail_cost * rate_G2E,database)
female = DefineVariable('female', gender == 1,database)
male = DefineVariable('male', gender == 0,database)


# Utilities
__Car_male = ASC_CAR_MALE + BETA_COST_MALE * car_cost_euro + BETA_TT_CAR_MALE * car_time
__Car_female = ASC_CAR_FEMALE + BETA_COST_FEMALE * car_cost_euro + BETA_TT_CAR_FEMALE * car_time
__Car = __Car_male * male + __Car_female * female

__Rail_male =  BETA_COST_MALE * rail_cost_euro + BETA_TT_RAIL_MALE * rail_time 
__Rail_female =  BETA_COST_FEMALE * rail_cost_euro + BETA_TT_RAIL_FEMALE * rail_time
__Rail = __Rail_male * male + __Rail_female * female

__V = {0: __Car,1: __Rail}
__av = {0: 1,1: 1}

# The choice model is a logit, with availability conditions
logprob = models.loglogit(__V,__av,choice)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "binary_socio_econ_netherlands"
results = biogeme.estimate()
# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)
print(f"Nbr of observations: {database.getNumberOfObservations()}")
print(f"LL(0) =    {results.data.initLogLike:.3f}")
print(f"LL(beta) = {results.data.logLike:.3f}")
print(f"rho bar square = {results.data.rhoBarSquare:.3g}")
print(f"Output file: {results.data.htmlFileName}")
