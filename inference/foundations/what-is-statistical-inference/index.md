---
layout: default
title: "1. What Is Statistical Inference?"
description: "Inference is structured reasoning from a sample to a population under uncertainty. Learn what inference does, what it assumes, and what it can (and cannot) claim."
permalink: /inference/foundations/what-is-statistical-inference/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the structure and the correct conceptual flow. Examples, graphs,
        and software demonstrations will be added later without changing the lesson order.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Inference Block 1 -->
<script>
  (function () {
    var KEY = "esa_continue_inference_foundations_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/foundations/what-is-statistical-inference/",
      label: "Lesson 1 — What Is Statistical Inference?",
      ts: Date.now()
    }));

    // (Optional but consistent) also refresh "last visited block" for Inference home
    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/foundations/",
      label: "Block 1 — Inference Foundations",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Lesson 1</span>
        <span class="badge">Foundations</span>
        <span class="badge">Uncertainty</span>
      </div>

      <h1>1. What Is Statistical Inference?</h1>
      <p class="lead">
        Statistical inference is the disciplined way we use a <strong>sample</strong> to learn about a
        <strong>population</strong> when we cannot observe everyone. It answers: <em>What can we claim, and how uncertain are we?</em>
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/foundations/">Back to Block 1</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: structure first. Visuals and software examples will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to explain what statistical inference is, distinguish
      <strong>describing a dataset</strong> from <strong>learning about a population</strong>, and state what inference can
      (and cannot) justify.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Inference is not certainty.</strong> It is a framework for making population-level statements
        using sample evidence, while explicitly quantifying uncertainty.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Descriptive vs inferential thinking</h2>
    <p>
      A common confusion is treating descriptive statistics as if they automatically generalize.
      They do not. Inference requires assumptions about how the data were generated.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Descriptive statistics</h3>
      <ul class="bullets">
        <li>Summarize the observed data</li>
        <li>Mean, median, SD, plots, tables</li>
        <li>No generalization required</li>
      </ul>
      <p class="muted-mini">
        Question: “What happened in <em>this</em> dataset?”
      </p>
    </div>

    <div class="card">
      <h3>Statistical inference</h3>
      <ul class="bullets">
        <li>Learn about a population from a sample</li>
        <li>Quantify uncertainty (SE, CI, p-values)</li>
        <li>Depends on design/assumptions</li>
      </ul>
      <p class="muted-mini">
        Question: “What can we say about the <em>population</em>?”
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Why inference is needed</h2>
    <p>
      If we could measure everyone, there would be no inference problem.
      But in real work we face:
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Constraints</h3>
      <ul class="bullets">
        <li>Cost/time limits</li>
        <li>Ethical constraints (medicine, experiments)</li>
        <li>Population may be huge or changing</li>
      </ul>
    </div>

    <div class="card">
      <h3>Variability</h3>
      <p style="margin:0;">
        Even with a good sampling method, different random samples lead to different summaries.
        <strong>This sampling variability is the source of uncertainty.</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) The inference objects (preview)</h2>
    <p>
      Inference has a clean “object model”. We will formalize it in the next lessons,
      but you should already see the structure:
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li><strong>Population</strong> → the full group we care about</li>
      <li><strong>Parameter</strong> → the target population quantity (e.g., mean \(\mu\), proportion \(p\))</li>
      <li><strong>Sample</strong> → the observed subset of data</li>
      <li><strong>Statistic</strong> → a number computed from the sample (e.g., \(\bar X\), \(\hat p\))</li>
      <li><strong>Estimator</strong> → a rule that maps data to an estimate (a statistic viewed as a method)</li>
      <li><strong>Standard error</strong> → the scale of estimator variability across samples</li>
    </ul>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    A key mental shift: the parameter is fixed but unknown; the statistic is random because the sample is random.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) What inference produces</h2>
    <p>
      Inference typically produces outputs in two forms:
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Estimation</h3>
      <ul class="bullets">
        <li><strong>Point estimate</strong> (one number)</li>
        <li><strong>Interval estimate</strong> (confidence interval)</li>
      </ul>
      <p class="muted-mini">
        Output: “A plausible range for the parameter.”
      </p>
    </div>

    <div class="card">
      <h3>Testing / decisions</h3>
      <ul class="bullets">
        <li>Hypothesis test</li>
        <li>Test statistic + p-value</li>
        <li>Decision under a chosen \(\alpha\)</li>
      </ul>
      <p class="muted-mini">
        Output: “Is the data inconsistent with a claim?”
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) What inference cannot do (common misconceptions)</h2>
    <p>
      Many mistakes happen because people ask inference to do something it is not designed to do.
      Here are the big ones we will revisit throughout the unit:
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Misconception A: “A sample result is the truth”</h3>
      <p>
        A sample estimate is not the population parameter. It is one realization from a sampling process.
      </p>
    </div>

    <div class="card">
      <h3>Misconception B: “Randomness cancels out automatically”</h3>
      <p>
        Randomness decreases with larger \(n\), but it never becomes zero. Uncertainty is managed, not removed.
      </p>
    </div>

    <div class="card">
      <h3>Misconception C: “p-value = probability the null is true”</h3>
      <p>
        A p-value is a conditional probability about data under an assumption, not a direct probability of a hypothesis.
      </p>
    </div>

    <div class="card">
      <h3>Misconception D: “Inference fixes bad data”</h3>
      <p>
        Biased sampling, measurement error, and confounding cannot be repaired by formulas. Design dominates.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Explain inference as population learning from sample evidence</li>
        <li>Separate descriptive summaries from inferential claims</li>
        <li>Identify the key objects: parameter, statistic, estimator, SE</li>
        <li>Know the typical outputs: estimation (CI) and testing (p-value)</li>
        <li>Avoid the most common inference misconceptions</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we formalize the target of inference by defining
        <strong>populations</strong> and <strong>parameters</strong> precisely.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/foundations/populations-parameters-target/">
          Next lesson: 2. Populations, Parameters, and the Target of Estimation →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Back to Block 1</div>
        <div class="mini-body">
          <a href="/inference/foundations/" style="color:#1a73e8; text-decoration:underline;">
            Block 1 — Inference Foundations
          </a>
        </div>
      </div>
    </div>

  </div>
</section>