# Michel Bierlaire
# Sun Oct 21 22:51:33 2018

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
exclude = ((  ArrivalTimeHours_1   ==  -1  )  + BestAlternative_3)!=0
database.remove(exclude)
  
# How is choice coded in the dataset:
__chosenAlternative = (  BestAlternative_1   *  1  ) + (  BestAlternative_2   *  2  )

#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
Constant1_MALE	 = Beta('Constant1_MALE',0,None,None,1)
Constant2_MALE	 = Beta('Constant2_MALE',0,None,None,0)
Fare_MALE	 = Beta('Fare_MALE',0,None,None,0)
Legroom_MALE	 = Beta('Legroom_MALE',0,None,None,0)
SchedDE_MALE	 = Beta('SchedDE_MALE',0,None,None,0)
SchedDL_MALE	 = Beta('SchedDL_MALE',0,None,None,0)
Total_TT_MALE	 = Beta('Total_TT_MALE',0,None,None,0)

Constant1_FEMALE	 = Beta('Constant1_FEMALE',0,None,None,1)
Constant2_FEMALE	 = Beta('Constant2_FEMALE',0,None,None,0)
Fare_FEMALE	 = Beta('Fare_FEMALE',0,None,None,0)
Legroom_FEMALE	 = Beta('Legroom_FEMALE',0,None,None,0)
SchedDE_FEMALE	 = Beta('SchedDE_FEMALE',0,None,None,0)
SchedDL_FEMALE	 = Beta('SchedDL_FEMALE',0,None,None,0)
Total_TT_FEMALE	 = Beta('Total_TT_FEMALE',0,None,None,0)




# Define here arithmetic expressions for name that are not directly  available from the data

Male  = DefineVariable('Male', q17_Gender   ==  1 ,database)
Female  = DefineVariable('Female', 1  -  Male  ,database)
Leisure  = DefineVariable('Leisure', TripPurpose   ==  2 ,database)
NonLeisure  = DefineVariable('NonLeisure', 1  -  Leisure  ,database)
Opt1_Fare  = DefineVariable('Opt1_Fare', Fare_1   /  100 ,database)
Opt2_Fare  = DefineVariable('Opt2_Fare', Fare_2   /  100 ,database)
Opt3_Fare  = DefineVariable('Opt3_Fare', Fare_3   /  100 ,database)
Opt1_LogFare  = DefineVariable('Opt1_LogFare', Fare_1   /  100 ,database)
Opt2_LogFare  = DefineVariable('Opt2_LogFare', Fare_2   /  100 ,database)
Opt3_LogFare  = DefineVariable('Opt3_LogFare', Fare_3   /  100 ,database)
Opt1_Legroom  = DefineVariable('Opt1_Legroom',(  Legroom_1   -  2  ) *  2 ,database)
Opt2_Legroom  = DefineVariable('Opt2_Legroom',(  Legroom_2   -  2  ) *  2 ,database)
Opt3_Legroom  = DefineVariable('Opt3_Legroom',(  Legroom_3   -  2  ) *  2 ,database)
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
__Opt1_MALE = Constant1_MALE + Fare_MALE * Opt1_Fare + Legroom_MALE * Opt1_Legroom + SchedDE_MALE * Opt1_SchedDelayEarly + SchedDL_MALE * Opt1_SchedDelayLate + Total_TT_MALE * TripTimeHours_1
__Opt2_MALE = Constant2_MALE + Fare_MALE * Opt2_Fare + Legroom_MALE * Opt2_Legroom + SchedDE_MALE * Opt2_SchedDelayEarly + SchedDL_MALE * Opt2_SchedDelayLate + Total_TT_MALE * TripTimeHours_2

__Opt1_FEMALE = Constant1_FEMALE + Fare_FEMALE * Opt1_Fare + Legroom_FEMALE * Opt1_Legroom + SchedDE_FEMALE * Opt1_SchedDelayEarly + SchedDL_FEMALE * Opt1_SchedDelayLate + Total_TT_FEMALE * TripTimeHours_1
__Opt2_FEMALE = Constant2_FEMALE + Fare_FEMALE * Opt2_Fare + Legroom_FEMALE * Opt2_Legroom + SchedDE_FEMALE * Opt2_SchedDelayEarly + SchedDL_FEMALE * Opt2_SchedDelayLate + Total_TT_FEMALE * TripTimeHours_2

__Opt1 = Male * __Opt1_MALE + Female * __Opt1_FEMALE
__Opt2 = Male * __Opt2_MALE + Female * __Opt2_FEMALE

__V = {1: __Opt1,2: __Opt2}
__av = {1: 1,2: 1}

# The choice model is a logit, with availability conditions
logprob = models.loglogit(__V,__av,__chosenAlternative)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "binary_socio_econ_airline"
results = biogeme.estimate()
# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)
print(f"Nbr of observations: {database.getNumberOfObservations()}")
print(f"LL(0) =    {results.data.initLogLike:.3f}")
print(f"LL(beta) = {results.data.logLike:.3f}")
print(f"rho bar square = {results.data.rhoBarSquare:.3g}")
print(f"Output file: {results.data.htmlFileName}")




