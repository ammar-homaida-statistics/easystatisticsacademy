# Regression Analysis: From Foundations to Mastery — Lesson 1.7
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 1.7 — Inference for the Regression Parameters
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

x <- c(2.226, 3.84, 3.235, 2.897, 2.842, 4.367, 4.768, 2.221, 3.885, 2.644, 4.984, 4.819, 3.826,
       4.235, 3.403, 4.491, 3.169, 2.786, 2.573, 2.392, 3.44, 3.108, 3.921, 1.645, 3.167)
y <- c(36.16, 13.58, 26.48, 18.77, 24.81, 7.7, 14.69, 32.24, 20.64, 22.1, 10.36, 6.81, 14.71,
       15.42, 23.3, 12.24, 19.08, 21.25, 31.97, 29.96, 22.39, 30.8, 12.54, 43.57, 34.22)
fit <- lm(y ~ x)
summary(fit)$coefficients            # estimates, se, t and p-values for H0: beta = 0
confint(fit, level = 0.95)           # t-intervals for beta0 and beta1
anova(fit)                           # F = t^2

# Test H0: beta1 = -7.7 (the true value)
b1 <- coef(fit)[["x"]]; se1 <- coef(summary(fit))["x", "Std. Error"]
t_stat <- (b1 - (-7.7)) / se1
c(t = t_stat, p = 2 * pt(-abs(t_stat), df = df.residual(fit)))

# 95% interval for sigma^2
SSE <- deviance(fit); dfr <- df.residual(fit)
c(lower = SSE / qchisq(0.975, dfr), upper = SSE / qchisq(0.025, dfr))

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")
fit_auto <- lm(mpg ~ I(weight / 1000), data = auto)
summary(fit_auto)$coefficients
confint(fit_auto)
anova(fit_auto)
b1 <- coef(fit_auto)[[2]]; se1 <- coef(summary(fit_auto))[2, 2]
t8 <- (b1 - (-8)) / se1
c(t = t8, p = 2 * pt(-abs(t8), df.residual(fit_auto)))