# Translated to .py by Evanthia Kazagli
# 2017
# Adapted for PandasBiogeme by Michel Bierlaire
# Thu Nov  1 17:57:12 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
from biogeme.models import lognested, logcnl_avail
from biogeme.expressions import Beta, DefineVariable

df = pd.read_csv("swissmetro.dat",'\t')
database = db.Database("swissmetro",df)
pd.options.display.float_format = '{:.3g}'.format
globals().update(database.variables)

exclude = ((  PURPOSE   !=  1  ) * (  PURPOSE   !=  3  ) + (  CHOICE   ==  0  ) + ( AGE == 6 ))>0
database.remove(exclude)


#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed

ASC_CAR	 = Beta('ASC_CAR',0,None,None,0)
ASC_SBB	 = Beta('ASC_SBB',0,None,None,1)
ASC_SM	 = Beta('ASC_SM',0,None,None,0)
B_HE	 = Beta('B_HE',0,None,None,0)
B_COST	 = Beta('B_COST',0,None,None,0)
B_CAR_TIME	 = Beta('B_CAR_TIME',0,None,None,0)
B_SBB_TIME	 = Beta('B_SBB_TIME',0,None,None,0)
B_SM_TIME	 = Beta('B_SM_TIME',0,None,None,0)
B_SENIOR	 = Beta('B_SENIOR',0,None,None,0)
B_GA	 = Beta('B_GA',0,None,None,0)

# Nest parameters
Rail_based = Beta('Rail_based',1,1,None,0)
classic = Beta('classic',1,1,None,0)

# Alpha parameters
Rail_based_SM = Beta('Rail_based_SM',1,1e-05,1,1)
Rail_based_Train = Beta('Rail_based_Train',0.5,1e-05,1,1)#
classic_Car = Beta('classic_Car',1,1e-05,1,1)
classic_Train = 1 - Rail_based_Train #

# Define here arithmetic expressions for name that are not directly 
# available from the data
SENIOR  = DefineVariable('SENIOR', AGE   ==  5 ,database)
CAR_AV_SP  = DefineVariable('CAR_AV_SP', CAR_AV    *  (  SP   !=  0  ),database)
SM_COST  = DefineVariable('SM_COST', SM_CO   * (  GA   ==  0  ),database)
TRAIN_AV_SP  = DefineVariable('TRAIN_AV_SP', TRAIN_AV    *  (  SP   !=  0  ),database)
TRAIN_COST  = DefineVariable('TRAIN_COST', TRAIN_CO   * (  GA   ==  0  ),database)
TRAIN_TT_SCALED = DefineVariable('TRAIN_TT_SCALED',\
                                 TRAIN_TT / 100.0,database)
TRAIN_COST_SCALED = DefineVariable('TRAIN_COST_SCALED',\
                                   TRAIN_COST / 100,database)
SM_TT_SCALED = DefineVariable('SM_TT_SCALED', SM_TT / 100.0,database)
SM_COST_SCALED = DefineVariable('SM_COST_SCALED', SM_COST / 100,database)
CAR_TT_SCALED = DefineVariable('CAR_TT_SCALED', CAR_TT / 100,database)
CAR_CO_SCALED = DefineVariable('CAR_CO_SCALED', CAR_CO / 100,database)
TRAIN_HE_SCALED = DefineVariable('TRAIN_HE_SCALED', TRAIN_HE / 100,database)
SM_HE_SCALED = DefineVariable('SM_HE_SCALED', SM_HE / 100,database)

# Utilities
Car_SP = ASC_CAR + B_CAR_TIME * CAR_TT_SCALED + B_COST * CAR_CO_SCALED
SBB_SP = ASC_SBB + B_SBB_TIME * TRAIN_TT_SCALED + B_COST * TRAIN_COST_SCALED + B_HE * TRAIN_HE_SCALED + B_GA * GA
SM_SP = ASC_SM + B_SM_TIME * SM_TT_SCALED + B_COST * SM_COST_SCALED + B_HE * SM_HE_SCALED + B_GA * GA
V = {3: Car_SP,1: SBB_SP,2: SM_SP}
av = {3: CAR_AV_SP,1: TRAIN_AV_SP,2: SM_AV}

# Definition of nests
alpha_Rail_based = {1: Rail_based_Train, 2: Rail_based_SM, 3: 0}
alpha_classic = {1: classic_Train, 2: 0, 3: classic_Car}

nest_Rail_based = Rail_based, alpha_Rail_based
nest_classic = classic, alpha_classic

nests = nest_Rail_based, nest_classic

# CNL (Cross-Nested Logit Model), with availability conditions
logprob = logcnl_avail(V, av, nests, CHOICE)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "MEV_SM_CNL_fix"
results = biogeme.estimate()

# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)
print(f"Nbr of observations: {database.getNumberOfObservations()}")
print(f"LL(0) =    {results.data.initLogLike:.3f}")
print(f"LL(beta) = {results.data.logLike:.3f}")
print(f"rho bar square = {results.data.rhoBarSquare:.3g}")
print(f"Output file: {results.data.htmlFileName}")
