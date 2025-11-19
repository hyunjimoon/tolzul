# Michel Bierlaire
# Wed Oct 31 18:48:52 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.models import logit
from biogeme.expressions import Beta, DefineVariable, log
import numpy as np

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

# The choice model is a logit, with availability conditions
logprob = models.loglogit(V,avail,choice)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "logit_Tel_socioec"
results = biogeme.estimate()

# Duplicate the database
database_lowInc = db.Database("telephone_lowInc",pd.DataFrame.copy(database.data))
database_medInc = db.Database("telephone_medInc",pd.DataFrame.copy(database.data))
database_highInc = db.Database("telephone_highInc",pd.DataFrame.copy(database.data))

# Remove observations
database_lowInc.remove(inc > 2)
database_medInc.remove(((inc < 3)+(inc > 4))>0)
database_highInc.remove(inc < 5)
print(f"Total number of observations: {database.getNumberOfObservations()}")
print(f"Low incone                  : {database_lowInc.getNumberOfObservations()}")
print(f"Medium income               : {database_medInc.getNumberOfObservations()}")
print(f"High income                 : {database_highInc.getNumberOfObservations()}")


##### Aggregate marketshares

prob_BM = logit(V,avail,1)
prob_SM = logit(V,avail,2)
prob_LF = logit(V,avail,3)
prob_EF = logit(V,avail,4)
prob_MF = logit(V,avail,5)

#Utilities
future_V_BM = ASC_BM + B_MCOST * log(cost1)
future_V_SM = ASC_SM + B_MCOST * log(cost2 + 4)
future_V_LF = ASC_LF + B_FCOST * log(cost3 + 6) + B_USERS * users
future_V_EF = ASC_EF + B_FCOST * log(cost4 + 7) + B_USERS * users
future_V_MF = ASC_MF + B_FCOST * log(cost5 + 11) + B_USERS * users
future_V = {1: future_V_BM, 2: future_V_SM, 3: future_V_LF, 4: future_V_EF, 5: future_V_MF}
future_prob_BM = logit(future_V,avail,1)
future_prob_SM = logit(future_V,avail,2)
future_prob_LF = logit(future_V,avail,3)
future_prob_EF = logit(future_V,avail,4)
future_prob_MF = logit(future_V,avail,5)

simulate = {'Prob. BM': prob_BM,
            'Prob. SM': prob_SM,
            'Prob. LF': prob_LF,
            'Prob. EF': prob_EF,
            'Prob. MF': prob_MF,
            'Future prob. BM': future_prob_BM,
            'Future prob. SM': future_prob_SM,
            'Future prob. LF': future_prob_LF,
            'Future prob. EF': future_prob_EF,
            'Future prob. MF': future_prob_MF}

biosim_low  = bio.BIOGEME(database_lowInc,simulate)
biosim_low.modelName = "marketShares_lowInc"
simresults_low = biosim_low.simulate(dict(zip(results.data.betaNames, results.data.betaValues)))
biosim_med  = bio.BIOGEME(database_medInc,simulate)
biosim_med.modelName = "marketShares_medInc"
simresults_med = biosim_med.simulate(dict(zip(results.data.betaNames, results.data.betaValues)))
biosim_hi  = bio.BIOGEME(database_highInc,simulate)
biosim_hi.modelName = "marketShares_hiInc"
simresults_hi = biosim_hi.simulate(dict(zip(results.data.betaNames, results.data.betaValues)))

# Gather the results in a table

columns = ['Low inc.','Med inc.','Hi inc.','Fut low inc.','Fut med inc.', 'Fut hi inc.']
summary = pd.DataFrame(columns=columns)

bm = {'Low inc.':100*simresults_low['Prob. BM'].mean(),
      'Med inc.':100*simresults_med['Prob. BM'].mean(),
      'Hi inc.':100*simresults_hi['Prob. BM'].mean(),
      'Fut low inc.':100*simresults_low['Future prob. BM'].mean(),
      'Fut med inc.':100*simresults_med['Future prob. BM'].mean(),
      'Fut hi inc.' :100*simresults_hi['Future prob. BM'].mean()}
summary.loc['BM'] = pd.Series(bm)

sm = {'Low inc.':100*simresults_low['Prob. SM'].mean(),
      'Med inc.':100*simresults_med['Prob. SM'].mean(),
      'Hi inc.':100*simresults_hi['Prob. SM'].mean(),
      'Fut low inc.':100*simresults_low['Future prob. SM'].mean(),
      'Fut med inc.':100*simresults_med['Future prob. SM'].mean(),
      'Fut hi inc.' :100*simresults_hi['Future prob. SM'].mean()}
summary.loc['SM'] = pd.Series(sm)

lf = {'Low inc.':100*simresults_low['Prob. LF'].mean(),
      'Med inc.':100*simresults_med['Prob. LF'].mean(),
      'Hi inc.':100*simresults_hi['Prob. LF'].mean(),
      'Fut low inc.':100*simresults_low['Future prob. LF'].mean(),
      'Fut med inc.':100*simresults_med['Future prob. LF'].mean(),
      'Fut hi inc.' :100*simresults_hi['Future prob. LF'].mean()}
summary.loc['LF'] = pd.Series(lf)

ef = {'Low inc.':100*simresults_low['Prob. EF'].mean(),
      'Med inc.':100*simresults_med['Prob. EF'].mean(),
      'Hi inc.':100*simresults_hi['Prob. EF'].mean(),
      'Fut low inc.':100*simresults_low['Future prob. EF'].mean(),
      'Fut med inc.':100*simresults_med['Future prob. EF'].mean(),
      'Fut hi inc.' :100*simresults_hi['Future prob. EF'].mean()}
summary.loc['EF'] = pd.Series(ef)

mf = {'Low inc.':100*simresults_low['Prob. MF'].mean(),
      'Med inc.':100*simresults_med['Prob. MF'].mean(),
      'Hi inc.':100*simresults_hi['Prob. MF'].mean(),
      'Fut low inc.':100*simresults_low['Future prob. MF'].mean(),
      'Fut med inc.':100*simresults_med['Future prob. MF'].mean(),
      'Fut hi inc.' :100*simresults_hi['Future prob. MF'].mean()}
summary.loc['MF'] = pd.Series(mf)

print(summary)

