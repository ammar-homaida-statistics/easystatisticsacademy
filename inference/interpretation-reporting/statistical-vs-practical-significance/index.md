---
layout: default
title: Statistical vs Practical Significance
description: Learn the difference between statistical significance and practical significance, and why both are necessary for sound decision-making.
permalink: /inference/interpretation-reporting/statistical-vs-practical-significance/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_interpretation_reporting_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/interpretation-reporting/statistical-vs-practical-significance/",
    label: "Statistical vs Practical Significance",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 6</span>
      <span class="badge">Interpretation & Reporting</span>
      <span class="badge">Decision Making</span>
    </div>

    <h1>Statistical vs Practical Significance</h1>

    <p class="lead">
      Statistical significance tells us whether evidence exists against a null hypothesis.
    </p>

    <p class="lead">
      Practical significance asks whether the observed effect is large enough to matter in the real world.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/interpretation-reporting/p-values-what-they-mean/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/interpretation-reporting/interpreting-confidence-intervals/">
         Next: Interpreting Confidence Intervals →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Two Different Questions</h2>

    <p>
      Statistical analysis often answers two separate questions:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Question</th>
            <th>Answer Provided By</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Is there evidence of an effect?</td>
            <td>Statistical significance</td>
          </tr>

          <tr>
            <td>Is the effect important?</td>
            <td>Practical significance</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      These questions are related, but they are not the same.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        An effect can be statistically significant without being practically important, and practically important without being statistically significant.
      </p>

    </div>

    <h2>What Is Statistical Significance?</h2>

    <p>
      Statistical significance concerns evidence against the null hypothesis.
    </p>

    <p>
      A result is often called statistically significant when:
    </p>

    <div class="example-box">

      <p>
        p ≤ α
      </p>
    </div>

    <p>
      Under this framework, the observed data would be considered unlikely if the null hypothesis were true.
    </p>

    <h2>What Statistical Significance Does NOT Tell Us</h2>

    <p>
      A statistically significant result does not automatically tell us:
    </p>

    <ul class="bullets">

      <li>How large the effect is</li>

      <li>Whether the effect is meaningful</li>

      <li>Whether the effect justifies action</li>

      <li>Whether the effect has practical consequences</li>

    </ul>

    <h2>What Is Practical Significance?</h2>

    <p>
      Practical significance concerns real-world importance.
    </p>

    <p>
      It asks:
    </p>

    <div class="example-box">

      <p>
        Is the observed effect large enough to matter?
      </p>
    </div>

    <p>
      The answer depends on context, goals, costs, benefits, and consequences.
    </p>

    <h2>A Medical Example</h2>

    <p>
      Suppose a new medication reduces blood pressure by:
    </p>

    <div class="example-box">

      <p>
        0.2 mmHg
      </p>
    </div>

    <p>
      With a very large sample size, this difference might produce:
    </p>

    <div class="example-box">

      <p>
        p &lt; 0.001
      </p>
    </div>

    <p>
      The result is statistically significant.
    </p>

    <p>
      However, a reduction of only 0.2 mmHg may have little clinical importance.
    </p>

    <h2>A Business Example</h2>

    <p>
      Suppose a website redesign increases conversion rates from:
    </p>

    <div class="example-box">

      <p>
        10.00% to 10.02%
      </p>
    </div>

    <p>
      A large dataset might detect this difference statistically.
    </p>

    <p>
      Whether it matters financially depends on implementation costs and business objectives.
    </p>

    <h2>The Role of Sample Size</h2>

    <p>
      Sample size strongly influences statistical significance.
    </p>

    <p>
      Larger samples make it easier to detect small effects.
    </p>

    <div class="concept-box">

      <strong>Important consequence:</strong>

      <p>
        Very large samples can make tiny effects statistically significant.
      </p>

    </div>

    <h2>An Illustration</h2>

    <p>
      Consider two effects:
    </p>

      

    <p>
      Statistical significance focuses on detectability.
    </p>

    <p>
      Practical significance focuses on magnitude and consequences.
    </p>

    <h2>Effect Size Bridges the Gap</h2>

    <p>
      Effect size measures the magnitude of an effect.
    </p>

    <p>
      Unlike p-values, effect sizes directly address practical importance.
    </p>

    <p>
      Common measures include:
    </p>

    <ul class="bullets">

      <li>Cohen's d</li>

      <li>Correlation coefficients</li>

      <li>Odds ratios</li>

      <li>Risk differences</li>

      <li>Mean differences</li>

    </ul>

    <h2>Confidence Intervals Also Help</h2>

    <p>
      Confidence intervals provide information about:
    </p>

    <ul class="bullets">

      <li>Magnitude of effects</li>

      <li>Precision of estimates</li>

      <li>Plausible ranges of values</li>

    </ul>

    <p>
      They often provide more insight than a significance decision alone.
    </p>

    <h2>A Non-Significant but Important Effect</h2>

    <p>
      Suppose a pilot study finds:
    </p>

    <div class="example-box">

      <p>
        Large estimated improvement
      </p>

      <p>
        p = 0.08
      </p>

    </div>

    <p>
      The study fails to reach conventional significance.
    </p>

    <p>
      However, the estimated effect may still be practically important.
    </p>

    <p>
      The study might simply lack sufficient power.
    </p>

    <h2>Decision Making Requires Context</h2>

    <p>
      Practical significance depends on:
    </p>

    <ul class="bullets">

      <li>Scientific importance</li>

      <li>Economic impact</li>

      <li>Clinical relevance</li>

      <li>Policy consequences</li>

      <li>Risk considerations</li>

    </ul>

    <p>
      Statistics alone cannot determine these judgments.
    </p>

    <h2>Why Researchers Report More Than P-Values</h2>

    <p>
      Modern reporting often includes:
    </p>

    <ul class="bullets">

      <li>P-values</li>

      <li>Effect sizes</li>

      <li>Confidence intervals</li>

      <li>Study limitations</li>

    </ul>

    <p>
      Together these provide a fuller picture of the evidence.
    </p>

    <h2>Interpreting Results Responsibly</h2>

    <p>
      When reading research findings, it is useful to ask:
    </p>

    <ol>

      <li>Is the result statistically significant?</li>

      <li>How large is the effect?</li>

      <li>Is the effect practically meaningful?</li>

      <li>How precise is the estimate?</li>

    </ol>

    <p>
      These questions lead to more thoughtful interpretation.
    </p>

    <h2>Common Mistakes</h2>

    <div class="concept-box">

      <strong>Avoid these errors:</strong>

      <ul class="bullets">

        <li>Equating significance with importance</li>

        <li>Ignoring effect size</li>

        <li>Ignoring confidence intervals</li>

        <li>Making decisions based only on p-values</li>

      </ul>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      Statistical significance and practical significance serve different purposes.
    </p>

    <p>
      Statistical significance evaluates evidence against a null hypothesis.
    </p>

    <p>
      Practical significance evaluates whether an effect matters in the real world.
    </p>

    <p>
      Responsible interpretation requires considering both.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Statistical significance addresses whether evidence exists for an effect, while practical significance addresses whether the effect is important. Sound conclusions require attention to both questions.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Confidence intervals provide one of the most useful tools for understanding both uncertainty and effect magnitude.
    </p>

    <p>
      Yet confidence intervals are frequently misunderstood.
    </p>

    <p>
      The next lesson focuses on how to interpret confidence intervals correctly and avoid common mistakes.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Statistical significance and practical significance are different concepts</li>

        <li>Statistical significance focuses on evidence against H₀</li>

        <li>Practical significance focuses on real-world importance</li>

        <li>Large samples can make tiny effects statistically significant</li>

        <li>Effect size helps assess practical importance</li>

        <li>Confidence intervals provide information about magnitude and uncertainty</li>

        <li>Decision making requires context beyond p-values</li>

        <li>Good reporting includes significance measures, effect sizes, and confidence intervals</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/interpretation-reporting/p-values-what-they-mean/">
         ← Previous: P-Values: What They Mean
      </a>

      <a class="btn"
         href="/inference/interpretation-reporting/interpreting-confidence-intervals/">
         Next: Interpreting Confidence Intervals →
      </a>

    </div>

  </div>

</section>