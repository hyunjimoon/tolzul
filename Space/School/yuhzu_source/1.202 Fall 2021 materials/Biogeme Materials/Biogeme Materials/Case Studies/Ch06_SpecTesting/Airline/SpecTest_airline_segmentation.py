# Michel Bierlaire
# Tue Oct 23 16:22:45 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.expressions import Beta, DefineVariable, log

df = pd.read_csv("airline.dat",'\t')
database = db.Database("airline",df)
pd.options.display.float_format = '{:.3g}'.format
globals().update(database.variables)


database.remove(ArrivalTimeHours_1   ==  -1)

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

# Define here arithmetic expressions for name that are not directly 
# available from the data

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

# Duplicate the database
database_NA = db.Database("airline_NA",pd.DataFrame.copy(database.data))
database_males = db.Database("airline_males",pd.DataFrame.copy(database.data))
database_females = db.Database("airline_females",pd.DataFrame.copy(database.data))

# Remove observations
database_NA.remove(((  q17_Gender   ==  1  ) + (  q17_Gender   ==  2  )) > 0)
database_males.remove(((  q17_Gender   ==  2  ) + (  q17_Gender   ==  -1  ) + (  q17_Gender   ==  99  )) > 0)
database_females.remove(((  q17_Gender   ==  1  ) + (  q17_Gender   ==  -1  ) + (  q17_Gender   ==  99  )) > 0)
print(f"Total number of observations: {database.getNumberOfObservations()}")
print(f"Females                     : {database_females.getNumberOfObservations()}")
print(f"Males                       : {database_males.getNumberOfObservations()}")
print(f"NA                          : {database_NA.getNumberOfObservations()}")



#Utilities
Opt1 = Constant1 + Fare * Fare_1 + Legroom * Legroom_1 + SchedDE * Opt1_SchedDelayEarly + SchedDL * Opt1_SchedDelayLate + Total_TT1 * TripTimeHours_1
Opt2 = Constant2 + Fare * Fare_2 + Legroom * Legroom_2 + SchedDE * Opt2_SchedDelayEarly + SchedDL * Opt2_SchedDelayLate + Total_TT2 * TripTimeHours_2
Opt3 = Constant3 + Fare * Fare_3 + Legroom * Legroom_3 + SchedDE * Opt3_SchedDelayEarly + SchedDL * Opt3_SchedDelayLate + Total_TT3 * TripTimeHours_3
V = {1: Opt1,2: Opt2,3: Opt3}
av = {1: 1,2: 1,3: 1}

# The choice model is a logit, with availability conditions
logprob = models.loglogit(V,av,chosenAlternative)

biogeme_full  = bio.BIOGEME(database,logprob)
biogeme_full.modelName = "fullSample"
results_full = biogeme_full.estimate()
ll_full = results_full.data.logLike

biogeme_females  = bio.BIOGEME(database_females,logprob)
biogeme_females.modelName = "females"
results_females = biogeme_females.estimate()
ll_females = results_females.data.logLike

biogeme_males  = bio.BIOGEME(database_males,logprob)
biogeme_males.modelName = "males"
results_males = biogeme_males.estimate()
ll_males = results_males.data.logLike

biogeme_NA  = bio.BIOGEME(database_NA,logprob)
biogeme_NA.modelName = "NA"
results_NA = biogeme_NA.estimate()
ll_NA = results_NA.data.logLike


print(f"LL full:    {ll_full:.3f} Parameters: {results_full.data.nparam}")
print(f"LL females: {ll_females:.3f}  Parameters: {results_females.data.nparam}")
print(f"LL males:   {ll_males:.3f} Parameters: {results_males.data.nparam}")
print(f"LL NA:      {ll_NA:.3f}  Parameters: {results_NA.data.nparam}")
unrestricted = ll_females+ll_males+ll_NA
print(f"Sum LL :    {unrestricted:.3f}")
lr = -2 * (ll_full - unrestricted)
print(f"likelihood ratio: {lr:.3f}")
