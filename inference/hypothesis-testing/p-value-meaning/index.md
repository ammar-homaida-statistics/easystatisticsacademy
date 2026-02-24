---
layout: default
title: "4. p-Value: Meaning and Interpretation"
description: "Define the p-value precisely, understand its probabilistic meaning under H0, and avoid common misinterpretations."
permalink: /inference/hypothesis-testing/p-value-meaning/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 establishes the formal definition of the p-value and correct interpretation.
        Applied examples, simulations, and reporting templates will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_hypothesis_testing_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/hypothesis-testing/p-value-meaning/",
      label: "Lesson 4 — p-Value: Meaning and Interpretation",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/hypothesis-testing/",
      label: "Block 3 — Hypothesis Testing",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">p-value</span>
        <span class="badge">Evidence</span>
      </div>

      <h1>4. p-Value: Meaning and Interpretation</h1>

      <p class="lead">
        The p-value measures how extreme the observed test statistic would be
        <strong>if the null hypothesis were true</strong>.
        It is a probability computed under the null model — not a probability that the null is true.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/">Back to Block 3</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        The p-value quantifies extremeness under H<sub>0</sub>.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define the p-value formally, interpret it correctly,
      and identify common misconceptions.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Formal definition</h2>
      <p style="margin:0;">
        The p-value is the probability, under H<sub>0</sub>,
        of obtaining a test statistic at least as extreme
        as the one observed.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Mathematical definition</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Two-sided test</h3>
      <p style="margin:0;">
        \[
        p = P\big(|T| \ge |t_{\text{obs}}| \mid H_0\big)
        \]
      </p>
    </div>

    <div class="card">
      <h3>One-sided (greater)</h3>
      <p style="margin:0;">
        \[
        p = P\big(T \ge t_{\text{obs}} \mid H_0\big)
        \]
      </p>
    </div>

    <div class="card">
      <h3>One-sided (smaller)</h3>
      <p style="margin:0;">
        \[
        p = P\big(T \le t_{\text{obs}} \mid H_0\big)
        \]
      </p>
    </div>

    <div class="card">
      <h3>Key condition</h3>
      <p style="margin:0;">
        All probabilities are computed assuming H<sub>0</sub> is true.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) What the p-value measures</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Small p-value</h3>
      <p style="margin:0;">
        The observed result would be rare if H<sub>0</sub> were true.
      </p>
    </div>

    <div class="card">
      <h3>Large p-value</h3>
      <p style="margin:0;">
        The observed result is consistent with H<sub>0</sub>.
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    A small p-value signals incompatibility between the data and the null model.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) What the p-value is NOT</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Not the probability that H<sub>0</sub> is true</h3>
      <p style="margin:0;">
        The p-value assumes H<sub>0</sub> is true.
        It does not assign a probability to hypotheses.
      </p>
    </div>

    <div class="card">
      <h3>Not the probability that results occurred “by chance”</h3>
      <p style="margin:0;">
        All sampling variability is chance.
        The p-value measures extremeness under a specific model.
      </p>
    </div>

    <div class="card">
      <h3>Not the size of the effect</h3>
      <p style="margin:0;">
        A tiny effect can produce a small p-value if the sample size is large.
      </p>
    </div>

    <div class="card">
      <h3>Not evidence of practical importance</h3>
      <p style="margin:0;">
        Statistical significance does not imply practical significance.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Interpreting a p-value correctly</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Correct interpretation template:
      <br><br>
      “If the null hypothesis were true, the probability of observing
      a test statistic at least this extreme would be ___.”
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Notice the conditional structure: probability of data given H<sub>0</sub>, not probability of H<sub>0</sub> given data.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Relationship to the test statistic</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Larger absolute values of the standardized statistic
      correspond to smaller p-values.
    </p>
  </div>

  <p style="margin-top:.75rem;">
    The p-value is a transformation of the test statistic through its reference distribution.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define the p-value formally</li>
        <li>Interpret it as a probability under H<sub>0</sub></li>
        <li>Avoid common misinterpretations</li>
        <li>Understand its link to the standardized test statistic</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we formalize the role of the significance level \(\alpha\)
        and how it controls Type I error.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/hypothesis-testing/significance-level-alpha/">
          Next lesson: 5. Significance Level (α) →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/hypothesis-testing/test-statistic-standardization/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Test Statistic and Standardization
          </a>
        </div>
      </div>
    </div>
  </div>
</section>