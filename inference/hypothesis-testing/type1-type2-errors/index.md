---
layout: default
title: Type I and Type II Errors
description: Learn the two fundamental mistakes possible in hypothesis testing and how they shape statistical decision-making.
permalink: /inference/hypothesis-testing/type1-type2-errors/
sidebar: false
math: true
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_hypothesis_testing_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/hypothesis-testing/type1-type2-errors/",
    label: "Type I and Type II Errors",
    ts: Date.now()
  }));
  } catch (_) {
    // Lesson remains usable if persistent storage is denied.
  }

})();
</script>

<!-- Scope mobile table containment to this lesson's pre-existing and new tables. -->
<style>
@media (max-width:760px) {
  #main-content .content-narrow {
    display:block;
    width:100%;
    max-width:100%;
    min-width:0;
    /* Clip accidental page-level overflow; tables and formula have their own keyboard-accessible scrollers. */
    overflow-x:clip;
  }
  #main-content .content-narrow .table-wrap {
    display:block;
    width:100%;
    max-width:100%;
    min-width:0;
    overflow-x:auto;
    overscroll-behavior-x:contain;
  }
  #main-content .content-narrow .table-wrap table {
    display:table;
    width:max-content;
    min-width:640px;
    max-width:none;
    overflow:visible;
    white-space:normal;
  }
}
</style>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 3</span>
      <span class="badge">Hypothesis Testing</span>
      <span class="badge">Decision Errors</span>
    </div>

    <h1>Type I and Type II Errors</h1>

    <p class="lead">
      Hypothesis testing provides a structured decision process, but no statistical decision rule is perfect.
    </p>

    <p class="lead">
      Because decisions are based on samples rather than entire populations, mistakes can occur. Understanding these mistakes is central to statistical inference.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/hypothesis-testing/significance-level-alpha/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/power-and-effect-size/">
         Next: Power and Effect Size →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Errors Are Unavoidable</h2>

    <p>
      Hypothesis tests make decisions using incomplete information.
    </p>

    <p>
      We observe a sample, not an entire population.
    </p>

    <p>
      Because samples vary randomly,
      a statistical decision can occasionally be wrong.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Even a perfectly designed hypothesis test can make mistakes because random sampling variability is unavoidable.
      </p>

    </div>

    <h2>The Two Possible Realities</h2>

    <p>
      In truth, only one of two situations can exist:
    </p>

    <ul class="bullets">

      <li>The null hypothesis is true.</li>

      <li>The null hypothesis is false.</li>

    </ul>

    <p>
      However, we do not know which situation is correct.
    </p>

    <h2>The Two Possible Decisions</h2>

    <p>
      A hypothesis test can produce one of two decisions:
    </p>

    <ul class="bullets">

      <li>Reject H₀</li>

      <li>Fail to reject H₀</li>

    </ul>

    <p>
      Combining realities and decisions creates four possible outcomes.
    </p>

    <h2>The Decision Table</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Reality</th>
            <th>Reject H₀</th>
            <th>Fail to Reject H₀</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>H₀ True</td>
            <td>Type I Error</td>
            <td>Correct Decision</td>
          </tr>

          <tr>
            <td>H₀ False</td>
            <td>Correct Decision</td>
            <td>Type II Error</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Two outcomes are correct decisions.
    </p>

    <p>
      Two outcomes are errors.
    </p>

    <h2>Type I Error</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A Type I error occurs when a true null hypothesis is rejected.
      </p>

    </div>

    <p>
      In simple language:
    </p>

    <div class="example-box">

      <p>
        Detecting an effect that does not actually exist.
      </p>

    </div>

    <h2>Examples of Type I Errors</h2>

    <div class="example-box">

      <p>
        Concluding a drug works when it actually does not.
      </p>

      <p>
        Concluding a manufacturing process changed when it actually did not.
      </p>

      <p>
        Concluding a website redesign improved conversions when it actually had no effect.
      </p>

    </div>

    <h2>The Probability of a Type I Error</h2>

    <p>
      For a test calibrated to significance level α, the Type I error
      probability is at most α for every parameter value θ allowed under
      the null hypothesis (the set Θ₀):
    </p>

    \[
\sup_{\theta\in\Theta_0}P_{\theta}(\text{reject }H_0)\le\alpha
\]

    <p>
      For example:
    </p>

    <div class="example-box">

      <p>
        α = 0.05
      </p>
    </div>

    <p>
      means a Type I error rate of at most 5% under the null model,
      provided the test is correctly calibrated. Equality holds for
      a test with exact size 0.05, but discrete or conservative tests
      can have a smaller Type I error probability.
    </p>

    <h2>Type II Error</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A Type II error occurs when a false null hypothesis is not rejected.
      </p>

    </div>

    <p>
      In simple language:
    </p>

    <div class="example-box">

      <p>
        Missing a real effect that actually exists.
      </p>

    </div>

    <h2>Examples of Type II Errors</h2>

    <div class="example-box">

      <p>
        Failing to detect a genuine drug effect when the null hypothesis is false.
      </p>

      <p>
        Missing a real safety problem in a manufacturing process.
      </p>

      <p>
        Failing to detect a genuine difference between two teaching methods.
      </p>

    </div>

    <h2>The Probability of a Type II Error</h2>

    <p>
      The probability of a Type II error is denoted by:
    </p>

    \[
\beta(\theta)=P_{\theta}(\text{fail to reject }H_0),
\qquad\theta\in\Theta_1
\]

    <p>
      Here θ lies in the alternative-hypothesis set Θ₁. The Type II
      error probability β(θ) is defined at a particular alternative
      and depends on several factors:
    </p>

    <ul class="bullets">

      <li>Sample size</li>

      <li>Variability</li>

      <li>Effect size</li>

      <li>Significance level</li>

    </ul>

    <h2>Why Type II Errors Are Harder</h2>

    <p>
      Type I errors are easy to define because they assume the null hypothesis is true.
    </p>

    <p>
      Type II errors depend on how false the null hypothesis is.
    </p>

    <p>
      Therefore their probability varies across situations.
    </p>

    <h2>A Medical Testing Example</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Statistical Decision</th>
            <th>Medical Analogy</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Type I Error</td>
            <td>Healthy patient diagnosed as sick</td>
          </tr>

          <tr>
            <td>Type II Error</td>
            <td>Sick patient diagnosed as healthy</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Both mistakes can be costly,
      but the consequences differ.
    </p>

    <h2>The Tradeoff Between Errors</h2>

    <p>
      Reducing one type of error often increases the other.
    </p>

    <p>
      For example,
      lowering:
    </p>

    \[
\alpha:\ 0.05\longrightarrow0.01
\]

    <p>
      makes rejection more difficult.
    </p>

    <p>
      For a fixed sample size and a family of tests whose rejection regions
      are nested, this cannot increase Type I error and can increase Type II
      error for a given alternative. It is not an unavoidable tradeoff
      if the study design or sample size can also change.
    </p>

    <div class="concept-box">

      <strong>Tradeoff:</strong>

      <p>
        Making false alarms less likely often makes missed detections more likely.
      </p>

    </div>

    <section class="concept-box" id="esa-errors-lab" aria-labelledby="esa-errors-title" style="min-width:0;max-width:100%;overflow-x:hidden;overflow-wrap:anywhere">
  <h2 id="esa-errors-title">Interactive Type I / Type II Decision Experiment</h2>
  <p>Compare 1,000 independent simulated experiments when H₀ is true with 1,000 independent experiments when a <strong>specified positive alternative</strong> is true. The model assumes independently sampled <strong>N(μ,1)</strong> observations and a two-sided z-test of <strong>H₀: μ = 0</strong> at a known population standard deviation of 1. Under the alternative, μ = Δ &gt; 0.</p>
  <p>The simulator draws the standardized sample mean directly from its <strong>exact normal sampling distribution</strong> (equivalent to drawing n independent normal observations and averaging them). It rejects H₀ when |Z| exceeds the two-sided normal critical value. This is an exact-model example, <strong>not</strong> a universal description of real study errors.</p>
  <div style="display:flex;flex-wrap:wrap;gap:1rem;align-items:end">
    <label for="esa-errors-n">Sample size n
      <select id="esa-errors-n"><option value="10">10</option><option value="30" selected>30</option><option value="100">100</option></select>
    </label>
    <label for="esa-errors-effect">True mean difference Δ (σ = 1)
      <select id="esa-errors-effect"><option value="0.2">0.2</option><option value="0.5" selected>0.5</option><option value="1">1.0</option></select>
    </label>
    <label for="esa-errors-alpha">Two-sided significance level α
      <select id="esa-errors-alpha"><option value="0.01">0.01</option><option value="0.05" selected>0.05</option><option value="0.10">0.10</option></select>
    </label>
    <label for="esa-errors-seed">Reproducible seed
      <input id="esa-errors-seed" type="number" min="1" max="2147483647" step="1" value="2026" inputmode="numeric" style="max-width:11rem">
    </label>
    <button id="esa-errors-run" class="btn" type="button">Run 2,000 tests</button>
    <button id="esa-errors-reset" class="btn btn-outline" type="button">Reset</button>
  </div>
  <p id="esa-errors-status" role="status" aria-live="polite"></p>
  <div class="table-wrap" style="width:100%;max-width:100%;min-width:0;overflow-x:auto"><table>
    <caption>Outcomes for <span id="esa-errors-n-rep">1000</span> tests in each scenario</caption>
    <thead><tr><th>Reality</th><th>Reject H₀</th><th>Fail to reject H₀</th></tr></thead>
    <tbody>
      <tr><th scope="row">H₀ true (μ = 0)</th><td>Type I error: <output id="esa-errors-fp">—</output></td><td>Correct decision: <output id="esa-errors-tn">—</output></td></tr>
      <tr><th scope="row">Alternative true (μ = Δ)</th><td>Correct detection: <output id="esa-errors-tp">—</output></td><td>Type II error: <output id="esa-errors-fn">—</output></td></tr>
    </tbody>
  </table></div>
  <div class="table-wrap" style="width:100%;max-width:100%;min-width:0;overflow-x:auto"><table>
    <caption>Theoretical probabilities versus empirical simulation proportions</caption>
    <thead><tr><th>Probability</th><th>Exact normal-model target</th><th>Simulated rate</th></tr></thead>
    <tbody>
      <tr><td>Type I error under H₀</td><td><output id="esa-errors-alpha-theory">—</output></td><td><output id="esa-errors-alpha-empirical">—</output></td></tr>
      <tr><td>Power under specified H₁</td><td><output id="esa-errors-power-theory">—</output></td><td><output id="esa-errors-power-empirical">—</output></td></tr>
      <tr><td>Type II error under specified H₁</td><td><output id="esa-errors-beta-theory">—</output></td><td><output id="esa-errors-beta-empirical">—</output></td></tr>
    </tbody>
  </table></div>
  <p>Under the specified alternative, the standardized statistic has a shifted normal distribution with mean Δ√n and variance 1. Consequently the theoretical power is:</p>
  <div role="region" aria-label="Theoretical power equation; scroll horizontally on smaller screens" tabindex="0"
       style="display:block;max-width:100%;min-width:0;overflow-x:auto;overscroll-behavior-x:contain">
  \[
    1-\Phi(z_{1-\alpha/2}-\Delta\sqrt{n})+
    \Phi(-z_{1-\alpha/2}-\Delta\sqrt{n}).
  \]
  </div>
  <p>Type II probability is one minus power. At the null, the calibrated two-sided test has exact Type I rate α. Simulated frequencies fluctuate around these targets. Rejecting H₀ does not prove the alternative, and failing to reject does not prove the null. The model does not cover dependence, unknown σ, optional stopping, multiplicity, or model misspecification.</p>
</section>

<h2>Why Sample Size Helps</h2>

    <p>
      Increasing sample size often improves decision quality.
    </p>

    <p>
      Larger samples reduce uncertainty and make real effects easier to detect.
    </p>

    <p>
      As a result:
    </p>

    <ul class="bullets">

      <li>Type II error rates often decrease.</li>

      <li>Statistical power often increases.</li>

    </ul>

    <h2>The Courtroom Analogy Revisited</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Statistics</th>
            <th>Courtroom Analogy</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Type I Error</td>
            <td>Convicting an innocent person</td>
          </tr>

          <tr>
            <td>Type II Error</td>
            <td>Acquitting a guilty person</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Society often designs legal systems to make Type I errors extremely rare,
      even if that increases Type II errors.
    </p>

    <p>
      Different applications may prioritize different error types.
    </p>

    <h2>Which Error Is Worse?</h2>

    <p>
      There is no universal answer.
    </p>

    <p>
      The consequences depend on context.
    </p>

    <div class="example-box">

      <p>
        Drug approval may prioritize minimizing Type I errors.
      </p>

      <p>
        Disease screening may prioritize minimizing Type II errors.
      </p>

      <p>
        Fraud detection systems may balance both.
      </p>

    </div>

    <h2>The Relationship to Statistical Power</h2>

    <p>
      The probability of correctly detecting a false null hypothesis is called power.
    </p>

    <p>
      Power is directly related to Type II error:
    </p>

    \[
\operatorname{Power}(\theta)=P_{\theta}(\text{reject }H_0)
=1-\beta(\theta),\qquad\theta\in\Theta_1
\]

    <p>
      Power and Type II error are evaluated at the same specified alternative θ.
      Failure to reject H₀ does not prove that H₀ is true or that treatments
      are equivalent. Establishing equivalence requires a separate equivalence
      design and a pre-specified equivalence margin.
    </p>

    <p>
      This relationship becomes a major topic in the next lesson.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Hypothesis testing is fundamentally a decision-making process under uncertainty.
    </p>

    <p>
      Type I and Type II errors define the risks associated with those decisions.
    </p>

    <p>
      Understanding these risks helps researchers design studies and interpret results responsibly.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        A Type I error occurs when a true null hypothesis is rejected. A Type II error occurs when a false null hypothesis is not rejected. Statistical inference balances the risks of these two kinds of mistakes.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Type II errors describe missed discoveries.
    </p>

    <p>
      Researchers often want to know how likely a study is to detect a real effect when one exists.
    </p>

    <p>
      That probability is called statistical power.
    </p>

    <p>
      The next lesson introduces power, effect size, and the factors that influence a study's ability to detect meaningful effects.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Hypothesis tests can make two kinds of errors</li>

        <li>A Type I error rejects a true null hypothesis</li>

        <li>A Type II error fails to reject a false null hypothesis</li>

        <li>A calibrated level-α test has Type I error probability at most α; exact-size tests attain equality</li>

        <li>The probability of a Type II error is denoted by β</li>

        <li>Reducing one error type often increases the other</li>

        <li>Sample size can reduce Type II errors</li>

        <li>Statistical power equals 1 − β</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/significance-level-alpha/">
         ← Previous: Significance Level (α)
      </a>

      <a class="btn"
         href="/inference/hypothesis-testing/power-and-effect-size/">
         Next: Power and Effect Size →
      </a>

    </div>

  </div>

</section>
<script src="/js/type1-type2-errors-lab.js" defer></script>
