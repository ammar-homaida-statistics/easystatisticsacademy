---
layout: default
title: Post-Hoc Tests and Multiple Comparisons
description: Learn why significant ANOVA results often require follow-up analyses and how post-hoc procedures control error rates when making multiple comparisons.
permalink: /inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_classical_tests_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/",
    label: "Post-Hoc Tests and Multiple Comparisons",
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
      <span class="badge">ANOVA Follow-Up</span>
    </div>

    <h1>Post-Hoc Tests and Multiple Comparisons</h1>

    <p class="lead">
      A significant ANOVA result tells us that at least one population mean differs, but it does not identify which groups are different.
    </p>

    <p class="lead">
      Post-hoc procedures provide systematic ways to investigate group differences while controlling the increased risk of false-positive conclusions.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/one-way-anova-f-test/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/regression-and-modeling/">
         Next Block: Regression and Modeling →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Happens After ANOVA?</h2>

    <p>
      Recall that one-way ANOVA tests:
    </p>

    0

    <p>
      against the alternative that at least one population mean differs.
    </p>

    <p>
      If ANOVA is not significant, there is little evidence of meaningful differences among the groups.
    </p>

    <p>
      If ANOVA is significant, the next question becomes:
    </p>

    <div class="example-box">

      <p>
        Which groups are actually different?
      </p>
    </div>

    <h2>The Limitation of ANOVA</h2>

    <div class="concept-box">

      <strong>Important limitation:</strong>

      <p>
        ANOVA is a global test. It determines whether differences exist somewhere among the groups, but it does not identify where those differences occur.
      </p>

    </div>

    <p>
      Additional analyses are required to locate specific group differences.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose ANOVA compares four teaching methods:
    </p>

    <div class="example-box">

      <p>Method A</p>
      <p>Method B</p>
      <p>Method C</p>
      <p>Method D</p>
    </div>

    <p>
      A significant F test indicates that at least one mean differs.
    </p>

    <p>
      However, ANOVA does not tell us whether:
    </p>

    <ul class="bullets">

      <li>A differs from B</li>

      <li>A differs from C</li>

      <li>B differs from D</li>

      <li>Several groups differ simultaneously</li>

    </ul>

    <h2>Why Not Run Many t Tests?</h2>

    <p>
      One possibility is performing every pairwise comparison separately.
    </p>

    <p>
      Unfortunately, this creates a new problem.
    </p>

    <div class="concept-box">

      <strong>Multiple-comparison problem:</strong>

      <p>
        As the number of hypothesis tests increases, the probability of obtaining at least one false-positive result also increases.
      </p>

    </div>

    <h2>The Family-Wise Error Rate</h2>

    <p>
      When many tests are performed simultaneously, statisticians often focus on:
    </p>

    <div class="example-box">

      <p>
        Family-Wise Error Rate (FWER)
      </p>
    </div>

    <p>
      This is the probability of making at least one Type I error among a collection of related tests.
    </p>

    <h2>An Illustration</h2>

    <p>
      Suppose each individual test uses:
    </p>

    1

    <p>
      Running many tests makes the overall probability of at least one false positive substantially larger than 0.05.
    </p>

    <p>
      Therefore, adjustments become necessary.
    </p>

    <h2>What Are Post-Hoc Tests?</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Post-hoc tests are follow-up procedures conducted after a significant omnibus test such as ANOVA to determine which specific group differences are statistically significant.
      </p>

    </div>

    <h2>Common Post-Hoc Procedures</h2>

    <p>
      Several methods are commonly used.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Procedure</th>
            <th>Main Purpose</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Tukey's HSD</td>
            <td>All pairwise comparisons</td>
          </tr>

          <tr>
            <td>Bonferroni Correction</td>
            <td>General error control</td>
          </tr>

          <tr>
            <td>Holm Procedure</td>
            <td>Improved Bonferroni approach</td>
          </tr>

          <tr>
            <td>Scheffé Method</td>
            <td>Flexible contrasts</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Tukey's HSD</h2>

    <p>
      Tukey's Honest Significant Difference procedure is one of the most widely used post-hoc methods.
    </p>

    <p>
      It is designed specifically for comparing all pairs of means while maintaining control of the overall error rate.
    </p>

    <h2>Bonferroni Adjustment</h2>

    <p>
      The Bonferroni approach modifies the significance threshold by dividing:
    </p>

    2

    <p>
      by the number of comparisons.
    </p>

    <p>
      For example:
    </p>

    3

    <p>
      This reduces the chance of false positives.
    </p>

    <h2>The Trade-Off</h2>

    <p>
      Stronger error control generally comes with a cost.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Benefit</th>
            <th>Cost</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Fewer false positives</td>
            <td>Lower statistical power</td>
          </tr>

          <tr>
            <td>Stronger error control</td>
            <td>Harder to detect small effects</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>How Many Comparisons Are There?</h2>

    <p>
      With:
    </p>

    4

    <p>
      groups, the number of pairwise comparisons equals:
    </p>

    5

    <p>
      The number of tests grows quickly as more groups are added.
    </p>

    <h2>Example</h2>

    <p>
      With four groups:
    </p>

    6

    <p>
      pairwise comparisons are possible.
    </p>

    <h2>Practical Interpretation</h2>

    <p>
      A complete ANOVA analysis often follows this sequence:
    </p>

    <div class="example-box">

      <p>
        Step 1: Perform ANOVA
      </p>

      <p>
        Step 2: Determine whether ANOVA is significant
      </p>

      <p>
        Step 3: Apply post-hoc procedures if needed
      </p>

      <p>
        Step 4: Interpret specific group differences
      </p>

    </div>

    <h2>Beyond Pairwise Comparisons</h2>

    <p>
      Some studies focus on planned comparisons or specific contrasts chosen before collecting data.
    </p>

    <p>
      These approaches can sometimes provide greater power than broad post-hoc analyses.
    </p>

    <p>
      Designing such analyses requires careful planning and domain knowledge.
    </p>

    <h2>Connection to Modern Statistics</h2>

    <p>
      Multiple-comparison issues appear throughout statistics, not only in ANOVA.
    </p>

    <p>
      They arise in:
    </p>

    <ul class="bullets">

      <li>A/B testing</li>

      <li>Medical trials</li>

      <li>Genomics</li>

      <li>Machine learning model evaluation</li>

      <li>Large-scale experimentation</li>

    </ul>

    <p>
      Modern statistical practice places substantial emphasis on controlling false discoveries.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      ANOVA provides evidence that differences exist among group means.
    </p>

    <p>
      Post-hoc procedures provide the tools needed to identify those differences while maintaining appropriate control of statistical error rates.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        A significant ANOVA result indicates that at least one mean differs, but additional analyses are needed to identify specific group differences. Post-hoc procedures address this challenge while controlling the increased risk of false-positive conclusions created by multiple comparisons.
      </p>

    </div>

    <h2>Completing the Classical Tests Block</h2>

    <p>
      You have now completed the major classical hypothesis-testing procedures commonly introduced in introductory statistics.
    </p>

    <p>
      These methods provide a foundation for comparing means, proportions, categorical distributions, and relationships among variables.
    </p>

    <p>
      The next block expands these ideas into regression and statistical modeling, where relationships between variables can be quantified and used for prediction.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>ANOVA identifies whether differences exist but not where they occur</li>

        <li>Post-hoc tests locate specific group differences</li>

        <li>Multiple comparisons increase the risk of Type I errors</li>

        <li>The family-wise error rate measures overall false-positive risk</li>

        <li>Tukey, Bonferroni, Holm, and Scheffé are common post-hoc procedures</li>

        <li>Stronger error control often reduces statistical power</li>

        <li>Multiple-comparison issues arise throughout statistics</li>

        <li>Post-hoc analyses complement ANOVA by identifying specific differences</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/one-way-anova-f-test/">
         ← Previous: One-Way ANOVA and the F Test
      </a>

      <a class="btn"
         href="/inference/regression-and-modeling/">
         Next Block: Regression and Modeling →
      </a>

    </div>

  </div>

</section>