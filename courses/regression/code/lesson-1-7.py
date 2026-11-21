# Regression Analysis: From Foundations to Mastery — Lesson 1.7
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 1.7 — Inference for the Regression Parameters
 Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).
"""

import numpy as np
from scipy import stats

x = np.array([2.226, 3.84, 3.235, 2.897, 2.842, 4.367, 4.768, 2.221, 3.885, 2.644, 4.984, 4.819, 3.826,
              4.235, 3.403, 4.491, 3.169, 2.786, 2.573, 2.392, 3.44, 3.108, 3.921, 1.645, 3.167])
y = np.array([36.16, 13.58, 26.48, 18.77, 24.81, 7.7, 14.69, 32.24, 20.64, 22.1, 10.36, 6.81, 14.71,
              15.42, 23.3, 12.24, 19.08, 21.25, 31.97, 29.96, 22.39, 30.8, 12.54, 43.57, 34.22])

def slr_inference(x, y, beta10=0.0, level=0.95):
    n = len(y)
    Sxx = np.sum((x - x.mean())**2)
    b1 = np.sum((x - x.mean()) * (y - y.mean())) / Sxx
    b0 = y.mean() - b1 * x.mean()
    e = y - b0 - b1 * x
    SSE = e @ e; dfr = n - 2; s2 = SSE / dfr
    se1 = np.sqrt(s2 / Sxx); se0 = np.sqrt(s2 * (1 / n + x.mean()**2 / Sxx))
    q = stats.t.ppf(1 - (1 - level) / 2, dfr)
    t1 = (b1 - beta10) / se1
    SSR = np.sum((b0 + b1 * x - y.mean())**2)
    return dict(b0=b0, se0=se0, ci0=(b0 - q * se0, b0 + q * se0),
                b1=b1, se1=se1, ci1=(b1 - q * se1, b1 + q * se1),
                t1=t1, p1=2 * stats.t.sf(abs(t1), dfr),
                F=SSR / s2, pF=stats.f.sf(SSR / s2, 1, dfr), SSE=SSE, dfr=dfr,
                ci_sigma2=(SSE / stats.chi2.ppf(1 - (1 - level) / 2, dfr),
                           SSE / stats.chi2.ppf((1 - level) / 2, dfr)))

res = slr_inference(x, y)
print(f"b0 = {res['b0']:.4f} (se {res['se0']:.4f}), 95% CI ({res['ci0'][0]:.4f}, {res['ci0'][1]:.4f})")
print(f"b1 = {res['b1']:.4f} (se {res['se1']:.4f}), 95% CI ({res['ci1'][0]:.4f}, {res['ci1'][1]:.4f})")
print(f"H0: beta1 = 0:  t = {res['t1']:.4f}, p = {res['p1']:.2e};  F = {res['F']:.4f} = t^2 = {res['t1']**2:.4f}")
r7 = slr_inference(x, y, beta10=-7.7)
print(f"H0: beta1 = -7.7: t = {r7['t1']:.4f}, p = {r7['p1']:.4f}")
print(f"95% CI for sigma^2: ({res['ci_sigma2'][0]:.4f}, {res['ci_sigma2'][1]:.4f})")

import pandas as pd
cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"')
xa = auto["weight"].to_numpy() / 1000
ya = auto["mpg"].to_numpy()
ra = slr_inference(xa, ya)
print(f"b0 = {ra['b0']:.4f} (se {ra['se0']:.4f}), 95% CI ({ra['ci0'][0]:.4f}, {ra['ci0'][1]:.4f})")
print(f"b1 = {ra['b1']:.4f} (se {ra['se1']:.4f}), t = {ra['t1']:.4f}, 95% CI ({ra['ci1'][0]:.4f}, {ra['ci1'][1]:.4f})")
print(f"F = {ra['F']:.2f}; 95% CI for sigma^2: ({ra['ci_sigma2'][0]:.4f}, {ra['ci_sigma2'][1]:.4f})")
r8 = slr_inference(xa, ya, beta10=-8)
print(f"H0: beta1 = -8: t = {r8['t1']:.4f}, p = {r8['p1']:.4f}")