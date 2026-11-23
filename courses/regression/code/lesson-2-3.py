# Regression Analysis: From Foundations to Mastery — Lesson 2.3
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 2.3 — Least Squares in Matrix Form
 Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).
"""

import numpy as np
import pandas as pd

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"')
y = auto["mpg"].to_numpy()
w = auto["weight"].to_numpy() / 1000
yr = auto["model_year"].to_numpy().astype(float)
n = len(y)
X = np.column_stack([np.ones(n), w, yr])

b_ne = np.linalg.solve(X.T @ X, X.T @ y)              # normal equations
Q, R = np.linalg.qr(X)                                 # reduced QR: Q is n x 3
b_qr = np.linalg.solve(R, Q.T @ y)                     # R b = Q'y (triangular)
print("normal equations:", b_ne.round(6))
print("QR:              ", b_qr.round(6))
print("max difference:  ", f"{np.abs(b_ne - b_qr).max():.1e}")
print(f"cond(X) = {np.linalg.cond(X):.1f}, cond(X'X) = {np.linalg.cond(X.T @ X):.4g}")

# Uses np, auto, X, y, Q and b_qr from Section 5.1 (run that code first).
h = (Q**2).sum(axis=1)                                 # diag(H) = row sums of Q^2
e = y - X @ b_qr
print(f"trace(H) = {h.sum():.6f}, sum(e) = {e.sum():.1e}, max|X'e| = {np.abs(X.T @ e).max():.1e}")
SST = np.sum((y - y.mean())**2); SSE = e @ e; SSR = np.sum((X @ b_qr - y.mean())**2)
print(f"SST = {SST:.2f}, SSR = {SSR:.2f}, SSE = {SSE:.2f}, R2 = {SSR / SST:.4f}")
print(f"mean h = {h.mean():.5f}, min h = {h.min():.5f}, max h = {h.max():.4f}")
top = np.argsort(h)[::-1][:5]
print(auto.loc[top, ["car_name", "weight", "model_year"]].assign(h=h[top].round(4)))

# Uses np, auto, X and h from Sections 5.1-5.2 (run that code first).
import matplotlib.pyplot as plt

XtX_inv = np.linalg.inv(X.T @ X)
new = np.array([[1, 3.0, 76], [1, 2.5, 82], [1, 4.5, 82]])
h00 = np.einsum("ij,jk,ik->i", new, XtX_inv, new)
print("h00:", h00.round(4), " max h in data:", h.max().round(4))

fig, ax = plt.subplots(figsize=(6.5, 4.2))
ax.scatter(auto["weight"], auto["model_year"] + 1900, s=5 + 2500 * h,
           facecolors="none", edgecolors="gray", linewidths=0.8)
ax.scatter(new[:, 1] * 1000, new[:, 2] + 1900, marker="x", s=90, linewidths=3, color="red")
for (_, wt, yy), hh in zip(new, h00):
    ax.annotate(f"h00 = {hh:.4f}", (wt * 1000, yy + 1900), textcoords="offset points",
                xytext=(0, 8), ha="center", color="red")
ax.set_ylim(1969.5, 1983.8)
ax.set_xlabel("Weight (lb)"); ax.set_ylabel("Model year")
plt.tight_layout()
plt.show()

# Uses np, auto, y and n from Section 5.1 (run that code first).
X_dep = np.column_stack([np.ones(n), auto["weight"], auto["weight"] * 0.45359237])
b_mn, _, rank, _ = np.linalg.lstsq(X_dep, y, rcond=None)
X_lb = np.column_stack([np.ones(n), auto["weight"]])
b_lb = np.linalg.lstsq(X_lb, y, rcond=None)[0]
print("rank:", rank, " minimum-norm solution:", b_mn)
print("max |fitted difference|:", f"{np.abs(X_dep @ b_mn - X_lb @ b_lb).max():.1e}")
print("identified combination (per lb):", round(b_mn[1] + 0.45359237 * b_mn[2], 6),
      " one-predictor slope:", round(b_lb[1], 6))
