---
layout: default
title: Design and Conclusions
description: Learn how study design determines the strength of statistical conclusions and why different designs support different types of claims.
permalink: /applied-statistics/study-design/design-and-conclusions/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_applied_statistics_study_design_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/applied-statistics/study-design/design-and-conclusions/",
    label: "Design and Conclusions",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Applied Statistics</span>
      <span class="badge">Block 2</span>
      <span class="badge">Study Design</span>
      <span class="badge">Inference</span>
    </div>

    <h1>Design and Conclusions</h1>

    <p class="lead">
      Statistical analyses do not automatically justify every type of conclusion.
    </p>

    <p class="lead">
      The strength of a conclusion depends heavily on how the study was designed and how the data were collected.
    </p>

    <p class="lead">
      Understanding this connection helps researchers make claims that are supported by evidence rather than assumptions.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/applied-statistics/study-design/bias-confounding/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/applied-statistics/assumptions/">
         Next: Assumptions →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Conclusions Depend on Design</h2>

    <p>
      Researchers often focus on statistical results such as p-values, confidence intervals, or model coefficients.
    </p>

    <p>
      However, these results can only support conclusions that are consistent with the study design.
    </p>

    <p>
      Strong analyses cannot compensate for fundamental limitations in how data were collected.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Study design determines what kinds of conclusions can reasonably be drawn from statistical evidence.
      </p>

    </div>

    <h2>Different Designs Support Different Claims</h2>

    <p>
      Not all studies provide the same type of evidence.
    </p>

    <p>
      Some designs support causal conclusions, while others primarily support descriptive or associative conclusions.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Design Type</th>
            <th>Primary Conclusion</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Descriptive Survey</td>
            <td>Description</td>
          </tr>

          <tr>
            <td>Cross-Sectional Study</td>
            <td>Association</td>
          </tr>

          <tr>
            <td>Cohort Study</td>
            <td>Association and temporal patterns</td>
          </tr>

          <tr>
            <td>Randomized Experiment</td>
            <td>Causal evidence</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Description Is Not Explanation</h2>

    <p>
      Some studies simply describe populations.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Average income</li>

      <li>Population age distribution</li>

      <li>Voting preferences</li>

    </ul>

    <p>
      These studies summarize characteristics but do not explain why patterns exist.
    </p>

    <h2>Association Is Not Causation</h2>

    <p>
      One of the most important principles in applied statistics is that association does not automatically imply causation.
    </p>

    <p>
      Observing a relationship between two variables does not prove that one causes the other.
    </p>

    <p>
      Confounding variables, reverse causality, and other explanations may exist.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Statistical relationships alone are usually insufficient to establish cause-and-effect conclusions.
      </p>

    </div>

    <h2>A Common Mistake</h2>

    <p>
      Suppose researchers observe that individuals who exercise regularly tend to have lower rates of disease.
    </p>

    <p>
      A cross-sectional study may reveal this association.
    </p>

    <p>
      However, the study alone may not establish that exercise caused the difference.
    </p>

    <p>
      Other factors such as diet, income, or healthcare access may contribute.
    </p>

    <h2>Temporal Order Matters</h2>

    <p>
      To argue that one variable causes another, researchers generally need evidence that:
    </p>

    <ul class="bullets">

      <li>The cause occurs before the effect</li>

      <li>The variables are related</li>

      <li>Alternative explanations are minimized</li>

    </ul>

    <p>
      Some study designs are better suited for demonstrating temporal order than others.
    </p>

    <h2>Why Experiments Are Powerful</h2>

    <p>
      Randomized experiments help researchers control many competing explanations.
    </p>

    <p>
      Because participants are assigned to conditions, observed differences are more plausibly attributed to the intervention.
    </p>

    <p>
      This strengthens causal inference.
    </p>

    <div class="example-box">

      <p>
        Treatment Assigned → Outcome Measured
      </p>
    </div>

    <p>
      The assignment process provides important evidence that is unavailable in many observational studies.
    </p>

    <h2>Observational Studies Still Matter</h2>

    <p>
      Although observational studies often provide weaker causal evidence, they remain extremely valuable.
    </p>

    <p>
      They are frequently used when:
    </p>

    <ul class="bullets">

      <li>Experiments are unethical</li>

      <li>Experiments are impractical</li>

      <li>Researchers need real-world data</li>

      <li>Rare events are being studied</li>

    </ul>

    <p>
      Important scientific discoveries have emerged from observational research.
    </p>

    <h2>Generalization Depends on Sampling</h2>

    <p>
      Conclusions about a broader population require representative sampling.
    </p>

    <p>
      If the sample differs substantially from the population, conclusions may not generalize appropriately.
    </p>

    <p>
      Strong internal evidence alone is not sufficient.
    </p>

    <h2>Internal and External Validity</h2>

    <p>
      Researchers often distinguish between:
    </p>

    <ul class="bullets">

      <li>Internal validity</li>

      <li>External validity</li>

    </ul>

    <p>
      Internal validity concerns whether conclusions are justified within the study itself.
    </p>

    <p>
      External validity concerns whether findings generalize beyond the study.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Concept</th>
            <th>Question</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Internal Validity</td>
            <td>Are conclusions justified for this study?</td>
          </tr>

          <tr>
            <td>External Validity</td>
            <td>Do findings generalize elsewhere?</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Claims Should Match Evidence</h2>

    <p>
      Responsible researchers align their conclusions with the strength of available evidence.
    </p>

    <p>
      Strong claims require strong designs.
    </p>

    <p>
      Weak designs require more cautious interpretations.
    </p>

    <div class="concept-box">

      <strong>Important principle:</strong>

      <p>
        Conclusions should never be stronger than the evidence supporting them.
      </p>

    </div>

    <h2>Evaluating Research Findings</h2>

    <p>
      When reading a study, ask:
    </p>

    <ul class="bullets">

      <li>How were data collected?</li>

      <li>Was the study experimental or observational?</li>

      <li>Could confounding variables explain the results?</li>

      <li>Is the sample representative?</li>

      <li>Do the conclusions match the design?</li>

    </ul>

    <p>
      These questions help assess the credibility of findings.
    </p>

    <h2>Statistical Significance Is Not Enough</h2>

    <p>
      A statistically significant result does not automatically imply an important or causal finding.
    </p>

    <p>
      Significance addresses evidence against a null hypothesis.
    </p>

    <p>
      Study design determines how that evidence should be interpreted.
    </p>

    <h2>Good Design Before Good Analysis</h2>

    <p>
      Effective statistical practice begins with thoughtful design.
    </p>

    <p>
      Researchers who invest effort in sampling, measurement, randomization, and bias reduction create stronger foundations for analysis.
    </p>

    <p>
      The quality of conclusions often depends more on design decisions than on analytical complexity.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        The most sophisticated statistical analysis cannot fully rescue conclusions from a poorly designed study.
      </p>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      Study design and statistical conclusions are inseparable.
    </p>

    <p>
      Researchers must understand not only how to analyze data but also what their data can legitimately support.
    </p>

    <p>
      Strong designs produce stronger evidence, more reliable interpretations, and more credible conclusions.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Statistical conclusions should reflect the strength of the study design. Different designs support different types of claims, and responsible researchers align their conclusions with the evidence available.
      </p>

    </div>

    <h2>Completing the Study Design Block</h2>

    <p>
      You have now completed the Study Design block.
    </p>

    <p>
      In this block, you learned how studies are structured, how samples are selected, how bias and confounding arise, and how design choices influence the conclusions researchers can draw.
    </p>

    <p>
      These concepts form the foundation for evaluating evidence and conducting sound statistical investigations.
    </p>

    <p>
      The next block focuses on assumptions, where you will learn the conditions that statistical methods rely upon and how violations can affect results.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Study design determines the strength of statistical conclusions</li>

        <li>Different designs support different types of claims</li>

        <li>Description, association, and causation are distinct conclusions</li>

        <li>Association alone does not establish causation</li>

        <li>Experiments provide stronger causal evidence than most observational studies</li>

        <li>Sampling affects generalizability and external validity</li>

        <li>Conclusions should match the available evidence</li>

        <li>Strong study design is essential for credible statistical inference</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/applied-statistics/study-design/bias-confounding/">
         ← Previous: Bias and Confounding
      </a>

      <a class="btn"
         href="/applied-statistics/assumptions/">
         Next: Assumptions →
      </a>

    </div>

  </div>

</section>