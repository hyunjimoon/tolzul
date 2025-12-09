# Michel Bierlaire
# Thu Oct 25 16:44:11 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.expressions import Beta, DefineVariable, log

df = pd.read_csv("swissmetro.dat",'\t')
database = db.Database("swissmetro",df)
pd.options.display.float_format = '{:.3g}'.format
globals().update(database.variables)


exclude = ((  PURPOSE   !=  1  ) * (  PURPOSE   !=  3  ) + (  CHOICE   ==  0  ) + (  AGE == 6  ))>0
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
B_CAR_COST	 = Beta('B_CAR_COST',0,None,None,0)
B_CAR_TIME	 = Beta('B_CAR_TIME',0,None,None,0)
B_GA	 = Beta('B_GA',0,None,None,0)
B_HE	 = Beta('B_HE',0,None,None,0)
B_SM_COST	 = Beta('B_SM_COST',0,None,None,0)
B_SM_TIME	 = Beta('B_SM_TIME',0,None,None,0)
B_TIME	 = Beta('B_TIME',0,None,None,0)
B_TRAIN_COST	 = Beta('B_TRAIN_COST',0,None,None,0)
B_TRAIN_TIME	 = Beta('B_TRAIN_TIME',0,None,None,0)

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


av = {3: CAR_AV_SP,1: TRAIN_AV_SP,2: SM_AV}

# Model 1
M1_Car_SP = ASC_CAR + B_CAR_TIME * CAR_TT_SCALED + B_CAR_COST * CAR_CO_SCALED
M1_SBB_SP = ASC_SBB + B_TRAIN_TIME * TRAIN_TT_SCALED + B_TRAIN_COST * TRAIN_COST_SCALED
M1_SM_SP = ASC_SM + B_SM_TIME * SM_TT_SCALED + B_SM_COST * SM_COST_SCALED
M1_V = {3: M1_Car_SP,1: M1_SBB_SP,2: M1_SM_SP}
M1_logprob = models.loglogit(M1_V,av,CHOICE)

#Model 2
M2_Car_SP = ASC_CAR + B_TIME * CAR_TT_SCALED + B_CAR_COST * CAR_CO_SCALED
M2_SBB_SP = ASC_SBB + B_TIME * TRAIN_TT_SCALED + B_TRAIN_COST * TRAIN_COST_SCALED + B_HE * TRAIN_HE_SCALED + B_GA * GA
M2_SM_SP = ASC_SM + B_TIME * SM_TT_SCALED + B_SM_COST * SM_COST_SCALED + B_HE * SM_HE_SCALED + B_GA * GA
M2_V = {3: M2_Car_SP,1: M2_SBB_SP,2: M2_SM_SP}
M2_logprob = models.loglogit(M2_V,av,CHOICE)

# Composite model 
MC_Car_SP = ASC_CAR + B_CAR_TIME * CAR_TT_SCALED + B_CAR_COST * CAR_CO_SCALED
MC_SBB_SP = ASC_SBB + B_TRAIN_TIME * TRAIN_TT_SCALED + B_TRAIN_COST * TRAIN_COST_SCALED + B_HE * TRAIN_HE_SCALED + B_GA * GA
MC_SM_SP = ASC_SM + B_SM_TIME * SM_TT_SCALED + B_SM_COST * SM_COST_SCALED + B_HE * SM_HE_SCALED + B_GA * GA
MC_V = {3: MC_Car_SP,1: MC_SBB_SP,2: MC_SM_SP}
MC_logprob = models.loglogit(MC_V,av,CHOICE)

biogeme_M1  = bio.BIOGEME(database,M1_logprob)
biogeme_M1.modelName = "coxTest_M1"
results_M1 = biogeme_M1.estimate()
ll_M1 = results_M1.data.logLike

biogeme_M2  = bio.BIOGEME(database,M2_logprob)
biogeme_M2.modelName = "coxTest_M2"
results_M2 = biogeme_M2.estimate()
ll_M2 = results_M2.data.logLike

biogeme_MC  = bio.BIOGEME(database,MC_logprob)
biogeme_MC.modelName = "coxTest_MC"
results_MC = biogeme_MC.estimate()
ll_MC = results_MC.data.logLike

print(f"LL M1: {ll_M1:.3f} rhobar: {results_M1.data.rhoBarSquare:.3f}  Parameters: {results_M1.data.nparam}")
print(f"LL M2: {ll_M2:.3f}  rhobar: {results_M2.data.rhoBarSquare:.3f}  Parameters: {results_M2.data.nparam}")
print(f"LL MC: {ll_MC:.3f}  rhobar: {results_MC.data.rhoBarSquare:.3f}  Parameters: {results_MC.data.nparam}")
lr_M1 = -2 * (ll_M1 - ll_MC)
print(f"LR model 1 vs composite: {lr_M1:.3f}")
lr_M2 = -2 * (ll_M2 - ll_MC)
print(f"LR model 2 vs composite: {lr_M2:.3f}")
print("Output files:")
print(f"{results_M1.data.htmlFileName}")
print(f"{results_M2.data.htmlFileName}")
print(f"{results_MC.data.htmlFileName}")
