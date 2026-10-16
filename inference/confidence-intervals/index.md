---
layout: default
title: Block 2 — Confidence Intervals
description: "Build confidence intervals correctly: the logic of coverage, margin of error, critical values (z/t), and interval construction for means, proportions, and comparisons."
permalink: /inference/confidence-intervals/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_inference_last_block_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/confidence-intervals/",
    label: "Block 2 — Confidence Intervals",
    ts: Date.now()
  }));
  } catch (_) {
    // Gracefully continue when the browser denies persistent storage.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card hero-split">

    <!-- LEFT -->

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Inference</span>
        <span class="badge">Block 2</span>
        <span class="badge">Intervals</span>
        <span class="badge">Coverage</span>
      </div>

      <h1>Block 2 — Confidence Intervals</h1>

      <p class="lead">
        Confidence intervals provide a structured way to quantify uncertainty
        around statistical estimates.
      </p>

      <p class="lead">
        This block develops interval estimation from first principles,
        showing how estimates,
        standard errors,
        and critical values combine to produce meaningful uncertainty statements.
      </p>

      <p class="muted-mini">
        12 lessons • Core inferential tools • Builds on Inference Foundations • Prepares for Hypothesis Testing
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
          📏
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            Point estimates alone are incomplete.
            Confidence intervals provide the uncertainty context needed for
            responsible statistical conclusions and evidence-based decisions.
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
          <div class="mini-body">Core statistical inference</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Build and interpret confidence intervals
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Next block</div>
          <div class="mini-body">
            Hypothesis Testing
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-inference-ci"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-inference-ci-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-inference-ci-btn"
        href="#"
      >
        Continue
      </a>

    </div>

  </div>

</section>


<!-- CONFIDENCE INTERVAL SELF-CHECK -->
<section class="section" id="esa-ci-self-check-section" aria-labelledby="esa-ci-self-check-heading">
  <div class="content-narrow esa-self-check" id="esa-ci-self-check">
    <h2 id="esa-ci-self-check-heading">Check Your Confidence Interval Understanding</h2>
    <p>Answer each question for immediate feedback and a short explanation. Use Tab and the arrow keys to navigate the choices. Answers are not saved or transmitted.</p>
    <fieldset data-answer="b" data-explanation="A frequentist 95% procedure covers the fixed parameter in about 95% of repeated samples, under its model and sampling assumptions. It does not assign a 95% probability to the parameter after observing this particular interval.">
      <legend>1. What does 95% confidence mean for a valid interval procedure?</legend>
      <label><input type="radio" name="esa-ci-check-1" value="a"> The fixed population parameter has a 95% probability of changing between samples.</label>
      <label><input type="radio" name="esa-ci-check-1" value="b"> Approximately 95% of intervals built by the same procedure would contain the fixed parameter in repeated sampling.</label>
      <label><input type="radio" name="esa-ci-check-1" value="c"> 95% of all sample observations must lie inside each interval.</label>
      <p class="esa-check-feedback" role="status" aria-live="polite"></p>
    </fieldset>

    <fieldset data-answer="a" data-explanation="Margin of error equals critical value times estimated standard error: 1.96 × 0.02 = 0.0392.">
      <legend>2. If the standard error is 0.02 and the two-sided 95% z critical value is 1.96, what is the margin of error?</legend>
      <label><input type="radio" name="esa-ci-check-2" value="a"> 0.0392</label>
      <label><input type="radio" name="esa-ci-check-2" value="b"> 0.0200</label>
      <label><input type="radio" name="esa-ci-check-2" value="c"> 0.0980</label>
      <p class="esa-check-feedback" role="status" aria-live="polite"></p>
    </fieldset>

    <fieldset data-answer="c" data-explanation="A typical standard error is proportional to 1 divided by the square root of sample size. Increasing n fourfold halves the standard error and approximately halves the margin of error and width.">
      <legend>3. Under independent sampling and the same variability, what happens to the approximate confidence interval width when sample size quadruples?</legend>
      <label><input type="radio" name="esa-ci-check-3" value="a"> It doubles.</label>
      <label><input type="radio" name="esa-ci-check-3" value="b"> It remains unchanged.</label>
      <label><input type="radio" name="esa-ci-check-3" value="c"> It is approximately halved.</label>
      <p class="esa-check-feedback" role="status" aria-live="polite"></p>
    </fieldset>

    <fieldset data-answer="a" data-explanation="At the same standard error, a higher confidence level requires a larger critical value and therefore a larger margin of error; coverage and precision trade off.">
      <legend>4. With the same data and interval method, how does a 99% confidence interval compare with a 95% confidence interval?</legend>
      <label><input type="radio" name="esa-ci-check-4" value="a"> It is wider because the critical value increases.</label>
      <label><input type="radio" name="esa-ci-check-4" value="b"> It is narrower because 99% means higher precision.</label>
      <label><input type="radio" name="esa-ci-check-4" value="c"> It has exactly the same width.</label>
      <p class="esa-check-feedback" role="status" aria-live="polite"></p>
    </fieldset>

    <fieldset data-answer="b" data-explanation="For a two-sided test and its corresponding 95% interval under matching assumptions, excluding the null value 20 implies rejection at the 5% significance level. The point estimate is not proof of the exact parameter.">
      <legend>5. A 95% confidence interval for a mean is [12, 18]. What follows for the matching two-sided test H₀: μ = 20 at α = 0.05?</legend>
      <label><input type="radio" name="esa-ci-check-5" value="a"> Do not reject H₀ because the confidence level is high.</label>
      <label><input type="radio" name="esa-ci-check-5" value="b"> Reject H₀ because the interval excludes 20.</label>
      <label><input type="radio" name="esa-ci-check-5" value="c"> The interval proves that μ equals 15.</label>
      <p class="esa-check-feedback" role="status" aria-live="polite"></p>
    </fieldset>

    <fieldset data-answer="c" data-explanation="The plug-in standard error is the square root of p̂ times (1 − p̂) divided by n. A Wald interval needs sufficient successes and failures and can under-cover, especially near 0 or 1; Wilson intervals are often better.">
      <legend>6. In a simple 95% Wald interval for a sample proportion, which quantity is estimated using p̂ and n?</legend>
      <label><input type="radio" name="esa-ci-check-6" value="a"> The population standard deviation of continuous observations.</label>
      <label><input type="radio" name="esa-ci-check-6" value="b"> The exact realized sampling error of the point estimate.</label>
      <label><input type="radio" name="esa-ci-check-6" value="c"> The standard error of the sample proportion.</label>
      <p class="esa-check-feedback" role="status" aria-live="polite"></p>
    </fieldset>
  </div>
</section>
<script>
(function () {
  const quiz = document.getElementById("esa-ci-self-check");
  if (!quiz) return;
  quiz.querySelectorAll("fieldset").forEach(field => {
    field.addEventListener("change", event => {
      const choice = event.target;
      if (!choice.matches('input[type="radio"]') || !choice.checked) return;
      const feedback = field.querySelector(".esa-check-feedback");
      if (!feedback) return;
      const correct = choice.value === field.dataset.answer;
      feedback.textContent = (correct ? "Correct. " : "Not quite. ") +
        field.dataset.explanation;
      feedback.dataset.state = correct ? "correct" : "incorrect";
    });
  });
})();
</script>


<!-- CONFIDENCE INTERVAL METHOD SELECTION GUIDE -->
<section class="section" id="esa-ci-method-guide" aria-labelledby="esa-ci-method-guide-heading">
  <div class="content-narrow">
    <h2 id="esa-ci-method-guide-heading">Which Confidence Interval Should I Study?</h2>
    <p>Choose the quantity you want to estimate and how the data were collected.
      This guide points to an existing lesson; a valid method still depends on
      sampling design, independence, sample size and distributional assumptions.</p>
    <div class="concept-box esa-ci-method-card">
      <div class="esa-ci-method-fields">
        <div>
          <label for="esa-ci-goal"><strong>What are you estimating?</strong></label>
          <select id="esa-ci-goal">
            <option value="mean">A population mean or difference of means</option>
            <option value="proportion">A population proportion or difference of proportions</option>
          </select>
        </div>
        <div>
          <label for="esa-ci-design"><strong>What is the sample design?</strong></label>
          <select id="esa-ci-design">
            <option value="one">One sample</option>
            <option value="independent">Two independent groups</option>
            <option value="paired">Paired or matched observations</option>
          </select>
        </div>
        <div id="esa-ci-known-sigma-wrapper">
          <label for="esa-ci-known-sigma"><strong>For one population mean, is population σ genuinely known?</strong></label>
          <select id="esa-ci-known-sigma">
            <option value="unknown">No, σ is estimated from the sample</option>
            <option value="known">Yes, σ is known independently of the sample</option>
          </select>
        </div>
      </div>
      <div id="esa-ci-method-result" role="status" aria-live="polite">
        <p id="esa-ci-method-name"></p>
        <p id="esa-ci-method-assumptions"></p>
        <p id="esa-ci-method-caution"></p>
        <p id="esa-ci-method-link-wrapper"></p>
      </div>
      <p class="muted-mini">This learning guide covers the confidence interval methods
        taught in this block. Paired binary proportions, clustered designs,
        repeated measures, sparse count methods and complex sampling require
        specialized methods outside this selection tool.</p>
      <noscript>JavaScript is required for this selection guide. The published confidence
        interval lessons remain available below.</noscript>
    </div>
  </div>
</section>
<style>
  #esa-ci-method-guide,#esa-ci-method-guide .esa-ci-method-card {min-width:0;max-width:100%;overflow-wrap:anywhere}
  #esa-ci-method-guide .esa-ci-method-fields {display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:14px}
  #esa-ci-method-guide label {display:block;margin-bottom:7px}
  #esa-ci-method-guide select {display:block;box-sizing:border-box;width:100%;max-width:100%;min-width:0;padding:10px;margin:0}
  #esa-ci-method-guide #esa-ci-method-result p {margin:8px 0}
  #esa-ci-method-guide #esa-ci-method-result a {display:inline-block}
  #esa-ci-method-guide [hidden] {display:none!important}
</style>
<script>
(function () {
  "use strict";
  function init() {
    const root=document.getElementById("esa-ci-method-guide");
    if (!root) return;
    const field=id=>root.querySelector("#"+id);
    const goal=field("esa-ci-goal"),design=field("esa-ci-design"),
          sigma=field("esa-ci-known-sigma");
    const published=new Set(Array.from(document.querySelectorAll(
      "#lessons .lesson-card h3 a[href]"),a=>a.getAttribute("href"))
      .filter(path=>typeof path==="string" &&
       /^\/inference\/confidence-intervals\/[a-z0-9-]+\/$/.test(path)));
    const base="/inference/confidence-intervals/";
    const methods={
      "mean-one-known":{
        name:"Z confidence interval for a mean (known σ)",
        path:base+"ci-for-mean-sigma-known-z/",
        assumptions:"Genuinely known population σ; independent observations and a normal sampling distribution, either exactly under normal sampling or approximately with suitable sample size.",
        caution:"Do not treat a sample standard deviation as a known population σ."
      },
      "mean-one-unknown":{
        name:"One-sample t confidence interval for a mean",
        path:base+"ci-for-mean-sigma-unknown-t/",
        assumptions:"Independent observations; a nearly normal population for small samples, or appropriate large-sample justification.",
        caution:"Assess strong skewness, influential outliers and the sample design."
      },
      "mean-independent":{
        name:"Welch confidence interval for independent mean differences",
        path:base+"ci-for-difference-of-means-independent/",
        assumptions:"Independent groups and observations within groups; use separate sample variances and Welch–Satterthwaite degrees of freedom.",
        caution:"Paired data must not be treated as independent. Extremely small samples require appropriate distributional conditions."
      },
      "mean-paired":{
        name:"Paired t confidence interval for a mean difference",
        path:base+"ci-for-paired-mean-difference/",
        assumptions:"Meaningfully matched observations; independence across pairs; approximately normal differences for small samples, or suitable large-sample justification.",
        caution:"Calculate within-pair differences first and analyze their variability, not the marginal group standard deviations."
      },
      "proportion-one":{
        name:"Confidence interval for one population proportion",
        path:base+"ci-for-proportion/",
        assumptions:"Independent binary observations and an appropriate sampling design; choose an interval method whose coverage is justified for the expected counts.",
        caution:"The simple Wald interval can have poor coverage near 0 or 1 and with small samples. Consider Wilson or exact methods as appropriate."
      },
      "proportion-independent":{
        name:"Confidence interval for two independent proportions",
        path:base+"ci-for-difference-of-proportions/",
        assumptions:"Independent binary observations within each of two independent groups; sufficient sample sizes for the chosen approximation.",
        caution:"Paired proportions and sparse counts need different procedures; a normal Wald interval can perform poorly near boundaries."
      }
    };
    function update() {
      const showSigma=goal.value==="mean"&&design.value==="one";
      field("esa-ci-known-sigma-wrapper").hidden=!showSigma;
      const key=goal.value+"-"+design.value+(showSigma?"-"+sigma.value:"");
      const item=methods[key];
      const name=field("esa-ci-method-name"),assumptions=field("esa-ci-method-assumptions"),
            caution=field("esa-ci-method-caution"),link=field("esa-ci-method-link-wrapper");
      link.replaceChildren();
      if (!item || !published.has(item.path)) {
        name.textContent="No direct method in this block for this combination.";
        assumptions.textContent="Reconsider the sampling design and consult a design-specific statistical reference.";
        caution.textContent="This guide does not invent a method or link to an unpublished lesson.";
        return;
      }
      name.textContent="Suggested lesson: "+item.name;
      assumptions.textContent="Conditions: "+item.assumptions;
      caution.textContent="Caution: "+item.caution;
      const a=document.createElement("a");
      a.href=item.path;a.className="btn btn-outline";
      a.textContent="Open "+item.name+" lesson";
      link.appendChild(a);
    }
    [goal,design,sigma].forEach(input=>input.addEventListener("change",update));
    update();
  }
  if (document.readyState==="loading") document.addEventListener("DOMContentLoaded",init,{once:true});
  else init();
})();
</script>

<!-- LESSONS -->

<section class="section" id="lessons">

  <div class="section-head">

    <h2>Lessons</h2>

    <p>
      These lessons develop interval estimation from conceptual foundations
      through practical construction and interpretation.
    </p>

  </div>

  <div class="grid grid-2">

    <!-- LESSON 1 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/what-is-a-confidence-interval/">
          What Is a Confidence Interval?
        </a>
      </h3>

      <p>
        Learn the meaning of confidence intervals,
        long-run coverage,
        and what “95% confidence” actually means.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Coverage</span>
        <span class="pill">Confidence</span>
        <span class="pill">Foundations</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/what-is-a-confidence-interval/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 2 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/">
          CI Blueprint: Estimate ± Margin of Error
        </a>
      </h3>

      <p>
        Learn the universal structure shared by nearly all confidence intervals.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Blueprint</span>
        <span class="pill">Margin of Error</span>
        <span class="pill">Structure</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 3 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/critical-values-z-and-t/">
          Critical Values: z and t
        </a>
      </h3>

      <p>
        Understand critical values,
        confidence levels,
        and why z and t distributions are used.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">z</span>
        <span class="pill">t</span>
        <span class="pill">Critical Values</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/critical-values-z-and-t/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 4 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/ci-for-mean-sigma-known-z/">
          CI for a Mean (σ Known): z-Interval
        </a>
      </h3>

      <p>
        Construct confidence intervals for a population mean
        when the population standard deviation is known.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Mean</span>
        <span class="pill">z-Interval</span>
        <span class="pill">Estimation</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/ci-for-mean-sigma-known-z/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 5 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/">
          CI for a Mean (σ Unknown): t-Interval
        </a>
      </h3>

      <p>
        Use sample variability and t critical values
        to construct confidence intervals for means.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Mean</span>
        <span class="pill">t-Interval</span>
        <span class="pill">Degrees of Freedom</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 6 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/conditions-normality-clt-independence/">
          Conditions for Valid CIs
        </a>
      </h3>

      <p>
        Learn the assumptions required for confidence intervals
        and how to assess them in practice.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Conditions</span>
        <span class="pill">CLT</span>
        <span class="pill">Validity</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/conditions-normality-clt-independence/"
      >
        Open lesson
      </a>

    </div>

<!-- LESSON 7 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/ci-for-proportion/">
          CI for a Proportion
        </a>
      </h3>

      <p>
        Construct confidence intervals for population proportions
        and understand the success–failure condition.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Proportion</span>
        <span class="pill">SE</span>
        <span class="pill">Conditions</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/ci-for-proportion/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 8 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/ci-for-difference-of-means-independent/">
          CI for Difference of Means (Independent Samples)
        </a>
      </h3>

      <p>
        Compare two population means using confidence intervals
        for independent samples.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Two Samples</span>
        <span class="pill">Means</span>
        <span class="pill">Comparison</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/ci-for-difference-of-means-independent/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 9 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/ci-for-difference-of-proportions/">
          CI for Difference of Proportions
        </a>
      </h3>

      <p>
        Estimate and interpret differences between two population proportions.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Proportions</span>
        <span class="pill">Comparison</span>
        <span class="pill">Inference</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/ci-for-difference-of-proportions/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 10 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/ci-for-paired-mean-difference/">
          CI for Paired Data (Mean of Differences)
        </a>
      </h3>

      <p>
        Learn how paired designs are analyzed
        through intervals for difference scores.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Paired Data</span>
        <span class="pill">Differences</span>
        <span class="pill">t-Interval</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/ci-for-paired-mean-difference/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 11 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/width-and-precision-what-controls/">
          CI Width and Precision: What Controls It?
        </a>
      </h3>

      <p>
        Learn how sample size,
        variability,
        and confidence level affect interval width.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Precision</span>
        <span class="pill">Sample Size</span>
        <span class="pill">Width</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/width-and-precision-what-controls/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 12 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/common-mistakes-and-interpretation/">
          Interpretation and Common Mistakes
        </a>
      </h3>

      <p>
        Learn correct interval interpretation
        and avoid common misconceptions about confidence.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Interpretation</span>
        <span class="pill">Mistakes</span>
        <span class="pill">Reporting</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/common-mistakes-and-interpretation/"
      >
        Open lesson
      </a>

    </div>

  </div>

</section>

<!-- BLOCK MAP -->

<section class="section section-slim">

  <div class="callout">

    <div class="callout-copy" style="min-width:0;">

      <h2>How this block fits into inference</h2>

      <p>
        Confidence intervals are the first major inferential tool.
        They combine estimation and uncertainty into a single framework,
        providing information about both plausible parameter values and estimation precision.
      </p>

      <div class="table-wrap">

        <table>

          <thead>

            <tr>
              <th>Concept</th>
              <th>Why it matters later</th>
            </tr>

          </thead>

          <tbody>

            <tr>
              <td>Confidence Level</td>
              <td>Controls long-run coverage of interval procedures</td>
            </tr>

            <tr>
              <td>Margin of Error</td>
              <td>Quantifies uncertainty around estimates</td>
            </tr>

            <tr>
              <td>Critical Values</td>
              <td>Connect sampling distributions to inference</td>
            </tr>

            <tr>
              <td>Standard Error</td>
              <td>Determines interval width and precision</td>
            </tr>

            <tr>
              <td>Interval Interpretation</td>
              <td>Foundation for correct statistical reporting</td>
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

        <li>Understand confidence intervals as long-run coverage procedures</li>

        <li>Use the universal estimate ± margin of error framework</li>

        <li>Choose appropriate z and t critical values</li>

        <li>Construct intervals for means, proportions, and comparisons</li>

        <li>Check assumptions required for valid confidence intervals</li>

        <li>Interpret interval width and statistical precision correctly</li>

        <li>Avoid common confidence interval misconceptions</li>

        <li>Prepare for Hypothesis Testing</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next block</div>

        <div class="mini-body">
          Continue to <strong>Hypothesis Testing</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          Every confidence interval combines an estimate with a measure of uncertainty.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Big transition</div>

        <div class="mini-body">
          The same sampling distributions used for intervals will power hypothesis tests.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/inference/foundations/">
      ← Previous Block: Inference Foundations
    </a>

    <a class="btn" href="/inference/hypothesis-testing/">
      Next Block: Hypothesis Testing →
    </a>

  </div>

</section>

<!-- CONTINUE READING SCRIPT -->

<script>
(function () {

  try {

    const KEY =
      "esa_continue_inference_confidence_intervals_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    // Trust only exact published lesson hrefs in this block's own lesson cards.
    // Do not allow external schemes, traversal, query strings, anchors, or other blocks.
    const published = new Set(
      Array.from(document.querySelectorAll("#lessons .lesson-card h3 a[href]"),
        link => link.getAttribute("href"))
        .filter(url => typeof url === "string" &&
          /^\/inference\/confidence-intervals\/[a-z0-9-]+\/$/.test(url))
    );
    if (!data || typeof data.url !== "string" ||
        typeof data.label !== "string" || !data.label.trim() ||
        data.label.length > 200 || !published.has(data.url)) return;

    const wrap =
      document.getElementById(
        "continue-reading-inference-ci"
      );

    const label =
      document.getElementById(
        "continue-reading-inference-ci-label"
      );

    const btn =
      document.getElementById(
        "continue-reading-inference-ci-btn"
      );

    if (!wrap || !label || !btn) return;

    const strong = document.createElement("strong");
    strong.textContent = data.label;
    label.replaceChildren("You last visited: ", strong);

    btn.href = data.url;

    wrap.style.display = "block";

  } catch (e) {}

})();
</script>