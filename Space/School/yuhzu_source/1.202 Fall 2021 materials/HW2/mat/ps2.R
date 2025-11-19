setwd('C:\\Users\\Yuzhu\\OneDrive - Massachusetts Institute of Technology\\Spring_2022\\1.202\\HW2')
library(purrr)
library(tidyr)
library(ggplot2)
library(Hmisc)

# Problem 1: Aggregate Trip Generation Rates
data = read.csv('CaseStudy1_Data.csv')
summary(data)
pairs(data)
hist.data.frame(data,nclass = 5) # data hist
cor(data, method = c("pearson", "kendall", "spearman")) # correlation matrix
lm1 <- lm(TODU ~ ACO + AHS + SI + SRI + UI, data = data)
summary(lm1)
lm2 <- lm(TODU ~ ACO + UI, data = data)
summary(lm2)
lm3 <- lm(TODU ~ ACO, data = data)
summary(lm3)

# Problem 2: Simulation Exercise
# a)
gamma = 0.5772
eta = 3
mu = 1.2

