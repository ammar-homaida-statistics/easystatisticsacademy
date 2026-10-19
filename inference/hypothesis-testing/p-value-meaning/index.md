---
layout: default
title: p-Value Meaning
description: Learn what a p-value measures, how it is computed conceptually, and how to interpret it correctly in hypothesis testing.
permalink: /inference/hypothesis-testing/p-value-meaning/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_hypothesis_testing_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/hypothesis-testing/p-value-meaning/",
    label: "p-Value Meaning",
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
      <span class="badge">Core Concept</span>
    </div>

    <h1>p-Value Meaning</h1>

    <p class="lead">
      A p-value summarizes how unusual a specified test result would be under the null model; interpretation requires the test direction and its assumptions.
    </p>

    <p class="lead">
      It connects the observed data to the null hypothesis by quantifying how unusual the observed result would be if the null hypothesis were true.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/hypothesis-testing/test-statistic-standardization/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/significance-level-alpha/">
         Next: Significance Level (α) →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why We Need the p-Value</h2>

    <p>
      In the previous lesson,
      we learned how to compute a test statistic.
    </p>

    <p>
      Suppose a test produces:
    </p>

    
    \[
    z_{\mathrm{obs}}\ \text{(the observed standardized statistic)}
    \]


    <p>
      Is that unusual?
    </p>

    <p>
      A test statistic alone does not answer the question.
    </p>

    <p>
      We need a probability that tells us how surprising such a result would be under the null hypothesis.
    </p>

    <h2>The Formal Definition</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Given a prespecified test statistic, null model, and alternative direction, the p-value is the probability—calculated under that null model—of a test statistic at least as extreme as the one observed.
      </p>

    </div>

    <p>
      This definition is the foundation of classical hypothesis testing.
    </p>

    <h2>The Assumption Behind Every p-Value</h2>

    <p>
      Every p-value calculation begins by assuming:
    </p>

    
    \[
    H_0\ \text{(null hypothesis)}
    \]


    <p>
      is true.
    </p>

    <p>
      The p-value asks:
    </p>

    <div class="example-box">

      <p>
        If the null hypothesis were actually true, how surprising would the observed data be?
      </p>

    </div>

    <h2>Understanding "At Least as Extreme"</h2>

    <p>
      Hypothesis testing does not consider only the observed result.
    </p>

    <p>
      It also considers outcomes even more inconsistent with the null hypothesis.
    </p>

    <div class="concept-box">

      <strong>Important idea:</strong>

      <p>
        The relevant tail or tails depend on the test statistic and the preselected alternative. For a discrete statistic, include the observed value and outcomes at least as extreme as it under that test's ordering.
      </p>

    </div>

    <h2>A Coin-Flipping Example</h2>

    <p>
      Suppose the null hypothesis is a fair coin and the <strong>two-sided</strong>
      alternative is that the probability of heads differs from 0.5. In 100
      independent flips, we observe <strong>90 heads</strong>. Under the null,
      the head count has the exact binomial distribution:
    </p>

    \[
    H_0:p=0.5,\qquad H_1:p\ne0.5,\qquad X\sim\operatorname{Binomial}(100,0.5)\text{ under }H_0.
    \]

    <p>
      For this symmetric binomial null, counting outcomes at least as far from
      the expected 50 heads as the observed 90 means <strong>10 or fewer heads,
      or 90 or more heads</strong>. The exact two-sided p-value is:
    </p>

    \[
    \begin{aligned}
    p_{\text{two-sided}}
    &=P_{H_0}(X\le10)+P_{H_0}(X\ge90)\\
    &=2\sum_{k=90}^{100}\binom{100}{k}(0.5)^{100}\\
    &\approx 3.0632901754\times10^{-17}.
    \end{aligned}
    \]

    <p>
      If the alternative had instead been chosen <strong>before observing
      the flips</strong> as H₁: p &gt; 0.5, only the upper tail would count:
    </p>

    \[
    p_{\text{right-tailed}}=P_{H_0}(X\ge90)
    =\sum_{k=90}^{100}\binom{100}{k}(0.5)^{100}
    \approx 1.5316450877\times10^{-17}.
    \]

    <p>
      These are probabilities of tail outcomes <em>assuming the coin is fair</em>,
      not probabilities that the fair-coin hypothesis is true. The exact
      equality between the two-sided p-value and twice the upper-tail p-value
      uses this symmetric binomial null and this particular extremeness ordering;
      it is not a universal rule for all discrete tests.
    </p>

    <h2>Large p-Values</h2>

    <p>
      A large p-value means the prespecified statistic is not especially unusual under the null model. It does <strong>not</strong> demonstrate that the null is true, nor that the data favor it over an alternative.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>p-Value</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Large</td>
            <td>Data are not unusual under H₀</td>
          </tr>

          <tr>
            <td>Near 1</td>
            <td>Little discrepancy for this statistic; not evidence that H₀ is true</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Small p-Values</h2>

    <p>
      Small p-values indicate that the observed statistic would be unusual under the null model; they do not quantify the effect size, the practical importance, or the probability that H₀ is false.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>p-Value</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Small</td>
            <td>Data are unusual under H₀</td>
          </tr>

          <tr>
            <td>Very small</td>
            <td>Strong evidence against H₀</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Evidence Scale</h2>

    <p>
      The p-value can help assess compatibility with the null, but numerical cutoffs are <strong>decision conventions, not universal grades of evidence</strong>. The test design, assumptions, sample size, and any multiplicity or data-dependent selection matter.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>p-Value</th>
            <th>Illustrative interpretation (if the test is valid)</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>0.20</td>
            <td>Not unusual enough for a 0.05 decision threshold; does not establish H₀</td>
          </tr>

          <tr>
            <td>0.05</td>
            <td>At the conventional 0.05 boundary; not a universal evidence label</td>
          </tr>

          <tr>
            <td>0.01</td>
            <td>Less compatible with this null model than a larger p-value would be, for the same prespecified test</td>
          </tr>

          <tr>
            <td>0.001</td>
            <td>More unusual under this null model; still does not directly measure an effect or posterior probability</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      For the same valid, prespecified test, smaller p-values indicate stronger disagreement between the observed statistic and its null distribution. Comparing numbers across different tests or samples does not automatically compare scientific importance or evidential strength.
    </p>

    <h2>How Test Statistics and p-Values Connect</h2>

    <p>
      For a standard normal <strong>two-sided z-test</strong>, larger absolute z-values give smaller p-values. For a one-sided test, the direction also matters; a large z in the wrong direction produces a large p-value.
    </p>

    <div class="example-box">

      <p>
        z = 0.3 → large p-value
      </p>

      <p>
        z = 1.2 → moderate p-value
      </p>

      <p>
        z = 3.5 → very small p-value
      </p>

    </div>

    <p>
      The farther the statistic lies from the null expectation,
      the more unusual it becomes.
    </p>

    <h2>What the p-Value Is NOT</h2>

    <p>
      Many incorrect interpretations appear in practice.
    </p>

    <h3>Incorrect Interpretation #1</h3>

    <div class="example-box">

      <p>
        “The p-value is the probability that the null hypothesis is true.”
      </p>

    </div>

    <p>
      This is false.
    </p>

    <p>
      Classical hypothesis testing does not assign probabilities to hypotheses.
    </p>

    <h2>Incorrect Interpretation #2</h2>

    <div class="example-box">

      <p>
        “The p-value is the probability that the observed result occurred by chance.”
      </p>

    </div>

    <p>
      This statement is also inaccurate.
    </p>

    <p>
      The p-value assumes the null hypothesis is true and measures how surprising the data would be under that assumption.
    </p>

    <h2>Incorrect Interpretation #3</h2>

    <div class="example-box">

      <p>
        “A large p-value proves the null hypothesis.”
      </p>

    </div>

    <p>
      This is false as well.
    </p>

    <p>
      A large p-value simply means the data do not provide strong evidence against the null hypothesis.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Lack of evidence against H₀ is not proof that H₀ is correct.
      </p>

    </div>

    <h2>A Courtroom Analogy</h2>

    <p>
      Consider a criminal trial.
    </p>

    <ul class="bullets">

      <li>Null hypothesis = innocence</li>

      <li>Alternative hypothesis = guilt</li>

      <li>Data = evidence</li>

    </ul>

    <p>
      A small p-value corresponds to evidence that would be very surprising if innocence were true.
    </p>

    <p>
      Therefore innocence becomes harder to maintain.
    </p>

    <h2>The Role of Sampling Variability</h2>

    <p>
      Even when the null hypothesis is true,
      unusual samples occasionally occur.
    </p>

    <p>
      The p-value quantifies how rare those samples would be.
    </p>

    <p>
      This is why probability plays a central role in hypothesis testing.
    </p>

    <h2>Evidence Versus Importance</h2>

    <p>
      A small p-value does not automatically imply a large or important effect.
    </p>

    <div class="example-box">

      <p>
        A tiny effect can produce a tiny p-value if the sample size is extremely large.
      </p>
    </div>

    <p>
      Statistical evidence and practical importance are different concepts.
    </p>

    <h2>The Decision Problem</h2>

    <p>
      We now know how to measure evidence against the null hypothesis.
    </p>

    <p>
      But how small must a p-value be before we decide the evidence is strong enough?
    </p>

    <p>
      To answer that question,
      statisticians define a threshold called the significance level.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        A p-value measures how unusual the observed data would be if the null hypothesis were true. Smaller p-values indicate stronger evidence against the null hypothesis.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      The p-value measures evidence,
      but a formal decision rule still requires a cutoff.
    </p>

    <p>
      The significance level provides that cutoff and determines when evidence is considered strong enough to reject the null hypothesis.
    </p>

    <p>
      The next lesson introduces significance levels, alpha, and statistical decision rules.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The p-value assumes the null hypothesis is true</li>

        <li>It measures the probability of results at least as extreme as the observed result</li>

        <li>Small p-values indicate stronger evidence against H₀</li>

        <li>Large p-values indicate limited evidence against H₀, not positive proof that H₀ is true</li>

        <li>The p-value is not the probability that H₀ is true</li>

        <li>A large p-value does not prove H₀</li>

        <li>Statistical evidence and practical importance are different ideas</li>

        <li>p-values provide evidence, while significance levels provide decision rules</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/test-statistic-standardization/">
         ← Previous: Test Statistic and Standardization
      </a>

      <a class="btn"
         href="/inference/hypothesis-testing/significance-level-alpha/">
         Next: Significance Level (α) →
      </a>

    </div>

  </div>

</section>