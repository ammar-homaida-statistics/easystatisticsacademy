---
layout: default
title: Cumulative Distribution Function (CDF)
description: Learn how cumulative distribution functions describe probabilities up to a given value and provide a unified framework for both discrete and continuous random variables.
permalink: /probability/random-variables/cumulative-distribution-function/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_random_variables_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/random-variables/cumulative-distribution-function/",
    label: "Cumulative Distribution Function (CDF)",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 3</span>
      <span class="badge">Random Variables</span>
      <span class="badge">Distributions</span>
    </div>

    <h1>Cumulative Distribution Function (CDF)</h1>

    <p class="lead">
      Probability mass functions and probability density functions describe probabilities differently.
    </p>

    <p class="lead">
      The cumulative distribution function provides a single framework that works for both discrete and continuous random variables.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/random-variables/continuous-random-variables/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/random-variables/expectation/">
         Next: Expectation →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why We Need the CDF</h2>

    <p>
      We have already seen two types of random variables:
    </p>

    <ul class="bullets">

      <li>Discrete random variables</li>

      <li>Continuous random variables</li>

    </ul>

    <p>
      Discrete variables use probability mass functions.
    </p>

    <p>
      Continuous variables use probability density functions.
    </p>

    <p>
      The cumulative distribution function provides a common language for both.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        A cumulative distribution function gives the probability that a random variable is less than or equal to a specified value.
      </p>

    </div>

    <h2>The Definition of a CDF</h2>

    <p>
      The cumulative distribution function of a random variable X is defined as:
    </p>

    0

    <p>
      This formula represents the probability that X takes a value less than or equal to x.
    </p>

    <h2>Understanding the Word "Cumulative"</h2>

    <p>
      The term cumulative means that probabilities accumulate as we move from left to right along the number line.
    </p>

    <p>
      Every value less than or equal to x contributes to the total probability.
    </p>

    <div class="example-box">

      <p>
        Instead of focusing on a single value,
        the CDF considers all values up to that point.
      </p>

    </div>

    <h2>A Discrete Example</h2>

    <p>
      Suppose a fair die is rolled.
    </p>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = Number shown on the die
      </p>

    </div>

    <p>
      What is:
    </p>

    <div class="example-box">

      <p>
        F(3)
      </p>

    </div>

    <p>
      By definition:
    </p>

    1

    <p>
      The values satisfying this condition are:
    </p>

    <div class="example-box">

      <p>
        1, 2, 3
      </p>

    </div>

    <p>
      Therefore:
    </p>

    2

    <h2>A Continuous Example</h2>

    <p>
      Suppose X represents height.
    </p>

    <p>
      Then:
    </p>

    <div class="example-box">

      <p>
        F(170)
      </p>

    </div>

    <p>
      represents:
    </p>

    <div class="example-box">

      <p>
        Probability that height is 170 cm or less.
      </p>

    </div>

    <p>
      For continuous variables,
      the CDF corresponds to accumulated area under the density curve.
    </p>

    <h2>The CDF and Area Under the Curve</h2>

    <p>
      For continuous random variables:
    </p>

    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        The CDF at x equals the area under the PDF to the left of x.
      </p>

    </div>

    <p>
      As more area is accumulated,
      the CDF increases.
    </p>

    <h2>Properties of Every CDF</h2>

    <p>
      Regardless of the type of random variable,
      all cumulative distribution functions satisfy several important properties.
    </p>

    <h3>Property 1: Values Are Between 0 and 1</h3>

    3

    <p>
      Since probabilities range from 0 to 1,
      the CDF must also remain within these bounds.
    </p>

    <h3>Property 2: The CDF Never Decreases</h3>

    <p>
      As x increases,
      additional probability may be accumulated.
    </p>

    <p>
      Probability cannot be lost.
    </p>

    <p>
      Therefore,
      the CDF is always nondecreasing.
    </p>

    <h3>Property 3: The CDF Approaches One</h3>

    <p>
      Eventually all possible outcomes are included.
    </p>

    <p>
      Therefore:
    </p>

    <div class="example-box">

      <p>
        Far to the right:
        F(x) → 1
      </p>

    </div>

    <h3>Property 4: The CDF Approaches Zero</h3>

    <p>
      Far to the left,
      no outcomes have yet been accumulated.
    </p>

    <div class="example-box">

      <p>
        Far to the left:
        F(x) → 0
      </p>

    </div>

    <h2>What a CDF Graph Looks Like</h2>

    <p>
      A cumulative distribution function begins near zero and gradually increases toward one.
    </p>

    <p>
      It never moves downward.
    </p>

    <p>
      The exact shape depends on the underlying distribution.
    </p>

    <h2>Discrete CDFs</h2>

    <p>
      For discrete variables,
      the CDF appears as a staircase.
    </p>

    <p>
      Each jump corresponds to probability assigned to a particular value.
    </p>

    <div class="example-box">

      <p>
        Probability accumulates in steps.
      </p>

    </div>

    <h2>Continuous CDFs</h2>

    <p>
      For continuous variables,
      the CDF is usually smooth.
    </p>

    <p>
      Probability accumulates continuously as x increases.
    </p>

    <div class="example-box">

      <p>
        Probability accumulates gradually.
      </p>

    </div>

    <h2>Finding Probabilities Using the CDF</h2>

    <p>
      One major advantage of the CDF is that interval probabilities can be computed easily.
    </p>

    <p>
      For any two values a and b:
    </p>

    4

    <p>
      This formula works for many probability calculations.
    </p>

    <h2>An Example of an Interval Probability</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        F(10) = 0.80
      </p>

      <p>
        F(5) = 0.35
      </p>

    </div>

    <p>
      Then:
    </p>

    5

    <p>
      The probability that X falls between 5 and 10 is 0.45.
    </p>

    <h2>Why the CDF Is Important</h2>

    <p>
      The cumulative distribution function is one of the most fundamental objects in probability.
    </p>

    <p>
      In fact,
      a probability distribution can be completely described by its CDF.
    </p>

    <p>
      Knowing the CDF means knowing the entire distribution.
    </p>

    <h2>Applications of CDFs</h2>

    <ul class="bullets">

      <li>Probability calculations</li>

      <li>Percentiles</li>

      <li>Risk analysis</li>

      <li>Statistical inference</li>

      <li>Reliability engineering</li>

      <li>Machine learning</li>

    </ul>

    <p>
      CDFs appear throughout modern statistics and data science.
    </p>

    <h2>The Bridge to Expectation</h2>

    <p>
      So far,
      we have focused on describing probabilities and distributions.
    </p>

    <p>
      Another important question is:
    </p>

    <div class="example-box">

      <p>
        What value should we expect to observe on average?
      </p>

    </div>

    <p>
      This question leads to one of the most important concepts in probability:
      expectation.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The next lesson introduces expectation,
      often called the expected value or mean of a random variable.
    </p>

    <p>
      Expectation summarizes the center of a probability distribution and plays a central role throughout probability and statistics.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The cumulative distribution function is defined as F(x) = P(X ≤ x)</li>

        <li>The CDF accumulates probability from left to right</li>

        <li>The CDF works for both discrete and continuous random variables</li>

        <li>For continuous variables, the CDF represents accumulated area under the PDF</li>

        <li>Every CDF is nondecreasing and ranges from 0 to 1</li>

        <li>Interval probabilities can be found using differences of CDF values</li>

        <li>A probability distribution is completely determined by its CDF</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/random-variables/continuous-random-variables/">
         ← Previous: Continuous Random Variables
      </a>

      <a class="btn"
         href="/probability/random-variables/expectation/">
         Next: Expectation →
      </a>

    </div>

  </div>

</section>