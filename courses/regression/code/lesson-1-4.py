# Regression Analysis: From Foundations to Mastery — Lesson 1.4
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 1.4 — Statistical Properties of the OLS Estimators
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
n = len(y)

Sxx = np.sum((x - x.mean())**2)
b1 = np.sum((x - x.mean()) * (y - y.mean())) / Sxx
b0 = y.mean() - b1 * x.mean()
e = y - b0 - b1 * x
SSE = e @ e
s2 = SSE / (n - 2)
print(f"SSE = {SSE:.4f}, sigma2_hat = {s2:.4f}, sigma_hat = {np.sqrt(s2):.4f}")
print(f"se(b1) = {np.sqrt(s2 / Sxx):.4f}, se(b0) = {np.sqrt(s2 * (1/n + x.mean()**2 / Sxx)):.4f}")
print(f"Cov(b0, b1) estimate = {-x.mean() * s2 / Sxx:.4f}, "
      f"correlation = {-x.mean() / np.sqrt(Sxx / n + x.mean()**2):.4f}")
print(f"ML estimate SSE/n = {SSE / n:.4f}")

# Self-contained: reads the 398 Auto MPG weights and needs nothing from earlier sections.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"')
x = auto["weight"].to_numpy() / 1000; n = len(x); Sxx = np.sum((x - x.mean())**2)

rng = np.random.default_rng(2026)
R, beta0, beta1, sigma = 10_000, 46.3, -7.7, 4.34
k = (x - x.mean()) / Sxx
Y = beta0 + beta1 * x + rng.normal(0, sigma, size=(R, n))
B1 = Y @ k
B0 = Y.mean(axis=1) - B1 * x.mean()
S2 = ((Y - B0[:, None] - B1[:, None] * x)**2).sum(axis=1) / (n - 2)
sd_theory = sigma / np.sqrt(Sxx)
print(f"mean b1 = {B1.mean():.4f}, sd b1 = {B1.std(ddof=1):.4f}, theory sd = {sd_theory:.4f}")
print(f"mean sigma2_hat = {S2.mean():.4f}, true sigma^2 = {sigma**2:.4f}")

grid = np.linspace(B1.min(), B1.max(), 200)
fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(B1, bins=50, density=True, color="lightgray", edgecolor="white")
ax.plot(grid, np.exp(-0.5 * ((grid - beta1) / sd_theory)**2) / (sd_theory * np.sqrt(2 * np.pi)), linewidth=2)
ax.axvline(beta1, linestyle="--", color="black")
ax.set_xlabel("Simulated slope estimates")
ax.set_ylabel("Density")
plt.show()
