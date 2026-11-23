# Regression Analysis: From Foundations to Mastery — Lesson 2.2
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 2.2 — The Matrix Formulation
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")
auto$w <- auto$weight / 1000

X <- model.matrix(~ w + model_year, data = auto)   # the design matrix
y <- auto$mpg
head(X, 3)
XtX <- crossprod(X)                                # t(X) %*% X
Xty <- crossprod(X, y)
XtX; Xty
qr(X)$rank
ev <- eigen(XtX, symmetric = TRUE)$values
ev; max(ev) / min(ev)                              # condition number
solve(XtX, Xty)                                    # same estimates as Lesson 2.1

Xc <- model.matrix(~ I(w - 3) + I(model_year - 76), data = auto)
evc <- eigen(crossprod(Xc), symmetric = TRUE)$values
max(evc) / min(evc)

# Uses auto from Section 5.1 (run that code first).
X_units <- cbind(1, auto$weight, auto$weight * 0.45359237)
qr(X_units)$rank
X_trap <- cbind(1, sapply(1:3, function(k) as.numeric(auto$origin == k)))
qr(X_trap)$rank
round(eigen(crossprod(X_trap), symmetric = TRUE)$values, 6)

# Self-contained: needs nothing from earlier sections.
set.seed(2026)
n <- 5; mu <- 1:5; sigma <- 2; R <- 1e5
C <- diag(n) - matrix(1, n, n) / n
Y <- matrix(rnorm(R * n, sd = sigma), R, n) + matrix(mu, R, n, byrow = TRUE)
q <- rowSums((Y %*% C) * Y)                         # y' C y for every row
c(sim_mean = mean(q), mc_se = sd(q) / sqrt(R),
  theory = (n - 1) * sigma^2 + drop(t(mu) %*% C %*% mu))

A <- rbind(c(1, 1, 0, 0, 0) / 2, c(0, 0, 1, 1, 1) / 3)
Z <- Y %*% t(A)
colMeans(Z); drop(A %*% mu)
cov(Z); sigma^2 * A %*% t(A)
