# Michel Bierlaire
# Sun Oct 21 23:27:59 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.expressions import Beta, DefineVariable

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
FareInc	 = Beta('FareInc',0,None,None,0)
Income2	 = Beta('Income2',0,None,None,0)
Income3	 = Beta('Income3',0,None,None,0)
MI_2	 = Beta('MI_2',0,None,None,0)
MI_3	 = Beta('MI_3',0,None,None,0)
Legroom	 = Beta('Legroom',0,None,None,0)
SchedDE	 = Beta('SchedDE',0,None,None,0)
SchedDL	 = Beta('SchedDL',0,None,None,0)
Total_TT	 = Beta('Total_TT',0,None,None,0)

# Define here arithmetic expressions for name that are not directly available from the data

# Dummy variable for missing income
MissingIncome  = DefineVariable('MissingIncome', Cont_Income == -1 ,database)

# Continous income if available, 0 otherwise
ContinuousIncome  = DefineVariable('ContinuousIncome', (Cont_Income != -1) * Cont_Income ,database)

# Fare divided by income, if income available, 0 otherwise
FarePerIncome_1 = DefineVariable('FarePerIncome_1',( Cont_Income != -1 ) * Fare_1 / Cont_Income ,database)
FarePerIncome_2 = DefineVariable('FarePerIncome_2',( Cont_Income != -1 ) * Fare_2 / Cont_Income ,database)
FarePerIncome_3 = DefineVariable('FarePerIncome_3',( Cont_Income != -1 ) * Fare_3 / Cont_Income ,database)
DepartureTimeSensitive  = DefineVariable('DepartureTimeSensitive', q11_DepartureOrArrivalIsImportant   ==  1 ,database)
ArrivalTimeSensitive  = DefineVariable('ArrivalTimeSensitive', q11_DepartureOrArrivalIsImportant   ==  2 ,database)
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
Opt1 = Constant1  + Fare * Fare_1 + FareInc * FarePerIncome_1  + Legroom * Legroom_1 + SchedDE * Opt1_SchedDelayEarly + SchedDL * Opt1_SchedDelayLate + Total_TT * TripTimeHours_1
Opt2 = Constant2 + Fare * Fare_2 + FareInc * FarePerIncome_2  + Legroom * Legroom_2 + SchedDE * Opt2_SchedDelayEarly + SchedDL * Opt2_SchedDelayLate + Total_TT * TripTimeHours_2 + Income2 * ContinuousIncome / 1000 + MI_2 * MissingIncome
Opt3 = Constant3 + Fare * Fare_3 + FareInc * FarePerIncome_3  + Legroom * Legroom_3 + SchedDE * Opt3_SchedDelayEarly + SchedDL * Opt3_SchedDelayLate + Total_TT * TripTimeHours_3 + Income3 * ContinuousIncome / 1000 + MI_3 * MissingIncome
V = {1: Opt1,2: Opt2,3: Opt3}
av = {1: 1,2: 1,3: 1}

# The choice model is a logit, with availability conditions
logprob = models.loglogit(V,av,chosenAlternative)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "logit_airline_socioecon"
results = biogeme.estimate()
# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)
print(f"Nbr of observations: {database.getNumberOfObservations()}")
print(f"LL(0) =    {results.data.initLogLike:.3f}")
print(f"LL(beta) = {results.data.logLike:.3f}")
print(f"rho bar square = {results.data.rhoBarSquare:.3g}")
print(f"Output file: {results.data.htmlFileName}")

