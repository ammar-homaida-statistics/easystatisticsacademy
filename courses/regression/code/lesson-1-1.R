# Regression Analysis: From Foundations to Mastery — Lesson 1.1
# https://easystatisticsacademy.com/courses/regression/
# Data: Auto MPG, Quinlan (1993), UCI ML Repository, https://doi.org/10.24432/C5859H (CC BY 4.0).
# Download auto-mpg.data from the UCI page and save it as data/auto-mpg.data next to this script.

# Lesson 1.1 — What Is Regression?
#  Standalone script generated from lesson.qmd. Run from the lesson folder (data/auto-mpg.data).

cols <- c("mpg", "cylinders", "displacement", "horsepower", "weight",
          "acceleration", "model_year", "origin", "car_name")
auto <- read.table("data/auto-mpg.data", col.names = cols, na.strings = "?")

summary(auto[, c("mpg", "weight")])

# Mean mpg within 500-lb weight bands (the heaviest band is 4500-5500 lb)
breaks <- c(1500, 2000, 2500, 3000, 3500, 4000, 4500, 5500)
auto$band <- cut(auto$weight, breaks = breaks, right = FALSE)
band_stats <- aggregate(mpg ~ band, data = auto,
                        FUN = function(v) c(n = length(v), mean = mean(v), sd = sd(v)))
band_stats <- do.call(data.frame, band_stats)
names(band_stats) <- c("band", "n", "mean_mpg", "sd_mpg")
print(band_stats, digits = 4)

mid <- aggregate(weight ~ band, data = auto, FUN = mean)
plot(auto$weight, auto$mpg, pch = 16, col = rgb(0, 0, 0, 0.3),
     xlab = "Weight (lb)", ylab = "Fuel economy (mpg)")
points(mid$weight, band_stats$mean_mpg, pch = 19, cex = 1.8, type = "b", lwd = 2)