---
layout: default
title: Independence and Random Sampling
description: Learn why independence and random sampling are fundamental assumptions behind nearly every statistical inference procedure.
permalink: /inference/foundations/independence-and-random-sampling/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_foundations_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/foundations/independence-and-random-sampling/",
    label: "Independence and Random Sampling",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 1</span>
      <span class="badge">Foundations</span>
      <span class="badge">Assumptions</span>
    </div>

    <h1>Independence and Random Sampling</h1>

    <p class="lead">
      Statistical inference relies on more than formulas and calculations.
    </p>

    <p class="lead">
      Behind every confidence interval, p-value, and hypothesis test are assumptions about how the data were collected. Two of the most important are independence and random sampling.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/foundations/confidence-vs-significance-preview/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/foundations/sampling-bias-vs-statistical-bias/">
         Next: Sampling Bias vs Statistical Bias →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Assumptions Matter</h2>

    <p>
      Statistical inference uses probability to describe uncertainty.
    </p>

    <p>
      Probability models only work when certain assumptions are approximately true.
    </p>

    <p>
      If the assumptions fail,
      inferential conclusions can become unreliable.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Good statistical methods cannot rescue badly collected data.
      </p>

    </div>

    <h2>The Foundation of Inference</h2>

    <p>
      Most inferential procedures assume:
    </p>

    <ul class="bullets">

      <li>Observations are randomly selected</li>

      <li>Observations are independent</li>

    </ul>

    <p>
      These assumptions allow probability theory to describe sampling behavior accurately.
    </p>

    <h2>What Is Random Sampling?</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Random sampling is a process in which population members are selected using chance rather than judgment or convenience.
      </p>

    </div>

    <p>
      Every population member should have a known opportunity to be selected.
    </p>

    <h2>Why Random Sampling Matters</h2>

    <p>
      Random sampling helps ensure that samples resemble the population.
    </p>

    <p>
      It reduces systematic selection distortions.
    </p>

    <div class="example-box">

      <p>
        Election polls
      </p>

      <p>
        Customer surveys
      </p>

      <p>
        Quality-control inspections
      </p>

    </div>

    <p>
      All rely on random sampling principles.
    </p>

    <h2>Random Sampling Does Not Mean Perfect Sampling</h2>

    <p>
      Random samples can still differ from the population.
    </p>

    <p>
      Sampling variability guarantees that no sample is perfect.
    </p>

    <p>
      However,
      random sampling prevents systematic favoritism toward certain outcomes.
    </p>

    <h2>What Is Independence?</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Observations are independent when knowing one observation provides no information about another observation.
      </p>

    </div>

    <p>
      Independence means observations behave as separate pieces of information.
    </p>

    <h2>An Example of Independence</h2>

    <p>
      Suppose we randomly select customers from a large customer database.
    </p>

    <p>
      One customer's spending generally tells us little about another randomly selected customer's spending.
    </p>

    <p>
      These observations are approximately independent.
    </p>

    <h2>An Example of Dependence</h2>

    <p>
      Suppose we measure the same person repeatedly.
    </p>

    <div class="example-box">

      <p>
        Monday blood pressure
      </p>

      <p>
        Tuesday blood pressure
      </p>

      <p>
        Wednesday blood pressure
      </p>

    </div>

    <p>
      These observations are related.
    </p>

    <p>
      One measurement provides information about another.
    </p>

    <p>
      Independence is violated.
    </p>

    <h2>Why Independence Is Important</h2>

    <p>
      Most statistical formulas assume observations contribute unique information.
    </p>

    <p>
      When observations are dependent,
      the effective amount of information is smaller than it appears.
    </p>

    <p>
      Standard errors can become misleading.
    </p>

    <h2>What Happens When Independence Fails?</h2>

    <p>
      Violations of independence often cause:
    </p>

    <ul class="bullets">

      <li>Incorrect standard errors</li>

      <li>Misleading confidence intervals</li>

      <li>Invalid p-values</li>

      <li>Overconfident conclusions</li>

    </ul>

    <p>
      The results may appear more precise than they truly are.
    </p>

    <h2>Random Sampling and Independence Are Related</h2>

    <p>
      In many situations,
      random sampling helps produce approximately independent observations.
    </p>

    <p>
      Especially when:
    </p>

    <div class="example-box">

      <p>
        Sample size is small relative to population size.
      </p>

    </div>

    <p>
      This is why introductory statistics often treats random sampling and independence together.
    </p>

    <h2>The 10% Condition</h2>

    <p>
      A common guideline states:
    </p>

    <div class="concept-box">

      <strong>10% Condition:</strong>

      <p>
        Sampling without replacement is often treated as approximately independent when the sample is less than 10% of the population.
      </p>

    </div>

    <p>
      This approximation is widely used in statistical practice.
    </p>

    <h2>Examples Where Independence Is Reasonable</h2>

    <ul class="bullets">

      <li>Randomly selected voters</li>

      <li>Randomly selected customers</li>

      <li>Randomly sampled manufactured products</li>

      <li>Large population surveys</li>

    </ul>

    <p>
      These settings often satisfy inferential assumptions reasonably well.
    </p>

    <h2>Examples Where Independence May Fail</h2>

    <ul class="bullets">

      <li>Repeated measurements on the same person</li>

      <li>Students within the same classroom</li>

      <li>Family members from the same household</li>

      <li>Time-series observations</li>

      <li>Social network data</li>

    </ul>

    <p>
      These situations often require specialized statistical methods.
    </p>

    <h2>Random Sampling vs Random Assignment</h2>

    <p>
      These ideas are often confused.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Concept</th>
            <th>Purpose</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Random Sampling</td>
            <td>Represent a population</td>
          </tr>

          <tr>
            <td>Random Assignment</td>
            <td>Create comparable treatment groups</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Both involve randomness,
      but they solve different problems.
    </p>

    <h2>Can Inference Work Without Perfect Random Sampling?</h2>

    <p>
      In practice,
      perfectly random samples are uncommon.
    </p>

    <p>
      Statistical methods can still be useful when assumptions are approximately satisfied.
    </p>

    <p>
      However,
      stronger violations require greater caution.
    </p>

    <h2>The Inferential Chain</h2>

    <p>
      Most inferential procedures depend on:
    </p>

    <ol>

      <li>Random sampling</li>

      <li>Approximate independence</li>

      <li>Valid sampling distributions</li>

      <li>Reliable standard errors</li>

      <li>Reliable confidence intervals and tests</li>

    </ol>

    <p>
      If the first links fail,
      later conclusions may also fail.
    </p>

    <h2>Why Researchers Care So Much About Data Collection</h2>

    <p>
      Statistical inference begins long before calculations are performed.
    </p>

    <p>
      The quality of conclusions depends heavily on how data are obtained.
    </p>

    <p>
      Good sampling designs are often more important than sophisticated analyses.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Random sampling helps produce representative data, while independence ensures observations provide separate information. Together they form the foundation of reliable statistical inference.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Independence and random sampling help reduce distortions,
      but they do not eliminate all forms of bias.
    </p>

    <p>
      A particularly important distinction exists between sampling bias and statistical bias.
    </p>

    <p>
      The next lesson explains these two concepts and why confusing them can lead to major inferential mistakes.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Statistical inference depends on assumptions about data collection</li>

        <li>Random sampling helps create representative samples</li>

        <li>Independence means observations provide separate information</li>

        <li>Violations of independence can distort standard errors and p-values</li>

        <li>The 10% condition often justifies approximate independence</li>

        <li>Random sampling and random assignment are different concepts</li>

        <li>Reliable inference begins with reliable data collection</li>

        <li>Random sampling and independence are foundational assumptions in statistics</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/foundations/confidence-vs-significance-preview/">
         ← Previous: Confidence vs Significance Preview
      </a>

      <a class="btn"
         href="/inference/foundations/sampling-bias-vs-statistical-bias/">
         Next: Sampling Bias vs Statistical Bias →
      </a>

    </div>

  </div>

</section>