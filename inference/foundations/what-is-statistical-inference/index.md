---
layout: default
title: What Is Statistical Inference?
description: Learn what statistical inference is and how statisticians use samples to learn about unknown populations.
permalink: /inference/foundations/what-is-statistical-inference/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_foundations_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/foundations/what-is-statistical-inference/",
    label: "What Is Statistical Inference?",
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
      <span class="badge">Lesson 1</span>
    </div>

    <h1>What Is Statistical Inference?</h1>

    <p class="lead">
      Data analysis often begins with a sample, but the real goal is usually to understand a larger population.
    </p>

    <p class="lead">
      Statistical inference provides the tools for moving from sample evidence to conclusions about unknown population characteristics.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/foundations/">
         ← Back to Foundations
      </a>

      <a class="btn btn-outline"
         href="/inference/foundations/populations-parameters-target/">
         Next: Populations, Parameters, and Targets →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Statistical Inference Exists</h2>

    <p>
      In most real-world situations,
      collecting data from an entire population is impossible, expensive, or impractical.
    </p>

    <div class="example-box">

      <p>
        Survey every voter in a country
      </p>

      <p>
        Test every manufactured product
      </p>

      <p>
        Measure every customer
      </p>

      <p>
        Observe every future event
      </p>

    </div>

    <p>
      Instead,
      we collect a sample and use it to learn about the population.
    </p>

    <h2>What Is Statistical Inference?</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Statistical inference is the process of using sample data to draw conclusions about a population.
      </p>

    </div>

    <p>
      Inference goes beyond describing observed data.
    </p>

    <p>
      It attempts to learn about quantities that are not directly observed.
    </p>

    <h2>Descriptive Statistics vs Statistical Inference</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Descriptive Statistics</th>
            <th>Statistical Inference</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Summarizes observed data</td>
            <td>Draws conclusions beyond the sample</td>
          </tr>

          <tr>
            <td>Describes what happened</td>
            <td>Estimates what is unknown</td>
          </tr>

          <tr>
            <td>Focuses on data</td>
            <td>Focuses on populations</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Core Challenge</h2>

    <p>
      Samples never perfectly match populations.
    </p>

    <p>
      Different samples produce different results.
    </p>

    <div class="example-box">

      <p>
        Sample A → Average income = $48,000
      </p>

      <p>
        Sample B → Average income = $51,000
      </p>

      <p>
        Sample C → Average income = $49,500
      </p>

    </div>

    <p>
      Statistical inference helps us quantify and manage this uncertainty.
    </p>

    <h2>The Basic Logic of Inference</h2>

    <p>
      Statistical inference follows a simple pattern:
    </p>

    <ol>

      <li>Collect a sample.</li>

      <li>Compute sample statistics.</li>

      <li>Measure uncertainty.</li>

      <li>Draw conclusions about the population.</li>

    </ol>

    <p>
      Every inferential method follows this general logic.
    </p>

    <h2>Why Probability Is Necessary</h2>

    <p>
      Inference depends on probability theory.
    </p>

    <p>
      Probability tells us how sample statistics behave under repeated sampling.
    </p>

    <p>
      Without probability,
      we could not evaluate uncertainty or reliability.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Probability provides the mathematical foundation for statistical inference.
      </p>

    </div>

    <h2>What Are We Trying to Learn?</h2>

    <p>
      Inference often focuses on unknown population quantities such as:
    </p>

    <ul class="bullets">

      <li>Population mean</li>

      <li>Population proportion</li>

      <li>Population variance</li>

      <li>Differences between groups</li>

      <li>Relationships between variables</li>

    </ul>

    <p>
      These quantities are called parameters.
    </p>

    <h2>Two Major Goals of Inference</h2>

    <p>
      Most inferential procedures belong to one of two categories.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Goal</th>
            <th>Question</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Estimation</td>
            <td>What is the parameter value?</td>
          </tr>

          <tr>
            <td>Hypothesis Testing</td>
            <td>What does the evidence suggest?</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Estimation</h2>

    <p>
      Estimation attempts to determine plausible values for unknown parameters.
    </p>

    <div class="example-box">

      <p>
        Estimate average customer spending
      </p>

      <p>
        Estimate election support
      </p>

      <p>
        Estimate disease prevalence
      </p>

    </div>

    <p>
      Confidence intervals are a major estimation tool.
    </p>

    <h2>Hypothesis Testing</h2>

    <p>
      Hypothesis testing evaluates claims using sample evidence.
    </p>

    <div class="example-box">

      <p>
        Is a new treatment effective?
      </p>

      <p>
        Has a process changed?
      </p>

      <p>
        Are two groups different?
      </p>

    </div>

    <p>
      Statistical tests help answer these questions systematically.
    </p>

    <h2>Uncertainty Is Central</h2>

    <p>
      Unlike pure mathematics,
      statistical conclusions are rarely certain.
    </p>

    <p>
      Instead,
      conclusions are expressed with quantified uncertainty.
    </p>

    <div class="example-box">

      <p>
        95% confidence interval
      </p>

      <p>
        p-value
      </p>

      <p>
        Margin of error
      </p>

    </div>

    <p>
      These measures communicate the strength of evidence.
    </p>

    <h2>Examples of Statistical Inference</h2>

    <ul class="bullets">

      <li>Election polling</li>

      <li>Medical research</li>

      <li>A/B testing</li>

      <li>Quality control</li>

      <li>Market research</li>

      <li>Economic forecasting</li>

      <li>Machine learning evaluation</li>

    </ul>

    <p>
      Statistical inference is used wherever decisions must be made under uncertainty.
    </p>

    <h2>The Inferential Framework</h2>

    <p>
      Much of modern statistics can be summarized by a simple idea:
    </p>

    <div class="concept-box">

      <strong>Framework:</strong>

      <p>
        Use a sample to learn about a population while accounting for uncertainty caused by sampling variability.
      </p>

    </div>

    <h2>What Makes Inference Possible?</h2>

    <p>
      The entire field relies on concepts developed in probability:
    </p>

    <ul class="bullets">

      <li>Random variables</li>

      <li>Probability distributions</li>

      <li>Sampling distributions</li>

      <li>Law of Large Numbers</li>

      <li>Central Limit Theorem</li>

    </ul>

    <p>
      These ideas make reliable inference possible.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Before building inferential procedures,
      we must clearly distinguish populations from samples and parameters from statistics.
    </p>

    <p>
      These distinctions form the language of statistical inference.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Statistical inference uses samples to learn about populations</li>

        <li>Inference goes beyond description and addresses unknown quantities</li>

        <li>Probability theory provides the foundation for inference</li>

        <li>Most inferential goals involve estimation or hypothesis testing</li>

        <li>Sampling variability creates uncertainty</li>

        <li>Inference quantifies uncertainty rather than eliminating it</li>

        <li>Population parameters are the primary targets of inference</li>

        <li>Statistical inference is central to modern data-driven decision making</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/foundations/">
         ← Back to Foundations
      </a>

      <a class="btn"
         href="/inference/foundations/populations-parameters-target/">
         Next: Populations, Parameters, and Targets →
      </a>

    </div>

  </div>

</section>