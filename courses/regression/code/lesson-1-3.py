# Regression Analysis: From Foundations to Mastery — Lesson 1.3
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 1.3 — Ordinary Least Squares Estimation
 Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).
"""

import numpy as np
import pandas as pd

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"')
x = auto["weight"].to_numpy() / 1000          # weight in 1000 lb
y = auto["mpg"].to_numpy()

# From the formulas
Sxx = np.sum((x - x.mean())**2)
Sxy = np.sum((x - x.mean()) * (y - y.mean()))
b1 = Sxy / Sxx
b0 = y.mean() - b1 * x.mean()
print(f"n = {len(y)}, b0 = {b0:.6f}, b1 = {b1:.6f}")

# The same fit by solving the least-squares problem directly
X = np.column_stack([np.ones_like(x), x])
coef, *_ = np.linalg.lstsq(X, y, rcond=None)
print("lstsq:", coef)

# Theorem 1.3.2: the identities hold up to floating-point error
yhat = X @ coef
e = y - yhat
print(f"sum e = {e.sum():.2e}, sum x*e = {(x*e).sum():.2e}, sum yhat*e = {(yhat*e).sum():.2e}")

import matplotlib.pyplot as plt
grid = np.linspace(x.min(), x.max(), 100)
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(x, y, s=12, alpha=0.35, color="black")
ax.plot(grid, b0 + b1 * grid, linewidth=2)
ax.plot(x.mean(), y.mean(), marker="x", markersize=12, markeredgewidth=2)
ax.set_xlabel("Weight (1000 lb)")
ax.set_ylabel("Fuel economy (mpg)")
plt.show()