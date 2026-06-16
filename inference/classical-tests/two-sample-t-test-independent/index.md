---
layout: default
title: Two-Sample t Test (Independent Samples)
description: Learn how the two-sample t test compares the means of two independent populations and evaluates whether their average values differ.
permalink: /inference/classical-tests/two-sample-t-test-independent/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_classical_tests_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/two-sample-t-test-independent/",
    label: "Two-Sample t Test (Independent Samples)",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 4</span>
      <span class="badge">Classical Tests</span>
      <span class="badge">Two Groups</span>
    </div>

    <h1>Two-Sample t Test (Independent Samples)</h1>

    <p class="lead">
      Many research questions involve comparing two separate groups rather than a single population.
    </p>

    <p class="lead">
      The two-sample t test evaluates whether the means of two independent populations differ significantly.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/paired-t-test/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/classical-tests/one-proportion-z-test/">
         Next: One-Proportion Z Test →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Research Question</h2>

    <p>
      Suppose researchers want to compare:
    </p>

    <ul class="bullets">

      <li>A treatment group and a control group</li>

      <li>Students taught using two methods</li>

      <li>Average salaries in two industries</li>

      <li>Mean blood pressure in two populations</li>

    </ul>

    <p>
      The goal is to determine whether the population means differ.
    </p>

    <h2>Independent Samples</h2>

    <div class="concept-box">

      <strong>Independent samples:</strong>

      <p>
        Observations in one group are unrelated to observations in the other group.
      </p>

    </div>

    <p>
      This distinguishes the two-sample t test from the paired t test.
    </p>

    <h2>Examples of Independent Samples</h2>

    <div class="example-box">

      <p>
        Treatment group vs control group
      </p>

      <p>
        Men vs women
      </p>

      <p>
        School A vs School B
      </p>

      <p>
        Machine A vs Machine B
      </p>

    </div>

    <h2>Examples That Are NOT Independent</h2>

    <div class="example-box">

      <p>
        Before-and-after measurements on the same person
      </p>

      <p>
        Matched twins
      </p>

      <p>
        Repeated measurements on the same subject
      </p>

    </div>

    <p>
      These situations require a paired t test instead.
    </p>

    <h2>The Parameters of Interest</h2>

    <p>
      Let:
    </p>

    0

    <p>
      denote the mean of population 1 and:
    </p>

    1

    <p>
      denote the mean of population 2.
    </p>

    <p>
      The quantity of interest is:
    </p>

    2

    <h2>The Hypotheses</h2>

    <p>
      The standard two-sided hypotheses are:
    </p>

    3

    <br><br>

    4

    <p>
      Under the null hypothesis, the two population means are equal.
    </p>

    <h2>One-Sided Alternatives</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Alternative Hypothesis</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>μ₁ − μ₂ ≠ 0</td>
            <td>Means differ</td>
          </tr>

          <tr>
            <td>μ₁ − μ₂ &gt; 0</td>
            <td>Population 1 has larger mean</td>
          </tr>

          <tr>
            <td>μ₁ − μ₂ &lt; 0</td>
            <td>Population 1 has smaller mean</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Sample Statistics</h2>

    <p>
      For the two samples we observe:
    </p>

    <ul class="bullets">

      <li>x̄₁ = sample mean of group 1</li>

      <li>x̄₂ = sample mean of group 2</li>

      <li>s₁ = sample standard deviation of group 1</li>

      <li>s₂ = sample standard deviation of group 2</li>

      <li>n₁ = sample size of group 1</li>

      <li>n₂ = sample size of group 2</li>

    </ul>

    <h2>The Observed Difference</h2>

    <p>
      The observed estimate of:
    </p>

    5

    <p>
      is:
    </p>

    6

    <p>
      This quantity measures the observed difference between groups.
    </p>

    <h2>The Standard Error</h2>

    <p>
      For the common Welch two-sample t test:
    </p>

    7

    <p>
      This combines uncertainty from both samples.
    </p>

    <h2>The Test Statistic</h2>

    <p>
      The two-sample t statistic is:
    </p>

    8

    <p>
      Under the null hypothesis, the expected difference equals zero.
    </p>

    <h2>Why Welch's Test Is Common</h2>

    <p>
      Historically, many textbooks assumed equal population variances.
    </p>

    <p>
      Modern practice often prefers Welch's t test because it works well even when population variances differ.
    </p>

    <div class="concept-box">

      <strong>Practical recommendation:</strong>

      <p>
        Welch's two-sample t test is usually the default choice unless there is strong justification for assuming equal variances.
      </p>

    </div>

    <h2>Example Setup</h2>

    <div class="example-box">

      <p>x̄₁ = 82</p>
      <p>x̄₂ = 76</p>
      <p>s₁ = 10</p>
      <p>s₂ = 12</p>
      <p>n₁ = 25</p>
      <p>n₂ = 25</p>

    </div>

    <h2>Observed Difference</h2>

    <p>
      The estimated difference is:
    </p>

    9

    <p>
      The sample suggests group 1 scores higher on average.
    </p>

    <h2>Calculating the Standard Error</h2>

    <p>
      Using:
    </p>

    10

    <p>
      gives approximately:
    </p>

    11

    <h2>Calculating the t Statistic</h2>

    <p>
      Therefore:
    </p>

    12

    <p>
      This statistic is evaluated using the appropriate t distribution.
    </p>

    <h2>The p-Value</h2>

    <p>
      The p-value measures how unusual a difference this large would be if:
    </p>

    13

    <p>
      were actually true.
    </p>

    <p>
      Small p-values indicate evidence that the population means differ.
    </p>

    <h2>Confidence Interval Connection</h2>

    <p>
      The corresponding confidence interval is:
    </p>

    14

    <p>
      This interval estimates plausible values for:
    </p>

    15

    <h2>Interpreting the Confidence Interval</h2>

    <p>
      If:
    </p>

    16

    <p>
      is outside the interval,
      the corresponding hypothesis test rejects:
    </p>

    17

    <p>
      at the matching significance level.
    </p>

    <h2>Assumptions</h2>

    <p>
      The two-sample t test assumes:
    </p>

    <ul class="bullets">

      <li>Random sampling</li>

      <li>Independent observations within groups</li>

      <li>Independent groups</li>

      <li>Approximately normal populations or sufficiently large samples</li>

    </ul>

    <h2>Paired vs Independent Samples</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Paired t Test</th>
            <th>Two-Sample t Test</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Matched observations</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Independent groups</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Parameter tested</td>
            <td>μd</td>
            <td>μ₁ − μ₂</td>
          </tr>

          <tr>
            <td>Analyzes differences directly</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      The two-sample t test is one of the most important procedures in statistics because many scientific questions involve comparing two independent groups.
    </p>

    <p>
      The test extends the one-sample t framework by incorporating uncertainty from two separate samples and evaluating differences between population means.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The two-sample t test evaluates whether two independent population means differ. It compares the observed difference in sample means to the amount of variability expected from random sampling.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Not all research questions involve means.
    </p>

    <p>
      Many studies focus on proportions, such as approval rates, success rates, or disease prevalence.
    </p>

    <p>
      The next lesson introduces the one-proportion Z test, the standard procedure for testing population proportions.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The two-sample t test compares two independent population means</li>

        <li>The parameter of interest is μ₁ − μ₂</li>

        <li>The null hypothesis usually states μ₁ − μ₂ = 0</li>

        <li>Welch's t test is commonly preferred in practice</li>

        <li>The test statistic compares the observed difference to its standard error</li>

        <li>Independent groups are required</li>

        <li>Confidence intervals estimate plausible values for μ₁ − μ₂</li>

        <li>The procedure is widely used in experimental and observational research</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/paired-t-test/">
         ← Previous: Paired t Test
      </a>

      <a class="btn"
         href="/inference/classical-tests/one-proportion-z-test/">
         Next: One-Proportion Z Test →
      </a>

    </div>

  </div>

</section>