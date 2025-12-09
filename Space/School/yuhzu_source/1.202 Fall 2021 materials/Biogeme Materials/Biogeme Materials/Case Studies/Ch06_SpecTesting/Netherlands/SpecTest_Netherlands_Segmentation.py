# Tim Hillel
# Thu Mar 14 13:49:48 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.expressions import Beta, DefineVariable, log

df = pd.read_csv("netherlands.dat",'\t')
database = db.Database("netherlands",df)
pd.options.display.float_format = '{:.3g}'.format
globals().update(database.variables)


exclude = sp != 0
database.remove(exclude)


#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_CAR	 = Beta('ASC_CAR',0,None,None,0)
ASC_RAIL	 = Beta('ASC_RAIL',0,None,None,1)
BETA_COST	 = Beta('BETA_COST',0,None,None,0)
BETA_TIME_CAR	 = Beta('BETA_TIME_CAR',0,None,None,0)
BETA_TIME_RAIL	 = Beta('BETA_TIME_RAIL',0,None,None,0)

# Define here arithmetic expressions for name that are not directly available from the data
rail_time  = DefineVariable('rail_time',(  rail_ivtt   +  rail_acc_time   ) +  rail_egr_time  ,database)
car_time  = DefineVariable('car_time', car_ivtt   +  car_walk_time  ,database)

rate_G2E  = DefineVariable('rate_G2E',0.44378022,database)
car_cost_euro  = DefineVariable('car_cost_euro',car_cost * rate_G2E,database)
rail_cost_euro  = DefineVariable('rail_cost_euro', rail_cost * rate_G2E,database)

# Utilities
__Car = ASC_CAR + BETA_COST * car_cost_euro + BETA_TIME_CAR * car_time
__Rail = ASC_RAIL + BETA_COST * rail_cost_euro + BETA_TIME_RAIL * rail_time

__V = {0: __Car,1: __Rail}
__av = {0: 1,1: 1}



# Duplicate the database
database_males = db.Database("netherlands_males",pd.DataFrame.copy(database.data))
database_females = db.Database("netherlands_females",pd.DataFrame.copy(database.data))
# Remove observations
database_males.remove(gender   ==  1)
database_females.remove(gender   ==  0)
print(f"Total number of observations: {database.getNumberOfObservations()}")
print(f"Females                     : {database_females.getNumberOfObservations()}")
print(f"Males                       : {database_males.getNumberOfObservations()}")

logprob = models.loglogit(__V,__av,choice)

biogeme_full  = bio.BIOGEME(database,logprob)
biogeme_full.modelName = "SpecTest_Netherlands_fullSample"
results_full = biogeme_full.estimate()
ll_full = results_full.data.logLike

biogeme_females  = bio.BIOGEME(database_females,logprob)
biogeme_females.modelName = "SpecTest_Netherlands_females"
results_females = biogeme_females.estimate()
ll_females = results_females.data.logLike

biogeme_males  = bio.BIOGEME(database_males,logprob)
biogeme_males.modelName = "SpecTest_Netherlands_males"
results_males = biogeme_males.estimate()
ll_males = results_males.data.logLike

print(f"LL full:    {ll_full:.3f}  Parameters: {results_full.data.nparam}")
print(f"LL females: {ll_females:.3f}  Parameters: {results_females.data.nparam}")
print(f"LL males:   {ll_males:.3f}  Parameters: {results_males.data.nparam}")
unrestricted = ll_females+ll_males
print(f"Sum LL :    {unrestricted:.3f}")
lr = -2 * (ll_full - unrestricted)
print(f"likelihood ratio: {lr:.3f}")
print("Output files:")
print(f"{results_full.data.htmlFileName}")
print(f"{results_females.data.htmlFileName}")
print(f"{results_males.data.htmlFileName}")

