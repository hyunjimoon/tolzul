setwd('C:\\Users\\Yuzhu\\OneDrive - Massachusetts Institute of Technology\\Spring_2022\\1.202\\HW3')
library(ggplot2)
library(dplyr)

d <- read.csv(file='CaseStudy2_Tran.csv')
d$vmt_p_veh <- d$vmt*1000000 / (d$vehicles * 1000)
d[ d == "." ] <- NA
d <- mutate_all(d, function(x) as.numeric(as.character(x)))
d <- d[complete.cases(d), ]

# a - create variables
d_shifted <- d[-(1),]

# VMT variables
vmt_mdata <- data.frame(ln_vmt_p_veh = log(d_shifted$vmt*1000000 / (d_shifted$vehicles * 1000)))
vmt_mdata$ln_gdp_p_capita <- log(d_shifted$gdpcap)
vmt_mdata$ln_pgas_p_gal <- log(d_shifted$pgas)
vmt_mdata$ln_mpg <- log(d_shifted$mpg)
vmt_mdata$ln_veh_p_driv <- log(d_shifted$vehdriv)
vmt_mdata$ln_psuburbs <- log(d_shifted$psuburbs)
vmt_mdata$ln_vmt_p_veh_t_minus_1 <- log(d$vmt_p_veh[-(nrow(d))])

# Veh variables
veh_mdata <- data.frame(ln_veh_p_driv = log(d_shifted$vehdriv))
veh_mdata$ln_gdp_p_capita <- log(d_shifted$gdpcap)
veh_mdata$ln_pgas_p_gal <- log(d_shifted$pgas)
veh_mdata$ln_pveh <- log(d_shifted$pvehicle)
veh_mdata$ln_lfp <- log(d_shifted$lfp)
veh_mdata$ln_psuburbs <- log(d_shifted$psuburbs)
veh_mdata$ln_veh_p_driv_t_minus_1 <- log(d$vehdriv[-(nrow(d))])

# b - OLS
vmt_lm <- lm(ln_vmt_p_veh ~ ln_gdp_p_capita + ln_pgas_p_gal + ln_mpg + ln_veh_p_driv + ln_psuburbs + ln_vmt_p_veh_t_minus_1, data=vmt_mdata)
summary(vmt_lm)


veh_lm <- lm(ln_veh_p_driv ~ ln_gdp_p_capita + ln_pgas_p_gal + ln_pveh + ln_lfp + ln_psuburbs + ln_veh_p_driv_t_minus_1, data=veh_mdata)
summary(veh_lm)

# c - DW
# VMT
r_vmt <- data.frame(residuals = residuals(vmt_lm)[-(1)])
r_vmt$residuals_t_minus_1 <- residuals(vmt_lm)[-(length(residuals(vmt_lm)))]
r_vmt$sum_squared <- (r_vmt$residuals-r_vmt$residuals_t_minus_1)^2
s1 <- sum(r_vmt$sum_squared)
s2 <- sum((residuals(vmt_lm))^2)
DW = s1 / s2
r_vmt_lm <- lm(residuals ~ residuals_t_minus_1, data=r_vmt)
summary(r_vmt_lm)

# veh Model
r_veh <- data.frame(residuals = residuals(veh_lm)[-(1)])
r_veh$residuals_t_minus_1 <- residuals(veh_lm)[-(length(residuals(veh_lm)))]
r_veh$sum_squared <- (r_veh$residuals-r_veh$residuals_t_minus_1)^2
s1 <- sum(r_veh$sum_squared)
s2 <- sum((residuals(veh_lm))^2)
DW = s1 / s2
r_veh_lm <- lm(residuals ~ residuals_t_minus_1, data=r_veh)
summary(r_veh_lm)

# d - OLS without lagged endogenous variable
vmt_mdata2 <- data.frame(ln_vmt_p_veh = log(d$vmt*1000000 / (d$vehicles * 1000)))
vmt_mdata2$ln_gdp_p_capita <- log(d$gdpcap)
vmt_mdata2$ln_pgas_p_gal <- log(d$pgas)
vmt_mdata2$ln_mpg <- log(d$mpg)
vmt_mdata2$ln_veh_p_driv <- log(d$vehdriv)
vmt_mdata2$ln_psuburbs <- log(d$psuburbs)

vmt_lm2 <- lm(ln_vmt_p_veh ~ ln_gdp_p_capita + ln_pgas_p_gal + ln_mpg + ln_veh_p_driv + ln_psuburbs, data=vmt_mdata2)
summary(vmt_lm2)

vmt_mdata2$ln_roadcap <- log(d$roadcap)
vmt_mdata2$ln_roads <- log(d$roads)
vmt_mdata2$ln_p_veh <- log(d$pvehicle)

# my proposed model
vmt_lm3 <- lm(ln_vmt_p_veh ~ ln_gdp_p_capita + ln_pgas_p_gal + ln_mpg + ln_veh_p_driv, data=vmt_mdata2)
summary(vmt_lm3)

r_vmt2 <- data.frame(residuals = residuals(vmt_lm2)[-(1)])
r_vmt2$residuals_t_minus_1 <- residuals(vmt_lm2)[-(length(residuals(vmt_lm2)))]
r_vmt2$sum_squared <- (r_vmt2$residuals-r_vmt2$residuals_t_minus_1)^2
s1 <- sum(r_vmt2$sum_squared)
s2 <- sum((residuals(vmt_lm2))^2)
DW = s1 / s2

# e - Cochrane-Orcutt
rhos <- c(-99, summary(r_vmt_lm)$coefficients[2,1])


co_update_rho <- function(rho_hat, vmt_mdata) {
  vmt_mdata_t <- vmt_mdata[-(1),]
  vmt_mdata_t_minus_1 <- vmt_mdata[-(nrow(vmt_mdata)),]
  
  vmt_co_mdata <- data.frame(ln_vmt_p_veh_star = vmt_mdata_t$ln_vmt_p_veh - rho_hat*vmt_mdata_t_minus_1$ln_vmt_p_veh)
  vmt_co_mdata$ln_gdp_p_capita_star <- vmt_mdata_t$ln_gdp_p_capita - rho_hat*vmt_mdata_t_minus_1$ln_gdp_p_capita
  vmt_co_mdata$ln_pgas_p_gal_star <- vmt_mdata_t$ln_pgas_p_gal - rho_hat*vmt_mdata_t_minus_1$ln_pgas_p_gal
  vmt_co_mdata$ln_mpg_star <- vmt_mdata_t$ln_mpg - rho_hat*vmt_mdata_t_minus_1$ln_mpg
  vmt_co_mdata$ln_veh_p_driv_star <- vmt_mdata_t$ln_veh_p_driv - rho_hat*vmt_mdata_t_minus_1$ln_veh_p_driv
  vmt_co_mdata$ln_psuburbs_star <- vmt_mdata_t$ln_psuburbs - rho_hat*vmt_mdata_t_minus_1$ln_psuburbs
  vmt_co_mdata$ln_vmt_p_veh_t_minus_1_star <- vmt_mdata_t$ln_vmt_p_veh_t_minus_1 - rho_hat*vmt_mdata_t_minus_1$ln_vmt_p_veh_t_minus_1
  
  vmt_co_lm <- lm(ln_vmt_p_veh_star ~ ln_gdp_p_capita_star + ln_pgas_p_gal_star + ln_mpg_star + ln_veh_p_driv_star + ln_psuburbs_star + ln_vmt_p_veh_t_minus_1_star , data=vmt_co_mdata)
  summary(vmt_co_lm)
  
  beta_hat_1 <- c(summary(vmt_co_lm)$coefficients[1,1] / (1 - rho_hat))
  beta_hat_2_to_7 = summary(vmt_co_lm)$coefficients[(2:7),1]
  beta_hats <- append(beta_hat_1, beta_hat_2_to_7)
  #print(beta_hats)
  
  residuals_after_co <- vmt_mdata$ln_vmt_p_veh - beta_hat_1 - data.matrix(vmt_mdata[,(2:7)])%*% matrix(beta_hat_2_to_7)
  
  r_vmt_after_co <- data.frame(residuals = residuals_after_co[-(1)])
  r_vmt_after_co$residuals_t_minus_1 <- residuals_after_co[-(length(residuals_after_co))]
  r_vmt_after_co$sum_squared <- (r_vmt_after_co$residuals-r_vmt_after_co$residuals_t_minus_1)^2
  
  r_vmt_after_co_lm <- lm(residuals ~ residuals_t_minus_1, data=r_vmt_after_co)
  rho_hat_after_co <- summary(r_vmt_after_co_lm)$coefficients[2,1]
  
  co_results <- list("rho_hat_after_co" = rho_hat_after_co, "beta_hats" = beta_hats, "residuals_after_co" = residuals_after_co)
  return(co_results)
}

beta_hats <- c()
residuals_after_co <- data.frame()
threshold = 0.01
while (abs(rhos[length(rhos)] - rhos[length(rhos)-1]) > threshold) {
  results = co_update_rho(rhos[length(rhos)], vmt_mdata)
  rhos <- append(rhos, results$rho_hat_after_co)
  beta_hats <- results$beta_hats
  residuals_after_co <- results$residuals_after_co
}

# R-squared
SSR <- sum(residuals_after_co^2)
SST <- sum((vmt_mdata$ln_vmt_p_veh - mean(vmt_mdata$ln_vmt_p_veh))^2)
R_squared <- 1- SSR / SST
N <- nrow(vmt_mdata)
K <- 7
adjusted_R_squared <- 1- (SSR*(N-K)) / (SST*(N-1))

# f - repeating b, d, and e using data through 1970
# see hw3_part_f.r

# g - forecast for 2016
summary(vmt_lm)

# last record of valid data: 1990
cols <- c('gdpcap', 'pgas', 'mpg', 'vehdriv', 'psuburbs')

raw_d <- read.csv(file='CaseStudy2_Tran.csv')
raw_d$vmt_p_veh <- raw_d$vmt*1000000 / (raw_d$vehicles * 1000)
raw_d[ raw_d == "." ] <- NA
raw_d <- mutate_all(raw_d, function(x) as.numeric(as.character(x)))

forecast_mdata <- raw_d[(41:45),append(c('year', 'vmt', 'vehicles'),cols)]
row.names(forecast_mdata) <- NULL

forecast_mdata$ln_vmt_p_veh <- log(forecast_mdata$vmt*1000000 / (forecast_mdata$vehicles * 1000))

add_forecast_data <- function(year, forecast_mdata) {
  for (forecast_year in 1991:year) {
    # print(forecast_year)
    if (forecast_year %in% forecast_mdata$year) {
      this_row <- strtoi(rownames(forecast_mdata)[forecast_mdata$year==forecast_year])
    } else {
      old_nrows <- nrow(forecast_mdata)
      this_row <- old_nrows + 1
      forecast_mdata[this_row,'year'] <- forecast_year
    }
    # print(this_row)
    year_diff <- forecast_year - forecast_mdata[1,1]
    
    rates <- c(0.018, -0.008, 0.007, 0, 0.0017)
    
    for (i in 1:length(cols)) {
      if (is.null(forecast_mdata[this_row, cols[i]]) | is.na(forecast_mdata[this_row, cols[i]])) {
        forecast_mdata[this_row, cols[i]] <- forecast_mdata[this_row-1, cols[i]]*((1+rates[i])^1)
      }
    }
    y_hat <- -1
    if (is.null(forecast_mdata[this_row, "ln_vmt_p_veh"]) | is.na(forecast_mdata[this_row, "ln_vmt_p_veh"])) {
      print(forecast_year)
      print(this_row)
      print(forecast_mdata[this_row-1, "ln_vmt_p_veh"])
      y_hat <- beta_hats[1] + 
      beta_hats["ln_gdp_p_capita_star"]*log(forecast_mdata[this_row, "gdpcap"]) + 
      beta_hats["ln_pgas_p_gal_star"]*log(forecast_mdata[this_row, "pgas"]) + 
      beta_hats["ln_mpg_star"]*log(forecast_mdata[this_row, "mpg"]) + 
      beta_hats["ln_veh_p_driv_star"]*log(forecast_mdata[this_row, "vehdriv"]) + 
      beta_hats["ln_psuburbs_star"]*log(forecast_mdata[this_row, "psuburbs"]) + 
      beta_hats["ln_vmt_p_veh_t_minus_1_star"]*forecast_mdata[this_row-1, "ln_vmt_p_veh"]
      forecast_mdata[this_row, "ln_vmt_p_veh"] <- y_hat
      print(y_hat)
    }
  }
  return(forecast_mdata)
}


forecast_mdata <- add_forecast_data(2016, forecast_mdata)

plot(forecast_mdata$year, exp(forecast_mdata$ln_vmt_p_veh))
