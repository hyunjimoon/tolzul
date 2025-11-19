setwd('C:\\Users\\Yuzhu\\OneDrive - Massachusetts Institute of Technology\\Spring_2022\\1.202\\HW2')
library(Hmisc)
library(ggplot2)
library(tidyr)
library(reshape2)

# ----------------------------------

# Problem 1
data <- read.csv(file='CaseStudy1_Data.csv')
attach(data)
summary(data)
hist.data.frame(data, nclass=5)

ggplot(data, aes(SRI,TODU))+
  geom_point(size=3)+
  theme(axis.text = element_text(size = 30), 
        axis.title = element_text(size = 30))

dmelt <- melt(data, id.vars='TODU', variable.name='series')
ggplot(dmelt, aes(TODU, value))+
  geom_point()+
  facet_grid(series ~ .)

round(cor(data),2)

lm1 <- lm(TODU ~ ACO + UI, data=data)
summary(lm1)

lm2 <- lm(TODU ~ ACO, data=data)
summary(lm2)

# ----------------------------------

# Problem 2

# The following random variable generating method is adopted from:
# https://stats.stackexchange.com/questions/88697/sample-from-a-custom-continuous-distribution-in-r

# part a
gumbel_pdf <- function(epsilon, mu, eta) {
  mu*exp(-mu*(epsilon-eta))*exp(-exp(-mu*(epsilon-eta)))
}

gumbel_cdf <- function(epsilon, mu, eta) {
  exp(-exp(-mu*(epsilon-eta)))
}

epsilon_min <- -100
epsilon_max <- 100
n_epsilon <- 5000000 # number of samples
mu <- 1.2
eta <- 3
gamma <- 0.5772

# true stats
true_mode <- eta
true_mean <- eta + gamma/mu
true_variance <- pi^2/(6*mu^2)

# simulate data
simulate_gumbel <- function(epsilon_min, epsilon_max, n_epsilon, mu, eta, gamma) {
  xy <- data.frame(proposed = runif(n_epsilon, min = epsilon_min, max = epsilon_max))
  
  xy$fit <- gumbel_pdf(xy$proposed, mu, eta)
  xy$random <- runif(n_epsilon, min = 0, max = 1)
  
  maxDens <- max(xy$fit)
  
  xy$accepted <- with(xy, random <= fit/maxDens)
  
  # retain only those values which are "below" the custom distribution
  xy <- xy[xy$accepted, ]
  return(xy$proposed)
}

simulated_epsilon <- simulate_gumbel(epsilon_min, epsilon_max, n_epsilon, mu, eta, gamma)

hist(simulated_epsilon, freq = FALSE, breaks = 100, col = "light grey",
     main=(paste("PDF of Gumbel(",round(eta,2),",",mu,")")), xlab='x')

curve(gumbel_pdf(x, mu, eta),
      from = epsilon_min, to = epsilon_max, n=n_epsilon, add = TRUE, col = "red", lwd = 2)

# simulated data stats

summary(simulated_epsilon)

mode<-function(x){which.max(tabulate(x))}
mode(simulated_epsilon)
var(simulated_epsilon)

# part b
eta_j <- 5
mu <- 1.2
J <- 1
N <- 10

eta <- 1/mu*log(J*exp(mu*eta_j))

ej_maxs <- list()
for (j in 1:J) {
  ej <- simulate_gumbel(epsilon_min, epsilon_max, n_epsilon, mu, eta_j, gamma)
  h_temp <- hist(ej, freq = FALSE, breaks = 100, col = "light grey",
       main=expression(paste("Histogram of ",epsilon)), xlab='x', xlim=c(0, max_es))
  breaks <- as.data.frame(h_temp$breaks)
  
  h <- merge(h, t_temp, by='breaks')
  # ej_max <- max(ej)
  # ej_maxs <- append(ej_maxs, ej_max)
}
hist(unlist(es), freq = FALSE, breaks = 100, col = "light grey",
     main=expression(paste("Histogram of ",epsilon)), xlab='x', xlim=c(0, max_es))

true_variance <- pi^2/(6*mu^2)
true_expected_value <- eta+gamma/mu

e <- simulate_gumbel(epsilon_min, epsilon_max, n_epsilon, mu, eta, gamma)
summary(e)
var(e)

max_es = ceiling(max(unlist(es)))
hist(unlist(es), freq = FALSE, breaks = 100, col = "light grey",
     main=expression(paste("Histogram of ",epsilon)), xlab='x', xlim=c(0, max_es))

curve(gumbel_pdf(x, mu, eta),
      from = epsilon_min, to = epsilon_max, n=n_epsilon, add = TRUE, col = "red", lwd = 2)

mean(unlist(es))
# part c
eta_js <- c(8, 8.2, 7.5, 7.8)
mu <- 1.2
J <- 4

# eta <- 1/mu*log(J*exp(mu*eta_j))
ejs <- list()
eta_components <- list()
for (eta_j in eta_js) {
  ej <- max(simulate_gumbel(epsilon_min, epsilon_max, n_epsilon, mu, eta_j, gamma))
  ejs <- append(ejs, ej)
  eta_component <- exp(mu*eta_j)
  eta_components <- append(eta_components, eta_component)
}

eta <- 1/mu*log(sum(eta_components))
true_variance <- pi^2/(6*mu^2)
true_expected_value <- eta+gamma/mu

e <- simulate_gumbel(epsilon_min, epsilon_max, n_epsilon, mu, eta, gamma)
summary(e)
var(e)

hist(e, freq = FALSE, breaks = 100, col = "light grey",
     main=(paste("PDF of Gumbel(",round(eta,2),",",mu,")")), xlab='x')

