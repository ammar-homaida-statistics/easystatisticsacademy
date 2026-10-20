---
layout: default
title: Asymptotic Theory
description: Consistency, asymptotic normality, Slutsky’s theorem, and the delta method.
permalink: /mathematical-statistics/asymptotic-theory/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#f3f6ff; border:2px solid #3f51b5; padding:1.5rem; border-radius:10px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#1a237e; font-size:1.6rem;">🚧 This Block Is Under Construction</h2>
      <p style="margin:0; color:#283593; line-height:1.6;">
        This block develops large-sample theory used throughout mathematical statistics:
        convergence, asymptotic distributions, and approximation tools.
      </p>
    </div>
  </div>
</section>

<section class="hero hero-lesson">
  <div class="hero-card hero-split">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Convergence</span>
        <span class="badge">Asymptotic normality</span>
        <span class="badge">Slutsky</span>
        <span class="badge">Delta method</span>
      </div>

      <h1>Block 6 — Asymptotic Theory</h1>

      <p class="lead">
        Learn the rigorous tools that justify approximation in inference:
        convergence, limiting distributions, and transformations.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/">Back: Mathematical Statistics</a>
        <a class="btn" href="/mathematical-statistics/alternative-estimation-methods/">Next block: Alternative Methods</a>
      </div>

      <p class="muted-mini">
        This block is the bridge between estimation theory and practical inference approximations.
      </p>

    </div>

    <div class="hero-panel">
      <div class="panel-card">

        <h2 class="panel-title">Recommended lesson order</h2>

        <ol class="quickstart">
          <li><a href="#lessons">Modes of convergence (review)</a><span class="meta">Probability tools</span></li>
          <li><a href="#lessons">Consistency of MLE (idea)</a><span class="meta">Why MLE converges</span></li>
          <li><a href="#lessons">Asymptotic normality of MLE</a><span class="meta">Main result</span></li>
          <li><a href="#lessons">Slutsky & mapping theorems</a><span class="meta">Combining limits</span></li>
          <li><a href="#lessons">Delta method</a><span class="meta">Transformations</span></li>
        </ol>

      </div>
    </div>
  </div>
</section>

<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons</h2>
    <p>“Continue reading” resumes your last visited lesson in this block.</p>
  </div>

  <div id="continue-reading-ms-b6" style="display:none; margin-top:0.75rem;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p class="muted-mini" id="continue-reading-ms-b6-label" style="margin:0 0 .75rem 0;"></p>
        <a class="btn" id="continue-reading-ms-b6-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/asymptotic-theory/modes-of-convergence-review/">
          Modes of convergence (review)
        </a>
      </h3>
      <p>Convergence in probability, distribution, almost sure; when each is used.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/asymptotic-theory/modes-of-convergence-review/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/asymptotic-theory/consistency-of-mle-idea/">
          Consistency of MLE (idea)
        </a>
      </h3>
      <p>Why maximizing likelihood tends to recover the true parameter under regularity.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/asymptotic-theory/consistency-of-mle-idea/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/asymptotic-theory/asymptotic-normality-of-mle/">
          Asymptotic normality of MLE
        </a>
      </h3>
      <p>The key approximation result behind standard errors and Wald intervals.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/asymptotic-theory/asymptotic-normality-of-mle/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/asymptotic-theory/slutsky-theorem-and-continuous-mapping/">
          Slutsky theorem and continuous mapping
        </a>
      </h3>
      <p>How limiting distributions combine and transform under smooth functions.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/asymptotic-theory/slutsky-theorem-and-continuous-mapping/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/asymptotic-theory/delta-method/">
          Delta method
        </a>
      </h3>
      <p>Approximate the distribution of transformations of estimators using Taylor expansion.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/asymptotic-theory/delta-method/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<script>
(function() {
  "use strict";
  const key="esa_continue_ms_asymptotics_last_lesson_v0";
  const root="/mathematical-statistics/asymptotic-theory/";
  const allowed={
  "/mathematical-statistics/asymptotic-theory/modes-of-convergence-review/": "Lesson 1 — Modes of Convergence",
  "/mathematical-statistics/asymptotic-theory/consistency-of-mle-idea/": "Lesson 2 — Consistency of MLE",
  "/mathematical-statistics/asymptotic-theory/asymptotic-normality-of-mle/": "Lesson 3 — Asymptotic Normality of MLE",
  "/mathematical-statistics/asymptotic-theory/slutsky-theorem-and-continuous-mapping/": "Lesson 4 — Slutsky Theorem",
  "/mathematical-statistics/asymptotic-theory/delta-method/": "Lesson 5 — Delta Method"
};
  const wrap=document.getElementById("continue-reading-ms-b6");
  const label=document.getElementById("continue-reading-ms-b6-label");
  const link=document.getElementById("continue-reading-ms-b6-btn");
  try {
    localStorage.setItem("esa_continue_ms_last_block_v0",
      JSON.stringify({label:"Block 6 — Asymptotic Theory",url:root}));
  } catch (_) { /* Progress is optional. */ }
  if (!wrap||!label||!link) return;
  try {
    const raw=localStorage.getItem(key);
    if(!raw) return;
    const value=JSON.parse(raw);
    if(!value||typeof value!=="object"||Array.isArray(value)) return;
    if(typeof value.url!=="string"||!Object.prototype.hasOwnProperty.call(allowed,value.url)) return;
    if(typeof value.label!=="string"||value.label!==allowed[value.url]) return;
    if(typeof value.ts!=="number"||!Number.isFinite(value.ts)||value.ts<=0
       ||value.ts>Date.now()+86400000) return;
    label.textContent="You last visited: "+value.label;
    link.setAttribute("href",value.url);
    wrap.style.display="block";
  } catch (_) { /* Untrusted storage is ignored. */ }
})();
</script>
