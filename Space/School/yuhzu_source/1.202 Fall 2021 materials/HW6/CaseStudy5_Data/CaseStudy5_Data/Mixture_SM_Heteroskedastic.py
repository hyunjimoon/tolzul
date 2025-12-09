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
ASC_CAR_mean = Beta('ASC_CAR_mean',0,-30,30,0)
ASC_CAR_std = Beta('ASC_CAR_std',0,-10,10,0)
ASC_SBB_mean = Beta('ASC_SBB_mean',0,-10,10,1) #fix to zero
ASC_SBB_std = Beta('ASC_SBB_std',0,-10,10,0)
ASC_SM_mean = Beta('ASC_SM_mean',0,-30,30,0)
ASC_SM_std = Beta('ASC_SM_std',0,-10,10,0)
BETA_COST = Beta('BETA_COST',0,-1,1,0)
BETA_HE = Beta('BETA_HE',0,-1,1,0)
BETA_TIME = Beta('BETA_TIME',0,-1,1,0)

# Random parameters
# Normalization: First estimate all three, then fix the smallest std to 0 and estimate again
ASC_CAR_random = ASC_CAR_mean + ASC_CAR_std * bioDraws('ASC_CAR_random','NORMAL')
ASC_SBB_random= ASC_SBB_mean + ASC_SBB_std * bioDraws('ASC_SBB_random','NORMAL')
ASC_SM_random= ASC_SM_mean + ASC_SM_std * bioDraws('ASC_SM_random','NORMAL')

# Define here arithmetic expressions for variables that are not directly
# available in the data file
SM_COST = DefineVariable('SM_COST', SM_CO   * (  GA   ==  0  ), database)
TRAIN_COST = DefineVariable('TRAIN_COST', TRAIN_CO   * (  GA   ==  0  ), database)
one = DefineVariable('one',1, database)

# Utilities
V_Car_SP = ASC_CAR_random * one + BETA_TIME * CAR_TT/100 + BETA_COST * CAR_CO/100
V_SBB_SP = ASC_SBB_random * one + BETA_TIME * TRAIN_TT/100 + BETA_COST * TRAIN_COST/100 + BETA_HE * TRAIN_HE/100
V_SM_SP = ASC_SM_random * one + BETA_TIME * SM_TT/100 + BETA_COST * SM_COST/100 + BETA_HE * SM_HE/100

#
V = {3: V_Car_SP,1: V_SBB_SP,2: V_SM_SP}

# Associate the availability conditions with the alternatives
CAR_AV_SP =  DefineVariable('CAR_AV_SP',CAR_AV  * (  SP   !=  0  ),database)
TRAIN_AV_SP =  DefineVariable('TRAIN_AV_SP',TRAIN_AV  * (  SP   !=  0  ),database)
av = {1: TRAIN_AV_SP,2: SM_AV,3: CAR_AV_SP}

# Here we use the "biogeme" way for backward compatibility
exclude = (( PURPOSE != 1 ) * (  PURPOSE   !=  3  ) +  ( CHOICE == 0 )) > 0
database.remove(exclude)

# The choice model is a logit, with availability conditions
prob = models.logit(V,av,CHOICE)
logprob = log(MonteCarlo(prob))

# You can change the number of draws
biogeme = bio.BIOGEME(database,logprob,numberOfDraws=100)

biogeme.modelName = 'Mixture_SM_Heteroskedastic'
results = biogeme.estimate()
print(results)
