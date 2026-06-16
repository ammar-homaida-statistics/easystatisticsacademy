---
layout: default
title: What Makes a Good Estimator?
description: Learn the key properties statisticians use to evaluate estimators, including unbiasedness, consistency, efficiency, and precision.
permalink: /inference/foundations/what-makes-good-estimator/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_foundations_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/foundations/what-makes-good-estimator/",
    label: "What Makes a Good Estimator?",
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
      <span class="badge">Estimator Quality</span>
    </div>

    <h1>What Makes a Good Estimator?</h1>

    <p class="lead">
      Estimators are the workhorses of statistical inference.
    </p>

    <p class="lead">
      Some estimators provide reliable information about population parameters, while others can be inaccurate, unstable, or inefficient. Understanding what makes an estimator good is essential for sound statistical practice.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/foundations/bias-and-variance-intuition/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/foundations/inference-pipeline-estimator-se-ci-test/">
         Next: Inference Pipeline →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Not All Estimators Are Equal</h2>

    <p>
      Multiple estimators may exist for the same population parameter.
    </p>

    <p>
      For example,
      several different formulas could be proposed to estimate a population mean or variance.
    </p>

    <p>
      The question becomes:
    </p>

    <div class="example-box">

      <p>
        Which estimator should we trust?
      </p>

    </div>

    <p>
      Statistical theory provides criteria for answering that question.
    </p>

    <h2>The Goal of an Estimator</h2>

    <p>
      A good estimator should provide values that are:
    </p>

    <ul class="bullets">

      <li>Accurate</li>

      <li>Stable</li>

      <li>Reliable</li>

      <li>Informative</li>

    </ul>

    <p>
      Several formal properties help evaluate whether an estimator achieves these goals.
    </p>

    <h2>Property 1: Unbiasedness</h2>

    <p>
      One of the most important properties is unbiasedness.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        An estimator is unbiased if its expected value equals the true population parameter.
      </p>

    </div>

    <p>
      Mathematically:
    </p>

    0

    <h2>Why Unbiasedness Matters</h2>

    <p>
      An unbiased estimator is centered on the correct target.
    </p>

    <p>
      Across repeated samples,
      it neither systematically overestimates nor underestimates the parameter.
    </p>

    <div class="example-box">

      <p>
        Average estimate = True parameter
      </p>

    </div>

    <h2>Unbiased Does Not Mean Perfect</h2>

    <p>
      An estimator can be unbiased yet still produce wildly varying estimates.
    </p>

    <p>
      Therefore unbiasedness alone is not sufficient.
    </p>

    <p>
      We must also consider variability.
    </p>

    <h2>Property 2: Low Variance</h2>

    <p>
      A good estimator should not fluctuate excessively across samples.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Low variance means estimates remain relatively stable under repeated sampling.
      </p>

    </div>

    <p>
      Smaller variance leads to smaller standard errors.
    </p>

    <p>
      Smaller standard errors lead to more precise inference.
    </p>

    <h2>Why Variance Matters</h2>

    <p>
      Imagine two unbiased estimators.
    </p>

    <p>
      One varies dramatically from sample to sample.
    </p>

    <p>
      The other stays close to the true value.
    </p>

    <p>
      Most statisticians would prefer the more stable estimator.
    </p>

    <h2>Property 3: Consistency</h2>

    <p>
      Consistency concerns what happens as sample size increases.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A consistent estimator converges toward the true parameter as sample size grows.
      </p>

    </div>

    <p>
      Informally:
    </p>

    <div class="example-box">

      <p>
        More data → Better estimates
      </p>

    </div>

    <p>
      Most commonly used estimators are designed to be consistent.
    </p>

    <h2>The Law of Large Numbers Connection</h2>

    <p>
      Consistency is closely connected to the Law of Large Numbers.
    </p>

    <p>
      As larger samples are collected,
      estimation error tends to decrease.
    </p>

    <p>
      The estimator becomes increasingly reliable.
    </p>

    <h2>Property 4: Efficiency</h2>

    <p>
      Suppose two estimators are both unbiased.
    </p>

    <p>
      Which should be preferred?
    </p>

    <p>
      Usually the one with smaller variance.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        An efficient estimator achieves lower variance than competing estimators.
      </p>

    </div>

    <h2>Efficiency in Practice</h2>

    <p>
      Efficient estimators extract more information from the same data.
    </p>

    <p>
      This leads to:
    </p>

    <ul class="bullets">

      <li>Narrower confidence intervals</li>

      <li>More powerful tests</li>

      <li>Greater precision</li>

    </ul>

    <h2>Property 5: Small Standard Error</h2>

    <p>
      Standard error summarizes estimator variability.
    </p>

    <p>
      Good estimators generally have smaller standard errors.
    </p>

    <div class="example-box">

      <p>
        Smaller SE → More precise estimates
      </p>

      <p>
        Larger SE → Less precise estimates
      </p>

    </div>

    <h2>Bias and Variance Together</h2>

    <p>
      Good estimation requires balancing bias and variance.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Estimator Type</th>
            <th>Quality</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Low Bias + Low Variance</td>
            <td>Excellent</td>
          </tr>

          <tr>
            <td>Low Bias + High Variance</td>
            <td>Unstable</td>
          </tr>

          <tr>
            <td>High Bias + Low Variance</td>
            <td>Consistently Wrong</td>
          </tr>

          <tr>
            <td>High Bias + High Variance</td>
            <td>Poor</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Ideal Estimator</h2>

    <p>
      An ideal estimator would be:
    </p>

    <ul class="bullets">

      <li>Unbiased</li>

      <li>Consistent</li>

      <li>Efficient</li>

      <li>Low variance</li>

      <li>Small standard error</li>

    </ul>

    <p>
      In practice,
      no estimator is perfect,
      but many perform very well.
    </p>

    <h2>A Familiar Example</h2>

    <p>
      The sample mean:
    </p>

    1

    <p>
      is widely used because it possesses several desirable properties.
    </p>

    <ul class="bullets">

      <li>Unbiased for μ</li>

      <li>Consistent</li>

      <li>Generally efficient under common assumptions</li>

    </ul>

    <p>
      This explains its central role in statistics.
    </p>

    <h2>How Good Estimators Improve Inference</h2>

    <p>
      Better estimators lead to:
    </p>

    <ul class="bullets">

      <li>Better confidence intervals</li>

      <li>More reliable hypothesis tests</li>

      <li>More accurate conclusions</li>

      <li>Improved decision making</li>

    </ul>

    <p>
      Much of statistical theory focuses on developing and evaluating estimators.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Statistical inference depends on using sample information to learn about unknown parameters.
    </p>

    <p>
      The quality of those conclusions depends heavily on the quality of the estimators involved.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Good estimators are centered correctly, stable across samples, improve with more data, and provide precise information about unknown parameters.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      We now have all the foundational pieces:
    </p>

    <ul class="bullets">

      <li>Parameters</li>

      <li>Estimators</li>

      <li>Sampling distributions</li>

      <li>Standard errors</li>

      <li>Estimator quality</li>

    </ul>

    <p>
      The next lesson combines these ideas into a complete inferential workflow that connects estimation, uncertainty, confidence intervals, and hypothesis testing.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Good estimators provide reliable information about population parameters</li>

        <li>Unbiased estimators are centered on the true parameter</li>

        <li>Low variance produces stable estimates</li>

        <li>Consistent estimators improve as sample size increases</li>

        <li>Efficient estimators achieve lower variance than alternatives</li>

        <li>Small standard errors imply greater precision</li>

        <li>Both bias and variance influence estimator quality</li>

        <li>Estimator quality directly affects inferential conclusions</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/foundations/bias-and-variance-intuition/">
         ← Previous: Bias and Variance Intuition
      </a>

      <a class="btn"
         href="/inference/foundations/inference-pipeline-estimator-se-ci-test/">
         Next: Inference Pipeline →
      </a>

    </div>

  </div>

</section>