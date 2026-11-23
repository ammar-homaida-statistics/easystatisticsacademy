# Regression Analysis: From Foundations to Mastery — Lesson 1.9
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 1.9 — Case Study: A Complete Simple Regression Analysis
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")
auto$w <- auto$weight / 1000

# Step 1: know the data
summary(auto[, c("mpg", "weight")])
table(auto$origin)

# Steps 3-5: fit, fit quality, inference
fit <- lm(mpg ~ w, data = auto)
summary(fit)
confint(fit)

# Step 6: prediction for a 2800-lb car
predict(fit, data.frame(w = 2.8), interval = "confidence")
predict(fit, data.frame(w = 2.8), interval = "prediction")

# Uses auto and fit from Section 5, Step 3 (run that code first).
e <- resid(fit)
six <- cut(auto$w, quantile(auto$w, seq(0, 1, length.out = 7)), include.lowest = TRUE)
round(rbind(mean_resid = tapply(e, six, mean), sd_resid = tapply(e, six, sd)), 2)

op <- par(mfrow = c(1, 2), mar = c(4, 4, 1, 1))
plot(auto$w, auto$mpg, pch = 16, col = rgb(0, 0, 0, 0.3),
     xlab = "Weight (1000 lb)", ylab = "Fuel economy (mpg)")
abline(fit, lwd = 2)
plot(auto$w, e, pch = 16, col = rgb(0, 0, 0, 0.3),
     xlab = "Weight (1000 lb)", ylab = "Residual (mpg)")
abline(h = 0, lty = 2)
points(tapply(auto$w, six, mean), tapply(e, six, mean), pch = 19, cex = 1.6, type = "b", lwd = 2)
par(op)

# The five largest residuals
head(auto[order(-abs(e)), c("car_name", "weight", "mpg", "model_year")], 5)
