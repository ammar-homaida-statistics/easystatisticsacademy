---
layout: default
title: One-Sided vs Two-Sided Tests
description: Learn the difference between one-sided and two-sided hypothesis tests, when each should be used, and how they affect statistical conclusions.
permalink: /inference/hypothesis-testing/one-sided-vs-two-sided/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_hypothesis_testing_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/hypothesis-testing/one-sided-vs-two-sided/",
    label: "One-Sided vs Two-Sided Tests",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 3</span>
      <span class="badge">Hypothesis Testing</span>
      <span class="badge">Test Design</span>
    </div>

    <h1>One-Sided vs Two-Sided Tests</h1>

    <p class="lead">
      Not all research questions ask the same thing.
    </p>

    <p class="lead">
      Some questions look for any difference from a null value, while others focus on a specific direction. This distinction determines whether a hypothesis test is one-sided or two-sided.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/hypothesis-testing/power-and-effect-size/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/ci-and-test-connection/">
         Next: Confidence Intervals and Tests →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Direction Matters</h2>

    <p>
      Consider a company launching a new manufacturing process.
    </p>

    <p>
      The company may ask:
    </p>

    <div class="example-box">

      <p>
        Has the average production output changed?
      </p>
    </div>

    <p>
      Or it may ask:
    </p>

    <div class="example-box">

      <p>
        Has the average production output increased?
      </p>
    </div>

    <p>
      These questions are not identical.
    </p>

    <p>
      The first looks for change in either direction.
    </p>

    <p>
      The second looks only for improvement.
    </p>

    <h2>The Two-Sided Test</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A two-sided test evaluates whether a parameter differs from the null value in either direction.
      </p>

    </div>

    <p>
      A typical two-sided hypothesis pair is:
    </p>

    
    \[
    H_0:\mu=\mu_0
    \]


    <br><br>

    
    \[
    H_a:\mu\ne\mu_0
    \]


    <p>
      The alternative hypothesis allows values above or below the null value.
    </p>

    <h2>What Counts as Evidence?</h2>

    <p>
      For a two-sided test,
      evidence against the null hypothesis can come from either direction.
    </p>

    <div class="example-box">

      <p>
        Sample mean much larger than 100
      </p>

      <p>
        Sample mean much smaller than 100
      </p>

    </div>

    <p>
      Both outcomes support the alternative hypothesis.
    </p>

    <h2>The One-Sided Test</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A one-sided test evaluates whether a parameter differs from the null value in a specific direction.
      </p>

    </div>

    <p>
      There are two forms of one-sided tests.
    </p>

    <h2>Right-Tailed Test</h2>

    <p>
      A right-tailed test looks for values larger than the null value.
    </p>

    
    \[
    H_0:\mu\le\mu_0
    \]


    <br><br>

    
    \[
    H_a:\mu>\mu_0
    \]


    <p>
      Only unusually large observations provide evidence against H₀.
    </p>

    <h2>Left-Tailed Test</h2>

    <p>
      A left-tailed test looks for values smaller than the null value.
    </p>

    
    \[
    H_0:\mu\ge\mu_0
    \]


    <br><br>

    
    \[
    H_a:\mu<\mu_0
    \]


    <p>
      Only unusually small observations provide evidence against H₀.
    </p>

    <h2>The Tail Concept</h2>

    <p>
      The term "tail" refers to extreme regions of a probability distribution.
    </p>

    <p>
      In a one-sided test,
      the rejection region is placed entirely in one tail.
    </p>

    <p>
      In a two-sided test,
      the rejection region is divided between both tails.
    </p>

    <h2>Visual Comparison</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Test Type</th>
            <th>Evidence Location</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Left-Tailed</td>
            <td>Lower tail only</td>
          </tr>

          <tr>
            <td>Right-Tailed</td>
            <td>Upper tail only</td>
          </tr>

          <tr>
            <td>Two-Sided</td>
            <td>Both tails</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>How p-Values Differ</h2>

    <p>
      Suppose a test statistic equals:
    </p>

    
    \[
    Z=z_{\mathrm{obs}}>0
    \]


    <p>
      For a <strong>prespecified standard normal z-test</strong>, the tail
      probabilities depend on which alternative was selected before seeing
      the result. Write Φ for the standard normal cumulative distribution
      function:
    </p>

    \[
    \begin{aligned}
    p_{\mathrm{right}}&=1-\Phi(z_{\mathrm{obs}}),\\
    p_{\mathrm{left}}&=\Phi(z_{\mathrm{obs}}),\\
    p_{\mathrm{two}}&=2\min\{\Phi(z_{\mathrm{obs}}),1-\Phi(z_{\mathrm{obs}})\}
    =2[1-\Phi(|z_{\mathrm{obs}}|)].
    \end{aligned}
    \]

    <p>
      For example, when z = 2, the right-tail p-value is approximately
      <strong>0.02275</strong>, the left-tail p-value is approximately
      <strong>0.97725</strong>, and the two-sided p-value is approximately
      <strong>0.04550</strong>. If a right-tailed alternative was specified
      in advance, a positive statistic agrees with that direction; a
      left-tailed alternative produces a large p-value for this same positive
      statistic.
    </p>

    <p>
      In this symmetric z-test, the two-sided p-value is twice the
      <em>smaller</em> one-sided tail probability. It is <strong>not</strong>
      necessarily twice the p-value of whichever one-sided alternative was
      selected. For asymmetric or discrete null distributions, two-sided
      p-values require a specified extremeness rule and cannot always be
      obtained by doubling a single tail.
    </p>

    <h2>Why One-Sided Tests Have More Power</h2>

    <p>
      Because all of the significance level:
    </p>

    
    \[
    \alpha
    \]


    <p>
      is placed in a single tail,
      one-sided tests can detect effects more easily in the specified direction.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        For fixed sample size and significance level, a one-sided test can have greater power for effects in its preselected direction, but can have much lower power for effects in the opposite direction.
      </p>

    </div>

    <h2>The Cost of a One-Sided Test</h2>

    <p>
      A one-sided test completely ignores evidence in the opposite direction.
    </p>

    <p>
      For example:
    </p>

    <div class="example-box">

      <p>
        Hₐ: μ > 100
      </p>
    </div>

    <p>
      Even an extremely small sample mean does not support this alternative.
    </p>

    <p>
      The test is not designed to detect decreases.
    </p>

    <h2>When Should a One-Sided Test Be Used?</h2>

    <p>
      A one-sided test is appropriate only when:
    </p>

    <ul class="bullets">

      <li>The research question is genuinely directional.</li>

      <li>The opposite direction is scientifically irrelevant.</li>

      <li>The direction is specified before data collection.</li>

    </ul>

    <h2>When Should a Two-Sided Test Be Used?</h2>

    <p>
      A two-sided test is generally preferred when:
    </p>

    <ul class="bullets">

      <li>Any departure from the null value matters.</li>

      <li>Either direction is possible.</li>

      <li>The direction is uncertain before data collection.</li>

    </ul>

    <p>
      For this reason,
      two-sided tests are the default in many scientific disciplines.
    </p>

    <h2>A Common Mistake</h2>

    <div class="example-box">

      <p>
        Examine the data first and then choose a one-sided test because the effect appears positive.
      </p>
    </div>

    <p>
      This practice is statistically invalid.
    </p>

    <p>
      The direction must be chosen before seeing the data.
    </p>

    <h2>Connection to Confidence Intervals</h2>

    <p>
      Two-sided hypothesis tests correspond naturally to two-sided confidence intervals.
    </p>

    <p>
      For example:
    </p>

    <div class="example-box">

      <p>
        95% confidence interval ↔ α = 0.05 two-sided test
      </p>
    </div>

    <p>
      This relationship becomes important in the next lesson.
    </p>

    <h2>Comparing the Approaches</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>One-Sided</th>
            <th>Two-Sided</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Tests one direction only</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Detects both directions</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Greater directional power</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Most common scientific default</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      One-sided and two-sided tests answer different scientific questions.
    </p>

    <p>
      Choosing the appropriate form requires understanding the research objective before analyzing data.
    </p>

    <p>
      The decision affects p-values, power, rejection regions, and interpretation.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Two-sided tests detect departures from the null hypothesis in either direction, while one-sided tests focus on a specific direction. The choice must be made before examining the data and should be driven by the research question.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Confidence intervals and hypothesis tests often appear as separate statistical tools.
    </p>

    <p>
      In reality,
      they are closely connected and frequently lead to identical conclusions.
    </p>

    <p>
      The next lesson explores the relationship between confidence intervals and hypothesis tests.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Two-sided tests look for differences in either direction</li>

        <li>One-sided tests look for differences in a specific direction</li>

        <li>Left-tailed and right-tailed tests are the two one-sided forms</li>

        <li>With a standard normal null, one-sided p-values depend on the preselected tail; the two-sided p-value uses both tails</li>

        <li>One-sided tests have greater power in the chosen direction</li>

        <li>One-sided tests ignore evidence in the opposite direction</li>

        <li>The choice of test must be made before observing the data</li>

        <li>Two-sided tests are the default in many scientific fields</li>

        <li>Confidence intervals and hypothesis tests are closely related</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/power-and-effect-size/">
         ← Previous: Power and Effect Size
      </a>

      <a class="btn"
         href="/inference/hypothesis-testing/ci-and-test-connection/">
         Next: Confidence Intervals and Tests →
      </a>

    </div>

  </div>

</section>