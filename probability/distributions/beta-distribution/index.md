---
layout: default
title: Beta Distribution
description: Learn how the beta distribution models probabilities and proportions, and why it is fundamental in Bayesian statistics.
permalink: /probability/distributions/beta-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/beta-distribution/",
    label: "Beta Distribution",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 5</span>
      <span class="badge">Distributions</span>
      <span class="badge">Continuous</span>
    </div>

    <h1>Beta Distribution</h1>

    <p class="lead">
      Many real-world quantities represent probabilities or proportions.
    </p>

    <p class="lead">
      The beta distribution is specifically designed to model values that must lie between 0 and 1.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/gamma-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/normal-distribution/">
         Next: Normal Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Beta Distribution?</h2>

    <p>
      The beta distribution is a continuous probability distribution defined on the interval from 0 to 1.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A beta distribution models uncertain probabilities, proportions, and percentages that must remain between 0 and 1.
      </p>

    </div>

    <h2>Why We Need the Beta Distribution</h2>

    <p>
      Many quantities naturally have lower and upper limits.
    </p>

    <div class="example-box">

      <p>
        Probability of success
      </p>

      <p>
        Conversion rate
      </p>

      <p>
        Market share
      </p>

      <p>
        Fraction of defective products
      </p>

      <p>
        Percentage of voters supporting a candidate
      </p>

    </div>

    <p>
      These values can never be less than 0 or greater than 1.
    </p>

    <p>
      The beta distribution was designed for exactly this situation.
    </p>

    <h2>The Parameters</h2>

    <p>
      The beta distribution uses two shape parameters:
    </p>

    <ul class="bullets">

      <li>α (alpha)</li>

      <li>β (beta)</li>

    </ul>

    <p>
      These parameters determine the shape of the distribution.
    </p>

    <h2>Notation</h2>

    <p>
      A beta random variable is written as:
    </p>

    <div class="example-box">

      <p>
        X ~ Beta(α, β)
      </p>

    </div>

    <p>
      Different values of α and β create dramatically different shapes.
    </p>

    <h2>The Probability Density Function</h2>

    <p>
      The beta density function is:
    </p>

    0

    <p>
      for:
    </p>

    1

    <p>
      where:
    </p>

    2

    <p>
      is the beta function.
    </p>

    <h2>The Beta Function</h2>

    <p>
      The beta function is a mathematical constant that ensures the total area under the density equals one.
    </p>

    <p>
      It is closely related to the gamma function studied previously.
    </p>

    <h2>Shape Flexibility</h2>

    <p>
      One of the most useful properties of the beta distribution is its flexibility.
    </p>

    <p>
      Different parameter values create very different shapes.
    </p>

    <h2>Case 1: Uniform Distribution</h2>

    <p>
      When:
    </p>

    3

    <p>
      the beta distribution becomes:
    </p>

    <div class="example-box">

      <p>
        Uniform(0,1)
      </p>

    </div>

    <p>
      Every value between 0 and 1 is equally likely.
    </p>

    <h2>Case 2: Symmetric Bell Shape</h2>

    <p>
      When:
    </p>

    <div class="example-box">

      <p>
        α = β > 1
      </p>

    </div>

    <p>
      the distribution becomes symmetric around 0.5.
    </p>

    <p>
      Larger parameter values create a stronger concentration near the center.
    </p>

    <h2>Case 3: Right-Skewed Shape</h2>

    <p>
      When:
    </p>

    <div class="example-box">

      <p>
        α &lt; β
      </p>

    </div>

    <p>
      more probability is concentrated near zero.
    </p>

    <p>
      Small values become more likely than large values.
    </p>

    <h2>Case 4: Left-Skewed Shape</h2>

    <p>
      When:
    </p>

    <div class="example-box">

      <p>
        α &gt; β
      </p>

    </div>

    <p>
      more probability is concentrated near one.
    </p>

    <p>
      Large values become more likely than small values.
    </p>

    <h2>The Mean</h2>

    <p>
      The expected value of a beta distribution is:
    </p>

    4

    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        The mean reflects the balance between α and β.
      </p>

    </div>

    <h2>Example of the Mean</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        α = 8
      </p>

      <p>
        β = 2
      </p>

    </div>

    <p>
      Then:
    </p>

    5

    <p>
      The distribution is centered near 0.8.
    </p>

    <h2>The Variance</h2>

    <p>
      The variance is:
    </p>

    6

    <p>
      Variability depends on both parameters.
    </p>

    <h2>How Confidence Changes Shape</h2>

    <p>
      Consider two distributions with the same mean:
    </p>

    <div class="example-box">

      <p>
        Beta(2,2)
      </p>

      <p>
        Beta(200,200)
      </p>

    </div>

    <p>
      Both have mean 0.5.
    </p>

    <p>
      However,
      Beta(200,200) is much more concentrated around 0.5.
    </p>

    <p>
      Larger parameters imply greater certainty.
    </p>

    <h2>The Bayesian Interpretation</h2>

    <p>
      The beta distribution is especially important in Bayesian statistics.
    </p>

    <p>
      It is often used to represent uncertainty about an unknown probability.
    </p>

    <div class="example-box">

      <p>
        What is the true conversion rate?
      </p>

      <p>
        What is the true disease prevalence?
      </p>

      <p>
        What is the true click-through probability?
      </p>

    </div>

    <p>
      The beta distribution provides a probability model for these unknown probabilities.
    </p>

    <h2>Why Bayesian Analysts Love the Beta Distribution</h2>

    <p>
      When observing successes and failures,
      beta distributions update very naturally.
    </p>

    <p>
      This mathematical convenience makes them a standard Bayesian tool.
    </p>

    <h2>Applications of the Beta Distribution</h2>

    <ul class="bullets">

      <li>A/B testing</li>

      <li>Marketing conversion analysis</li>

      <li>Reliability estimation</li>

      <li>Medical probability modeling</li>

      <li>Survey response proportions</li>

      <li>Bayesian inference</li>

    </ul>

    <p>
      Any uncertain probability may potentially be modeled with a beta distribution.
    </p>

    <h2>Relationship to Other Distributions</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Distribution</th>
            <th>Relationship</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Uniform</td>
            <td>Beta(1,1)</td>
          </tr>

          <tr>
            <td>Gamma</td>
            <td>Closely related through the beta function</td>
          </tr>

          <tr>
            <td>Bernoulli/Binomial</td>
            <td>Common Bayesian partner</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Why the Beta Distribution Matters</h2>

    <p>
      The beta distribution is the standard probability model for uncertain probabilities.
    </p>

    <p>
      Its flexibility allows it to represent a wide range of beliefs and data situations.
    </p>

    <p>
      It plays a foundational role in modern Bayesian statistics and decision-making under uncertainty.
    </p>

    <h2>The Limitation</h2>

    <p>
      Beta distributions are restricted to values between 0 and 1.
    </p>

    <p>
      Many natural measurements can take any real value.
    </p>

    <div class="example-box">

      <p>
        Heights
      </p>

      <p>
        Test scores
      </p>

      <p>
        Measurement errors
      </p>

      <p>
        IQ scores
      </p>

    </div>

    <p>
      Such quantities are often modeled using the most famous probability distribution of all:
      the normal distribution.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The normal distribution is the central distribution of probability and statistics.
    </p>

    <p>
      Its appearance throughout science, data analysis, and machine learning makes it one of the most important concepts in all of statistics.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The beta distribution models probabilities and proportions between 0 and 1</li>

        <li>It is controlled by two shape parameters, α and β</li>

        <li>The beta distribution can take many different shapes</li>

        <li>The mean equals α/(α + β)</li>

        <li>The variance depends on both α and β</li>

        <li>Beta(1,1) is the uniform distribution</li>

        <li>The beta distribution is fundamental in Bayesian statistics</li>

        <li>It is widely used to model uncertainty about probabilities</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/gamma-distribution/">
         ← Previous: Gamma Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/normal-distribution/">
         Next: Normal Distribution →
      </a>

    </div>

  </div>

</section>