# Translated to .py by Monique A. Stinson
# Modified by Peiyu Jing

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
from biogeme.models import piecewise

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
B_MCOST1	 = Beta('B_MCOST1',0,-10,10,0)
B_MCOST2	 = Beta('B_MCOST2',0,-10,10,0)
B_MCOST3	 = Beta('B_MCOST3',0,-10,10,0)

# Define here arithmetic expressions for name that are not directly
# available from the data

one  = DefineVariable('one',1,database)
# Variables for the piecewise linear specification
thresholds1 = [10,40,50]
pw_cost1 = piecewise(cost1 ,thresholds1)
cost11  = DefineVariable('cost11', pw_cost1[0],database)
cost12  = DefineVariable('cost12', pw_cost1[1],database)
cost13  = DefineVariable('cost13', pw_cost1[2],database)

thresholds2 = [10,40,50]
pw_cost2 = piecewise(cost2 ,thresholds2)
cost21  = DefineVariable('cost21', pw_cost2[0],database)
cost22  = DefineVariable('cost22', pw_cost2[1],database)
cost23  = DefineVariable('cost23', pw_cost2[2],database)

#Utilities
V_BM = ASC_BM * one + B_MCOST1 * cost11 + B_MCOST2 * cost12 + B_MCOST3 * cost13
V_SM = ASC_SM * one + B_MCOST1 * cost21 + B_MCOST2 * cost22 + B_MCOST3 * cost23
V_LF = ASC_LF * one + B_FCOST * cost3
V_EF = ASC_EF * one + B_FCOST * cost4
V_MF = ASC_MF * one + B_FCOST * cost5

V = {1: V_BM, 2: V_SM, 3: V_LF, 4: V_EF, 5: V_MF}
avail = {1: avail1, 2: avail2, 3: avail3, 4: avail4, 5: avail5}

# Estimation of the model
logprob = bioLogLogit(V,avail,choice)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "MNL_Tel_piecewise"
results = biogeme.estimate()

# Print the estimated values
betas = results.getBetaValues()
for k,v in betas.items():
    print(f"{k}=\t{v:.3g}")

# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)

