---
layout: default
title: Confidence Interval for a Mean (σ Known) — z Interval
description: Learn how to construct and interpret a confidence interval for a population mean when the population standard deviation is known.
permalink: /inference/confidence-intervals/ci-for-mean-sigma-known-z/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_confidence_intervals_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/confidence-intervals/ci-for-mean-sigma-known-z/",
    label: "Confidence Interval for a Mean (σ Known) — z Interval",
    ts: Date.now()
  }));
  } catch (_) {
    // Gracefully continue when the browser denies persistent storage.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 2</span>
      <span class="badge">Confidence Intervals</span>
      <span class="badge">Mean Estimation</span>
    </div>

    <h1>Confidence Interval for a Mean (σ Known) — z Interval</h1>

    <p class="lead">
      This is the classic confidence interval for estimating a population mean when the population standard deviation is known.
    </p>

    <p class="lead">
      Although this situation is uncommon in practice, it provides the foundation for understanding many other confidence intervals.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/confidence-intervals/critical-values-z-and-t/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/">
         Next: CI for Mean (σ Unknown) →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Problem</h2>

    <p>
      Suppose we want to estimate an unknown population mean:
    </p>

    
    \[
    \mu
    \]


    <p>
      using a random sample.
    </p>

    <p>
      We observe a sample mean,
      but because samples vary,
      the estimate is uncertain.
    </p>

    <p>
      A confidence interval helps quantify that uncertainty.
    </p>

    <h2>The Key Assumption</h2>

    <p>
      This method assumes the population standard deviation is known:
    </p>

    
    \[
    \sigma\ \text{known}
    \]


    <p>
      This assumption is rare in real applications,
      but it greatly simplifies the mathematics.
    </p>

    <h2>Why the z Distribution Is Used</h2>

    <p>
      Knowing σ determines the standard error but <strong>does not by itself make the sample mean normally distributed</strong>. If independent observations come from a normal population with known positive σ, the standardized mean has an exact standard normal distribution at every sample size.
    </p>

    <p>
      For independent, identically distributed observations from a nonnormal population with finite positive variance, a sufficiently accurate Central Limit Theorem approximation may instead justify using normal critical values. The resulting coverage is then approximate, not automatically exact.
    </p>

    <h2>The Standard Error of the Mean</h2>

    <p>
      For the mean of <strong>n independent observations with common variance σ²</strong>:
    </p>

    
    \[
    \bar X=\frac{1}{n}\sum_{i=1}^{n}X_i
    \]


    <p>
      the standard error is:
    </p>

    
    \[
    \operatorname{SE}(\bar X)=\frac{\sigma}{\sqrt n}
    \]


    <p>
      This measures the typical variability of sample means across repeated samples.
    </p>

    <h2>The Confidence Interval Formula</h2>

    <p>
      Applying the confidence interval blueprint:
    </p>

    
    \[
    \bar x\pm z_{1-\alpha/2}\frac{\sigma}{\sqrt n}
    \]


    <p>
      This is the two-sided z confidence interval for a population mean. Its stated confidence level is exact under the independent normal-population model with known σ (using the unrounded critical value); under a justified large-sample normal approximation, coverage is only approximate.
    </p>

    <h2>Understanding the Components</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Symbol</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>x̄</td>
            <td>Sample mean</td>
          </tr>

          <tr>
            <td>z*</td>
            <td>Critical value</td>
          </tr>

          <tr>
            <td>σ</td>
            <td>Population standard deviation</td>
          </tr>

          <tr>
            <td>n</td>
            <td>Sample size</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Common z Critical Values</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Confidence Level</th>
            <th>z*</th>
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

    <h2>Example Setup</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        Sample mean = 50
      </p>

      <p>
        Population standard deviation = 12
      </p>

      <p>
        Sample size = 36
      </p>

      <p>
        Confidence level = 95%
      </p>

    </div>

    <h2>Step 1: Compute the Standard Error</h2>

    <p>
      Using:
    </p>

    
    \[
    \operatorname{SE}(\bar X)=\frac{\sigma}{\sqrt n}
    \]


    <p>
      we obtain:
    </p>

    
    \[
    \operatorname{SE}(\bar X)=\frac{12}{\sqrt{36}}=2
    \]


    <h2>Step 2: Find the Critical Value</h2>

    <p>
      For a 95% confidence interval:
    </p>

    <div class="example-box">

      <p>
        z* = 1.96
      </p>

    </div>

    <h2>Step 3: Compute the Margin of Error</h2>

    <p>
      Margin of error:
    </p>

    
    \[
    \operatorname{ME}=z_{0.975}\operatorname{SE}=1.96(2)=3.92
    \]


    <h2>Step 4: Construct the Interval</h2>

    <p>
      Therefore:
    </p>

    
    \[
    [\,50-3.92,\ 50+3.92\,]=[\,46.08,\ 53.92\,]
    \]


    <p>
      giving:
    </p>

    <div class="example-box">

      <p>
        (46.08, 53.92)
      </p>

    </div>

    <h2>Interpreting the Result</h2>

    <p>
      A correct interpretation is:
    </p>

    <div class="example-box">

      <p>
        In this worked example, the normal-population model with known σ gives a procedure with 95% repeated-sampling coverage using the exact z critical value; with the rounded 1.96 used here, coverage is approximately 95%. For other populations, a normal approximation requires additional assumptions.
      </p>

    </div>

    <p>
      The interval suggests plausible values for the population mean lie between 46.08 and 53.92.
    </p>

    <h2>What Affects Interval Width?</h2>

    <p>
      The width depends on:
    </p>

    <ul class="bullets">

      <li>Confidence level</li>

      <li>Population variability</li>

      <li>Sample size</li>

    </ul>

    <h2>Effect of Confidence Level</h2>

    <p>
      Increasing confidence increases the critical value.
    </p>

    <p>
      Larger critical values produce wider intervals.
    </p>

    <div class="example-box">

      <p>
        99% confidence → wider interval than 95%
      </p>
    </div>

    <h2>Effect of Population Variability</h2>

    <p>
      Larger values of σ increase the standard error.
    </p>

    <p>
      Larger standard errors create wider intervals.
    </p>

    <div class="example-box">

      <p>
        More variability → more uncertainty
      </p>
    </div>

    <h2>Effect of Sample Size</h2>

    <p>
      Increasing sample size reduces:
    </p>

    
    \[
    \operatorname{SE}(\bar X)=\frac{\sigma}{\sqrt n}\ \propto\ n^{-1/2}
    \]


    <p>
      and therefore narrows the interval.
    </p>

    <div class="example-box">

      <p>
        Larger sample → smaller SE → narrower interval
      </p>
    </div>

    <h2>When Is This Method Valid?</h2>

    <p>
      The z interval for a mean is appropriate when:
    </p>

    <ul class="bullets">

      <li>The relevant population standard deviation σ is known and positive</li>

      <li>Observations follow a suitable sampling design; the usual σ/√n formula assumes independent observations with common variance</li>

      <li><strong>Exact normal-model case:</strong> independent normally distributed observations with common μ and σ²</li>

      <li><strong>Approximate case:</strong> for example, independent identically distributed observations with finite positive variance and a sample size large enough that the normal approximation is accurate for the population shape</li>

    </ul>

    <p>
      Distinguish the two justifications:
    </p>

    <ul class="bullets">

      <li>A normal population makes the sample mean normal at any sample size in the usual independent model.</li>

      <li>The CLT supplies only asymptotic normality for a nonnormal population; the familiar <em>n = 30</em> shortcut is not a universal guarantee.</li>

    </ul>

    <h2>Why This Method Is Rare in Practice</h2>

    <p>
      Real-world analysts almost never know the exact population standard deviation.
    </p>

    <p>
      Instead,
      σ must be estimated from the sample.
    </p>

    <p>
      That additional uncertainty requires a different interval.
    </p>

    <h2>The Historical Importance of the z Interval</h2>

    <p>
      Although rarely used directly,
      the z interval introduces the key ideas behind confidence intervals:
    </p>

    <ul class="bullets">

      <li>Estimate</li>

      <li>Standard error</li>

      <li>Critical value</li>

      <li>Margin of error</li>

    </ul>

    <p>
      Nearly all future confidence intervals follow the same structure.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        With known positive σ and a justified normal sampling distribution (exact or approximate), use the sample mean, a z critical value and the standard error σ/√n. Knowing σ alone is insufficient to justify exact coverage.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      In real applications,
      population variability is usually unknown.
    </p>

    <p>
      To handle this additional uncertainty,
      statisticians replace σ with the sample standard deviation and use the t distribution.
    </p>

    <p>
      The next lesson introduces the confidence interval for a mean when σ is unknown.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The z interval estimates a population mean with known σ <strong>and</strong> a justified exact or approximate normal sampling distribution</li>

        <li>The standard error equals σ/√n</li>

        <li>The interval formula is x̄ ± z*SE</li>

        <li>95% confidence corresponds to z* = 1.96</li>

        <li>Larger confidence levels create wider intervals</li>

        <li>Larger sample sizes create narrower intervals</li>

        <li>Larger population variability creates wider intervals</li>

        <li>The z interval provides the foundation for more realistic t intervals</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/critical-values-z-and-t/">
         ← Previous: Critical Values — z and t
      </a>

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/">
         Next: CI for Mean (σ Unknown) →
      </a>

    </div>

  </div>

</section>