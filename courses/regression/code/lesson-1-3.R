# Regression Analysis: From Foundations to Mastery — Lesson 1.3
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 1.3 — Ordinary Least Squares Estimation
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")
auto$weight_k <- auto$weight / 1000            # weight in 1000 lb

# From the formulas
x <- auto$weight_k; y <- auto$mpg
Sxx <- sum((x - mean(x))^2)
Sxy <- sum((x - mean(x)) * (y - mean(y)))
b1  <- Sxy / Sxx
b0  <- mean(y) - b1 * mean(x)
c(n = length(y), b0 = b0, b1 = b1)

# The same fit with lm()
fit <- lm(mpg ~ weight_k, data = auto)
coef(fit)

# Theorem 1.3.2: the identities hold up to floating-point error
e <- resid(fit)
c(sum_e = sum(e), sum_xe = sum(x * e), sum_yhat_e = sum(fitted(fit) * e))

plot(auto$weight_k, auto$mpg, pch = 16, col = rgb(0, 0, 0, 0.35),
     xlab = "Weight (1000 lb)", ylab = "Fuel economy (mpg)")
abline(fit, lwd = 2)
points(mean(auto$weight_k), mean(auto$mpg), pch = 4, cex = 2, lwd = 2)