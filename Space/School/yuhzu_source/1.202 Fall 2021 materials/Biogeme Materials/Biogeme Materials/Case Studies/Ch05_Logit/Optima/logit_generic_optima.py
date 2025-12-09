# Translated to .py by Anna Fernández
# Adapted to PandasBiogeme by Michel Bierlaire
# Sun Oct 21 23:35:54 2018
import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.expressions import Beta, DefineVariable

df = pd.read_csv("optimaDataset.dat",'\t')
database = db.Database("optimaDataset",df)
pd.options.display.float_format = '{:.3g}'.format
globals().update(database.variables)

### The condition CostCarCHF was not originally there.
exclude =  ((Choice == -1) + (  CostCarCHF   <  0  )) >0
database.remove(exclude)

#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_CAR	 = Beta('ASC_CAR',0,None,None,0)
ASC_SM	 = Beta('ASC_SM',0,None,None,0)
ASC_PT	 = Beta('ASC_PT',0,None,None,1)
BETA_COST	 = Beta('BETA_COST',0,None,None,0)
BETA_DIST_SM	 = Beta('BETA_DIST_SM',0,None,None,0)
BETA_DIST_CAR	 = Beta('BETA_DIST_CAR',0,None,None,0)
BETA_DIST	 = Beta('BETA_DIST',0,None,None,0)
BETA_TIME	 = Beta('BETA_TIME',0,None,None,0)

# Define here arithmetic expressions for name that are not directly
# available from the data


#Utilities
CAR = ASC_CAR + BETA_TIME * TimeCar + BETA_COST * CostCarCHF + BETA_DIST_CAR * distance_km
SM = ASC_SM + BETA_DIST_SM * distance_km
PT = ASC_PT + BETA_TIME * TimePT + BETA_COST * MarginalCostPT
V = {1: CAR,2: SM,0: PT}
av = {1: 1,2: 1,0: 1}


# Logit model, with availability conditions
logprob = models.loglogit(V,av,Choice)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "logit_generic_optima"
results = biogeme.estimate()
# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)
print(f"Nbr of observations: {database.getNumberOfObservations()}")
print(f"LL(0) =    {results.data.initLogLike:.3f}")
print(f"LL(beta) = {results.data.logLike:.3f}")
print(f"rho bar square = {results.data.rhoBarSquare:.3g}")
print(f"Output file: {results.data.htmlFileName}")
