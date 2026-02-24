---
layout: default
title: "3. Test Statistic and Standardization"
description: "Learn what a test statistic is, why we standardize estimates into SE units, and how standardization creates z/t-style scales for hypothesis testing."
permalink: /inference/hypothesis-testing/test-statistic-standardization/
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
        Version 0 locks the logic of test statistics and standardization.
        Worked examples, visuals, and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_hypothesis_testing_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/hypothesis-testing/test-statistic-standardization/",
      label: "Lesson 3 — Test Statistic and Standardization",
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
        <span class="badge">Lesson 3</span>
        <span class="badge">Test statistic</span>
        <span class="badge">SE units</span>
      </div>

      <h1>3. Test Statistic and Standardization</h1>

      <p class="lead">
        A hypothesis test converts data into a single number that measures evidence against the null.
        This number is the <strong>test statistic</strong>.
        Standardization puts results on a common scale by measuring distance from the null in
        <strong>standard error units</strong>.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/">Back to Block 3</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Core idea: “How many SEs away from the null is the observed estimate?”
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define a test statistic,
      explain standardization, and recognize the universal structure behind z and t tests.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        Most classical tests are built from the same template:
        <strong>(estimate − null value) ÷ standard error</strong>.
        The resulting number is comparable across problems because it is measured in SE units.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What is a test statistic?</h2>
    <p>
      A <strong>test statistic</strong> is a function of the sample that summarizes the evidence against
      the null hypothesis.
      Under the null hypothesis, the test statistic has a known (or approximated) sampling distribution.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      A test statistic is a <strong>statistic</strong> (depends on data), designed so that
      “more extreme” values are less likely under \(H_0\).
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    The p-value will be computed from the sampling distribution of this statistic under \(H_0\).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) The universal structure: distance / uncertainty</h2>
    <p>
      Many tests can be understood as:
      distance between the observed estimate and the null value,
      scaled by the typical sampling variability.
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.05rem;">
      <strong>
      \[
      \text{Test statistic}
      \;=\;
      \frac{\text{estimate} - \text{null value}}{\text{standard error}}
      \]
      </strong>
    </p>
  </div>

  <div class="grid grid-2" style="margin-top:1rem;">
    <div class="card">
      <h3>Numerator = signal</h3>
      <p style="margin:0;">
        \(\text{estimate} - \text{null value}\) measures the observed departure from \(H_0\).
      </p>
    </div>

    <div class="card">
      <h3>Denominator = noise</h3>
      <p style="margin:0;">
        \(\text{SE}\) measures how much the estimate typically varies across samples when \(H_0\) is true.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) What “standardization” means</h2>
    <p>
      Standardization means converting a raw difference into a number of standard errors.
      This creates a universal unit:
      “how many SEs away from the null.”
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Raw difference (not comparable)</h3>
      <p style="margin:0;">
        A difference of 2 units might be huge in one context and tiny in another.
      </p>
    </div>

    <div class="card">
      <h3>SE units (comparable)</h3>
      <p style="margin:0;">
        A value like 3.0 means “three standard errors away,” which is interpretable across problems.
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Standardization is why z/t values can be compared to reference distributions.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) z vs t: same structure, different reference distribution</h2>
    <p>
      The standardized statistic often follows a known distribution under \(H_0\).
      Which distribution you use depends on how the standard error is computed.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>z-style statistics</h3>
      <p style="margin:0;">
        Used when variability is known or when large-sample approximations apply.
      </p>
      <p style="margin-top:.75rem; margin-bottom:0;">
        \[
        Z = \frac{\text{estimate} - \text{null value}}{\text{SE}}
        \quad\text{and}\quad
        Z \approx N(0,1)\ \text{under } H_0
        \]
      </p>
    </div>

    <div class="card">
      <h3>t-style statistics</h3>
      <p style="margin:0;">
        Used when variability is estimated from the same data (common for means).
      </p>
      <p style="margin-top:.75rem; margin-bottom:0;">
        \[
        T = \frac{\text{estimate} - \text{null value}}{\text{SE}}
        \quad\text{and}\quad
        T \sim t_{\text{df}}\ \text{under } H_0
        \]
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    The formula looks the same; the difference is the reference distribution and degrees of freedom.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) “More extreme” depends on the alternative</h2>
    <p>
      Once standardized, you must define what counts as extreme.
      That depends on whether the alternative is two-sided or one-sided.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Two-sided alternative</h3>
      <p style="margin:0;">
        Extremeness is measured by magnitude:
        large \(|T|\) or large \(|Z|\).
      </p>
      <p style="margin-top:.75rem; margin-bottom:0;">
        \[
        \text{extreme} \iff |T|\ \text{is large}
        \]
      </p>
    </div>

    <div class="card">
      <h3>One-sided alternative</h3>
      <p style="margin:0;">
        Extremeness is directional:
        large positive values (or large negative values) depending on \(H_1\).
      </p>
      <p style="margin-top:.75rem; margin-bottom:0;">
        \[
        \text{extreme} \iff T\ \text{is large in the direction of } H_1
        \]
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Common traps (and how to avoid them)</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Trap A: Using SD instead of SE</h3>
      <p style="margin:0;">
        Tests standardize by the <strong>standard error of the estimator</strong>, not the raw data spread.
      </p>
    </div>

    <div class="card">
      <h3>Trap B: Mixing the wrong SE with the wrong distribution</h3>
      <p style="margin:0;">
        If you estimate \(\sigma\) from the sample for a mean test, you typically use a t reference distribution.
      </p>
    </div>

    <div class="card">
      <h3>Trap C: Forgetting the null value</h3>
      <p style="margin:0;">
        Always subtract the hypothesized value from \(H_0\) (often 0 for differences).
      </p>
    </div>

    <div class="card">
      <h3>Trap D: Ignoring the alternative direction</h3>
      <p style="margin:0;">
        The alternative determines whether extremeness is one tail or two tails.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define a test statistic and its role in hypothesis testing</li>
        <li>Explain standardization as “distance in SE units”</li>
        <li>Recognize the universal form \((\text{estimate}-\text{null})/\text{SE}\)</li>
        <li>Understand how z and t tests share structure but differ in reference distributions</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we define the <strong>p-value</strong> precisely and explain what it does (and does not) mean.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/hypothesis-testing/p-value-meaning/">
          Next lesson: 4. p-Value: Meaning and Interpretation →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/hypothesis-testing/null-and-alternative/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Null and Alternative Hypotheses
          </a>
        </div>
      </div>
    </div>

  </div>
</section>