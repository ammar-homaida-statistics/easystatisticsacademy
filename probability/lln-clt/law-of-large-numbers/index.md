---
layout: default
title: Law of Large Numbers
description: Learn how the Law of Large Numbers explains why averages and proportions become more stable as sample sizes increase.
permalink: /probability/lln-clt/law-of-large-numbers/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_lln_clt_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/lln-clt/law-of-large-numbers/",
    label: "Law of Large Numbers",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 6</span>
      <span class="badge">LLN & CLT</span>
      <span class="badge">Core Theorem</span>
    </div>

    <h1>Law of Large Numbers</h1>

    <p class="lead">
      One of the most important results in probability explains why averages become more reliable as we collect more data.
    </p>

    <p class="lead">
      The Law of Large Numbers provides the foundation for statistical estimation, polling, experimentation, and data science.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/lln-clt/convergence-intuition/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/lln-clt/weak-vs-strong-lln/">
         Next: Weak vs Strong LLN →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is the Law of Large Numbers?</h2>

    <p>
      The Law of Large Numbers (LLN) states that sample averages tend to approach the true population mean as the sample size increases.
    </p>

    <div class="concept-box">

      <strong>Core idea:</strong>

      <p>
        More observations lead to more stable averages.
      </p>

    </div>

    <h2>The Big Question</h2>

    <p>
      Suppose we repeatedly observe a random process.
    </p>

    <div class="example-box">

      <p>
        Toss a coin
      </p>

      <p>
        Roll a die
      </p>

      <p>
        Measure customer spending
      </p>

      <p>
        Record daily temperatures
      </p>

    </div>

    <p>
      Will the average eventually settle near the true value?
    </p>

    <p>
      The Law of Large Numbers says yes.
    </p>

    <h2>A Coin Toss Example</h2>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        Head = 1
      </p>

      <p>
        Tail = 0
      </p>

    </div>

    <p>
      The population mean is:
    </p>

    0

    <p>
      because a fair coin lands heads with probability 0.5.
    </p>

    <p>
      After a few tosses,
      the sample average may vary substantially.
    </p>

    <div class="example-box">

      <p>
        1.00
      </p>

      <p>
        0.75
      </p>

      <p>
        0.40
      </p>

      <p>
        0.67
      </p>

    </div>

    <p>
      As the number of tosses grows,
      the average typically moves closer to 0.5.
    </p>

    <h2>The Sample Mean</h2>

    <p>
      For observations:
    </p>

    <div class="example-box">

      <p>
        X₁, X₂, ..., Xₙ
      </p>

    </div>

    <p>
      the sample mean is:
    </p>

    1

    <p>
      The Law of Large Numbers concerns the behavior of this quantity as n becomes large.
    </p>

    <h2>The Main Result</h2>

    <p>
      If observations are independent and identically distributed with finite mean:
    </p>

    <p>
      then:
    </p>

    2

    <p>
      as the sample size increases.
    </p>

    <p>
      The sample mean converges toward the population mean.
    </p>

    <h2>What This Means Practically</h2>

    <p>
      Small samples can be misleading.
    </p>

    <p>
      Large samples tend to be more representative.
    </p>

    <div class="example-box">

      <p>
        10 survey responses → unstable estimate
      </p>

      <p>
        10,000 survey responses → much more stable estimate
      </p>

    </div>

    <p>
      The Law of Large Numbers explains why larger datasets are valuable.
    </p>

    <h2>Randomness Does Not Disappear</h2>

    <p>
      A common misconception is that outcomes become deterministic.
    </p>

    <p>
      Individual observations remain random.
    </p>

    <p>
      What becomes stable is the average.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        The Law of Large Numbers applies to averages, not individual outcomes.
      </p>

    </div>

    <h2>A Die Rolling Example</h2>

    <p>
      Consider repeatedly rolling a fair die.
    </p>

    <p>
      The population mean equals:
    </p>

    3

    <p>
      because:
    </p>

    4

    <p>
      Early averages may fluctuate considerably.
    </p>

    <p>
      After thousands of rolls,
      the average usually becomes very close to 3.5.
    </p>

    <h2>Why the Law Works</h2>

    <p>
      Positive and negative deviations from the true mean tend to cancel each other out.
    </p>

    <p>
      As more observations accumulate,
      the influence of any single observation decreases.
    </p>

    <p>
      The average becomes increasingly stable.
    </p>

    <h2>Connection to Variability</h2>

    <p>
      The variability of the sample mean decreases as sample size grows.
    </p>

    <p>
      Specifically:
    </p>

    5

    <p>
      for independent observations.
    </p>

    <p>
      Larger n produces smaller variance.
    </p>

    <h2>Why Polls Improve with Larger Samples</h2>

    <p>
      Election polls estimate population proportions.
    </p>

    <p>
      Small samples can produce large errors.
    </p>

    <p>
      Larger samples usually produce estimates closer to the truth.
    </p>

    <p>
      The Law of Large Numbers provides the theoretical justification.
    </p>

    <h2>Applications of the Law of Large Numbers</h2>

    <ul class="bullets">

      <li>Survey sampling</li>

      <li>Quality control</li>

      <li>Scientific experiments</li>

      <li>Machine learning</li>

      <li>Monte Carlo simulation</li>

      <li>Financial forecasting</li>

      <li>Clinical trials</li>

    </ul>

    <p>
      Nearly every data-driven field relies on this principle.
    </p>

    <h2>What the Law Does Not Say</h2>

    <p>
      The Law of Large Numbers does not guarantee:
    </p>

    <ul class="bullets">

      <li>Perfect estimates</li>

      <li>Fast convergence</li>

      <li>No future fluctuations</li>

      <li>Accurate results from biased data</li>

    </ul>

    <p>
      It simply states that averages tend to move closer to the true mean as sample size grows.
    </p>

    <h2>The Gambling Misunderstanding</h2>

    <p>
      Some people incorrectly believe the Law of Large Numbers implies short-run balancing.
    </p>

    <div class="example-box">

      <p>
        "Five tails in a row means a head is due."
      </p>

    </div>

    <p>
      This is false.
    </p>

    <p>
      The theorem concerns long-run averages,
      not immediate compensation for recent outcomes.
    </p>

    <h2>Why This Theorem Is Fundamental</h2>

    <p>
      Statistics seeks to learn about populations using samples.
    </p>

    <p>
      That goal would be impossible if sample averages failed to approach population values.
    </p>

    <p>
      The Law of Large Numbers guarantees that collecting more data generally improves estimation.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Several versions of the Law of Large Numbers exist.
    </p>

    <p>
      The next lesson compares the weak and strong forms of the theorem and explains how they differ mathematically.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The Law of Large Numbers states that sample averages approach population means</li>

        <li>Larger samples generally produce more stable estimates</li>

        <li>The theorem concerns long-run behavior</li>

        <li>Individual observations remain random</li>

        <li>The variability of sample means decreases as sample size increases</li>

        <li>The theorem underlies polling, experimentation, and statistical estimation</li>

        <li>The Law of Large Numbers does not imply short-run balancing of outcomes</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/lln-clt/convergence-intuition/">
         ← Previous: Convergence Intuition
      </a>

      <a class="btn"
         href="/probability/lln-clt/weak-vs-strong-lln/">
         Next: Weak vs Strong LLN →
      </a>

    </div>

  </div>

</section>