# Michel Bierlaire
# Thu Oct 25 08:22:01 2018

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
B_USERS	 = Beta('B_USERS',0,None,None,0)

# Define here arithmetic expressions for name that are not directly
# available from the data

logcostBM  = DefineVariable('logcostBM', log(cost1),database)
logcostSM  = DefineVariable('logcostSM', log(cost2),database)
logcostLF  = DefineVariable('logcostLF', log(cost3),database)
logcostEF  = DefineVariable('logcostEF', log(cost4),database)
logcostMF  = DefineVariable('logcostMF', log(cost5),database)

#Utilities
V_BM = ASC_BM + B_MCOST * logcostBM
V_SM = ASC_SM + B_MCOST * logcostSM
V_LF = ASC_LF + B_FCOST * logcostLF + B_USERS * users
V_EF = ASC_EF + B_FCOST * logcostEF + B_USERS * users
V_MF = ASC_MF + B_FCOST * logcostMF + B_USERS * users



V = {1: V_BM, 2: V_SM, 3: V_LF, 4: V_EF, 5: V_MF}
avail = {1: avail1, 2: avail2, 3: avail3, 4: avail4, 5: avail5}

# Duplicate the database
database_lowInc = db.Database("telephone_lowInc",pd.DataFrame.copy(database.data))
database_medInc = db.Database("telephone_medInc",pd.DataFrame.copy(database.data))
database_highInc = db.Database("telephone_highInc",pd.DataFrame.copy(database.data))

# Remove observations
database_lowInc.remove(((inc==2)+(inc==3)+(inc==4)+(inc==5))>0)
database_medInc.remove(((inc==1)+(inc==5))>0)
database_highInc.remove(((inc==1)+(inc==2)+(inc==3)+(inc==4))>0)
print(f"Total number of observations: {database.getNumberOfObservations()}")
print(f"Low incone                  : {database_lowInc.getNumberOfObservations()}")
print(f"Medium income               : {database_medInc.getNumberOfObservations()}")
print(f"High income                 : {database_highInc.getNumberOfObservations()}")


# The choice model is a logit, with availability conditions
logprob = models.loglogit(V,avail,choice)

# A specification without the ASC for EF is necessary for the low
# income category.

V_EF_noAsc = B_FCOST * logcostEF + B_USERS * users
V_noAsc = {1: V_BM, 2: V_SM, 3: V_LF, 4: V_EF_noAsc, 5: V_MF}
logprob_noAsc = models.loglogit(V_noAsc,avail,choice)


biogeme_full  = bio.BIOGEME(database,logprob)
biogeme_full.modelName = "segmentation_fullSample"
results_full = biogeme_full.estimate()
ll_full = results_full.data.logLike

biogeme_lowInc  = bio.BIOGEME(database_lowInc,logprob_noAsc)
biogeme_lowInc.modelName = "segmentation_lowInc"
results_lowInc = biogeme_lowInc.estimate()
ll_lowInc = results_lowInc.data.logLike

biogeme_medInc  = bio.BIOGEME(database_medInc,logprob)
biogeme_medInc.modelName = "segmentation_medInc"
results_medInc = biogeme_medInc.estimate()
ll_medInc = results_medInc.data.logLike

biogeme_highInc  = bio.BIOGEME(database_highInc,logprob)
biogeme_highInc.modelName = "segmentation_highInc"
results_highInc = biogeme_highInc.estimate()
ll_highInc = results_highInc.data.logLike

print(f"LL full:          {ll_full:.3f}  Parameters: {results_full.data.nparam}")
print(f"LL low income:    {ll_lowInc:.3f}  Parameters: {results_lowInc.data.nparam}")
print(f"LL medium income: {ll_medInc:.3f}  Parameters: {results_medInc.data.nparam}")
print(f"LL high income:   {ll_highInc:.3f}   Parameters: {results_highInc.data.nparam}")
unrestricted = ll_lowInc + ll_medInc + ll_highInc
print(f"Sum LL:           {unrestricted:.3f}")
lr = -2 * (ll_full - unrestricted)
print(f"likelihood ratio: {lr:.3f}")
print("Output files:")
print(f"{results_full.data.htmlFileName}")
print(f"{results_lowInc.data.htmlFileName}")
print(f"{results_medInc.data.htmlFileName}")
print(f"{results_highInc.data.htmlFileName}")
