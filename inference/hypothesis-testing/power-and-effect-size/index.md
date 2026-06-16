---
layout: default
title: Power and Effect Size
description: Learn what statistical power means, how it relates to Type II errors, and why effect size is crucial for detecting meaningful differences.
permalink: /inference/hypothesis-testing/power-and-effect-size/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_hypothesis_testing_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/hypothesis-testing/power-and-effect-size/",
    label: "Power and Effect Size",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 3</span>
      <span class="badge">Hypothesis Testing</span>
      <span class="badge">Study Design</span>
    </div>

    <h1>Power and Effect Size</h1>

    <p class="lead">
      A good hypothesis test should detect real effects when they exist.
    </p>

    <p class="lead">
      Statistical power measures a test's ability to discover genuine effects, while effect size measures the magnitude of those effects.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/hypothesis-testing/type1-type2-errors/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/one-sided-vs-two-sided/">
         Next: One-Sided vs Two-Sided Tests →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Power Matters</h2>

    <p>
      Suppose a new treatment genuinely improves patient outcomes.
    </p>

    <p>
      Ideally,
      a statistical study should detect that improvement.
    </p>

    <p>
      However,
      because of random sampling variability,
      a study can sometimes miss a real effect.
    </p>

    <p>
      Statistical power measures how likely a study is to avoid that mistake.
    </p>

    <h2>The Definition of Power</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Statistical power is the probability that a hypothesis test correctly rejects a false null hypothesis.
      </p>

    </div>

    <p>
      In simple language:
    </p>

    <div class="example-box">

      <p>
        Power measures a study's ability to detect real effects.
      </p>
    </div>

    <h2>The Connection to Type II Errors</h2>

    <p>
      In the previous lesson,
      we learned that:
    </p>

    0

    <p>
      Power is simply the complement:
    </p>

    1

    <p>
      Therefore:
    </p>

    <ul class="bullets">

      <li>High power means few missed effects.</li>

      <li>Low power means many missed effects.</li>

    </ul>

    <h2>The Decision Table Revisited</h2>

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
            <td>Power</td>
            <td>Type II Error</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Power represents the desirable outcome when the null hypothesis is actually false.
    </p>

    <h2>An Example</h2>

    <p>
      Suppose a study has:
    </p>

    2

    <p>
      This means:
    </p>

    <div class="example-box">

      <p>
        If a real effect exists, the study will detect it about 80% of the time.
      </p>
    </div>

    <p>
      The corresponding Type II error probability is:
    </p>

    3

    <h2>What Is Effect Size?</h2>

    <p>
      Detecting an effect depends not only on the quality of the study,
      but also on how large the effect actually is.
    </p>

    <div class="concept-box">

      <strong>Effect Size:</strong>

      <p>
        Effect size measures the magnitude of a difference, relationship, or change.
      </p>

    </div>

    <p>
      It describes practical size rather than statistical evidence.
    </p>

    <h2>Examples of Effect Size</h2>

    <div class="example-box">

      <p>
        Mean difference between treatments
      </p>

      <p>
        Difference in conversion rates
      </p>

      <p>
        Correlation strength
      </p>

      <p>
        Improvement in exam scores
      </p>

    </div>

    <h2>Small vs Large Effects</h2>

    <p>
      Consider two drugs:
    </p>

    <div class="example-box">

      <p>
        Drug A reduces blood pressure by 1 mmHg.
      </p>

      <p>
        Drug B reduces blood pressure by 15 mmHg.
      </p>

    </div>

    <p>
      Drug B has a much larger effect size.
    </p>

    <p>
      Larger effects are generally easier to detect statistically.
    </p>

    <h2>Why Effect Size Affects Power</h2>

    <p>
      When the true effect is large,
      the observed data tend to fall farther from the null hypothesis.
    </p>

    <p>
      Larger departures produce larger test statistics and smaller p-values.
    </p>

    <p>
      As a result,
      power increases.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Large effects are easier to detect than small effects.
      </p>

    </div>

    <h2>The Four Main Factors Affecting Power</h2>

    <p>
      Statistical power depends primarily on four quantities.
    </p>

    <h3>1. Effect Size</h3>

    <p>
      Larger effects increase power.
    </p>

    <h3>2. Sample Size</h3>

    <p>
      Larger samples reduce uncertainty and increase power.
    </p>

    <h3>3. Variability</h3>

    <p>
      Greater variability makes effects harder to detect and reduces power.
    </p>

    <h3>4. Significance Level</h3>

    <p>
      Larger:
    </p>

    4

    <p>
      makes rejection easier and increases power.
    </p>

    <h2>How Sample Size Influences Power</h2>

    <p>
      Increasing sample size is often the most effective way to improve power.
    </p>

    <p>
      Larger samples:
    </p>

    <ul class="bullets">

      <li>Reduce standard errors</li>

      <li>Increase test statistics</li>

      <li>Improve precision</li>

      <li>Increase power</li>

    </ul>

    <h2>The Power Tradeoff</h2>

    <p>
      Reducing Type I errors often increases Type II errors.
    </p>

    <p>
      Therefore:
    </p>

    <ul class="bullets">

      <li>Smaller α → lower power</li>

      <li>Larger α → higher power</li>

    </ul>

    <p>
      Statistical design often involves balancing these competing goals.
    </p>

    <h2>The Common 80% Rule</h2>

    <p>
      Many scientific studies aim for:
    </p>

    5

    <p>
      or:
    </p>

    <div class="example-box">

      <p>
        80% power
      </p>
    </div>

    <p>
      This means researchers accept approximately a 20% chance of missing a real effect of a specified size.
    </p>

    <h2>Power Analysis</h2>

    <p>
      Before collecting data,
      researchers often perform a power analysis.
    </p>

    <p>
      A power analysis estimates the sample size needed to achieve a desired power level.
    </p>

    <div class="example-box">

      <p>
        Desired power = 80%
      </p>

      <p>
        Desired α = 0.05
      </p>

      <p>
        Expected effect size = specified in advance
      </p>

    </div>

    <p>
      These inputs determine the required sample size.
    </p>

    <h2>Statistical Significance vs Effect Size</h2>

    <p>
      Statistical significance and effect size are not the same thing.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Concept</th>
            <th>Measures</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>p-value</td>
            <td>Evidence against H₀</td>
          </tr>

          <tr>
            <td>Effect size</td>
            <td>Magnitude of the effect</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      A tiny effect can become statistically significant if the sample size is extremely large.
    </p>

    <h2>Practical Importance</h2>

    <p>
      Researchers should ask:
    </p>

    <div class="example-box">

      <p>
        Is the detected effect large enough to matter in practice?
      </p>
    </div>

    <p>
      Power helps detect effects.
    </p>

    <p>
      Effect size helps judge whether those effects are meaningful.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Hypothesis testing is not merely about obtaining significant p-values.
    </p>

    <p>
      A useful study should have enough power to detect meaningful effects while controlling error rates.
    </p>

    <p>
      Effect size and power therefore play central roles in study design.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Statistical power is the probability of detecting a real effect when one exists. Power increases with larger effect sizes, larger samples, lower variability, and less stringent significance thresholds.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Not all hypothesis tests ask the same question.
    </p>

    <p>
      Some tests look for effects in either direction,
      while others focus on a specific direction.
    </p>

    <p>
      The next lesson explores one-sided and two-sided tests and how the choice affects statistical inference.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Power is the probability of correctly rejecting a false null hypothesis</li>

        <li>Power equals 1 − β</li>

        <li>Effect size measures the magnitude of an effect</li>

        <li>Larger effects are easier to detect</li>

        <li>Larger samples generally increase power</li>

        <li>Greater variability decreases power</li>

        <li>Power analysis helps determine required sample sizes</li>

        <li>Statistical significance and practical importance are distinct concepts</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/type1-type2-errors/">
         ← Previous: Type I and Type II Errors
      </a>

      <a class="btn"
         href="/inference/hypothesis-testing/one-sided-vs-two-sided/">
         Next: One-Sided vs Two-Sided Tests →
      </a>

    </div>

  </div>

</section>