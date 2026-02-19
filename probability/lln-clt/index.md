---
layout: default
title: Block 6 — Law of Large Numbers & CLT
description: Understand convergence in probability, why averages stabilize (LLN), and why sums become approximately normal (CLT). These results power modern statistical inference.
permalink: /probability/lln-clt/
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
        This block introduces convergence ideas and the two most important
        theoretical results in probability: the Law of Large Numbers (LLN)
        and the Central Limit Theorem (CLT).
        These results explain why statistical inference works.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited block" -->
<script>
  (function () {
    var KEY = "esa_continue_probability_last_block_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/lln-clt/",
      label: "Block 6 — Law of Large Numbers & CLT",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Convergence</span>
        <span class="badge">LLN</span>
        <span class="badge">CLT</span>
      </div>

      <h1>Block 6 — Law of Large Numbers &amp; CLT</h1>
      <p class="lead">
        Why do averages stabilize?  
        Why do sums look normal?  
        This block explains the mathematical foundations behind statistical inference.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/">Back to Probability</a>
        <a class="btn" href="#lessons">Open lessons</a>
      </div>

      <p class="muted-mini">
        These results connect probability theory to real-world data analysis.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>Convergence intuition</strong><span class="meta">What does “approaches” mean?</span></li>
          <li style="margin:.35rem 0;"><strong>Law of Large Numbers</strong><span class="meta">Why averages stabilize</span></li>
          <li style="margin:.35rem 0;"><strong>Central Limit Theorem</strong><span class="meta">Why normal appears everywhere</span></li>
          <li style="margin:.35rem 0;"><strong>Normal approximation</strong><span class="meta">Practical probability tools</span></li>
          <li style="margin:.35rem 0;"><strong>Inference bridge</strong><span class="meta">Why confidence intervals work</span></li>
          <li style="margin:.35rem 0;"><strong>Simulation logic</strong><span class="meta">Empirical verification later</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- Continue Reading -->
<section class="section" id="continue-reading-block6" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block6-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block6-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Follow the conceptual order carefully. Each lesson builds directly
      on Block 5 distributions.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/probability/lln-clt/convergence-intuition/">1. Convergence Intuition</a></h3>
      <p>What does convergence mean? Informal ideas before formal statements.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/lln-clt/convergence-intuition/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/lln-clt/law-of-large-numbers/">2. Law of Large Numbers (LLN)</a></h3>
      <p>Why sample averages converge to expected value.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/lln-clt/law-of-large-numbers/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/lln-clt/weak-vs-strong-lln/">3. Weak vs Strong LLN</a></h3>
      <p>Difference between convergence in probability and almost sure convergence.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/lln-clt/weak-vs-strong-lln/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/lln-clt/central-limit-theorem/">4. Central Limit Theorem (CLT)</a></h3>
      <p>Standardized sums converge to normal distribution.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/lln-clt/central-limit-theorem/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/lln-clt/normal-approximation/">5. Normal Approximation</a></h3>
      <p>Using CLT to approximate binomial and other distributions.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/lln-clt/normal-approximation/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/probability/lln-clt/inference-bridge/">6. Why Inference Works</a></h3>
      <p>How LLN and CLT justify confidence intervals and hypothesis testing.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/lln-clt/inference-bridge/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 6</h2>
      <ul class="bullets">
        <li>Understand convergence in probability</li>
        <li>Explain why sample averages stabilize</li>
        <li>State and interpret the Central Limit Theorem</li>
        <li>Use normal approximation correctly</li>
        <li>Understand why statistical inference is justified</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/probability/sampling-distributions/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 7 — Sampling Distributions</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_probability_lln_clt_lesson_v0";

    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block6");
      var label = document.getElementById("continue-reading-block6-label");
      var btn = document.getElementById("continue-reading-block6-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>