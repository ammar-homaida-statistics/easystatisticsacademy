# Regression Analysis: From Foundations to Mastery — Lesson 1.2
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 1.2 — Correlation versus Regression
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")
x <- auto$weight / 1000; y <- auto$mpg

r  <- cor(x, y)
b1 <- r * sd(y) / sd(x)                       # Theorem 1.2.3(a)
g1 <- r * sd(x) / sd(y)                       # slope of x on y
c(r = r, sd_x = sd(x), sd_y = sd(y), b1 = b1, g1 = g1,
  product = b1 * g1, r_squared = r^2)

coef(lm(y ~ x))                               # same slope as b1
coef(lm(x ~ y))                               # same slope as g1
cor(auto$weight * 0.45359237, auto$mpg)       # weight in kg: r unchanged

# Uses x, y, b1 and g1 from Section 5.1 (run that code first).
plot(x, y, pch = 16, col = rgb(0, 0, 0, 0.3),
     xlab = "Weight (1000 lb)", ylab = "Fuel economy (mpg)")
abline(a = mean(y) - b1 * mean(x), b = b1, lwd = 2)
abline(a = mean(y) - mean(x) / g1, b = 1 / g1, lwd = 2, lty = 2)
points(mean(x), mean(y), pch = 4, cex = 2, lwd = 2)

# Uses x, y and r from Section 5.1 (run that code first).
zx <- (x - mean(x)) / sd(x); zy <- (y - mean(y)) / sd(y)
heavy <- x >= quantile(x, 0.9)
c(n = sum(heavy), mean_zx = mean(zx[heavy]),
  linear_prediction = r * mean(zx[heavy]), mean_zy = mean(zy[heavy]))
