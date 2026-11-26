# Regression Analysis: From Foundations to Mastery — Lesson 2.5
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 2.5 — Interpreting Coefficients in Multiple Regression
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")
auto <- na.omit(auto)                                   # 392 cars with horsepower
auto$w <- auto$weight / 1000; auto$hp <- auto$horsepower / 100
fit <- lm(mpg ~ w + model_year + hp, data = auto)
summary(fit)$coefficients

# Frisch-Waugh-Lovell for weight
ry <- residuals(lm(mpg ~ model_year + hp, data = auto))
rw <- residuals(lm(w ~ model_year + hp, data = auto))
c(fwl_slope = sum(rw * ry) / sum(rw^2), full_coef = unname(coef(fit)["w"]))
max(abs((ry - coef(fit)["w"] * rw) - residuals(fit)))

rh  <- residuals(lm(hp ~ w + model_year, data = auto))
ryh <- residuals(lm(mpg ~ w + model_year, data = auto))
op <- par(mfrow = c(1, 2))
plot(rw, ry, pch = 16, col = rgb(0, 0, 0, 0.35),
     xlab = "weight | others", ylab = "mpg | others", main = "Weight")
abline(0, coef(fit)["w"], lwd = 2)
plot(rh, ryh, pch = 16, col = rgb(0, 0, 0, 0.35),
     xlab = "horsepower | others", ylab = "mpg | others", main = "Horsepower")
abline(0, coef(fit)["hp"], lwd = 2)
par(op)

# Uses auto and fit from Section 5.2 (run that code first).
short <- lm(mpg ~ w + hp, data = auto)
Delta <- coef(lm(model_year ~ w + hp, data = auto))
b <- coef(fit)
rbind(short_model = coef(short),
      identity = b[c("(Intercept)", "w", "hp")] + Delta * b["model_year"])

vif <- sapply(c("w", "model_year", "hp"), function(v) {
  others <- setdiff(c("w", "model_year", "hp"), v)
  Rj2 <- summary(lm(reformulate(others, v), data = auto))$r.squared
  1 / (1 - Rj2)
})
Sjj <- sapply(auto[c("w", "model_year", "hp")], function(x) sum((x - mean(x))^2))
cbind(VIF = vif, se_formula = sigma(fit) * sqrt(vif / Sjj),
      se_lm = summary(fit)$coefficients[-1, 2])

# Self-contained: reads the 392 predictor rows and needs nothing from earlier sections.
cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- na.omit(read.table("data/auto-mpg.data", col.names = cols, na.strings = "?"))
X  <- cbind(1, auto$weight / 1000, auto$model_year, auto$horsepower / 100)
X1 <- X[, c(1, 2, 4)]                                   # short model: no model year
n <- nrow(X); beta <- c(-13.7, -6.45, 0.749, -0.50); sigma <- 3.43; R <- 10000
A_full  <- solve(crossprod(X), t(X))
A_short <- solve(crossprod(X1), t(X1))
Delta <- drop(A_short %*% X[, 3])
set.seed(2026)
Y <- matrix(drop(X %*% beta), R, n, byrow = TRUE) + matrix(rnorm(R * n, 0, sigma), R, n)
B_full <- Y %*% t(A_full); B_short <- Y %*% t(A_short)
rmse <- function(est, truth) sqrt(mean((est - truth)^2))
data.frame(
  coef = c("weight", "horsepower"),
  truth = beta[c(2, 4)],
  predicted_short = beta[c(2, 4)] + Delta[2:3] * beta[3],
  full_mean = colMeans(B_full[, c(2, 4)]), full_sd = apply(B_full[, c(2, 4)], 2, sd),
  short_mean = colMeans(B_short[, 2:3]), short_sd = apply(B_short[, 2:3], 2, sd),
  rmse_full = c(rmse(B_full[, 2], beta[2]), rmse(B_full[, 4], beta[4])),
  rmse_short = c(rmse(B_short[, 2], beta[2]), rmse(B_short[, 3], beta[4])))
