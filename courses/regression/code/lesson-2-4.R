# Regression Analysis: From Foundations to Mastery — Lesson 2.4
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 2.4 — Properties of the OLS Estimator
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")
auto$w <- auto$weight / 1000
fit <- lm(mpg ~ w + model_year, data = auto)
X <- model.matrix(fit)
n <- nrow(X); df_res <- df.residual(fit)               # 395
SSE <- sum(residuals(fit)^2); s2 <- SSE / df_res
c(SSE = SSE, sigma2_hat = s2, sigma_hat = sqrt(s2))
V <- s2 * solve(crossprod(X))                          # same as vcov(fit)
V; max(abs(V - vcov(fit)))
sqrt(diag(V))                                          # standard errors
cov2cor(V)                                             # correlations of the estimates
cor(auto$w, auto$model_year)

lin_comb <- function(a, level = 0.95) {
  est <- sum(a * coef(fit)); se <- sqrt(drop(t(a) %*% V %*% a))
  q <- qt(1 - (1 - level) / 2, df_res)
  c(estimate = est, se = se, lower = est - q * se, upper = est + q * se)
}
rbind(mean_3000lb_1976 = lin_comb(c(1, 3, 76)),
      ten_years = lin_comb(c(0, 0, 10)))

# Self-contained: reads the 398 (weight, year) pairs and needs nothing from earlier sections.
cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")
X <- cbind(1, auto$weight / 1000, auto$model_year)
n <- nrow(X); m <- n - ncol(X)
XtX_inv <- solve(crossprod(X)); A <- XtX_inv %*% t(X)
beta <- c(-14.2, -6.66, 0.757); sigma <- 3.43; R <- 10000
set.seed(2026)

simulate <- function(E) {                               # E: R x n matrix of errors
  Y <- matrix(drop(X %*% beta), R, n, byrow = TRUE) + E
  B <- Y %*% t(A)                                       # R x 3 estimates
  S <- rowSums((Y - B %*% t(X))^2)                      # SSE
  q <- qt(0.975, m); se_w <- sqrt(S / m * XtX_inv[2, 2])
  list(B = B, S = S,
       summary = c(mean_bw = mean(B[, 2]), sd_bw = sd(B[, 2]), mean_s2 = mean(S / m),
                   mean_Q = mean(S / sigma^2), var_Q = var(S / sigma^2),
                   cor_bw_SSE = cor(B[, 2], S),
                   coverage = mean(abs(B[, 2] - beta[2]) <= q * se_w)))
}
norm <- simulate(matrix(rnorm(R * n, 0, sigma), R, n))
skew <- simulate(matrix(sigma * (rexp(R * n) - 1), R, n))
h <- rowSums((X %*% XtX_inv) * X)
round(cbind(normal = norm$summary, skewed = skew$summary,
            theory = c(beta[2], sigma * sqrt(XtX_inv[2, 2]), sigma^2, m, 2 * m, 0, 0.95)), 4)
c(var_Q_theory_kappa9 = 2 * m + 6 * sum((1 - h)^2))

op <- par(mfrow = c(1, 2))
hist(norm$S / sigma^2, breaks = 50, freq = FALSE, main = "Normal errors", xlab = "SSE / sigma^2",
     xlim = c(200, 600), ylim = c(0, 0.015))   # same scale in both panels
curve(dchisq(x, m), add = TRUE, lwd = 2)
hist(skew$S / sigma^2, breaks = 50, freq = FALSE, main = "Skewed errors", xlab = "SSE / sigma^2",
     xlim = c(200, 600), ylim = c(0, 0.015))   # same scale in both panels
curve(dchisq(x, m), add = TRUE, lwd = 2)
par(op)
