# Regression Analysis: From Foundations to Mastery — Lesson 1.8
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 1.8 — Confidence Intervals for the Mean Response and Prediction Intervals
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

x <- c(2.226, 3.84, 3.235, 2.897, 2.842, 4.367, 4.768, 2.221, 3.885, 2.644, 4.984, 4.819, 3.826,
       4.235, 3.403, 4.491, 3.169, 2.786, 2.573, 2.392, 3.44, 3.108, 3.921, 1.645, 3.167)
y <- c(36.16, 13.58, 26.48, 18.77, 24.81, 7.7, 14.69, 32.24, 20.64, 22.1, 10.36, 6.81, 14.71,
       15.42, 23.3, 12.24, 19.08, 21.25, 31.97, 29.96, 22.39, 30.8, 12.54, 43.57, 34.22)
fit <- lm(y ~ x)
new <- data.frame(x = c(3.0, 5.0))
predict(fit, new, interval = "confidence", level = 0.95)
predict(fit, new, interval = "prediction", level = 0.95)
c(true_mean_at_3 = 46 - 7.7 * 3, true_mean_at_5 = 46 - 7.7 * 5)

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")
auto$w <- auto$weight / 1000
fit_auto <- lm(mpg ~ w, data = auto)
predict(fit_auto, data.frame(w = c(2.0, 3.0, 4.5)), interval = "confidence")
predict(fit_auto, data.frame(w = c(2.0, 3.0, 4.5)), interval = "prediction")

grid <- data.frame(w = seq(min(auto$w), max(auto$w), length.out = 200))
ci <- predict(fit_auto, grid, interval = "confidence")
pi <- predict(fit_auto, grid, interval = "prediction")
plot(auto$w, auto$mpg, pch = 16, col = rgb(0, 0, 0, 0.3),
     xlab = "Weight (1000 lb)", ylab = "Fuel economy (mpg)")
polygon(c(grid$w, rev(grid$w)), c(pi[, "lwr"], rev(pi[, "upr"])),
        col = rgb(0, 0.5, 0.5, 0.15), border = NA)
polygon(c(grid$w, rev(grid$w)), c(ci[, "lwr"], rev(ci[, "upr"])),
        col = rgb(0, 0.5, 0.5, 0.5), border = NA)
lines(grid$w, ci[, "fit"], lwd = 2)

# In-sample check: proportion of cars inside their 95% prediction interval, by weight third
pi_obs <- predict(fit_auto, auto, interval = "prediction")
inside <- auto$mpg >= pi_obs[, "lwr"] & auto$mpg <= pi_obs[, "upr"]
third <- cut(auto$w, quantile(auto$w, c(0, 1/3, 2/3, 1)), include.lowest = TRUE,
             labels = c("light", "medium", "heavy"))
round(c(all = mean(inside), tapply(inside, third, mean)), 3)
