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
N_FLAT = Beta('m_FLAT',2.16,1,10,1)
N_MEAS = Beta('m_MEAS',2.16,1,10,1)
#
N_FLAT_LF = Beta('a_FLAT_LF',0.5,0,1,0)
N_FLAT_EF = Beta('a_FLAT_EF',1,0,1,1)
N_FLAT_MF = Beta('a_FLAT_MF',1,0,1,1)
N_MEAS_SM = Beta('a_FLAT_SM',1,0,1,1)
N_MEAS_BM = Beta('a_MEAS_BM',1,0,1,1)
#
N_MEAS_LF = 1 - N_FLAT_LF

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
alpha_N_FLAT = {1: 0, 2: 0, 3: N_FLAT_LF, 4: N_FLAT_EF, 5: N_FLAT_MF}
alpha_N_MEAS = {1: N_MEAS_BM, 2: N_MEAS_SM, 3: N_MEAS_LF, 4: 0, 5: 0}

nest_N_FLAT = N_FLAT, alpha_N_FLAT
nest_N_MEAS = N_MEAS, alpha_N_MEAS

nests = nest_N_FLAT, nest_N_MEAS

# CNL (Cross-Nested Logit Model), with availability conditions
logprob = models.logcnl_avail(V,avail,nests,choice)

# Estimation of the model
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "MEV_Tel_CNL_var"
results = biogeme.estimate()

# Print the estimated values
betas = results.getBetaValues()
for k,v in betas.items():
    print(f"{k}=\t{v:.3g}")

# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)
