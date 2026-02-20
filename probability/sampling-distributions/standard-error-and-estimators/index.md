---
layout: default
title: "2. Standard Error & Estimators"
description: "Estimators as random variables: bias, variance, consistency intuition, and the standard error as the scale of sampling uncertainty."
permalink: /probability/sampling-distributions/standard-error-and-estimators/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 defines the estimator framework (bias/variance/SE) and locks the conceptual order.
        Worked examples, simulations, and software workflows will be added in Version 1.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Block 7 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_sampling_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/sampling-distributions/standard-error-and-estimators/",
      label: "Lesson 2 — Standard Error & Estimators",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">Estimators</span>
        <span class="badge">Standard Error</span>
      </div>

      <h1>2. Standard Error &amp; Estimators</h1>

      <p class="lead">
        An <strong>estimator</strong> is a statistic used to estimate an unknown parameter.
        Because it is computed from a random sample, it is itself a random variable and has a
        <strong>sampling distribution</strong>. The <strong>standard error</strong> measures its typical sampling fluctuation.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/sampling-distributions/">Back to Block 7</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Inference is built from two ingredients: an estimator + its standard error.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define an estimator and estimate,
      compute bias and variance (conceptually), interpret standard error, and connect these ideas
      to precision and sample size.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        Estimator quality is about the sampling distribution:
        <strong>center</strong> (bias) and <strong>spread</strong> (variance / standard error).
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Parameter, estimator, estimate</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Parameter</h3>
      <p style="margin:0;">
        A fixed but unknown quantity describing the population, e.g. \(\mu\), \(\sigma^2\), \(p\).
      </p>
    </div>

    <div class="card">
      <h3>Estimator vs estimate</h3>
      <p style="margin:0;">
        The estimator is a random variable \(T\).  
        The estimate is the realized value \(t\) from your sample.
      </p>
    </div>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      Example:
      \[
      \overline{X}=\frac{1}{n}\sum_{i=1}^n X_i
      \]
      is an <strong>estimator</strong> of \(\mu\). The number you compute from data is the <strong>estimate</strong>.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Bias: does it hit the target on average?</h2>
    <p>
      Bias measures systematic error in the center of the sampling distribution.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      The bias of an estimator \(T\) for parameter \(\theta\) is
      \[
      \operatorname{Bias}(T)=\mathbb{E}[T]-\theta.
      \]
    </p>
  </div>

  <div class="grid grid-2" style="margin-top:1rem;">
    <div class="card">
      <h3>Unbiased</h3>
      <p style="margin:0;">
        \(\mathbb{E}[T]=\theta\)  ⇒  \(\operatorname{Bias}(T)=0\).
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Centered correctly in repeated sampling.
      </p>
    </div>

    <div class="card">
      <h3>Biased</h3>
      <p style="margin:0;">
        \(\mathbb{E}[T]\neq \theta\) ⇒ systematic shift.
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Bias can be small and still acceptable if variance is much smaller.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Variance and standard error: how noisy is the estimator?</h2>
    <p>
      Variance measures spread of the sampling distribution. Standard error is its standard deviation.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      \[
      \operatorname{Var}(T)=\mathbb{E}\!\left[(T-\mathbb{E}[T])^2\right],
      \qquad
      \operatorname{SE}(T)=\sqrt{\operatorname{Var}(T)}.
      \]
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Interpretation</h2>
      <p style="margin:0;">
        Standard error is the “typical sampling error” scale.
        Smaller SE means more precise estimates.
      </p>
    </div>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Key example (sample mean)</h3>
    <p style="margin:0;">
      If \(X_1,\dots,X_n\) are i.i.d. with variance \(\sigma^2\):
      \[
      \operatorname{Var}(\overline{X})=\frac{\sigma^2}{n},
      \qquad
      \operatorname{SE}(\overline{X})=\frac{\sigma}{\sqrt{n}}.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This is why doubling the sample size does not halve uncertainty; it reduces it by a factor of \(\sqrt{2}\).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) MSE: one number combining bias and variance</h2>
    <p>
      Mean squared error summarizes overall accuracy around the true parameter.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      \[
      \operatorname{MSE}(T)=\mathbb{E}\!\left[(T-\theta)^2\right]
      =\operatorname{Var}(T)+\operatorname{Bias}(T)^2.
      \]
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Bias–variance tradeoff (preview)</h2>
      <p style="margin:0;">
        A slightly biased estimator can be better if it has much smaller variance.
        This idea appears again in shrinkage methods and regularization.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Consistency (intuitive definition)</h2>
    <p>
      Consistency means the estimator converges to the true parameter as sample size increases.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      An estimator \(T_n\) is <strong>consistent</strong> for \(\theta\) if
      \[
      T_n \xrightarrow[]{P} \theta \quad \text{as } n\to\infty.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    LLN often provides consistency (e.g., \(\overline{X}\) for \(\mu\)).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Why SE is everywhere in inference</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Confidence intervals are typically: <strong>estimate ± critical value × SE</strong>.</li>
      <li>Test statistics are typically: <strong>(estimate − null) / SE</strong>.</li>
      <li>As \(n\) increases, SE usually decreases, making inference sharper.</li>
    </ul>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      Generic form:
      \[
      \frac{T-\theta}{\operatorname{SE}(T)} \approx \text{(reference distribution)}.
      \]
    </p>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Distinguish parameter, estimator, and estimate</li>
        <li>Define and interpret bias, variance, and standard error</li>
        <li>Use \(\operatorname{MSE}=\operatorname{Var}+\operatorname{Bias}^2\) as a quality summary</li>
        <li>Understand how sample size affects precision through SE</li>
        <li>Prepare to derive the sampling distribution of \(\overline{X}\) under Normal models</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we standardize estimators and build confidence intervals using the
        <strong>z-statistic</strong> under Normal assumptions.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/sampling-distributions/z-statistic-and-ci/">
          Next lesson: 3. z-Statistic &amp; Confidence Intervals →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/sampling-distributions/what-is-a-sampling-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1 — What Is a Sampling Distribution?
          </a>
        </div>
      </div>
    </div>
  </div>
</section>