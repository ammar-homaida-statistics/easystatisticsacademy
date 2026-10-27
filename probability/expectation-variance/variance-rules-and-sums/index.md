---
layout: default
title: Variance Rules and Sums
description: Learn how variance behaves when random variables are added together and why independence plays a crucial role.
permalink: /probability/expectation-variance/variance-rules-and-sums/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_expectation_variance_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/expectation-variance/variance-rules-and-sums/",
    label: "Variance Rules & Sums of Variables",
    ts: Date.now()
  }));
  } catch (_) {
    // Storage permissions must not prevent accessing the lesson or explorer.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 4</span>
      <span class="badge">Expectation & Variance</span>
      <span class="badge">Variability</span>
    </div>

    <h1>Variance Rules and Sums</h1>

    <p class="lead">
      Expectation adds beautifully regardless of dependence.
    </p>

    <p class="lead">
      Variance behaves differently. Understanding how variances combine is essential for analyzing uncertainty in sums of random variables.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/expectation-variance/linearity-of-expectation/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/expectation-variance/covariance/">
         Next: Covariance →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>From Expectation to Variance</h2>

    <p>
      In the previous lesson,
      we learned that expectations always add.
    </p>

    \[
\operatorname{E}(X+Y)=\operatorname{E}(X)+\operatorname{E}(Y)
\]

    <p>
      Variance is more complicated because it depends not only on individual variability but also on how variables move together.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The variance of a sum depends on both the individual variances and the relationship between the variables.
      </p>

    </div>

    <h2>Review: What Variance Measures</h2>

    <p>
      Variance measures the average squared distance from the mean.
    </p>

    \[
\operatorname{Var}(X)=\operatorname{E}\big[(X-\operatorname{E}X)^2\big]
\]

    <p>
      Larger variances indicate greater spread around the expected value.
    </p>

    <h2>Variance of a Constant</h2>

    <p>
      A constant never changes.
    </p>

    <p>
      Therefore,
      it has no variability.
    </p>

    \[
\operatorname{Var}(c)=0
\]

    <p>
      for any constant c.
    </p>

    <h2>Adding a Constant</h2>

    <p>
      Adding a constant shifts the center of a distribution but does not change its spread.
    </p>

    \[
\operatorname{Var}(X+c)=\operatorname{Var}(X)
\]

    <p>
      The variability remains exactly the same.
    </p>

    <h2>Multiplying by a Constant</h2>

    <p>
      Scaling a variable changes its variability.
    </p>

    <p>
      The variance rule is:
    </p>

    \[
\operatorname{Var}(cX)=c^2\operatorname{Var}(X)
\]

    <p>
      Notice the square.
    </p>

    <p>
      Variance responds to scaling more strongly than expectation.
    </p>

    <h2>Example: Scaling Measurements</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        Var(X) = 4
      </p>

    </div>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        Y = 3X
      </p>

    </div>

    <p>
      Then:
    </p>

    \[
\operatorname{Var}(Y)=\operatorname{Var}(3X)=3^2\cdot4=36
\]

    <p>
      The variance increases by a factor of nine.
    </p>

    <h2>Variance of a Sum</h2>

    <p>
      Now consider two random variables:
    </p>

    <div class="example-box">

      <p>
        X
      </p>

      <p>
        Y
      </p>

    </div>

    <p>
      What is:
    </p>

    \[
\operatorname{Var}(X+Y)
\]

    <p>
      Unlike expectation,
      the answer is not always the simple sum of the variances.
    </p>

    <h2>The General Formula</h2>

    <p>
      The complete variance rule is:
    </p>

    \[
\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)
\]

    <p>
      The additional term involves covariance, which measures their joint linear variation. This identity requires finite second moments but not independence.
    </p>

    <h2>Why the Extra Term Appears</h2>

    <p>
      If X and Y tend to increase together,
      the total variability becomes larger.
    </p>

    <p>
      If one tends to increase while the other decreases,
      the total variability becomes smaller.
    </p>

    <p>
      Covariance captures this relationship.
    </p>

    <h2>The Special Case of Independence</h2>

    <p>
      When X and Y are independent:
    </p>

    \[
\operatorname{Cov}(X,Y)=0
\]

    <p>
      Therefore:
    </p>

    \[
\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)
\]

    <p>
      This is the variance rule most frequently used in introductory probability.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Variances add when the variables have zero covariance. Independence is sufficient, but not necessary: dependent random variables can also be uncorrelated.
      </p>

    </div>

    <h2>Example: Two Independent Dice</h2>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = First die
      </p>

      <p>
        Y = Second die
      </p>

    </div>

    <p>
      Each die has variance:
    </p>

    \[
\operatorname{Var}(X)=\operatorname{Var}(Y)=\frac{1^2+2^2+3^2+4^2+5^2+6^2}{6}-3.5^2=\frac{35}{12}
\]

    <p>
      Since the dice are independent:
    </p>

    \[
\operatorname{Var}(X+Y)=\frac{35}{12}+\frac{35}{12}=\frac{35}{6}\approx5.8333
\]

    <p>
      The variances simply add.
    </p>


    <!-- INTERACTIVE VARIANCE EXPLORER -->
    <section class="concept-box esa-variance-explorer" id="esa-variance-explorer"
             aria-labelledby="esa-variance-explorer-title">
      <h2 id="esa-variance-explorer-title">Interactive Variance of Sums and Differences</h2>
      <p>Explore how covariance changes the variance of a sum or difference. Supply positive standard deviations
         and a correlation coefficient between −1 and +1. Correlation is undefined if either standard deviation is zero.</p>
      <form id="esa-variance-explorer-form" novalidate>
        <div class="esa-variance-input-grid">
          <div>
            <label for="esa-variance-sdx">Standard deviation of X</label>
            <input type="number" id="esa-variance-sdx" name="sdx" inputmode="decimal"
                   min="0.000001" max="1000000" step="any" value="2" required>
          </div>
          <div>
            <label for="esa-variance-sdy">Standard deviation of Y</label>
            <input type="number" id="esa-variance-sdy" name="sdy" inputmode="decimal"
                   min="0.000001" max="1000000" step="any" value="3" required>
          </div>
          <div class="esa-variance-correlation">
            <label for="esa-variance-rho">Correlation ρ (−1 to +1): <output id="esa-variance-rho-label" for="esa-variance-rho">0.00</output></label>
            <input type="range" id="esa-variance-rho" name="correlation"
                   min="-1" max="1" step="0.05" value="0" aria-describedby="esa-variance-rho-help">
            <p class="muted-mini" id="esa-variance-rho-help">Use the left/right arrow keys for increments of 0.05, or select an example below.</p>
          </div>
        </div>
        <div class="esa-variance-presets" aria-label="Correlation examples">
          <button class="btn btn-outline" type="button" data-rho="-1">ρ = −1</button>
          <button class="btn btn-outline" type="button" data-rho="0">ρ = 0</button>
          <button class="btn btn-outline" type="button" data-rho="1">ρ = +1</button>
        </div>
        <p class="esa-variance-formula">
          <strong>Formula:</strong> Cov(X,Y) = ρ × SD(X) × SD(Y);
          Var(X ± Y) = SD(X)² + SD(Y)² ± 2Cov(X,Y).
        </p>
        <div class="example-box" id="esa-variance-results" role="status" aria-live="polite">
          <p>Cov(X,Y): <strong><output id="esa-variance-cov">0</output></strong></p>
          <p>Var(X + Y): <strong><output id="esa-variance-plus">13</output></strong></p>
          <p>Var(X − Y): <strong><output id="esa-variance-minus">13</output></strong></p>
          <p id="esa-variance-explanation">Zero correlation means zero covariance and equal sum/difference variances. It does not necessarily mean independence.</p>
        </div>
        <p id="esa-variance-error" role="alert" hidden></p>
      </form>
      <p class="muted-mini">These are population-variance identities for random variables with finite second
        moments and positive standard deviations. Dependence changes the covariance term. Independence
        implies zero covariance, but the converse is generally false. The values ρ = ±1 describe
        perfect linear relationships, not typical independent variables.</p>
    </section>
    <style>
      #esa-variance-explorer {max-width:100%;min-width:0;overflow-wrap:anywhere;}
      #esa-variance-explorer .esa-variance-input-grid {
        display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin:16px 0;
      }
      #esa-variance-explorer .esa-variance-input-grid>div {min-width:0;}
      #esa-variance-explorer label {display:block;font-weight:650;margin-bottom:6px;}
      #esa-variance-explorer input[type="number"] {
        width:100%;max-width:100%;min-width:0;box-sizing:border-box;
        background:var(--surface);color:var(--text);border:1px solid var(--border-strong);
        border-radius:8px;padding:10px;font:inherit;
      }
      #esa-variance-explorer input:focus-visible,#esa-variance-explorer button:focus-visible {
        outline:2px solid var(--accent);outline-offset:2px;
      }
      #esa-variance-explorer .esa-variance-correlation {grid-column:1/-1;}
      #esa-variance-explorer input[type="range"] {display:block;width:100%;max-width:100%;box-sizing:border-box;margin:0;accent-color:var(--brand);}
      #esa-variance-explorer .esa-variance-presets {display:flex;flex-wrap:wrap;gap:8px;margin:10px 0;}
      #esa-variance-explorer .esa-variance-presets button {min-width:85px;}
      #esa-variance-explorer .esa-variance-formula {overflow-wrap:anywhere;}
      #esa-variance-error {font-weight:700;color:#b42318;}
      @media(max-width:600px) {
        #esa-variance-explorer .esa-variance-input-grid {grid-template-columns:minmax(0,1fr);}
      }
    </style>
    <script>
    (function () {
      const form = document.getElementById("esa-variance-explorer-form");
      if (!form) return;
      const sdX = document.getElementById("esa-variance-sdx");
      const sdY = document.getElementById("esa-variance-sdy");
      const rho = document.getElementById("esa-variance-rho");
      const rhoLabel = document.getElementById("esa-variance-rho-label");
      const cov = document.getElementById("esa-variance-cov");
      const plus = document.getElementById("esa-variance-plus");
      const minus = document.getElementById("esa-variance-minus");
      const explanation = document.getElementById("esa-variance-explanation");
      const error = document.getElementById("esa-variance-error");

      function format(value) {
        const rounded = Math.abs(value) < 1e-10 ? 0 : value;
        return Number(rounded.toPrecision(10)).toLocaleString("en-US",{maximumFractionDigits:10});
      }
      function render() {
        const x = Number(sdX.value);
        const y = Number(sdY.value);
        const r = Number(rho.value);
        rhoLabel.textContent = Number.isFinite(r) ? r.toFixed(2) : "—";
        let message = "";
        if (!sdX.value.trim() || !Number.isFinite(x) || x <= 0 || x > 1000000 ||
            !sdY.value.trim() || !Number.isFinite(y) || y <= 0 || y > 1000000) {
          message = "Enter positive standard deviations, each no greater than 1,000,000.";
        } else if (!rho.value.trim() || !Number.isFinite(r) || r < -1 || r > 1) {
          message = "Correlation must be between −1 and +1.";
        }
        if (message) {
          cov.textContent = "—"; plus.textContent = "—"; minus.textContent = "—";
          explanation.textContent = "";
          error.textContent = message; error.hidden = false;
          return;
        }
        const c = r * x * y;
        const a = x*x + y*y;
        const variancePlus = a + 2*c;
        const varianceMinus = a - 2*c;
        error.textContent = ""; error.hidden = true;
        cov.textContent = format(c);
        plus.textContent = format(variancePlus);
        minus.textContent = format(varianceMinus);
        if (r === 0) {
          explanation.textContent = "At ρ = 0, covariance vanishes and both variances equal the sum of the individual variances. Zero correlation does not prove independence.";
        } else if (r > 0) {
          explanation.textContent = "Positive correlation raises the variance of X + Y and lowers the variance of X − Y compared with zero correlation.";
        } else {
          explanation.textContent = "Negative correlation lowers the variance of X + Y and raises the variance of X − Y compared with zero correlation.";
        }
      }
      form.addEventListener("submit", event => { event.preventDefault(); render(); });
      form.addEventListener("input", render);
      form.addEventListener("change", render);
      form.querySelectorAll("[data-rho]").forEach(button => {
        button.addEventListener("click", () => {
          rho.value = button.dataset.rho;
          render();
        });
      });
      render();
    })();
    </script>

    <h2>Variance of a Difference</h2>

    <p>
      A similar rule applies to subtraction.
    </p>

    \[
\operatorname{Var}(X-Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)-2\operatorname{Cov}(X,Y)
\]

    <p>
      The covariance term changes sign.
    </p>

    <h2>Independent Variables and Differences</h2>

    <p>
      If X and Y are independent:
    </p>

    \[
\operatorname{Var}(X-Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)
\]

    <p>
      Surprisingly,
      the same addition rule appears.
    </p>

    <p>
      Under zero covariance, the variance of a sum and the variance of a difference both equal the sum of the individual variances. Without this condition, the covariance terms have opposite signs.
    </p>

    <h2>Extending to Many Variables</h2>

    <p>
      For variables with zero pairwise covariances (including mutually independent variables):
    </p>

    \[
\operatorname{Var}\!\left(\sum_{i=1}^{n}X_i\right)=\sum_{i=1}^{n}\operatorname{Var}(X_i)\quad\text{if all pairwise covariances vanish}
\]

    <p>
      This rule is essential in probability theory,
      statistics,
      and data science.
    </p>

    <h2>Why This Matters</h2>

    <p>
      Many real-world quantities are sums.
    </p>

    <div class="example-box">

      <p>
        Total sales
      </p>

      <p>
        Total claims
      </p>

      <p>
        Total arrivals
      </p>

      <p>
        Total profits
      </p>

    </div>

    <p>
      Understanding how variability accumulates is critical for risk assessment and forecasting.
    </p>

    <h2>Expectation Versus Variance</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Quantity</th>
            <th>Addition Rule</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Expectation</td>
            <td>Always adds</td>
          </tr>

          <tr>
            <td>Variance</td>
            <td>Depends on covariance</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      This distinction is one of the most important ideas in probability.
    </p>

    <h2>The Missing Piece</h2>

    <p>
      We have repeatedly mentioned covariance,
      but we have not yet defined it.
    </p>

    <p>
      Covariance measures how variables co-vary linearly, but covariance equal to zero does not in general establish independence.
    </p>

    <p>
      It is the key to understanding how variances combine.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The next lesson introduces covariance,
      a measure of joint variability between random variables.
    </p>

    <p>
      Covariance provides the missing connection between expectation,
      variance,
      dependence,
      and correlation.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Var(c) = 0 for any constant</li>

        <li>Var(X + c) = Var(X)</li>

        <li>Var(cX) = c²Var(X)</li>

        <li>Variance of a sum depends on covariance</li>

        <li>Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y)</li>

        <li>Independent variables have covariance zero</li>

        <li>Variances add directly only when variables are independent or uncorrelated</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/expectation-variance/linearity-of-expectation/">
         ← Previous: Linearity of Expectation
      </a>

      <a class="btn"
         href="/probability/expectation-variance/covariance/">
         Next: Covariance →
      </a>

    </div>

  </div>

</section>