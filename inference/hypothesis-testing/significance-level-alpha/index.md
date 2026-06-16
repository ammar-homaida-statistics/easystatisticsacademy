---
layout: default
title: Significance Level (α)
description: Learn what the significance level represents, why it is chosen before analyzing data, and how it guides hypothesis-testing decisions.
permalink: /inference/hypothesis-testing/significance-level-alpha/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_hypothesis_testing_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/hypothesis-testing/significance-level-alpha/",
    label: "Significance Level (α)",
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
      <span class="badge">Decision Rules</span>
    </div>

    <h1>Significance Level (α)</h1>

    <p class="lead">
      A p-value measures evidence against the null hypothesis, but evidence alone does not produce a decision.
    </p>

    <p class="lead">
      To make decisions consistently, statisticians choose a significance level that determines how much evidence is required before rejecting the null hypothesis.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/hypothesis-testing/p-value-meaning/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/type1-type2-errors/">
         Next: Type I and Type II Errors →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why a Decision Rule Is Needed</h2>

    <p>
      Suppose a study produces:
    </p>

    <div class="example-box">

      <p>
        p = 0.08
      </p>
    </div>

    <p>
      Is that small enough to reject the null hypothesis?
    </p>

    <p>
      Different people might answer differently.
    </p>

    <p>
      To avoid subjective decisions,
      hypothesis testing uses a predefined threshold.
    </p>

    <h2>The Significance Level</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        The significance level is a predetermined probability threshold used to decide whether the evidence against the null hypothesis is strong enough to reject it.
      </p>

    </div>

    <p>
      It is denoted by:
    </p>

    0

    <h2>The Basic Decision Rule</h2>

    <p>
      After computing a p-value:
    </p>

    <div class="concept-box">

      <strong>Decision Rule:</strong>

      <p>
        Reject H₀ if p ≤ α.
      </p>

      <p>
        Fail to reject H₀ if p > α.
      </p>

    </div>

    <p>
      This rule is the foundation of classical hypothesis testing.
    </p>

    <h2>The Most Common Choice</h2>

    <p>
      In many fields,
      the standard choice is:
    </p>

    1

    <p>
      This convention became widespread through historical statistical practice.
    </p>

    <p>
      Although common,
      it is not a universal law.
    </p>

    <h2>Other Common Significance Levels</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>α</th>
            <th>Usage</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>0.10</td>
            <td>More lenient evidence standard</td>
          </tr>

          <tr>
            <td>0.05</td>
            <td>Most common default</td>
          </tr>

          <tr>
            <td>0.01</td>
            <td>Stricter evidence requirement</td>
          </tr>

          <tr>
            <td>0.001</td>
            <td>Very strong evidence required</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Interpreting α</h2>

    <p>
      The significance level is chosen before examining the data.
    </p>

    <p>
      It specifies how willing we are to risk incorrectly rejecting a true null hypothesis.
    </p>

    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        α controls the long-run probability of falsely rejecting a true null hypothesis.
      </p>

    </div>

    <h2>An Example Decision</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        α = 0.05
      </p>

      <p>
        p = 0.03
      </p>

    </div>

    <p>
      Since:
    </p>

    2

    <p>
      we reject the null hypothesis.
    </p>

    <p>
      The data provide sufficient evidence according to the chosen standard.
    </p>

    <h2>Another Example</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        α = 0.05
      </p>

      <p>
        p = 0.18
      </p>

    </div>

    <p>
      Since:
    </p>

    3

    <p>
      we fail to reject the null hypothesis.
    </p>

    <p>
      The sample does not provide sufficiently strong evidence against H₀.
    </p>

    <h2>Reject vs Fail to Reject</h2>

    <p>
      Hypothesis testing uses very specific language.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Decision</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Reject H₀</td>
            <td>Evidence against H₀ is sufficiently strong</td>
          </tr>

          <tr>
            <td>Fail to Reject H₀</td>
            <td>Evidence against H₀ is insufficient</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Notice that we never say:
    </p>

    <div class="example-box">

      <p>
        “Accept H₀”
      </p>
    </div>

    <p>
      because lack of evidence against H₀ does not prove it is true.
    </p>

    <h2>The Relationship Between Confidence Intervals and α</h2>

    <p>
      Confidence intervals and hypothesis tests are closely connected.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Confidence Level</th>
            <th>Equivalent α</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>90%</td>
            <td>0.10</td>
          </tr>

          <tr>
            <td>95%</td>
            <td>0.05</td>
          </tr>

          <tr>
            <td>99%</td>
            <td>0.01</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      In many situations:
    </p>

    <div class="example-box">

      <p>
        A null value outside a 95% confidence interval corresponds to rejection at α = 0.05.
      </p>
    </div>

    <h2>Why Not Always Use a Tiny α?</h2>

    <p>
      A very small significance level reduces false rejections.
    </p>

    <p>
      However,
      it also makes it harder to detect real effects.
    </p>

    <p>
      There is a tradeoff between caution and sensitivity.
    </p>

    <div class="concept-box">

      <strong>Tradeoff:</strong>

      <p>
        Smaller α decreases false alarms but increases the chance of missing real effects.
      </p>

    </div>

    <h2>Scientific Context Matters</h2>

    <p>
      Different fields often choose different significance levels.
    </p>

    <div class="example-box">

      <p>
        Medical studies may require stricter evidence.
      </p>

      <p>
        Exploratory research may tolerate a larger α.
      </p>

    </div>

    <p>
      The consequences of making errors influence the choice.
    </p>

    <h2>What α Does Not Mean</h2>

    <p>
      The significance level is often misunderstood.
    </p>

    <h3>Incorrect Interpretation</h3>

    <div class="example-box">

      <p>
        “α is the probability that H₀ is true.”
      </p>
    </div>

    <p>
      This is false.
    </p>

    <p>
      The significance level concerns decision errors,
      not probabilities assigned to hypotheses.
    </p>

    <h2>The Long-Run Perspective</h2>

    <p>
      Imagine repeating the same study thousands of times when the null hypothesis is actually true.
    </p>

    <p>
      If:
    </p>

    4

    <p>
      then approximately 5% of those studies would incorrectly reject H₀.
    </p>

    <p>
      This repeated-sampling interpretation is fundamental.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      The p-value measures evidence.
    </p>

    <p>
      The significance level provides a decision threshold.
    </p>

    <p>
      Together they transform uncertainty into a formal statistical decision process.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The significance level α is a predefined evidence threshold that controls how much evidence is required before rejecting the null hypothesis. It determines the long-run risk of falsely rejecting a true null hypothesis.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Hypothesis-testing decisions can sometimes be wrong.
    </p>

    <p>
      We may reject a true null hypothesis or fail to reject a false one.
    </p>

    <p>
      The next lesson introduces Type I and Type II errors, the two fundamental kinds of mistakes in statistical decision-making.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The significance level is denoted by α</li>

        <li>α is chosen before examining the data</li>

        <li>Reject H₀ when p ≤ α</li>

        <li>Fail to reject H₀ when p > α</li>

        <li>α = 0.05 is the most common choice</li>

        <li>α controls the long-run probability of falsely rejecting a true H₀</li>

        <li>Smaller α requires stronger evidence</li>

        <li>Confidence intervals and significance tests are closely connected</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/p-value-meaning/">
         ← Previous: p-Value Meaning
      </a>

      <a class="btn"
         href="/inference/hypothesis-testing/type1-type2-errors/">
         Next: Type I and Type II Errors →
      </a>

    </div>

  </div>

</section>