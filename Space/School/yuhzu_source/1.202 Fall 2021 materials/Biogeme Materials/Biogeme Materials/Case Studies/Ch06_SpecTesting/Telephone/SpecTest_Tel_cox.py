# Michel Bierlaire
# Thu Oct 25 08:50:07 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.expressions import Beta, DefineVariable, log

df = pd.read_csv("telephone.dat",'\t')
database = db.Database("telephone",df)
pd.options.display.float_format = '{:.3g}'.format
globals().update(database.variables)

#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_BM	 = Beta('ASC_BM',0,None,None,0)
ASC_SM	 = Beta('ASC_SM',0,None,None,1)
ASC_LF	 = Beta('ASC_LF',0,None,None,0)
ASC_EF	 = Beta('ASC_EF',0,None,None,0)
ASC_MF	 = Beta('ASC_MF',0,None,None,0)
B_FCOST	 = Beta('B_FCOST',0,None,None,0)
B_MCOST	 = Beta('B_MCOST',0,None,None,0)
B_COST	 = Beta('B_COST',0,None,None,0)
B_USERS	 = Beta('B_USERS',0,None,None,0)

# Define here arithmetic expressions for name that are not directly
# available from the data

logcostBM  = DefineVariable('logcostBM', log(cost1),database)
logcostSM  = DefineVariable('logcostSM', log(cost2),database)
logcostLF  = DefineVariable('logcostLF', log(cost3),database)
logcostEF  = DefineVariable('logcostEF', log(cost4),database)
logcostMF  = DefineVariable('logcostMF', log(cost5),database)

#Utilities model 1
M1_V_BM = ASC_BM + B_MCOST * cost1
M1_V_SM = ASC_SM + B_MCOST * cost2
M1_V_LF = ASC_LF + B_FCOST * cost3
M1_V_EF = ASC_EF + B_FCOST * cost4
M1_V_MF = ASC_MF + B_FCOST * cost5

M1_V = {1: M1_V_BM, 2: M1_V_SM, 3: M1_V_LF, 4: M1_V_EF, 5: M1_V_MF}

# The choice model is a logit, with availability conditions
avail = {1: avail1, 2: avail2, 3: avail3, 4: avail4, 5: avail5}
M1_logprob = models.loglogit(M1_V,avail,choice)

#Utilities model 2
M2_V_BM = ASC_BM + B_COST * cost1
M2_V_SM = ASC_SM + B_COST * cost2
M2_V_LF = ASC_LF + B_COST * cost3 + B_USERS * users
M2_V_EF = ASC_EF + B_COST * cost4 + B_USERS * users
M2_V_MF = ASC_MF + B_COST * cost5 + B_USERS * users

M2_V = {1: M2_V_BM, 2: M2_V_SM, 3: M2_V_LF, 4: M2_V_EF, 5: M2_V_MF}
M2_logprob = models.loglogit(M2_V,avail,choice)

#Utilities model C
MC_V_BM = ASC_BM + B_MCOST * cost1
MC_V_SM = ASC_SM + B_MCOST * cost2
MC_V_LF = ASC_LF + B_FCOST * cost3 + B_USERS * users
MC_V_EF = ASC_EF + B_FCOST * cost4 + B_USERS * users
MC_V_MF = ASC_MF + B_FCOST * cost5 + B_USERS * users

MC_V = {1: MC_V_BM, 2: MC_V_SM, 3: MC_V_LF, 4: MC_V_EF, 5: MC_V_MF}
MC_logprob = models.loglogit(MC_V,avail,choice)

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

