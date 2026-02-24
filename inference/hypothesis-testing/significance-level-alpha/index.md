---
layout: default
title: "5. Significance Level (α)"
description: "Define the significance level α, understand its role in controlling Type I error, and distinguish between α and the p-value."
permalink: /inference/hypothesis-testing/significance-level-alpha/
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
        Version 0 establishes the formal meaning of the significance level α
        and its relationship to Type I error.
        Examples, simulations, and decision diagrams will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_hypothesis_testing_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/hypothesis-testing/significance-level-alpha/",
      label: "Lesson 5 — Significance Level (α)",
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
        <span class="badge">Lesson 5</span>
        <span class="badge">α</span>
        <span class="badge">Type I Error</span>
      </div>

      <h1>5. Significance Level (α)</h1>

      <p class="lead">
        The significance level \( \alpha \) is a pre-specified threshold
        that controls the probability of making a Type I error.
        It defines how much false-positive risk we are willing to tolerate.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/">Back to Block 3</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        α is chosen before seeing the data.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define the significance level formally,
      distinguish α from the p-value,
      and understand how α controls Type I error.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core definition</h2>
      <p style="margin:0;">
        The significance level \( \alpha \) is the probability of rejecting \(H_0\)
        when \(H_0\) is actually true.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Formal probability statement</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      \[
      \alpha = P(\text{Reject } H_0 \mid H_0 \text{ is true})
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This is a long-run frequency statement across repeated experiments.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Where α enters the procedure</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Critical value approach</h3>
      <p style="margin:0;">
        Choose a cutoff so that the rejection region has probability α under \(H_0\).
      </p>
    </div>

    <div class="card">
      <h3>p-value approach</h3>
      <p style="margin:0;">
        Reject \(H_0\) if:
        \[
        p \le \alpha
        \]
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Both approaches are mathematically equivalent.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Common α values</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>α = 0.10</h3>
      <p style="margin:0;">Less strict, higher false-positive tolerance.</p>
    </div>

    <div class="card">
      <h3>α = 0.05</h3>
      <p style="margin:0;">Standard conventional choice in many fields.</p>
    </div>

    <div class="card">
      <h3>α = 0.01</h3>
      <p style="margin:0;">More stringent, lower false-positive rate.</p>
    </div>

    <div class="card">
      <h3>Smaller α</h3>
      <p style="margin:0;">Harder to reject \(H_0\); reduces Type I error.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) α vs p-value</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>α</h3>
      <ul class="bullets">
        <li>Chosen before observing data</li>
        <li>Controls false-positive rate</li>
        <li>Fixed decision threshold</li>
      </ul>
    </div>

    <div class="card">
      <h3>p-value</h3>
      <ul class="bullets">
        <li>Computed from the data</li>
        <li>Measures extremeness under \(H_0\)</li>
        <li>Compared to α for decision</li>
      </ul>
    </div>
  </div>

  <div class="card" style="margin-top:1rem;">
    Decision rule:
    <br><br>
    If \(p \le \alpha\) → reject \(H_0\).  
    If \(p > \alpha\) → fail to reject \(H_0\).
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Interpretation in repeated sampling</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      If we repeat the same experiment many times under \(H_0\),
      approximately \(100\alpha\%\) of those experiments
      would incorrectly reject the null hypothesis.
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    α is a property of the procedure — not of a single dataset.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Common misconceptions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Not the probability that H<sub>0</sub> is true</h3>
      <p style="margin:0;">α controls error rate, not belief in hypotheses.</p>
    </div>

    <div class="card">
      <h3>Not adjustable after seeing data</h3>
      <p style="margin:0;">Choosing α post hoc invalidates error guarantees.</p>
    </div>

    <div class="card">
      <h3>Smaller α ≠ better in all cases</h3>
      <p style="margin:0;">Reducing α increases the risk of missing real effects.</p>
    </div>

    <div class="card">
      <h3>α does not measure effect size</h3>
      <p style="margin:0;">It only sets a decision threshold.</p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define α formally</li>
        <li>Understand its link to Type I error</li>
        <li>Distinguish α from the p-value</li>
        <li>Interpret α as long-run false-positive control</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we examine Type I and Type II errors
        and how they interact with power.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/hypothesis-testing/type1-type2-errors/">
          Next lesson: 6. Type I and Type II Errors →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/hypothesis-testing/p-value-meaning/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: p-Value: Meaning and Interpretation
          </a>
        </div>
      </div>
    </div>
  </div>
</section>