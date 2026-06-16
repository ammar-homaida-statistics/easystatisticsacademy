---
layout: default
title: Multiple Testing and False Positives
description: Learn why conducting many hypothesis tests increases the chance of false positives and how statisticians address the multiple-testing problem.
permalink: /inference/interpretation-reporting/multiple-testing-and-false-positives/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_interpretation_reporting_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/interpretation-reporting/multiple-testing-and-false-positives/",
    label: "Multiple Testing and False Positives",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 6</span>
      <span class="badge">Interpretation & Reporting</span>
      <span class="badge">Multiple Testing</span>
    </div>

    <h1>Multiple Testing and False Positives</h1>

    <p class="lead">
      Hypothesis-testing procedures are usually taught one test at a time.
    </p>

    <p class="lead">
      In practice, researchers often perform many tests simultaneously, creating an increased risk of false-positive findings.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/interpretation-reporting/interpreting-effect-sizes/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/interpretation-reporting/reporting-results-clear-language/">
         Next: Reporting Results in Clear Language →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Basic Problem</h2>

    <p>
      A significance level controls the probability of a Type I error for a single hypothesis test.
    </p>

    <p>
      For example:
    </p>

    <div class="example-box">

      <p>
        α = 0.05
      </p>
    </div>

    <p>
      means a false positive is expected about 5% of the time when the null hypothesis is true.
    </p>

    <p>
      This interpretation applies to one test.
    </p>

    <h2>What Happens With Many Tests?</h2>

    <p>
      Suppose a researcher performs:
    </p>

    <div class="example-box">

      <p>
        20 independent hypothesis tests
      </p>
    </div>

    <p>
      using:
    </p>

    <div class="example-box">

      <p>
        α = 0.05
      </p>
    </div>

    <p>
      Even if every null hypothesis is true, some tests may appear significant purely by chance.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The more tests we perform, the greater the chance of obtaining at least one false positive.
      </p>

    </div>

    <h2>A Simple Illustration</h2>

    <p>
      Imagine repeatedly flipping a fair coin.
    </p>

    <p>
      One unusual outcome may not be surprising if enough opportunities are provided.
    </p>

    <p>
      Similarly, when many statistical tests are performed, rare events become more likely to occur somewhere in the collection of tests.
    </p>

    <h2>The Family-Wise Error Rate</h2>

    <p>
      The probability of making at least one Type I error among multiple tests is called the:
    </p>

    <div class="example-box">

      <p>
        Family-Wise Error Rate (FWER)
      </p>
    </div>

    <p>
      This quantity is often much larger than the nominal significance level for individual tests.
    </p>

    <h2>An Approximation</h2>

    <p>
      For independent tests, the probability of at least one false positive is:
    </p>

    

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>α = significance level for each test</li>

      <li>m = number of tests</li>

    </ul>

    <h2>Example</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>α = 0.05</p>
      <p>m = 20 tests</p>

    </div>

    <p>
      Then:
    </p>

    

    <p>
      There is approximately a 64% chance of observing at least one false positive.
    </p>

    <p>
      This is much larger than 5%.
    </p>

    <h2>Why This Matters</h2>

    <p>
      Researchers often explore many variables, outcomes, or subgroup comparisons.
    </p>

    <p>
      Without adjustment:
    </p>

    <ul class="bullets">

      <li>False discoveries become more common</li>

      <li>Evidence can be overstated</li>

      <li>Replication becomes more difficult</li>

    </ul>

    <h2>A Research Example</h2>

    <p>
      Suppose a medical study compares:
    </p>

    <ul class="bullets">

      <li>Blood pressure</li>

      <li>Heart rate</li>

      <li>Cholesterol</li>

      <li>Weight</li>

      <li>Several biomarkers</li>

    </ul>

    <p>
      across multiple treatment groups.
    </p>

    <p>
      The number of hypothesis tests can quickly become large.
    </p>

    <p>
      Some significant findings may emerge purely by chance.
    </p>

    <h2>Data Mining and False Positives</h2>

    <p>
      Modern datasets often contain hundreds or thousands of variables.
    </p>

    <p>
      If researchers search extensively for significant relationships:
    </p>

    <div class="example-box">

      <p>
        Some statistically significant results may appear even when no true relationships exist.
      </p>
    </div>

    <p>
      This phenomenon is sometimes called:
    </p>

    <div class="example-box">

      <p>
        Data dredging or p-hacking
      </p>
    </div>

    <h2>P-Hacking</h2>

    <p>
      P-hacking occurs when researchers repeatedly analyze data in ways that increase the chance of obtaining significant results.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Testing many outcomes</li>

      <li>Trying multiple models</li>

      <li>Removing observations selectively</li>

      <li>Stopping data collection after significance appears</li>

    </ul>

    <p>
      These practices can inflate false-positive rates.
    </p>

    <h2>The Bonferroni Correction</h2>

    <p>
      One of the simplest approaches to controlling family-wise error is:
    </p>

    <div class="example-box">

      <p>
        Bonferroni correction
      </p>
    </div>

    <p>
      The adjusted significance level becomes:
    </p>

    

    <h2>Bonferroni Example</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>α = 0.05</p>
      <p>m = 10 tests</p>

    </div>

    <p>
      Then:
    </p>

    

    <p>
      Each individual test must meet the stricter threshold.
    </p>

    <h2>Advantages and Limitations</h2>

    <p>
      Bonferroni correction is:
    </p>

    <ul class="bullets">

      <li>Simple</li>

      <li>Easy to explain</li>

      <li>Conservative</li>

    </ul>

    <p>
      However, it can reduce statistical power, especially when many tests are performed.
    </p>

    <h2>False Discovery Rate</h2>

    <p>
      In some applications, researchers focus on controlling:
    </p>

    <div class="example-box">

      <p>
        False Discovery Rate (FDR)
      </p>
    </div>

    <p>
      rather than family-wise error.
    </p>

    <p>
      FDR methods aim to limit the proportion of false positives among declared discoveries.
    </p>

    <h2>Why FDR Became Important</h2>

    <p>
      Fields such as:
    </p>

    <ul class="bullets">

      <li>Genomics</li>

      <li>Bioinformatics</li>

      <li>Machine learning</li>

      <li>Large-scale experimentation</li>

    </ul>

    <p>
      often involve thousands of simultaneous tests.
    </p>

    <p>
      Traditional family-wise controls may become too restrictive.
    </p>

    <h2>Pre-Registration</h2>

    <p>
      One strategy for reducing false positives is:
    </p>

    <div class="example-box">

      <p>
        Pre-registration
      </p>
    </div>

    <p>
      Researchers specify hypotheses and analysis plans before seeing the data.
    </p>

    <p>
      This reduces opportunities for selective reporting.
    </p>

    <h2>Exploratory vs Confirmatory Analysis</h2>

    <p>
      It is useful to distinguish:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Type</th>
            <th>Purpose</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Exploratory</td>
            <td>Generate hypotheses</td>
          </tr>

          <tr>
            <td>Confirmatory</td>
            <td>Test pre-specified hypotheses</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Multiple-testing concerns are especially important in exploratory analyses.
    </p>

    <h2>Replication as a Safeguard</h2>

    <p>
      Even with statistical corrections, replication remains one of the strongest protections against false discoveries.
    </p>

    <p>
      Genuine effects should be observable across multiple independent studies.
    </p>

    <h2>Reporting Multiple Tests Transparently</h2>

    <p>
      Good reporting practices include:
    </p>

    <ul class="bullets">

      <li>Reporting the number of tests conducted</li>

      <li>Describing adjustment procedures</li>

      <li>Distinguishing exploratory analyses</li>

      <li>Reporting effect sizes and confidence intervals</li>

    </ul>

    <p>
      Transparency helps readers evaluate the strength of evidence.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Hypothesis testing works well when a small number of carefully planned comparisons are performed.
    </p>

    <p>
      As the number of tests grows, false positives become increasingly likely.
    </p>

    <p>
      Multiple-testing adjustments and transparent reporting help maintain the reliability of statistical conclusions.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Conducting many hypothesis tests increases the likelihood of false positives. Researchers use methods such as Bonferroni corrections, false-discovery-rate procedures, pre-registration, and replication to reduce this risk.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Even when statistical analyses are performed correctly, results can still be misunderstood if they are communicated poorly.
    </p>

    <p>
      Effective reporting requires translating statistical findings into language that is accurate, clear, and accessible.
    </p>

    <p>
      The next lesson focuses on communicating statistical results in clear language for both technical and non-technical audiences.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Multiple testing increases the chance of false positives</li>

        <li>The family-wise error rate grows as more tests are performed</li>

        <li>P-hacking can inflate false-positive rates</li>

        <li>Bonferroni correction is a simple adjustment method</li>

        <li>False discovery rate methods are useful for large-scale testing</li>

        <li>Pre-registration helps reduce selective reporting</li>

        <li>Exploratory and confirmatory analyses should be distinguished</li>

        <li>Replication remains one of the strongest safeguards against false discoveries</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/interpretation-reporting/interpreting-effect-sizes/">
         ← Previous: Interpreting Effect Sizes
      </a>

      <a class="btn"
         href="/inference/interpretation-reporting/reporting-results-clear-language/">
         Next: Reporting Results in Clear Language →
      </a>

    </div>

  </div>

</section>