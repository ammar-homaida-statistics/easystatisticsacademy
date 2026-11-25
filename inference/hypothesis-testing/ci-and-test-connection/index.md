---
layout: default
title: Confidence Intervals and Tests
description: Learn the deep connection between confidence intervals and hypothesis tests and how they often lead to the same statistical conclusions.
permalink: /inference/hypothesis-testing/ci-and-test-connection/
sidebar: false
learning_resource: true
translation_pair: ci-and-test-connection
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_hypothesis_testing_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/hypothesis-testing/ci-and-test-connection/",
    label: "Connection Between CIs and Tests",
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
      <span class="badge">Big Picture</span>
    </div>

    <h1>Confidence Intervals and Tests</h1>

    <p><a href="/ar/inference/hypothesis-testing/ci-and-test-connection/" lang="ar" dir="rtl" hreflang="ar">النسخة العربية: فترات الثقة واختبارات الفرضيات</a></p>
    {% include lab-noscript.html %}

    <p class="lead">
      Confidence intervals and hypothesis tests are often taught as separate statistical tools.
    </p>

    <p class="lead">
      In reality, they are closely connected and frequently provide the same inferential conclusion from different perspectives.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/hypothesis-testing/one-sided-vs-two-sided/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/practical-significance/">
         Next: Practical Significance →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Two Tools, One Goal</h2>

    <p>
      Both confidence intervals and hypothesis tests use sample data to make statements about population parameters.
    </p>

    <p>
      Both rely on:
    </p>

    <ul class="bullets">

      <li>Sampling distributions</li>

      <li>Standard errors</li>

      <li>Probability models</li>

      <li>Random sampling assumptions</li>

    </ul>

    <p>
      Their goals are slightly different:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Method</th>
            <th>Main Question</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Confidence Interval</td>
            <td>What parameter values are plausible?</td>
          </tr>

          <tr>
            <td>Hypothesis Test</td>
            <td>Is a specific claim plausible?</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Key Insight</h2>

    <div class="concept-box">

      <strong>Fundamental relationship:</strong>

      <p>
        A confidence interval contains all parameter values that would not be rejected by the corresponding hypothesis test.
      </p>

    </div>

    <p>
      This is one of the most important connections in statistical inference.
    </p>

    <h2>The Null Value Idea</h2>

    <p>
      Suppose we are testing:
    </p>

    
    \[
    H_0:\theta=\theta_0
    \]


    <br><br>

    
    \[
    H_a:\theta\ne\theta_0
    \]


    <p>
      The value:
    </p>

    
    \[
    \theta_0
    \]


    <p>
      is called the null value.
    </p>

    <p>
      The confidence interval helps determine whether that value remains plausible.
    </p>

    <h2>The Decision Rule</h2>

    <div class="concept-box">

      <strong>Equivalent rule:</strong>

      <p>
        If the null value lies outside the confidence interval, reject H₀.
      </p>

      <p>
        If the null value lies inside the confidence interval, fail to reject H₀.
      </p>

    </div>

    <p>
      This rule works for many common inferential procedures.
    </p>

    <h2>Example 1: Rejecting the Null</h2>

    <p>
      Suppose a 95% confidence interval for a population mean is:
    </p>

    <div class="example-box">

      <p>
        (102, 108)
      </p>
    </div>

    <p>
      and we test:
    </p>

    
    \[
    H_0:\mu=100
    \]


    <p>
      Because:
    </p>

    <div class="example-box">

      <p>
        100 is outside the interval.
      </p>
    </div>

    <p>
      We reject the null hypothesis at:
    </p>

    
    \[
    \alpha=0.05
    \]


    <h2>Example 2: Failing to Reject</h2>

    <p>
      Suppose the confidence interval is:
    </p>

    <div class="example-box">

      <p>
        (96, 108)
      </p>
    </div>

    <p>
      Since:
    </p>

    <div class="example-box">

      <p>
        100 lies inside the interval.
      </p>
    </div>

    <p>
      We fail to reject:
    </p>

    
    \[
    H_0:\mu=100
    \]


    <h2>Why This Happens</h2>

    <p>
      Confidence intervals are constructed using the same ingredients as hypothesis tests.
    </p>

    <ul class="bullets">

      <li>Estimate</li>

      <li>Standard error</li>

      <li>Critical values</li>

      <li>Sampling distributions</li>

    </ul>

    <p>
      The mathematics underlying both procedures is nearly identical.
    </p>

    <h2>The Confidence-Level Connection</h2>

    <p>
      The correspondence depends on matching confidence levels and significance levels.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Confidence Interval</th>
            <th>Equivalent Test Level</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>90% CI</td>
            <td>α = 0.10</td>
          </tr>

          <tr>
            <td>95% CI</td>
            <td>α = 0.05</td>
          </tr>

          <tr>
            <td>99% CI</td>
            <td>α = 0.01</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Visual Interpretation</h2>

    <p>
      A confidence interval provides a range of parameter values consistent with the observed data.
    </p>

    <p>
      A hypothesis test evaluates one specific parameter value.
    </p>

    <p>
      If the tested value falls outside the plausible range,
      it is rejected.
    </p>

    <h2>Confidence Intervals Provide More Information</h2>

    <p>
      A hypothesis test typically produces:
    </p>

    <ul class="bullets">

      <li>Reject H₀</li>

      <li>Fail to reject H₀</li>

    </ul>

    <p>
      A confidence interval provides:
    </p>

    <ul class="bullets">

      <li>Estimated effect size</li>

      <li>Precision</li>

      <li>Uncertainty</li>

      <li>Plausible parameter values</li>

    </ul>

    <p>
      This is one reason many researchers prefer reporting confidence intervals alongside hypothesis tests.
    </p>

    <h2>Difference Parameters and Zero</h2>

    <p>
      For many applications,
      the null hypothesis corresponds to:
    </p>

    
    \[
    H_0:\Delta=0
    \]


    <p>
      because zero represents:
    </p>

    <ul class="bullets">

      <li>No treatment effect</li>

      <li>No mean difference</li>

      <li>No change</li>

      <li>No association</li>

    </ul>

    <h2>Example: Mean Difference</h2>

    <p>
      Suppose a confidence interval for a treatment effect is:
    </p>

    <div class="example-box">

      <p>
        (2.1, 7.5)
      </p>
    </div>

    <p>
      Since:
    </p>

    
    \[
    0
    \]


    <p>
      is not contained in the interval,
      the corresponding hypothesis test rejects:
    </p>

    
    \[
    H_0:\Delta=0
    \]


    <h2>Example: No Significant Difference</h2>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        (-1.2, 5.4)
      </p>
    </div>

    <p>
      Since zero is included,
      the corresponding test fails to reject the null hypothesis.
    </p>

    <!-- Batch #101: confidence interval and test duality laboratory -->
    <section class="concept-box" id="esa-cid-lab" aria-labelledby="esa-cid-heading">
      <h3 id="esa-cid-heading">Interactive lab: the interval and the test give the same answer</h3>
      <p>For one mean with standard error \(\mathrm{SE}=s/\sqrt n\) (or \(\sigma/\sqrt n\) for the z version), the test of \(H_0:\mu=\mu_0\) rejects exactly when \(\mu_0\) falls outside the matching interval:</p>
      <div class="esa-cid-math" dir="ltr" tabindex="0" role="region" aria-label="Duality between the two-sided interval and the two-sided test">
      \[
      \left|\frac{\bar x-\mu_0}{\mathrm{SE}}\right|>c_{1-\alpha/2}
      \iff
      \mu_0\notin\left[\bar x-c_{1-\alpha/2}\,\mathrm{SE},\ \bar x+c_{1-\alpha/2}\,\mathrm{SE}\right].
      \]
      </div>
      <p>A one-sided test matches a one-sided bound: the right-tailed test (\(H_a:\mu&gt;\mu_0\)) pairs with the lower bound \(\bar x-c_{1-\alpha}\,\mathrm{SE}\), and the left-tailed test with the upper bound \(\bar x+c_{1-\alpha}\,\mathrm{SE}\).</p>
      <div class="esa-cid-grid">
        <label for="esa-cid-method">Reference distribution<select id="esa-cid-method"><option value="t" selected>t (σ unknown, uses s)</option><option value="z">z (σ known)</option></select></label>
        <label for="esa-cid-side">Alternative<select id="esa-cid-side"><option value="two-sided" selected>Two-sided (μ ≠ μ₀) ↔ two-sided interval</option><option value="greater">Right-tailed (μ &gt; μ₀) ↔ lower bound</option><option value="less">Left-tailed (μ &lt; μ₀) ↔ upper bound</option></select></label>
        <label for="esa-cid-mean">Sample mean x̄<input id="esa-cid-mean" type="number" step="any" inputmode="decimal" value="104.2" aria-describedby="esa-cid-error"></label>
        <label for="esa-cid-sd">SD (s, or σ for z)<input id="esa-cid-sd" type="number" step="any" min="0" inputmode="decimal" value="8.5" aria-describedby="esa-cid-error"></label>
        <label for="esa-cid-n">Sample size n<input id="esa-cid-n" type="number" step="1" min="2" inputmode="numeric" value="25" aria-describedby="esa-cid-error"></label>
        <label for="esa-cid-mu0">Null value μ₀<input id="esa-cid-mu0" type="number" step="any" inputmode="decimal" value="100" aria-describedby="esa-cid-error"></label>
        <label for="esa-cid-alpha">Significance level α<input id="esa-cid-alpha" type="number" step="any" min="0.001" max="0.5" inputmode="decimal" value="0.05" aria-describedby="esa-cid-error"></label>
      </div>
      <div class="esa-cid-controls"><button class="btn btn-outline" type="button" id="esa-cid-example">μ₀ outside</button><button class="btn btn-outline" type="button" id="esa-cid-inside-ex">μ₀ inside</button><button class="btn btn-outline" type="button" id="esa-cid-boundary">Put μ₀ on the boundary</button></div>
      <p id="esa-cid-error" role="alert" hidden></p>
      <section id="esa-cid-results" aria-label="Interval and test results" role="status" aria-live="polite" aria-atomic="true">
        <div class="table-wrap"><table><caption>Interval and test for the same data</caption><tbody>
          <tr><th scope="row">Critical value</th><td><output id="esa-cid-crit" dir="ltr">t(24) = 2.0639</output></td></tr>
          <tr><th scope="row">Confidence interval or bound</th><td><output id="esa-cid-ci" dir="ltr">95%: [100.6914, 107.7086]</output></td></tr>
          <tr><th scope="row">Is μ₀ inside?</th><td><output id="esa-cid-inside">No — μ₀ is outside the interval</output></td></tr>
          <tr><th scope="row">Test statistic</th><td><output id="esa-cid-stat" dir="ltr">t = 2.4706</output></td></tr>
          <tr><th scope="row">p-value</th><td><output id="esa-cid-p" dir="ltr">0.020981</output></td></tr>
          <tr><th scope="row">Decision</th><td><output id="esa-cid-decision">Reject H₀ at α = 0.05 (p &lt; α)</output></td></tr>
        </tbody></table></div>
        <p id="esa-cid-agree">Interval and test agree.</p>
      </section>
      <p class="muted-mini">With the boundary button, μ₀ sits exactly on an endpoint, so the test statistic equals the critical value and p = α. This lab treats the interval as closed and rejects only when p &lt; α, matching the table below; some texts use p ≤ α with an open interval. The two conventions differ only on this boundary, which has probability zero for continuous data. The z version assumes σ is known; the t version assumes approximately normal data or a large enough n.</p>
    </section>
    <style>
    #esa-cid-lab,#esa-cid-lab *{box-sizing:border-box}
    #esa-cid-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
    #esa-cid-lab label{display:block;font-weight:650;margin:6px 0}
    #esa-cid-lab :is(input,select){display:block;width:100%;min-width:0;font:inherit;padding:8px;margin-top:4px;border:1px solid #777;border-radius:6px}
    #esa-cid-lab .esa-cid-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));gap:4px 10px}
    #esa-cid-lab .esa-cid-controls{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
    #esa-cid-lab .table-wrap,.esa-cid-math{max-width:100%;overflow-x:auto}
    .esa-cid-math{direction:ltr}
    #esa-cid-lab [hidden]{display:none!important}
    #esa-cid-lab :is(input,select,button):focus-visible,.esa-cid-math:focus-visible{outline:2px solid #0f766e;outline-offset:3px}
    </style>
    <script defer src="/js/ci-test-duality-lab.js"></script>

    <h2>The Relationship to p-Values</h2>

    <p>
      Confidence intervals and p-values tell a consistent story.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Confidence Interval Result</th>
            <th>p-Value Result</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Null value outside interval</td>
            <td>p &lt; α</td>
          </tr>

          <tr>
            <td>Null value inside interval</td>
            <td>p ≥ α</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Why Researchers Often Report Both</h2>

    <p>
      Confidence intervals and hypothesis tests complement each other.
    </p>

    <div class="example-box">

      <p>
        Hypothesis test → Is there evidence?
      </p>

      <p>
        Confidence interval → How large is the effect?
      </p>
    </div>

    <p>
      Together they provide a richer understanding of the results.
    </p>

    <h2>Limitations of Focusing Only on Significance</h2>

    <p>
      A statistically significant result may correspond to a very small effect.
    </p>

    <p>
      Confidence intervals help reveal whether an effect is scientifically or practically important.
    </p>

    <p>
      This leads naturally to the idea of practical significance.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Confidence intervals and hypothesis tests are not competing methods.
    </p>

    <p>
      They are two views of the same inferential framework.
    </p>

    <p>
      Understanding their connection helps unify many ideas from statistical inference.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        A confidence interval contains the parameter values that remain plausible given the data. If a null-hypothesis value falls outside the interval, the corresponding hypothesis test rejects that null value at the matching significance level.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Statistical significance tells us whether an effect is detectable.
    </p>

    <p>
      It does not tell us whether the effect is important.
    </p>

    <p>
      The next lesson introduces practical significance and explains why statistically significant results are not always meaningful in real-world applications.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Confidence intervals and hypothesis tests are closely connected</li>

        <li>A confidence interval contains values not rejected by the corresponding test</li>

        <li>Null values outside intervals imply rejection of H₀</li>

        <li>Null values inside intervals imply failure to reject H₀</li>

        <li>95% confidence intervals correspond to α = 0.05 tests</li>

        <li>Confidence intervals provide more information than a simple reject/fail decision</li>

        <li>p-values and confidence intervals generally tell a consistent story</li>

        <li>Confidence intervals help assess both statistical and practical importance</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/one-sided-vs-two-sided/">
         ← Previous: One-Sided vs Two-Sided Tests
      </a>

      <a class="btn"
         href="/inference/hypothesis-testing/practical-significance/">
         Next: Practical Significance →
      </a>

    </div>

  </div>

</section>