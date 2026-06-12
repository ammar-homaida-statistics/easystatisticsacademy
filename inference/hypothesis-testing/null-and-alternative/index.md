---
layout: default
title: Null and Alternative Hypotheses
description: Learn how null and alternative hypotheses are formulated and why they form the foundation of statistical hypothesis testing.
permalink: /inference/hypothesis-testing/null-and-alternative/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_hypothesis_testing_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/hypothesis-testing/null-and-alternative/",
    label: "Null and Alternative Hypotheses",
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
      <span class="badge">Foundations</span>
    </div>

    <h1>Null and Alternative Hypotheses</h1>

    <p class="lead">
      Every hypothesis test begins with two competing statements about a population.
    </p>

    <p class="lead">
      These statements formalize the claim being evaluated and the competing explanation suggested by the data.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/hypothesis-testing/what-is-a-hypothesis-test/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/test-statistic-standardization/">
         Next: Test Statistic and Standardization →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Need for Two Hypotheses</h2>

    <p>
      Hypothesis testing works by comparing two competing explanations for observed data.
    </p>

    <p>
      One explanation assumes that nothing unusual is happening.
    </p>

    <p>
      The other assumes that a meaningful effect or difference exists.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Every hypothesis test is a structured comparison between a default explanation and a competing explanation.
      </p>

    </div>

    <h2>The Null Hypothesis</h2>

    <div class="concept-box">

      <strong>Null Hypothesis:</strong>

      <p>
        The null hypothesis is the default claim that represents no effect, no difference, or no change.
      </p>

    </div>

    <p>
      It is denoted by:
    </p>

    0

    <p>
      The null hypothesis serves as the assumption under which the probability calculations of a hypothesis test are performed.
    </p>

    <h2>The Alternative Hypothesis</h2>

    <div class="concept-box">

      <strong>Alternative Hypothesis:</strong>

      <p>
        The alternative hypothesis represents the claim that an effect, difference, or relationship exists.
      </p>

    </div>

    <p>
      It is denoted by:
    </p>

    1

    <p>
      or sometimes:
    </p>

    2

    <p>
      The alternative represents the explanation supported when the data are sufficiently inconsistent with the null hypothesis.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose a manufacturer claims that a machine fills bottles with an average of:
    </p>

    3

    <p>
      The hypotheses might be:
    </p>

    4

    <br><br>

    5

    <p>
      Here the null states that the machine is operating correctly,
      while the alternative suggests that the average fill amount differs from the target.
    </p>

    <h2>Why Equality Appears in the Null</h2>

    <p>
      The null hypothesis always contains an equality statement.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Allowed in H₀</th>
            <th>Not Used Alone in H₀</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>=</td>
            <td>≠</td>
          </tr>

          <tr>
            <td>≤</td>
            <td>&gt;</td>
          </tr>

          <tr>
            <td>≥</td>
            <td>&lt;</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      This requirement allows probability calculations to be made under a specific assumption.
    </p>

    <h2>The Three Common Forms</h2>

    <p>
      Alternative hypotheses usually take one of three forms.
    </p>

    <h3>Two-Sided Alternative</h3>

    <p>
      Tests whether the parameter differs in either direction.
    </p>

    6

    <br><br>

    7

    <h3>Right-Tailed Alternative</h3>

    <p>
      Tests whether the parameter is larger than the null value.
    </p>

    8

    <br><br>

    9

    <h3>Left-Tailed Alternative</h3>

    <p>
      Tests whether the parameter is smaller than the null value.
    </p>

    10

    <br><br>

    11

    <h2>Choosing the Alternative</h2>

    <p>
      The research question determines the alternative hypothesis.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Research Question</th>
            <th>Alternative Form</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Different?</td>
            <td>≠</td>
          </tr>

          <tr>
            <td>Greater?</td>
            <td>&gt;</td>
          </tr>

          <tr>
            <td>Smaller?</td>
            <td>&lt;</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Another Example: Election Polling</h2>

    <p>
      Suppose a candidate needs more than 50% support to win.
    </p>

    <p>
      The hypotheses might be:
    </p>

    12

    <br><br>

    13

    <p>
      The alternative directly reflects the question of interest.
    </p>

    <h2>The Legal-System Analogy</h2>

    <p>
      A common analogy compares hypothesis testing to a courtroom.
    </p>

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
            <td>Null hypothesis</td>
            <td>Presumption of innocence</td>
          </tr>

          <tr>
            <td>Alternative hypothesis</td>
            <td>Claim of guilt</td>
          </tr>

          <tr>
            <td>Data</td>
            <td>Evidence</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The burden of evidence falls on overturning the default assumption.
    </p>

    <h2>Failing to Reject Is Not Accepting</h2>

    <p>
      One of the most important ideas in hypothesis testing is:
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Failing to reject the null hypothesis does not prove the null hypothesis is true.
      </p>

    </div>

    <p>
      It only means that the sample did not provide strong enough evidence against it.
    </p>

    <h2>Why We Start With the Null</h2>

    <p>
      Statistical tests calculate probabilities assuming:
    </p>

    14

    <p>
      is true.
    </p>

    <p>
      The entire testing framework is built around evaluating whether the observed data are unusually inconsistent with that assumption.
    </p>

    <h2>Hypotheses and Parameters</h2>

    <p>
      Hypotheses are statements about population parameters,
      not sample statistics.
    </p>

    <div class="example-box">

      <p>
        Correct: μ = 100
      </p>

      <p>
        Correct: p = 0.40
      </p>

      <p>
        Incorrect: x̄ = 100
      </p>

      <p>
        Incorrect: p̂ = 0.40
      </p>

    </div>

    <p>
      The goal is to learn about populations using sample data.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Null and alternative hypotheses define the competing explanations in a hypothesis test.
    </p>

    <p>
      Once these hypotheses are specified,
      the next step is measuring how far the observed data depart from the null hypothesis.
    </p>

    <p>
      That measurement is called a test statistic.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Every hypothesis test compares a null hypothesis representing a default claim against an alternative hypothesis representing a competing explanation. The evidence in the data determines whether the null remains plausible.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Hypotheses define what is being tested,
      but they do not tell us how unusual the data are.
    </p>

    <p>
      To quantify evidence,
      statisticians convert observed results into standardized measures called test statistics.
    </p>

    <p>
      The next lesson introduces test statistics and the idea of standardization.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Every hypothesis test involves a null and alternative hypothesis</li>

        <li>The null hypothesis represents the default claim</li>

        <li>The alternative hypothesis represents a competing explanation</li>

        <li>The null hypothesis always contains an equality statement</li>

        <li>Alternatives may be two-sided, left-tailed, or right-tailed</li>

        <li>Hypotheses are statements about population parameters</li>

        <li>Failing to reject the null does not prove it is true</li>

        <li>The testing framework begins by assuming the null hypothesis is true</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/what-is-a-hypothesis-test/">
         ← Previous: What Is a Hypothesis Test?
      </a>

      <a class="btn"
         href="/inference/hypothesis-testing/test-statistic-standardization/">
         Next: Test Statistic and Standardization →
      </a>

    </div>

  </div>

</section>