# Regression Analysis: From Foundations to Mastery — Lesson 2.5
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 2.5 — Interpreting Coefficients in Multiple Regression
 Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"').dropna().reset_index(drop=True)
y = auto["mpg"].to_numpy()
w = auto["weight"].to_numpy() / 1000
yr = auto["model_year"].to_numpy().astype(float)
hp = auto["horsepower"].to_numpy() / 100
n = len(y)

def ls(v, *xs):
    """Least squares of v on an intercept and xs: returns (coefficients, residuals)."""
    X = np.column_stack([np.ones(len(v)), *xs])
    b = np.linalg.lstsq(X, v, rcond=None)[0]
    return b, v - X @ b

b, e = ls(y, w, yr, hp)
print("full model:", b.round(4))
_, ry = ls(y, yr, hp); _, rw = ls(w, yr, hp)              # Frisch-Waugh-Lovell for weight
print("FWL slope:", round((rw @ ry) / (rw @ rw), 4), " full coefficient:", round(b[1], 4))
print("max |residual difference|:", f"{np.abs((ry - b[1] * rw) - e).max():.1e}")

_, ryh = ls(y, w, yr); _, rh = ls(hp, w, yr)
fig, axes = plt.subplots(1, 2, figsize=(8, 3.6))
for ax, rx, ryy, slope, title, lab in ((axes[0], rw, ry, b[1], "Weight", "weight | others"),
                                       (axes[1], rh, ryh, b[3], "Horsepower", "horsepower | others")):
    ax.scatter(rx, ryy, s=10, alpha=0.35, color="black")
    g = np.linspace(rx.min(), rx.max(), 2)
    ax.plot(g, slope * g, linewidth=2)
    ax.set_title(title); ax.set_xlabel(lab); ax.set_ylabel("mpg | others")
plt.tight_layout()
plt.show()

# Uses np, y, w, yr, hp, n, ls, b and e from Section 5.2 (run that code first).
b_short, _ = ls(y, w, hp)
Delta, _ = ls(yr, w, hp)
print("short model:     ", b_short.round(4))
print("identity:        ", (b[[0, 1, 3]] + Delta * b[2]).round(4))
print("Delta:           ", Delta.round(4))

X = np.column_stack([np.ones(n), w, yr, hp])
sigma_hat = np.sqrt(e @ e / (n - 4))
se_lm = sigma_hat * np.sqrt(np.diag(np.linalg.inv(X.T @ X)))
preds = {"weight": w, "year": yr, "horsepower": hp}
for j, (name, xj) in enumerate(preds.items(), start=1):
    others = [v for k, v in preds.items() if k != name]
    _, r = ls(xj, *others)
    Rj2 = 1 - (r @ r) / np.sum((xj - xj.mean())**2)
    Sjj = np.sum((xj - xj.mean())**2)
    print(f"{name:10s} VIF = {1 / (1 - Rj2):.3f}  se formula = {sigma_hat / np.sqrt((1 - Rj2) * Sjj):.4f}"
          f"  se = {se_lm[j]:.4f}")

# Self-contained: reads the 392 predictor rows and needs nothing from earlier sections.
import numpy as np
import pandas as pd

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"').dropna()
X = np.column_stack([np.ones(len(auto)), auto["weight"] / 1000, auto["model_year"],
                     auto["horsepower"] / 100])
X1 = X[:, [0, 1, 3]]                                    # short model: no model year
n = len(X); beta = np.array([-13.7, -6.45, 0.749, -0.50]); sigma, R = 3.43, 10_000
A_full = np.linalg.solve(X.T @ X, X.T)
A_short = np.linalg.solve(X1.T @ X1, X1.T)
Delta = A_short @ X[:, 2]
rng = np.random.default_rng(2026)
Y = X @ beta + sigma * rng.standard_normal((R, n))
B_full, B_short = Y @ A_full.T, Y @ A_short.T
rmse = lambda est, truth: np.sqrt(np.mean((est - truth)**2))
print(pd.DataFrame({
    "truth": beta[[1, 3]],
    "predicted_short": beta[[1, 3]] + Delta[1:] * beta[2],
    "full_mean": B_full[:, [1, 3]].mean(axis=0), "full_sd": B_full[:, [1, 3]].std(axis=0, ddof=1),
    "short_mean": B_short[:, 1:].mean(axis=0), "short_sd": B_short[:, 1:].std(axis=0, ddof=1),
    "rmse_full": [rmse(B_full[:, 1], beta[1]), rmse(B_full[:, 3], beta[3])],
    "rmse_short": [rmse(B_short[:, 1], beta[1]), rmse(B_short[:, 2], beta[3])]},
    index=["weight", "horsepower"]).round(4).to_string())
