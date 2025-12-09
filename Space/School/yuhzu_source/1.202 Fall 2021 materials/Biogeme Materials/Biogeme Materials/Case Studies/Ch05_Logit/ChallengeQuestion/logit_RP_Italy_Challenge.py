# Michel Bierlaire, EPFL
#
# Translated to .py by Jing Ding-Mastera
#
# Adapted to PandasBiogeme by Michel Bierlaire
# Tue Oct 23 16:12:40 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.expressions import Beta, DefineVariable

df = pd.read_csv("italy.dat",'\t')
database = db.Database("italy",df)
pd.options.display.float_format = '{:.3g}'.format
globals().update(database.variables)


exclude = sp > 0
database.remove(exclude)

#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_car	 = Beta('ASC_car',0,None,None,0)
ASC_train	 = Beta('ASC_train',0,None,None,0)
B_cost	 = Beta('B_cost',0,None,None,0)
B_Veh_time	 = Beta('B_Veh_time',0,None,None,0)
B_Wal_time	 = Beta('B_Wal_time',0,None,None,0)
B_nb_car	 = Beta('B_nb_car',0,None,None,0)

# Define here arithmetic expressions for name that are not directly available from the data

nb_car  = DefineVariable('nb_car',car_lic * 10 * (  ch   ==  2  ),database)

# Utilities
TrainRP = ASC_train + B_Veh_time * tt_t + B_Wal_time * wt_t + B_cost * c_t
CarRP = ASC_car + B_Veh_time * tt_c + B_Wal_time * wt_c + B_cost * c_c + B_nb_car * nb_car
BusRP = B_Veh_time * tt_b + B_Wal_time * wt_b + B_cost * c_b

V = {1: TrainRP,2: CarRP,3: BusRP}
av = {1: av1,2: av2,3: av3}

# The choice model is a logit, with availability conditions
logprob = models.loglogit(V,av,ch)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "logit_RP_Italy_Challenge"
results = biogeme.estimate()
# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)
print(f"Nbr of observations: {database.getNumberOfObservations()}")
print(f"LL(0) =    {results.data.initLogLike:.3f}")
print(f"LL(beta) = {results.data.logLike:.3f}")
print(f"rho bar square = {results.data.rhoBarSquare:.3g}")
print(f"Output file: {results.data.htmlFileName}")
