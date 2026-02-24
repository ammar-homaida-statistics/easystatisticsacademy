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
        <span class="badge">H0</span>
        <span class="badge">H1</span>
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
        The structure of H0 and H1 determines the entire logic of the test.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Precisely formulate null and alternative hypotheses, understand why equality belongs in H0,
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
    <h2>1) The Null Hypothesis (H0)</h2>
    <p>
      The null hypothesis represents the baseline claim.
      It typically states that a parameter equals a specific value.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      General form:
      <br><br>
      <strong>H0: parameter = reference value</strong>
    </p>
  </div>

  <div class="grid grid-2" style="margin-top:1rem;">
    <div class="card">
      <h3>Mean example</h3>
      <p style="margin:0;">
        H0: mu = mu0
      </p>
    </div>

    <div class="card">
      <h3>Proportion example</h3>
      <p style="margin:0;">
        H0: p = p0
      </p>
    </div>

    <div class="card">
      <h3>Difference example</h3>
      <p style="margin:0;">
        H0: mu1 − mu2 = 0
      </p>
    </div>

    <div class="card">
      <h3>Regression example</h3>
      <p style="margin:0;">
        H0: beta = 0
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Equality is placed in H0 because we need a precise distribution under the null model.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Why equality is in H0</h2>
    <p>
      Hypothesis testing requires a fully specified probability model.
      Equality provides the exact parameter value needed to compute the sampling distribution.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Important reasoning</h2>
      <p style="margin:0;">
        If H0 were written with inequality (for example, mu ≥ mu0),
        the distribution of the test statistic would not be uniquely determined.
        Therefore, equality belongs in H0.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) The Alternative Hypothesis (H1 or Ha)</h2>
    <p>
      The alternative hypothesis defines the direction or type of departure from H0.
      It expresses what we are prepared to detect.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Two-sided alternative</h3>
      <p>
        H1: parameter ≠ reference value
      </p>
      <p class="muted-mini">
        Detects any difference (larger or smaller).
      </p>
    </div>

    <div class="card">
      <h3>One-sided alternative (greater)</h3>
      <p>
        H1: parameter &gt; reference value
      </p>
      <p class="muted-mini">
        Detects increases only.
      </p>
    </div>

    <div class="card">
      <h3>One-sided alternative (smaller)</h3>
      <p>
        H1: parameter &lt; reference value
      </p>
      <p class="muted-mini">
        Detects decreases only.
      </p>
    </div>

    <div class="card">
      <h3>Directional commitment</h3>
      <p>
        The direction must be chosen before seeing the data.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Choosing one-sided vs two-sided</h2>
    <p>
      The choice affects the rejection region and the p-value calculation.
      A one-sided test concentrates all probability in one tail.
      A two-sided test splits it across both tails.
    </p>
  </div>

  <div class="card">
    <strong>Two-sided test:</strong> more conservative, detects any deviation.<br>
    <strong>One-sided test:</strong> more powerful in one direction, but blind to the opposite direction.
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    The decision must be justified by the research question, not by the observed data.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Logical structure of testing</h2>
  </div>

  <div class="card">
    Step 1: Assume H0 is true.<br>
    Step 2: Compute a test statistic from the data.<br>
    Step 3: Measure how extreme the statistic is under H0.<br>
    Step 4: Decide whether the evidence contradicts H0.
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Formulate null hypotheses using equality</li>
        <li>Specify two-sided and one-sided alternatives correctly</li>
        <li>Understand how hypothesis structure affects the test</li>
        <li>Avoid post-hoc directional changes</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we formalize how evidence is measured using standardized test statistics.
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