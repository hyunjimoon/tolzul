# Translated to .py by Monique A. Stinson
# Modified by Peiyu Jing

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models

pandas = pd.read_table("telephone.dat")
database = db.Database("telephone",pandas)

from headers import *
  
#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_BM	 = Beta('ASC_BM',0,-10,10,0)
ASC_EF	 = Beta('ASC_EF',0,-10,10,0)
ASC_LF	 = Beta('ASC_LF',0,-10,10,0)
ASC_MF	 = Beta('ASC_MF',0,-10,10,0)
ASC_SM	 = Beta('ASC_SM',0,-10,10,1)
B_COST	 = Beta('B_COST',0,-10,10,0)
#
# parameters relevant to the nests
N_FLAT = Beta('N_FLAT',1,1,10, 0)
N_MEAS = Beta('N_MEAS',1,1,10, 0)

# Define here arithmetic expressions for names that are not directly
# available from the data

one  = DefineVariable('one',1,database)
logcostBM  = DefineVariable('logcostBM', log(cost1),database)
logcostSM  = DefineVariable('logcostSM', log(cost2),database)
logcostLF  = DefineVariable('logcostLF', log(cost3),database)
logcostEF  = DefineVariable('logcostEF', log(cost4),database)
logcostMF  = DefineVariable('logcostMF', log(cost5),database)

#Utilities
V_BM = ASC_BM * one + B_COST * logcostBM
V_SM = ASC_SM * one + B_COST * logcostSM
V_LF = ASC_LF * one + B_COST * logcostLF
V_EF = ASC_EF * one + B_COST * logcostEF
V_MF = ASC_MF * one + B_COST * logcostMF

V = {1: V_BM, 2: V_SM, 3: V_LF, 4: V_EF, 5: V_MF}
avail = {1: avail1, 2: avail2, 3: avail3, 4: avail4, 5: avail5}

#Definitions of nests
N_FLAT = N_FLAT, [3, 4, 5]
N_MEAS = N_MEAS, [1, 2]

nests = N_FLAT, N_MEAS

# Estimation of the model
logprob = models.lognested(V,avail,nests,choice)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "MEV_Tel_NL_unrestricted"
results = biogeme.estimate()

# Print the estimated values
betas = results.getBetaValues()
for k,v in betas.items():
    print(f"{k}=\t{v:.3g}")

# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)


