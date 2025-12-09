# Translated to .py by Jing Ding-Mastera
# 2017
# Adapted to PandasBiogeme by Michel Bierlaire
# Thu Nov  1 19:03:06 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
from biogeme.models import logit
from datetime import datetime

pandas = pd.read_table("airline.dat")
database = db.Database("airline",pandas)
pd.options.display.float_format = '{:.3g}'.format

globals().update(database.variables)
from biogeme.expressions import *

  
# Choice
chosenAlternative = ( (  BestAlternative_1   *  1  ) + (  BestAlternative_2   *  2  ) ) + (  BestAlternative_3   *  3  )

#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_1 = Beta('ASC_1',0,None,None,1)
ASC_2 = Beta('ASC_2',0,None,None,0)
ASC_3 = Beta('ASC_3',0,None,None,0)
BETA_LogFare_Business = Beta('BETA_LogFare_Business',0,None,None,0)
BETA_LogFare_NonBusiness = Beta('BETA_LogFare_NonBusiness',0,None,None,0)
BETA_TotalTripTime = Beta('BETA_TotalTripTime',0,None,None,0)
BETA_TotalTripTime_std = Beta('BETA_TotalTripTime_std',0,None,None,0)
BETA_Legroom = Beta('BETA_Legroom',0,None,None,0)
BETA_SchedDelayEarly	 = Beta('BETA_SchedDelayEarly',0,None,None,0)
BETA_SchedDelayLate	 = Beta('BETA_SchedDelayLate',0,None,None,0)

# Define a random parameter, normally distirbuted, designed to be used
# for Monte-Carlo simulation
B_TIME_RND = BETA_TotalTripTime + BETA_TotalTripTime_std * bioDraws('B_TIME_RND','NORMAL')

# Define here arithmetic expressions for name that are not directly available from the data

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

Opt1LogFare_Business    =  DefineVariable('Opt1LogFare_Business',log( Fare_1 ) * ( TripPurpose == 1 ),database)
Opt1LogFare_NonBusiness =  DefineVariable('Opt1LogFare_NonBusiness',log( Fare_1 ) * ( TripPurpose != 1 ),database)
Opt2LogFare_Business    =  DefineVariable('Opt2LogFare_Business',log( Fare_2 ) * ( TripPurpose == 1 ),database)
Opt2LogFare_NonBusiness =  DefineVariable('Opt2LogFare_NonBusiness',log( Fare_2 ) * ( TripPurpose != 1 ),database)
Opt3LogFare_Business    =  DefineVariable('Opt3LogFare_Business',log( Fare_3 ) * ( TripPurpose == 1 ),database)
Opt3LogFare_NonBusiness =  DefineVariable('Opt3LogFare_NonBusiness',log( Fare_3 ) * ( TripPurpose != 1 ),database) 

# Utilities
Opt1 = ASC_1 + BETA_LogFare_Business * Opt1LogFare_Business + BETA_LogFare_NonBusiness * Opt1LogFare_NonBusiness + B_TIME_RND * TripTimeHours_1 + BETA_Legroom * Legroom_1 + BETA_SchedDelayEarly * Opt1_SchedDelayEarly + BETA_SchedDelayLate * Opt1_SchedDelayLate
Opt2 = ASC_2 + BETA_LogFare_Business * Opt2LogFare_Business + BETA_LogFare_NonBusiness * Opt2LogFare_NonBusiness + B_TIME_RND * TripTimeHours_2 + BETA_Legroom * Legroom_2 + BETA_SchedDelayEarly * Opt2_SchedDelayEarly + BETA_SchedDelayLate * Opt2_SchedDelayLate
Opt3 = ASC_3 + BETA_LogFare_Business * Opt3LogFare_Business + BETA_LogFare_NonBusiness * Opt3LogFare_NonBusiness + B_TIME_RND * TripTimeHours_3 + BETA_Legroom * Legroom_3 + BETA_SchedDelayEarly * Opt3_SchedDelayEarly + BETA_SchedDelayLate * Opt3_SchedDelayLate

V = {1: Opt1,2: Opt2,3: Opt3}
av = {1: 1,2: 1,3: 1}


# MNL (Multinomial Logit model), with availability conditions
prob = logit(V,av,chosenAlternative)
logprob = log(MonteCarlo(prob))

biogeme = bio.BIOGEME(database,logprob,numberOfDraws=1000)
biogeme.modelName = "Mixture_airline"
start_time = datetime.now()
results = biogeme.estimate()
print(f"Estimation time: {datetime.now() - start_time}")
# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)
print(f"Nbr of observations: {database.getNumberOfObservations()}")
print(f"LL(0) =    {results.data.initLogLike:.3f}")
print(f"LL(beta) = {results.data.logLike:.3f}")
print(f"rho bar square = {results.data.rhoBarSquare:.3g}")
print(f"Output file: {results.data.htmlFileName}")
