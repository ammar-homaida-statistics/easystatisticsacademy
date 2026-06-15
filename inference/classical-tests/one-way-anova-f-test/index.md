---
layout: default
title: One-Way ANOVA and the F Test
description: Learn how one-way ANOVA compares the means of three or more groups and uses the F statistic to determine whether meaningful differences exist.
permalink: /inference/classical-tests/one-way-anova-f-test/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_classical_tests_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/one-way-anova-f-test/",
    label: "One-Way ANOVA and the F Test",
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
      <span class="badge">ANOVA</span>
    </div>

    <h1>One-Way ANOVA and the F Test</h1>

    <p class="lead">
      Researchers often need to compare the means of three or more groups simultaneously.
    </p>

    <p class="lead">
      One-way Analysis of Variance (ANOVA) provides a systematic way to determine whether at least one population mean differs from the others.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/chi-square-homogeneity-test/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/">
         Next: Post-Hoc Tests and Multiple Comparisons →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Problem with Multiple t Tests</h2>

    <p>
      Suppose researchers compare average exam scores from:
    </p>

    <ul class="bullets">

      <li>Teaching Method A</li>

      <li>Teaching Method B</li>

      <li>Teaching Method C</li>

      <li>Teaching Method D</li>

    </ul>

    <p>
      One possible approach is performing many pairwise t tests.
    </p>

    <p>
      However, repeated testing increases the probability of making at least one Type I error.
    </p>

    <div class="concept-box">

      <strong>Key motivation:</strong>

      <p>
        ANOVA allows comparison of multiple means while controlling the overall false-positive rate.
      </p>

    </div>

    <h2>What Does ANOVA Mean?</h2>

    <p>
      ANOVA stands for:
    </p>

    <div class="example-box">

      <p>
        Analysis of Variance
      </p>
    </div>

    <p>
      Although the goal is comparing means, the method works by analyzing sources of variation in the data.
    </p>

    <h2>The Research Question</h2>

    <p>
      Suppose there are:
    </p>

    0

    <p>
      populations with means:
    </p>

    1

    <p>
      We want to determine whether all means are equal.
    </p>

    <h2>The Hypotheses</h2>

    <p>
      The null hypothesis is:
    </p>

    2

    <p>
      The alternative hypothesis is:
    </p>

    <div class="example-box">

      <p>
        Hₐ: At least one population mean differs.
      </p>
    </div>

    <p>
      Notice that ANOVA does not identify which mean differs.
    </p>

    <p>
      It only tests whether evidence of any difference exists.
    </p>

    <h2>The Core Idea</h2>

    <p>
      ANOVA compares two sources of variability:
    </p>

    <ul class="bullets">

      <li>Variation between group means</li>

      <li>Variation within groups</li>

    </ul>

    <p>
      If group means differ substantially relative to within-group variation, evidence against the null hypothesis increases.
    </p>

    <h2>Between-Group Variation</h2>

    <p>
      Between-group variation measures how far group means are from the overall mean.
    </p>

    <p>
      Large between-group variation suggests population means may differ.
    </p>

    <h2>Within-Group Variation</h2>

    <p>
      Within-group variation measures natural variability among observations inside each group.
    </p>

    <p>
      This variation is expected even when all population means are equal.
    </p>

    <h2>The ANOVA Logic</h2>

    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        If between-group variation is much larger than within-group variation, the observed group differences are unlikely to be explained by random sampling alone.
      </p>

    </div>

    <h2>The F Statistic</h2>

    <p>
      ANOVA summarizes this comparison using:
    </p>

    3

    <p>
      The F statistic is a ratio of variances.
    </p>

    <h2>Interpreting F</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>F Value</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Near 1</td>
            <td>Evidence consistent with equal means</td>
          </tr>

          <tr>
            <td>Moderately large</td>
            <td>Some evidence of differences</td>
          </tr>

          <tr>
            <td>Very large</td>
            <td>Strong evidence against H₀</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Example Dataset</h2>

    <p>
      Suppose average scores are observed for three teaching methods.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Group</th>
            <th>Sample Mean</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>A</td>
            <td>72</td>
          </tr>

          <tr>
            <td>B</td>
            <td>81</td>
          </tr>

          <tr>
            <td>C</td>
            <td>85</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      ANOVA evaluates whether these observed differences are larger than expected from random sampling variation.
    </p>

    <h2>The ANOVA Table</h2>

    <p>
      Results are commonly summarized in an ANOVA table.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Source</th>
            <th>SS</th>
            <th>df</th>
            <th>MS</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Between Groups</td>
            <td>SSB</td>
            <td>k − 1</td>
            <td>MSB</td>
          </tr>

          <tr>
            <td>Within Groups</td>
            <td>SSW</td>
            <td>N − k</td>
            <td>MSW</td>
          </tr>

          <tr>
            <td>Total</td>
            <td>SST</td>
            <td>N − 1</td>
            <td>—</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Degrees of Freedom</h2>

    <p>
      ANOVA uses two degrees-of-freedom values:
    </p>

    <ul class="bullets">

      <li>Numerator: k − 1</li>

      <li>Denominator: N − k</li>

    </ul>

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>k = number of groups</li>

      <li>N = total sample size</li>

    </ul>

    <h2>The F Distribution</h2>

    <p>
      Under:
    </p>

    4

    <p>
      the test statistic follows an F distribution.
    </p>

    <p>
      The F distribution:
    </p>

    <ul class="bullets">

      <li>Is always positive</li>

      <li>Is right-skewed</li>

      <li>Depends on two degrees-of-freedom values</li>

    </ul>

    <h2>The p-Value</h2>

    <p>
      Once the F statistic is computed, the p-value is obtained from the F distribution.
    </p>

    <p>
      Large F values produce small p-values.
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

    5

    <p>
      means the data provide evidence that at least one population mean differs.
    </p>

    <p>
      ANOVA alone does not reveal which groups differ.
    </p>

    <h2>Assumptions</h2>

    <p>
      One-way ANOVA assumes:
    </p>

    <ul class="bullets">

      <li>Independent observations</li>

      <li>Random sampling</li>

      <li>Approximately normal populations</li>

      <li>Equal population variances across groups</li>

    </ul>

    <h2>Why Equal Variances Matter</h2>

    <p>
      ANOVA compares sources of variation.
    </p>

    <p>
      Severe differences in population variances can affect the reliability of the F test.
    </p>

    <p>
      Alternative procedures exist when this assumption is violated.
    </p>

    <h2>ANOVA vs Multiple t Tests</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Multiple t Tests</th>
            <th>ANOVA</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Compares many groups</td>
            <td>Inefficient</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Controls overall Type I error</td>
            <td>Poorly</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Single global test</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Common Applications</h2>

    <div class="example-box">

      <p>
        Comparing teaching methods
      </p>

      <p>
        Comparing medical treatments
      </p>

      <p>
        Comparing manufacturing processes
      </p>

      <p>
        Comparing marketing strategies
      </p>

      <p>
        Comparing regional outcomes
      </p>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      One-way ANOVA generalizes the two-sample t test to situations involving three or more groups.
    </p>

    <p>
      Instead of comparing groups individually, it evaluates all groups simultaneously using the ratio of between-group variation to within-group variation.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        One-way ANOVA tests whether multiple population means are equal. It uses the F statistic to compare between-group variation to within-group variation and determines whether observed mean differences are larger than expected by chance.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      A significant ANOVA result indicates that at least one group differs.
    </p>

    <p>
      However, it does not identify which specific groups are different.
    </p>

    <p>
      The next lesson introduces post-hoc tests and multiple-comparison procedures that help locate those differences while controlling error rates.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>One-way ANOVA compares three or more population means</li>

        <li>The null hypothesis states that all population means are equal</li>

        <li>The F statistic compares between-group variation to within-group variation</li>

        <li>Large F values indicate stronger evidence against equal means</li>

        <li>A significant result implies at least one mean differs</li>

        <li>ANOVA does not identify which groups differ</li>

        <li>The method controls overall Type I error better than multiple t tests</li>

        <li>The F distribution depends on numerator and denominator degrees of freedom</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/chi-square-homogeneity-test/">
         ← Previous: Chi-Square Test of Homogeneity
      </a>

      <a class="btn"
         href="/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/">
         Next: Post-Hoc Tests and Multiple Comparisons →
      </a>

    </div>

  </div>

</section>