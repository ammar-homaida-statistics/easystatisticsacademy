---
layout: default
title: "6. Conditions for Valid Confidence Intervals"
description: "Confidence intervals require structural assumptions. This lesson defines the conditions (independence, random sampling, normality/CLT, and proportion checks) and explains what happens when they fail."
permalink: /inference/confidence-intervals/conditions-normality-clt-independence/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 locks the <strong>validity checklist</strong>. Diagnostics and fixes come later.
        The goal is to prevent “correct formulas” applied to invalid settings.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Inference Block 2 -->
<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/conditions-normality-clt-independence/",
      label: "Lesson 6 — Conditions for Valid Confidence Intervals",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/confidence-intervals/",
      label: "Block 2 — Confidence Intervals",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Lesson 6</span>
        <span class="badge">Assumptions</span>
        <span class="badge">Validity</span>
      </div>

      <h1>6. Conditions for Valid Confidence Intervals</h1>
      <p class="lead">
        A confidence interval is only meaningful if its assumptions are reasonable.
        This lesson provides a clean checklist: <strong>design → independence → distribution conditions</strong>.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: checklist first. Fixes and alternatives (bootstrap, robust intervals) come later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to verify whether a confidence interval method is valid for your data,
      and explain what kind of failure occurs if assumptions do not hold.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Confidence intervals are probability statements about the long-run behavior of the method.</strong>
        If the method’s assumptions are violated, the stated confidence level may no longer be true.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) The validity checklist (big picture)</h2>
    <p>
      Before computing any CI, check in this order:
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>A) Target & design</h3>
      <ul class="bullets">
        <li>Is the population/parameter clearly defined?</li>
        <li>Is the sampling/assignment mechanism credible?</li>
        <li>Are you estimating the right parameter for the question?</li>
      </ul>
    </div>

    <div class="card">
      <h3>B) Independence</h3>
      <ul class="bullets">
        <li>Are observations independent?</li>
        <li>Any clustering, repeated measures, time dependence?</li>
        <li>If sampling without replacement: is the sample small relative to population?</li>
      </ul>
    </div>

    <div class="card">
      <h3>C) Distribution condition (mean)</h3>
      <ul class="bullets">
        <li>Population approximately normal <em>or</em> sample large (CLT)</li>
        <li>No extreme outliers for small/moderate n</li>
      </ul>
    </div>

    <div class="card">
      <h3>D) Distribution condition (proportion)</h3>
      <ul class="bullets">
        <li>Large counts: \(n\hat p\) and \(n(1-\hat p)\) sufficiently large</li>
        <li>Independence (same as above)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Independence (the most important assumption)</h2>
    <p>
      Most CI formulas assume the data behave like a random sample of independent observations.
      If independence fails, standard errors are wrong.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Independence is plausible when</h3>
      <ul class="bullets">
        <li>Random sampling from a population</li>
        <li>Random assignment in an experiment</li>
        <li>No repeated measurements from the same unit</li>
      </ul>
    </div>

    <div class="card">
      <h3>Independence is questionable when</h3>
      <ul class="bullets">
        <li>Cluster sampling (schools, families, hospitals)</li>
        <li>Time series / sequential measurements</li>
        <li>Before-after on the same subjects (paired data)</li>
      </ul>
    </div>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Practical warning</h2>
      <p style="margin:0;">
        Violated independence typically makes intervals <strong>too narrow</strong> (overconfident),
        because the effective sample size is smaller than n.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) The “10% condition” (sampling without replacement)</h2>
    <p>
      If you sample without replacement from a finite population, independence is approximately valid
      when the sample is small relative to the population.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      A common rule:
      <strong>\(n \le 0.10\,N\)</strong>
      (sample size is at most 10% of the population size).
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    When this fails, a finite population correction may be needed (later topic).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Mean intervals: normality vs CLT</h2>
    <p>
      For confidence intervals about a mean (z or t), validity depends on how close the sampling distribution
      of \(\bar X\) is to normal.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Small n</h3>
      <p>
        If n is small, you need the population distribution to be reasonably normal,
        and you must be careful with outliers/skewness.
      </p>
    </div>

    <div class="card">
      <h3>Large n (CLT)</h3>
      <p>
        If n is large, the Central Limit Theorem makes \(\bar X\) approximately normal
        even if the population is not perfectly normal (unless extremely heavy-tailed).
      </p>
    </div>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Outliers matter</h3>
    <p style="margin:0;">
      One extreme outlier can dominate the mean and inflate/ distort S, especially for small samples.
      In that case, a “valid-looking” CI can be misleading.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Proportion intervals: large-count condition</h2>
    <p>
      For the standard z interval for a proportion, validity comes from a normal approximation to the binomial.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      Check counts (often with \(\hat p\)):
      \[
      n\hat p \ge 10
      \quad \text{and} \quad
      n(1-\hat p) \ge 10
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    If these counts are small (or p is near 0 or 1), normal-based CIs can perform poorly.
    Alternatives (Wilson / exact / bootstrap) come later.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) What happens when conditions fail?</h2>
    <p>
      A failure typically shows up as incorrect coverage:
      the method does not achieve the advertised confidence level.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Too narrow intervals</h3>
      <p>
        Often caused by dependence or under-estimated SE.
        Leads to overconfidence.
      </p>
    </div>

    <div class="card">
      <h3>Incorrect center or misleading target</h3>
      <p>
        Often caused by sampling bias or a poorly defined population/parameter.
        Even “wide” intervals can be meaningless if the target is wrong.
      </p>
    </div>

    <div class="card">
      <h3>Skew/heavy tails (mean case)</h3>
      <p>
        Can break the normal approximation for small/moderate samples.
      </p>
    </div>

    <div class="card">
      <h3>Small counts (proportion case)</h3>
      <p>
        Normal approximation fails; coverage can be far from the nominal level.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>7) Common traps</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Trap A: Treating “large n” as magic</h3>
      <p>
        Large n helps, but dependence and bias can still destroy validity.
      </p>
    </div>

    <div class="card">
      <h3>Trap B: Ignoring the study design</h3>
      <p>
        The design determines what inference is allowed. Formulas don’t fix sampling bias.
      </p>
    </div>

    <div class="card">
      <h3>Trap C: Skipping count checks for proportions</h3>
      <p>
        The z-proportion interval requires large counts.
      </p>
    </div>

    <div class="card">
      <h3>Trap D: Confusing SD vs SE</h3>
      <p>
        The interval width must be driven by SE, not raw variability.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Apply a correct validity checklist before computing a CI</li>
        <li>Identify when z/t assumptions for a mean are reasonable</li>
        <li>Identify when the normal approximation for a proportion is reasonable</li>
        <li>Explain how failures affect coverage and interpretation</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next we construct a confidence interval for a <strong>proportion</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/ci-for-proportion/">
          Next lesson: 7. CI for a Proportion →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 5: CI for a Mean (t Interval)
          </a>
        </div>
      </div>
    </div>

  </div>
</section>