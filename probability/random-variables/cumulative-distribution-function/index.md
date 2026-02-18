---
layout: default
title: "4. Cumulative Distribution Function (CDF)"
description: "The cumulative distribution function (CDF) unifies discrete and continuous random variables and provides a complete description of a distribution."
permalink: /probability/random-variables/cumulative-distribution-function/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the structure and the correct conceptual flow.
        Numerical examples, graphs, and software demonstrations will be added later without changing the lesson order.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 3 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_random_variables_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/random-variables/cumulative-distribution-function/",
      label: "Lesson 4 — Cumulative Distribution Function (CDF)",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">CDF</span>
        <span class="badge">Unifying concept</span>
      </div>

      <h1>4. Cumulative Distribution Function (CDF)</h1>
      <p class="lead">
        The cumulative distribution function (CDF) provides a complete description of a random variable.
        It works for both discrete and continuous cases and connects probability to inequality statements.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/random-variables/">Back to Block 3</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        The CDF answers the most common probability question: “What is the probability that X is less than or equal to x?”
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define the CDF, interpret its properties,
      and use it to compute probabilities for both discrete and continuous random variables.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key definition</h2>
      <p style="margin:0;">
        For any random variable X, the cumulative distribution function is:
        <strong>F(x) = P(X ≤ x)</strong>.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What the CDF represents</h2>
    <p>
      The CDF accumulates probability from negative infinity up to x.
      It tells you how much probability mass lies to the left of x.
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>F(x) increases as x increases.</li>
      <li>F(x) approaches 0 as x → −∞.</li>
      <li>F(x) approaches 1 as x → +∞.</li>
    </ul>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Interpretation</h2>
      <p style="margin:0;">
        F(x) is the proportion of probability mass to the left of x.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) CDF in the discrete case</h2>
    <p>
      For a discrete random variable, the CDF is a step function.
    </p>
  </div>

  <div class="card">
    <p>
      F(x) = Σ P(X = k) for all k ≤ x.
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Important property</h3>
    <p>
      The CDF jumps at each possible value of X.
      The size of the jump equals the probability mass at that point.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) CDF in the continuous case</h2>
    <p>
      For a continuous random variable with density f(x):
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      <strong>F(x) = ∫₋∞ˣ f(t) dt</strong>
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Connection to PDF</h3>
    <p>
      If F(x) is differentiable, then:
    </p>
    <p style="margin:0;"><strong>f(x) = F′(x)</strong></p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Probability using CDF</h3>
    <p style="margin:0;">
      P(a ≤ X ≤ b) = F(b) − F(a)
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Fundamental properties of any CDF</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <ul class="bullets">
        <li>0 ≤ F(x) ≤ 1</li>
        <li>F(x) is non-decreasing</li>
        <li>Right-continuous</li>
      </ul>
    </div>

    <div class="card">
      <ul class="bullets">
        <li>lim x→−∞ F(x) = 0</li>
        <li>lim x→+∞ F(x) = 1</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Why the CDF is powerful</h2>
    <p>
      The CDF completely determines the distribution.
      Once you know F(x), you can compute any probability involving inequalities.
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Handles both discrete and continuous cases.</li>
      <li>Works for mixed distributions.</li>
      <li>Foundation for quantiles and inverse transform sampling.</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Confusing CDF with PDF/PMF</li>
        <li>Forgetting CDF is non-decreasing</li>
        <li>Ignoring right-continuity in discrete case</li>
        <li>Using F(b) − F(a) incorrectly when variables are discrete</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define and interpret F(x) = P(X ≤ x)</li>
        <li>Connect CDF to PMF and PDF</li>
        <li>Compute probabilities using F(b) − F(a)</li>
        <li>Prepare for expectation and variance next</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we define <strong>expectation</strong>: the long-run average value of a random variable under its distribution.
      </p>

      <!-- ✅ FIXED: matches your folder name "expectation" -->
      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/random-variables/expectation/">
          Next lesson: 5. Expectation →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/random-variables/continuous-random-variables/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Continuous Random Variables & PDF
          </a>
        </div>
      </div>
    </div>
  </div>
</section>