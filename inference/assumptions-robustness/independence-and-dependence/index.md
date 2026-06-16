---
layout: default
title: Independence and Dependence
description: Learn why independence is one of the most important assumptions in statistics, how dependence arises, and how violations can affect inference.
permalink: /inference/assumptions-robustness/independence-and-dependence/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_assumptions_robustness_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/assumptions-robustness/independence-and-dependence/",
    label: "Independence and Dependence",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 7</span>
      <span class="badge">Assumptions & Robustness</span>
      <span class="badge">Independence</span>
    </div>

    <h1>Independence and Dependence</h1>

    <p class="lead">
      Independence is one of the most important assumptions in statistical inference.
    </p>

    <p class="lead">
      Unlike many mild departures from normality, violations of independence can seriously distort standard errors, confidence intervals, hypothesis tests, and conclusions.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/assumptions-robustness/checking-normality-what-and-why/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/assumptions-robustness/heteroscedasticity-variance-issues/">
         Next: Heteroscedasticity & Variance Issues →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Independence Matters</h2>

    <p>
      Most statistical methods assume that observations provide separate pieces of information.
    </p>

    <p>
      If observations are strongly related to one another, the amount of information in a dataset may be much smaller than the sample size suggests.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Independence means that information provided by one observation does not directly determine information provided by another observation.
      </p>

    </div>

    <h2>What Is Independence?</h2>

    <p>
      Informally, two observations are independent if learning one does not change what we expect about the other.
    </p>

    <p>
      In probability theory, independence means:
    </p>

    0

    <p>
      Knowledge about one event provides no information about the occurrence of the other.
    </p>

    <h2>Examples of Independent Observations</h2>

    <ul class="bullets">

      <li>Randomly selected individuals from a large population</li>

      <li>Independent experimental units</li>

      <li>Repeated fair coin flips</li>

      <li>Measurements collected from unrelated subjects</li>

    </ul>

    <p>
      In these situations, one observation typically provides little information about another.
    </p>

    <h2>What Is Dependence?</h2>

    <p>
      Dependence occurs when observations are connected in some way.
    </p>

    <p>
      Information from one observation helps predict or explain another observation.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Dependence exists when observations influence one another or share common sources of variation.
      </p>

    </div>

    <h2>Examples of Dependence</h2>

    <ul class="bullets">

      <li>Repeated measurements from the same person</li>

      <li>Students within the same classroom</li>

      <li>Patients within the same hospital</li>

      <li>Daily stock prices over time</li>

      <li>Members of the same household</li>

    </ul>

    <p>
      These observations are naturally related rather than fully independent.
    </p>

    <h2>A Classroom Example</h2>

    <p>
      Suppose test scores are collected from students in the same classroom.
    </p>

    <p>
      Students share:
    </p>

    <ul class="bullets">

      <li>The same teacher</li>

      <li>The same curriculum</li>

      <li>The same environment</li>

    </ul>

    <p>
      As a result, their scores may be more similar than scores from randomly selected students across many schools.
    </p>

    <h2>Why Dependence Causes Problems</h2>

    <p>
      Most standard formulas assume that every observation contributes entirely new information.
    </p>

    <p>
      When observations are dependent:
    </p>

    <ul class="bullets">

      <li>Effective sample size decreases</li>

      <li>Standard errors may be underestimated</li>

      <li>Confidence intervals may be too narrow</li>

      <li>P-values may become artificially small</li>

    </ul>

    <p>
      These problems can create false confidence in results.
    </p>

    <h2>The Effective Sample Size Idea</h2>

    <p>
      Imagine collecting 100 observations that are nearly identical.
    </p>

    <p>
      Although the dataset contains 100 records, it does not provide the same amount of information as 100 truly independent observations.
    </p>

    <p>
      Dependence reduces informational diversity.
    </p>

    <h2>Time-Series Dependence</h2>

    <p>
      Dependence commonly occurs in data collected over time.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Stock prices</li>

      <li>Weather measurements</li>

      <li>Website traffic</li>

      <li>Economic indicators</li>

    </ul>

    <p>
      Today's value often resembles yesterday's value.
    </p>

    <h2>Autocorrelation</h2>

    <p>
      Dependence across time is often called:
    </p>

    <div class="example-box">

      <p>
        Autocorrelation
      </p>
    </div>

    <p>
      Positive autocorrelation means nearby observations tend to be similar.
    </p>

    <p>
      Negative autocorrelation means nearby observations tend to move in opposite directions.
    </p>

    <h2>Clustered Data</h2>

    <p>
      Dependence also appears when observations belong to groups.
    </p>

    <p>
      Common examples include:
    </p>

    <ul class="bullets">

      <li>Schools</li>

      <li>Hospitals</li>

      <li>Families</li>

      <li>Geographic regions</li>

    </ul>

    <p>
      Observations within a cluster are often more alike than observations from different clusters.
    </p>

    <h2>Repeated-Measures Data</h2>

    <p>
      Another common source of dependence occurs when the same individual is measured multiple times.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Before-and-after studies</li>

      <li>Longitudinal studies</li>

      <li>Growth tracking</li>

      <li>Medical follow-up studies</li>

    </ul>

    <p>
      Measurements from the same person are rarely independent.
    </p>

    <h2>Can Independence Be Checked?</h2>

    <p>
      Unlike normality, independence is often difficult to verify directly from data alone.
    </p>

    <p>
      Analysts frequently rely on:
    </p>

    <ul class="bullets">

      <li>Study design information</li>

      <li>Sampling procedures</li>

      <li>Knowledge of the data-generating process</li>

      <li>Diagnostic plots</li>

    </ul>

    <p>
      Understanding how data were collected is often crucial.
    </p>

    <h2>Design Matters</h2>

    <p>
      Independence is frequently a design assumption rather than a model assumption.
    </p>

    <p>
      Questions such as:
    </p>

    <ul class="bullets">

      <li>Were units sampled randomly?</li>

      <li>Are observations clustered?</li>

      <li>Are repeated measurements present?</li>

    </ul>

    <p>
      are often more important than formal statistical diagnostics.
    </p>

    <h2>Handling Dependence</h2>

    <p>
      When dependence exists, specialized methods may be required.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Paired analyses</li>

      <li>Mixed-effects models</li>

      <li>Time-series models</li>

      <li>Cluster-robust standard errors</li>

    </ul>

    <p>
      These methods explicitly account for dependence structures.
    </p>

    <h2>Independence vs Normality</h2>

    <p>
      Analysts often worry more about normality than independence.
    </p>

    <p>
      In practice:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Violation</th>
            <th>Typical Consequence</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Mild non-normality</td>
            <td>Often minor</td>
          </tr>

          <tr>
            <td>Strong dependence</td>
            <td>Potentially severe</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      This is why independence is often considered one of the most important assumptions in inference.
    </p>

    <h2>The Robustness Perspective</h2>

    <p>
      Many statistical methods are reasonably robust to modest departures from normality.
    </p>

    <p>
      Fewer methods are robust to serious dependence that is ignored during analysis.
    </p>

    <p>
      Understanding dependence is therefore critical for trustworthy inference.
    </p>

    <h2>A Practical Checklist</h2>

    <p>
      Before performing inference, ask:
    </p>

    <ol>

      <li>Could observations influence one another?</li>

      <li>Were repeated measurements collected?</li>

      <li>Are observations clustered?</li>

      <li>Is there a time component?</li>

      <li>Does the analysis account for these relationships?</li>

    </ol>

    <h2>The Bigger Picture</h2>

    <p>
      Independence is a foundational assumption because it determines how much information is truly present in a dataset.
    </p>

    <p>
      Ignoring dependence can produce misleading confidence intervals, significance tests, and conclusions.
    </p>

    <p>
      Understanding where dependence arises is therefore a crucial part of responsible statistical analysis.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Independence means observations provide separate information, while dependence means observations are related. Violations of independence can substantially distort statistical inference and often require specialized methods.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Another important assumption concerns variability.
    </p>

    <p>
      Many methods assume that variability remains reasonably constant across observations or groups.
    </p>

    <p>
      The next lesson examines heteroscedasticity, unequal variances, and how changing variability can affect statistical conclusions.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Independence is one of the most important assumptions in inference</li>

        <li>Dependent observations share information</li>

        <li>Dependence reduces effective sample size</li>

        <li>Ignoring dependence can underestimate standard errors</li>

        <li>Time-series, clustered, and repeated-measures data commonly exhibit dependence</li>

        <li>Independence is often a design assumption</li>

        <li>Specialized methods exist for dependent data</li>

        <li>Violations of independence are often more serious than mild non-normality</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/assumptions-robustness/checking-normality-what-and-why/">
         ← Previous: Checking Normality: What and Why
      </a>

      <a class="btn"
         href="/inference/assumptions-robustness/heteroscedasticity-variance-issues/">
         Next: Heteroscedasticity & Variance Issues →
      </a>

    </div>

  </div>

</section>