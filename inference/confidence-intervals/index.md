<!-- =========================================================
BLOCK 2 — CONFIDENCE INTERVALS
File: /inference/confidence-intervals/index.md
========================================================= -->
---
layout: default
title: Block 2 — Confidence Intervals
description: Build confidence intervals correctly: the logic of coverage, margin of error, critical values (z/t), and interval construction for means, proportions, and comparisons.
permalink: /inference/confidence-intervals/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This block develops <strong>confidence intervals</strong> from first principles:
        coverage interpretation, margin of error, and how the correct sampling distribution
        (z or t) turns an estimate and a standard error into an interval.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited block" -->
<script>
  (function () {
    var KEY = "esa_continue_inference_last_block_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/",
      label: "Block 2 — Confidence Intervals",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Intervals</span>
        <span class="badge">Coverage</span>
        <span class="badge">Margin of error</span>
      </div>

      <h1>Block 2 — Confidence Intervals</h1>
      <p class="lead">
        A confidence interval is a structured way to report uncertainty.
        This block teaches how intervals are constructed, what they mean,
        and how to choose the correct critical value (z or t) depending on what is known.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/">Back to Statistical Inference</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Lessons will expand without changing URLs or order.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>CI logic</strong><span class="meta">Coverage as long-run frequency</span></li>
          <li style="margin:.35rem 0;"><strong>Margin of error</strong><span class="meta">Critical value × SE</span></li>
          <li style="margin:.35rem 0;"><strong>z vs t</strong><span class="meta">Known vs unknown \(\sigma\)</span></li>
          <li style="margin:.35rem 0;"><strong>Core CIs</strong><span class="meta">Mean, proportion, difference of means</span></li>
          <li style="margin:.35rem 0;"><strong>Assumptions</strong><span class="meta">Independence, normality/CLT, conditions</span></li>
          <li style="margin:.35rem 0;"><strong>Interpretation</strong><span class="meta">Width, precision, and reporting</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading (lesson-level placeholder key for this block) -->
<section class="section" id="continue-reading-block2" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block2-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block2-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons are published in order to keep interval logic coherent.
      The list below is the permanent structure for this block.
    </p>
  </div>

  <div class="grid grid-2">

    <!-- Lesson 1 -->
    <div class="card lesson-card">
      <h3><a href="/inference/confidence-intervals/what-is-a-confidence-interval/">1. What Is a Confidence Interval?</a></h3>
      <p>Intervals as procedures with long-run coverage: the meaning of “95% confidence”.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/confidence-intervals/what-is-a-confidence-interval/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 2 -->
    <div class="card lesson-card">
      <h3><a href="/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/">2. CI Blueprint: Estimate ± Margin of Error</a></h3>
      <p>The universal structure: estimate, SE, critical value, and margin of error.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 3 -->
    <div class="card lesson-card">
      <h3><a href="/inference/confidence-intervals/critical-values-z-and-t/">3. Critical Values: z and t</a></h3>
      <p>How critical values are chosen; two-sided vs one-sided; degrees of freedom for t.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/confidence-intervals/critical-values-z-and-t/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 4 -->
    <div class="card lesson-card">
      <h3><a href="/inference/confidence-intervals/ci-for-mean-sigma-known-z/">4. CI for a Mean (σ Known): z-Interval</a></h3>
      <p>Constructing \(\mu\) intervals when \(\sigma\) is known (rare, but clarifies the logic).</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/confidence-intervals/ci-for-mean-sigma-known-z/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 5 -->
    <div class="card lesson-card">
      <h3><a href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/">5. CI for a Mean (σ Unknown): t-Interval</a></h3>
      <p>Using \(s\), t critical values, and interpreting degrees of freedom.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 6 -->
    <div class="card lesson-card">
      <h3><a href="/inference/confidence-intervals/conditions-normality-clt-independence/">6. Conditions for Valid CIs</a></h3>
      <p>Independence, random sampling, normality/CLT logic, and what to do when conditions fail.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/confidence-intervals/conditions-normality-clt-independence/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 7 -->
    <div class="card lesson-card">
      <h3><a href="/inference/confidence-intervals/ci-for-proportion/">7. CI for a Proportion</a></h3>
      <p>Intervals for \(p\): standard error \( \sqrt{\hat{p}(1-\hat{p})/n}\) and the success–failure condition.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/confidence-intervals/ci-for-proportion/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 8 -->
    <div class="card lesson-card">
      <h3><a href="/inference/confidence-intervals/ci-for-difference-of-means-independent/">8. CI for Difference of Means (Independent Samples)</a></h3>
      <p>Two groups: standard error for \(\bar{X}_1-\bar{X}_2\), Welch vs pooled preview.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/confidence-intervals/ci-for-difference-of-means-independent/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 9 -->
    <div class="card lesson-card">
      <h3><a href="/inference/confidence-intervals/ci-for-difference-of-proportions/">9. CI for Difference of Proportions</a></h3>
      <p>Comparing two rates: \(\hat{p}_1-\hat{p}_2\) and its standard error.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/confidence-intervals/ci-for-difference-of-proportions/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 10 -->
    <div class="card lesson-card">
      <h3><a href="/inference/confidence-intervals/ci-for-paired-mean-difference/">10. CI for Paired Data (Mean of Differences)</a></h3>
      <p>Paired designs: reduce to one-sample t-interval on the difference scores.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/confidence-intervals/ci-for-paired-mean-difference/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 11 -->
    <div class="card lesson-card">
      <h3><a href="/inference/confidence-intervals/width-and-precision-what-controls/">11. CI Width and Precision: What Controls It?</a></h3>
      <p>How \(n\), variability, and confidence level change interval width; planning for precision.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/confidence-intervals/width-and-precision-what-controls/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 12 -->
    <div class="card lesson-card">
      <h3><a href="/inference/confidence-intervals/common-mistakes-and-interpretation/">12. Interpretation and Common Mistakes</a></h3>
      <p>Correct wording, wrong wording, and typical beginner traps (parameter probability, overlap myths, etc.).</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/confidence-intervals/common-mistakes-and-interpretation/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 2</h2>
      <ul class="bullets">
        <li>Construct confidence intervals using the universal CI blueprint</li>
        <li>Choose correct critical values (z or t) and interpret degrees of freedom</li>
        <li>Build CIs for means, proportions, and basic comparisons</li>
        <li>Check validity conditions and interpret intervals responsibly</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/inference/hypothesis-testing/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 3 — Hypothesis Testing</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading Script (lesson-level) -->
<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block2");
      var label = document.getElementById("continue-reading-block2-label");
      var btn = document.getElementById("continue-reading-block2-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>