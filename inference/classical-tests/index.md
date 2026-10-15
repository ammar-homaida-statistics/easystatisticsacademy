---
layout: default
title: Block 4 — Classical Tests
description: "Learn the classical hypothesis tests used everywhere: z and t tests, chi-square tests, ANOVA (F tests), and the core assumptions and interpretations behind them."
permalink: /inference/classical-tests/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_inference_last_block_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/",
    label: "Block 4 — Classical Tests",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card hero-split">

    <!-- LEFT -->

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Inference</span>
        <span class="badge">Block 4</span>
        <span class="badge">z / t</span>
        <span class="badge">χ² / F</span>
      </div>

      <h1>Block 4 — Classical Tests</h1>

      <p class="lead">
        Classical hypothesis tests are the standard tools used to evaluate
        means, proportions, categorical relationships, and group differences.
      </p>

      <p class="lead">
        This block develops the major testing procedures used throughout
        statistics, emphasizing assumptions, interpretation,
        and choosing the correct test for the question at hand.
      </p>

      <p class="muted-mini">
        12 lessons • Applied inference toolkit • Builds on Hypothesis Testing • Prepares for Power & Sample Size
      </p>

      <div class="hero-actions">

        <a class="btn" href="#lessons">
          Open Lessons
        </a>

        <a class="btn btn-outline" href="/inference/">
          Back to Statistical Inference
        </a>

      </div>

      <div class="hero-highlight">

        <div class="hero-highlight-icon">
          🧪
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            Most real-world statistical analyses rely on a small collection
            of classical tests. Understanding when and why they work
            is more important than memorizing formulas.
          </p>

        </div>

      </div>

    </div>

    <!-- RIGHT -->

    <div class="hero-panel">

      <div class="panel-card">

        <h2 class="panel-title">Block overview</h2>

        <div class="mini">
          <div class="mini-title">Lessons</div>
          <div class="mini-body">12 structured lessons</div>
        </div>

        <div class="mini">
          <div class="mini-title">Level</div>
          <div class="mini-body">Applied statistical inference</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Select and interpret classical tests correctly
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Next block</div>
          <div class="mini-body">
            Power & Sample Size
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-inference-classical"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-inference-classical-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-inference-classical-btn"
        href="#"
      >
        Continue
      </a>

    </div>

  </div>

</section>

<style>
  #test-selection-guide, #test-selection-guide .content-narrow, #esa-test-guide {
    min-width: 0;
    max-width: 100%;
    box-sizing: border-box;
  }
  #esa-test-guide select {
    display: block;
    width: 100%;
    min-width: 0;
    max-width: 100%;
    box-sizing: border-box;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  #esa-test-result {
    min-width: 0;
    max-width: 100%;
    box-sizing: border-box;
    overflow-wrap: anywhere;
  }
</style>
<!-- METHOD-SELECTION GUIDE: explanatory, non-diagnostic learning aid -->
<section class="section" id="test-selection-guide" aria-labelledby="esa-test-guide-heading">
  <div class="content-narrow">
    <h2 id="esa-test-guide-heading">Choose a Statistical Test</h2>
    <p>Explore which classical test matches a research question. The result is a starting point: verify study design, independence, distributional assumptions and sample size before applying any procedure.</p>
    <div class="card" id="esa-test-guide">
      <label for="esa-test-outcome"><strong>What outcome are you analyzing?</strong></label>
      <select id="esa-test-outcome" style="display:block;width:100%;max-width:100%;padding:10px;margin:8px 0 16px">
        <option value="mean">A numerical measurement / population mean</option>
        <option value="binary">A yes/no outcome / population proportion</option>
        <option value="categorical">Categorical counts / category distribution</option>
      </select>
      <label for="esa-test-design"><strong>Which study design or question?</strong></label>
      <select id="esa-test-design" style="display:block;width:100%;max-width:100%;padding:10px;margin:8px 0 16px">
        <option value="one">One sample compared with a reference</option>
        <option value="paired">Paired / matched observations</option>
        <option value="independent">Two independent samples or groups</option>
        <option value="multiple">Three or more independent groups</option>
        <option value="association">Association between two categorical variables</option>
      </select>
      <div id="esa-test-sigma-wrapper">
        <label for="esa-test-sigma"><strong>For a one-sample mean, is population σ known?</strong></label>
        <select id="esa-test-sigma" style="display:block;width:100%;max-width:100%;padding:10px;margin:8px 0 16px">
          <option value="unknown">No — use the sample standard deviation</option>
          <option value="known">Yes — population σ is genuinely known</option>
        </select>
      </div>
      <div id="esa-test-result" role="status" aria-live="polite" aria-atomic="true" style="padding:12px;border:1px solid currentColor;border-radius:8px;margin-top:12px">
        Select your outcome and design to see a recommendation.
      </div>
    </div>
    <p class="muted-mini">This guide covers the classical methods taught in this block. Repeated-measures ANOVA, clustered designs, nonparametric tests and small-count exact methods require separate consideration; incompatible combinations show an explanation rather than a misleading recommendation.</p>
    <noscript>JavaScript is required for the interactive guide. Use the linked test lessons below to compare assumptions and methods.</noscript>
  </div>
</section>
<script>
(function () {
  const guide = document.getElementById("esa-test-guide");
  if (!guide) return;
  const outcome = guide.querySelector("#esa-test-outcome");
  const design = guide.querySelector("#esa-test-design");
  const sigma = guide.querySelector("#esa-test-sigma");
  const sigmaWrapper = guide.querySelector("#esa-test-sigma-wrapper");
  const result = guide.querySelector("#esa-test-result");
  const root = "/inference/classical-tests/";
  // Entries are educational choices, not automatic statistical analyses.
  const methods = {
    "mean-one-unknown": ["One-Sample t Test for a Mean", "one-sample-t-test-for-mean/", "Use when observations are independent and population σ is unknown. Exact small-sample t inference assumes a normally distributed population; assess outliers and sampling."],
    "mean-one-known": ["One-Sample Z Test for a Mean", "one-sample-z-test-for-mean/", "Requires genuinely known population σ, independent observations and a normal sampling distribution (exact for normal data, approximate under suitable large-sample conditions)."],
    "mean-paired": ["Paired t Test", "paired-t-test/", "Analyze within-pair numerical differences. Pairs should be independent of other pairs; small-sample inference assumes approximately normal differences."],
    "mean-independent": ["Two-Sample t Test (Welch)", "two-sample-t-test-independent/", "For independent groups, Welch's test estimates separate variances; check independent observations, outliers and normality or adequate sample sizes."],
    "mean-multiple": ["One-Way ANOVA", "one-way-anova-f-test/", "Compare means across three or more independent groups. Standard ANOVA assumes independent errors, approximately normal errors within groups and common within-group variance; otherwise consider alternatives."],
    "binary-one": ["One-Proportion Z Test", "one-proportion-z-test/", "Use for independent binary trials with sufficient expected successes and failures under the null hypothesis. Sparse counts may need exact methods."],
    "binary-independent": ["Two-Proportion Z Test", "two-proportion-z-test/", "Compare independent groups' event proportions when expected counts justify the pooled-null normal approximation. Small samples may require exact methods."],
    "categorical-one": ["Chi-Square Goodness-of-Fit", "chi-square-goodness-of-fit/", "Compare observed category counts against a pre-specified probability distribution; independent observations and adequate expected counts are important."],
    "categorical-independent": ["Chi-Square Homogeneity Test", "chi-square-homogeneity-test/", "Compare categorical distributions across independently sampled populations or groups; inspect expected counts."],
    "categorical-association": ["Chi-Square Independence Test", "chi-square-independence-test/", "Test association between two categorical variables measured on independent observations in one sampled population; check expected counts."]
  };
  function update() {
    sigmaWrapper.hidden = !(outcome.value === "mean" && design.value === "one");
    const suffix = outcome.value === "mean" && design.value === "one" ? "-" + sigma.value : "";
    const choice = methods[outcome.value + "-" + design.value + suffix];
    result.replaceChildren();
    if (!choice) {
      result.textContent = "This combination needs a different design-specific method. Reconsider the outcome and sampling structure; see the lessons below or consult a statistical reference.";
      return;
    }
    const heading = document.createElement("strong");
    heading.textContent = "Suggested starting point: ";
    const link = document.createElement("a");
    link.href = root + choice[1];
    link.textContent = choice[0];
    const explanation = document.createElement("p");
    explanation.textContent = choice[2];
    result.append(heading, link, explanation);
  }
  outcome.addEventListener("change", update);
  design.addEventListener("change", update);
  sigma.addEventListener("change", update);
  update();
})();
</script>

<!-- LESSONS -->

<section class="section" id="lessons">

  <div class="section-head">

    <h2>Lessons</h2>

    <p>
      These lessons cover the major testing procedures used throughout
      research, business, medicine, social science, and data analysis.
    </p>

  </div>

  <div class="grid grid-2">

    <!-- LESSON 1 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/classical-tests/decision-framework-and-assumptions/">
          Decision Framework and Assumptions
        </a>
      </h3>

      <p>
        Review the hypothesis-testing framework
        and the assumptions that make statistical tests valid.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Review</span>
        <span class="pill">Assumptions</span>
        <span class="pill">Framework</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/classical-tests/decision-framework-and-assumptions/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 2 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/classical-tests/one-sample-z-test-for-mean/">
          One-Sample z Test for a Mean
        </a>
      </h3>

      <p>
        Learn the classic z test for population means
        when the population standard deviation is known.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">z Test</span>
        <span class="pill">Mean</span>
        <span class="pill">Inference</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/classical-tests/one-sample-z-test-for-mean/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 3 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/classical-tests/one-sample-t-test-for-mean/">
          One-Sample t Test for a Mean
        </a>
      </h3>

      <p>
        Learn the standard one-sample mean test
        used when population variability is unknown.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">t Test</span>
        <span class="pill">Mean</span>
        <span class="pill">Degrees of Freedom</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/classical-tests/one-sample-t-test-for-mean/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 4 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/classical-tests/paired-t-test/">
          Paired t Test
        </a>
      </h3>

      <p>
        Analyze paired and matched observations
        through tests on difference scores.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Paired</span>
        <span class="pill">Differences</span>
        <span class="pill">Matched Data</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/classical-tests/paired-t-test/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 5 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/classical-tests/two-sample-t-test-independent/">
          Two-Sample t Test (Independent Samples)
        </a>
      </h3>

      <p>
        Compare two population means
        using independent samples and t distributions.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Two Samples</span>
        <span class="pill">Means</span>
        <span class="pill">Comparison</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/classical-tests/two-sample-t-test-independent/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 6 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/classical-tests/one-proportion-z-test/">
          One-Proportion z Test
        </a>
      </h3>

      <p>
        Test population proportions using normal approximations
        and proportion standard errors.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Proportion</span>
        <span class="pill">z Test</span>
        <span class="pill">Categorical Data</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/classical-tests/one-proportion-z-test/"
      >
        Open lesson
      </a>

    </div>

<!-- LESSON 7 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/classical-tests/two-proportion-z-test/">
          Two-Proportion z Test
        </a>
      </h3>

      <p>
        Compare two population proportions
        and evaluate whether observed differences are statistically meaningful.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Two Proportions</span>
        <span class="pill">Comparison</span>
        <span class="pill">z Test</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/classical-tests/two-proportion-z-test/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 8 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/classical-tests/chi-square-goodness-of-fit/">
          Chi-Square Goodness-of-Fit Test
        </a>
      </h3>

      <p>
        Test whether observed categorical counts
        match an expected probability distribution.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Chi-Square</span>
        <span class="pill">GOF</span>
        <span class="pill">Categorical</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/classical-tests/chi-square-goodness-of-fit/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 9 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/classical-tests/chi-square-independence-test/">
          Chi-Square Test of Independence
        </a>
      </h3>

      <p>
        Evaluate whether two categorical variables
        are statistically associated using contingency tables.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Association</span>
        <span class="pill">Contingency Tables</span>
        <span class="pill">Chi-Square</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/classical-tests/chi-square-independence-test/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 10 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/classical-tests/chi-square-homogeneity-test/">
          Chi-Square Test of Homogeneity
        </a>
      </h3>

      <p>
        Compare categorical distributions
        across populations or groups.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Homogeneity</span>
        <span class="pill">Groups</span>
        <span class="pill">Chi-Square</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/classical-tests/chi-square-homogeneity-test/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 11 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/classical-tests/one-way-anova-f-test/">
          One-Way ANOVA (F Test for 3+ Means)
        </a>
      </h3>

      <p>
        Compare three or more group means
        using the analysis of variance framework.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">ANOVA</span>
        <span class="pill">F Test</span>
        <span class="pill">Multiple Groups</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/classical-tests/one-way-anova-f-test/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 12 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/">
          Post-hoc Tests and Multiple Comparisons
        </a>
      </h3>

      <p>
        Learn why repeated testing inflates false positives
        and how adjustment procedures address the problem.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Multiple Testing</span>
        <span class="pill">Bonferroni</span>
        <span class="pill">Post-hoc</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/"
      >
        Open lesson
      </a>

    </div>

  </div>

</section>

<!-- BLOCK MAP -->

<section class="section section-slim">

  <div class="callout">

    <div class="callout-copy">

      <h2>How this block fits into inference</h2>

      <p>
        This block turns hypothesis-testing theory into practical procedures.
        Each classical test is built on the same inferential framework,
        but applies to different types of data and research questions.
      </p>

      <div class="table-wrap">

        <table>

          <thead>

            <tr>
              <th>Test Family</th>
              <th>Primary Use</th>
            </tr>

          </thead>

          <tbody>

            <tr>
              <td>z Tests</td>
              <td>Means and proportions with normal approximations</td>
            </tr>

            <tr>
              <td>t Tests</td>
              <td>Inference for means when variability is estimated</td>
            </tr>

            <tr>
              <td>Chi-Square Tests</td>
              <td>Categorical distributions and associations</td>
            </tr>

            <tr>
              <td>ANOVA (F Tests)</td>
              <td>Comparing multiple group means</td>
            </tr>

            <tr>
              <td>Post-hoc Procedures</td>
              <td>Controlling false positives after multiple comparisons</td>
            </tr>

          </tbody>

        </table>

      </div>

    </div>

  </div>

</section>

<!-- GOALS -->

<section class="section section-slim">

  <div class="callout">

    <div class="callout-copy">

      <h2>Goal of this block</h2>

      <ul class="bullets">

        <li>Select the correct classical test for a given research question</li>

        <li>Understand the assumptions behind z, t, chi-square, and F tests</li>

        <li>Interpret test statistics and p-values correctly</li>

        <li>Distinguish between different study designs and data types</li>

        <li>Understand when normal approximations are appropriate</li>

        <li>Recognize limitations of statistical significance alone</li>

        <li>Report results with effect sizes and practical context</li>

        <li>Prepare for study design, power analysis, and sample-size planning</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next block</div>

        <div class="mini-body">
          Continue to <strong>Power & Sample Size</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          Different questions require different tests, but all rely on the same inferential logic.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Big transition</div>

        <div class="mini-body">
          The next block focuses on designing studies that can reliably detect meaningful effects.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/inference/hypothesis-testing/">
      ← Previous Block: Hypothesis Testing
    </a>

    <a class="btn" href="/inference/power-sample-size/">
      Next Block: Power & Sample Size →
    </a>

  </div>

</section>

<!-- CONTINUE READING SCRIPT -->

<script>
(function () {

  try {

    const KEY =
      "esa_continue_inference_classical_tests_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    if (!data || !data.url || !data.label) return;

    const wrap =
      document.getElementById(
        "continue-reading-inference-classical"
      );

    const label =
      document.getElementById(
        "continue-reading-inference-classical-label"
      );

    const btn =
      document.getElementById(
        "continue-reading-inference-classical-btn"
      );

    if (!wrap || !label || !btn) return;

    label.innerHTML =
      "You last visited: <strong>" +
      data.label +
      "</strong>";

    btn.href = data.url;

    wrap.style.display = "block";

  } catch (e) {}

})();
</script>