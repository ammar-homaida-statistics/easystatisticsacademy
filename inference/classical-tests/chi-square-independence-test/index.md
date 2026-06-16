---
layout: default
title: Chi-Square Test of Independence
description: Learn how the chi-square test of independence evaluates whether two categorical variables are associated.
permalink: /inference/classical-tests/chi-square-independence-test/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_classical_tests_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/chi-square-independence-test/",
    label: "Chi-Square Test of Independence",
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
      <span class="badge">Categorical Association</span>
    </div>

    <h1>Chi-Square Test of Independence</h1>

    <p class="lead">
      Many studies seek to determine whether two categorical variables are related.
    </p>

    <p class="lead">
      The chi-square test of independence evaluates whether an observed association between categorical variables is stronger than would be expected from random variation alone.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/chi-square-goodness-of-fit/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/classical-tests/chi-square-homogeneity-test/">
         Next: Chi-Square Test of Homogeneity →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Research Question</h2>

    <p>
      Suppose researchers collect data on:
    </p>

    <ul class="bullets">

      <li>Gender and product preference</li>

      <li>Smoking status and disease occurrence</li>

      <li>Education level and voting behavior</li>

      <li>Device type and website conversion</li>

    </ul>

    <p>
      The question becomes:
    </p>

    <div class="example-box">

      <p>
        Are these variables related?
      </p>
    </div>

    <p>
      This is the purpose of the chi-square test of independence.
    </p>

    <h2>What Does Independence Mean?</h2>

    <div class="concept-box">

      <strong>Independence:</strong>

      <p>
        Two variables are independent if knowledge of one variable provides no information about the other.
      </p>

    </div>

    <p>
      Under independence, category proportions remain the same across groups.
    </p>

    <h2>The Null and Alternative Hypotheses</h2>

    <div class="example-box">

      <p>
        H₀: The variables are independent.
      </p>

      <p>
        Hₐ: The variables are associated.
      </p>

    </div>

    <p>
      The test does not specify the nature of the association.
    </p>

    <p>
      It only evaluates whether evidence of a relationship exists.
    </p>

    <h2>Contingency Tables</h2>

    <p>
      Data are organized into a contingency table.
    </p>

    <p>
      Example:
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th></th>
            <th>Prefers A</th>
            <th>Prefers B</th>
            <th>Total</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Male</td>
            <td>40</td>
            <td>60</td>
            <td>100</td>
          </tr>

          <tr>
            <td>Female</td>
            <td>70</td>
            <td>30</td>
            <td>100</td>
          </tr>

          <tr>
            <td>Total</td>
            <td>110</td>
            <td>90</td>
            <td>200</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Observed Counts</h2>

    <p>
      The entries inside the table are the observed counts:
    </p>

    0

    <p>
      These are the actual frequencies recorded in the sample.
    </p>

    <h2>Expected Counts Under Independence</h2>

    <p>
      If the variables are independent, expected counts can be calculated from the row and column totals.
    </p>

    <p>
      The formula is:
    </p>

    1

    <h2>Example Expected Count</h2>

    <p>
      For the Male–Prefers A cell:
    </p>

    2

    <p>
      Under independence, we would expect 55 observations in that cell.
    </p>

    <h2>Observed vs Expected</h2>

    <p>
      The observed count was:
    </p>

    <div class="example-box">

      <p>
        40
      </p>
    </div>

    <p>
      The expected count was:
    </p>

    <div class="example-box">

      <p>
        55
      </p>
    </div>

    <p>
      This discrepancy contributes to the test statistic.
    </p>

    <h2>The Chi-Square Statistic</h2>

    <p>
      The test statistic is:
    </p>

    3

    <p>
      The sum is taken across every cell in the contingency table.
    </p>

    <h2>Interpreting χ²</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>χ² Value</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Small</td>
            <td>Observed counts close to independence expectations</td>
          </tr>

          <tr>
            <td>Large</td>
            <td>Evidence of association</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Chi-Square Distribution</h2>

    <p>
      Under:
    </p>

    4

    <p>
      the test statistic follows a chi-square distribution approximately.
    </p>

    <p>
      Larger χ² values produce smaller p-values.
    </p>

    <h2>Degrees of Freedom</h2>

    <p>
      For a contingency table with:
    </p>

    <ul class="bullets">

      <li>r rows</li>

      <li>c columns</li>

    </ul>

    <p>
      the degrees of freedom are:
    </p>

    5

    <h2>Example</h2>

    <p>
      For a:
    </p>

    <div class="example-box">

      <p>
        2 × 2 table
      </p>
    </div>

    <p>
      we have:
    </p>

    6

    <h2>The p-Value</h2>

    <p>
      Once:
    </p>

    <ul class="bullets">

      <li>χ² is computed</li>

      <li>Degrees of freedom are determined</li>

    </ul>

    <p>
      the p-value is obtained from the chi-square distribution.
    </p>

    <h2>Decision Rule</h2>

    <div class="concept-box">

      <strong>Decision Rule:</strong>

      <p>
        Reject H₀ if p ≤ α.
      </p>

      <p>
        Fail to reject H₀ if p > α.
      </p>

    </div>

    <h2>What Does Rejection Mean?</h2>

    <p>
      Rejecting:
    </p>

    7

    <p>
      means the data provide evidence that the variables are associated.
    </p>

    <p>
      It does not establish causation.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Association does not imply causation.
      </p>

    </div>

    <h2>Assumptions</h2>

    <ul class="bullets">

      <li>Random sampling</li>

      <li>Independent observations</li>

      <li>Categorical variables</li>

      <li>Sufficiently large expected counts</li>

    </ul>

    <h2>Expected Count Guideline</h2>

    <p>
      A common recommendation is:
    </p>

    <div class="example-box">

      <p>
        All expected counts should generally be at least 5.
      </p>
    </div>

    <p>
      This helps ensure a reliable chi-square approximation.
    </p>

    <h2>Applications</h2>

    <div class="example-box">

      <p>
        Marketing research
      </p>

      <p>
        Medical studies
      </p>

      <p>
        Social-science surveys
      </p>

      <p>
        Political polling
      </p>

      <p>
        User-behavior analysis
      </p>

    </div>

    <h2>Independence vs Goodness-of-Fit</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Goodness-of-Fit</th>
            <th>Independence Test</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Variables</td>
            <td>One</td>
            <td>Two</td>
          </tr>

          <tr>
            <td>Question</td>
            <td>Matches expected distribution?</td>
            <td>Variables associated?</td>
          </tr>

          <tr>
            <td>Expected counts from</td>
            <td>Hypothesized probabilities</td>
            <td>Row and column totals</td>
          </tr>

          <tr>
            <td>Table structure</td>
            <td>Single categorical variable</td>
            <td>Contingency table</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Measuring Association Strength</h2>

    <p>
      A significant chi-square result indicates that an association exists.
    </p>

    <p>
      However, significance alone does not describe the strength of the relationship.
    </p>

    <p>
      Additional measures such as Cramér's V are often used to quantify association strength.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      The chi-square test of independence is one of the most important methods for categorical data analysis.
    </p>

    <p>
      It allows researchers to investigate relationships between variables without requiring numerical measurements.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The chi-square test of independence evaluates whether two categorical variables are associated. It compares observed counts to the counts expected under independence and determines whether discrepancies are larger than expected by chance.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      The chi-square test of independence analyzes association within a single population.
    </p>

    <p>
      A closely related procedure compares categorical distributions across multiple populations or groups.
    </p>

    <p>
      The next lesson introduces the chi-square test of homogeneity.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The test evaluates whether two categorical variables are independent</li>

        <li>Data are organized in contingency tables</li>

        <li>Expected counts are computed from row and column totals</li>

        <li>The chi-square statistic measures discrepancies between observed and expected counts</li>

        <li>Degrees of freedom equal (r − 1)(c − 1)</li>

        <li>Rejecting H₀ suggests an association exists</li>

        <li>Association does not imply causation</li>

        <li>The test is widely used across social sciences, medicine, business, and public policy</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/chi-square-goodness-of-fit/">
         ← Previous: Chi-Square Goodness-of-Fit Test
      </a>

      <a class="btn"
         href="/inference/classical-tests/chi-square-homogeneity-test/">
         Next: Chi-Square Test of Homogeneity →
      </a>

    </div>

  </div>

</section>