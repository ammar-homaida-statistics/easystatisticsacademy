---
layout: default
title: One-Sample t Test for a Mean
description: Learn how the one-sample t test evaluates whether a population mean differs from a hypothesized value when the population standard deviation is unknown.
permalink: /inference/classical-tests/one-sample-t-test-for-mean/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_classical_tests_lesson_v0";

  try {
  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/one-sample-t-test-for-mean/",
    label: "One-Sample t Test for a Mean",
    ts: Date.now()
  }));
  } catch (_) {
    // Disabled browser storage must not interrupt the lesson.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 4</span>
      <span class="badge">Classical Tests</span>
      <span class="badge">t Test</span>
    </div>

    <h1>One-Sample t Test for a Mean</h1>

    <p class="lead">
      The one-sample t test is one of the most widely used procedures in statistics.
    </p>

    <p class="lead">
      It evaluates whether a population mean differs from a hypothesized value when the population standard deviation is unknown.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/one-sample-z-test-for-mean/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/classical-tests/paired-t-test/">
         Next: Paired t Test →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Do We Need the t Test?</h2>

    <p>
      The Z test assumes the population standard deviation:
    </p>

    \[
\sigma
\]

    <p>
      is known.
    </p>

    <p>
      In real applications, this is rarely true.
    </p>

    <p>
      Instead, we estimate population variability using the sample standard deviation:
    </p>

    \[
s
\]

    <p>
      This additional uncertainty changes the sampling distribution and leads to the t test.
    </p>

    <h2>The Research Question</h2>

    <p>
      Suppose a university claims that students study an average of:
    </p>

    \[
\mu_0=20\ \text{hours/week}
\]

    <p>
      A researcher collects a sample and wants to determine whether the true population mean differs from this value.
    </p>

    <h2>When Is a One-Sample t Test Appropriate?</h2>

    <div class="concept-box">

      <strong>Use a one-sample t test when:</strong>

      <ul class="bullets">

        <li>The parameter of interest is a population mean.</li>

        <li>A single random sample is observed.</li>

        <li>The population standard deviation is unknown.</li>

        <li>Observations are independent.</li>

        <li>The population is approximately normal or the sample size is sufficiently large.</li>

      </ul>

    </div>

    <h2>The Hypotheses</h2>

    <p>
      The standard hypotheses are:
    </p>

    \[
H_0:\mu=\mu_0
\]

    <br><br>

    \[
H_1:\mu\ne\mu_0
\]

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>μ = population mean</li>

      <li>μ₀ = hypothesized value</li>

    </ul>

    <h2>Possible Alternatives</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Alternative Hypothesis</th>
            <th>Test Type</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>μ ≠ μ₀</td>
            <td>Two-sided</td>
          </tr>

          <tr>
            <td>μ &gt; μ₀</td>
            <td>Right-tailed</td>
          </tr>

          <tr>
            <td>μ &lt; μ₀</td>
            <td>Left-tailed</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Estimated Standard Error</h2>

    <p>
      Since σ is unknown, we estimate it using:
    </p>

    \[
\widehat{\operatorname{SE}}(\bar X)=\frac{s}{\sqrt{n}}
\]

    <p>
      This estimate introduces additional uncertainty.
    </p>

    <h2>The t Statistic</h2>

    <p>
      The test statistic becomes:
    </p>

    \[
t=\frac{\bar X-\mu_0}{s/\sqrt{n}}
\]

    <p>
      Just like the Z statistic, it measures how many standard errors separate the sample mean from the null value.
    </p>

    <h2>Why Not Use the Normal Distribution?</h2>

    <p>
      Because:
    </p>

    \[
\sigma
\]

    <p>
      is estimated from the sample, the exact null distribution under normal sampling has heavier tails than the standard normal distribution.
    </p>

    <p>
      Therefore, use the Student's t reference distribution when normal sampling is justified. For larger samples, an approximate t analysis can also be appropriate under regularity conditions.
    </p>

    <h2>The t Distribution</h2>

    <p>
      For independent observations from a normal population, the statistic follows a Student's t distribution with n − 1 degrees of freedom exactly under the null hypothesis. With nonnormal data it is an approximation that needs suitable conditions; n = 25 alone does not guarantee validity.
    </p>

    <p>
      Compared with the normal distribution, the t distribution has:
    </p>

    <ul class="bullets">

      <li>More spread</li>

      <li>Heavier tails</li>

      <li>Greater probability of extreme values</li>

    </ul>

    <h2>Degrees of Freedom</h2>

    <p>
      Every t distribution is identified by its degrees of freedom:
    </p>

    \[
\nu=n-1
\]

    <p>
      Different sample sizes produce different t distributions.
    </p>

    <h2>What Happens as Sample Size Increases?</h2>

    <p>
      Larger samples estimate variability more accurately.
    </p>

    <p>
      Consequently:
    </p>

    <div class="concept-box">

      <strong>Important result:</strong>

      <p>
        As degrees of freedom increase, the t distribution approaches the standard normal distribution.
      </p>

    </div>

    <h2>Example Setup</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>μ₀ = 20</p>
      <p>x̄ = 18</p>
      <p>s = 4</p>
      <p>n = 25</p>
      <p>α = 0.05</p>

    </div>

    <h2>Step 1: Compute the Standard Error</h2>

    <p>
      Using:
    </p>

    \[
\widehat{\operatorname{SE}}(\bar X)=\frac{s}{\sqrt{n}}
\]

    <p>
      gives:
    </p>

    \[
\widehat{\operatorname{SE}}(\bar X)=\frac{4}{\sqrt{25}}=0.8
\]

    <h2>Step 2: Compute the t Statistic</h2>

    <p>
      Substitute into the formula:
    </p>

    \[
t=\frac{18-20}{4/\sqrt{25}}=\frac{-2}{0.8}
\]

    <p>
      Therefore:
    </p>

    \[
t=-2.5
\]

    <h2>Step 3: Determine Degrees of Freedom</h2>

    <p>
      Using:
    </p>

    \[
\nu=n-1
\]

    <p>
      gives:
    </p>

    \[
\nu=25-1=24
\]

    <h2>Step 4: Compute the p-Value</h2>

    <p>
      Using the t distribution with:
    </p>

    \[
\nu=24
\]

    <p>
      the two-sided p-value is approximately:
    </p>

    <div class="example-box">

      <p>
        p ≈ 0.01965
      </p>
    </div>

    <h2>Step 5: Make the Decision</h2>

    <p>
      Compare:
    </p>

    <div class="example-box">

      <p>p ≈ 0.01965</p>
      <p>α = 0.05</p>

    </div>

    <p>
      Since:
    </p>

    \[
p\approx0.01965<\alpha=0.05
\]

    <p>
      we reject:
    </p>

    \[
H_0
\]

    <h2>Step 6: Interpret the Result</h2>

    <p>
      Statistical conclusion:
    </p>

    <div class="example-box">

      <p>
        Reject the null hypothesis.
      </p>
    </div>

    <p>
      Practical conclusion:
    </p>

    <div class="example-box">

      <p>
        The sample provides evidence that the population mean differs from 20 hours per week.
      </p>
    </div>

    <h2>Critical Values and the t Distribution</h2>

    <p>
      The critical values depend on both:
    </p>

    <ul class="bullets">

      <li>Significance level</li>

      <li>Degrees of freedom</li>

    </ul>

    <p>
      Unlike the Z test, there is no single universal critical value.
    </p>

    <h2>Confidence Interval Connection</h2>

    <p>
      The corresponding confidence interval is:
    </p>

    \[
\bar X\pm t_{1-\alpha/2,n-1}\frac{s}{\sqrt{n}}
\]

    <p>
      where:
    </p>

    \[
t_{1-\alpha/2,n-1}\ \text{is the t critical value with }n-1\text{ degrees of freedom}
\]

    <p>
      comes from the t distribution.
    </p>

    <p>
      As with all classical tests, the standard two-sided one-sample t test and this t interval produce matching decisions at corresponding confidence levels under the same assumptions. Here, using t₀.₉₇₅,₂₄ ≈ 2.0639 gives a 95% interval of approximately [16.35, 19.65] hours/week; 20 is excluded.
    </p>

    <h2>Assumptions Revisited</h2>

    <p>
      The one-sample t test assumes:
    </p>

    <ul class="bullets">

      <li>Random sampling</li>

      <li>Independent observations</li>

      <li>Approximately normal population or sufficiently large sample</li>

      <li>No severe violations affecting inference</li>

    </ul>

    <h2>Z Test vs t Test</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Z Test</th>
            <th>t Test</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Population σ known</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Uses sample s</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Distribution used</td>
            <td>Normal</td>
            <td>t Distribution</td>
          </tr>

          <tr>
            <td>Common in practice</td>
            <td>Rare</td>
            <td>Very common</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      The one-sample t test extends the logic of the Z test to realistic situations where population variability is unknown.
    </p>

    <p>
      By accounting for uncertainty in the estimated standard deviation, it provides valid inference for a much broader range of practical applications.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The one-sample t test evaluates whether a population mean differs from a hypothesized value when the population standard deviation is unknown. It replaces σ with the sample standard deviation and uses the t distribution to account for the resulting uncertainty.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Many studies collect observations in naturally matched pairs.
    </p>

    <p>
      Examples include before-and-after measurements, repeated observations on the same subject, and matched experimental designs.
    </p>

    <p>
      The next lesson introduces the paired t test, which analyzes differences within paired observations.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The one-sample t test is used when σ is unknown</li>

        <li>The standard error is estimated using s/√n</li>

        <li>The test statistic is t = (x̄ − μ₀)/(s/√n)</li>

        <li>The t distribution accounts for uncertainty in estimating σ</li>

        <li>Degrees of freedom equal n − 1</li>

        <li>The t distribution approaches the normal distribution as sample size increases</li>

        <li>The t test is far more common in practice than the Z test</li>

        <li>Confidence intervals and t tests are closely connected</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/one-sample-z-test-for-mean/">
         ← Previous: One-Sample Z Test for a Mean
      </a>

      <a class="btn"
         href="/inference/classical-tests/paired-t-test/">
         Next: Paired t Test →
      </a>

    </div>

  </div>

</section>