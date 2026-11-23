# Regression Analysis: From Foundations to Mastery — Lesson 1.4
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 1.4 — Statistical Properties of the OLS Estimators
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")
x <- auto$weight / 1000; y <- auto$mpg; n <- length(y)

fit <- lm(y ~ x)
SSE <- sum(resid(fit)^2)
sigma2_hat <- SSE / (n - 2)
Sxx <- sum((x - mean(x))^2)
c(SSE = SSE, sigma2_hat = sigma2_hat, sigma_hat = sqrt(sigma2_hat),
  se_b1 = sqrt(sigma2_hat / Sxx),
  se_b0 = sqrt(sigma2_hat * (1 / n + mean(x)^2 / Sxx)),
  sigma2_ML = SSE / n)

summary(fit)$coefficients[, 1:2]   # lm() reports the same standard errors
vcov(fit)                           # estimated covariance matrix

# Self-contained: reads the 398 Auto MPG weights and needs nothing from earlier sections.
cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")
x <- auto$weight / 1000; n <- length(x); Sxx <- sum((x - mean(x))^2)

set.seed(2026)
R <- 10000; beta0 <- 46.3; beta1 <- -7.7; sigma <- 4.34
k <- (x - mean(x)) / Sxx
sims <- replicate(R, {
  ysim <- beta0 + beta1 * x + rnorm(n, 0, sigma)
  b1s <- sum(k * ysim); b0s <- mean(ysim) - b1s * mean(x)
  c(b0 = b0s, b1 = b1s, s2 = sum((ysim - b0s - b1s * x)^2) / (n - 2))
})
c(mean_b1 = mean(sims["b1", ]), sd_b1 = sd(sims["b1", ]),
  theory_sd_b1 = sigma / sqrt(Sxx),
  mean_s2 = mean(sims["s2", ]), sigma2 = sigma^2)
hist(sims["b1", ], breaks = 50, freq = FALSE,
     main = "", xlab = "Simulated slope estimates")
curve(dnorm(x, beta1, sigma / sqrt(Sxx)), add = TRUE, lwd = 2)
abline(v = beta1, lty = 2)
