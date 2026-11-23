# Regression Analysis: From Foundations to Mastery — Lesson 1.8
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 1.8 — Confidence Intervals for the Mean Response and Prediction Intervals
 Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).
"""

import numpy as np
from scipy import stats

x = np.array([2.226, 3.84, 3.235, 2.897, 2.842, 4.367, 4.768, 2.221, 3.885, 2.644, 4.984, 4.819, 3.826,
              4.235, 3.403, 4.491, 3.169, 2.786, 2.573, 2.392, 3.44, 3.108, 3.921, 1.645, 3.167])
y = np.array([36.16, 13.58, 26.48, 18.77, 24.81, 7.7, 14.69, 32.24, 20.64, 22.1, 10.36, 6.81, 14.71,
              15.42, 23.3, 12.24, 19.08, 21.25, 31.97, 29.96, 22.39, 30.8, 12.54, 43.57, 34.22])

def slr_intervals(x, y, x0, level=0.95):
    """Fitted values, confidence intervals for the mean and prediction intervals at x0."""
    n = len(y)
    Sxx = np.sum((x - x.mean())**2)
    b1 = np.sum((x - x.mean()) * (y - y.mean())) / Sxx
    b0 = y.mean() - b1 * x.mean()
    s = np.sqrt(np.sum((y - b0 - b1 * x)**2) / (n - 2))
    q = stats.t.ppf(1 - (1 - level) / 2, n - 2)
    x0 = np.atleast_1d(np.asarray(x0, dtype=float))
    h0 = 1 / n + (x0 - x.mean())**2 / Sxx
    fit = b0 + b1 * x0
    return dict(fit=fit,
                ci=(fit - q * s * np.sqrt(h0), fit + q * s * np.sqrt(h0)),
                pi=(fit - q * s * np.sqrt(1 + h0), fit + q * s * np.sqrt(1 + h0)))

r = slr_intervals(x, y, [3.0, 5.0])
for j, x0 in enumerate([3.0, 5.0]):
    print(f"x0 = {x0}: fit = {r['fit'][j]:.4f}, "
          f"95% CI ({r['ci'][0][j]:.4f}, {r['ci'][1][j]:.4f}), "
          f"95% PI ({r['pi'][0][j]:.4f}, {r['pi'][1][j]:.4f}), "
          f"true mean = {46 - 7.7 * x0:.2f}")

# Uses np and slr_intervals from Section 5 (run that code first).
import pandas as pd
import matplotlib.pyplot as plt

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"')
xa = auto["weight"].to_numpy() / 1000
ya = auto["mpg"].to_numpy()

ra = slr_intervals(xa, ya, [2.0, 3.0, 4.5])
for j, w in enumerate([2.0, 3.0, 4.5]):
    print(f"{w * 1000:.0f} lb: fit = {ra['fit'][j]:.4f}, CI ({ra['ci'][0][j]:.4f}, {ra['ci'][1][j]:.4f}), "
          f"PI ({ra['pi'][0][j]:.4f}, {ra['pi'][1][j]:.4f})")

grid = np.linspace(xa.min(), xa.max(), 200)
rg = slr_intervals(xa, ya, grid)
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(xa, ya, s=12, alpha=0.3, color="black")
ax.fill_between(grid, rg["pi"][0], rg["pi"][1], alpha=0.15, color="teal", label="95% prediction band")
ax.fill_between(grid, rg["ci"][0], rg["ci"][1], alpha=0.5, color="teal", label="95% confidence band")
ax.plot(grid, rg["fit"], color="black", linewidth=2)
ax.set_xlabel("Weight (1000 lb)")
ax.set_ylabel("Fuel economy (mpg)")
ax.legend(loc="upper right")
plt.show()

# In-sample check: proportion of cars inside their 95% prediction interval, by weight third
ro = slr_intervals(xa, ya, xa)
inside = (ya >= ro["pi"][0]) & (ya <= ro["pi"][1])
third = pd.qcut(xa, 3, labels=["light", "medium", "heavy"])
print("all:", round(inside.mean(), 3),
      pd.Series(inside).groupby(third, observed=True).mean().round(3).to_dict())
