---
layout: default
title: Mathematical Statistics
description: The theory of estimation: statistical models, likelihood, estimator properties, Fisher information, and asymptotic results.
permalink: /mathematical-statistics/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#eef5ff; border:2px solid #3f51b5; padding:1.5rem; border-radius:10px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#1a237e; font-size:1.8rem; letter-spacing:0.5px;">
        📐 Mathematical Statistics — Theory of Estimation
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#283593; line-height:1.6;">
        This unit develops the formal theory behind statistical estimation.
        We move from statistical models to likelihood, study properties of estimators,
        and derive asymptotic results that power modern inference and machine learning.
      </p>
    </div>
  </div>
</section>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Estimation theory</span>
        <span class="badge">Likelihood</span>
        <span class="badge">Fisher information</span>
        <span class="badge">Asymptotics</span>
      </div>

      <h1>Mathematical Statistics</h1>
      <p class="lead">
        Learn how estimators are constructed, evaluated, and justified.
        Understand likelihood, efficiency, and asymptotic normality —
        the theoretical backbone of statistical inference.
      </p>

      <div class="hero-actions">
        <a class="btn" href="/probability/">Prerequisite: Probability</a>
        <a class="btn btn-outline" href="/inference/">Next: Statistical Inference</a>
      </div>

      <p class="muted-mini">
        This unit focuses strictly on estimation theory.
        Hypothesis testing and confidence intervals are developed in the Inference section.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">Suggested learning order</h2>
        <ol class="quickstart">
          <li><a href="#blocks">Statistical models</a><span class="meta">Parametric structure</span></li>
          <li><a href="#blocks">Likelihood framework</a><span class="meta">Core estimation engine</span></li>
          <li><a href="#blocks">Maximum likelihood estimation</a><span class="meta">Constructing estimators</span></li>
          <li><a href="#blocks">Estimator properties</a><span class="meta">Bias, variance, MSE</span></li>
          <li><a href="#blocks">Fisher information & efficiency</a><span class="meta">Efficiency bounds</span></li>
          <li><a href="#blocks">Asymptotic theory</a><span class="meta">Large-sample behavior</span></li>
          <li><a href="#blocks">Alternative estimation methods</a><span class="meta">Beyond MLE</span></li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section" id="blocks">
  <div class="section-head">
    <h2>Blocks (Unit Structure)</h2>
    <p>
      Mathematical Statistics is organized into seven structured blocks.
      Each block builds formally on the previous one and prepares you
      for full statistical inference.
    </p>
  </div>

  <div class="grid grid-2">

    <!-- Block 1 -->
    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/statistical-models/">Block 1 — Statistical Models</a>
      </h3>
      <p>
        Define statistical models rigorously: parametric families,
        parameter spaces, identifiability, and modeling assumptions.
        Establish the formal framework for estimation.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/statistical-models/">Open block</a>
      </div>
    </div>

    <!-- Block 2 -->
    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/likelihood-and-log-likelihood/">Block 2 — Likelihood & Log-Likelihood</a>
      </h3>
      <p>
        Develop the likelihood function, log-likelihood, score function,
        and information concepts. Understand why likelihood is central
        to estimation theory.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/likelihood-and-log-likelihood/">Open block</a>
      </div>
    </div>

    <!-- Block 3 -->
    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/maximum-likelihood-estimation/">Block 3 — Maximum Likelihood Estimation</a>
      </h3>
      <p>
        Construct estimators using likelihood equations.
        Study existence, uniqueness, invariance, and classical examples.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/maximum-likelihood-estimation/">Open block</a>
      </div>
    </div>

    <!-- Block 4 -->
    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/estimator-properties/">Block 4 — Estimator Properties</a>
      </h3>
      <p>
        Evaluate estimators using bias, variance, mean squared error,
        consistency, and efficiency. Learn how estimators are compared formally.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/estimator-properties/">Open block</a>
      </div>
    </div>

    <!-- Block 5 -->
    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/fisher-information-and-efficiency/">Block 5 — Fisher Information & Efficiency</a>
      </h3>
      <p>
        Study Fisher information, Cramér–Rao lower bound,
        and the concept of efficiency. Understand the limits of precision.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/fisher-information-and-efficiency/">Open block</a>
      </div>
    </div>

    <!-- Block 6 -->
    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/asymptotic-theory/">Block 6 — Asymptotic Theory</a>
      </h3>
      <p>
        Analyze large-sample behavior: consistency, asymptotic normality,
        Taylor expansions, Slutsky’s theorem, and the delta method.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/asymptotic-theory/">Open block</a>
      </div>
    </div>

    <!-- Block 7 -->
    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/alternative-estimation-methods/">Block 7 — Alternative Estimation Methods</a>
      </h3>
      <p>
        Explore method of moments and other estimation frameworks
        that extend beyond maximum likelihood.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/alternative-estimation-methods/">Open block</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Goal of this unit</h2>
      <ul class="bullets">
        <li>Formalize statistical models and parameters</li>
        <li>Understand likelihood as the core estimation principle</li>
        <li>Evaluate estimators using rigorous criteria</li>
        <li>Derive asymptotic results that justify inference procedures</li>
        <li>Prepare cleanly for Statistical Inference</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Prerequisite</div>
        <div class="mini-body">Probability theory (random variables, expectation, CLT).</div>
      </div>
      <div class="mini">
        <div class="mini-title">Next section</div>
        <div class="mini-body">Statistical Inference — confidence intervals and hypothesis testing.</div>
      </div>
      <div class="mini">
        <div class="mini-title">Scope</div>
        <div class="mini-body">This unit focuses on theory. Applications follow in Inference and Modeling.</div>
      </div>
    </div>
  </div>
</section>