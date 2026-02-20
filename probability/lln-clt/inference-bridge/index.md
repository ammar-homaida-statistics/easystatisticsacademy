---
layout: default
title: "6. Why Inference Works"
description: "How LLN and CLT justify confidence intervals and hypothesis testing: sampling distributions, standard error, and long-run guarantees."
permalink: /probability/lln-clt/inference-bridge/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 explains the logic behind statistical inference: why intervals and tests can be trusted in the long run.
        Worked examples and software demos will be added in Version 1.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_lln_clt_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/lln-clt/inference-bridge/",
      label: "Lesson 6 — Why Inference Works",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Lesson 6</span>
        <span class="badge">Inference</span>
        <span class="badge">Bridge</span>
      </div>

      <h1>6. Why Inference Works</h1>

      <p class="lead">
        Statistical inference is possible because sample summaries become stable (LLN)
        and their fluctuations become predictable (CLT). This lesson connects those ideas to
        <strong>confidence intervals</strong> and <strong>hypothesis tests</strong>.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/lln-clt/">Back to Block 6</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Inference = “estimate and test using probability guarantees about sampling.”
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to explain (in probability terms)
      why confidence intervals have a target coverage and why hypothesis tests have controlled error rates.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        Inference works because the <strong>sampling distribution</strong> of an estimator is (approximately) known.
        LLN gives consistency; CLT gives approximate normality and standard errors.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What “inference” is, in one line</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      We observe a sample and use it to learn about an unknown parameter (like \(\mu\) or \(p\))
      while quantifying uncertainty using probability.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) The sampling distribution is the engine</h2>
    <p>
      Let \(X_1,\dots,X_n\) be i.i.d. with mean \(\mu\) and variance \(\sigma^2\).
      The sample mean is:
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.05rem;">
      \[
      \overline{X}=\frac{1}{n}\sum_{i=1}^n X_i.
      \]
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Why it matters</h2>
      <p style="margin:0;">
        Inference needs the distribution of \(\overline{X}\) (or another estimator) across repeated samples.
        That distribution is called the sampling distribution.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) LLN gives consistency (stability)</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      LLN tells us:
      \[
      \overline{X} \xrightarrow[]{P} \mu.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Meaning: as \(n\) grows, \(\overline{X}\) gets close to \(\mu\) with high probability.
    This is the basic “stability” behind estimation.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) CLT gives shape + scale (predictable error)</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      CLT tells us:
      \[
      \frac{\overline{X}-\mu}{\sigma/\sqrt{n}} \xrightarrow[]{d} N(0,1).
      \]
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      So for large \(n\),
      \[
      \overline{X}\approx N\!\left(\mu,\frac{\sigma^2}{n}\right).
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This is what makes error bars and probability statements possible.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Standard error: the uncertainty unit</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      The standard deviation of \(\overline{X}\) is:
      \[
      \operatorname{SD}(\overline{X})=\frac{\sigma}{\sqrt{n}}.
      \]
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Interpretation</h2>
      <p style="margin:0;">
        \(\sigma/\sqrt{n}\) is the natural “noise level” of the sample mean.  
        Bigger \(n\) → smaller uncertainty.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Confidence intervals (coverage logic)</h2>
    <p>
      A 95% confidence interval is constructed so that, in repeated sampling,
      it contains the true parameter about 95% of the time.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      If \(\sigma\) is known and \(n\) is large:
      \[
      \mu \in \overline{X} \pm z_{0.975}\,\frac{\sigma}{\sqrt{n}}.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Where \(z_{0.975}\approx 1.96\).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>7) Hypothesis tests (error control logic)</h2>
    <p>
      A hypothesis test uses the sampling distribution to decide whether data is “too unlikely”
      under a null model.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      Example (mean test idea):
      \[
      Z=\frac{\overline{X}-\mu_0}{\sigma/\sqrt{n}}.
      \]
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <ul class="bullets">
      <li>\(\alpha\) controls Type I error: false rejection probability under \(H_0\).</li>
      <li>Power increases with \(n\): smaller standard error makes detection easier.</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>8) Why this is a “bridge” lesson</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Probability gives convergence + approximation (LLN/CLT).</li>
      <li>Statistics uses them to build estimators, intervals, and tests.</li>
      <li>Next block formalizes sampling distributions (t, chi-square, F, etc.).</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Explain inference using LLN (stability) and CLT (approximate normality)</li>
        <li>Interpret standard error as uncertainty scale</li>
        <li>Understand why CI coverage and test error control are possible</li>
        <li>Be ready for Sampling Distributions (Block 7)</li>
      </ul>
    </div>
  </div>
</section>

<!-- ✅ Next block navigation -->
<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we move to <strong>Block 7 — Sampling Distributions</strong>,
        where we study the distributions of statistics like \(\overline{X}\), \(S^2\), and test statistics.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/sampling-distributions/">
          Next block: Block 7 — Sampling Distributions →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/lln-clt/normal-approximation/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 5 — Normal Approximation
          </a>
        </div>
      </div>
    </div>
  </div>
</section>