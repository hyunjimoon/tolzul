# Use R, check each of these examples separately
# true model: y = 1.5 + 1*x + 1*z + epsilon
# intercept = 1.5, both coefficients = 1.0

# Reading data for CCS2
# CS2_data <- read_csv("CaseStudy2_Tran.csv")
# CS2_data <- CS2_data[complete.cases(CS2_data), ]

################################### EXAMPLE 1 ###################################
# Multicollinearity: small sample + small correlation
# gamma determines the correlation between x and z
# small gamma -> low correlation
set.seed(42)
N=100
gamma = 0.05

# Assigning variables
z <- rnorm(N, 1, 1)
x <- gamma*z + rnorm(N, 1, 0.4)
y <- 1.5 + z + x + rnorm(N, 0, 1)

# Regression
# Here we are regressing y on x and y
ex1 <- lm(y ~ x + z)

# Display regression results
summary(ex1)

################################### EXAMPLE 2 ###################################
# Multicollinearity: small sample + large correlation
# large gamma -> high correlation
set.seed(32)
N=100
gamma = 5

# Assigning variables
z <- rnorm(N, 1, 1)
x <- gamma*z + rnorm(N, 1, 0.4)
y <- 1.5 + z + x + rnorm(N, 0, 1)

# Regression
ex2 <- lm(y ~ x + z)
summary(ex2)

################################### EXAMPLE 3 ###################################
# Multicollinearity: large sample + large correlation
# large gamma -> high correlation
# but sample size is large
set.seed(32)
N=100000
gamma = 5

# Assigning variables
z <- rnorm(N, 1, 1)
x <- gamma*z + rnorm(N, 1, 0.4)
y <- 1.5 + z + x + rnorm(N, 0, 1)

# Regression
ex3 <- lm(y ~ x + z)
summary(ex3)

################################### EXAMPLE 4 ###################################
# Heteroscedasticity: testing for presence by plotting epsilon vs x and z
set.seed(42)
N=1000
gamma = 0.05

# Assigning variables
z <- rnorm(N, 1, 1)
x <- gamma*z + rnorm(N, 1, 0.4)
y <- 1.5 + z + x + rnorm(N, 0, 1)

# Regression
ex4 <- lm(y ~ x + z)

# Epsilon
epsilon = ex4$residuals
plot(x, epsilon)
plot(z, epsilon)
# The epsilon has a constant variance = 1, independent of the x and z

################################### EXAMPLE 5 ###################################
# Heteroscedasticity: testing for presence by plotting epsilon vs x and z
set.seed(42)
N=1000
gamma = 0.05

# Assigning variables
z <- rnorm(N, 1, 1)
x <- gamma*z + rnorm(N, 1, 0.4)
# In this example, we make the variance of epsilon a function of x
y <- NULL
for(i in 1:N){y[i] <- 1.5 + z[i] + x[i] + rnorm(1, 0, abs(x[i]))}

# Regression
ex5 <- lm(y ~ x + z)

# Epsilon
epsilon = ex5$residuals
plot(x, epsilon)
# The epsilon has heteroscedasticity

########################## Calculating Standard Errors ##########################

##### Regular standard errors
X <- cbind(1, x, z)
exSE <- lm(y ~ x + z)

# Check the standard errors from the regression
summary(exSE)

# Alternatively, you can calculate them manually
Vmat = (var(epsilon) * solve(t(X)%*%X)) * N / (N - 2)
sqrt(diag(Vmat))

# Or use a separate library
library(sandwich)
sqrt(diag(vcov(exSE)))

# Check that the three methods are the same

##### Robust standard errors
# Manual
V = diag(epsilon^2)
Vmat = solve(t(X)%*%X)%*%t(X)%*%(V)%*%X%*%solve(t(X)%*%X) * N / (N - 3)
sqrt(diag(Vmat))

# Using sandwich library
sqrt(diag(vcovHC(exSE, type = "HC0")))

################################### EXAMPLE 6 ###################################
# Omitted variable bias with correlation between x and z
set.seed(42)
N=1000
gamma = -0.5

# Assigning variables
z <- rnorm(N, 1, 1)
x <- gamma*z + rnorm(N, 1, 0.4)
y <- 1.5 + z + x + rnorm(N, 0, 1)

# Regression
ex61 <- lm(y ~ x + z)
summary(ex61)

# Regression on only x (omitting z)
ex62 <- lm(y ~ x)
summary(ex62)

# Regression on only z (omitting x)
ex63 <- lm(y ~ z)
summary(ex63)

################################### EXAMPLE 7 ###################################
# Measurement error
set.seed(42)
N=1000

# Assigning variables
x <- rnorm(N, 1, 0.4)
z <- rnorm(N, 1, 1)
Xerr <- x + rnorm(N, 0, 0.5)
y <- 1.5 + z + x + rnorm(N, 0, 1)

# Regression
ex7 <- lm(y ~ Xerr + z)
summary(ex7)

##### To find endogeneity, try plotting the error vs x or z
