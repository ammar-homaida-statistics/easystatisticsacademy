---
layout: default
title: Z Statistic and Confidence Intervals
description: Learn how z-statistics standardize estimates and how confidence intervals are constructed from sampling distributions.
permalink: /probability/sampling-distributions/z-statistic-and-ci/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_sampling_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/sampling-distributions/z-statistic-and-ci/",
    label: "Z Statistic and Confidence Intervals",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 7</span>
      <span class="badge">Sampling Distributions</span>
      <span class="badge">Inference</span>
    </div>

    <h1>Z Statistic and Confidence Intervals</h1>

    <p class="lead">
      Estimators vary from sample to sample, but standard errors tell us how much variation to expect.
    </p>

    <p class="lead">
      Z-statistics and confidence intervals use that information to measure uncertainty and draw conclusions about unknown population parameters.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/sampling-distributions/standard-error-and-estimators/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/sampling-distributions/t-distribution-and-t-test/">
         Next: t Distribution and t Test →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Standardization Matters</h2>

    <p>
      Different variables use different units.
    </p>

    <div class="example-box">

      <p>
        Dollars
      </p>

      <p>
        Kilograms
      </p>

      <p>
        Test scores
      </p>

      <p>
        Percentages
      </p>

    </div>

    <p>
      To compare results fairly,
      statisticians convert them to a common scale.
    </p>

    <p>
      This process is called standardization.
    </p>

    <h2>The Z Statistic</h2>

    <p>
      A z-statistic measures how far an estimate lies from a target value in units of standard error.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A z-statistic tells us how many standard errors an estimate is above or below a reference value.
      </p>

    </div>

    <h2>The Formula</h2>

    <p>
      The general z-statistic is:
    </p>

    0

    <p>
      The numerator measures distance from the target.
    </p>

    <p>
      The denominator scales that distance using expected sampling variability.
    </p>

    <h2>Interpreting Z Values</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Z Value</th>
            <th>Interpretation</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>0</td>
            <td>Exactly at the reference value</td>
          </tr>

          <tr>
            <td>1</td>
            <td>One standard error above</td>
          </tr>

          <tr>
            <td>-1</td>
            <td>One standard error below</td>
          </tr>

          <tr>
            <td>2</td>
            <td>Two standard errors above</td>
          </tr>

          <tr>
            <td>-2</td>
            <td>Two standard errors below</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Example: Sample Mean</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        Sample mean = 105
      </p>

      <p>
        Reference value = 100
      </p>

      <p>
        Standard error = 2
      </p>

    </div>

    <p>
      Then:
    </p>

    1

    <p>
      The estimate is 2.5 standard errors above the reference value.
    </p>

    <h2>The Standard Normal Distribution</h2>

    <p>
      Under many conditions,
      z-statistics follow the standard normal distribution:
    </p>

    <div class="example-box">

      <p>
        Mean = 0
      </p>

      <p>
        Standard deviation = 1
      </p>

    </div>

    <p>
      This allows probabilities to be calculated using standard normal tables or software.
    </p>

    <h2>The 95% Rule</h2>

    <p>
      For a standard normal distribution:
    </p>

    <div class="example-box">

      <p>
        About 95% of values lie within ±1.96 standard deviations of the mean.
      </p>

    </div>

    <p>
      This fact is the foundation of the most common confidence interval.
    </p>

    <h2>What Is a Confidence Interval?</h2>

    <p>
      A confidence interval provides a range of plausible values for an unknown population parameter.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A confidence interval combines an estimate with a margin of error to express uncertainty.
      </p>

    </div>

    <h2>The General Structure</h2>

    <p>
      Confidence intervals have the form:
    </p>

    2

    <p>
      The margin of error depends on the standard error and confidence level.
    </p>

    <h2>The 95% Confidence Interval Formula</h2>

    <p>
      For many large-sample situations:
    </p>

    3

    <p>
      This produces an approximate 95% confidence interval.
    </p>

    <h2>Example Confidence Interval</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        Sample mean = 50
      </p>

      <p>
        Standard error = 3
      </p>

    </div>

    <p>
      The margin of error is:
    </p>

    4

    <p>
      Therefore:
    </p>

    5

    <p>
      giving:
    </p>

    <div class="example-box">

      <p>
        [44.12, 55.88]
      </p>

    </div>

    <h2>Interpreting a Confidence Interval</h2>

    <p>
      A common interpretation is:
    </p>

    <div class="example-box">

      <p>
        We are 95% confident that the population parameter lies within the interval.
      </p>

    </div>

    <p>
      The interval reflects uncertainty from sampling variability.
    </p>

    <h2>What Confidence Does NOT Mean</h2>

    <p>
      Confidence intervals are often misunderstood.
    </p>

    <p>
      A 95% confidence interval does not mean:
    </p>

    <div class="example-box">

      <p>
        There is a 95% probability the parameter is inside this particular interval.
      </p>

    </div>

    <p>
      The parameter is fixed.
    </p>

    <p>
      The interval is random because it depends on the sample.
    </p>

    <h2>Confidence Level and Width</h2>

    <p>
      Higher confidence requires wider intervals.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Confidence Level</th>
            <th>Approximate Multiplier</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>90%</td>
            <td>1.645</td>
          </tr>

          <tr>
            <td>95%</td>
            <td>1.96</td>
          </tr>

          <tr>
            <td>99%</td>
            <td>2.576</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Greater confidence means accepting a wider range of plausible values.
    </p>

    <h2>The Role of Sample Size</h2>

    <p>
      Since:
    </p>

    6

    <p>
      larger samples reduce standard error.
    </p>

    <p>
      Smaller standard errors produce narrower confidence intervals.
    </p>

    <p>
      Larger samples therefore provide more precise estimates.
    </p>

    <h2>Why Z Statistics Matter</h2>

    <p>
      Z-statistics provide a common language for measuring evidence and uncertainty.
    </p>

    <p>
      They appear throughout:
    </p>

    <ul class="bullets">

      <li>Confidence intervals</li>

      <li>Hypothesis testing</li>

      <li>Regression analysis</li>

      <li>Machine learning evaluation</li>

    </ul>

    <h2>The Big Picture</h2>

    <p>
      Estimators provide numerical summaries.
    </p>

    <p>
      Standard errors measure uncertainty.
    </p>

    <p>
      Z-statistics standardize results.
    </p>

    <p>
      Confidence intervals combine all three to communicate what the data suggest about unknown population parameters.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The z-statistic works well when population variability is known or sample sizes are large.
    </p>

    <p>
      In practice,
      population variability is often unknown.
    </p>

    <p>
      The next lesson introduces the t-distribution and t-tests, which address this common situation.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Z-statistics measure distance in units of standard error</li>

        <li>The standard normal distribution is the basis for many inferential methods</li>

        <li>Confidence intervals provide ranges of plausible parameter values</li>

        <li>A 95% confidence interval often uses the multiplier 1.96</li>

        <li>Confidence intervals combine estimates and margins of error</li>

        <li>Larger samples produce narrower confidence intervals</li>

        <li>Z-statistics and confidence intervals are fundamental inferential tools</li>

        <li>They rely directly on sampling distributions and standard errors</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/sampling-distributions/standard-error-and-estimators/">
         ← Previous: Standard Error and Estimators
      </a>

      <a class="btn"
         href="/probability/sampling-distributions/t-distribution-and-t-test/">
         Next: t Distribution and t Test →
      </a>

    </div>

  </div>

</section>