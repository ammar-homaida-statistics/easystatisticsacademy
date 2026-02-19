---
layout: default
title: "10. Beta Distribution"
description: "A flexible distribution on [0, 1] used to model probabilities and proportions; conjugate prior for Bernoulli/binomial models."
permalink: /probability/distributions/beta-distribution/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 defines structure, parameters, and core formulas.
        Visual intuition, worked examples, and simulations will be added next.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/distributions/beta-distribution/",
      label: "Lesson 10 — Beta Distribution",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 10</span>
        <span class="badge">Continuous</span>
        <span class="badge">Proportions</span>
      </div>

      <h1>10. Beta Distribution</h1>

      <p class="lead">
        The Beta distribution is defined on <strong>[0, 1]</strong> and is one of the most useful continuous
        distributions in statistics because it models <strong>probabilities, proportions, and rates</strong>.
        Its shape is extremely flexible and is controlled by two positive parameters.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Think: “a distribution for an unknown probability p.”
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition</h2>
    <p>
      A random variable <strong>X</strong> follows a Beta distribution with parameters
      <strong>&alpha; &gt; 0</strong> and <strong>&beta; &gt; 0</strong> if it has probability density function:
    </p>
  </div>

  <div class="card">
    <p style="font-size:1.1rem; margin:0;">
      $$
      f(x)=\frac{1}{B(\alpha,\beta)}\,x^{\alpha-1}(1-x)^{\beta-1},
      \quad 0\le x\le 1
      $$
    </p>

    <p class="muted-mini" style="margin-top:.75rem;">
      Here <strong>B(&alpha;,&beta;)</strong> is the Beta function:
      $$
      B(\alpha,\beta)=\int_0^1 x^{\alpha-1}(1-x)^{\beta-1}\,dx
      $$
      and it connects to the Gamma function via:
      $$
      B(\alpha,\beta)=\frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}.
      $$
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Beta is the natural distribution for uncertain probabilities.</strong>
        If a parameter must stay between 0 and 1, Beta is a first-choice model.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Parameters and shape intuition</h2>
    <p>
      The parameters <strong>&alpha;</strong> and <strong>&beta;</strong> control the shape near 0 and near 1.
      Different values produce very different behaviors.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>How to read &alpha; and &beta;</h3>
      <ul class="bullets">
        <li>If <strong>&alpha; &gt; 1</strong>, density tends to be low near 0; if <strong>&alpha; &lt; 1</strong>, it spikes near 0.</li>
        <li>If <strong>&beta; &gt; 1</strong>, density tends to be low near 1; if <strong>&beta; &lt; 1</strong>, it spikes near 1.</li>
        <li>If <strong>&alpha; = &beta;</strong>, the distribution is symmetric around 0.5.</li>
      </ul>
    </div>

    <div class="card">
      <h3>Common shape regimes</h3>
      <ul class="bullets">
        <li><strong>&alpha; = &beta; = 1</strong> → Uniform on [0, 1]</li>
        <li><strong>&alpha; &gt; 1, &beta; &gt; 1</strong> → unimodal (peak inside the interval)</li>
        <li><strong>&alpha; &lt; 1, &beta; &lt; 1</strong> → U-shaped (mass near 0 and 1)</li>
        <li><strong>&alpha; \gg &beta;</strong> → mass near 1; <strong>&beta; \gg &alpha;</strong> → mass near 0</li>
      </ul>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    In practice: choose &alpha; and &beta; to encode how strongly you believe the probability is near 0, near 1, or around the middle.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Mean and variance</h2>
    <p>
      The Beta distribution has closed-form mean and variance, which make it easy to interpret.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      $$
      \mathbb{E}[X]=\frac{\alpha}{\alpha+\beta}
      $$
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      $$
      \mathrm{Var}(X)=\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}
      $$
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Interpretation shortcut</h2>
      <p style="margin:0;">
        The sum <strong>&alpha;+&beta;</strong> controls concentration:
        larger values make the distribution tighter (less uncertain), smaller values make it wider (more uncertain).
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Mode (when it exists)</h2>
    <p>
      When <strong>&alpha; &gt; 1</strong> and <strong>&beta; &gt; 1</strong>, the Beta distribution has a single interior mode.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      $$
      \mathrm{mode}(X)=\frac{\alpha-1}{\alpha+\beta-2},
      \quad \text{for } \alpha>1,\ \beta>1.
      $$
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    If &alpha; ≤ 1 or &beta; ≤ 1, the highest density may occur at the boundaries (0 or 1).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Why Beta matters (statistical modeling viewpoint)</h2>
    <p>
      Beta is central in probability and statistics because it naturally models unknown probabilities.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Proportions and rates</h3>
      <ul class="bullets">
        <li>Click-through rate (CTR)</li>
        <li>Defect rate in manufacturing</li>
        <li>Prevalence (proportion) in epidemiology</li>
        <li>Conversion rate in business analytics</li>
      </ul>
    </div>

    <div class="card">
      <h3>Bayesian connection (preview)</h3>
      <p>
        In Bayesian inference, if the probability of “success” is <strong>p</strong>, a common prior model is:
      </p>
      <p style="margin:0;">
        $$
        p \sim \mathrm{Beta}(\alpha,\beta).
        $$
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Later, you will see that Beta combines cleanly with Bernoulli/binomial data (conjugacy).
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Forgetting the support is <strong>[0, 1]</strong> (Beta cannot model values outside this interval)</li>
        <li>Interpreting &alpha; and &beta; as “mean and variance” directly (they are shape parameters)</li>
        <li>Ignoring the role of <strong>&alpha;+&beta;</strong> in controlling uncertainty</li>
        <li>Using Beta for data values that are exactly 0 or 1 without thinking (boundary issues may need special handling)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Know the Beta PDF on [0, 1] and the role of the Beta function</li>
        <li>Interpret how &alpha; and &beta; shape the distribution</li>
        <li>Compute mean and variance</li>
        <li>Understand why Beta is a natural model for unknown probabilities</li>
        <li>Be ready for the Normal distribution next</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we study the most important distribution in statistics:
        the <strong>Normal distribution</strong> and its role as a universal approximation.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/distributions/normal-distribution/">
          Next lesson: 11. Normal Distribution →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/distributions/gamma-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 9 — Gamma Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>