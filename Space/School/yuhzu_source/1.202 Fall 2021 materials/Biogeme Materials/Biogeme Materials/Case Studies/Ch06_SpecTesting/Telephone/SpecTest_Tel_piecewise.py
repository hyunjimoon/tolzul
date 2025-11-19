# Michel Bierlaire
# Thu Oct 25 09:07:51 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.expressions import Beta, DefineVariable, log
from biogeme.models import piecewiseVariables
import numpy as np
import matplotlib.pyplot as plt

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
B_MCOST1 = Beta('B_MCOST1',0,None,None,0)
B_MCOST2 = Beta('B_MCOST2',0,None,None,0)
B_MCOST3 = Beta('B_MCOST3',0,None,None,0)

# Define here arithmetic expressions for name that are not directly
# available from the data

logcostBM  = DefineVariable('logcostBM', log(cost1),database)
logcostSM  = DefineVariable('logcostSM', log(cost2),database)
logcostLF  = DefineVariable('logcostLF', log(cost3),database)
logcostEF  = DefineVariable('logcostEF', log(cost4),database)
logcostMF  = DefineVariable('logcostMF', log(cost5),database)

# Variables for the piecewise linear specification
thresholds = [None,10,50,None]
piecewise_cost1 = piecewiseVariables(cost1,thresholds)
piecewise_cost2 = piecewiseVariables(cost2,thresholds)

cost11  = DefineVariable('cost11', piecewise_cost1[0],database)
cost12  = DefineVariable('cost12', piecewise_cost1[1],database)
cost13  = DefineVariable('cost13', piecewise_cost1[2],database)
cost21  = DefineVariable('cost21', piecewise_cost2[0],database)
cost22  = DefineVariable('cost22', piecewise_cost2[1],database)
cost23  = DefineVariable('cost23', piecewise_cost2[2],database)

#Utilities restricted model 
M1_V_BM = ASC_BM + B_MCOST * cost1
M1_V_SM = ASC_SM + B_MCOST * cost2
M1_V_LF = ASC_LF + B_FCOST * cost3
M1_V_EF = ASC_EF + B_FCOST * cost4
M1_V_MF = ASC_MF + B_FCOST * cost5

M1_V = {1: M1_V_BM, 2: M1_V_SM, 3: M1_V_LF, 4: M1_V_EF, 5: M1_V_MF}

# The choice model is a logit, with availability conditions
avail = {1: avail1, 2: avail2, 3: avail3, 4: avail4, 5: avail5}
M1_logprob = models.loglogit(M1_V,avail,choice)

#Utilities unrestricted model 
M2_V_BM = ASC_BM + B_MCOST1 * cost11 + B_MCOST2 * cost12 + B_MCOST3 * cost13
M2_V_SM = ASC_SM + B_MCOST1 * cost21 + B_MCOST2 * cost22 + B_MCOST3 * cost23
M2_V_LF = ASC_LF + B_FCOST * cost3
M2_V_EF = ASC_EF + B_FCOST * cost4
M2_V_MF = ASC_MF + B_FCOST * cost5

M2_V = {1: M2_V_BM, 2: M2_V_SM, 3: M2_V_LF, 4: M2_V_EF, 5: M2_V_MF}
M2_logprob = models.loglogit(M2_V,avail,choice)

biogeme_M1  = bio.BIOGEME(database,M1_logprob)
biogeme_M1.modelName = "piecewise_restricted"
results_M1 = biogeme_M1.estimate()
ll_M1 = results_M1.data.logLike

biogeme_M2  = bio.BIOGEME(database,M2_logprob)
biogeme_M2.modelName = "piecewise_unrestricted"
results_M2 = biogeme_M2.estimate()
ll_M2 = results_M2.data.logLike

print(f"LL restr.:   {ll_M1:.3f}  rhobar: {results_M1.data.rhoBarSquare:.3f}  Parameters: {results_M1.data.nparam}")
print(f"LL unrestr.: {ll_M2:.3f}  rhobar: {results_M2.data.rhoBarSquare:.3f}  Parameters: {results_M2.data.nparam}")
lr = -2 * (ll_M1 - ll_M2)
print(f"Likelihood ratio: {lr:.3f}")
print("Output files:")
print(f"{results_M1.data.htmlFileName}")
print(f"{results_M2.data.htmlFileName}")

def utilLinear(cost):
    beta = ['B_MCOST']
    betaValue = results_M1.getBetaValues(beta)
    return betaValue['B_MCOST'] * cost

def utilPW(cost):
    piecewise_cost = piecewiseVariables(cost,thresholds)
    betas = ['B_MCOST1','B_MCOST2','B_MCOST3']
    betaValues = results_M2.getBetaValues(betas)
    V = betaValues['B_MCOST1'] * piecewise_cost[0].getValue() + betaValues['B_MCOST2'] * piecewise_cost[1].getValue() + betaValues['B_MCOST3'] * piecewise_cost[2].getValue()
    return V

costs = np.arange(0,60,0.5)
vl = [utilLinear(c) for c in costs]
vpw = [utilPW(c) for c in costs]

fig, ax = plt.subplots()
ax.plot(costs,vl,label='Linear')
ax.plot(costs,vpw,label='Piecewise')
ax.legend()
plt.xlabel("Cost")
plt.ylabel("Utility")
plt.show()


