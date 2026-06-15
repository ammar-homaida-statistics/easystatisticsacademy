---
layout: default
title: Post-Hoc Tests and Multiple Comparisons
description: Learn why post-hoc tests are needed after ANOVA and how statisticians control error rates when making multiple comparisons.
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
      A significant ANOVA result tells us that at least one group mean differs, but it does not identify which groups are different.
    </p>

    <p class="lead">
      Post-hoc procedures provide a systematic way to investigate specific group differences while controlling the risk of false discoveries.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/one-way-anova-f-test/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/power-sample-size/">
         Next Block: Power & Sample Size →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What ANOVA Does Not Tell Us</h2>

    <p>
      Recall that a significant ANOVA result leads us to reject:
    </p>

    0

    <p>
      However, ANOVA does not reveal:
    </p>

    <ul class="bullets">

      <li>Which groups differ</li>

      <li>How many groups differ</li>

      <li>The magnitude of those differences</li>

    </ul>

    <p>
      Additional analysis is required.
    </p>

    <h2>A Motivating Example</h2>

    <p>
      Suppose an ANOVA compares four teaching methods:
    </p>

    <div class="example-box">

      <p>Method A</p>
      <p>Method B</p>
      <p>Method C</p>
      <p>Method D</p>

    </div>

    <p>
      The ANOVA result is statistically significant.
    </p>

    <p>
      We now know that at least one mean differs, but we do not know whether:
    </p>

    <div class="example-box">

      <p>A differs from B</p>
      <p>A differs from C</p>
      <p>B differs from D</p>
      <p>Several pairs differ simultaneously</p>

    </div>

    <h2>The Temptation</h2>

    <p>
      One simple idea is to perform many pairwise t tests.
    </p>

    <p>
      For four groups, we could compare:
    </p>

    <ul class="bullets">

      <li>A vs B</li>

      <li>A vs C</li>

      <li>A vs D</li>

      <li>B vs C</li>

      <li>B vs D</li>

      <li>C vs D</li>

    </ul>

    <p>
      Unfortunately, this creates a new problem.
    </p>

    <h2>The Multiple Comparisons Problem</h2>

    <p>
      Every hypothesis test carries a chance of making a Type I error.
    </p>

    <p>
      If each test uses:
    </p>

    1

    <p>
      then conducting many tests increases the probability of obtaining at least one false positive.
    </p>

    <div class="concept-box">

      <strong>Key issue:</strong>

      <p>
        The more tests we perform, the greater the overall probability of incorrectly rejecting at least one true null hypothesis.
      </p>

    </div>

    <h2>Family-Wise Error Rate</h2>

    <p>
      The probability of making one or more Type I errors across a family of tests is called the:
    </p>

    <div class="example-box">

      <p>
        Family-Wise Error Rate (FWER)
      </p>
    </div>

    <p>
      Controlling this error rate is one of the primary goals of post-hoc procedures.
    </p>

    <h2>Why Control Error Rates?</h2>

    <p>
      Consider conducting 20 independent tests using:
    </p>

    2

    <p>
      Even if every null hypothesis is true, obtaining at least one significant result becomes surprisingly likely.
    </p>

    <p>
      Multiple-comparison procedures help prevent misleading conclusions.
    </p>

    <h2>What Are Post-Hoc Tests?</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Post-hoc tests are follow-up procedures performed after a significant omnibus test such as ANOVA.
      </p>

    </div>

    <p>
      They identify which specific comparisons are statistically significant while controlling overall error rates.
    </p>

    <h2>Common Post-Hoc Procedures</h2>

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
            <td>Tukey HSD</td>
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
      Tukey's Honestly Significant Difference procedure is one of the most commonly used post-hoc methods.
    </p>

    <p>
      It is specifically designed for:
    </p>

    <div class="example-box">

      <p>
        All pairwise mean comparisons
      </p>
    </div>

    <p>
      while controlling the overall Type I error rate.
    </p>

    <h2>The Bonferroni Idea</h2>

    <p>
      Bonferroni correction adjusts the significance level according to the number of comparisons.
    </p>

    <p>
      The adjusted threshold becomes:
    </p>

    3

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>α = desired family-wise error rate</li>

      <li>m = number of comparisons</li>

    </ul>

    <h2>Trade-Offs</h2>

    <p>
      Stronger error control often reduces statistical power.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Approach</th>
            <th>Type I Error</th>
            <th>Power</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Loose control</td>
            <td>Higher</td>
            <td>Higher</td>
          </tr>

          <tr>
            <td>Strict control</td>
            <td>Lower</td>
            <td>Lower</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Choosing a procedure often involves balancing these competing goals.
    </p>

    <h2>Planned vs Post-Hoc Comparisons</h2>

    <p>
      Some comparisons are specified before data collection.
    </p>

    <p>
      These are called:
    </p>

    <div class="example-box">

      <p>
        Planned Comparisons
      </p>
    </div>

    <p>
      Others are chosen after inspecting results.
    </p>

    <p>
      These are:
    </p>

    <div class="example-box">

      <p>
        Post-Hoc Comparisons
      </p>
    </div>

    <p>
      Post-hoc analyses typically require stronger error control because they are data-driven.
    </p>

    <h2>Effect Size Still Matters</h2>

    <p>
      Statistical significance does not automatically imply practical importance.
    </p>

    <p>
      After identifying significant differences, researchers often evaluate:
    </p>

    <ul class="bullets">

      <li>Mean differences</li>

      <li>Confidence intervals</li>

      <li>Effect sizes</li>

    </ul>

    <p>
      These quantities help assess practical significance.
    </p>

    <h2>Modern Perspective</h2>

    <p>
      Modern statistical reporting often combines:
    </p>

    <ul class="bullets">

      <li>ANOVA results</li>

      <li>Post-hoc comparisons</li>

      <li>Confidence intervals</li>

      <li>Effect-size measures</li>

    </ul>

    <p>
      This provides a more complete understanding of group differences.
    </p>

    <h2>Relationship to Future Topics</h2>

    <p>
      Multiple-comparison ideas extend far beyond ANOVA.
    </p>

    <p>
      They appear in:
    </p>

    <ul class="bullets">

      <li>Clinical trials</li>

      <li>Genomics</li>

      <li>A/B testing</li>

      <li>Large-scale experimentation</li>

      <li>Machine learning evaluation</li>

    </ul>

    <p>
      Whenever many hypotheses are tested simultaneously, multiplicity becomes an important concern.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      ANOVA provides an overall test for mean differences, but additional procedures are needed to identify where those differences occur.
    </p>

    <p>
      Post-hoc methods help researchers explore specific comparisons while maintaining appropriate control over false-positive findings.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Post-hoc tests are follow-up procedures used after significant omnibus tests such as ANOVA. They identify specific group differences while controlling the increased risk of Type I errors caused by multiple comparisons.
      </p>

    </div>

    <h2>Completing the Classical Tests Block</h2>

    <p>
      You have now completed the major classical hypothesis-testing procedures covered in introductory statistical inference.
    </p>

    <p>
      The next block focuses on power analysis and sample-size determination—tools that help researchers design studies before data collection begins.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>ANOVA identifies whether any group differences exist but not which groups differ</li>

        <li>Multiple comparisons increase the risk of Type I errors</li>

        <li>The family-wise error rate measures overall false-positive risk</li>

        <li>Post-hoc procedures control error rates while identifying specific differences</li>

        <li>Tukey, Bonferroni, Holm, and Scheffé are common approaches</li>

        <li>Stronger error control often reduces statistical power</li>

        <li>Planned comparisons differ from post-hoc comparisons</li>

        <li>Practical interpretation should include effect sizes and confidence intervals</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/one-way-anova-f-test/">
         ← Previous: One-Way ANOVA and the F Test
      </a>

      <a class="btn"
         href="/inference/power-sample-size/">
         Next Block: Power &amp; Sample Size →
      </a>

    </div>

  </div>

</section>