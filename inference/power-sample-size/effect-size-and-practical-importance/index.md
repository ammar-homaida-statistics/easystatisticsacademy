---
layout: default
title: "2. Effect Size and Practical Importance"
description: "Define effect size formally and distinguish statistical significance from practical importance."
permalink: /inference/power-sample-size/effect-size-and-practical-importance/
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
        Version 0 establishes the formal definition of effect size
        and clarifies the difference between statistical and practical importance.
        Applied examples and domain-specific interpretations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_power_sample_size_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/power-sample-size/effect-size-and-practical-importance/",
      label: "Lesson 2 — Effect Size & Practical Importance",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/power-sample-size/",
      label: "Block 5 — Power & Sample Size",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">Effect Size</span>
        <span class="badge">Magnitude</span>
      </div>

      <h1>2. Effect Size and Practical Importance</h1>

      <p class="lead">
        Effect size measures the magnitude of a phenomenon.
        It answers a different question than statistical significance:
        not “Is there evidence?” but “How large is the effect?”
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/power-sample-size/">Back to Block 5</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Detectability and importance are not the same concept.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define effect size formally,
      understand standardized vs raw effect sizes,
      and distinguish statistical significance from practical importance.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core principle</h2>
      <p style="margin:0;">
        Statistical significance depends on sample size.
        Effect size describes magnitude independently of sample size.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Raw effect size</h2>
  </div>

  <div class="card">
    Difference in means:
    \[
    \Delta = \mu_1 - \mu_2
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Difference in proportions:
    \[
    \Delta = p_1 - p_2
    \]
  </div>

  <p class="muted-mini">
    Raw effect size keeps the original measurement scale.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Standardized effect size</h2>
  </div>

  <div class="card">
    Cohen's d:
    \[
    d = \frac{\mu_1 - \mu_2}{\sigma}
    \]
  </div>

  <p>
    Standardization expresses the difference in units of standard deviation,
    allowing comparison across studies.
  </p>

  <div class="card" style="margin-top:1rem;">
    For ANOVA:
    <br><br>
    Eta-squared:
    \[
    \eta^2 = \frac{SS_{Between}}{SS_{Total}}
    \]
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Statistical vs practical significance</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Statistical significance</h3>
      <p>
        Determined by p-value and alpha.
        Influenced by sample size.
      </p>
    </div>

    <div class="card">
      <h3>Practical importance</h3>
      <p>
        Determined by magnitude and domain context.
        Independent of sample size.
      </p>
    </div>
  </div>

  <div class="card" style="margin-top:1rem;">
    A very small effect can be statistically significant
    if sample size is large.
  </div>

  <div class="card" style="margin-top:1rem;">
    A meaningful effect may fail to reach significance
    in a small sample study.
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Role in power analysis</h2>
  </div>

  <div class="card">
    Power increases as effect size increases.
  </div>

  <p>
    Sample size calculations require specifying
    the minimum effect size worth detecting.
  </p>

  <div class="card" style="margin-top:1rem;">
    Study planning question:
    <br><br>
    What is the smallest meaningful effect?
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define raw and standardized effect sizes</li>
        <li>Distinguish magnitude from significance</li>
        <li>Understand role of effect size in power</li>
        <li>Avoid confusing statistical with practical importance</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now visualize how power changes
        as effect size, alpha, and sample size vary.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/power-sample-size/power-curve-and-tradeoffs/">
          Next lesson: 3. Power Curves and Trade-offs →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/power-sample-size/what-is-statistical-power/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: What Is Statistical Power?
          </a>
        </div>
      </div>
    </div>
  </div>
</section>