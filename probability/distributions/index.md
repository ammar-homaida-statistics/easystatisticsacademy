---
layout: default
title: Block 5 — Common Distributions
description: Learn the core distributions used everywhere: discrete and continuous families, how to recognize them, compute probabilities, and interpret parameters in real applications.
permalink: /probability/distributions/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Section Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This block introduces the most important named probability distributions (discrete and continuous).
        Lessons are being published in fixed pedagogical order as part of the Probability unit.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited block" for Probability home -->
<script>
  (function () {
    var KEY = "esa_continue_probability_last_block_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/distributions/",
      label: "Block 5 — Common Distributions",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Distributions</span>
        <span class="badge">Discrete</span>
        <span class="badge">Continuous</span>
      </div>

      <h1>Block 5 — Common Distributions</h1>
      <p class="lead">
        Distributions are reusable probability models. This block teaches you how to recognize the right model,
        interpret parameters, compute probabilities, and connect each distribution to real data situations.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/">Back to Probability</a>
        <a class="btn" href="#lessons">Open lessons</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Lessons will be refined without changing order.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>Discrete distributions</strong><span class="meta">Counts and events</span></li>
          <li style="margin:.35rem 0;"><strong>Continuous distributions</strong><span class="meta">Measurements and waiting times</span></li>
          <li style="margin:.35rem 0;"><strong>Parameter meaning</strong><span class="meta">Interpretation & modeling</span></li>
          <li style="margin:.35rem 0;"><strong>Recognition patterns</strong><span class="meta">Which distribution fits?</span></li>
          <li style="margin:.35rem 0;"><strong>Connections</strong><span class="meta">Approximation & relationships</span></li>
          <li style="margin:.35rem 0;"><strong>Software</strong><span class="meta">Excel / R / Python / SPSS later</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-block5" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block5-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block5-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Work through these lessons in order. Each lesson page is active
      (even if still being developed), so you can navigate the full structure now.
    </p>
  </div>

  <h3 style="margin-top:0;">Discrete distributions</h3>
  <div class="grid grid-2" style="margin-top:.75rem;">

    <div class="card lesson-card">
      <h3><a href="/probability/distributions/bernoulli-distribution/">1. Bernoulli Distribution</a></h3>
      <p>Single trial with success/failure; the building block for many models.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/distributions/bernoulli-distribution/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/distributions/binomial-distribution/">2. Binomial Distribution</a></h3>
      <p>Number of successes in n independent Bernoulli trials.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/distributions/binomial-distribution/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/distributions/geometric-distribution/">3. Geometric Distribution</a></h3>
      <p>Waiting time until the first success; memoryless property preview.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/distributions/geometric-distribution/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/distributions/negative-binomial-distribution/">4. Negative Binomial Distribution</a></h3>
      <p>Waiting time until r successes; generalizes geometric.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/distributions/negative-binomial-distribution/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/distributions/poisson-distribution/">5. Poisson Distribution</a></h3>
      <p>Counts of events in time/space under a constant rate model.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/distributions/poisson-distribution/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/distributions/hypergeometric-distribution/">6. Hypergeometric Distribution</a></h3>
      <p>Sampling without replacement; contrasts with binomial.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/distributions/hypergeometric-distribution/">Open lesson</a>
      </div>
    </div>

  </div>

  <h3 style="margin-top:2rem;">Continuous distributions</h3>
  <div class="grid grid-2" style="margin-top:.75rem;">

    <div class="card lesson-card">
      <h3><a href="/probability/distributions/uniform-distribution/">7. Uniform Distribution</a></h3>
      <p>Equal density on an interval; baseline continuous model.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/distributions/uniform-distribution/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/distributions/exponential-distribution/">8. Exponential Distribution</a></h3>
      <p>Waiting times; memorylessness; link to Poisson processes later.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/distributions/exponential-distribution/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/distributions/gamma-distribution/">9. Gamma Distribution</a></h3>
      <p>Flexible waiting time model; includes exponential as a special case.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/distributions/gamma-distribution/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/distributions/beta-distribution/">10. Beta Distribution</a></h3>
      <p>Models probabilities (0–1); foundation for Bayesian updating later.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/distributions/beta-distribution/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/distributions/normal-distribution/">11. Normal Distribution</a></h3>
      <p>The central model: symmetry, standardization, and approximation.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/distributions/normal-distribution/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/distributions/lognormal-distribution/">12. Lognormal Distribution</a></h3>
      <p>Positive skewed data; multiplicative effects; log transform intuition.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/distributions/lognormal-distribution/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 5</h2>
      <ul class="bullets">
        <li>Recognize the most common named distributions from context</li>
        <li>Interpret parameters correctly (what they mean in real systems)</li>
        <li>Compute probabilities using PMF/PDF/CDF logic</li>
        <li>Understand key relationships and approximations (binomial ↔ Poisson, etc.)</li>
        <li>Be ready for convergence tools (LLN & CLT) in Block 6</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/probability/lln-clt/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 6 — Law of Large Numbers &amp; CLT</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading Script -->
<script>
  (function () {
    var KEY = "esa_continue_probability_distributions_lesson_v0";

    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block5");
      var label = document.getElementById("continue-reading-block5-label");
      var btn = document.getElementById("continue-reading-block5-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>