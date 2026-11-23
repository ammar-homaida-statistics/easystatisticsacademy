# Regression Analysis: From Foundations to Mastery — Lesson 1.9
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 1.9 — Case Study: A Complete Simple Regression Analysis
 Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).
"""

import numpy as np
import pandas as pd
from scipy import stats

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"')
x = auto["weight"].to_numpy() / 1000
y = auto["mpg"].to_numpy()
n = len(y)

# Step 1: know the data
print(auto[["mpg", "weight"]].describe().round(2))
print(auto["origin"].value_counts().sort_index().to_dict())

# Steps 3-5: fit, fit quality, inference
Sxx = np.sum((x - x.mean())**2)
b1 = np.sum((x - x.mean()) * (y - y.mean())) / Sxx
b0 = y.mean() - b1 * x.mean()
fitted = b0 + b1 * x
e = y - fitted
s = np.sqrt(e @ e / (n - 2))
se1 = s / np.sqrt(Sxx)
q = stats.t.ppf(0.975, n - 2)
R2 = 1 - (e @ e) / np.sum((y - y.mean())**2)
print(f"b0 = {b0:.4f}, b1 = {b1:.4f} (se {se1:.4f}), 95% CI ({b1 - q * se1:.4f}, {b1 + q * se1:.4f})")
print(f"t = {b1 / se1:.2f}, R2 = {R2:.4f}, sigma_hat = {s:.4f}")

# Step 6: prediction for a 2800-lb car
x0 = 2.8
h0 = 1 / n + (x0 - x.mean())**2 / Sxx
y0 = b0 + b1 * x0
print(f"x0 = 2800 lb: fit {y0:.3f}, CI ({y0 - q * s * np.sqrt(h0):.3f}, {y0 + q * s * np.sqrt(h0):.3f}), "
      f"PI ({y0 - q * s * np.sqrt(1 + h0):.3f}, {y0 + q * s * np.sqrt(1 + h0):.3f})")

# Uses np, pd, auto, x, y, b0, b1 and e from Section 5, Step 3 (run that code first).
import matplotlib.pyplot as plt

six = pd.qcut(x, 6)
res = pd.DataFrame({"w": x, "e": e, "six": six})
by_six = res.groupby("six", observed=True).agg(w_mean=("w", "mean"), mean_resid=("e", "mean"),
                                               sd_resid=("e", "std"))
print(by_six.round(2))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.6))
ax1.scatter(x, y, s=10, alpha=0.3, color="black")
grid = np.linspace(x.min(), x.max(), 100)
ax1.plot(grid, b0 + b1 * grid, linewidth=2)
ax1.set_xlabel("Weight (1000 lb)"); ax1.set_ylabel("Fuel economy (mpg)")
ax2.scatter(x, e, s=10, alpha=0.3, color="black")
ax2.axhline(0, linestyle="--", color="gray")
ax2.plot(by_six["w_mean"], by_six["mean_resid"], marker="o", markersize=8, linewidth=2)
ax2.set_xlabel("Weight (1000 lb)"); ax2.set_ylabel("Residual (mpg)")
plt.tight_layout()
plt.show()

top = np.argsort(-np.abs(e))[:5]
print(auto.loc[top, ["car_name", "weight", "mpg", "model_year"]].assign(residual=e[top].round(2)))
