---
layout: default
title: Chi-Square Test of Homogeneity
description: Learn how the chi-square test of homogeneity compares categorical distributions across multiple populations or groups.
permalink: /inference/classical-tests/chi-square-homogeneity-test/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_classical_tests_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/chi-square-homogeneity-test/",
    label: "Chi-Square Test of Homogeneity",
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
      <span class="badge">Categorical Comparisons</span>
    </div>

    <h1>Chi-Square Test of Homogeneity</h1>

    <p class="lead">
      Researchers often want to compare categorical distributions across multiple populations or groups.
    </p>

    <p class="lead">
      The chi-square test of homogeneity evaluates whether different populations share the same distribution of a categorical variable.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/chi-square-independence-test/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/classical-tests/one-way-anova-f-test/">
         Next: One-Way ANOVA and the F Test →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Research Question</h2>

    <p>
      Suppose a company surveys customers in three cities and records their preferred product category.
    </p>

    <p>
      The question is:
    </p>

    <div class="example-box">

      <p>
        Do customer preferences have the same distribution across all cities?
      </p>
    </div>

    <p>
      Similar questions appear throughout statistics.
    </p>

    <ul class="bullets">

      <li>Do political preferences differ across regions?</li>

      <li>Do treatment outcomes differ across hospitals?</li>

      <li>Do purchasing patterns differ across age groups?</li>

      <li>Do product preferences differ across countries?</li>

    </ul>

    <h2>What Does Homogeneity Mean?</h2>

    <div class="concept-box">

      <strong>Homogeneity:</strong>

      <p>
        Multiple populations are homogeneous if they share the same categorical distribution.
      </p>

    </div>

    <p>
      The test evaluates whether observed differences between groups are larger than expected from random sampling variation.
    </p>

    <h2>The Hypotheses</h2>

    <div class="example-box">

      <p>
        H₀: All populations have the same categorical distribution.
      </p>

      <p>
        Hₐ: At least one population has a different distribution.
      </p>

    </div>

    <p>
      The alternative does not identify which population differs.
    </p>

    <p>
      It only indicates that a difference exists somewhere.
    </p>

    <h2>Example Data</h2>

    <p>
      Suppose customer preferences are recorded in three cities.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>City</th>
            <th>Product A</th>
            <th>Product B</th>
            <th>Product C</th>
            <th>Total</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>City 1</td>
            <td>40</td>
            <td>35</td>
            <td>25</td>
            <td>100</td>
          </tr>

          <tr>
            <td>City 2</td>
            <td>30</td>
            <td>45</td>
            <td>25</td>
            <td>100</td>
          </tr>

          <tr>
            <td>City 3</td>
            <td>50</td>
            <td>30</td>
            <td>20</td>
            <td>100</td>
          </tr>

          <tr>
            <td>Total</td>
            <td>120</td>
            <td>110</td>
            <td>70</td>
            <td>300</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Observed Counts</h2>

    <p>
      The frequencies in the table are the observed counts:
    </p>

    0

    <p>
      These represent the actual data collected from the populations.
    </p>

    <h2>Expected Counts Under H₀</h2>

    <p>
      If all populations share the same distribution,
      expected counts are calculated using:
    </p>

    1

    <p>
      This formula is identical to the one used in the chi-square test of independence.
    </p>

    <h2>Example Expected Count</h2>

    <p>
      For City 1 and Product A:
    </p>

    2

    <p>
      Under homogeneity, 40 observations would be expected in that cell.
    </p>

    <h2>The Chi-Square Statistic</h2>

    <p>
      The test statistic is:
    </p>

    3

    <p>
      The sum is computed across all cells in the table.
    </p>

    <h2>What Does χ² Measure?</h2>

    <p>
      The chi-square statistic measures how far the observed distributions are from what would be expected if all populations shared the same categorical pattern.
    </p>

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
            <td>Groups appear similar</td>
          </tr>

          <tr>
            <td>Large</td>
            <td>Evidence that distributions differ</td>
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
      Larger values correspond to stronger evidence against homogeneity.
    </p>

    <h2>Degrees of Freedom</h2>

    <p>
      For a table with:
    </p>

    <ul class="bullets">

      <li>r populations (rows)</li>

      <li>c categories (columns)</li>

    </ul>

    <p>
      the degrees of freedom are:
    </p>

    5

    <h2>Example</h2>

    <p>
      For the example above:
    </p>

    <div class="example-box">

      <p>
        3 rows × 3 columns
      </p>
    </div>

    <p>
      therefore:
    </p>

    6

    <h2>The p-Value</h2>

    <p>
      After computing:
    </p>

    <ul class="bullets">

      <li>χ²</li>

      <li>Degrees of freedom</li>

    </ul>

    <p>
      the p-value is obtained from the chi-square distribution.
    </p>

    <p>
      Small p-values indicate evidence that the distributions differ.
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

    <h2>Interpreting a Rejection</h2>

    <p>
      Rejecting:
    </p>

    7

    <p>
      means the data provide evidence that at least one population has a different categorical distribution.
    </p>

    <p>
      Additional analysis may be required to identify where the differences occur.
    </p>

    <h2>Assumptions</h2>

    <ul class="bullets">

      <li>Independent random samples from each population</li>

      <li>Independent observations within samples</li>

      <li>Categorical outcomes</li>

      <li>Sufficiently large expected counts</li>

    </ul>

    <h2>Expected Count Guideline</h2>

    <p>
      A commonly used recommendation is:
    </p>

    <div class="example-box">

      <p>
        Expected counts should generally be at least 5.
      </p>
    </div>

    <p>
      This supports the validity of the chi-square approximation.
    </p>

    <h2>Homogeneity vs Independence</h2>

    <p>
      Mathematically, the chi-square test of homogeneity and the chi-square test of independence use identical calculations.
    </p>

    <p>
      The difference lies in the study design and research question.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Independence Test</th>
            <th>Homogeneity Test</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Research Question</td>
            <td>Are variables associated?</td>
            <td>Are distributions identical?</td>
          </tr>

          <tr>
            <td>Samples</td>
            <td>One population</td>
            <td>Multiple populations</td>
          </tr>

          <tr>
            <td>Calculations</td>
            <td>Same</td>
            <td>Same</td>
          </tr>

          <tr>
            <td>Degrees of Freedom</td>
            <td>Same formula</td>
            <td>Same formula</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Applications</h2>

    <div class="example-box">

      <p>
        Consumer preference comparisons
      </p>

      <p>
        Election results across regions
      </p>

      <p>
        Educational outcome comparisons
      </p>

      <p>
        Medical treatment comparisons
      </p>

      <p>
        Market-segmentation studies
      </p>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      The chi-square test of homogeneity provides a powerful framework for comparing categorical distributions across populations.
    </p>

    <p>
      It extends categorical-data analysis beyond single populations and allows researchers to investigate differences among groups.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The chi-square test of homogeneity evaluates whether multiple populations share the same categorical distribution. It compares observed counts to expected counts under the assumption of identical distributions and determines whether differences are larger than expected by chance.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Many research questions involve comparing more than two population means rather than categorical distributions.
    </p>

    <p>
      Performing multiple t tests becomes inefficient and increases error rates.
    </p>

    <p>
      The next lesson introduces one-way ANOVA and the F test, the standard method for comparing means across several groups simultaneously.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The test compares categorical distributions across multiple populations</li>

        <li>The null hypothesis states that all populations share the same distribution</li>

        <li>Expected counts use row totals, column totals, and the grand total</li>

        <li>The chi-square statistic measures overall discrepancy between observed and expected counts</li>

        <li>Degrees of freedom equal (r − 1)(c − 1)</li>

        <li>Small p-values suggest that distributions differ across populations</li>

        <li>The calculations are identical to the chi-square independence test</li>

        <li>The difference lies in the study design and research objective</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/chi-square-independence-test/">
         ← Previous: Chi-Square Test of Independence
      </a>

      <a class="btn"
         href="/inference/classical-tests/one-way-anova-f-test/">
         Next: One-Way ANOVA and the F Test →
      </a>

    </div>

  </div>

</section>