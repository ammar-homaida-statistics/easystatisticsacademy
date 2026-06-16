---
layout: default
title: Uniform Distribution
description: Learn how the uniform distribution models situations where all outcomes within a range are equally likely.
permalink: /probability/distributions/uniform-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/uniform-distribution/",
    label: "Uniform Distribution",
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

    <h1>Uniform Distribution</h1>

    <p class="lead">
      Many distributions assign different probabilities to different values.
    </p>

    <p class="lead">
      The uniform distribution is unique because every value within a specified range is equally likely.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/hypergeometric-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/exponential-distribution/">
         Next: Exponential Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Uniform Distribution?</h2>

    <p>
      A uniform distribution describes a random variable whose values are equally likely within a specified interval.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        In a uniform distribution, every value in the interval has the same probability density.
      </p>

    </div>

    <h2>A Simple Example</h2>

    <p>
      Suppose a random number is selected between 0 and 10.
    </p>

    <p>
      Every value inside that interval is equally likely.
    </p>

    <div class="example-box">

      <p>
        2.3 is just as likely as 7.8
      </p>

      <p>
        0.5 is just as likely as 9.2
      </p>

    </div>

    <p>
      No region is favored over another.
    </p>

    <h2>Continuous Uniform Distribution</h2>

    <p>
      The most common version is the continuous uniform distribution.
    </p>

    <p>
      It is defined on an interval:
    </p>

    0

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>a = lower bound</li>

      <li>b = upper bound</li>

    </ul>

    <h2>Notation</h2>

    <p>
      A continuous uniform random variable is written as:
    </p>

    <div class="example-box">

      <p>
        X ~ Uniform(a,b)
      </p>

    </div>

    <p>
      The interval boundaries completely determine the distribution.
    </p>

    <h2>The Probability Density Function</h2>

    <p>
      The probability density is constant throughout the interval.
    </p>

    1

    <p>
      for:
    </p>

    2

    <p>
      and zero elsewhere.
    </p>

    <h2>Why the Density Is Constant</h2>

    <p>
      Since all values are equally likely,
      the graph of the density is a horizontal line.
    </p>

    <p>
      The total area under the curve must equal one.
    </p>

    <p>
      Therefore the height must be:
    </p>

    3

    <h2>The Shape</h2>

    <p>
      The probability density graph forms a rectangle.
    </p>

    <div class="example-box">

      <p>
        Equal height everywhere
      </p>

      <p>
        No peaks
      </p>

      <p>
        No skewness
      </p>

    </div>

    <p>
      This simple shape explains the name "uniform."
    </p>

    <h2>Probabilities as Areas</h2>

    <p>
      For continuous distributions,
      probabilities correspond to areas under the density curve.
    </p>

    <p>
      Therefore:
    </p>

    4

    <p>
      whenever c and d lie inside the interval.
    </p>

    <h2>Example: Probability in a Subinterval</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        X ~ Uniform(0,10)
      </p>

    </div>

    <p>
      What is:
    </p>

    <div class="example-box">

      <p>
        P(2 ≤ X ≤ 5)
      </p>

    </div>

    <p>
      Using the interval-length rule:
    </p>

    5

    <p>
      The probability equals 0.3.
    </p>

    <h2>Single Values Have Zero Probability</h2>

    <p>
      Continuous random variables behave differently from discrete variables.
    </p>

    <p>
      For any specific value:
    </p>

    6

    <p>
      because individual points have zero area.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Continuous distributions assign probability to intervals, not individual values.
      </p>

    </div>

    <h2>The Mean</h2>

    <p>
      The expected value is:
    </p>

    7

    <p>
      This is simply the midpoint of the interval.
    </p>

    <h2>Example of the Mean</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        X ~ Uniform(0,10)
      </p>

    </div>

    <p>
      Then:
    </p>

    8

    <p>
      The center lies exactly in the middle.
    </p>

    <h2>The Variance</h2>

    <p>
      The variance of a continuous uniform distribution is:
    </p>

    9

    <p>
      The spread depends only on the interval width.
    </p>

    <h2>Standard Deviation</h2>

    <p>
      Taking the square root gives:
    </p>

    10

    <p>
      Wider intervals produce larger variability.
    </p>

    <h2>Common Applications</h2>

    <ul class="bullets">

      <li>Random number generation</li>

      <li>Simulation studies</li>

      <li>Randomized experiments</li>

      <li>Computer games</li>

      <li>Modeling equally likely arrival times</li>

    </ul>

    <p>
      Uniform distributions are fundamental in simulation and computational statistics.
    </p>

    <h2>Uniform Distribution in Simulation</h2>

    <p>
      Most random-number generators begin by producing values from a uniform distribution.
    </p>

    <p>
      Other probability distributions are often generated from uniform random numbers.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The uniform distribution serves as the foundation of modern simulation methods.
      </p>

    </div>

    <h2>Discrete Versus Continuous Uniform</h2>

    <p>
      There is also a discrete uniform distribution.
    </p>

    <div class="example-box">

      <p>
        Rolling a fair die
      </p>

      <p>
        Drawing a random day of the week
      </p>

    </div>

    <p>
      In this lesson,
      we focus on the continuous version,
      which is more important for continuous probability models.
    </p>

    <h2>Why the Uniform Distribution Matters</h2>

    <p>
      The uniform distribution is the simplest continuous distribution.
    </p>

    <p>
      It introduces key ideas such as:
    </p>

    <ul class="bullets">

      <li>Probability density functions</li>

      <li>Area-based probabilities</li>

      <li>Continuous random variables</li>

      <li>Interval probabilities</li>

    </ul>

    <p>
      These ideas form the basis for many advanced continuous distributions.
    </p>

    <h2>The Limitation</h2>

    <p>
      Uniform distributions assume all values are equally likely.
    </p>

    <p>
      Many real-world waiting-time problems do not behave this way.
    </p>

    <div class="example-box">

      <p>
        Time until the next customer arrives
      </p>

      <p>
        Time until a machine fails
      </p>

      <p>
        Time until a phone call occurs
      </p>

    </div>

    <p>
      These waiting-time problems are often modeled by the exponential distribution.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The exponential distribution is one of the most important continuous probability distributions.
    </p>

    <p>
      It models waiting times between random events and possesses a remarkable memoryless property.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The uniform distribution assigns equal probability density throughout an interval</li>

        <li>Its density is constant and equal to 1/(b − a)</li>

        <li>Probabilities are determined by interval lengths</li>

        <li>Single points have probability zero</li>

        <li>The mean equals (a + b)/2</li>

        <li>The variance equals (b − a)²/12</li>

        <li>The uniform distribution is fundamental to simulation and continuous probability theory</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/hypergeometric-distribution/">
         ← Previous: Hypergeometric Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/exponential-distribution/">
         Next: Exponential Distribution →
      </a>

    </div>

  </div>

</section>