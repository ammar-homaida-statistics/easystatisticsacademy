# Regression Analysis: From Foundations to Mastery — Lesson 1.5
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 1.5 — Interpreting the Coefficients
 Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).
"""

import numpy as np
import pandas as pd

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"')

def summarise_fit(x, y):
    n = len(y)
    Sxx = np.sum((x - x.mean())**2)
    b1 = np.sum((x - x.mean()) * (y - y.mean())) / Sxx
    b0 = y.mean() - b1 * x.mean()
    e = y - b0 - b1 * x
    s = np.sqrt(e @ e / (n - 2))
    se1 = s / np.sqrt(Sxx)
    se0 = s * np.sqrt(1 / n + x.mean()**2 / Sxx)
    R2 = 1 - (e @ e) / np.sum((y - y.mean())**2)
    return dict(b0=b0, b1=b1, se_b0=se0, se_b1=se1, t_b1=b1 / se1, R2=R2)

w, y = auto["weight"].to_numpy(), auto["mpg"].to_numpy()
versions = {
    "pounds": w,
    "hundreds_lb": w / 100,
    "thousands_lb": w / 1000,
    "thousands_kg": w * 0.45359237 / 1000,
    "centred_3000lb": (w - 3000) / 1000,
}
table = pd.DataFrame({k: summarise_fit(v, y) for k, v in versions.items()}).T
print(table.round(6))

# Uses np, w, y and summarise_fit from Section 5.1 (run that code first).
x = w / 1000
f = summarise_fit(x, y)
for x0 in (1.0, 6.0):
    print(f"prediction at {x0 * 1000:.0f} lb: {f['b0'] + f['b1'] * x0:.2f} mpg")
print("observed weight range:", w.min(), "to", w.max(), "lb")

L100 = 235.214583 / y                                          # non-linear change
fL = summarise_fit(x, L100)
print(f"L/100 km fit: b0 = {fL['b0']:.4f}, b1 = {fL['b1']:.4f}, R2 = {fL['R2']:.4f}")

b_log = summarise_fit(x, np.log(y))["b1"]
print(f"log(mpg) slope = {b_log:.4f}; "
      f"{100 * (np.exp(b_log) - 1):.1f}% per 1000 lb; {100 * (np.exp(b_log / 10) - 1):.2f}% per 100 lb")
