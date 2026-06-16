---
layout: default
title: Hypergeometric Distribution
description: Learn how the hypergeometric distribution models sampling without replacement from a finite population.
permalink: /probability/distributions/hypergeometric-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/hypergeometric-distribution/",
    label: "Hypergeometric Distribution",
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
      <span class="badge">Sampling</span>
    </div>

    <h1>Hypergeometric Distribution</h1>

    <p class="lead">
      Many probability models assume independent trials with replacement.
    </p>

    <p class="lead">
      The hypergeometric distribution handles a different situation: sampling without replacement from a finite population.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/poisson-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/uniform-distribution/">
         Next: Uniform Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Hypergeometric Distribution?</h2>

    <p>
      A hypergeometric distribution models the number of successes obtained when drawing a sample from a finite population without replacement.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A hypergeometric random variable counts the number of successes in a sample drawn without replacement from a finite population.
      </p>

    </div>

    <h2>The Key Difference</h2>

    <p>
      Unlike the binomial distribution,
      sampling is performed without replacement.
    </p>

    <p>
      As a result,
      probabilities change after each draw.
    </p>

    <div class="example-box">

      <p>
        Draw one card from a deck.
      </p>

      <p>
        The deck composition changes before the next draw.
      </p>

    </div>

    <p>
      This creates dependence between observations.
    </p>

    <h2>A Classic Example</h2>

    <p>
      Consider a standard deck of 52 cards.
    </p>

    <p>
      Suppose we draw 5 cards.
    </p>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = Number of aces drawn
      </p>

    </div>

    <p>
      Since cards are not replaced,
      X follows a hypergeometric distribution.
    </p>

    <h2>The Four Parameters</h2>

    <p>
      A hypergeometric distribution is determined by four values.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Parameter</th>
            <th>Meaning</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>N</td>
            <td>Total population size</td>
          </tr>

          <tr>
            <td>K</td>
            <td>Number of successes in population</td>
          </tr>

          <tr>
            <td>n</td>
            <td>Sample size</td>
          </tr>

          <tr>
            <td>x</td>
            <td>Observed successes in sample</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Notation</h2>

    <p>
      A hypergeometric random variable is commonly written as:
    </p>

    <div class="example-box">

      <p>
        X ~ Hypergeometric(N, K, n)
      </p>

    </div>

    <p>
      The parameters describe the population and sample structure.
    </p>

    <h2>Understanding the Population</h2>

    <p>
      Imagine a population containing:
    </p>

    <div class="example-box">

      <p>
        K successes
      </p>

      <p>
        N − K failures
      </p>

    </div>

    <p>
      We draw n items without replacement and count successes.
    </p>

    <h2>The Probability Formula</h2>

    <p>
      The probability of observing exactly x successes is:
    </p>

    0

    <p>
      This is the hypergeometric probability mass function.
    </p>

    <h2>Interpreting the Formula</h2>

    <p>
      The numerator counts favorable samples.
    </p>

    <ul class="bullets">

      <li>Select x successes from K available successes.</li>

      <li>Select n − x failures from N − K failures.</li>

    </ul>

    <p>
      The denominator counts all possible samples of size n.
    </p>

    <h2>Example: Defective Products</h2>

    <p>
      Suppose a shipment contains:
    </p>

    <div class="example-box">

      <p>
        N = 100 products
      </p>

      <p>
        K = 10 defective products
      </p>

    </div>

    <p>
      A sample of:
    </p>

    <div class="example-box">

      <p>
        n = 5 products
      </p>

    </div>

    <p>
      is selected without replacement.
    </p>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = Number of defective products found
      </p>

    </div>

    <p>
      X follows a hypergeometric distribution.
    </p>

    <h2>Possible Values</h2>

    <p>
      The number of successes cannot exceed:
    </p>

    <ul class="bullets">

      <li>The sample size</li>

      <li>The number of successes available</li>

    </ul>

    <p>
      Therefore possible values depend on N, K, and n.
    </p>

    <h2>The Mean</h2>

    <p>
      The expected value is:
    </p>

    1

    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        The expected number of successes equals the sample size multiplied by the population success proportion.
      </p>

    </div>

    <h2>Example of the Mean</h2>

    <p>
      Using:
    </p>

    <div class="example-box">

      <p>
        N = 100
      </p>

      <p>
        K = 10
      </p>

      <p>
        n = 5
      </p>

    </div>

    <p>
      We obtain:
    </p>

    2

    <p>
      On average,
      half a defective product is expected per sample.
    </p>

    <h2>The Variance</h2>

    <p>
      The variance is:
    </p>

    3

    <p>
      The final fraction is called the finite population correction factor.
    </p>

    <h2>The Finite Population Correction</h2>

    <p>
      Because sampling occurs without replacement,
      observations become dependent.
    </p>

    <p>
      This dependence reduces variability.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Hypergeometric variance is smaller than comparable binomial variance because sampling without replacement reduces uncertainty.
      </p>

    </div>

    <h2>Hypergeometric Versus Binomial</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Binomial</th>
            <th>Hypergeometric</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Replacement</td>
            <td>With replacement</td>
            <td>Without replacement</td>
          </tr>

          <tr>
            <td>Independence</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Probability Constant?</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Population Size</td>
            <td>Effectively infinite</td>
            <td>Finite</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>When Binomial Is a Good Approximation</h2>

    <p>
      If the population is very large relative to the sample:
    </p>

    <div class="example-box">

      <p>
        Sample size is less than about 5% of the population.
      </p>

    </div>

    <p>
      Then the hypergeometric distribution is often well approximated by a binomial distribution.
    </p>

    <p>
      In that case,
      dependence becomes negligible.
    </p>

    <h2>Applications of the Hypergeometric Distribution</h2>

    <ul class="bullets">

      <li>Quality control sampling</li>

      <li>Card games</li>

      <li>Election auditing</li>

      <li>Inventory inspection</li>

      <li>Biological sampling</li>

      <li>Survey analysis</li>

    </ul>

    <p>
      Any finite-population sampling problem without replacement may involve a hypergeometric model.
    </p>

    <h2>The Shape of the Distribution</h2>

    <p>
      Hypergeometric distributions can be symmetric or skewed depending on:
    </p>

    <ul class="bullets">

      <li>Population size</li>

      <li>Success proportion</li>

      <li>Sample size</li>

    </ul>

    <p>
      Their shapes often resemble binomial distributions when populations are large.
    </p>

    <h2>Why This Distribution Matters</h2>

    <p>
      The hypergeometric distribution provides a realistic model for many sampling situations because real-world sampling often occurs without replacement.
    </p>

    <p>
      It bridges probability theory and practical statistical sampling.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      So far,
      we have focused primarily on discrete distributions.
    </p>

    <p>
      The next lesson introduces the uniform distribution,
      one of the simplest continuous probability distributions and the starting point for continuous probability models.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The hypergeometric distribution models sampling without replacement</li>

        <li>It counts successes drawn from a finite population</li>

        <li>The distribution depends on N, K, and n</li>

        <li>The mean equals n(K/N)</li>

        <li>The variance includes a finite population correction factor</li>

        <li>Sampling without replacement creates dependence between observations</li>

        <li>Hypergeometric models are widely used in quality control and survey sampling</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/poisson-distribution/">
         ← Previous: Poisson Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/uniform-distribution/">
         Next: Uniform Distribution →
      </a>

    </div>

  </div>

</section>