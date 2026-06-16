---
layout: default
title: Decision Framework and Assumptions
description: Learn the general workflow behind classical hypothesis tests and the assumptions required for valid statistical conclusions.
permalink: /inference/classical-tests/decision-framework-and-assumptions/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_classical_tests_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/decision-framework-and-assumptions/",
    label: "Decision Framework and Assumptions",
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
      <span class="badge">Foundations</span>
    </div>

    <h1>Decision Framework and Assumptions</h1>

    <p class="lead">
      Although many hypothesis tests exist, they all follow the same underlying decision framework.
    </p>

    <p class="lead">
      Before learning individual tests, it is important to understand the common workflow and the assumptions that make statistical conclusions trustworthy.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/">
         ← Block Home
      </a>

      <a class="btn btn-outline"
         href="/inference/classical-tests/one-sample-z-test-for-mean/">
         Next: One-Sample Z Test for a Mean →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Learn a General Framework?</h2>

    <p>
      The next lessons introduce several classical hypothesis tests.
    </p>

    <p>
      At first they may appear different,
      but most follow nearly identical logic.
    </p>

    <p>
      Understanding the common structure makes learning individual tests much easier.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Classical hypothesis tests differ mainly in their formulas. Their decision process is largely the same.
      </p>

    </div>

    <h2>The Universal Testing Workflow</h2>

    <p>
      Most hypothesis tests follow six major steps.
    </p>

    <ol>

      <li>Define the research question.</li>

      <li>State the hypotheses.</li>

      <li>Check assumptions.</li>

      <li>Compute a test statistic.</li>

      <li>Compute a p-value.</li>

      <li>Make a decision and interpret the result.</li>

    </ol>

    <h2>Step 1: Define the Research Question</h2>

    <p>
      Every statistical test begins with a substantive question.
    </p>

    <div class="example-box">

      <p>
        Is the mean different from a target value?
      </p>

      <p>
        Are two population means equal?
      </p>

      <p>
        Is a population proportion larger than 50%?
      </p>

      <p>
        Are two variables independent?
      </p>

    </div>

    <p>
      The question determines the appropriate test.
    </p>

    <h2>Step 2: State the Hypotheses</h2>

    <p>
      Next, formulate:
    </p>

    0

    <p>
      and:
    </p>

    1

    <p>
      The hypotheses translate the research question into statistical language.
    </p>

    <h2>Example</h2>

    <p>
      If a company claims its average bottle fill is:
    </p>

    2

    <p>
      then:
    </p>

    3

    <br><br>

    4

    <h2>Step 3: Check Assumptions</h2>

    <p>
      Every hypothesis test relies on assumptions.
    </p>

    <p>
      If important assumptions fail,
      conclusions may become unreliable.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        A statistically correct calculation can still produce misleading conclusions if assumptions are violated.
      </p>

    </div>

    <h2>Common Assumption Categories</h2>

    <ul class="bullets">

      <li>Random sampling</li>

      <li>Independence</li>

      <li>Normality (or large-sample approximation)</li>

      <li>Equal variances (for some tests)</li>

      <li>Adequate sample size</li>

    </ul>

    <h2>Random Sampling</h2>

    <p>
      Most inference procedures assume the sample represents the population fairly.
    </p>

    <p>
      Random sampling helps justify that assumption.
    </p>

    <div class="example-box">

      <p>
        Biased samples can produce biased conclusions regardless of sample size.
      </p>
    </div>

    <h2>Independence</h2>

    <p>
      Many statistical formulas assume observations do not influence one another.
    </p>

    <p>
      Independence is often justified through:
    </p>

    <ul class="bullets">

      <li>Random sampling</li>

      <li>Random assignment</li>

      <li>Appropriate study design</li>

    </ul>

    <h2>Normality</h2>

    <p>
      Some tests assume the underlying population is approximately normal.
    </p>

    <p>
      Others rely on the Central Limit Theorem when sample sizes are sufficiently large.
    </p>

    <div class="concept-box">

      <strong>Rule of thumb:</strong>

      <p>
        Larger samples generally make normal approximations more reliable.
      </p>

    </div>

    <h2>Step 4: Compute a Test Statistic</h2>

    <p>
      After assumptions are checked,
      the observed sample is compared to the null hypothesis.
    </p>

    <p>
      Most test statistics follow:
    </p>

    5

    <p>
      The statistic measures how far the data depart from the null hypothesis.
    </p>

    <h2>Step 5: Compute a p-Value</h2>

    <p>
      Once the test statistic is known,
      we calculate the probability of obtaining results at least as extreme under:
    </p>

    6

    <p>
      This probability is the p-value.
    </p>

    <h2>Step 6: Make a Decision</h2>

    <p>
      Compare:
    </p>

    <p>
      p-value and significance level:
    </p>

    7

    <div class="concept-box">

      <strong>Decision Rule:</strong>

      <p>
        Reject H₀ if p ≤ α.
      </p>

      <p>
        Fail to reject H₀ if p > α.
      </p>

    </div>

    <h2>Interpretation Comes Last</h2>

    <p>
      The statistical decision itself is not the final goal.
    </p>

    <p>
      Researchers must translate the result back into the original context.
    </p>

    <div class="example-box">

      <p>
        Statistical conclusion:
      </p>

      <p>
        Reject H₀.
      </p>

      <hr>

      <p>
        Practical conclusion:
      </p>

      <p>
        The data provide evidence that average bottle fills differ from 500 mL.
      </p>

    </div>

    <h2>The Role of Assumptions</h2>

    <p>
      Assumptions are often treated as a checklist,
      but they are more than that.
    </p>

    <p>
      Assumptions justify the probability calculations used to obtain p-values.
    </p>

    <p>
      Without them,
      the theoretical sampling distributions may no longer apply.
    </p>

    <h2>What Happens When Assumptions Fail?</h2>

    <p>
      Violations can lead to:
    </p>

    <ul class="bullets">

      <li>Incorrect p-values</li>

      <li>Incorrect confidence intervals</li>

      <li>Inflated Type I error rates</li>

      <li>Reduced statistical power</li>

    </ul>

    <h2>Different Tests, Same Logic</h2>

    <p>
      The specific formulas change across tests:
    </p>

    <ul class="bullets">

      <li>Z tests</li>

      <li>T tests</li>

      <li>Chi-square tests</li>

      <li>ANOVA</li>

      <li>Proportion tests</li>

    </ul>

    <p>
      But the decision framework remains remarkably similar.
    </p>

    <h2>A Quick Framework Summary</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Step</th>
            <th>Purpose</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>1</td>
            <td>Define question</td>
          </tr>

          <tr>
            <td>2</td>
            <td>State hypotheses</td>
          </tr>

          <tr>
            <td>3</td>
            <td>Check assumptions</td>
          </tr>

          <tr>
            <td>4</td>
            <td>Compute test statistic</td>
          </tr>

          <tr>
            <td>5</td>
            <td>Compute p-value</td>
          </tr>

          <tr>
            <td>6</td>
            <td>Make and interpret decision</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      Statistical tests are not isolated formulas.
    </p>

    <p>
      They are applications of a general inferential framework built on probability, sampling distributions, and uncertainty.
    </p>

    <p>
      Understanding this framework makes every subsequent test easier to learn and interpret.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Every classical hypothesis test follows the same basic process: define a question, state hypotheses, verify assumptions, compute a test statistic, calculate a p-value, and make a decision. Assumptions are essential because they justify the probability calculations behind the test.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      The first classical hypothesis test we will study is the one-sample Z test for a population mean.
    </p>

    <p>
      This test applies when population variability is known and serves as the foundation for many other inferential procedures.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Most hypothesis tests follow the same six-step workflow</li>

        <li>Research questions determine the appropriate test</li>

        <li>Hypotheses formalize competing explanations</li>

        <li>Assumptions justify probability calculations</li>

        <li>Test statistics measure departure from the null hypothesis</li>

        <li>p-values quantify evidence against H₀</li>

        <li>Decisions are based on comparing p-values to α</li>

        <li>Interpretation must connect statistical conclusions to the original problem</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/">
         ← Block Home
      </a>

      <a class="btn"
         href="/inference/classical-tests/one-sample-z-test-for-mean/">
         Next: One-Sample Z Test for a Mean →
      </a>

    </div>

  </div>

</section>