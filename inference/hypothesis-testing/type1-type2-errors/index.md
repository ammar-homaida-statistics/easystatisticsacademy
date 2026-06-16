---
layout: default
title: Type I and Type II Errors
description: Learn the two fundamental mistakes possible in hypothesis testing and how they shape statistical decision-making.
permalink: /inference/hypothesis-testing/type1-type2-errors/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_hypothesis_testing_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/hypothesis-testing/type1-type2-errors/",
    label: "Type I and Type II Errors",
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
      <span class="badge">Decision Errors</span>
    </div>

    <h1>Type I and Type II Errors</h1>

    <p class="lead">
      Hypothesis testing provides a structured decision process, but no statistical decision rule is perfect.
    </p>

    <p class="lead">
      Because decisions are based on samples rather than entire populations, mistakes can occur. Understanding these mistakes is central to statistical inference.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/hypothesis-testing/significance-level-alpha/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/power-and-effect-size/">
         Next: Power and Effect Size →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Errors Are Unavoidable</h2>

    <p>
      Hypothesis tests make decisions using incomplete information.
    </p>

    <p>
      We observe a sample, not an entire population.
    </p>

    <p>
      Because samples vary randomly,
      a statistical decision can occasionally be wrong.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Even a perfectly designed hypothesis test can make mistakes because random sampling variability is unavoidable.
      </p>

    </div>

    <h2>The Two Possible Realities</h2>

    <p>
      In truth, only one of two situations can exist:
    </p>

    <ul class="bullets">

      <li>The null hypothesis is true.</li>

      <li>The null hypothesis is false.</li>

    </ul>

    <p>
      However, we do not know which situation is correct.
    </p>

    <h2>The Two Possible Decisions</h2>

    <p>
      A hypothesis test can produce one of two decisions:
    </p>

    <ul class="bullets">

      <li>Reject H₀</li>

      <li>Fail to reject H₀</li>

    </ul>

    <p>
      Combining realities and decisions creates four possible outcomes.
    </p>

    <h2>The Decision Table</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Reality</th>
            <th>Reject H₀</th>
            <th>Fail to Reject H₀</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>H₀ True</td>
            <td>Type I Error</td>
            <td>Correct Decision</td>
          </tr>

          <tr>
            <td>H₀ False</td>
            <td>Correct Decision</td>
            <td>Type II Error</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Two outcomes are correct decisions.
    </p>

    <p>
      Two outcomes are errors.
    </p>

    <h2>Type I Error</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A Type I error occurs when a true null hypothesis is rejected.
      </p>

    </div>

    <p>
      In simple language:
    </p>

    <div class="example-box">

      <p>
        Detecting an effect that does not actually exist.
      </p>

    </div>

    <h2>Examples of Type I Errors</h2>

    <div class="example-box">

      <p>
        Concluding a drug works when it actually does not.
      </p>

      <p>
        Concluding a manufacturing process changed when it actually did not.
      </p>

      <p>
        Concluding a website redesign improved conversions when it actually had no effect.
      </p>

    </div>

    <h2>The Probability of a Type I Error</h2>

    <p>
      The significance level directly controls the probability of a Type I error.
    </p>

    0

    <p>
      For example:
    </p>

    <div class="example-box">

      <p>
        α = 0.05
      </p>
    </div>

    <p>
      implies a long-run Type I error rate of approximately 5%.
    </p>

    <h2>Type II Error</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A Type II error occurs when a false null hypothesis is not rejected.
      </p>

    </div>

    <p>
      In simple language:
    </p>

    <div class="example-box">

      <p>
        Missing a real effect that actually exists.
      </p>

    </div>

    <h2>Examples of Type II Errors</h2>

    <div class="example-box">

      <p>
        Concluding a drug does not work when it actually does.
      </p>

      <p>
        Missing a real safety problem in a manufacturing process.
      </p>

      <p>
        Concluding two teaching methods are equivalent when one truly performs better.
      </p>

    </div>

    <h2>The Probability of a Type II Error</h2>

    <p>
      The probability of a Type II error is denoted by:
    </p>

    1

    <p>
      Unlike α,
      β depends on several factors:
    </p>

    <ul class="bullets">

      <li>Sample size</li>

      <li>Variability</li>

      <li>Effect size</li>

      <li>Significance level</li>

    </ul>

    <h2>Why Type II Errors Are Harder</h2>

    <p>
      Type I errors are easy to define because they assume the null hypothesis is true.
    </p>

    <p>
      Type II errors depend on how false the null hypothesis is.
    </p>

    <p>
      Therefore their probability varies across situations.
    </p>

    <h2>A Medical Testing Example</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Statistical Decision</th>
            <th>Medical Analogy</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Type I Error</td>
            <td>Healthy patient diagnosed as sick</td>
          </tr>

          <tr>
            <td>Type II Error</td>
            <td>Sick patient diagnosed as healthy</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Both mistakes can be costly,
      but the consequences differ.
    </p>

    <h2>The Tradeoff Between Errors</h2>

    <p>
      Reducing one type of error often increases the other.
    </p>

    <p>
      For example,
      lowering:
    </p>

    2

    <p>
      makes rejection more difficult.
    </p>

    <p>
      This reduces Type I errors but may increase Type II errors.
    </p>

    <div class="concept-box">

      <strong>Tradeoff:</strong>

      <p>
        Making false alarms less likely often makes missed detections more likely.
      </p>

    </div>

    <h2>Why Sample Size Helps</h2>

    <p>
      Increasing sample size often improves decision quality.
    </p>

    <p>
      Larger samples reduce uncertainty and make real effects easier to detect.
    </p>

    <p>
      As a result:
    </p>

    <ul class="bullets">

      <li>Type II error rates often decrease.</li>

      <li>Statistical power often increases.</li>

    </ul>

    <h2>The Courtroom Analogy Revisited</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Statistics</th>
            <th>Courtroom Analogy</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Type I Error</td>
            <td>Convicting an innocent person</td>
          </tr>

          <tr>
            <td>Type II Error</td>
            <td>Acquitting a guilty person</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Society often designs legal systems to make Type I errors extremely rare,
      even if that increases Type II errors.
    </p>

    <p>
      Different applications may prioritize different error types.
    </p>

    <h2>Which Error Is Worse?</h2>

    <p>
      There is no universal answer.
    </p>

    <p>
      The consequences depend on context.
    </p>

    <div class="example-box">

      <p>
        Drug approval may prioritize minimizing Type I errors.
      </p>

      <p>
        Disease screening may prioritize minimizing Type II errors.
      </p>

      <p>
        Fraud detection systems may balance both.
      </p>

    </div>

    <h2>The Relationship to Statistical Power</h2>

    <p>
      The probability of correctly detecting a false null hypothesis is called power.
    </p>

    <p>
      Power is directly related to Type II error:
    </p>

    3

    <p>
      This relationship becomes a major topic in the next lesson.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Hypothesis testing is fundamentally a decision-making process under uncertainty.
    </p>

    <p>
      Type I and Type II errors define the risks associated with those decisions.
    </p>

    <p>
      Understanding these risks helps researchers design studies and interpret results responsibly.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        A Type I error occurs when a true null hypothesis is rejected. A Type II error occurs when a false null hypothesis is not rejected. Statistical inference balances the risks of these two kinds of mistakes.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Type II errors describe missed discoveries.
    </p>

    <p>
      Researchers often want to know how likely a study is to detect a real effect when one exists.
    </p>

    <p>
      That probability is called statistical power.
    </p>

    <p>
      The next lesson introduces power, effect size, and the factors that influence a study's ability to detect meaningful effects.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Hypothesis tests can make two kinds of errors</li>

        <li>A Type I error rejects a true null hypothesis</li>

        <li>A Type II error fails to reject a false null hypothesis</li>

        <li>The probability of a Type I error equals α</li>

        <li>The probability of a Type II error is denoted by β</li>

        <li>Reducing one error type often increases the other</li>

        <li>Sample size can reduce Type II errors</li>

        <li>Statistical power equals 1 − β</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/significance-level-alpha/">
         ← Previous: Significance Level (α)
      </a>

      <a class="btn"
         href="/inference/hypothesis-testing/power-and-effect-size/">
         Next: Power and Effect Size →
      </a>

    </div>

  </div>

</section>