# Regression Analysis: From Foundations to Mastery — Lesson 1.6
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 1.6 — Goodness of Fit
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")
x <- auto$weight / 1000; y <- auto$mpg
fit <- lm(y ~ x)

SST <- sum((y - mean(y))^2)
SSE <- sum(resid(fit)^2)
SSR <- sum((fitted(fit) - mean(y))^2)
c(SST = SST, SSR = SSR, SSE = SSE, SSR_plus_SSE = SSR + SSE,
  R2 = SSR / SST, r_squared = cor(x, y)^2, corr_y_yhat_sq = cor(y, fitted(fit))^2,
  sigma_hat = sigma(fit), s_y = sd(y))
anova(fit)                       # the same decomposition as an ANOVA table

# 'anscombe' is a data set built into R
op <- par(mfrow = c(2, 2), mar = c(4, 4, 1, 1))
for (k in 1:4) {
  xk <- anscombe[[paste0("x", k)]]; yk <- anscombe[[paste0("y", k)]]
  fk <- lm(yk ~ xk)
  plot(xk, yk, pch = 19, xlim = c(3, 20), ylim = c(2, 14),
       xlab = paste0("x", k), ylab = paste0("y", k))
  abline(fk, lwd = 2)
  print(round(c(set = k, b0 = coef(fk)[[1]], b1 = coef(fk)[[2]],
                R2 = summary(fk)$r.squared, sigma = sigma(fk)), 4))
}
par(op)