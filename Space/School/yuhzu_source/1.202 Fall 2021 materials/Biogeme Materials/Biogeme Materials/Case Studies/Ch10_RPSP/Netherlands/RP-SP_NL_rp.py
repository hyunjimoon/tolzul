# Translated to .py by Yundi Zhang
# Jan 05 2017
# Adapted to PandasBiogeme by Michel Bierlaire
# Sun Nov  4 14:03:17 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
from biogeme.models import loglogit

pandas = pd.read_table("netherlands.dat")
database = db.Database("netherlands",pandas)
pd.options.display.float_format = '{:.3g}'.format


globals().update(database.variables)
from biogeme.expressions import *

exclude = sp != 0
database.remove(exclude)


#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_RP_CAR	 = Beta('ASC_RP_CAR',0,None,None,1)
ASC_RP_RAIL	 = Beta('ASC_RP_RAIL',0,None,None,0)
BETA_COST	 = Beta('BETA_COST',0,None,None,0)
BETA_TIME	 = Beta('BETA_TIME',0,None,None,0)

# Define here arithmetic expressions for name that are not directly available from the data
rail_time  = DefineVariable('rail_time', rail_ivtt   +  rp_rail_ovt ,database)
car_time  = DefineVariable('car_time', car_ivtt   +  rp_car_ovt ,database )

# Utilities
Car = ASC_RP_CAR + BETA_COST * car_cost + BETA_TIME * car_time
Rail = ASC_RP_RAIL + BETA_COST * rail_cost + BETA_TIME * rail_time
V = {0: Car,1: Rail}
av = {0: rp,1: rp}

# The choice model is a logit, with availability conditions
logprob = loglogit(V,av,choice)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "RP-SP_NL_rp"
results = biogeme.estimate()
# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)
print(f"Nbr of observations: {database.getNumberOfObservations()}")
print(f"LL(0) =    {results.data.initLogLike:.3f}")
print(f"LL(beta) = {results.data.logLike:.3f}")
print(f"rho bar square = {results.data.rhoBarSquare:.3g}")
print(f"Output file: {results.data.htmlFileName}")


