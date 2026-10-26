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

  try {
  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/",
    label: "Post-Hoc Tests and Multiple Comparisons",
    ts: Date.now()
  }));
  } catch (_) {
    // Disabled browser storage must not interrupt the lesson.
  }

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
      In the example of four teaching methods, a valid significant
      one-way ANOVA leads us to reject the joint null hypothesis:
    </p>

    \[
H_0:\ \mu_A=\mu_B=\mu_C=\mu_D
\]

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

    \[
\alpha_{\mathrm{per\ test}}=0.05
\]

    <p>
      then testing many true null hypotheses can increase the probability
      of at least one false positive. The exact family-wise error
      probability depends on dependence between rejection events and
      on the actual sizes of the individual tests.
    </p>

    <div class="concept-box">

      <strong>Key issue:</strong>

      <p>
        When many true hypotheses are tested, the chance of one or more
        false positives can exceed the per-test error rate.
        Adding a test cannot decrease the family-wise error probability,
        but dependence may prevent a strict increase.
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
      Consider 20 tests with mutually independent rejection events
      under their true null hypotheses, each of exact Type I error
      probability 0.05. In this illustrative case:
    </p>

    \[
P(\text{at least one false positive})
=1-(1-0.05)^{20}=1-0.95^{20}\approx0.642
\]

    <p>
      The probability of at least one false positive is approximately
      0.6415, or 64.2%. The formula 1 − (1 − α)ᵐ requires independent
      rejection events of the specified exact size; a nominal test
      level alone does not guarantee that numerical value.
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
      Bonferroni correction divides the desired family-wise level α
      among m pre-specified tests, m ≥ 1. Applying an individual
      test level α/m controls family-wise Type I error at or below α
      when each component test is valid. This follows from the union
      bound and does not require independent tests.
    </p>

    <p>
      The adjusted threshold becomes:
    </p>

    \[
\alpha_{\mathrm{Bonferroni}}=\frac{\alpha}{m}
\]

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>α = desired family-wise error rate</li>

      <li>m = number of comparisons</li>

    </ul>

    <!-- Batch #74: multiple-testing decisions, adjusted p-values and illustrative FWER -->
<section class="concept-box" id="esa-multiple-comparisons-lab" aria-labelledby="esa-mc-heading">
<h2 id="esa-mc-heading">Interactive Multiple Comparisons: Bonferroni and Holm</h2>
<p>Enter a <strong>predefined family of 2–12 valid p-values</strong>. Compare unadjusted decisions to Bonferroni and Holm's step-down adjusted p-values. Hypotheses remain in their original entered order; Holm sorts internally and restores the original order.</p>
<div class="esa-mc-grid">
<div><label for="esa-mc-values">P-values (comma, space or newline separated)</label>
<textarea id="esa-mc-values" rows="3" spellcheck="false">0.003, 0.018, 0.041, 0.22</textarea></div>
<div><label for="esa-mc-alpha">Family-wise significance level α (0 &lt; α &lt; 1)</label>
<input id="esa-mc-alpha" type="number" min="0" max="1" step="any" value="0.05"></div>
</div>
<button class="btn btn-outline" type="button" id="esa-mc-reset">Restore example</button>
<p id="esa-mc-error" role="alert" hidden></p>
<section id="esa-mc-results" aria-live="polite" aria-label="Multiple comparisons adjusted p-values">
<p>Number of tests: <strong id="esa-mc-count">4</strong>.</p>
<div class="table-wrap"><table><caption>Comparison-wise and family-wise adjustments (six decimals)</caption>
<thead><tr><th scope="col">Test</th><th scope="col">Raw p</th><th scope="col">Bonferroni p</th><th scope="col">Holm p</th><th scope="col">Raw decision</th><th scope="col">Bonferroni</th><th scope="col">Holm</th></tr></thead>
<tbody id="esa-mc-rows"></tbody>
</table></div>
<svg id="esa-mc-chart" role="img" viewBox="0 0 610 265" style="display:block;width:100%;height:auto" aria-label="Unadjusted, Bonferroni and Holm adjusted p-values"></svg>
<p><strong>Color key:</strong> <span style="color:#a16207">Unadjusted</span> · <span style="color:#2563eb">Bonferroni</span> · <span style="color:#0f766e">Holm</span>. Red dashed line marks α.</p>
<p><strong>At least one false rejection across m tests:</strong> if all m nulls are true and the individual valid tests are independent, the unadjusted theoretical probability is <strong id="esa-mc-fwer">—</strong> (= 1−(1−α)ᵐ). This is <em>not</em> an estimate from the submitted p-values.</p>
<p>The union bound, valid without assuming independence, is at most <strong id="esa-mc-bound">—</strong> (= min(1,mα)) for unadjusted testing when each true-null test has size at most α.</p>
<p id="esa-mc-summary"></p>
</section>
<p class="muted-mini">Holm adjusted p-values are cumulative maxima of (m−j+1)p₍ⱼ₎ in sorted order, capped at 1. Bonferroni uses min(1,mp). Both control the family-wise error rate for a prespecified family of valid p-values under arbitrary dependence. Independence is assumed <em>only</em> for the illustrative 1−(1−α)ᵐ formula. P-values do not quantify effect size; this lab does not compute Tukey HSD or replace a full ANOVA or post-hoc analysis.</p>
</section>
<style>
#esa-multiple-comparisons-lab,#esa-multiple-comparisons-lab *{box-sizing:border-box}
#esa-multiple-comparisons-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-multiple-comparisons-lab .esa-mc-grid{display:grid;grid-template-columns:minmax(0,2fr) minmax(180px,1fr);gap:12px;margin:14px 0}
#esa-multiple-comparisons-lab label{display:block;font-weight:650;margin-bottom:5px}
#esa-multiple-comparisons-lab :is(textarea,input){font:inherit;width:100%;min-width:0;padding:10px;border:1px solid #777;border-radius:6px}
#esa-multiple-comparisons-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-multiple-comparisons-lab [hidden]{display:none!important}
#esa-multiple-comparisons-lab :is(textarea,input,button):focus-visible{outline:2px solid #0f766e;outline-offset:3px}
@media(max-width:600px){#esa-multiple-comparisons-lab .esa-mc-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/multiple-comparisons-explorer.js"></script>
<h2>Trade-Offs</h2>

    <p>
      With a fixed design and comparable tests, stronger family-wise
      error control often reduces the chance of detecting a true
      difference. Other designs or sample sizes can change that trade-off.
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