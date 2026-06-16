---
layout: default
title: Assumptions vs Robustness Mindset
description: Learn why statistical methods rely on assumptions, what robustness means, and how to think critically about conclusions when assumptions are imperfect.
permalink: /inference/assumptions-robustness/assumptions-vs-robustness-mindset/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_assumptions_robustness_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/assumptions-robustness/assumptions-vs-robustness-mindset/",
    label: "Assumptions vs Robustness Mindset",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 7</span>
      <span class="badge">Assumptions & Robustness</span>
      <span class="badge">Foundations</span>
    </div>

    <h1>Assumptions vs Robustness Mindset</h1>

    <p class="lead">
      Every statistical method relies on assumptions.
    </p>

    <p class="lead">
      However, useful statistical thinking is not about finding methods with perfect assumptions—it is about understanding how sensitive conclusions are when assumptions are not perfectly satisfied.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/assumptions-robustness/">
         ← Block Home
      </a>

      <a class="btn btn-outline"
         href="/inference/assumptions-robustness/model-assumptions-vs-design-assumptions/">
         Next: Model Assumptions vs Design Assumptions →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Assumptions Exist</h2>

    <p>
      Statistical methods are mathematical tools.
    </p>

    <p>
      To produce valid conclusions, those tools typically require certain conditions to hold.
    </p>

    <p>
      These conditions are called assumptions.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Assumptions connect mathematical theory to real-world data.
      </p>

    </div>

    <h2>A Familiar Example</h2>

    <p>
      Many confidence intervals and hypothesis tests rely on assumptions such as:
    </p>

    <ul class="bullets">

      <li>Random sampling</li>

      <li>Independence</li>

      <li>Approximate normality</li>

      <li>Sufficient sample size</li>

    </ul>

    <p>
      These assumptions help justify the formulas used in inference.
    </p>

    <h2>A Common Misconception</h2>

    <p>
      Students sometimes believe that statistical methods are either:
    </p>

    <ul class="bullets">

      <li>Completely valid</li>

      <li>Completely invalid</li>

    </ul>

    <p>
      depending on whether assumptions hold exactly.
    </p>

    <p>
      Real statistical practice is usually more nuanced.
    </p>

    <h2>The Reality of Data</h2>

    <p>
      Real datasets are rarely perfect.
    </p>

    <p>
      They may contain:
    </p>

    <ul class="bullets">

      <li>Outliers</li>

      <li>Missing values</li>

      <li>Skewed distributions</li>

      <li>Measurement error</li>

      <li>Small assumption violations</li>

    </ul>

    <p>
      Yet useful analyses are still possible.
    </p>

    <h2>What Is Robustness?</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Robustness is the ability of a statistical method to continue producing reliable results when assumptions are not perfectly satisfied.
      </p>

    </div>

    <p>
      Some methods are highly sensitive to violations.
    </p>

    <p>
      Others perform well even when conditions are only approximately met.
    </p>

    <h2>A Practical Analogy</h2>

    <p>
      Consider a bridge designed to support vehicles up to a certain weight.
    </p>

    <p>
      A small increase beyond the design target may not cause failure.
    </p>

    <p>
      Similarly, a statistical method may tolerate minor assumption violations without producing misleading conclusions.
    </p>

    <h2>Robust Does Not Mean Assumption-Free</h2>

    <p>
      A common misunderstanding is that robust methods require no assumptions.
    </p>

    <p>
      In reality:
    </p>

    <div class="example-box">

      <p>
        Robust methods still have assumptions—they are simply less sensitive to certain violations.
      </p>
    </div>

    <h2>Not All Assumptions Matter Equally</h2>

    <p>
      Some assumptions are critically important.
    </p>

    <p>
      Others have only a modest influence on results.
    </p>

    <p>
      Statistical judgment often involves determining:
    </p>

    <div class="example-box">

      <p>
        Which assumptions matter most in a particular analysis?
      </p>
    </div>

    <h2>An Example: Normality</h2>

    <p>
      Many classical methods assume normally distributed data.
    </p>

    <p>
      Yet with sufficiently large samples:
    </p>

    <ul class="bullets">

      <li>Confidence intervals often remain accurate</li>

      <li>Hypothesis tests often remain reliable</li>

      <li>The Central Limit Theorem provides protection</li>

    </ul>

    <p>
      This is an example of robustness.
    </p>

    <h2>An Example: Independence</h2>

    <p>
      Independence violations can be much more serious.
    </p>

    <p>
      If observations are strongly related:
    </p>

    <ul class="bullets">

      <li>Standard errors may be incorrect</li>

      <li>P-values may be misleading</li>

      <li>Confidence intervals may be inaccurate</li>

    </ul>

    <p>
      Some assumptions are harder to violate safely.
    </p>

    <h2>The Robustness Mindset</h2>

    <p>
      Instead of asking:
    </p>

    <div class="example-box">

      <p>
        Are the assumptions perfectly satisfied?
      </p>
    </div>

    <p>
      analysts often ask:
    </p>

    <div class="example-box">

      <p>
        Would the conclusion change if the assumptions were slightly wrong?
      </p>
    </div>

    <p>
      This question is often more useful.
    </p>

    <h2>Sensitivity Thinking</h2>

    <p>
      Robustness is closely connected to sensitivity analysis.
    </p>

    <p>
      Analysts may compare:
    </p>

    <ul class="bullets">

      <li>Different models</li>

      <li>Different assumptions</li>

      <li>Different subsets of data</li>

    </ul>

    <p>
      If conclusions remain similar, confidence increases.
    </p>

    <h2>Perfect Assumptions Rarely Exist</h2>

    <p>
      Waiting for perfect assumptions often means never performing an analysis.
    </p>

    <p>
      Real statistical work involves balancing:
    </p>

    <ul class="bullets">

      <li>Theoretical requirements</li>

      <li>Data limitations</li>

      <li>Practical objectives</li>

    </ul>

    <h2>Evidence Is Graduated</h2>

    <p>
      Statistical conclusions are rarely all-or-nothing.
    </p>

    <p>
      Instead, confidence in conclusions often depends on:
    </p>

    <ul class="bullets">

      <li>Data quality</li>

      <li>Assumption plausibility</li>

      <li>Method robustness</li>

      <li>Consistency across analyses</li>

    </ul>

    <h2>A Useful Checklist</h2>

    <p>
      Before trusting a result, ask:
    </p>

    <ol>

      <li>What assumptions does the method require?</li>

      <li>Are those assumptions plausible?</li>

      <li>How severe are any violations?</li>

      <li>How sensitive are the conclusions?</li>

      <li>Would alternative methods give similar answers?</li>

    </ol>

    <h2>Why This Matters</h2>

    <p>
      Statistical methods are tools for learning from imperfect information.
    </p>

    <p>
      Understanding robustness helps prevent:
    </p>

    <ul class="bullets">

      <li>Blind trust in formulas</li>

      <li>Overconfidence in conclusions</li>

      <li>Unnecessary rejection of useful methods</li>

    </ul>

    <h2>The Scientific Perspective</h2>

    <p>
      Science advances through evidence rather than certainty.
    </p>

    <p>
      Robust analyses strengthen evidence because conclusions do not depend entirely on fragile assumptions.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Assumptions are unavoidable in statistical analysis.
    </p>

    <p>
      The important question is not whether assumptions are perfect, but whether conclusions remain trustworthy when assumptions are only approximately true.
    </p>

    <p>
      Robustness provides a framework for answering that question.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Statistical methods rely on assumptions, but useful statistical thinking focuses on robustness. A robust method continues to provide reliable conclusions even when assumptions are not perfectly satisfied.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Not all assumptions arise from the same source.
    </p>

    <p>
      Some assumptions concern statistical models, while others concern how data were collected and how studies were designed.
    </p>

    <p>
      The next lesson explores the distinction between model assumptions and design assumptions, and why both are essential for valid inference.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Every statistical method relies on assumptions</li>

        <li>Real datasets rarely satisfy assumptions perfectly</li>

        <li>Robustness describes resistance to assumption violations</li>

        <li>Robust methods still have assumptions</li>

        <li>Some assumptions are more important than others</li>

        <li>Independence violations are often more serious than mild non-normality</li>

        <li>Sensitivity analysis helps evaluate robustness</li>

        <li>The goal is trustworthy conclusions, not perfect assumptions</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/assumptions-robustness/">
         ← Back to Block Home
      </a>

      <a class="btn"
         href="/inference/assumptions-robustness/model-assumptions-vs-design-assumptions/">
         Next: Model Assumptions vs Design Assumptions →
      </a>

    </div>

  </div>

</section>