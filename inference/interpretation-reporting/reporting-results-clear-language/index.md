---
layout: default
title: Reporting Results in Clear Language
description: Learn how to communicate statistical findings accurately, clearly, and effectively for both technical and non-technical audiences.
permalink: /inference/interpretation-reporting/reporting-results-clear-language/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_interpretation_reporting_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/interpretation-reporting/reporting-results-clear-language/",
    label: "Reporting Results in Clear Language",
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
      <span class="badge">Communication</span>
    </div>

    <h1>Reporting Results in Clear Language</h1>

    <p class="lead">
      Statistical analysis is only useful if its results can be understood and interpreted correctly.
    </p>

    <p class="lead">
      Effective communication requires translating technical findings into language that is accurate, clear, and meaningful to the intended audience.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/interpretation-reporting/multiple-testing-and-false-positives/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/interpretation-reporting/tables-figures-and-visual-communication/">
         Next: Tables, Figures, and Visual Communication →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Communication Matters</h2>

    <p>
      A perfectly executed statistical analysis can still fail if the results are communicated poorly.
    </p>

    <p>
      Misleading wording, technical jargon, and incomplete reporting can cause readers to misunderstand important findings.
    </p>

    <div class="concept-box">

      <strong>Goal:</strong>

      <p>
        Report results in a way that is accurate, understandable, and aligned with the evidence.
      </p>

    </div>

    <h2>Statistics Is About Communication</h2>

    <p>
      Statistical work often serves decision-making.
    </p>

    <p>
      Results may be read by:
    </p>

    <ul class="bullets">

      <li>Researchers</li>

      <li>Managers</li>

      <li>Policy makers</li>

      <li>Medical professionals</li>

      <li>The general public</li>

    </ul>

    <p>
      Many readers may not have advanced statistical training.
    </p>

    <h2>Start With the Research Question</h2>

    <p>
      Good reporting begins by connecting results to the original question.
    </p>

    <p>
      Instead of immediately presenting technical statistics, explain:
    </p>

    <div class="example-box">

      <p>
        What question was being investigated?
      </p>
    </div>

    <p>
      This helps readers understand why the analysis matters.
    </p>

    <h2>A Poor Example</h2>

    <div class="example-box">

      <p>
        t = 2.73, df = 118, p = 0.007
      </p>
    </div>

    <p>
      While technically correct, this statement alone provides little context.
    </p>

    <h2>A Better Example</h2>

    <div class="example-box">

      <p>
        Participants receiving the new treatment scored higher on average than those receiving the standard treatment, and the difference was statistically significant (t = 2.73, p = 0.007).
      </p>
    </div>

    <p>
      The second statement combines statistical information with practical meaning.
    </p>

    <h2>Use Plain Language When Possible</h2>

    <p>
      Technical terminology is sometimes necessary, but unnecessary jargon should be avoided.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Technical Phrase</th>
            <th>Clearer Alternative</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Reject H₀</td>
            <td>Evidence suggests a difference exists</td>
          </tr>

          <tr>
            <td>Parameter estimate</td>
            <td>Estimated value</td>
          </tr>

          <tr>
            <td>Sampling variability</td>
            <td>Natural variation from sample to sample</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Report More Than P-Values</h2>

    <p>
      A common mistake is reporting only whether a result was statistically significant.
    </p>

    <p>
      Good reporting typically includes:
    </p>

    <ul class="bullets">

      <li>Effect size</li>

      <li>Confidence interval</li>

      <li>P-value</li>

      <li>Practical interpretation</li>

    </ul>

    <p>
      Together these provide a fuller picture.
    </p>

    <h2>Focus on Magnitude</h2>

    <p>
      Readers often care most about:
    </p>

    <div class="example-box">

      <p>
        How large is the effect?
      </p>
    </div>

    <p>
      Reporting magnitude helps connect statistical findings to real-world implications.
    </p>

    <h2>Include Uncertainty</h2>

    <p>
      Statistical estimates are never perfectly precise.
    </p>

    <p>
      Confidence intervals communicate uncertainty and should often accompany point estimates.
    </p>

    <p>
      For example:
    </p>

    <div class="example-box">

      <p>
        Average improvement = 4.2 points
      </p>

      <p>
        95% CI: (1.3, 7.1)
      </p>

    </div>

    <p>
      This tells readers both the estimate and its plausible range.
    </p>

    <h2>Avoid Overstating Conclusions</h2>

    <p>
      Statistical evidence rarely proves anything with certainty.
    </p>

    <p>
      Avoid language such as:
    </p>

    <div class="example-box">

      <p>
        The treatment definitely works.
      </p>
    </div>

    <p>
      Prefer:
    </p>

    <div class="example-box">

      <p>
        The results provide evidence that the treatment improves outcomes.
      </p>
    </div>

    <h2>Distinguish Evidence From Proof</h2>

    <p>
      Statistical inference evaluates evidence.
    </p>

    <p>
      It does not provide mathematical proof in the same sense as geometry or logic.
    </p>

    <div class="concept-box">

      <strong>Important principle:</strong>

      <p>
        Statistical conclusions are probabilistic, not absolute.
      </p>

    </div>

    <h2>Be Careful With Causal Language</h2>

    <p>
      Not all studies support causal conclusions.
    </p>

    <p>
      Observational studies often identify associations rather than causes.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Potentially Misleading</th>
            <th>Safer Alternative</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>X causes Y</td>
            <td>X is associated with Y</td>
          </tr>

          <tr>
            <td>X leads to Y</td>
            <td>X is linked to Y</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Communicate Practical Importance</h2>

    <p>
      Readers should understand whether observed effects matter.
    </p>

    <p>
      Instead of reporting only:
    </p>

    <div class="example-box">

      <p>
        p &lt; 0.05
      </p>
    </div>

    <p>
      explain:
    </p>

    <div class="example-box">

      <p>
        The treatment reduced average recovery time by approximately five days.
      </p>
    </div>

    <p>
      This is much more informative.
    </p>

    <h2>Consider the Audience</h2>

    <p>
      Different audiences require different levels of detail.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Audience</th>
            <th>Typical Style</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Researchers</td>
            <td>Technical and detailed</td>
          </tr>

          <tr>
            <td>Managers</td>
            <td>Decision-focused</td>
          </tr>

          <tr>
            <td>General Public</td>
            <td>Plain language</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Use Numbers Thoughtfully</h2>

    <p>
      Excessive numerical precision can distract readers.
    </p>

    <p>
      Compare:
    </p>

    <div class="example-box">

      <p>
        Mean = 42.387164
      </p>
    </div>

    <p>
      with:
    </p>

    <div class="example-box">

      <p>
        Mean ≈ 42.4
      </p>
    </div>

    <p>
      The second version is often easier to interpret.
    </p>

    <h2>Provide Context</h2>

    <p>
      Statistical results become more meaningful when placed in context.
    </p>

    <p>
      Readers benefit from understanding:
    </p>

    <ul class="bullets">

      <li>How large the effect is</li>

      <li>How precise the estimate is</li>

      <li>Why the effect matters</li>

      <li>What limitations exist</li>

    </ul>

    <h2>Report Limitations Honestly</h2>

    <p>
      Every study has limitations.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Small sample sizes</li>

      <li>Measurement error</li>

      <li>Missing data</li>

      <li>Limited generalizability</li>

    </ul>

    <p>
      Transparent reporting strengthens credibility.
    </p>

    <h2>Common Reporting Mistakes</h2>

    <div class="concept-box">

      <strong>Avoid these pitfalls:</strong>

      <ul class="bullets">

        <li>Reporting only p-values</li>

        <li>Overstating certainty</li>

        <li>Ignoring uncertainty</li>

        <li>Using unnecessary jargon</li>

        <li>Making unsupported causal claims</li>

      </ul>

    </div>

    <h2>A Reporting Template</h2>

    <p>
      A useful reporting structure is:
    </p>

    <ol>

      <li>State the research question</li>

      <li>Summarize the main finding</li>

      <li>Report effect size</li>

      <li>Report uncertainty (CI)</li>

      <li>Report statistical evidence</li>

      <li>Discuss practical implications</li>

      <li>Mention limitations</li>

    </ol>

    <p>
      This framework helps readers understand both the results and their significance.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Statistical analysis is not complete when calculations end.
    </p>

    <p>
      Results must be communicated accurately and clearly to support understanding and decision-making.
    </p>

    <p>
      Effective reporting combines statistical rigor with accessible language.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Good statistical reporting explains what was studied, what was found, how certain the findings are, and why they matter. Clear communication is an essential part of responsible statistical practice.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Written explanations are only one component of effective communication.
    </p>

    <p>
      Tables, figures, and visualizations can often communicate patterns and results more effectively than text alone.
    </p>

    <p>
      The next lesson explores how to use tables and graphics to present statistical findings clearly and responsibly.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Statistical results should be communicated clearly and accurately</li>

        <li>Good reporting connects findings to the original research question</li>

        <li>Effect sizes and confidence intervals should accompany p-values</li>

        <li>Practical importance should be discussed explicitly</li>

        <li>Uncertainty should be communicated honestly</li>

        <li>Causal language should be used carefully</li>

        <li>Reporting should be tailored to the intended audience</li>

        <li>Clear communication is a fundamental part of statistical practice</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/interpretation-reporting/multiple-testing-and-false-positives/">
         ← Previous: Multiple Testing and False Positives
      </a>

      <a class="btn"
         href="/inference/interpretation-reporting/tables-figures-and-visual-communication/">
         Next: Tables, Figures, and Visual Communication →
      </a>

    </div>

  </div>

</section>