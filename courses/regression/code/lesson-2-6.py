# Regression Analysis: From Foundations to Mastery — Lesson 2.6
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 2.6 — Inference for Coefficients and Linear Combinations
 Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).
"""

import numpy as np
import pandas as pd
from scipy import stats

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"').dropna().reset_index(drop=True)
y = auto["mpg"].to_numpy()
X = np.column_stack([np.ones(len(y)), auto["weight"] / 1000, auto["model_year"],
                     auto["horsepower"] / 100])
n, k = X.shape; m = n - k
XtX_inv = np.linalg.inv(X.T @ X)
b = XtX_inv @ X.T @ y
e = y - X @ b
s = np.sqrt(e @ e / m)
se = s * np.sqrt(np.diag(XtX_inv))
q = stats.t.ppf(0.975, m)
t = b / se
print(f"df = {m}, sigma_hat = {s:.4f}, t_crit = {q:.4f}")
print(pd.DataFrame({"estimate": b, "se": se, "t": t, "p": 2 * stats.t.sf(np.abs(t), m),
                    "lower": b - q * se, "upper": b + q * se},
                   index=["intercept", "weight", "year", "horsepower"]).round(4).to_string())

# Uses np, X, XtX_inv, b, s, q and pd from Section 5.1 (run that code first).
X0 = np.array([[1, 3.0, 76, 1.0], [1, 2.2, 80, 0.7], [1, 2.0, 82, 2.0]])
fit0 = X0 @ b
h00 = np.einsum("ij,jk,ik->i", X0, XtX_inv, X0)
print(pd.DataFrame({"h00": h00, "fit": fit0,
                    "ci_lower": fit0 - q * s * np.sqrt(h00), "ci_upper": fit0 + q * s * np.sqrt(h00),
                    "pi_lower": fit0 - q * s * np.sqrt(1 + h00), "pi_upper": fit0 + q * s * np.sqrt(1 + h00)},
                   index=["3000 lb, 1976, 100 hp", "2200 lb, 1980, 70 hp",
                          "2000 lb, 1982, 200 hp"]).round(4).to_string())
print("largest observed leverage:", np.einsum("ij,jk,ik->i", X, XtX_inv, X).max().round(4))

# Uses np, stats, b, se, s, XtX_inv, m and q from Section 5.1 (run that code first).
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

idx = [1, 3]                                            # weight, horsepower
bS = b[idx]; VS = s**2 * XtX_inv[np.ix_(idx, idx)]
print("correlation of the two estimates:", round(VS[0, 1] / np.sqrt(VS[0, 0] * VS[1, 1]), 4))
Fq = stats.f.ppf(0.95, 2, m)
Fstat = lambda th: (bS - th) @ np.linalg.solve(VS, bS - th) / 2
print(f"F(A) = {Fstat(np.array([-5.7, 1.3])):.2f}, F(B) = {Fstat(np.array([-7.4, 1.6])):.2f}, "
      f"F_crit = {Fq:.3f}")

ang = np.linspace(0, 2 * np.pi, 400)
ell = bS[:, None] + np.linalg.cholesky(VS) @ np.vstack([np.cos(ang), np.sin(ang)]) * np.sqrt(2 * Fq)
qb = stats.t.ppf(1 - 0.05 / 4, m)
print("Bonferroni intervals:", np.c_[bS - qb * se[idx], bS + qb * se[idx]].round(4))
fig, ax = plt.subplots(figsize=(6, 4.2))
ax.plot(ell[0], ell[1], linewidth=2, color="black")
for mult, style in ((q, "--"), (qb, ":")):
    lo = bS - mult * se[idx]
    ax.add_patch(Rectangle(lo, *(2 * mult * se[idx]), fill=False, linestyle=style))
ax.plot(*bS, "ko")
for (x0, y0), lab in (((-5.7, 1.3), "A"), ((-7.4, 1.6), "B")):
    ax.plot(x0, y0, "x", color="red", markersize=9, markeredgewidth=2)
    ax.annotate(lab, (x0, y0), textcoords="offset points", xytext=(0, 7), ha="center", color="red")
ax.set_xlim(-7.8, -5.2); ax.set_ylim(-3.2, 2.2)
ax.set_xlabel("weight slope (mpg per 1000 lb)"); ax.set_ylabel("horsepower slope (mpg per 100 hp)")
plt.tight_layout()
plt.show()

# Self-contained: reads the 392 predictor rows and needs nothing from earlier sections.
import numpy as np
import pandas as pd
from scipy import stats

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"').dropna()
X = np.column_stack([np.ones(len(auto)), auto["weight"] / 1000, auto["model_year"],
                     auto["horsepower"] / 100])
n, k = X.shape; m = n - k
beta, sigma, R = np.array([-13.7, -6.45, 0.749, -0.50]), 3.43, 10_000
XtX_inv = np.linalg.inv(X.T @ X); A = XtX_inv @ X.T
rng = np.random.default_rng(2026)
Y = X @ beta + sigma * rng.standard_normal((R, n))
B = Y @ A.T; s2 = ((Y - B @ X.T)**2).sum(axis=1) / m
idx = [1, 3]; W_inv = np.linalg.inv(XtX_inv[np.ix_(idx, idx)])
D = B[:, idx] - beta[idx]                                # estimation errors
se1, se2 = np.sqrt(s2 * XtX_inv[1, 1]), np.sqrt(s2 * XtX_inv[3, 3])
qi, qb, Fq = stats.t.ppf(0.975, m), stats.t.ppf(1 - 0.05 / 4, m), stats.f.ppf(0.95, 2, m)
c1, c2 = np.abs(D[:, 0]) <= qi * se1, np.abs(D[:, 1]) <= qi * se2
Fs = np.einsum("ij,jk,ik->i", D, W_inv, D) / (2 * s2)
print({"weight_alone": c1.mean(), "hp_alone": c2.mean(), "both_separate": (c1 & c2).mean(),
       "both_bonferroni": ((np.abs(D[:, 0]) <= qb * se1) & (np.abs(D[:, 1]) <= qb * se2)).mean(),
       "ellipse": (Fs <= Fq).mean()})
