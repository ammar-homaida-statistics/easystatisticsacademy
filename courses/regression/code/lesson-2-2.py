# Regression Analysis: From Foundations to Mastery — Lesson 2.2
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 2.2 — The Matrix Formulation
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

X = np.column_stack([np.ones(len(y)), w, yr])       # the design matrix
print(X[:3])
XtX, Xty = X.T @ X, X.T @ y
print(XtX.round(3)); print(Xty.round(3))
print("rank:", np.linalg.matrix_rank(X))
ev = np.linalg.eigvalsh(XtX)                        # ascending order
print("eigenvalues:", ev.round(3), " condition number:", f"{ev[-1] / ev[0]:.4g}")
print("solution:", np.linalg.solve(XtX, Xty).round(4))

Xc = np.column_stack([np.ones(len(y)), w - 3, yr - 76])
evc = np.linalg.eigvalsh(Xc.T @ Xc)
print("condition number after centring:", round(evc[-1] / evc[0], 2))

# Uses np, y and auto from Section 5.1 (run that code first).
X_units = np.column_stack([np.ones(len(y)), auto["weight"], auto["weight"] * 0.45359237])
print("rank with lb and kg:", np.linalg.matrix_rank(X_units))
X_trap = np.column_stack([np.ones(len(y))] + [(auto["origin"] == k).astype(float) for k in (1, 2, 3)])
print("rank with all three origin indicators:", np.linalg.matrix_rank(X_trap))
print("eigenvalues:", np.linalg.eigvalsh(X_trap.T @ X_trap).round(6))

# Self-contained: needs nothing from earlier sections.
import numpy as np

rng = np.random.default_rng(2026)
n, mu, sigma, R = 5, np.arange(1.0, 6.0), 2.0, 100_000
C = np.eye(n) - np.ones((n, n)) / n
Y = mu + sigma * rng.standard_normal((R, n))
q = np.einsum("ij,jk,ik->i", Y, C, Y)               # y' C y for every row
print(f"simulated mean {q.mean():.3f} (MC se {q.std() / np.sqrt(R):.3f}); "
      f"theory {(n - 1) * sigma**2 + mu @ C @ mu:.1f}")

A = np.array([[1, 1, 0, 0, 0], [0, 0, 1, 1, 1]]) / np.array([[2], [3]])
Z = Y @ A.T
print("mean of Ay:", Z.mean(axis=0).round(3), " theory:", A @ mu)
print("cov of Ay:\n", np.cov(Z.T).round(3), "\ntheory:\n", (sigma**2 * A @ A.T).round(3))
