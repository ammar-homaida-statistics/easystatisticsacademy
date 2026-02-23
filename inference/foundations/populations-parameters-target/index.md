---
layout: default
title: "2. Populations, Parameters, and the Target of Estimation"
description: "Define populations and parameters precisely. Learn why parameters are fixed-but-unknown, how targets are defined, and how scope affects what you can claim."
permalink: /inference/foundations/populations-parameters-target/
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

<!-- ✅ Update "last visited lesson" for Inference Block 1 -->
<script>
  (function () {
    var KEY = "esa_continue_inference_foundations_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/foundations/populations-parameters-target/",
      label: "Lesson 2 — Populations, Parameters, and the Target of Estimation",
      ts: Date.now()
    }));

    // (Optional but consistent) also refresh "last visited block" for Inference home
    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/foundations/",
      label: "Block 1 — Inference Foundations",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">Parameters</span>
        <span class="badge">Scope</span>
      </div>

      <h1>2. Populations, Parameters, and the Target of Estimation</h1>
      <p class="lead">
        Inference starts by defining the target correctly.
        This lesson clarifies what a <strong>population</strong> is, what a <strong>parameter</strong> is,
        and why “unknown” does not mean “random”.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/foundations/">Back to Block 1</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
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
      By the end of this lesson, you should be able to define the population you are studying, specify a parameter as the
      target quantity, and explain the difference between a <strong>fixed-but-unknown parameter</strong> and a
      <strong>random statistic</strong>.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>A parameter belongs to the population.</strong> It is fixed (in the classical framework) even if we do not know it.
        Randomness enters through the sampling process, not through the parameter itself.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What is a population?</h2>
    <p>
      A population is the full set of units you want to learn about. Inference is impossible to interpret unless the population
      is defined clearly.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Examples of populations</h3>
      <ul class="bullets">
        <li>All undergraduate students at a specific university (2026)</li>
        <li>All customers who purchased in the last 30 days</li>
        <li>All patients meeting inclusion criteria in a clinic</li>
        <li>All manufactured items produced this week</li>
      </ul>
      <p class="muted-mini">
        Population definition always includes <strong>who</strong>, <strong>where</strong>, and <strong>when</strong>.
      </p>
    </div>

    <div class="card">
      <h3>Common mistake</h3>
      <p>
        People often say “the population is everyone” when they really mean a narrower group.
        If the population is not defined, your conclusions have no clear scope.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) What is a parameter?</h2>
    <p>
      A parameter is a numerical summary of the population distribution (or population relationship).
      It is the target you want to estimate.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Typical parameters</h3>
      <ul class="bullets">
        <li>Population mean: \(\mu\)</li>
        <li>Population proportion: \(p\)</li>
        <li>Population variance: \(\sigma^2\)</li>
        <li>Population correlation: \(\rho\)</li>
        <li>Regression slope(s): \(\beta\)</li>
      </ul>
    </div>

    <div class="card">
      <h3>Parameter ≠ dataset summary</h3>
      <p style="margin:0;">
        The parameter is defined even if you do not collect any data.
        Data are used to estimate it, but the parameter is not “created” by the sample.
      </p>
    </div>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Interpretation</h2>
      <p style="margin:0;">
        A parameter is a property of a conceptual data-generating process for the population.
        If you change the population definition, you change the parameter you are talking about.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Why parameters are “fixed but unknown”</h2>
    <p>
      In the standard (frequentist) inference framework, parameters are not random variables.
      The data are random because the sample you observe could have been different.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Fixed but unknown</h3>
      <p style="margin:0;">
        \(\mu\), \(p\), \(\sigma^2\), \(\beta\) are treated as fixed constants that describe the population.
        We don’t know them, so we estimate them.
      </p>
    </div>

    <div class="card">
      <h3>Random because of sampling</h3>
      <p style="margin:0;">
        \(\bar X\), \(\hat p\), \(S^2\), \(\hat\beta\) vary from sample to sample.
        Therefore they have <strong>sampling distributions</strong>.
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    The sentence “the mean is random” is usually incorrect in this framework; the correct statement is “the sample mean is random”.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) The target must be measurable and meaningful</h2>
    <p>
      Before estimating anything, you need a target that is:
      (1) well-defined, (2) measurable, and (3) relevant to the real question.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Well-defined target</h3>
      <ul class="bullets">
        <li>Specify the population</li>
        <li>Specify the variable</li>
        <li>Specify the summary (mean? proportion? difference?)</li>
      </ul>
    </div>

    <div class="card">
      <h3>Meaningful target</h3>
      <p>
        A statistically estimable parameter can still be meaningless if it does not match the real decision/problem.
        Target definition is a scientific step, not only a mathematical step.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Scope: what you can claim depends on how you sampled</h2>
    <p>
      Even if your estimator is perfect, you can only generalize to the population your sampling design supports.
      Inference is not a “free upgrade” from sample to world.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Good scope (typical)</h3>
      <p>
        If your sample is a credible random sample from a known population, you can generalize within that population
        (with quantified uncertainty).
      </p>
    </div>

    <div class="card">
      <h3>Weak scope (common)</h3>
      <p>
        Convenience samples (volunteers, online forms, “whoever answered”) often do not support broad population claims,
        even if the sample size is large.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Common traps (and how to avoid them)</h2>
    <p>
      Errors here are extremely costly because everything later (SE, CI, tests) depends on the target being correct.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Trap A: Undefined population</h3>
      <p>
        If you cannot define who/where/when, you cannot define the parameter you claim to estimate.
      </p>
    </div>

    <div class="card">
      <h3>Trap B: Treating a parameter as random</h3>
      <p>
        In frequentist inference, parameters are fixed. The randomness belongs to the estimator/statistic.
      </p>
    </div>

    <div class="card">
      <h3>Trap C: Changing the target after seeing data</h3>
      <p>
        Decide the target first. “Moving the goalposts” after looking at results undermines interpretation.
      </p>
    </div>

    <div class="card">
      <h3>Trap D: Over-generalizing beyond the sampling frame</h3>
      <p>
        You cannot claim “all people” if your sampling frame was “students in one city”.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define a population precisely (who/where/when)</li>
        <li>Define a parameter as the target population quantity</li>
        <li>Explain “fixed but unknown” parameters vs random statistics</li>
        <li>Understand how sampling design limits generalization</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we formalize the key shift of inference:
        <strong>statistics are random variables</strong> with distributions.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/foundations/statistics-as-random-variables/">
          Next lesson: 3. Statistics as Random Variables →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/foundations/what-is-statistical-inference/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: What Is Statistical Inference?
          </a>
        </div>
      </div>
    </div>

  </div>
</section>