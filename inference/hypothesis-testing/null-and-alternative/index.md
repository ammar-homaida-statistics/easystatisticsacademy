---
layout: default
title: "2. Null and Alternative Hypotheses"
description: "Define null and alternative hypotheses precisely: equality in H0, direction in H1, and how hypothesis form determines the test structure."
permalink: /inference/hypothesis-testing/null-and-alternative/
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
        Version 0 locks the formal structure of null and alternative hypotheses.
        Detailed applied examples and software illustrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_hypothesis_testing_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/hypothesis-testing/null-and-alternative/",
      label: "Lesson 2 — Null and Alternative Hypotheses",
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
        <span class="badge">Lesson 2</span>
        <span class="badge">H<sub>0</sub></span>
        <span class="badge">H<sub>1</sub></span>
      </div>

      <h1>2. Null and Alternative Hypotheses</h1>

      <p class="lead">
        A hypothesis test begins with two competing statements:
        a <strong>null hypothesis</strong> that defines the reference model,
        and an <strong>alternative hypothesis</strong> that defines the type of departure we aim to detect.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/">Back to Block 3</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        The structure of H<sub>0</sub> and H<sub>1</sub> determines the entire logic of the test.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Precisely formulate null and alternative hypotheses, understand why equality belongs in H<sub>0</sub>,
      and distinguish between two-sided and one-sided alternatives.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core principle</h2>
      <p style="margin:0;">
        The null hypothesis must define a <strong>specific reference value</strong>.
        The alternative defines how reality may differ from that reference.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) The null hypothesis (H<sub>0</sub>)</h2>
    <p>
      The null hypothesis represents the baseline claim.
      It typically states that a parameter equals a specific value.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      General form:
      <br><br>
      <strong>H<sub>0</sub>: parameter = reference value</strong>
    </p>
  </div>

  <div class="grid grid-2" style="margin-top:1rem;">
    <div class="card">
      <h3>Mean example</h3>
      <p style="margin:0;">
        \[
        H_0:\ \mu = \mu_0
        \]
      </p>
    </div>

    <div class="card">
      <h3>Proportion example</h3>
      <p style="margin:0;">
        \[
        H_0:\ p = p_0
        \]
      </p>
    </div>

    <div class="card">
      <h3>Difference example</h3>
      <p style="margin:0;">
        \[
        H_0:\ \mu_1 - \mu_2 = 0
        \]
      </p>
    </div>

    <div class="card">
      <h3>Regression example</h3>
      <p style="margin:0;">
        \[
        H_0:\ \beta = 0
        \]
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Equality is placed in H<sub>0</sub> because we need a precise distribution under the null model.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Why equality is in H<sub>0</sub></h2>
    <p>
      Hypothesis testing requires a fully specified probability model under the null.
      Equality provides the exact parameter value needed to compute the sampling distribution of the test statistic.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Important reasoning</h2>
      <p style="margin:0;">
        If H<sub>0</sub> were written with an inequality (for example, \(\mu \ge \mu_0\)),
        then the null would include many possible values of \(\mu\),
        and the distribution of the test statistic would not be uniquely determined.
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    In most introductory tests, H<sub>0</sub> is treated as a <strong>simple hypothesis</strong> (one exact value).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) The alternative hypothesis (H<sub>1</sub> or H<sub>a</sub>)</h2>
    <p>
      The alternative hypothesis defines the direction or type of departure from H<sub>0</sub>.
      It expresses what we are prepared to detect.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Two-sided alternative</h3>
      <p style="margin:0;">
        \[
        H_1:\ \text{parameter} \ne \text{reference value}
        \]
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Detects any difference (larger or smaller).
      </p>
    </div>

    <div class="card">
      <h3>One-sided alternative (greater)</h3>
      <p style="margin:0;">
        \[
        H_1:\ \text{parameter} > \text{reference value}
        \]
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Detects increases only.
      </p>
    </div>

    <div class="card">
      <h3>One-sided alternative (smaller)</h3>
      <p style="margin:0;">
        \[
        H_1:\ \text{parameter} < \text{reference value}
        \]
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Detects decreases only.
      </p>
    </div>

    <div class="card">
      <h3>Directional commitment</h3>
      <p style="margin:0;">
        The direction must be chosen <strong>before</strong> looking at the data.
        Otherwise, the stated error rates no longer match reality.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Choosing one-sided vs two-sided</h2>
    <p>
      The choice affects the rejection region and p-value calculation.
      A one-sided test concentrates the rejection region in one tail.
      A two-sided test splits it across both tails.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Two-sided test</h3>
      <ul class="bullets">
        <li>Use when deviations in both directions matter</li>
        <li>Standard default when direction is not justified</li>
        <li>More conservative for directional claims</li>
      </ul>
    </div>

    <div class="card">
      <h3>One-sided test</h3>
      <ul class="bullets">
        <li>Use only when direction is scientifically justified</li>
        <li>More power in the chosen direction</li>
        <li>Blind to effects in the opposite direction</li>
      </ul>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Do not choose “one-sided” because the observed effect went in that direction.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) A compact template (ready to reuse)</h2>
    <p>
      Most classical tests can be written using one of these three templates.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Two-sided</h3>
      <p style="margin:0;">
        \[
        H_0:\ \theta = \theta_0
        \qquad\text{vs}\qquad
        H_1:\ \theta \ne \theta_0
        \]
      </p>
    </div>

    <div class="card">
      <h3>One-sided (greater)</h3>
      <p style="margin:0;">
        \[
        H_0:\ \theta = \theta_0
        \qquad\text{vs}\qquad
        H_1:\ \theta > \theta_0
        \]
      </p>
    </div>

    <div class="card">
      <h3>One-sided (smaller)</h3>
      <p style="margin:0;">
        \[
        H_0:\ \theta = \theta_0
        \qquad\text{vs}\qquad
        H_1:\ \theta < \theta_0
        \]
      </p>
    </div>

    <div class="card">
      <h3>Meaning of \(\theta\)</h3>
      <p style="margin:0;">
        \(\theta\) can be \(\mu\), \(p\), \(\mu_1-\mu_2\), \(\beta\), \(\sigma^2\), etc.
        The structure stays the same.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Common traps (and how to avoid them)</h2>
    <p>
      Bad hypotheses create bad tests.
      Most errors are conceptual (not computational).
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Trap A: Putting equality in H<sub>1</sub></h3>
      <p style="margin:0;">
        The reference distribution is built under H<sub>0</sub>, so equality belongs there.
      </p>
    </div>

    <div class="card">
      <h3>Trap B: One-sided after seeing data</h3>
      <p style="margin:0;">
        This inflates false positives because you quietly change the rule.
      </p>
    </div>

    <div class="card">
      <h3>Trap C: Vague H<sub>0</sub></h3>
      <p style="margin:0;">
        “No difference” must be written as a specific parameter value (usually 0).
      </p>
    </div>

    <div class="card">
      <h3>Trap D: Testing the wrong parameter</h3>
      <p style="margin:0;">
        Always confirm what parameter your statistic targets (mean, proportion, difference, slope, etc.).
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Formulate H<sub>0</sub> with equality and a specific reference value</li>
        <li>Write correct two-sided and one-sided alternatives</li>
        <li>Understand how hypothesis form determines the rejection region</li>
        <li>Avoid post-hoc directional choices</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we define how evidence is measured using a <strong>test statistic</strong>
        and why standardization puts results on a universal scale.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/hypothesis-testing/test-statistic-standardization/">
          Next lesson: 3. Test Statistic and Standardization →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/hypothesis-testing/what-is-a-hypothesis-test/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: What Is a Hypothesis Test?
          </a>
        </div>
      </div>
    </div>

  </div>
</section>