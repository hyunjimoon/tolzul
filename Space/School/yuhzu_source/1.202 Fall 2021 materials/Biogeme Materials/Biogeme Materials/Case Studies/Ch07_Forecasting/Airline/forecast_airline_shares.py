# Michel Bierlaire
# Wed Oct 31 21:48:39 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.models import logit
from biogeme.expressions import Beta, DefineVariable, log, Derive
import numpy as np

df = pd.read_csv("airline.dat",'\t')
database = db.Database("airline",df)
pd.options.display.float_format = '{:.3g}'.format
globals().update(database.variables)


# Exclude
exclude = (  ArrivalTimeHours_1   ==  -1  )
database.remove(exclude)

# Choice
chosenAlternative = ( (  BestAlternative_1   *  1  ) + (  BestAlternative_2   *  2  ) ) + (  BestAlternative_3   *  3  )

#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
Constant1     = Beta('Constant1',0,None,None,1)
Constant2     = Beta('Constant2',0,None,None,0)
Constant3     = Beta('Constant3',0,None,None,0)
Fare     = Beta('Fare',0,None,None,0)
Legroom     = Beta('Legroom',0,None,None,0)
SchedDE     = Beta('SchedDE',0,None,None,0)
SchedDL     = Beta('SchedDL',0,None,None,0)
Total_TT1     = Beta('Total_TT1',0,None,None,0)
Total_TT2     = Beta('Total_TT2',0,None,None,0)
Total_TT3     = Beta('Total_TT3',0,None,None,0)

# Define here arithmetic expressions for name that are not directly available from the data

DepartureTimeSensitive  = DefineVariable('DepartureTimeSensitive', q11_DepartureOrArrivalIsImportant   ==  1 ,database)
ArrivalTimeSensitive  = DefineVariable('ArrivalTimeSensitive', q11_DepartureOrArrivalIsImportant   ==  2 ,database)
Missing  = DefineVariable('Missing',(  q11_DepartureOrArrivalIsImportant   !=  1  ) * (  q11_DepartureOrArrivalIsImportant   !=  2  ),database)
DesiredDepartureTime  = DefineVariable('DesiredDepartureTime',q12_IdealDepTime ,database)
DesiredArrivalTime  = DefineVariable('DesiredArrivalTime',q13_IdealArrTime ,database)
ScheduledDelay_1  = DefineVariable('ScheduledDelay_1',(  DepartureTimeSensitive   * (  DepartureTimeMins_1   -  DesiredDepartureTime   ) ) + (  ArrivalTimeSensitive   * (  ArrivalTimeMins_1   -  DesiredArrivalTime   ) ),database)
ScheduledDelay_2  = DefineVariable('ScheduledDelay_2',(  DepartureTimeSensitive   * (  DepartureTimeMins_2   -  DesiredDepartureTime   ) ) + (  ArrivalTimeSensitive   * (  ArrivalTimeMins_2   -  DesiredArrivalTime   ) ),database)
ScheduledDelay_3  = DefineVariable('ScheduledDelay_3',(  DepartureTimeSensitive   * (  DepartureTimeMins_3   -  DesiredDepartureTime   ) ) + (  ArrivalTimeSensitive   * (  ArrivalTimeMins_3   -  DesiredArrivalTime   ) ),database)
Opt1_SchedDelayEarly  = DefineVariable('Opt1_SchedDelayEarly',(  -(ScheduledDelay_1 )  * (  ScheduledDelay_1   <  0  ) ) /  60 ,database)
Opt2_SchedDelayEarly  = DefineVariable('Opt2_SchedDelayEarly',(  -(ScheduledDelay_2 )  * (  ScheduledDelay_2   <  0  ) ) /  60 ,database)
Opt3_SchedDelayEarly  = DefineVariable('Opt3_SchedDelayEarly',(  -(ScheduledDelay_3 )  * (  ScheduledDelay_3   <  0  ) ) /  60 ,database)
Opt1_SchedDelayLate  = DefineVariable('Opt1_SchedDelayLate',(  ScheduledDelay_1   * (  ScheduledDelay_1   >  0  ) ) /  60 ,database)
Opt2_SchedDelayLate  = DefineVariable('Opt2_SchedDelayLate',(  ScheduledDelay_2   * (  ScheduledDelay_2   >  0  ) ) /  60 ,database)
Opt3_SchedDelayLate  = DefineVariable('Opt3_SchedDelayLate',(  ScheduledDelay_3   * (  ScheduledDelay_3   >  0  ) ) /  60 ,database)

# Utilities
Opt1 = Constant1 + Fare * Fare_1 + Legroom * Legroom_1 + SchedDE * Opt1_SchedDelayEarly + SchedDL * Opt1_SchedDelayLate + Total_TT1 * TripTimeHours_1
Opt2 = Constant2 + Fare * Fare_2 + Legroom * Legroom_2 + SchedDE * Opt2_SchedDelayEarly + SchedDL * Opt2_SchedDelayLate + Total_TT2 * TripTimeHours_2
Opt3 = Constant3 + Fare * Fare_3 + Legroom * Legroom_3 + SchedDE * Opt3_SchedDelayEarly + SchedDL * Opt3_SchedDelayLate + Total_TT3 * TripTimeHours_3
V = {1: Opt1,2: Opt2,3: Opt3}
av = {1: 1,2: 1,3: 1}

# The choice model is a logit, with availability conditions
logprob = models.loglogit(V,av,chosenAlternative)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "logit_airline_specific"
results = biogeme.estimate()

# Duplicate the database
database_self = db.Database("airline_self",pd.DataFrame.copy(database.data))
database_other = db.Database("airline_other",pd.DataFrame.copy(database.data))

# Remove observations
database_self.remove(q03_WhoPays !=  1)
database_other.remove(q03_WhoPays == 1)
print(f"Total number of observations: {database.getNumberOfObservations()}")
print(f"Self paying                 : {database_self.getNumberOfObservations()}")
print(f"Others paying               : {database_other.getNumberOfObservations()}")

##### Aggregate marketshares
prob_1 = logit(V,av,1)
prob_2 = logit(V,av,2)
prob_3 = logit(V,av,3)

#### Future aggregate market shares
future_Opt1 = Constant1 + Fare * Fare_1 * 1.2 + Legroom * Legroom_1 + SchedDE * Opt1_SchedDelayEarly + SchedDL * Opt1_SchedDelayLate + Total_TT1 * TripTimeHours_1
future_V = {1: future_Opt1,2: Opt2,3: Opt3}
future_prob_1 = logit(future_V,av,1)
future_prob_2 = logit(future_V,av,2)
future_prob_3 = logit(future_V,av,3)

#### Expressions for the elasticities
direct_elas_Fare1_Opt1 = Derive(prob_1,'Fare_1')*Fare_1/prob_1
cross_elas_Fare1_Opt2 = Derive(prob_2,'Fare_1')*Fare_1/prob_2
cross_elas_Fare1_Opt3 = Derive(prob_3,'Fare_1')*Fare_1/prob_3

simulate = {'Prob1': prob_1,
    'Prob2': prob_2,
        'Prob3': prob_3,
            'Future prob1': future_prob_1,
            'Future prob2': future_prob_2,
            'Future prob3': future_prob_3,
            'Elast Fare1 Opt1': direct_elas_Fare1_Opt1,
            'Elast Fare1 Opt2': cross_elas_Fare1_Opt2,
            'Elast Fare1 Opt3': cross_elas_Fare1_Opt3}

biosim_self  = bio.BIOGEME(database_self,simulate)
biosim_self.modelName = "marketShares_self"
simresults_self = biosim_self.simulate(dict(zip(results.data.betaNames, results.data.betaValues)))
biosim_other  = bio.BIOGEME(database_other,simulate)
biosim_other.modelName = "marketShares_other"
simresults_other = biosim_other.simulate(dict(zip(results.data.betaNames, results.data.betaValues)))

# Gather the results in a table

columns = ['Self','Others','Fut self','Fut others']
summary = pd.DataFrame(columns=columns)

opt1 = {'Self':100*simresults_self['Prob1'].mean(),
    'Others':100*simresults_other['Prob1'].mean(),
    'Fut self':100*simresults_self['Future prob1'].mean(),
    'Fut others':100*simresults_other['Future prob1'].mean()}
summary.loc['Non stop'] = pd.Series(opt1)

opt2 = {'Self':100*simresults_self['Prob2'].mean(),
    'Others':100*simresults_other['Prob2'].mean(),
    'Fut self':100*simresults_self['Future prob2'].mean(),
    'Fut others':100*simresults_other['Future prob2'].mean()}
summary.loc['One stop - same airline'] = pd.Series(opt2)

opt3 = {'Self':100*simresults_self['Prob3'].mean(),
    'Others':100*simresults_other['Prob3'].mean(),
    'Fut self':100*simresults_self['Future prob3'].mean(),
    'Fut others':100*simresults_other['Future prob3'].mean()}
summary.loc['One stop - mult. airlines'] = pd.Series(opt3)

print(summary)

# Print out the elasticities

denominator_Opt1_self = simresults_self['Prob1'].sum()
denominator_Opt2_self = simresults_self['Prob2'].sum()
denominator_Opt3_self = simresults_self['Prob3'].sum()
denominator_Opt1_other = simresults_other['Prob1'].sum()
denominator_Opt2_other = simresults_other['Prob2'].sum()
denominator_Opt3_other = simresults_other['Prob3'].sum()

agg_direct_elas_Fare1_Opt1_self = (simresults_self['Prob1'] * simresults_self['Elast Fare1 Opt1'] / denominator_Opt1_self).sum()
agg_cross_elas_Fare1_Opt2_self = (simresults_self['Prob2'] * simresults_self['Elast Fare1 Opt2'] / denominator_Opt2_self).sum()
agg_cross_elas_Fare1_Opt3_self = (simresults_self['Prob3'] * simresults_self['Elast Fare1 Opt3'] / denominator_Opt3_self).sum()
agg_direct_elas_Fare1_Opt1_other = (simresults_other['Prob1'] * simresults_other['Elast Fare1 Opt1'] / denominator_Opt1_other).sum()
agg_cross_elas_Fare1_Opt2_other = (simresults_other['Prob2'] * simresults_other['Elast Fare1 Opt2'] / denominator_Opt2_other).sum()
agg_cross_elas_Fare1_Opt3_other = (simresults_other['Prob3'] * simresults_other['Elast Fare1 Opt3'] / denominator_Opt3_other).sum()

print(f"Aggregate direct elasticity of Opt1 wrt Fare1 (self): {agg_direct_elas_Fare1_Opt1_self:.3g}")
print(f"Aggregate cross elasticity of Opt2 wrt Fare1 (self): {agg_cross_elas_Fare1_Opt2_self:.3g}")
print(f"Aggregate cross elasticity of Opt3 wrt Fare1 (self): {agg_cross_elas_Fare1_Opt3_self:.3g}")
print(f"Aggregate direct elasticity of Opt1 wrt Fare1 (other): {agg_direct_elas_Fare1_Opt1_other:.3g}")
print(f"Aggregate cross elasticity of Opt2 wrt Fare1 (other): {agg_cross_elas_Fare1_Opt2_other:.3g}")
print(f"Aggregate cross elasticity of Opt3 wrt Fare1 (other): {agg_cross_elas_Fare1_Opt3_other:.3g}")
