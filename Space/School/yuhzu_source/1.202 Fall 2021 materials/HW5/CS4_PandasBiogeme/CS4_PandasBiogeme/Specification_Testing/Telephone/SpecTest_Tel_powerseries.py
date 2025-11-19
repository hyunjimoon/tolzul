# Translated to .py by Monique A. Stinson
# Modified by Peiyu Jing

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio

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
ASC_SM	 = Beta('ASC_SM',0,-10,10,1)
ASC_LF	 = Beta('ASC_LF',0,-10,10,0)
ASC_EF	 = Beta('ASC_EF',0,-10,10,0)
ASC_MF	 = Beta('ASC_MF',0,-10,10,0)
B_FCOST	 = Beta('B_FCOST',0,-10,10,0)
B_MCOST1 = Beta('B_MCOST1',0,-10,10,0)
B_MCOST2 = Beta('B_MCOST2',0,-10,10,0)

# Define here arithmetic expressions for name that are not directly
# available from the data

one  = DefineVariable('one',1,database)
cost11  = DefineVariable('cost11', cost1 * cost1 ,database)
cost22  = DefineVariable('cost22', cost2 * cost2 ,database)

#Utilities
V_BM = ASC_BM * one + B_MCOST1 * cost1 + B_MCOST2 * cost11
V_SM = ASC_SM * one + B_MCOST1 * cost2 + B_MCOST2 * cost22
V_LF = ASC_LF * one + B_FCOST * cost3
V_EF = ASC_EF * one + B_FCOST * cost4
V_MF = ASC_MF * one + B_FCOST * cost5

V = {1: V_BM, 2: V_SM, 3: V_LF, 4: V_EF, 5: V_MF}
avail = {1: avail1, 2: avail2, 3: avail3, 4: avail4, 5: avail5}

# Estimation of the model
logprob = bioLogLogit(V,avail,choice)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "MNL_Tel_powerseries"
results = biogeme.estimate()

# Print the estimated values
betas = results.getBetaValues()
for k,v in betas.items():
    print(f"{k}=\t{v:.3g}")

# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)

