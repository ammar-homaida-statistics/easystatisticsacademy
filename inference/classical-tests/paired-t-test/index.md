---
layout: default
title: Paired t Test
description: Learn how the paired t test analyzes matched observations and evaluates whether the average difference between paired measurements is zero.
permalink: /inference/classical-tests/paired-t-test/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_classical_tests_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/paired-t-test/",
    label: "Paired t Test",
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
      <span class="badge">Matched Samples</span>
    </div>

    <h1>Paired t Test</h1>

    <p class="lead">
      Many studies collect observations in naturally linked pairs rather than from independent groups.
    </p>

    <p class="lead">
      The paired t test evaluates whether the average difference within those pairs is significantly different from zero.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/one-sample-t-test-for-mean/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/classical-tests/two-sample-t-test-independent/">
         Next: Two-Sample t Test (Independent Samples) →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Makes Data Paired?</h2>

    <p>
      In some studies, observations naturally come in matched pairs.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Before-and-after measurements on the same person</li>

      <li>Blood pressure measured before and after treatment</li>

      <li>Student scores before and after a training program</li>

      <li>Matched twins or matched subjects</li>

    </ul>

    <p>
      In these situations, observations are not independent.
    </p>

    <h2>The Key Idea</h2>

    <div class="concept-box">

      <strong>Core principle:</strong>

      <p>
        A paired t test converts paired observations into differences and then performs a one-sample t test on those differences.
      </p>

    </div>

    <p>
      The individual measurements are not analyzed directly.
    </p>

    <p>
      Instead, the differences become the data.
    </p>

    <h2>Constructing Differences</h2>

    <p>
      For each pair:
    </p>

    \[
D_i=Y_{i,\mathrm{after}}-Y_{i,\mathrm{before}}
\]

    <p>
      This creates a new sample consisting entirely of differences.
    </p>

    <h2>The Parameter of Interest</h2>

    <p>
      The paired t test focuses on:
    </p>

    \[
\mu_D=E[D_i]
\]

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>μ<sub>d</sub> = population mean difference</li>

    </ul>

    <p>
      The question becomes:
    </p>

    <div class="example-box">

      <p>
        Is the average difference equal to zero?
      </p>
    </div>

    <h2>The Hypotheses</h2>

    <p>
      The standard paired t test uses:
    </p>

    \[
H_0:\mu_D=0
\]

    <br><br>

    \[
H_1:\mu_D\ne0
\]

    <p>
      Zero corresponds to no average change.
    </p>

    <h2>Alternative Forms</h2>

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
            <td>μ<sub>d</sub> ≠ 0</td>
            <td>Any average change</td>
          </tr>

          <tr>
            <td>μ<sub>d</sub> &gt; 0</td>
            <td>Average increase</td>
          </tr>

          <tr>
            <td>μ<sub>d</sub> &lt; 0</td>
            <td>Average decrease</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Example Dataset</h2>

    <p>
      Suppose five individuals participate in a training program.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Person</th>
            <th>Before</th>
            <th>After</th>
            <th>Difference</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>1</td>
            <td>70</td>
            <td>75</td>
            <td>5</td>
          </tr>

          <tr>
            <td>2</td>
            <td>68</td>
            <td>72</td>
            <td>4</td>
          </tr>

          <tr>
            <td>3</td>
            <td>75</td>
            <td>79</td>
            <td>4</td>
          </tr>

          <tr>
            <td>4</td>
            <td>71</td>
            <td>74</td>
            <td>3</td>
          </tr>

          <tr>
            <td>5</td>
            <td>69</td>
            <td>74</td>
            <td>5</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The paired t test analyzes:
    </p>

    <div class="example-box">

      <p>
        5, 4, 4, 3, 5
      </p>
    </div>

    <p>
      rather than the before and after scores separately.
    </p>

    <h2>The Sample Mean Difference</h2>

    <p>
      Let:
    </p>

    \[
\bar D=\frac1n\sum_{i=1}^n D_i
\]

    <p>
      denote the sample mean difference.
    </p>

    <p>
      This measures the average change observed in the sample.
    </p>

    <p>For the five displayed paired changes (5, 4, 4, 3, 5), the mean change is <strong>4.2</strong> and the sample standard deviation of changes is <strong>√0.7 ≈ 0.8367</strong>. The test concerns the population mean of within-person differences, not two unpaired group means.</p>
    <h2>The Standard Error</h2>

    <p>
      The standard error of the mean difference is:
    </p>

    \[
\widehat{\operatorname{SE}}(\bar D)=\frac{s_D}{\sqrt n}
\]

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>s<sub>d</sub> = sample standard deviation of differences</li>

      <li>n = number of pairs</li>

    </ul>

    <h2>The Test Statistic</h2>

    <p>
      The paired t statistic is:
    </p>

    \[
t=\frac{\bar D-0}{s_D/\sqrt n}
\]

    <p>
      Since the null value is usually zero,
      the formula simplifies naturally.
    </p>

    <p>For the displayed sample, the standard error is 0.8367/√5 ≈ 0.3742, so the t statistic is about <strong>11.225</strong> under the zero-change null. The exact two-sided t(4) reference p-value is approximately <strong>0.00036</strong>, assuming the population of paired differences is normally distributed.</p>
    <h2>Degrees of Freedom</h2>

    <p>
      As with a one-sample t test:
    </p>

    \[
\nu=n-1
\]

    <p>
      where n represents the number of pairs.
    </p>

    <h2>Why Pairing Helps</h2>

    <p>
      Pairing often removes subject-to-subject variability.
    </p>

    <p>
      Each participant effectively serves as their own control.
    </p>

    <div class="concept-box">

      <strong>Benefit:</strong>

      <p>
        Paired designs often produce smaller variability and greater statistical power than independent-sample designs.
      </p>

    </div>

    <h2>When Should a Paired t Test Be Used?</h2>

    <p>
      Use a paired t test when observations are meaningfully linked.
    </p>

    <div class="example-box">

      <p>
        Before vs after treatment
      </p>

      <p>
        Same subject measured twice
      </p>

      <p>
        Matched individuals
      </p>

      <p>
        Repeated measurements
      </p>

    </div>

    <h2>When Should It Not Be Used?</h2>

    <p>
      If the two samples are unrelated,
      a paired t test is inappropriate.
    </p>

    <div class="example-box">

      <p>
        Comparing students from School A and School B
      </p>

      <p>
        Comparing independent treatment groups
      </p>

    </div>

    <p>
      Such situations require independent-sample procedures instead.
    </p>

    <h2>Assumptions</h2>

    <p>
      The paired t test assumes:
    </p>

    <ul class="bullets">

      <li>Pairs are meaningfully matched</li>

      <li>Differences are independent across pairs</li>

      <li>A normally distributed population of differences for exact small-sample t inference; a large-sample approximation may be used under suitable conditions</li>

      <li>Pairs are randomly sampled</li>

    </ul>

    <h2>Confidence Interval for Mean Difference</h2>

    <p>
      The corresponding confidence interval is:
    </p>

    \[
\bar D\pm t_{1-\alpha/2,\,n-1}\frac{s_D}{\sqrt n}
\]

    <p>
      This interval estimates plausible values for:
    </p>

    \[
\mu_D
\]

    <p>Applied to the five displayed pairs, the 95% Student-t interval is approximately <strong>[3.16, 5.24]</strong> for the mean after-minus-before change. This does not include zero.</p>
    <h2>Interpretation Example</h2>

    <p>
      For the five paired changes shown in the example above:
    </p>

    <div class="example-box">

      <p>
        Mean difference = 4.2
      </p>

      <p>
        two-sided p ≈ 0.00036 (for the five displayed pairs)
      </p>

    </div>

    <p>
      The conclusion is:
    </p>

    <div class="example-box">

      <p>
        There is strong evidence that the average change differs from zero.
      </p>
    </div>

    <p>
      The sign of the mean difference indicates whether the change is positive or negative.
    </p>

    <h2>Paired vs Independent Samples</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Paired t Test</th>
            <th>Independent t Test</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Observations linked?</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Analyzes differences?</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Uses one sample of differences?</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Groups independent?</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      The paired t test extends the one-sample t test by applying it to differences created from matched observations.
    </p>

    <p>
      By controlling for pair-specific variation, paired designs often achieve more precise and powerful inference.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        A paired t test evaluates whether the average difference within matched pairs equals zero. The test converts paired observations into a single sample of differences and then performs a one-sample t test on those differences.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Many studies compare two entirely separate groups rather than matched observations.
    </p>

    <p>
      Examples include treatment versus control groups and comparisons between distinct populations.
    </p>

    <p>
      The next lesson introduces the two-sample t test for independent samples.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Paired data consist of matched observations</li>

        <li>The paired t test analyzes differences within pairs</li>

        <li>The parameter of interest is the population mean difference μd</li>

        <li>The null hypothesis usually states μd = 0</li>

        <li>The test statistic uses the sample of differences</li>

        <li>Degrees of freedom equal n − 1 where n is the number of pairs</li>

        <li>Pairing often reduces variability and increases power</li>

        <li>The paired t test should only be used when observations are genuinely linked</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/one-sample-t-test-for-mean/">
         ← Previous: One-Sample t Test for a Mean
      </a>

      <a class="btn"
         href="/inference/classical-tests/two-sample-t-test-independent/">
         Next: Two-Sample t Test (Independent Samples) →
      </a>

    </div>

  </div>

</section>