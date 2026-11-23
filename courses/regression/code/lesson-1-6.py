# Regression Analysis: From Foundations to Mastery — Lesson 1.6
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 1.6 — Goodness of Fit
 Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).
"""

import numpy as np
import pandas as pd

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"')
x = auto["weight"].to_numpy() / 1000
y = auto["mpg"].to_numpy()
n = len(y)

def ols(x, y):
    Sxx = np.sum((x - x.mean())**2)
    b1 = np.sum((x - x.mean()) * (y - y.mean())) / Sxx
    return y.mean() - b1 * x.mean(), b1

b0, b1 = ols(x, y)
yhat = b0 + b1 * x
SST = np.sum((y - y.mean())**2)
SSE = np.sum((y - yhat)**2)
SSR = np.sum((yhat - y.mean())**2)
print(f"SST = {SST:.4f}, SSR = {SSR:.4f}, SSE = {SSE:.4f}, SSR + SSE = {SSR + SSE:.4f}")
print(f"R2 = {SSR / SST:.6f}, r^2 = {np.corrcoef(x, y)[0, 1]**2:.6f}, "
      f"corr(y, yhat)^2 = {np.corrcoef(y, yhat)[0, 1]**2:.6f}")
print(f"sigma_hat = {np.sqrt(SSE / (n - 2)):.4f}, s_y = {y.std(ddof=1):.4f}")

# Uses np and ols from Section 5.1 (run that code first).
import matplotlib.pyplot as plt

x123 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], dtype=float)
x4   = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8], dtype=float)
ys = {
    1: [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68],
    2: [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74],
    3: [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73],
    4: [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89],
}
fig, axes = plt.subplots(2, 2, figsize=(7, 5.5), sharex=True, sharey=True)
grid = np.array([3, 20])
for k, ax in zip(ys, axes.ravel()):
    xk = x4 if k == 4 else x123
    yk = np.array(ys[k])
    a0, a1 = ols(xk, yk)
    ek = yk - a0 - a1 * xk
    R2k = 1 - ek @ ek / np.sum((yk - yk.mean())**2)
    print(f"set {k}: b0 = {a0:.4f}, b1 = {a1:.4f}, R2 = {R2k:.4f}, sigma = {np.sqrt(ek @ ek / 9):.4f}")
    ax.scatter(xk, yk, color="black", s=20)
    ax.plot(grid, a0 + a1 * grid, linewidth=2)
    ax.set_title(f"Data set {k}")
plt.tight_layout()
plt.show()
