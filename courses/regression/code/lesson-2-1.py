# Regression Analysis: From Foundations to Mastery — Lesson 2.1
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 2.1 — From One Predictor to Many
 Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).
"""

import numpy as np
import pandas as pd

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"')
y = auto["mpg"].to_numpy()
w = auto["weight"].to_numpy() / 1000                            # 1000 lb
yr = auto["model_year"].to_numpy().astype(float)

def ls_fit(y, *xs):
    """Least squares with an intercept; the matrix formulas are derived in Lessons 2.3-2.4."""
    X = np.column_stack([np.ones(len(y)), *xs])
    XtX_inv = np.linalg.inv(X.T @ X)
    b = XtX_inv @ X.T @ y
    e = y - X @ b
    n, k = X.shape
    s2 = e @ e / (n - k)
    return dict(b=b, se=np.sqrt(s2 * np.diag(XtX_inv)), sigma=np.sqrt(s2),
                R2=1 - e @ e / np.sum((y - y.mean())**2))

for name, xs in {"weight only": (w,), "year only": (yr,), "weight + year": (w, yr)}.items():
    f = ls_fit(y, *xs)
    print(f"{name:14s} b = {np.round(f['b'], 3)}  se = {np.round(f['se'], 3)}  "
          f"R2 = {f['R2']:.3f}  sigma = {f['sigma']:.3f}")

fc = ls_fit(y, w - 3, yr - 76)
print(f"centred intercept = {fc['b'][0]:.3f} (se {fc['se'][0]:.3f})")

# Theorem 2.1.1
b = ls_fit(y, w, yr)["b"]
delta = ls_fit(yr, w)["b"][1]
print(f"simple slope {ls_fit(y, w)['b'][1]:.4f} = partial {b[1]:.4f} + "
      f"{b[2]:.4f} x {delta:.4f} = {b[1] + b[2] * delta:.4f}")

# Uses y, w, yr, b and ls_fit from Section 5.2 (run that code first).
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

cmap = LinearSegmentedColormap.from_list("years", ["#2c7bb6", "#e6862a", "#d7191c"])
fig, ax = plt.subplots(figsize=(6.5, 4.2))
sc = ax.scatter(w, y, c=yr, cmap=cmap, s=12, alpha=0.7)
grid = np.linspace(w.min(), w.max(), 100)
for yy in (70, 76, 82):
    ax.plot(grid, b[0] + b[1] * grid + b[2] * yy, linewidth=2,
            color=cmap((yy - 70) / 12), label=f"19{yy}")
s = ls_fit(y, w)["b"]
ax.plot(grid, s[0] + s[1] * grid, "k--", linewidth=2, label="weight only")
fig.colorbar(sc, ax=ax, label="Model year")
ax.set_xlabel("Weight (1000 lb)"); ax.set_ylabel("Fuel economy (mpg)")
ax.legend(frameon=False)
plt.tight_layout()
plt.show()

# Uses auto, w, yr and b from Section 5.2 (run that code first).
print(f"prediction for a 4500-lb 1982 car: {b @ [1, 4.5, 82]:.2f} mpg")
print("heaviest 1982 car:", auto.loc[auto.model_year == 82, "weight"].max(), "lb")
print("cars from 1980-82 above 3500 lb:", int(((yr >= 80) & (w > 3.5)).sum()))
