---
layout: default
title: Conditions — Normality, CLT, and Independence
description: Learn the assumptions required for confidence intervals and how normality, the Central Limit Theorem, and independence support valid inference.
permalink: /inference/confidence-intervals/conditions-normality-clt-independence/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_confidence_intervals_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/confidence-intervals/conditions-normality-clt-independence/",
    label: "Conditions — Normality, CLT, and Independence",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 2</span>
      <span class="badge">Confidence Intervals</span>
      <span class="badge">Assumptions</span>
    </div>

    <h1>Conditions — Normality, CLT, and Independence</h1>

    <p class="lead">
      Confidence interval formulas are only as trustworthy as the assumptions behind them.
    </p>

    <p class="lead">
      Before constructing an interval, statisticians must verify that the conditions supporting the sampling distribution are reasonably satisfied.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/ci-for-proportion/">
         Next: CI for a Proportion →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Conditions Matter</h2>

    <p>
      Confidence intervals rely on probability models.
    </p>

    <p>
      Those probability models describe how estimates behave under repeated sampling.
    </p>

    <p>
      If the assumptions are severely violated,
      the interval may no longer achieve its advertised confidence level.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        A confidence interval is only as reliable as the assumptions used to justify it.
      </p>

    </div>

    <h2>The Three Major Conditions</h2>

    <p>
      For confidence intervals involving means, three conditions are especially important:
    </p>

    <ul class="bullets">

      <li>Independence</li>

      <li>Normality</li>

      <li>The Central Limit Theorem (CLT)</li>

    </ul>

    <p>
      Together they justify the sampling distribution used by confidence interval formulas.
    </p>

    <h2>Condition 1: Independence</h2>

    <p>
      Statistical formulas assume observations provide separate pieces of information.
    </p>

    <div class="concept-box">

      <strong>Independence:</strong>

      <p>
        Knowing one observation should not substantially determine another observation.
      </p>

    </div>

    <p>
      Independence is often the most important assumption in statistical inference.
    </p>

    <h2>Why Independence Matters</h2>

    <p>
      Standard error formulas assume information accumulates as sample size increases.
    </p>

    <p>
      If observations are strongly dependent,
      the effective amount of information is smaller than the sample size suggests.
    </p>

    <p>
      Confidence intervals may become misleadingly narrow.
    </p>

    <h2>How Independence Is Often Achieved</h2>

    <p>
      Independence is commonly approximated through:
    </p>

    <ul class="bullets">

      <li>Random sampling</li>

      <li>Random assignment</li>

      <li>Large populations relative to sample size</li>

    </ul>

    <p>
      Proper study design is often the first defense against dependence problems.
    </p>

    <h2>The 10% Condition</h2>

    <p>
      When sampling without replacement,
      a common guideline is:
    </p>

    <div class="concept-box">

      <strong>10% Condition:</strong>

      <p>
        The sample size should be less than about 10% of the population size.
      </p>

    </div>

    <p>
      This helps justify treating observations as approximately independent.
    </p>

    <h2>Condition 2: Normality</h2>

    <p>
      Confidence intervals for means are built using distributions that assume approximate normality.
    </p>

    <p>
      The question becomes:
    </p>

    <div class="example-box">

      <p>
        Is the sampling distribution of the sample mean approximately normal?
      </p>

    </div>

    <h2>When the Population Is Normal</h2>

    <p>
      If the population itself is normally distributed,
      then the sample mean is normally distributed for every sample size.
    </p>

    <div class="concept-box">

      <strong>Important fact:</strong>

      <p>
        A normal population guarantees a normal sampling distribution of the mean.
      </p>

    </div>

    <h2>The Real-World Problem</h2>

    <p>
      Most real populations are not perfectly normal.
    </p>

    <p>
      They may be:
    </p>

    <ul class="bullets">

      <li>Skewed</li>

      <li>Heavy-tailed</li>

      <li>Multimodal</li>

      <li>Contain outliers</li>

    </ul>

    <p>
      Fortunately,
      another powerful result often rescues us.
    </p>

    <h2>Condition 3: The Central Limit Theorem</h2>

    <p>
      The Central Limit Theorem explains why confidence intervals work surprisingly well.
    </p>

    <div class="concept-box">

      <strong>CLT:</strong>

      <p>
        As sample size increases, the sampling distribution of the sample mean becomes approximately normal, regardless of the population shape.
      </p>

    </div>

    <h2>Why the CLT Is So Important</h2>

    <p>
      Without the CLT,
      confidence intervals would require normal populations much more often.
    </p>

    <p>
      With the CLT,
      many practical datasets become analyzable using standard inferential methods.
    </p>

    <h2>The Sample Size Effect</h2>

    <p>
      Larger samples generally make the CLT more effective.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Sample Size</th>
            <th>Normal Approximation</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Small</td>
            <td>May be poor</td>
          </tr>

          <tr>
            <td>Moderate</td>
            <td>Often reasonable</td>
          </tr>

          <tr>
            <td>Large</td>
            <td>Usually very good</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Is n = 30 a Magic Number?</h2>

    <p>
      Many introductory courses mention:
    </p>

    <div class="example-box">

      <p>
        n ≥ 30
      </p>

    </div>

    <p>
      as a rule of thumb.
    </p>

    <p>
      However,
      there is nothing magical about 30.
    </p>

    <p>
      The required sample size depends on the population shape.
    </p>

    <h2>When Smaller Samples Can Work</h2>

    <p>
      If the population is approximately normal,
      even small samples may support valid confidence intervals.
    </p>

    <div class="example-box">

      <p>
        n = 10
      </p>

      <p>
        n = 15
      </p>
    </div>

    <p>
      can sometimes be sufficient.
    </p>

    <h2>When Larger Samples May Be Needed</h2>

    <p>
      Highly skewed populations may require substantially larger samples before the CLT produces a good approximation.
    </p>

    <div class="example-box">

      <p>
        Strong right skew
      </p>

      <p>
        Extreme outliers
      </p>

      <p>
        Heavy tails
      </p>

    </div>

    <p>
      These situations demand extra caution.
    </p>

    <h2>The Role of Outliers</h2>

    <p>
      Outliers can strongly affect both:
    </p>

    <ul class="bullets">

      <li>The sample mean</li>

      <li>The sample standard deviation</li>

    </ul>

    <p>
      Because mean confidence intervals depend on both quantities,
      extreme observations deserve careful investigation.
    </p>

    <h2>A Practical Checklist</h2>

    <p>
      Before constructing a confidence interval for a mean, ask:
    </p>

    <ol>

      <li>Was the sample obtained reasonably randomly?</li>

      <li>Are observations approximately independent?</li>

      <li>Is the sample less than 10% of the population?</li>

      <li>Is the population approximately normal, or is the sample large enough for the CLT?</li>

      <li>Are there serious outliers or extreme skewness?</li>

    </ol>

    <h2>What Happens If Conditions Fail?</h2>

    <p>
      Violations do not automatically invalidate an interval.
    </p>

    <p>
      The impact depends on:
    </p>

    <ul class="bullets">

      <li>Severity of the violation</li>

      <li>Sample size</li>

      <li>Type of interval</li>

    </ul>

    <p>
      Some violations are minor.
      Others can substantially distort coverage probabilities.
    </p>

    <h2>Why Statisticians Check Assumptions First</h2>

    <p>
      Computing an interval is easy.
    </p>

    <p>
      Determining whether the interval is trustworthy is the harder task.
    </p>

    <p>
      Good statistical practice emphasizes assumption checking before interpretation.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Confidence intervals rely on sampling distributions.
    </p>

    <p>
      Independence supports valid standard errors.
    </p>

    <p>
      Normality and the CLT support the distributions used for critical values.
    </p>

    <p>
      Together these conditions make confidence interval procedures work as intended.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Reliable confidence intervals require approximately independent observations and an approximately normal sampling distribution, obtained through population normality, the Central Limit Theorem, or both.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      So far we have focused on confidence intervals for means.
    </p>

    <p>
      Another extremely common inferential task is estimating population proportions.
    </p>

    <p>
      The next lesson develops confidence intervals for proportions and shows how the same interval blueprint applies in a new setting.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Confidence intervals rely on assumptions</li>

        <li>Independence is essential for valid standard errors</li>

        <li>The 10% condition helps justify approximate independence</li>

        <li>Normal populations produce normal sampling distributions</li>

        <li>The Central Limit Theorem often justifies normal approximations</li>

        <li>Larger samples improve the CLT approximation</li>

        <li>Outliers and strong skewness require caution</li>

        <li>Assumption checking is a critical part of statistical inference</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/">
         ← Previous: CI for Mean (σ Unknown)
      </a>

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-proportion/">
         Next: CI for a Proportion →
      </a>

    </div>

  </div>

</section>