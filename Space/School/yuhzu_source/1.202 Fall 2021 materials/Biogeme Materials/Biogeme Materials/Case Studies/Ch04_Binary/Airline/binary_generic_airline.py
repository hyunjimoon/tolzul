# Translated to .py by Anna Fernandez
# 30.09.2016
# Adapted to PandasBiogeme by Michel Bierlaire
# Sun Oct 21 22:38:31 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.expressions import Beta, DefineVariable

df = pd.read_csv("airline.dat", '\t')
database = db.Database("airline", df)
pd.options.display.float_format = '{:.3g}'.format

globals().update(database.variables)

# Exclude
exclude = ((ArrivalTimeHours_1 == -1) + BestAlternative_3) != 0
database.remove(exclude)

# How is choice coded in the dataset:
__chosenAlternative = (BestAlternative_1 * 1) + (BestAlternative_2 * 2)

# Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
Constant1 = Beta('Constant1', 0, None, None, 1)
Constant2 = Beta('Constant2', 0, None, None, 0)
Fare = Beta('Fare', 0, None, None, 0)
Legroom = Beta('Legroom', 0, None, None, 0)
SchedDE = Beta('SchedDE', 0, None, None, 0)
SchedDL = Beta('SchedDL', 0, None, None, 0)
Total_TT = Beta('Total_TT', 0, None, None, 0)

# Define here arithmetic expressions for name that are not directly
# available from the data

Subj_Income = DefineVariable('Subj_Income',
                             (q16_Income == 1) * 10 +
                             (q16_Income == 2) * 20 +
                             (q16_Income == 3) * 30 +
                             (q16_Income == 4) * 40 +
                             (q16_Income == 5) * 50 +
                             (q16_Income == 6) * 60 +
                             (q16_Income == 7) * 70 +
                             (q16_Income == 8) * 80 +
                             (q16_Income == 9) * 92.5 +
                             (q16_Income == 10) * 112.5 +
                             (q16_Income == 11) * 137.5 +
                             (q16_Income == 12) * 162.5 +
                             (q16_Income == 13) * 187.5 +
                             (q16_Income == 14) * 350 +
                             (q16_Income == -1) * 100 +
                             (q16_Income == 99) * 100, database)
Opt1_Legroom = DefineVariable('Opt1_Legroom', (Legroom_1 - 2) * 2, database)
Opt2_Legroom = DefineVariable('Opt2_Legroom', (Legroom_2 - 2) * 2, database)
Opt3_Legroom = DefineVariable('Opt3_Legroom', (Legroom_3 - 2) * 2, database)
Opt1_Fare = DefineVariable('Opt1_Fare', Fare_1 / 100, database)
Opt2_Fare = DefineVariable('Opt2_Fare', Fare_2 / 100, database)
Opt3_Fare = DefineVariable('Opt3_Fare', Fare_3 / 100, database)
DepartureTimeSensitive = DefineVariable('DepartureTimeSensitive', q11_DepartureOrArrivalIsImportant == 1, database)
ArrivalTimeSensitive = DefineVariable('ArrivalTimeSensitive', q11_DepartureOrArrivalIsImportant == 2, database)
Missing = DefineVariable('Missing', (q11_DepartureOrArrivalIsImportant != 1) * (q11_DepartureOrArrivalIsImportant != 2),
                         database)
DesiredDepartureTime = DefineVariable('DesiredDepartureTime', q12_IdealDepTime, database)
DesiredArrivalTime = DefineVariable('DesiredArrivalTime', q13_IdealArrTime, database)
ScheduledDelay_1 = DefineVariable('ScheduledDelay_1',
                                  (DepartureTimeSensitive * (DepartureTimeMins_1 - DesiredDepartureTime)) + (
                                              ArrivalTimeSensitive * (ArrivalTimeMins_1 - DesiredArrivalTime)),
                                  database)
ScheduledDelay_2 = DefineVariable('ScheduledDelay_2',
                                  (DepartureTimeSensitive * (DepartureTimeMins_2 - DesiredDepartureTime)) + (
                                              ArrivalTimeSensitive * (ArrivalTimeMins_2 - DesiredArrivalTime)),
                                  database)
ScheduledDelay_3 = DefineVariable('ScheduledDelay_3',
                                  (DepartureTimeSensitive * (DepartureTimeMins_3 - DesiredDepartureTime)) + (
                                              ArrivalTimeSensitive * (ArrivalTimeMins_3 - DesiredArrivalTime)),
                                  database)
Opt1_SchedDelayEarly = DefineVariable('Opt1_SchedDelayEarly', (-(ScheduledDelay_1) * (ScheduledDelay_1 < 0)) / 60,
                                      database)
Opt2_SchedDelayEarly = DefineVariable('Opt2_SchedDelayEarly', (-(ScheduledDelay_2) * (ScheduledDelay_2 < 0)) / 60,
                                      database)
Opt3_SchedDelayEarly = DefineVariable('Opt3_SchedDelayEarly', (-(ScheduledDelay_3) * (ScheduledDelay_3 < 0)) / 60,
                                      database)
Opt1_SchedDelayLate = DefineVariable('Opt1_SchedDelayLate', (ScheduledDelay_1 * (ScheduledDelay_1 > 0)) / 60, database)
Opt2_SchedDelayLate = DefineVariable('Opt2_SchedDelayLate', (ScheduledDelay_2 * (ScheduledDelay_2 > 0)) / 60, database)
Opt3_SchedDelayLate = DefineVariable('Opt3_SchedDelayLate', (ScheduledDelay_3 * (ScheduledDelay_3 > 0)) / 60, database)

# Utilities
__Opt1 = Constant1 + Fare * Opt1_Fare + Legroom * Opt1_Legroom + SchedDE * Opt1_SchedDelayEarly + SchedDL * Opt1_SchedDelayLate + Total_TT * TripTimeHours_1
__Opt2 = Constant2 + Fare * Opt2_Fare + Legroom * Opt2_Legroom + SchedDE * Opt2_SchedDelayEarly + SchedDL * Opt2_SchedDelayLate + Total_TT * TripTimeHours_2
__V = {1: __Opt1, 2: __Opt2}
__av = {1: 1, 2: 1}

# The choice model is a logit, with availability conditions
logprob = models.loglogit(__V, __av, __chosenAlternative)
biogeme = bio.BIOGEME(database, logprob)
biogeme.modelName = "binary_generic_airline"
results = biogeme.estimate()
# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)
print(f"Nbr of observations: {database.getNumberOfObservations()}")
print(f"LL(0) =    {results.data.initLogLike:.3f}")
print(f"LL(beta) = {results.data.logLike:.3f}")
print(f"rho bar square = {results.data.rhoBarSquare:.3g}")
print(f"Output file: {results.data.htmlFileName}")
