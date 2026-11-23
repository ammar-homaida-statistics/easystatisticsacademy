# Regression Analysis: From Foundations to Mastery — Lesson 1.2
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 1.2 — Correlation versus Regression
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

r = np.corrcoef(x, y)[0, 1]
sx, sy = x.std(ddof=1), y.std(ddof=1)
b1 = r * sy / sx                               # Theorem 1.2.3(a)
g1 = r * sx / sy                               # slope of x on y
print(f"r = {r:.6f}, s_x = {sx:.6f}, s_y = {sy:.6f}")
print(f"b1 = {b1:.6f}, g1 = {g1:.6f}, b1*g1 = {b1*g1:.6f}, r^2 = {r**2:.6f}")
print("Line of x on y, drawn in the (x, y) plane, has slope", round(1 / g1, 4))
print("r with weight in kg:", round(np.corrcoef(auto["weight"] * 0.45359237, y)[0, 1], 6))

# Uses np, x, y, b1 and g1 from Section 5.1 (run that code first).
import matplotlib.pyplot as plt
grid = np.linspace(x.min(), x.max(), 100)
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(x, y, s=12, alpha=0.3, color="black")
ax.plot(grid, y.mean() + b1 * (grid - x.mean()), linewidth=2, label="y on x")
ax.plot(grid, y.mean() + (grid - x.mean()) / g1, linewidth=2, linestyle="--", label="x on y")
ax.plot(x.mean(), y.mean(), marker="x", markersize=12, markeredgewidth=2, color="black")
ax.set_ylim(y.min() - 3, y.max() + 3)
ax.set_xlabel("Weight (1000 lb)")
ax.set_ylabel("Fuel economy (mpg)")
ax.legend()
plt.show()

# Uses np, x, y, r, sx and sy from Section 5.1 (run that code first).
zx = (x - x.mean()) / sx
zy = (y - y.mean()) / sy
heavy = x >= np.quantile(x, 0.9)
print(f"n = {heavy.sum()}, mean z_x = {zx[heavy].mean():.3f}, "
      f"r * mean z_x = {r * zx[heavy].mean():.3f}, mean z_y = {zy[heavy].mean():.3f}")
