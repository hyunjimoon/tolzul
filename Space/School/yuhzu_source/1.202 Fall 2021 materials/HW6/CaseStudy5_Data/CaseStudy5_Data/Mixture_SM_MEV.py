# Translated to .py by Meritxell Pacheco (December 2016)
########################################################
# Updated by Evanthia Kazagli (January 2017)
########################################################
# Updated by Peiyu Jing (April 2019)
########################################################

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.expressions import Beta, DefineVariable, bioDraws, PanelLikelihoodTrajectory, MonteCarlo, log

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
BETA_CAR_TIME_mean = Beta('BETA_CAR_TIME_mean',0,-10,10,0)
BETA_CAR_TIME_std = Beta('BETA_CAR_TIME_std',0,-10,10,0)
BETA_COST = Beta('BETA_COST',0,-10,10,0)
BETA_GA = Beta('BETA_GA',0,-10,50,0)
BETA_HE = Beta('BETA_HE',0,-10,10,0)
BETA_SEATS = Beta('BETA_SEATS',0,-10,10,0)
BETA_SENIOR = Beta('BETA_SENIOR',0,-10,10,0)
BETA_SM_TIME_mean = Beta('BETA_SM_TIME_mean',0,-10,10,0)
BETA_SM_TIME_std = Beta('BETA_SM_TIME_std',0,-10,10,0)
BETA_TRAIN_TIME_mean = Beta('BETA_TRAIN_TIME_mean',0,-10,10,0)
BETA_TRAIN_TIME_std = Beta('BETA_TRAIN_TIME_std',0,-10,10,0)
Classic = Beta('Classic',1,1,10, 0)
Innovative = Beta('Innovative',1,1,10,1)

#Randdom parameters
BETA_CAR_TIME_random = BETA_CAR_TIME_mean + BETA_CAR_TIME_std * bioDraws('BETA_CAR_TIME_random','NORMAL')
BETA_SM_TIME_random = BETA_SM_TIME_mean + BETA_SM_TIME_std * bioDraws('BETA_SM_TIME_random','NORMAL')
BETA_TRAIN_TIME_random = BETA_TRAIN_TIME_mean + BETA_TRAIN_TIME_std * bioDraws('BETA_TRAIN_TIME_random','NORMAL')

# Define here arithmetic expressions for variables that are not directly
# available in the data file
SENIOR  = DefineVariable('SENIOR', AGE   ==  5, database )
SM_COST  = DefineVariable('SM_COST', SM_CO   * (  GA   ==  0  ), database )
TRAIN_COST  = DefineVariable('TRAIN_COST', TRAIN_CO   * (  GA   ==  0  ), database )
one  = DefineVariable('one',1, database )

# Utilities
V_Car_SP = ASC_CAR * one + BETA_CAR_TIME_random * CAR_TT/100 + BETA_COST * CAR_CO/100
V_SBB_SP = ASC_SBB * one + BETA_TRAIN_TIME_random * TRAIN_TT/100 + BETA_COST * TRAIN_COST/100 + BETA_HE * TRAIN_HE/100 + BETA_GA * GA + BETA_SENIOR * SENIOR
V_SM_SP = ASC_SM * one + BETA_SM_TIME_random * SM_TT/100 + BETA_COST * SM_COST/100 + BETA_HE * SM_HE/100 + BETA_GA * GA + BETA_SEATS * SM_SEATS

# Nests: allocate alternatives into nests depending on your assumptions
nest_Classic = Classic, [1,3]
nest_Innovative = Innovative, [2]
nests = nest_Classic, nest_Innovative

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
prob = models.nested(V,av,nests,CHOICE)
logprob = log(MonteCarlo(prob))

import biogeme.messaging as msg
logger = msg.bioMessage()
#logger.setSilent()
#logger.setWarning()
#logger.setGeneral()
#logger.setDetailed()
logger.setDebug()

# You can change the number of draws
biogeme = bio.BIOGEME(database,logprob,numberOfDraws=100)

biogeme.modelName = 'Mixture_SM_MEV'
results = biogeme.estimate()
print(results)
