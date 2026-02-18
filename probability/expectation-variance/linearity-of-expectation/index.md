---
layout: default
title: "1. Linearity of Expectation"
description: "The most important rule for expectations: how expectation behaves under sums and transformations, and why independence is not needed."
permalink: /probability/expectation-variance/linearity-of-expectation/
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

<!-- ✅ Update "last visited lesson" for Probability Block 4 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_expectation_variance_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/expectation-variance/linearity-of-expectation/",
      label: "Lesson 1 — Linearity of Expectation",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Lesson 1</span>
        <span class="badge">Expectation</span>
        <span class="badge">Linearity</span>
      </div>

      <h1>1. Linearity of Expectation</h1>
      <p class="lead">
        Linearity of expectation is the single most useful rule in probability.
        It lets you compute expected values of complicated random quantities by breaking them into simpler parts —
        and it works <strong>without independence</strong>.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/expectation-variance/">Back to Block 4</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Key message: expectation is additive, even when variables are dependent.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to apply linearity to compute expectations of sums and
      transformed variables, and know exactly what assumptions are needed (and not needed).
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Linearity of expectation:</strong> you can “pull apart” sums and constants inside expectation.
        Independence is <strong>not</strong> required.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) The two core linearity rules</h2>
    <p>
      These rules are true for any random variables with finite expectations.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Rule A — Constants pull out</h3>
      <p style="margin:0;">
        For constants a and b:
        <strong>E[aX + b] = aE[X] + b</strong>
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Shifting by b moves the mean by b. Scaling by a scales the mean by a.
      </p>
    </div>

    <div class="card">
      <h3>Rule B — Expectation of a sum</h3>
      <p style="margin:0;">
        For any X and Y:
        <strong>E[X + Y] = E[X] + E[Y]</strong>
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        This holds even if X and Y are dependent.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) General form (many variables)</h2>
    <p>
      Linearity extends to any finite sum.
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      <strong>E\Big[\sum_{i=1}^n X_i\Big] = \sum_{i=1}^n E[X_i]</strong>
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Why this matters</h2>
      <p style="margin:0;">
        Many “expected number of …” questions are solved by turning the quantity into a sum,
        then applying this rule.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) What assumptions are needed?</h2>
    <p>
      This is where many learners make mistakes.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Independence is NOT required</h3>
      <p>
        Dependence affects variance and covariance, but not the additivity of expectation.
      </p>
      <ul class="bullets">
        <li>E[X+Y] always equals E[X]+E[Y] (when expectations exist).</li>
        <li>Even if X and Y “move together”.</li>
      </ul>
    </div>

    <div class="card">
      <h3>What you DO need</h3>
      <p>
        You need the expectations to exist (finite).
      </p>
      <ul class="bullets">
        <li>For most introductory distributions, this is satisfied.</li>
        <li>Edge cases exist (heavy tails), but are rare in Version 0.</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) How to use linearity (problem-solving pattern)</h2>
    <p>
      When asked to compute an expectation:
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Rewrite the random quantity as a sum of simpler pieces.</li>
      <li>Pull constants out of expectation.</li>
      <li>Split the expectation into parts.</li>
      <li>Compute each part using known means or definitions.</li>
    </ul>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Next lesson: variance does not behave this cleanly — and that’s why covariance exists.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Thinking you need independence to use E[X+Y]=E[X]+E[Y]</li>
        <li>Confusing E[XY] with E[X]E[Y] (that requires independence)</li>
        <li>Forgetting constants: E[aX+b]=aE[X]+b</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Use E[aX+b]=aE[X]+b correctly</li>
        <li>Use E[X+Y]=E[X]+E[Y] correctly (no independence needed)</li>
        <li>Apply linearity to sums of many variables</li>
        <li>Be ready for variance rules and covariance</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we study how variance behaves under transformations and sums,
        and why dependence introduces an extra covariance term.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/expectation-variance/variance-rules-and-sums/">
          Next lesson: 2. Variance Rules &amp; Sums of Variables →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/random-variables/variance-and-standard-deviation/" style="color:#1a73e8; text-decoration:underline;">
            Block 3 — Lesson 6: Variance &amp; Standard Deviation
          </a>
        </div>
      </div>
    </div>
  </div>
</section>