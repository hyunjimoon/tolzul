# Translated to .py by Meritxell Pacheco (December 2016)
########################################################
# Updated by Evanthia Kazagli (January 2017)
########################################################
# Updated by Peiyu Jing (April 2019)
########################################################

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.draws as draws
import biogeme.models as models

pandas = pd.read_table("swissmetro.dat")
database = db.Database("swissmetro",pandas)

# The Pandas data structure is available as database.data. Use all the
# Pandas functions to invesigate the database
#print(database.data.describe())

globals().update(database.variables)

#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_CAR = Beta('ASC_CAR',0,-10,10,0)
ASC_SBB = Beta('ASC_SBB',0,-10,10,1)
ASC_SM = Beta('ASC_SM',0,-10,10,0)
BETA_CAR_COST_mean = Beta('BETA_CAR_COST_mean',0,-10,10,0)
BETA_CAR_COST_std = Beta('BETA_CAR_COST_std',0,-10,10,0)
BETA_HE_mean = Beta('BETA_HE_mean',0,-10,10,0)
BETA_HE_std = Beta('BETA_HE_std',0,-10,10,0)
BETA_SM_COST_mean = Beta('BETA_SM_COST_mean',0,-10,10,0)
BETA_SM_COST_std = Beta('BETA_SM_COST_std',0,-10,10,0)
BETA_TIME = Beta('BETA_TIME',0,-10,10,0)
BETA_TRAIN_COST_mean = Beta('BETA_TRAIN_COST_mean',0,-10,10,0)
BETA_TRAIN_COST_std = Beta('BETA_TRAIN_COST_std',0,-10,10,0)

# Random parameters
BETA_CAR_COST_random = BETA_CAR_COST_mean + BETA_CAR_COST_std * bioDraws('BETA_CAR_COST_random','NORMAL')
BETA_HE_random = BETA_HE_mean + BETA_HE_std * bioDraws('BETA_HE_random','NORMAL')
BETA_SM_COST_random = BETA_SM_COST_mean + BETA_SM_COST_std * bioDraws('BETA_SM_COST_random','NORMAL')
BETA_TRAIN_COST_random = BETA_TRAIN_COST_mean + BETA_TRAIN_COST_std * bioDraws('BETA_TRAIN_COST_random','NORMAL')

# Expressions
SM_COST  = DefineVariable('SM_COST', SM_CO   * (  GA   ==  0  ), database)
TRAIN_COST  = DefineVariable('TRAIN_COST', TRAIN_CO   * (  GA   ==  0  ), database)
one  = DefineVariable('one',1, database)

# Utilities
V_Car_SP = ASC_CAR * one + BETA_TIME * CAR_TT/100 + BETA_CAR_COST_random * CAR_CO/100
V_SBB_SP = ASC_SBB * one + BETA_TIME * TRAIN_TT/100 + BETA_TRAIN_COST_random * TRAIN_COST/100 + BETA_HE_random * TRAIN_HE/100
V_SM_SP = ASC_SM * one + BETA_TIME * SM_TT/100 + BETA_SM_COST_random * SM_COST/100 + BETA_HE_random * SM_HE/100

#
V = {3: V_Car_SP,1: V_SBB_SP,2: V_SM_SP}

# Associate the availability conditions with the alternatives
CAR_AV_SP =  DefineVariable('CAR_AV_SP',CAR_AV  * (  SP   !=  0  ),database)
TRAIN_AV_SP =  DefineVariable('TRAIN_AV_SP',TRAIN_AV  * (  SP   !=  0  ),database)

av = {3: CAR_AV_SP,1: TRAIN_AV_SP,2: SM_AV}

# Here we use the "biogeme" way for backward compatibility
exclude = (( PURPOSE != 1 ) * (  PURPOSE   !=  3  ) +  ( CHOICE == 0 )) > 0
database.remove(exclude)

# The choice model is a logit, with availability conditions
prob = models.logit(V,av,CHOICE)
logprob = log(MonteCarlo(prob))

# You can change the number of draws
biogeme = bio.BIOGEME(database,logprob,numberOfDraws=100)

biogeme.modelName = 'Mixture_SM_RandomCoeff'
results = biogeme.estimate()
print(results)
