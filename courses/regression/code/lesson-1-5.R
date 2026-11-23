# Regression Analysis: From Foundations to Mastery — Lesson 1.5
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 1.5 — Interpreting the Coefficients
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")

summarise_fit <- function(x, y) {
  s <- summary(lm(y ~ x))
  c(b0 = coef(s)[1, 1], b1 = coef(s)[2, 1], se_b0 = coef(s)[1, 2],
    se_b1 = coef(s)[2, 2], t_b1 = coef(s)[2, 3], R2 = s$r.squared)
}
versions <- list(
  pounds           = auto$weight,
  hundreds_lb      = auto$weight / 100,
  thousands_lb     = auto$weight / 1000,
  thousands_kg     = auto$weight * 0.45359237 / 1000,
  centred_3000lb   = (auto$weight - 3000) / 1000)
round(t(sapply(versions, summarise_fit, y = auto$mpg)), 6)

# Uses auto from Section 5.1 (run that code first).
fit <- lm(mpg ~ I(weight / 1000), data = auto)
predict(fit, newdata = data.frame(weight = c(1000, 6000)))   # extrapolation
range(auto$weight)

auto$L100km <- 235.214583 / auto$mpg                          # non-linear change
coef(lm(L100km ~ I(weight / 1000), data = auto))
summary(lm(L100km ~ I(weight / 1000), data = auto))$r.squared

b_log <- unname(coef(lm(log(mpg) ~ I(weight / 1000), data = auto))[2])
c(b_log = b_log, pct_per_1000lb = 100 * (exp(b_log) - 1),
  pct_per_100lb = 100 * (exp(b_log / 10) - 1))
