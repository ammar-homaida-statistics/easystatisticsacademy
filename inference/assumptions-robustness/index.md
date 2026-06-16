---
layout: default
title: Block 7 — Assumptions & Robustness
description: Learn what can break inference and how to be robust: assumptions vs design, diagnostics, outliers, bootstrap methods, and sensitivity analysis.
permalink: /inference/assumptions-robustness/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_inference_last_block_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/assumptions-robustness/",
    label: "Block 7 — Assumptions & Robustness",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card hero-split">

    <!-- LEFT -->

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Inference</span>
        <span class="badge">Block 7</span>
        <span class="badge">Assumptions</span>
        <span class="badge">Robustness</span>
      </div>

      <h1>Block 7 — Assumptions & Robustness</h1>

      <p class="lead">
        Statistical methods are only as trustworthy as the assumptions behind them.
      </p>

      <p class="lead">
        This block develops the robustness mindset:
        understanding what assumptions inference relies on,
        diagnosing potential violations,
        and choosing appropriate alternatives when standard methods become unreliable.
      </p>

      <p class="muted-mini">
        10 lessons • Validity and diagnostics • Builds on Interpretation & Reporting • Completes Statistical Inference
      </p>

      <div class="hero-actions">

        <a class="btn" href="#lessons">
          Open Lessons
        </a>

        <a class="btn btn-outline" href="/inference/">
          Back to Statistical Inference
        </a>

      </div>

      <div class="hero-highlight">

        <div class="hero-highlight-icon">
          🛡️
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            Statistical procedures often work well when assumptions are approximately true,
            but can fail when assumptions are severely violated.
            Knowing how to diagnose problems and evaluate robustness is essential for trustworthy inference.
          </p>

        </div>

      </div>

    </div>

    <!-- RIGHT -->

    <div class="hero-panel">

      <div class="panel-card">

        <h2 class="panel-title">Block overview</h2>

        <div class="mini">
          <div class="mini-title">Lessons</div>
          <div class="mini-body">10 structured lessons</div>
        </div>

        <div class="mini">
          <div class="mini-title">Level</div>
          <div class="mini-body">Inference diagnostics and validation</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Evaluate validity and robustness of conclusions
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Final outcome</div>
          <div class="mini-body">
            Complete Statistical Inference toolkit
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-inference-robustness"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-inference-robustness-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-inference-robustness-btn"
        href="#"
      >
        Continue
      </a>

    </div>

  </div>

</section>

<!-- LESSONS -->

<section class="section" id="lessons">

  <div class="section-head">

    <h2>Lessons</h2>

    <p>
      These lessons develop the practical skills needed
      to assess assumptions,
      diagnose problems,
      and determine whether conclusions remain trustworthy.
    </p>

  </div>

  <div class="grid grid-2">

    <!-- LESSON 1 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/assumptions-robustness/assumptions-vs-robustness-mindset/">
          Assumptions vs Robustness: The Mindset
        </a>
      </h3>

      <p>
        Learn why assumptions exist,
        what robustness means,
        and how statisticians think about imperfect models.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Robustness</span>
        <span class="pill">Assumptions</span>
        <span class="pill">Mindset</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/assumptions-robustness/assumptions-vs-robustness-mindset/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 2 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/assumptions-robustness/model-assumptions-vs-design-assumptions/">
          Model Assumptions vs Design Assumptions
        </a>
      </h3>

      <p>
        Distinguish assumptions about data collection
        from assumptions about probability models and distributions.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Design</span>
        <span class="pill">Models</span>
        <span class="pill">Validity</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/assumptions-robustness/model-assumptions-vs-design-assumptions/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 3 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/assumptions-robustness/checking-normality-what-and-why/">
          Checking Normality: What and Why
        </a>
      </h3>

      <p>
        Understand what normality assumptions refer to
        and when departures from normality matter.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Normality</span>
        <span class="pill">Diagnostics</span>
        <span class="pill">Assumptions</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/assumptions-robustness/checking-normality-what-and-why/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 4 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/assumptions-robustness/independence-and-dependence/">
          Independence and Dependence
        </a>
      </h3>

      <p>
        Learn how dependence affects standard errors,
        confidence intervals,
        and hypothesis tests.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Independence</span>
        <span class="pill">Dependence</span>
        <span class="pill">Design</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/assumptions-robustness/independence-and-dependence/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 5 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/assumptions-robustness/heteroscedasticity-variance-issues/">
          Heteroscedasticity and Variance Issues
        </a>
      </h3>

      <p>
        Explore unequal variance patterns,
        their impact on inference,
        and the logic of robust standard errors.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Variance</span>
        <span class="pill">Heteroscedasticity</span>
        <span class="pill">Robust SE</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/assumptions-robustness/heteroscedasticity-variance-issues/"
      >
        Open lesson
      </a>

    </div>

<!-- LESSON 6 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/assumptions-robustness/outliers-and-influence/">
          Outliers and Influence
        </a>
      </h3>

      <p>
        Distinguish outliers,
        leverage points,
        and influential observations that can strongly affect conclusions.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Outliers</span>
        <span class="pill">Influence</span>
        <span class="pill">Diagnostics</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/assumptions-robustness/outliers-and-influence/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 7 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/assumptions-robustness/robust-alternatives-nonparametric/">
          Robust Alternatives and Nonparametric Thinking
        </a>
      </h3>

      <p>
        Learn alternative approaches that remain useful
        when standard parametric assumptions are questionable.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Nonparametric</span>
        <span class="pill">Robust Methods</span>
        <span class="pill">Alternatives</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/assumptions-robustness/robust-alternatives-nonparametric/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 8 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/assumptions-robustness/bootstrap-as-robust-tool/">
          Bootstrap as a Robust Tool
        </a>
      </h3>

      <p>
        Use resampling techniques to estimate uncertainty
        when analytical formulas become unreliable.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Bootstrap</span>
        <span class="pill">Resampling</span>
        <span class="pill">Uncertainty</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/assumptions-robustness/bootstrap-as-robust-tool/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 9 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/assumptions-robustness/sensitivity-analysis-and-specification/">
          Sensitivity Analysis and Specification
        </a>
      </h3>

      <p>
        Evaluate whether conclusions remain stable
        when reasonable modeling choices are changed.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Sensitivity</span>
        <span class="pill">Specification</span>
        <span class="pill">Robustness</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/assumptions-robustness/sensitivity-analysis-and-specification/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 10 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/assumptions-robustness/reporting-assumptions-and-limitations/">
          Reporting Assumptions and Limitations
        </a>
      </h3>

      <p>
        Learn how to document assumptions,
        diagnostics,
        robustness checks,
        and limitations transparently.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Reporting</span>
        <span class="pill">Limitations</span>
        <span class="pill">Transparency</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/assumptions-robustness/reporting-assumptions-and-limitations/"
      >
        Open lesson
      </a>

    </div>

  </div>

</section>

<!-- BLOCK MAP -->

<section class="section section-slim">

  <div class="callout">

    <div class="callout-copy">

      <h2>How this block fits into inference</h2>

      <p>
        Statistical inference depends on assumptions,
        but assumptions are rarely perfectly true.
        This block teaches how to evaluate validity,
        diagnose potential problems,
        and determine whether conclusions remain trustworthy under reasonable changes.
      </p>

      <div class="table-wrap">

        <table>

          <thead>

            <tr>
              <th>Concept</th>
              <th>Why it matters later</th>
            </tr>

          </thead>

          <tbody>

            <tr>
              <td>Design Assumptions</td>
              <td>Support causal and population-level conclusions</td>
            </tr>

            <tr>
              <td>Distributional Assumptions</td>
              <td>Justify standard inferential procedures</td>
            </tr>

            <tr>
              <td>Diagnostics</td>
              <td>Identify when assumptions may be violated</td>
            </tr>

            <tr>
              <td>Bootstrap & Robust Methods</td>
              <td>Provide alternatives when formulas become fragile</td>
            </tr>

            <tr>
              <td>Sensitivity Analysis</td>
              <td>Evaluates how stable conclusions remain</td>
            </tr>

          </tbody>

        </table>

      </div>

    </div>

  </div>

</section>

<!-- GOALS -->

<section class="section section-slim">

  <div class="callout">

    <div class="callout-copy">

      <h2>Goal of this block</h2>

      <ul class="bullets">

        <li>Identify the assumptions behind common inferential methods</li>

        <li>Distinguish design assumptions from model assumptions</li>

        <li>Evaluate normality, independence, and variance conditions appropriately</li>

        <li>Recognize the effects of outliers and influential observations</li>

        <li>Apply robust and nonparametric alternatives when needed</li>

        <li>Understand bootstrap methods as a flexible inferential tool</li>

        <li>Perform sensitivity analyses to assess conclusion stability</li>

        <li>Report assumptions, diagnostics, and limitations transparently</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next step</div>

        <div class="mini-body">
          Return to <strong>Statistical Inference</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          Statistical conclusions are strongest when they remain valid under reasonable departures from assumptions.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Completion</div>

        <div class="mini-body">
          This block completes the Statistical Inference pathway by focusing on validity, robustness, and trustworthy conclusions.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/inference/interpretation-reporting/">
      ← Previous Block: Interpretation & Reporting
    </a>

    <a class="btn" href="/inference/">
      Return to Statistical Inference →
    </a>

  </div>

</section>

<!-- CONTINUE READING SCRIPT -->

<script>
(function () {

  try {

    const KEY =
      "esa_continue_inference_assumptions_robustness_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    if (!data || !data.url || !data.label) return;

    const wrap =
      document.getElementById(
        "continue-reading-inference-robustness"
      );

    const label =
      document.getElementById(
        "continue-reading-inference-robustness-label"
      );

    const btn =
      document.getElementById(
        "continue-reading-inference-robustness-btn"
      );

    if (!wrap || !label || !btn) return;

    label.innerHTML =
      "You last visited: <strong>" +
      data.label +
      "</strong>";

    btn.href = data.url;

    wrap.style.display = "block";

  } catch (e) {}

})();
</script>