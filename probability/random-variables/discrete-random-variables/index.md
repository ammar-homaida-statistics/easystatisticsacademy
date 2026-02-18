---
layout: default
title: "2. Discrete Random Variables & PMF"
description: "Discrete random variables, support, probability mass function (PMF), and the core rules that make discrete distributions valid."
permalink: /probability/random-variables/discrete-random-variables/
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

<!-- ✅ Update "last visited lesson" for Probability Block 3 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_random_variables_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/random-variables/discrete-random-variables/",
      label: "Lesson 2 — Discrete Random Variables & PMF",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">Discrete</span>
        <span class="badge">PMF</span>
      </div>

      <h1>2. Discrete Random Variables &amp; PMF</h1>
      <p class="lead">
        A discrete random variable takes values in a countable set (finite or countably infinite).
        Its distribution is described by a <strong>probability mass function (PMF)</strong>, which assigns
        probability directly to each value.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/random-variables/">Back to Block 3</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Version 0: core structure first. Visuals and software examples will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define a discrete random variable, describe its
      distribution using a PMF, identify the support, and apply the basic rules (non-negativity and total mass = 1).
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>The PMF is a complete probability description of a discrete random variable.</strong>
        Once you know P(X=x) for all possible values x, you can compute any probability about X.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What “discrete” means</h2>
    <p>
      A random variable X is discrete if it can take values in a set you can list (at least in principle):
      <strong>{x₁, x₂, x₃, ...}</strong>.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Typical discrete examples</h3>
      <ul class="bullets">
        <li>Number of heads in 10 coin tosses</li>
        <li>Number of emails marked spam in a day</li>
        <li>Number of defects in a batch</li>
        <li>Number of customers arriving in an hour</li>
      </ul>
      <p class="muted-mini">
        Discrete variables often represent counts.
      </p>
    </div>

    <div class="card">
      <h3>Discrete does not always mean “small”</h3>
      <p>
        Discrete variables can take many values (even infinitely many), as long as the set is countable.
      </p>
      <ul class="bullets">
        <li>0, 1, 2, 3, ... (countably infinite)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) The support of a discrete random variable</h2>
    <p>
      The <strong>support</strong> is the set of values that X can take with positive probability.
      This is where the distribution “lives.”
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      <strong>Support(X) = { x : P(X = x) &gt; 0 }</strong>
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    In practice: identify the possible values first. Many probability mistakes come from an incorrect support.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Probability mass function (PMF)</h2>
    <p>
      The PMF assigns probability to each possible value:
    </p>
  </div>

  <div class="card">
    <p style="font-size:1.1rem; margin:0;">
      <strong>p(x) = P(X = x)</strong>
    </p>
  </div>

  <div class="grid grid-2" style="margin-top:1rem;">
    <div class="card">
      <h3>Rule 1 — Non-negativity</h3>
      <p style="margin:0;">
        <strong>p(x) ≥ 0</strong> for every x in the support.
      </p>
    </div>

    <div class="card">
      <h3>Rule 2 — Total probability equals 1</h3>
      <p style="margin:0;">
        <strong>Σ p(x) = 1</strong> (sum over all x in the support).
      </p>
    </div>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Interpretation</h2>
      <p style="margin:0;">
        A PMF is like a probability “budget.” You distribute total mass 1 across the possible values.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Computing probabilities from a PMF</h2>
    <p>
      For discrete variables, probabilities are computed by summing the PMF over the relevant values.
    </p>
  </div>

  <div class="card">
    <h3>Single value</h3>
    <p style="margin:0;"><strong>P(X = a) = p(a)</strong></p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Range of values</h3>
    <p style="margin:0;">
      <strong>P(X ∈ A) = Σ p(x)</strong> for x in A
    </p>
    <p class="muted-mini" style="margin-top:.5rem;">
      Here A is a set of values (not an event in the original sample space). The event is “X takes a value in A.”
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>At least / at most / between</h3>
    <ul class="bullets">
      <li><strong>P(X ≥ k)</strong> = Σ p(x) over x = k, k+1, ...</li>
      <li><strong>P(X ≤ k)</strong> = Σ p(x) over x = ..., k</li>
      <li><strong>P(a ≤ X ≤ b)</strong> = Σ p(x) over x = a,...,b</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) PMF vs event-based probability (connection)</h2>
    <p>
      A probability statement like <strong>P(X ≤ 2)</strong> is still an event probability:
      it refers to all outcomes whose mapped value is ≤ 2.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      <strong>{X ≤ 2}</strong> is an event in the original sample space,
      defined by the random variable mapping.
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This is how random variables convert event logic into numerical modeling.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Common traps (and how to avoid them)</h2>
    <p>
      Discrete probability is easy to do incorrectly if you lose track of the support or the summation logic.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Trap A: Forgetting to list the support</h3>
      <p>
        If you do not know what values are possible, your probabilities can silently exclude cases.
      </p>
    </div>

    <div class="card">
      <h3>Trap B: PMF values that do not sum to 1</h3>
      <p>
        Always check Σ p(x) = 1. If it fails, the model is inconsistent.
      </p>
    </div>

    <div class="card">
      <h3>Trap C: Treating PMF like a density</h3>
      <p>
        For discrete X, p(x) is a probability (mass), not an “area under a curve.”
        The continuous case is fundamentally different.
      </p>
    </div>

    <div class="card">
      <h3>Trap D: Confusing value sets with outcome sets</h3>
      <p>
        “X ∈ A” is an event in the outcome space, induced by values A.
        Keep the mapping in mind.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define a discrete random variable and its support</li>
        <li>Describe the distribution using a PMF p(x)=P(X=x)</li>
        <li>Compute probabilities by summing the PMF over values</li>
        <li>Be ready to study continuous random variables and the PDF</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we move to <strong>continuous random variables</strong>, where probabilities come from
        <em>areas</em> under a density function rather than summing masses.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/random-variables/continuous-random-variables/">
          Next lesson: 3. Continuous Random Variables &amp; PDF →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/random-variables/what-is-a-random-variable/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: What Is a Random Variable?
          </a>
        </div>
      </div>
    </div>
  </div>
</section>