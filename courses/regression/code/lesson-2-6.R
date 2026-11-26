# Regression Analysis: From Foundations to Mastery — Lesson 2.6
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 2.6 — Inference for Coefficients and Linear Combinations
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- na.omit(read.table("data/auto-mpg.data", col.names = cols, na.strings = "?"))
auto$w <- auto$weight / 1000; auto$hp <- auto$horsepower / 100
fit <- lm(mpg ~ w + model_year + hp, data = auto)
m <- df.residual(fit); c(df = m, sigma_hat = sigma(fit), t_crit = qt(0.975, m))
cbind(summary(fit)$coefficients, confint(fit))

# Uses auto and fit from Section 5.1 (run that code first).
new <- data.frame(w = c(3.0, 2.2, 2.0), model_year = c(76, 80, 82), hp = c(1.0, 0.7, 2.0))
X0 <- model.matrix(~ w + model_year + hp, data = new)
h00 <- rowSums((X0 %*% solve(crossprod(model.matrix(fit)))) * X0)
cbind(h00 = round(h00, 4),
      predict(fit, new, interval = "confidence"),
      predict(fit, new, interval = "prediction")[, -1])
max(hatvalues(fit))

# Uses auto and fit from Section 5.1 (run that code first).
b <- coef(fit); V <- vcov(fit); m <- df.residual(fit)
idx <- c("w", "hp"); bS <- b[idx]; VS <- V[idx, idx]
cov2cor(VS)
Fq <- qf(0.95, 2, m)
Fstat <- function(theta) drop(t(bS - theta) %*% solve(VS) %*% (bS - theta)) / 2
c(F_A = Fstat(c(-5.7, 1.3)), F_B = Fstat(c(-7.4, 1.6)), F_crit = Fq)

ang <- seq(0, 2 * pi, length.out = 400)
ell <- t(bS + t(chol(VS)) %*% rbind(cos(ang), sin(ang)) * sqrt(2 * Fq))
ci <- confint(fit)[idx, ]
bonf <- cbind(bS - qt(1 - 0.05 / 4, m) * sqrt(diag(VS)), bS + qt(1 - 0.05 / 4, m) * sqrt(diag(VS)))
plot(ell, type = "l", lwd = 2, xlab = "weight slope (mpg per 1000 lb)",
     ylab = "horsepower slope (mpg per 100 hp)", xlim = c(-7.8, -5.2), ylim = c(-3.2, 2.2))
rect(ci[1, 1], ci[2, 1], ci[1, 2], ci[2, 2], lty = 2)
rect(bonf[1, 1], bonf[2, 1], bonf[1, 2], bonf[2, 2], lty = 3)
points(bS[1], bS[2], pch = 19)
points(c(-5.7, -7.4), c(1.3, 1.6), pch = 4, cex = 1.5, lwd = 2, col = "red")
text(c(-5.7, -7.4), c(1.3, 1.6), c("A", "B"), pos = 3, col = "red")

# Self-contained: reads the 392 predictor rows and needs nothing from earlier sections.
cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- na.omit(read.table("data/auto-mpg.data", col.names = cols, na.strings = "?"))
X <- cbind(1, auto$weight / 1000, auto$model_year, auto$horsepower / 100)
n <- nrow(X); m <- n - ncol(X)
beta <- c(-13.7, -6.45, 0.749, -0.50); sigma <- 3.43; R <- 10000
XtX_inv <- solve(crossprod(X)); A <- XtX_inv %*% t(X)
set.seed(2026)
Y <- matrix(drop(X %*% beta), R, n, byrow = TRUE) + matrix(rnorm(R * n, 0, sigma), R, n)
B <- Y %*% t(A); s2 <- rowSums((Y - B %*% t(X))^2) / m
idx <- c(2, 4); W_inv <- solve(XtX_inv[idx, idx])
D <- sweep(B[, idx], 2, beta[idx])                     # estimation errors
se1 <- sqrt(s2 * XtX_inv[2, 2]); se2 <- sqrt(s2 * XtX_inv[4, 4])
qi <- qt(0.975, m); qb <- qt(1 - 0.05 / 4, m); Fq <- qf(0.95, 2, m)
c1 <- abs(D[, 1]) <= qi * se1; c2 <- abs(D[, 2]) <= qi * se2
Fs <- rowSums((D %*% W_inv) * D) / (2 * s2)
c(weight_alone = mean(c1), hp_alone = mean(c2), both_separate = mean(c1 & c2),
  both_bonferroni = mean(abs(D[, 1]) <= qb * se1 & abs(D[, 2]) <= qb * se2),
  ellipse = mean(Fs <= Fq))
