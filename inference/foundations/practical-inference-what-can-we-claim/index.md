---
layout: default
title: Practical Inference — What Can We Claim?
description: Learn how to decide what statistical claims are justified based on sampling design, assumptions, uncertainty, and evidence.
permalink: /inference/foundations/practical-inference-what-can-we-claim/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_foundations_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/foundations/practical-inference-what-can-we-claim/",
    label: "Practical Inference — What Can We Claim?",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 1</span>
      <span class="badge">Foundations</span>
      <span class="badge">Final Lesson</span>
    </div>

    <h1>Practical Inference — What Can We Claim?</h1>

    <p class="lead">
      Statistical inference is not only about formulas.
    </p>

    <p class="lead">
      It is also about knowing what conclusions are justified, what assumptions are required, and where the limits of the data lie.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/foundations/sampling-bias-vs-statistical-bias/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/">
         Next Block: Confidence Intervals →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Central Question</h2>

    <p>
      Every inferential analysis should end with one question:
    </p>

    <div class="example-box">

      <p>
        What can we legitimately claim from these data?
      </p>

    </div>

    <p>
      A statistical result is only useful when interpreted within the limits of the design, assumptions, and uncertainty.
    </p>

    <h2>Inference Depends on Design</h2>

    <p>
      The strength of a statistical claim depends heavily on how the data were collected.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Design Feature</th>
            <th>Supports</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Random sampling</td>
            <td>Generalization to a population</td>
          </tr>

          <tr>
            <td>Random assignment</td>
            <td>Causal conclusions</td>
          </tr>

          <tr>
            <td>Large sample size</td>
            <td>More precise estimates</td>
          </tr>

          <tr>
            <td>Representative sampling frame</td>
            <td>Reduced sampling bias</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Generalization Claims</h2>

    <p>
      Generalization means extending conclusions from a sample to a broader population.
    </p>

    <p>
      This is most justified when the sample was randomly selected from the target population.
    </p>

    <div class="concept-box">

      <strong>Rule:</strong>

      <p>
        Random sampling supports population generalization.
      </p>

    </div>

    <h2>Causal Claims</h2>

    <p>
      Causal claims are stronger than descriptive or associational claims.
    </p>

    <p>
      They require evidence that one variable actually produces a change in another.
    </p>

    <div class="concept-box">

      <strong>Rule:</strong>

      <p>
        Random assignment supports causal inference.
      </p>

    </div>

    <p>
      Without random assignment or a strong causal design,
      statistical association should not be interpreted as causation.
    </p>

    <h2>Association Claims</h2>

    <p>
      Many studies can support association but not causation.
    </p>

    <div class="example-box">

      <p>
        Higher study time is associated with higher exam scores.
      </p>

      <p>
        Higher income is associated with longer life expectancy.
      </p>

    </div>

    <p>
      These statements describe relationships,
      but they do not automatically prove cause and effect.
    </p>

    <h2>Uncertainty Must Be Reported</h2>

    <p>
      Inferential claims should include uncertainty.
    </p>

    <p>
      This uncertainty may appear as:
    </p>

    <ul class="bullets">

      <li>Standard errors</li>

      <li>Confidence intervals</li>

      <li>Margins of error</li>

      <li>p-values</li>

    </ul>

    <p>
      Reporting only a point estimate can make results seem more certain than they are.
    </p>

    <h2>Precision Matters</h2>

    <p>
      A result can be statistically valid but imprecise.
    </p>

    <div class="example-box">

      <p>
        Estimated effect = 10
      </p>

      <p>
        Confidence interval = −5 to 25
      </p>

    </div>

    <p>
      The estimate suggests a positive effect,
      but the interval is wide and includes many plausible values.
    </p>

    <h2>Statistical Significance Is Not Everything</h2>

    <p>
      Statistical significance tells us whether data are unusual under a null model.
    </p>

    <p>
      It does not automatically tell us whether the result is meaningful in practice.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Practical importance and statistical significance are different concepts.
      </p>

    </div>

    <h2>Check the Assumptions</h2>

    <p>
      Before trusting an inferential result,
      ask whether the assumptions are reasonable.
    </p>

    <ul class="bullets">

      <li>Was the sample representative?</li>

      <li>Were observations independent?</li>

      <li>Was the estimator appropriate?</li>

      <li>Was the uncertainty calculation valid?</li>

      <li>Were outliers or missing data handled transparently?</li>

    </ul>

    <h2>What Can We Claim?</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Evidence</th>
            <th>Reasonable Claim</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Convenience sample</td>
            <td>Describe the observed sample cautiously</td>
          </tr>

          <tr>
            <td>Random sample</td>
            <td>Generalize to the sampled population</td>
          </tr>

          <tr>
            <td>Randomized experiment</td>
            <td>Make stronger causal claims</td>
          </tr>

          <tr>
            <td>Observational association</td>
            <td>Claim association, not causation</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Common Overclaims</h2>

    <p>
      Statistical reports often go wrong by claiming more than the data support.
    </p>

    <div class="example-box">

      <p>
        Claiming causation from observational data
      </p>

      <p>
        Generalizing from an unrepresentative sample
      </p>

      <p>
        Ignoring uncertainty
      </p>

      <p>
        Treating significance as practical importance
      </p>

    </div>

    <h2>The Responsible Inference Checklist</h2>

    <ol>

      <li>Define the target population.</li>

      <li>Identify the parameter or claim.</li>

      <li>Evaluate the sampling design.</li>

      <li>Check independence and assumptions.</li>

      <li>Report the estimate and uncertainty.</li>

      <li>State conclusions with appropriate caution.</li>

    </ol>

    <h2>What This Block Established</h2>

    <p>
      This block introduced the foundation of statistical inference.
    </p>

    <ul class="bullets">

      <li>Populations and parameters</li>

      <li>Statistics as random variables</li>

      <li>Estimators and estimates</li>

      <li>Sampling distributions</li>

      <li>Standard errors</li>

      <li>Bias and estimator quality</li>

      <li>Confidence and significance</li>

      <li>Sampling assumptions</li>

    </ul>

    <p>
      These ideas support every inferential method that follows.
    </p>

    <h2>The Big Picture</h2>

    <p>
      Statistical inference is a disciplined way of learning from incomplete data.
    </p>

    <p>
      It does not remove uncertainty,
      but it helps quantify it.
    </p>

    <p>
      It does not guarantee truth,
      but it helps determine which claims are supported by evidence.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        A good inferential conclusion is not just statistically calculated. It is justified by the data design, assumptions, uncertainty, and scope of the research question.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      The next block focuses on confidence intervals.
    </p>

    <p>
      You will learn how to construct intervals,
      interpret confidence levels,
      choose critical values,
      and communicate uncertainty clearly.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Block 1 Takeaways</h2>

      <ul class="bullets">

        <li>Inference uses samples to learn about population parameters</li>

        <li>Statistics vary because samples vary</li>

        <li>Sampling distributions describe estimator behavior</li>

        <li>Standard errors measure inferential uncertainty</li>

        <li>Confidence intervals and tests rely on the same foundation</li>

        <li>Random sampling supports generalization</li>

        <li>Random assignment supports causal claims</li>

        <li>Valid claims must respect design, assumptions, and uncertainty</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/foundations/sampling-bias-vs-statistical-bias/">
         ← Previous: Sampling Bias vs Statistical Bias
      </a>

      <a class="btn"
         href="/inference/confidence-intervals/">
         Next Block: Confidence Intervals →
      </a>

    </div>

  </div>

</section>