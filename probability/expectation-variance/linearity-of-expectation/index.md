---
layout: default
title: Linearity of Expectation
description: Learn one of the most powerful results in probability: the expectation of a sum equals the sum of expectations.
permalink: /probability/expectation-variance/linearity-of-expectation/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_expectation_variance_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/expectation-variance/linearity-of-expectation/",
    label: "Linearity of Expectation",
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
      <span class="badge">Core Property</span>
    </div>

    <h1>Linearity of Expectation</h1>

    <p class="lead">
      Expectation has a remarkable property that makes many probability problems surprisingly simple.
    </p>

    <p class="lead">
      The expected value of a sum is always the sum of the expected values, even when random variables are dependent.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/expectation-variance/">
         ← Expectation & Variance Home
      </a>

      <a class="btn btn-outline"
         href="/probability/expectation-variance/variance-rules-and-sums/">
         Next: Variance Rules and Sums →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Linearity Matters</h2>

    <p>
      Many probability problems involve totals.
    </p>

    <div class="example-box">

      <p>
        Total sales during a day
      </p>

      <p>
        Total goals scored by a team
      </p>

      <p>
        Total defects in a production batch
      </p>

      <p>
        Total number of heads in many coin tosses
      </p>

    </div>

    <p>
      Rather than calculating the entire distribution of the total,
      expectation allows us to focus directly on the average outcome.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Expectations add together in a simple and predictable way.
      </p>

    </div>

    <h2>The Fundamental Rule</h2>

    <p>
      If X and Y are random variables:
    </p>

    0

    <p>
      This is called the linearity of expectation.
    </p>

    <p>
      It is one of the most useful results in probability theory.
    </p>

    <h2>Extending to Many Variables</h2>

    <p>
      The rule applies to any number of random variables.
    </p>

    1

    <p>
      Regardless of how many variables are involved,
      their expectations simply add.
    </p>

    <h2>The Surprising Part</h2>

    <p>
      Many probability rules require independence.
    </p>

    <p>
      Linearity of expectation does not.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Linearity of expectation works whether variables are independent or dependent.
      </p>

    </div>

    <p>
      This feature makes it extraordinarily powerful.
    </p>

    <h2>Example: Two Dice</h2>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = First die
      </p>

      <p>
        Y = Second die
      </p>

    </div>

    <p>
      We know:
    </p>

    2

    <p>
      and:
    </p>

    3

    <p>
      Therefore:
    </p>

    4

    <p>
      The average total of two dice is 7.
    </p>

    <h2>Expectation of a Difference</h2>

    <p>
      Linearity also applies to subtraction.
    </p>

    5

    <p>
      Expectations behave just like ordinary algebra.
    </p>

    <h2>Multiplying by a Constant</h2>

    <p>
      Constants can be factored out of expectations.
    </p>

    6

    <p>
      This property is often used when transforming variables.
    </p>

    <h2>Combining Constants and Variables</h2>

    <p>
      For a linear transformation:
    </p>

    7

    <p>
      The expected value transforms in exactly the same way.
    </p>

    <h2>Example: Exam Scores</h2>

    <p>
      Suppose the average exam score is:
    </p>

    <div class="example-box">

      <p>
        E(X) = 70
      </p>

    </div>

    <p>
      If every student's score receives 5 bonus points:
    </p>

    <div class="example-box">

      <p>
        Y = X + 5
      </p>

    </div>

    <p>
      Then:
    </p>

    8

    <p>
      The average score increases by exactly five points.
    </p>

    <h2>Indicator Variables</h2>

    <p>
      One of the most powerful applications of linearity uses indicator variables.
    </p>

    <p>
      An indicator variable equals:
    </p>

    <div class="example-box">

      <p>
        1 if an event occurs
      </p>

      <p>
        0 otherwise
      </p>

    </div>

    <p>
      For an indicator variable I:
    </p>

    9

    <p>
      This simple relationship is extremely useful in counting problems.
    </p>

    <h2>Example: Number of Heads</h2>

    <p>
      Suppose ten fair coins are tossed.
    </p>

    <p>
      Define:
    </p>

    <div class="example-box">

      <p>
        Iᵢ = 1 if toss i is heads
      </p>

      <p>
        Iᵢ = 0 if toss i is tails
      </p>

    </div>

    <p>
      The total number of heads is:
    </p>

    10

    <p>
      Applying linearity:
    </p>

    11

    <p>
      Since each expectation equals 0.5:
    </p>

    12

    <p>
      On average,
      five heads are expected.
    </p>

    <h2>Why This Is Useful</h2>

    <p>
      Notice that we never needed the entire distribution of H.
    </p>

    <p>
      Linearity allowed us to compute the expected total directly.
    </p>

    <p>
      This often saves substantial work.
    </p>

    <h2>Applications of Linearity</h2>

    <ul class="bullets">

      <li>Counting problems</li>

      <li>Machine learning</li>

      <li>Quality control</li>

      <li>Queueing systems</li>

      <li>Network analysis</li>

      <li>Risk management</li>

    </ul>

    <p>
      Many advanced probability proofs rely heavily on this principle.
    </p>

    <h2>A Common Mistake</h2>

    <p>
      Students often assume similar rules hold for variance.
    </p>

    <p>
      Expectation is linear,
      but variance behaves differently.
    </p>

    <div class="example-box">

      <p>
        Expectations always add.
      </p>

      <p>
        Variances require additional conditions.
      </p>

    </div>

    <p>
      This distinction is extremely important.
    </p>

    <h2>The Big Picture</h2>

    <p>
      Linearity of expectation transforms complicated random processes into manageable calculations.
    </p>

    <p>
      By focusing on averages,
      we can often bypass difficult probability computations entirely.
    </p>

    <p>
      This makes expectation one of the most practical tools in probability theory.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Expectation behaves very simply when variables are added together.
    </p>

    <p>
      Variance is more complicated.
    </p>

    <p>
      The next lesson explores how variances combine,
      when they add directly,
      and why independence becomes important.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>E(X + Y) = E(X) + E(Y)</li>

        <li>Linearity extends to any number of variables</li>

        <li>Linearity works even when variables are dependent</li>

        <li>Constants factor out of expectations</li>

        <li>E(aX + b) = aE(X) + b</li>

        <li>Indicator variables provide powerful applications of linearity</li>

        <li>Linearity of expectation is one of the most useful tools in probability</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/expectation-variance/">
         Expectation & Variance Home
      </a>

      <a class="btn"
         href="/probability/expectation-variance/variance-rules-and-sums/">
         Next: Variance Rules and Sums →
      </a>

    </div>

  </div>

</section>