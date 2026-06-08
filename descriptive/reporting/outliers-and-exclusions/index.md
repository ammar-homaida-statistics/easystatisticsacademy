---
layout: default
title: Outliers and Exclusions
description: Learn how to identify outliers, when exclusions may be appropriate, and how to report data-cleaning decisions responsibly.
permalink: /descriptive/reporting/outliers-and-exclusions/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_reporting_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/reporting/outliers-and-exclusions/",
    label: "Outliers and Exclusions",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 7</span>
      <span class="badge">Reporting</span>
      <span class="badge">Data Quality</span>
    </div>

    <h1>Outliers and Exclusions</h1>

    <p class="lead">
      Real-world datasets often contain unusual observations.
    </p>

    <p class="lead">
      Some observations represent important information,
      while others may result from errors.
      Learning how to handle outliers responsibly is an essential statistical skill.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/reporting/association-not-causation/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/reporting/mini-case-study-end-to-end/">
         Next: Mini Case Study (End-to-End) →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>Why This Topic Matters</h2>

    <p>
      Outliers can have a substantial impact on statistical summaries.
    </p>

    <p>
      They may influence means,
      standard deviations,
      correlations,
      graphs,
      and conclusions.
    </p>

    <p>
      Decisions about excluding observations should therefore be made carefully and transparently.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Outliers should be investigated, not automatically removed.
      </p>

    </div>

    <h2>What Is an Outlier?</h2>

    <p>
      An outlier is an observation that appears unusually distant from the majority of the data.
    </p>

    <p>
      Outliers may occur at either end of a distribution.
    </p>

    <div class="example-box">

      <p>
        10, 12, 13, 14, 15, 16, 120
      </p>
    </div>

    <p>
      The value 120 appears far from the remaining observations and would likely be considered an outlier.
    </p>

    <h2>Outliers Are Not Automatically Problems</h2>

    <p>
      A common mistake is assuming that all outliers are errors.
    </p>

    <p>
      Many outliers are legitimate observations.
    </p>

    <div class="example-box">

      <p>
        A billionaire's income may appear as an outlier in a population income dataset.
      </p>
    </div>

    <p>
      Although unusual,
      the observation may be completely valid.
    </p>

    <h2>Common Sources of Outliers</h2>

    <p>
      Outliers can arise from several sources:
    </p>

    <ul class="bullets">

      <li>Natural variation</li>

      <li>Rare events</li>

      <li>Measurement errors</li>

      <li>Data-entry mistakes</li>

      <li>Equipment failures</li>

      <li>Sampling issues</li>

    </ul>

    <p>
      Understanding the source is often more important than identifying the outlier itself.
    </p>

    <h2>Investigate Before Acting</h2>

    <p>
      Before excluding an observation,
      analysts should ask:
    </p>

    <ul class="bullets">

      <li>Is the value possible?</li>

      <li>Was it recorded correctly?</li>

      <li>Could it result from measurement error?</li>

      <li>Does it represent a special case?</li>

      <li>Would removing it change conclusions?</li>

    </ul>

    <p>
      These questions help guide responsible decision-making.
    </p>

    <h2>Data Errors Should Be Corrected</h2>

    <p>
      If an observation clearly results from an error,
      correction or removal may be justified.
    </p>

    <div class="example-box">

      <p>
        Age = 450 years
      </p>
    </div>

    <p>
      This value is impossible for a human and likely reflects a data-entry error.
    </p>

    <p>
      Such cases should be investigated and documented.
    </p>

    <h2>Valid Outliers Usually Stay</h2>

    <p>
      When an unusual observation is valid,
      removing it simply because it is inconvenient is poor statistical practice.
    </p>

    <p>
      Valid observations are part of the data-generating process and often contain important information.
    </p>

    <h2>What Is an Exclusion?</h2>

    <p>
      An exclusion occurs when one or more observations are intentionally removed from an analysis.
    </p>

    <p>
      Exclusions may occur before or after data collection.
    </p>

    <p>
      Every exclusion should have a clear justification.
    </p>

    <h2>Legitimate Reasons for Exclusion</h2>

    <ul class="bullets">

      <li>Recording errors</li>

      <li>Duplicate observations</li>

      <li>Equipment malfunctions</li>

      <li>Missing critical information</li>

      <li>Failure to meet predefined study criteria</li>

    </ul>

    <p>
      These reasons should be documented clearly.
    </p>

    <h2>Poor Reasons for Exclusion</h2>

    <ul class="bullets">

      <li>The value looks unusual</li>

      <li>The value reduces significance</li>

      <li>The value changes conclusions</li>

      <li>The value is inconvenient</li>

    </ul>

    <p>
      Excluding observations for these reasons introduces bias and undermines credibility.
    </p>

    <h2>Transparency Is Essential</h2>

    <p>
      Readers should know when observations have been excluded.
    </p>

    <p>
      Statistical reporting should clearly explain:
    </p>

    <ul class="bullets">

      <li>How many observations were removed</li>

      <li>Why they were removed</li>

      <li>When they were removed</li>

      <li>How exclusions affected analysis</li>

    </ul>

    <p>
      Transparency builds trust.
    </p>

    <h2>Report the Original Sample Size</h2>

    <p>
      Analysts should often report both:
    </p>

    <ul class="bullets">

      <li>Initial sample size</li>

      <li>Final analyzed sample size</li>

    </ul>

    <div class="example-box">

      <p>
        Initial sample: n = 520
      </p>

      <p>
        Excluded observations: 8
      </p>

      <p>
        Final sample: n = 512
      </p>

    </div>

    <p>
      This approach allows readers to evaluate the impact of exclusions.
    </p>

    <h2>Outliers and Summary Statistics</h2>

    <p>
      Outliers can influence some statistics more than others.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Statistic</th>
            <th>Sensitivity to Outliers</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Mean</td>
            <td>High</td>
          </tr>

          <tr>
            <td>Standard Deviation</td>
            <td>High</td>
          </tr>

          <tr>
            <td>Range</td>
            <td>Very High</td>
          </tr>

          <tr>
            <td>Median</td>
            <td>Low</td>
          </tr>

          <tr>
            <td>Interquartile Range</td>
            <td>Low</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      This is why robust measures are often preferred when extreme observations exist.
    </p>

    <h2>Use Graphs to Investigate Outliers</h2>

    <p>
      Visualizations are often the best way to identify unusual observations.
    </p>

    <p>
      Common tools include:
    </p>

    <ul class="bullets">

      <li>Boxplots</li>

      <li>Histograms</li>

      <li>Scatterplots</li>

      <li>Density plots</li>

    </ul>

    <p>
      These graphs help determine whether observations are isolated or part of a broader pattern.
    </p>

    <h2>Sensitivity Analysis</h2>

    <p>
      Analysts sometimes perform analyses both with and without outliers.
    </p>

    <p>
      This process is called a sensitivity analysis.
    </p>

    <p>
      Comparing results helps determine how strongly conclusions depend on specific observations.
    </p>

    <div class="example-box">

      <p>
        Mean with outlier = 82.4
      </p>

      <p>
        Mean without outlier = 75.9
      </p>

    </div>

    <p>
      Such differences may be important to report.
    </p>

    <h2>Ethical Reporting</h2>

    <p>
      Data analysis involves judgment,
      but judgment must be applied responsibly.
    </p>

    <p>
      Removing observations simply to obtain preferred results is unethical.
    </p>

    <p>
      Statistical integrity requires honest reporting of all decisions.
    </p>

    <h2>How to Report Exclusions</h2>

    <div class="example-box">

      <p>
        "Five observations were excluded because of confirmed data-entry errors. Analyses were conducted on the remaining 495 observations."
      </p>

    </div>

    <p>
      This statement clearly communicates what happened and why.
    </p>

    <h2>A Good Rule of Thumb</h2>

    <div class="concept-box">

      <strong>Practical guideline:</strong>

      <p>
        If an observation is unusual, investigate it.
        If it is incorrect, correct or remove it.
        If it is valid, report it and consider its influence.
      </p>

    </div>

    <h2>Why This Matters for Reporting</h2>

    <p>
      Readers need confidence that conclusions are based on evidence rather than selective reporting.
    </p>

    <p>
      Careful handling of outliers and exclusions improves:
    </p>

    <ul class="bullets">

      <li>Credibility</li>

      <li>Transparency</li>

      <li>Reproducibility</li>

      <li>Trustworthiness</li>

    </ul>

    <p>
      These qualities are essential in professional statistical work.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Throughout this course,
      we have learned how to describe data,
      summarize distributions,
      visualize patterns,
      and communicate findings.
    </p>

    <p>
      The next lesson brings everything together in a complete end-to-end case study that demonstrates the full descriptive statistics workflow.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Outliers are unusual observations but are not automatically errors</li>

        <li>Every outlier should be investigated before action is taken</li>

        <li>Valid outliers often contain important information</li>

        <li>Exclusions require clear justification and documentation</li>

        <li>Transparency is essential when observations are removed</li>

        <li>Different statistics respond differently to outliers</li>

        <li>Responsible handling of unusual observations improves statistical credibility</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/reporting/association-not-causation/">
         ← Previous: Association Is Not Causation
      </a>

      <a class="btn"
         href="/descriptive/reporting/mini-case-study-end-to-end/">
         Next: Mini Case Study (End-to-End) →
      </a>

    </div>

  </div>

</section>