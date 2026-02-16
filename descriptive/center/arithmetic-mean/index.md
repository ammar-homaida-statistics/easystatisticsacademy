---
layout: default
title: "Arithmetic Mean"
description: "Definition, formula, properties, interpretation, and limitations of the arithmetic mean."
permalink: /descriptive/center/arithmetic-mean/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/center/what-is-center/">
    ← Previous Lesson: What Is “Center”?
  </a>
</section>

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5;border:2px solid #ff9800;padding:2rem;border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0;color:#e65100;font-size:1.8rem;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0;font-size:1.05rem;color:#5d4037;line-height:1.6;">
        Worked examples, graphical illustrations, and software demonstrations (SPSS, R, Python, Excel) will be added in future updates.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Arithmetic Mean</h1>
    <p class="lead">
      The arithmetic mean is the most commonly used measure of center.
      It represents the balance point of a numerical dataset.
    </p>
  </div>

  <hr>

  <h2>1. Definition</h2>

  <p>
    For a dataset with <em>n</em> observations:
  </p>

  <p style="font-size:1.1rem;">
    x̄ = (x₁ + x₂ + … + xₙ) / n
  </p>

  <p>
    The mean equals the sum of all values divided by the number of observations.
  </p>

  <hr>

  <h2>2. Example</h2>

  <p><strong>Data:</strong> 4, 6, 8, 10</p>

  <p>
    x̄ = (4 + 6 + 8 + 10) / 4 = 7
  </p>

  <p>
    The mean value is 7.
  </p>

  <hr>

  <h2>3. Interpretation: The Balance Point</h2>

  <p>
    The arithmetic mean is the value that balances the data.
  </p>

  <p>
    One key mathematical property:
  </p>

  <p>
    The sum of deviations from the mean equals zero:
  </p>

  <p style="font-size:1.05rem;">
    Σ(xᵢ − x̄) = 0
  </p>

  <p>
    This makes the mean central in variance and standard deviation calculations.
  </p>

  <hr>

  <h2>4. Sensitivity to Outliers</h2>

  <p><strong>Data:</strong> 5, 6, 7, 8, 100</p>

  <p>
    Mean = (5 + 6 + 7 + 8 + 100) / 5 = 25.2
  </p>

  <p>
    Most values are between 5 and 8, yet the mean becomes 25.2.
  </p>

  <p>
    This shows:
  </p>

  <ul>
    <li>The mean uses all observations.</li>
    <li>It is highly sensitive to extreme values.</li>
  </ul>

  <hr>

  <h2>5. When Is the Mean Appropriate?</h2>

  <ul>
    <li>Numerical (interval or ratio) data</li>
    <li>Approximately symmetric distributions</li>
    <li>No extreme outliers</li>
  </ul>

  <p>
    The mean is inappropriate for:
  </p>

  <ul>
    <li>Nominal data</li>
    <li>Highly skewed distributions (without caution)</li>
  </ul>

  <hr>

  <h2>6. Conceptual Strength</h2>

  <p>
    The mean is mathematically powerful:
  </p>

  <ul>
    <li>Minimizes squared deviations</li>
    <li>Central to regression</li>
    <li>Foundation for variance and standard deviation</li>
  </ul>

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>The mean is the arithmetic average.</li>
    <li>It represents the balance point.</li>
    <li>It uses all observations.</li>
    <li>It is sensitive to outliers.</li>
  </ul>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/center/median/">
    Next Lesson → Median
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_center_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/center/arithmetic-mean/",
    label:"Lesson 2 — Arithmetic Mean",
    ts:Date.now()
  }));
})();
</script>