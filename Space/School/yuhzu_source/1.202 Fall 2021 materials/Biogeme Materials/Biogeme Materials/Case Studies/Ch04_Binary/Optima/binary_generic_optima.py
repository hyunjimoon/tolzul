# Translated to .py by Anna Fernández
# Adapted to PandasBiogeme by Michel Bierlaire
# Sun Oct 21 23:05:21 2018


import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.expressions import Beta, DefineVariable

df = pd.read_csv("optimaDataset.dat",'\t')
database = db.Database("optimaDataset",df)
pd.options.display.float_format = '{:.3g}'.format
globals().update(database.variables)

exclude =  ((Choice   ==  2 ) + (Choice == -1) + (  CostCarCHF   <=  0  )) >0
database.remove(exclude)

#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_CAR	 = Beta('ASC_CAR',0,None,None,1)
ASC_PT_SHORT	 = Beta('ASC_PT_SHORT',0,None,None,0)
ASC_PT_LONG	 = Beta('ASC_PT_LONG',0,None,None,0)
BETA_BURDEN	 = Beta('BETA_BURDEN',0,None,None,0)
BETA_COST	 = Beta('BETA_COST',0,None,None,0)
BETA_TIME	 = Beta('BETA_TIME',0,None,None,0)

# Define here arithmetic expressions for name that are not directly 
# available from the data

DistanceLessThan23  = DefineVariable('DistanceLessThan23', distance_km   <  23 ,database)
Burden  = DefineVariable('Burden',(  WalkingTimePT   +  WaitingTimePT   ) / (  NbTransf   +  1  ),database)

#Utilities
CAR = ASC_CAR + BETA_COST * CostCarCHF + BETA_TIME * TimeCar
PT = ASC_PT_SHORT * DistanceLessThan23 +  ASC_PT_LONG * (1-DistanceLessThan23) +BETA_COST * MarginalCostPT + BETA_TIME * TimePT   + BETA_BURDEN * Burden
V = {1: CAR,0: PT}
av = {1: 1,0: 1}


# Logit model, with availability conditions
logprob = models.loglogit(V,av,Choice)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "binary_generic_optima"
results = biogeme.estimate()
# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)
print(f"Nbr of observations: {database.getNumberOfObservations()}")
print(f"LL(0) =    {results.data.initLogLike:.3f}")
print(f"LL(beta) = {results.data.logLike:.3f}")
print(f"rho bar square = {results.data.rhoBarSquare:.3g}")
print(f"Output file: {results.data.htmlFileName}")


