---
layout: default
title: "12. Lognormal Distribution"
description: "The Lognormal distribution: modeling positive skewed data, exponential growth, and multiplicative processes derived from the Normal distribution."
permalink: /probability/distributions/lognormal-distribution/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 establishes the formal definition and key properties.
        Visual intuition, real-world examples, and software demonstrations will be added next.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/distributions/lognormal-distribution/",
      label: "Lesson 12 — Lognormal Distribution",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 12</span>
        <span class="badge">Continuous</span>
        <span class="badge">Positive Support</span>
      </div>

      <h1>12. Lognormal Distribution</h1>

      <p class="lead">
        A random variable is lognormally distributed if its logarithm is normally distributed.
        The lognormal distribution models strictly positive and right-skewed data,
        especially in multiplicative growth processes.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        If $$\ln(X)$$ is Normal, then $$X$$ is Lognormal.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define the Lognormal distribution using a Normal
      transformation, write its PDF, and interpret how parameters control location and skewness.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Lognormal = exponentiated Normal:</strong>
        if $$Y\sim \mathcal{N}(\mu,\sigma^2)$$ then $$X=\exp(Y)$$ is Lognormal.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      A random variable $$X$$ is <strong>Lognormal</strong> if:
      $$
      Y=\ln(X)\sim \mathcal{N}(\mu,\sigma^2).
      $$
    </p>

    <p class="muted-mini" style="margin-top:.75rem;">
      Notation (common): $$X\sim \mathrm{Lognormal}(\mu,\sigma^2).$$
      Here $$\mu$$ and $$\sigma^2$$ are parameters of $$\ln(X)$$ (not of $$X$$ directly).
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Support and density (PDF)</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Support:
      $$
      x>0.
      $$
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0; font-size:1.1rem;">
      $$
      f(x)=
      \frac{1}{x\,\sigma\sqrt{2\pi}}
      \exp\!\left(-\frac{(\ln x-\mu)^2}{2\sigma^2}\right),
      \quad x>0.
      $$
    </p>

    <p class="muted-mini" style="margin-top:.75rem;">
      The extra $$1/x$$ factor comes from the change-of-variables when moving from $$Y=\ln(X)$$ to $$X=\exp(Y)$$.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Key properties</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Median</h3>
      <p style="margin:0;">
        $$
        \mathrm{Median}(X)=e^{\mu}.
        $$
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Because $$\ln(X)$$ is symmetric around $$\mu$$.
      </p>
    </div>

    <div class="card">
      <h3>Mean</h3>
      <p style="margin:0;">
        $$
        \mathbb{E}[X]=e^{\mu+\sigma^2/2}.
        $$
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Mean is larger than the median when $$\sigma>0$$ (right skew).
      </p>
    </div>

    <div class="card">
      <h3>Variance</h3>
      <p style="margin:0;">
        $$
        \mathrm{Var}(X)=\left(e^{\sigma^2}-1\right)e^{2\mu+\sigma^2}.
        $$
      </p>
    </div>

    <div class="card">
      <h3>Interpretation of parameters</h3>
      <ul class="bullets">
        <li>$$\mu$$ controls the typical scale (median).</li>
        <li>$$\sigma$$ controls spread and skewness.</li>
        <li>Larger $$\sigma$$ ⇒ heavier right tail.</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Shape and intuition</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Strictly positive (no mass at 0 or below).</li>
      <li>Right-skewed (long right tail).</li>
      <li>Often fits data generated by <strong>multiplicative</strong> effects.</li>
      <li>Typical relationship: $$\mathbb{E}[X]>\mathrm{Median}(X).$$</li>
    </ul>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Modeling meaning</h2>
      <p style="margin:0;">
        If a quantity grows by multiplying random factors (compound growth),
        its logarithm becomes a sum of random terms — which often looks Normal.
        Then the original quantity becomes Lognormal.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Normal vs Lognormal (quick comparison)</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Normal</h3>
      <ul class="bullets">
        <li>Support: $$(-\infty,\infty)$$</li>
        <li>Symmetric</li>
        <li>Additive noise model</li>
      </ul>
    </div>

    <div class="card">
      <h3>Lognormal</h3>
      <ul class="bullets">
        <li>Support: $$(0,\infty)$$</li>
        <li>Right-skewed</li>
        <li>Multiplicative growth model</li>
      </ul>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This is why a log-transform is often used to “normalize” skewed positive data.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define Lognormal via $$\ln(X)\sim \mathcal{N}(\mu,\sigma^2)$$</li>
        <li>Use the Lognormal PDF correctly</li>
        <li>Compute mean, variance, and median</li>
        <li>Recognize when multiplicative processes suggest a Lognormal model</li>
      </ul>
    </div>
  </div>
</section>

<!-- ✅ Final navigation for Block 5 (no next lesson) -->
<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        This is the last lesson in Block 5 (Version 0).
        Next, we move forward to the next Probability block in the unit structure.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/">
          Back to Probability home →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/distributions/normal-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 11 — Normal Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>