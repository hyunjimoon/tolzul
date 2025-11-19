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
ASC_CAR = Beta('ASC_CAR',0,-3,3,0)
ASC_SBB = Beta('ASC_SBB',0,-10,10,1)
ASC_SM = Beta('ASC_SM',0,-30,30,0)
BETA_COST = Beta('BETA_COST',0,-1,1,0)
BETA_HE = Beta('BETA_HE',0,-1,1,0)
BETA_TIME = Beta('BETA_TIME',0,-1,1,0)
RAIL_mean = Beta('RAIL_mean',0,-10,10,1)
RAIL_std = Beta('RAIL_std',0,-10,10,0)
# Define a random parameter, normally distirbuted, designed to be used for Monte-Carlo simulation
RAIL_random = RAIL_mean + RAIL_std * bioDraws('RAIL_random','NORMAL')

# Define here arithmetic expressions for variables that are not directly
# available in the data file
SM_COST = DefineVariable('SM_COST', SM_CO   * (  GA   ==  0  ), database)
TRAIN_COST = DefineVariable('TRAIN_COST', TRAIN_CO   * (  GA   ==  0  ), database)
one = DefineVariable('one',1, database)

# Utilities
V_SBB_SP = ASC_SBB * one + BETA_TIME * TRAIN_TT/100 + BETA_COST * TRAIN_COST/100 + BETA_HE * TRAIN_HE/100 + RAIL_random * one
V_SM_SP = ASC_SM * one + BETA_TIME * SM_TT/100 + BETA_COST * SM_COST/100 + BETA_HE * SM_HE/100 + RAIL_random * one
V_Car_SP = ASC_CAR * one + BETA_TIME * CAR_TT/100 + BETA_COST * CAR_CO/100
#
V = {1:V_SBB_SP,2:V_SM_SP,3:V_Car_SP}

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

biogeme.modelName = 'Mixture_SM_ErrorComp_01'
results = biogeme.estimate()
print(results)

