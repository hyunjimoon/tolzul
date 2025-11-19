# Michel Bierlaire
# Thu Nov  1 16:06:52 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.models import logit
from biogeme.expressions import Beta, DefineVariable, log
import matplotlib.pyplot as plt
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
Constant1	 = Beta('Constant1',0,None,None,1)
Constant2	 = Beta('Constant2',0,None,None,0)
Constant3	 = Beta('Constant3',0,None,None,0)
Fare	 = Beta('Fare',0,None,None,0)
Legroom	 = Beta('Legroom',0,None,None,0)
SchedDE	 = Beta('SchedDE',0,None,None,0)
SchedDL	 = Beta('SchedDL',0,None,None,0)
Total_TT1	 = Beta('Total_TT1',0,None,None,0)
Total_TT2	 = Beta('Total_TT2',0,None,None,0)
Total_TT3	 = Beta('Total_TT3',0,None,None,0)

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

# Function that calculates the market shares for Non-Stop for a given scaling of the cost

def scenario(costScale,database):
    Opt1 = Constant1 + Fare * Fare_1 * costScale + Legroom * Legroom_1 + SchedDE * Opt1_SchedDelayEarly + SchedDL * Opt1_SchedDelayLate + Total_TT1 * TripTimeHours_1
    V = {1: Opt1,2: Opt2,3: Opt3}
    prob_1 = logit(V,av,1)
    simulate = {'Prob1': prob_1}
    biosim  = bio.BIOGEME(database,simulate)
    biosim.modelName = f"marketShares_Op1_{costScale}"
    simresults = biosim.simulate(dict(zip(results.data.betaNames, results.data.betaValues)))
    return 100*simresults['Prob1'].mean()

scales = np.arange(0.8,1.3,0.1)
shares_self = [scenario(s,database_self) for s in scales]
shares_other = [scenario(s,database_other) for s in scales]

fig, ax = plt.subplots()
ax.plot(100*scales,shares_self,label='Travelers pay')
ax.plot(100*scales,shares_other,label='Others pay')
ax.legend()
plt.xlabel("Modification of non-stop fare (%)")
plt.ylabel("Market shares of non-stop (%)")
plt.show()
