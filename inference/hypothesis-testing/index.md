---
layout: default
title: Block 3 — Hypothesis Testing
description: Learn the logic of hypothesis testing: null models, test statistics, p-values, Type I and II errors, power, and decision-making under uncertainty.
permalink: /inference/hypothesis-testing/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_inference_last_block_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/hypothesis-testing/",
    label: "Block 3 — Hypothesis Testing",
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
        <span class="badge">Block 3</span>
        <span class="badge">Testing</span>
        <span class="badge">p-values</span>
      </div>

      <h1>Block 3 — Hypothesis Testing</h1>

      <p class="lead">
        Hypothesis testing provides a formal framework for evaluating evidence
        and making decisions under uncertainty.
      </p>

      <p class="lead">
        This block develops testing logic from first principles,
        focusing on null models,
        p-values,
        error rates,
        and the interpretation of statistical evidence.
      </p>

      <p class="muted-mini">
        10 lessons • Core inferential reasoning • Builds on Confidence Intervals • Prepares for Classical Tests
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
          ⚖️
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            Hypothesis testing is one of the most widely used tools in statistics.
            Understanding its logic is essential for interpreting scientific evidence,
            evaluating claims,
            and avoiding common statistical misconceptions.
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
          <div class="mini-body">Core statistical inference</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Evaluate evidence using formal tests
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Next block</div>
          <div class="mini-body">
            Classical Tests
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-inference-testing"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-inference-testing-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-inference-testing-btn"
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
      These lessons build the conceptual foundations of hypothesis testing
      before introducing specific statistical procedures.
    </p>

  </div>

  <div class="grid grid-2">

    <!-- LESSON 1 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/hypothesis-testing/what-is-a-hypothesis-test/">
          What Is a Hypothesis Test?
        </a>
      </h3>

      <p>
        Learn how hypothesis tests formalize decision-making
        under uncertainty.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Testing</span>
        <span class="pill">Evidence</span>
        <span class="pill">Foundations</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/hypothesis-testing/what-is-a-hypothesis-test/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 2 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/hypothesis-testing/null-and-alternative/">
          Null and Alternative Hypotheses
        </a>
      </h3>

      <p>
        Understand the roles of H₀ and H₁
        and how hypotheses are formulated.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">H₀</span>
        <span class="pill">Alternative</span>
        <span class="pill">Setup</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/hypothesis-testing/null-and-alternative/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 3 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/hypothesis-testing/test-statistic-standardization/">
          Test Statistics and Standardization
        </a>
      </h3>

      <p>
        Learn how observed signals are converted
        into standardized evidence measures.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Test Statistic</span>
        <span class="pill">SE Units</span>
        <span class="pill">Standardization</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/hypothesis-testing/test-statistic-standardization/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 4 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/hypothesis-testing/p-value-meaning/">
          The p-Value: Meaning and Misinterpretation
        </a>
      </h3>

      <p>
        Understand what p-values represent,
        how they are computed,
        and common interpretation errors.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">p-value</span>
        <span class="pill">Interpretation</span>
        <span class="pill">Evidence</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/hypothesis-testing/p-value-meaning/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 5 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/hypothesis-testing/significance-level-alpha/">
          Significance Level (α) and Decision Rules
        </a>
      </h3>

      <p>
        Learn how significance levels control
        false positive risk and testing decisions.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Alpha</span>
        <span class="pill">Decision Rule</span>
        <span class="pill">Significance</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/hypothesis-testing/significance-level-alpha/"
      >
        Open lesson
      </a>

    </div>

<!-- LESSON 6 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/hypothesis-testing/type1-type2-errors/">
          Type I and Type II Errors
        </a>
      </h3>

      <p>
        Understand false positives,
        false negatives,
        and the trade-off between the two types of errors.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Type I</span>
        <span class="pill">Type II</span>
        <span class="pill">Errors</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/hypothesis-testing/type1-type2-errors/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 7 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/hypothesis-testing/power-and-effect-size/">
          Power and Effect Size
        </a>
      </h3>

      <p>
        Learn how statistical power relates to effect size,
        sample size,
        and the ability to detect real effects.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Power</span>
        <span class="pill">Effect Size</span>
        <span class="pill">Detection</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/hypothesis-testing/power-and-effect-size/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 8 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/hypothesis-testing/one-sided-vs-two-sided/">
          One-Sided vs Two-Sided Tests
        </a>
      </h3>

      <p>
        Learn when directional hypotheses are appropriate
        and how tail choices affect conclusions.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">One-Sided</span>
        <span class="pill">Two-Sided</span>
        <span class="pill">Tails</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/hypothesis-testing/one-sided-vs-two-sided/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 9 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/hypothesis-testing/ci-and-test-connection/">
          Connection Between CIs and Tests
        </a>
      </h3>

      <p>
        Discover why confidence intervals and hypothesis tests
        are different views of the same inferential framework.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">CI</span>
        <span class="pill">Testing</span>
        <span class="pill">Connection</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/hypothesis-testing/ci-and-test-connection/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 10 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/hypothesis-testing/practical-significance/">
          Statistical vs Practical Significance
        </a>
      </h3>

      <p>
        Learn why statistical significance does not automatically imply
        practical importance.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Significance</span>
        <span class="pill">Effect Size</span>
        <span class="pill">Interpretation</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/hypothesis-testing/practical-significance/"
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
        Confidence intervals quantify uncertainty.
        Hypothesis testing uses that same uncertainty framework
        to evaluate claims and make decisions based on evidence.
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
              <td>Null Hypothesis</td>
              <td>Provides the reference model for testing</td>
            </tr>

            <tr>
              <td>Test Statistic</td>
              <td>Measures evidence in standardized units</td>
            </tr>

            <tr>
              <td>p-Value</td>
              <td>Quantifies compatibility with the null model</td>
            </tr>

            <tr>
              <td>Error Types</td>
              <td>Explain risks associated with decisions</td>
            </tr>

            <tr>
              <td>Power</td>
              <td>Determines ability to detect meaningful effects</td>
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

        <li>Understand hypothesis testing as evidence evaluation under uncertainty</li>

        <li>Formulate null and alternative hypotheses correctly</li>

        <li>Interpret test statistics and p-values appropriately</li>

        <li>Understand significance levels and decision rules</li>

        <li>Distinguish Type I and Type II errors</li>

        <li>Explain statistical power and effect size</li>

        <li>Connect confidence intervals and hypothesis tests</li>

        <li>Distinguish statistical significance from practical significance</li>

        <li>Prepare for Classical Tests</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next block</div>

        <div class="mini-body">
          Continue to <strong>Classical Tests</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          Hypothesis testing measures how compatible observed data are with a null model.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Big transition</div>

        <div class="mini-body">
          The testing framework developed here becomes the foundation for t-tests, chi-square tests, and other classical procedures.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/inference/confidence-intervals/">
      ← Previous Block: Confidence Intervals
    </a>

    <a class="btn" href="/inference/classical-tests/">
      Next Block: Classical Tests →
    </a>

  </div>

</section>

<!-- CONTINUE READING SCRIPT -->

<script>
(function () {

  try {

    const KEY =
      "esa_continue_inference_hypothesis_testing_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    if (!data || !data.url || !data.label) return;

    const wrap =
      document.getElementById(
        "continue-reading-inference-testing"
      );

    const label =
      document.getElementById(
        "continue-reading-inference-testing-label"
      );

    const btn =
      document.getElementById(
        "continue-reading-inference-testing-btn"
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