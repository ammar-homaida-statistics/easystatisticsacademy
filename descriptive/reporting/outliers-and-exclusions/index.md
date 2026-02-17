---
layout: default
title: "Outliers, Exclusions, and Transparency"
description: When you may exclude values, how to justify it, and how to report exclusions ethically and clearly.
permalink: /descriptive/reporting/outliers-and-exclusions/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/reporting/association-not-causation/">
    ← Previous Lesson: Association ≠ Causation
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
        Examples, visuals, and software demonstrations (SPSS, R, Python, Excel) will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Outliers, Exclusions, and Transparency</h1>
    <p class="lead">
      Outliers are not mistakes by default.
      Excluding data is a serious decision.
      Transparency determines credibility.
    </p>
  </div>

  <hr>

  <h2>1. What Is an Outlier?</h2>
  <p>
    An outlier is an observation that lies unusually far from the rest of the data.
  </p>

  <p>It may be:</p>
  <ul>
    <li>A measurement error</li>
    <li>A data entry mistake</li>
    <li>A rare but valid observation</li>
    <li>A meaningful extreme case</li>
  </ul>

  <p>
    Outliers are statistical signals — not automatic deletions.
  </p>

  <hr>

  <h2>2. When Is Exclusion Justified?</h2>
  <p>Excluding data may be justified only when:</p>
  <ul>
    <li>The value is clearly a recording or typing error</li>
    <li>The value is impossible (e.g., age = 250)</li>
    <li>The value violates predefined study criteria</li>
    <li>The exclusion rule was defined before analysis</li>
  </ul>

  <p>
    Excluding values because they “look bad” or change results is not acceptable.
  </p>

  <hr>

  <h2>3. When Should Outliers Be Kept?</h2>
  <p>Keep the value if:</p>
  <ul>
    <li>It is valid and correctly measured</li>
    <li>It reflects natural variability</li>
    <li>It represents an important subgroup</li>
  </ul>

  <p>
    Real-world data often contain genuine extremes.
  </p>

  <hr>

  <h2>4. Always Report What You Did</h2>
  <p>If exclusions occur, you must clearly state:</p>
  <ul>
    <li>How many values were excluded</li>
    <li>Why they were excluded</li>
    <li>How exclusion changed the results</li>
  </ul>

  <p>Example:</p>
  <blockquote>
    Two observations were excluded due to confirmed data entry errors.
    Results are reported after exclusion; including them does not change the overall conclusion.
  </blockquote>

  <hr>

  <h2>5. Sensitivity Analysis (Best Practice)</h2>
  <p>A strong reporting practice is to show results:</p>
  <ul>
    <li>With outliers included</li>
    <li>With outliers excluded</li>
  </ul>

  <p>
    If conclusions change dramatically, this must be discussed.
  </p>

  <hr>

  <h2>6. Ethical Principle</h2>
  <p>Statistical credibility depends on transparency.</p>

  <p>Data cleaning decisions must be:</p>
  <ul>
    <li>Predefined when possible</li>
    <li>Objectively justified</li>
    <li>Fully documented</li>
  </ul>

  <hr>

  <h2>7. Summary</h2>
  <ul>
    <li>Outliers are signals, not automatic errors.</li>
    <li>Exclusion must be justified.</li>
    <li>Never remove data to “improve” results.</li>
    <li>Always report what you excluded and why.</li>
    <li>Transparency builds trust.</li>
  </ul>
</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/reporting/mini-case-study-end-to-end/">
    Next Lesson → Mini Case Study (End-to-End Descriptive Report)
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_reporting_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/reporting/outliers-and-exclusions/",
    label:"Lesson 8 — Outliers, Exclusions, and Transparency",
    ts:Date.now()
  }));
})();
</script>