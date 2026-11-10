---
layout: default
title: Practical Significance
description: Learn why statistical significance does not necessarily imply real-world importance and how practical significance complements hypothesis testing.
permalink: /inference/hypothesis-testing/practical-significance/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_hypothesis_testing_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/hypothesis-testing/practical-significance/",
    label: "Statistical vs Practical Significance",
    ts: Date.now()
  }));
  } catch (_) {
    // Lesson remains usable if persistent storage is denied.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 3</span>
      <span class="badge">Hypothesis Testing</span>
      <span class="badge">Interpretation</span>
    </div>

    <h1>Practical Significance</h1>

    <p class="lead">
      Statistical significance answers whether an effect is detectable.
    </p>

    <p class="lead">
      Practical significance answers whether that effect is large enough to matter in the real world.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/hypothesis-testing/ci-and-test-connection/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/classical-tests/">
         Next Block: Classical Tests →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

<section class="concept-box" id="esa-practical-significance-lab" aria-labelledby="esa-ps-heading">
<h2 id="esa-ps-heading">Interactive Statistical vs. Practical Significance Explorer</h2>
<p>Use a one-sample mean difference and a <strong>context-defined absolute practical threshold in the original units</strong>. The test uses the Student t distribution with sample SD and a two-sided null mean. Cohen's d here is the observed mean difference divided by sample SD; it is not itself a decision about practical importance.</p>
<div class="esa-ps-grid">
<div><label for="esa-ps-n">Sample size n</label><input type="number" min="2" max="1000000" step="1" value="400" id="esa-ps-n" aria-describedby="esa-ps-error"></div>
<div><label for="esa-ps-mean">Sample mean</label><input type="number" step="any" value="0.2" id="esa-ps-mean" aria-describedby="esa-ps-error"></div>
<div><label for="esa-ps-sd">Sample standard deviation s</label><input type="number" min="0" step="any" value="1" id="esa-ps-sd" aria-describedby="esa-ps-error"></div>
<div><label for="esa-ps-mu0">Null mean μ₀</label><input type="number" step="any" value="0" id="esa-ps-mu0" aria-describedby="esa-ps-error"></div>
<div><label for="esa-ps-threshold">Minimum practically important absolute difference</label><input type="number" min="0" step="any" value="0.5" id="esa-ps-threshold" aria-describedby="esa-ps-error"></div>
</div>
<button type="button" class="btn btn-outline" id="esa-ps-reset">Restore example</button>
<p id="esa-ps-error" role="alert" hidden></p>
<section id="esa-ps-results" role="status" aria-live="polite" aria-atomic="true">
<p>Observed mean difference: <output id="esa-ps-effect">—</output>; Cohen's d: <output id="esa-ps-d">—</output>.</p>
<p>t = <output id="esa-ps-t">—</output>, df = <output id="esa-ps-df">—</output>, two-sided p = <output id="esa-ps-p">—</output>.</p>
<p>95% confidence interval for the difference: [<output id="esa-ps-low">—</output>, <output id="esa-ps-high">—</output>].</p>
<p id="esa-ps-statistical"></p><p id="esa-ps-practical"></p>
<svg id="esa-ps-graph" viewBox="0 0 480 128" role="img" aria-label="Mean-difference confidence interval compared with practical thresholds" style="display:block;max-width:100%;width:100%;height:auto"></svg>
<p id="esa-ps-interpret"></p>
</section>
<p class="muted-mini">Assumes independent observations, appropriate sampling, and sufficient normality or robust approximation for the Student t procedure. This is an illustrative comparison, not a formal equivalence test. The threshold should be specified based on the research setting.</p>
</section>
<style>#esa-practical-significance-lab{max-width:100%;min-width:0;overflow-wrap:anywhere;box-sizing:border-box}#esa-practical-significance-lab .esa-ps-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,185px),1fr));gap:12px;margin:14px 0}#esa-practical-significance-lab label{display:block;font-weight:650;margin-bottom:6px}#esa-practical-significance-lab input{width:100%;max-width:100%;box-sizing:border-box;padding:9px;font:inherit}#esa-practical-significance-lab [hidden]{display:none!important}#esa-practical-significance-lab :is(input,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}</style>
<script defer src="/js/student-t-one-sample-explorer.js"></script>
<script defer src="/js/practical-significance-explorer.js"></script>

    <h2>The Missing Question</h2>

    <p>
      Hypothesis tests tell us whether the data provide evidence against a null hypothesis.
    </p>

    <p>
      However, an important question often remains:
    </p>

    <div class="example-box">

      <p>
        Even if the effect is real, is it important?
      </p>
    </div>

    <p>
      This question leads to the concept of practical significance.
    </p>

    <h2>Statistical vs Practical Significance</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Concept</th>
            <th>Question Answered</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Statistical Significance</td>
            <td>Is there evidence of an effect?</td>
          </tr>

          <tr>
            <td>Practical Significance</td>
            <td>Is the effect large enough to matter?</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      These concepts are related but fundamentally different.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose a new medication lowers blood pressure by:
    </p>

    <div class="example-box">

      <p>
        0.4 mmHg
      </p>
    </div>

    <p>
      A very large study produces:
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
      But a reduction of only 0.4 mmHg may be clinically unimportant.
    </p>

    <p>
      Statistical significance alone does not guarantee practical value.
    </p>

    <h2>Why Large Samples Matter</h2>

    <p>
      Large samples reduce standard errors.
    </p>

    <p>
      As sample size grows,
      even tiny effects can become statistically significant.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Statistical significance depends on both effect size and sample size.
      </p>

    </div>

    <h2>The Opposite Situation</h2>

    <p>
      Consider a small pilot study.
    </p>

    <p>
      The treatment improves outcomes substantially,
      but only a few participants are included.
    </p>

    <div class="example-box">

      <p>
        Large effect
      </p>

      <p>
        Small sample
      </p>

      <p>
        p = 0.08
      </p>

    </div>

    <p>
      The result is not statistically significant at:
    </p>

    
    \[
    \alpha=0.05
    \]


    <p>
      Yet the effect may still be practically important.
    </p>

    <h2>Evidence and Importance Are Different</h2>

    <p>
      Statistical significance measures evidence against:
    </p>

    
    \[
    H_0\ \text{(null hypothesis)}
    \]


    <p>
      Practical significance measures usefulness, impact, or relevance.
    </p>

    <p>
      One does not automatically imply the other.
    </p>

    <h2>Where Practical Significance Appears</h2>

    <div class="example-box">

      <p>
        Medicine: Is the treatment benefit clinically meaningful?
      </p>

      <p>
        Business: Is the revenue increase worth the cost?
      </p>

      <p>
        Education: Is the score improvement educationally important?
      </p>

      <p>
        Manufacturing: Is the quality improvement operationally valuable?
      </p>

    </div>

    <h2>The Role of Effect Size</h2>

    <p>
      Effect size is often the primary tool for assessing practical significance.
    </p>

    <p>
      Unlike p-values,
      effect sizes describe magnitude.
    </p>

    <div class="concept-box">

      <strong>Effect size answers:</strong>

      <p>
        How large is the effect?
      </p>

    </div>

    <h2>Confidence Intervals Help Too</h2>

    <p>
      Confidence intervals provide information about:
    </p>

    <ul class="bullets">

      <li>Effect size</li>

      <li>Precision</li>

      <li>Uncertainty</li>

      <li>Plausible values</li>

    </ul>

    <p>
      This makes them particularly useful for evaluating practical significance.
    </p>

    <h2>Example Using a Confidence Interval</h2>

    <p>
      Suppose a treatment effect has a 95% confidence interval:
    </p>

    <div class="example-box">

      <p>
        (0.1, 0.3)
      </p>
    </div>

    <p>
      The interval excludes zero,
      suggesting statistical significance.
    </p>

    <p>
      However,
      all plausible effects are very small.
    </p>

    <p>
      Practical importance may still be limited.
    </p>

    <h2>Domain Knowledge Matters</h2>

    <p>
      Practical significance cannot be determined by statistics alone.
    </p>

    <p>
      Subject-matter expertise is required.
    </p>

    <div class="example-box">

      <p>
        A 1% improvement may be trivial in one setting and enormously valuable in another.
      </p>
    </div>

    <h2>Minimum Important Difference</h2>

    <p>
      Many fields define a threshold for meaningful effects.
    </p>

    <div class="concept-box">

      <strong>Minimum Important Difference:</strong>

      <p>
        The smallest effect size considered practically meaningful.
      </p>

    </div>

    <p>
      Effects below this threshold may have little practical value even if statistically significant.
    </p>

    <h2>The Danger of Focusing Only on p-Values</h2>

    <p>
      A sole focus on statistical significance can lead to misleading conclusions.
    </p>

    <div class="example-box">

      <p>
        Significant but trivial effects may be overstated.
      </p>

      <p>
        Meaningful but underpowered effects may be overlooked.
      </p>

    </div>

    <p>
      Good statistical practice considers both evidence and magnitude.
    </p>

    <h2>A Better Reporting Strategy</h2>

    <p>
      Many researchers report:
    </p>

    <ul class="bullets">

      <li>p-values</li>

      <li>Effect sizes</li>

      <li>Confidence intervals</li>

    </ul>

    <p>
      Together these provide a fuller picture of the findings.
    </p>

    <h2>Decision-Making Perspective</h2>

    <p>
      Real-world decisions are rarely based on statistical significance alone.
    </p>

    <p>
      Decision-makers often consider:
    </p>

    <ul class="bullets">

      <li>Effect magnitude</li>

      <li>Cost</li>

      <li>Risk</li>

      <li>Feasibility</li>

      <li>Practical consequences</li>

    </ul>

    <p>
      Statistics provides evidence,
      but decisions require broader context.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Hypothesis testing is a valuable tool for detecting effects.
    </p>

    <p>
      Yet detecting an effect is only the first step.
    </p>

    <p>
      Researchers must also evaluate whether the effect is large enough to matter.
    </p>

    <p>
      Practical significance bridges the gap between statistical inference and real-world decision-making.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Statistical significance tells us whether an effect is detectable. Practical significance tells us whether the effect is meaningful. Good statistical reasoning requires considering both.
      </p>

    </div>

    <h2>Completing the Block</h2>

    <p>
      This concludes the Foundations of Hypothesis Testing block.
    </p>

    <p>
      We have developed the logic of null hypotheses, p-values, significance levels, decision errors, power, and interpretation.
    </p>

    <p>
      The next block applies these ideas to specific inferential procedures used throughout statistics.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Statistical significance and practical significance are different concepts</li>

        <li>Large samples can make tiny effects statistically significant</li>

        <li>Small studies can miss meaningful effects</li>

        <li>Effect size measures practical magnitude</li>

        <li>Confidence intervals help evaluate practical importance</li>

        <li>Subject-matter knowledge is essential for judging significance in practice</li>

        <li>Meaningful decisions require more than p-values alone</li>

        <li>Good inference considers evidence, uncertainty, and real-world impact together</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/ci-and-test-connection/">
         ← Previous: Confidence Intervals and Tests
      </a>

      <a class="btn"
         href="/inference/classical-tests/">
         Next Block: Classical Tests →
      </a>

    </div>

  </div>

</section>