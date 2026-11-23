# Regression Analysis: From Foundations to Mastery — Lesson 2.3
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 2.3 — Least Squares in Matrix Form
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")
auto$w <- auto$weight / 1000
X <- model.matrix(~ w + model_year, data = auto)
y <- auto$mpg

b_ne <- solve(crossprod(X), crossprod(X, y))          # normal equations
qx <- qr(X)
b_qr <- qr.coef(qx, y)                                 # QR: solves R b = Q'y
fit <- lm(mpg ~ w + model_year, data = auto)
cbind(normal_eq = drop(b_ne), qr = b_qr, lm = coef(fit))
max(abs(drop(b_ne) - b_qr))
c(kappa_X = kappa(X, exact = TRUE), kappa_XtX = kappa(crossprod(X), exact = TRUE))

# Uses auto, X, y and fit from Section 5.1 (run that code first).
h <- hatvalues(fit)                                    # diag(H), computed via QR
e <- residuals(fit)
c(trace_H = sum(h), sum_e = sum(e), max_abs_Xte = max(abs(crossprod(X, e))))
SST <- sum((y - mean(y))^2); SSE <- sum(e^2); SSR <- sum((fitted(fit) - mean(y))^2)
c(SST = SST, SSR = SSR, SSE = SSE, R2 = SSR / SST)
c(mean_h = mean(h), min_h = min(h), max_h = max(h))
top <- order(h, decreasing = TRUE)[1:5]
data.frame(auto[top, c("car_name", "weight", "model_year")], h = round(h[top], 4))

# Uses auto, X and h from Sections 5.1-5.2 (run that code first).
XtX_inv <- solve(crossprod(X))
new <- rbind(c(1, 3.0, 76), c(1, 2.5, 82), c(1, 4.5, 82))
h00 <- rowSums((new %*% XtX_inv) * new)
round(h00, 4)
plot(auto$weight, auto$model_year + 1900, cex = 0.4 + 60 * h, pch = 1,
     xlab = "Weight (lb)", ylab = "Model year", xlim = c(1500, 5200), ylim = c(1969.5, 1983.8))
points(new[, 2] * 1000, new[, 3] + 1900, pch = 4, cex = 2, lwd = 3, col = "red")
text(new[, 2] * 1000, new[, 3] + 1900, sprintf("h00 = %.4f", h00), pos = 3, col = "red")

# Uses auto and y from Section 5.1 (run that code first).
auto$weight_kg <- auto$weight * 0.45359237
fit_both <- lm(mpg ~ weight + weight_kg, data = auto)
coef(fit_both)                                         # NA for the aliased column
fit_lb <- lm(mpg ~ weight, data = auto)
max(abs(fitted(fit_both) - fitted(fit_lb)))
