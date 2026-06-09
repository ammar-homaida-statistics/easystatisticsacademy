---
layout: default
title: Applications and Mini Cases
description: Apply expectation, variance, covariance, correlation, and indicator variables to real-world probability problems.
permalink: /probability/expectation-variance/applications-mini-cases/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_expectation_variance_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/expectation-variance/applications-mini-cases/",
    label: "Applications and Mini Cases",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 4</span>
      <span class="badge">Expectation & Variance</span>
      <span class="badge">Applications</span>
    </div>

    <h1>Applications and Mini Cases</h1>

    <p class="lead">
      Probability concepts become truly valuable when they are applied to real decisions and real data.
    </p>

    <p class="lead">
      This lesson brings together expectation, variance, covariance, correlation, and indicator variables through practical examples.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/expectation-variance/indicator-random-variables/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/">
         Next Block: Distributions →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Bringing the Ideas Together</h2>

    <p>
      Throughout this block,
      we studied several important concepts:
    </p>

    <ul class="bullets">

      <li>Expectation</li>

      <li>Variance</li>

      <li>Covariance</li>

      <li>Correlation</li>

      <li>Indicator variables</li>

    </ul>

    <p>
      These ideas rarely appear in isolation.
    </p>

    <p>
      Real-world problems often require multiple concepts working together.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Probability models become powerful when expectation and variability are used together to describe uncertainty.
      </p>

    </div>

    <h2>Mini Case 1: Customer Arrivals</h2>

    <p>
      A small coffee shop records the number of customers arriving each hour.
    </p>

    <p>
      Historical data suggests:
    </p>

    <div class="example-box">

      <p>
        Expected arrivals = 30 customers
      </p>

      <p>
        Standard deviation = 5 customers
      </p>

    </div>

    <p>
      What do these values mean?
    </p>

    <ul class="bullets">

      <li>The average hour has about 30 customers.</li>

      <li>Actual customer counts vary around that average.</li>

      <li>A standard deviation of 5 indicates moderate variability.</li>

    </ul>

    <p>
      Managers can use this information for staffing decisions.
    </p>

    <h2>Mini Case 2: Insurance Risk</h2>

    <p>
      An insurance company estimates:
    </p>

    <div class="example-box">

      <p>
        Expected claim cost = $500
      </p>

      <p>
        Standard deviation = $2,000
      </p>

    </div>

    <p>
      The average claim cost appears manageable.
    </p>

    <p>
      However,
      the large standard deviation indicates substantial uncertainty.
    </p>

    <p>
      Variability is often as important as the average itself.
    </p>

    <h2>Mini Case 3: Exam Performance</h2>

    <p>
      Suppose two classes have:
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Class</th>
            <th>Mean</th>
            <th>Standard Deviation</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>A</td>
            <td>75</td>
            <td>4</td>
          </tr>

          <tr>
            <td>B</td>
            <td>75</td>
            <td>15</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Both classes have identical averages.
    </p>

    <p>
      Class B exhibits much greater variability.
    </p>

    <p>
      Expectation alone does not fully describe performance.
    </p>

    <h2>Mini Case 4: Portfolio Diversification</h2>

    <p>
      An investor owns two assets.
    </p>

    <p>
      Each asset has its own expected return and variance.
    </p>

    <p>
      The overall risk depends not only on the individual variances but also on covariance.
    </p>

    <div class="example-box">

      <p>
        Positive covariance → assets move together
      </p>

      <p>
        Negative covariance → assets offset one another
      </p>

    </div>

    <p>
      Diversification works because covariance influences total variability.
    </p>

    <h2>Mini Case 5: Website Clicks</h2>

    <p>
      A marketing team studies whether users click an advertisement.
    </p>

    <p>
      Define:
    </p>

    <div class="example-box">

      <p>
        I = 1 if the user clicks
      </p>

      <p>
        I = 0 otherwise
      </p>

    </div>

    <p>
      This is an indicator random variable.
    </p>

    <p>
      If:
    </p>

    <div class="example-box">

      <p>
        P(click) = 0.08
      </p>

    </div>

    <p>
      then:
    </p>

    0

    <p>
      The expected value equals the click probability.
    </p>

    <h2>Mini Case 6: Manufacturing Defects</h2>

    <p>
      A factory inspects 1,000 products.
    </p>

    <p>
      Each product has a 2% probability of being defective.
    </p>

    <p>
      Define an indicator variable for each item:
    </p>

    <div class="example-box">

      <p>
        Iᵢ = 1 if item i is defective
      </p>

      <p>
        Iᵢ = 0 otherwise
      </p>

    </div>

    <p>
      Total defects:
    </p>

    1

    <p>
      Using linearity of expectation:
    </p>

    2

    <p>
      The factory expects approximately 20 defective products.
    </p>

    <h2>Mini Case 7: Studying Relationships</h2>

    <p>
      A researcher investigates:
    </p>

    <div class="example-box">

      <p>
        Hours studied
      </p>

      <p>
        Exam score
      </p>

    </div>

    <p>
      A positive correlation is observed.
    </p>

    <p>
      This indicates that students who study more tend to score higher.
    </p>

    <p>
      However,
      correlation alone cannot establish causation.
    </p>

    <div class="concept-box">

      <strong>Reminder:</strong>

      <p>
        Correlation measures association, not cause-and-effect relationships.
      </p>

    </div>

    <h2>Choosing the Right Quantity</h2>

    <p>
      Different probability questions require different tools.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Question</th>
            <th>Tool</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>What is the average outcome?</td>
            <td>Expectation</td>
          </tr>

          <tr>
            <td>How variable are outcomes?</td>
            <td>Variance / Standard Deviation</td>
          </tr>

          <tr>
            <td>Do variables move together?</td>
            <td>Covariance</td>
          </tr>

          <tr>
            <td>How strong is the relationship?</td>
            <td>Correlation</td>
          </tr>

          <tr>
            <td>How many events occur?</td>
            <td>Indicator Variables</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Building a Probability Description</h2>

    <p>
      A complete probability description often includes:
    </p>

    <ul class="bullets">

      <li>Expected value</li>

      <li>Variance or standard deviation</li>

      <li>Relationships with other variables</li>

      <li>Probability distributions</li>

    </ul>

    <p>
      Together,
      these provide a much richer understanding than any single measure alone.
    </p>

    <h2>What We Learned in Block 4</h2>

    <p>
      This block expanded our understanding of expectation and variability.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Topic</th>
            <th>Main Idea</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Linearity of Expectation</td>
            <td>Expectations always add.</td>
          </tr>

          <tr>
            <td>Variance Rules</td>
            <td>Variability depends on covariance.</td>
          </tr>

          <tr>
            <td>Covariance</td>
            <td>Measures joint movement.</td>
          </tr>

          <tr>
            <td>Correlation</td>
            <td>Standardized measure of association.</td>
          </tr>

          <tr>
            <td>Indicator Variables</td>
            <td>Simplify counting problems.</td>
          </tr>

          <tr>
            <td>Applications</td>
            <td>Combine concepts in practical settings.</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Big Picture</h2>

    <p>
      Expectation describes center.
    </p>

    <p>
      Variance describes spread.
    </p>

    <p>
      Covariance and correlation describe relationships.
    </p>

    <p>
      Indicator variables simplify counting.
    </p>

    <p>
      Together,
      these concepts form the core mathematical toolkit for analyzing random phenomena.
    </p>

    <h2>Preparing for Distributions</h2>

    <p>
      So far,
      we have studied general properties of random variables.
    </p>

    <p>
      The next block introduces specific probability distributions.
    </p>

    <p>
      These distributions provide standardized models for many common types of random behavior and form the foundation of statistical modeling.
    </p>

    <!-- BLOCK TAKEAWAYS -->

    <div class="summary-box">

      <h2>Block 4 Takeaways</h2>

      <ul class="bullets">

        <li>Expectation measures long-run average behavior</li>

        <li>Linearity of expectation simplifies many calculations</li>

        <li>Variance measures uncertainty around the mean</li>

        <li>Covariance measures joint variability</li>

        <li>Correlation standardizes covariance</li>

        <li>Indicator variables simplify counting problems</li>

        <li>Expectation and variability are both necessary for describing uncertainty</li>

        <li>These concepts appear throughout statistics, finance, machine learning, and data science</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/expectation-variance/indicator-random-variables/">
         ← Previous: Indicator Random Variables
      </a>

      <a class="btn"
         href="/probability/expectation-variance/">
         Expectation & Variance Home
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/">
         Next Block: Distributions →
      </a>

    </div>

  </div>

</section>