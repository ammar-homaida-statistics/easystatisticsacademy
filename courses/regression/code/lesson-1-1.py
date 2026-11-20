# Regression Analysis: From Foundations to Mastery — Lesson 1.1
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

"""Lesson 1.1 — What Is Regression?
 Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).
"""

import numpy as np
import pandas as pd

cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
        "acceleration", "model_year", "origin", "car_name"]
auto = pd.read_csv("data/auto-mpg.data", sep=r"\s+", header=None,
                   names=cols, na_values="?", quotechar='"')

print(auto[["mpg", "weight"]].describe().round(2))

# Mean mpg within 500-lb weight bands (the heaviest band is 4500-5500 lb)
breaks = [1500, 2000, 2500, 3000, 3500, 4000, 4500, 5500]
auto["band"] = pd.cut(auto["weight"], bins=breaks, right=False)
band_stats = (auto.groupby("band", observed=True)["mpg"]
                  .agg(n="count", mean_mpg="mean", sd_mpg="std").round(2))
print(band_stats)

import matplotlib.pyplot as plt
mid = auto.groupby("band", observed=True)["weight"].mean()
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(auto["weight"], auto["mpg"], s=12, alpha=0.3, color="black")
ax.plot(mid.to_numpy(), band_stats["mean_mpg"].to_numpy(), marker="o", markersize=9, linewidth=2)
ax.set_xlabel("Weight (lb)")
ax.set_ylabel("Fuel economy (mpg)")
plt.show()