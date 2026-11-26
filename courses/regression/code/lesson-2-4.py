# Regression Analysis: From Foundations to Mastery — Lesson 2.4
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 2.4 — Properties of the OLS Estimator
 Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).
"""

import numpy as np
import pandas as pd
from scipy import stats

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"')
y = auto["mpg"].to_numpy()
X = np.column_stack([np.ones(len(y)), auto["weight"] / 1000, auto["model_year"]])
n, k = X.shape; df_res = n - k                          # 395
XtX_inv = np.linalg.inv(X.T @ X)
b = XtX_inv @ X.T @ y
e = y - X @ b
SSE = e @ e; s2 = SSE / df_res
print(f"SSE = {SSE:.2f}, sigma2_hat = {s2:.4f}, sigma_hat = {np.sqrt(s2):.4f}")
V = s2 * XtX_inv
print("estimated Cov(beta_hat):\n", V.round(6))
se = np.sqrt(np.diag(V)); print("standard errors:", se.round(5))
print("correlations of the estimates:\n", (V / np.outer(se, se)).round(4))
print("corr(weight, year):", round(np.corrcoef(X[:, 1], X[:, 2])[0, 1], 4))

def lin_comb(a, level=0.95):
    a = np.asarray(a, dtype=float)
    est = a @ b; s = np.sqrt(a @ V @ a); q = stats.t.ppf(1 - (1 - level) / 2, df_res)
    return np.round([est, s, est - q * s, est + q * s], 4)
print("mean at 3000 lb, 1976 (est, se, lower, upper):", lin_comb([1, 3, 76]))
print("ten model years at fixed weight:             ", lin_comb([0, 0, 10]))

# Self-contained: reads the 398 (weight, year) pairs and needs nothing from earlier sections.
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"')
X = np.column_stack([np.ones(len(auto)), auto["weight"] / 1000, auto["model_year"]])
n, k = X.shape; m = n - k
XtX_inv = np.linalg.inv(X.T @ X); A = XtX_inv @ X.T
beta, sigma, R = np.array([-14.2, -6.66, 0.757]), 3.43, 10_000
rng = np.random.default_rng(2026)

def simulate(E):                                        # E: R x n matrix of errors
    Y = X @ beta + E
    B = Y @ A.T                                         # R x 3 estimates
    S = ((Y - B @ X.T)**2).sum(axis=1)                  # SSE
    q = stats.t.ppf(0.975, m); se_w = np.sqrt(S / m * XtX_inv[1, 1])
    summary = dict(mean_bw=B[:, 1].mean(), sd_bw=B[:, 1].std(ddof=1), mean_s2=(S / m).mean(),
                   mean_Q=(S / sigma**2).mean(), var_Q=(S / sigma**2).var(ddof=1),
                   cor_bw_SSE=np.corrcoef(B[:, 1], S)[0, 1],
                   coverage=np.mean(np.abs(B[:, 1] - beta[1]) <= q * se_w))
    return S, summary

S_norm, norm = simulate(sigma * rng.standard_normal((R, n)))
S_skew, skew = simulate(sigma * (rng.exponential(1.0, (R, n)) - 1.0))
h = np.einsum("ij,jk,ik->i", X, XtX_inv, X)
theory = dict(mean_bw=beta[1], sd_bw=sigma * np.sqrt(XtX_inv[1, 1]), mean_s2=sigma**2,
              mean_Q=m, var_Q=2 * m, cor_bw_SSE=0.0, coverage=0.95)
print(pd.DataFrame({"normal": norm, "skewed": skew, "theory": theory}).round(4))
print("Var(SSE/sigma^2) predicted for kappa = 9:", round(2 * m + 6 * np.sum((1 - h)**2), 1))

grid = np.linspace(200, 600, 400)
fig, axes = plt.subplots(1, 2, figsize=(8, 3.4), sharey=True)
for ax, S, title in zip(axes, (S_norm, S_skew), ("Normal errors", "Skewed errors")):
    ax.hist(S / sigma**2, bins=50, density=True, color="lightgray", edgecolor="white")
    ax.plot(grid, stats.chi2.pdf(grid, m), linewidth=2)
    ax.set_title(title); ax.set_xlabel("SSE / sigma^2"); ax.set_xlim(200, 600)
axes[0].set_ylabel("Density")
plt.tight_layout()
plt.show()
