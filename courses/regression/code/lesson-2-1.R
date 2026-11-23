# Regression Analysis: From Foundations to Mastery — Lesson 2.1
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 2.1 — From One Predictor to Many
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")
auto$w <- auto$weight / 1000                                   # 1000 lb

m_w  <- lm(mpg ~ w, data = auto)
m_yr <- lm(mpg ~ model_year, data = auto)
m_2  <- lm(mpg ~ w + model_year, data = auto)
summary(m_2)$coefficients
c(R2_w = summary(m_w)$r.squared, R2_yr = summary(m_yr)$r.squared,
  R2_both = summary(m_2)$r.squared, sigma_both = sigma(m_2))

# Centred intercept: mean mpg of a 3000-lb car from 1976
coef(lm(mpg ~ I(w - 3) + I(model_year - 76), data = auto))

# Theorem 2.1.1
delta <- unname(coef(lm(model_year ~ w, data = auto))[2])
b <- unname(coef(m_2))
c(simple_slope = unname(coef(m_w)[2]), partial = b[2], beta2_times_delta = b[3] * delta,
  partial_plus_indirect = b[2] + b[3] * delta, delta = delta)

# Uses auto, b and m_w from Section 5.2 (run that code first).
pal <- colorRampPalette(c("#2c7bb6", "#e6862a", "#d7191c"))(13)
plot(auto$w, auto$mpg, pch = 16, col = adjustcolor(pal[auto$model_year - 69], 0.6),
     xlab = "Weight (1000 lb)", ylab = "Fuel economy (mpg)")
for (yy in c(70, 76, 82))
  abline(a = b[1] + b[3] * yy, b = b[2], lwd = 2, col = pal[yy - 69])
abline(m_w, lwd = 2, lty = 2)
legend("topright", c("1970", "1976", "1982", "weight only"), lwd = 2,
       lty = c(1, 1, 1, 2), col = c(pal[c(1, 7, 13)], "black"), bty = "n")

# Uses auto and b from Section 5.2 (run that code first).
sum(b * c(1, 4.5, 82))                                          # 4500-lb car, 1982
max(auto$weight[auto$model_year == 82])
sum(auto$model_year >= 80 & auto$weight > 3500)
plot(auto$model_year, auto$weight, xlab = "Model year", ylab = "Weight (lb)")
points(82, 4500, pch = 4, cex = 2, lwd = 3, col = "red")
