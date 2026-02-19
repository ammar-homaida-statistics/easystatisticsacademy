---
layout: default
title: "5. Indicator Random Variables"
description: "Indicator random variables turn events into algebra. A powerful tool for counting, expectation, and simplifying complex probability problems."
permalink: /probability/expectation-variance/indicator-random-variables/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 introduces the formal definition and core expectation property.
        Classic counting examples and simulations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 4 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_expectation_variance_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/expectation-variance/indicator-random-variables/",
      label: "Lesson 5 — Indicator Random Variables",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Lesson 5</span>
        <span class="badge">Indicator</span>
        <span class="badge">Counting</span>
      </div>

      <h1>5. Indicator Random Variables</h1>
      <p class="lead">
        Indicator random variables convert events into numerical objects.
        This simple idea makes many complicated expectation problems almost trivial.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/expectation-variance/">Back to Block 4</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Key message: turn events into 0–1 variables, then use linearity.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define indicator variables,
      compute their expectation and variance, and use them to solve counting problems.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key definition</h2>
      <p style="margin:0; font-size:1.1rem;">
        For an event A, the indicator variable is:
        <strong>I_A = 1 if A occurs, 0 otherwise.</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Basic properties</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Possible values</h3>
      <p style="margin:0;">
        I_A ∈ {0,1}
      </p>
    </div>

    <div class="card">
      <h3>Expectation</h3>
      <p style="margin:0;">
        <strong>E[I_A] = P(A)</strong>
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This is the most important property: expectation of an indicator equals the probability of the event.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Variance of an indicator</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Since I_A follows a Bernoulli structure:
    </p>
    <p style="margin-top:.5rem; font-size:1.1rem;">
      <strong>Var(I_A) = P(A)(1 − P(A))</strong>
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Indicators are Bernoulli random variables.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Why indicators are powerful</h2>
    <p>
      Many counting variables can be written as sums of indicators.
    </p>
  </div>

  <div class="card">
    <p>
      Suppose we want to count how many events A₁, A₂, …, A_n occur.
      Define indicators I₁, I₂, …, I_n.
    </p>
    <p style="margin-top:.5rem;">
      Then:
      <strong>X = I₁ + I₂ + … + I_n</strong>
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key consequence</h2>
      <p style="margin:0;">
        <strong>E[X] = E[I₁] + … + E[I_n] = P(A₁) + … + P(A_n)</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Independence not required</h2>
  </div>

  <div class="card">
    <p>
      Linearity of expectation does not require independence.
      Even if the events overlap, we can still sum their expectations.
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This is why indicators are extremely powerful in combinatorics and probability.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Classic modeling pattern</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Define indicator for each object/event.</li>
      <li>Write total quantity as a sum of indicators.</li>
      <li>Apply linearity of expectation.</li>
      <li>Compute simple probabilities.</li>
    </ul>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Many seemingly difficult expected value problems reduce to this four-step pattern.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Forgetting that E[I_A] = P(A)</li>
        <li>Thinking independence is required for linearity</li>
        <li>Confusing indicators with general Bernoulli trials</li>
        <li>Not defining indicators clearly before summing</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define indicator variables formally</li>
        <li>Compute their expectation and variance</li>
        <li>Use them to simplify counting problems</li>
        <li>Be ready to combine tools in applications</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we combine expectation, variance, covariance, and indicators
        in realistic modeling mini-cases.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/expectation-variance/applications-mini-cases/">
          Next lesson: 6. Applications — Mini Cases →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/expectation-variance/correlation/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Correlation
          </a>
        </div>
      </div>
    </div>
  </div>
</section>