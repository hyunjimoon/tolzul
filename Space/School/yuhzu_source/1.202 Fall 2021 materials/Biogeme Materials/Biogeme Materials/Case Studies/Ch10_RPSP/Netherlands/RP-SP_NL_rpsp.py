# Translated to .py by Yundi Zhang
# Jan 05 2017
# Adapted to PandasBiogeme by Michel Bierlaire
# Sun Nov  4 14:07:41 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
from biogeme.models import loglogit

pandas = pd.read_table("netherlands.dat")
database = db.Database("netherlands",pandas)
pd.options.display.float_format = '{:.3g}'.format


globals().update(database.variables)
from biogeme.expressions import *


#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_SP_CAR	 = Beta('ASC_SP_CAR',0,None,None,1)
ASC_SP_RAIL	 = Beta('ASC_SP_RAIL',0,None,None,0)
ASC_RP_CAR	 = Beta('ASC_RP_CAR',0,None,None,1)
ASC_RP_RAIL	 = Beta('ASC_RP_RAIL',0,None,None,0)
BETA_COST	 = Beta('BETA_COST',0,None,None,0)
BETA_TIME	 = Beta('BETA_TIME',0,None,None,0)
BETA_INERT	 = Beta('BETA_INERT',0,None,None,0)
THETA_SP	 = Beta('THETA_SP',1,0,None,0)

# Define here arithmetic expressions for name that are not directly available from the data
rail_time  = DefineVariable('rail_time', rail_ivtt   +  rp_rail_ovt ,database)
car_time  = DefineVariable('car_time', car_ivtt   +  rp_car_ovt  ,database)

# Utilities
SP__Car = ( ASC_SP_CAR + BETA_COST * car_cost + BETA_TIME * car_time ) * THETA_SP
SP__Rail = ( ASC_SP_RAIL + BETA_COST * rail_cost + BETA_TIME * rail_time + BETA_INERT * rp_choice ) * THETA_SP
RP__Car =  ASC_RP_CAR + BETA_COST * car_cost + BETA_TIME * car_time
RP__Rail =  ASC_RP_RAIL + BETA_COST * rail_cost + BETA_TIME * rail_time 
V = {0: RP__Car,1: RP__Rail,10: SP__Car,11: SP__Rail}
av = {0: rp,1: rp,10: sp,11: sp}

# The choice model is a logit, with availability conditions
logprob = loglogit(V,av,choice)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "RP-SP_NL_rpsp"
results = biogeme.estimate()
# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)
print(f"Nbr of observations: {database.getNumberOfObservations()}")
print(f"LL(0) =    {results.data.initLogLike:.3f}")
print(f"LL(beta) = {results.data.logLike:.3f}")
print(f"rho bar square = {results.data.rhoBarSquare:.3g}")
print(f"Output file: {results.data.htmlFileName}")


