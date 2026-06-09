---
layout: default
title: Continuous Random Variables
description: Learn how continuous random variables differ from discrete variables and why probabilities are represented using areas rather than individual values.
permalink: /probability/random-variables/continuous-random-variables/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_random_variables_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/random-variables/continuous-random-variables/",
    label: "Continuous Random Variables",
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
      <span class="badge">Continuous Variables</span>
    </div>

    <h1>Continuous Random Variables</h1>

    <p class="lead">
      Many real-world quantities are measured rather than counted.
    </p>

    <p class="lead">
      Continuous random variables describe measurements that can take infinitely many possible values within a range.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/random-variables/discrete-random-variables/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/random-variables/cumulative-distribution-function/">
         Next: Cumulative Distribution Function →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Continuous Random Variable?</h2>

    <p>
      A continuous random variable can take any value within an interval or collection of intervals.
    </p>

    <p>
      Unlike discrete variables,
      the possible values cannot be listed individually because infinitely many values exist.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Continuous random variables represent measurements and can take infinitely many possible values.
      </p>

    </div>

    <h2>Examples of Continuous Random Variables</h2>

    <div class="example-box">

      <p>
        Height of a person
      </p>

      <p>
        Weight of a package
      </p>

      <p>
        Temperature
      </p>

      <p>
        Time required to complete a task
      </p>

      <p>
        Amount of rainfall
      </p>

    </div>

    <p>
      Each of these variables can take values with arbitrary precision.
    </p>

    <h2>Why Continuous Variables Are Different</h2>

    <p>
      Consider measuring a person's height.
    </p>

    <p>
      Possible values include:
    </p>

    <div class="example-box">

      <p>
        170 cm
      </p>

      <p>
        170.1 cm
      </p>

      <p>
        170.12 cm
      </p>

      <p>
        170.123 cm
      </p>

    </div>

    <p>
      No matter how precise a measurement becomes,
      additional values can always exist between two nearby numbers.
    </p>

    <p>
      This infinite divisibility is a defining characteristic of continuous variables.
    </p>

    <h2>Discrete Versus Continuous</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Discrete</th>
            <th>Continuous</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Counts</td>
            <td>Measurements</td>
          </tr>

          <tr>
            <td>Countable values</td>
            <td>Infinite values in intervals</td>
          </tr>

          <tr>
            <td>PMF used</td>
            <td>PDF used</td>
          </tr>

          <tr>
            <td>Individual values can have probability</td>
            <td>Individual values have probability zero</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Surprising Property</h2>

    <p>
      One of the most surprising ideas in probability is:
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        The probability of any single value of a continuous random variable is zero.
      </p>

    </div>

    <p>
      For example:
    </p>

    0

    <p>
      even though 170 cm is a possible height.
    </p>

    <h2>Why Is the Probability Zero?</h2>

    <p>
      A continuous variable has infinitely many possible values.
    </p>

    <p>
      Probability must be spread across the entire continuum.
    </p>

    <p>
      As a result,
      no single point receives positive probability.
    </p>

    <p>
      Probability is assigned to intervals rather than individual values.
    </p>

    <h2>Probabilities Are About Ranges</h2>

    <p>
      Instead of asking:
    </p>

    <div class="example-box">

      <p>
        What is the probability that height equals exactly 170 cm?
      </p>

    </div>

    <p>
      we ask:
    </p>

    <div class="example-box">

      <p>
        What is the probability that height lies between 165 cm and 175 cm?
      </p>

    </div>

    <p>
      Continuous probability focuses on intervals.
    </p>

    <h2>Probability Density Functions (PDFs)</h2>

    <p>
      Continuous random variables use a probability density function rather than a probability mass function.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A probability density function describes how probability is distributed across the values of a continuous random variable.
      </p>

    </div>

    <h2>Density Is Not Probability</h2>

    <p>
      A common misconception is that the value of a density function is itself a probability.
    </p>

    <p>
      This is incorrect.
    </p>

    <p>
      Density indicates how concentrated probability is around a location.
    </p>

    <p>
      Actual probabilities are obtained from areas under the density curve.
    </p>

    <h2>The Area Interpretation</h2>

    <p>
      For continuous variables:
    </p>

    <div class="concept-box">

      <strong>Core principle:</strong>

      <p>
        Probability equals area under the density curve.
      </p>

    </div>

    <p>
      This interpretation is central to continuous probability theory.
    </p>

    <h2>Total Probability Equals One</h2>

    <p>
      Just as PMFs must sum to one,
      PDFs must satisfy an equivalent condition.
    </p>

    <p>
      The total area under the density curve must equal one.
    </p>

    <div class="example-box">

      <p>
        Entire area under the PDF = 1
      </p>

    </div>

    <p>
      This ensures that some value of the random variable must occur.
    </p>

    <h2>Probability Between Two Values</h2>

    <p>
      For continuous variables,
      probabilities are calculated over intervals.
    </p>

    <p>
      For example:
    </p>

    <div class="example-box">

      <p>
        Probability that height lies between 165 cm and 175 cm
      </p>

    </div>

    <p>
      corresponds to the area under the density curve between those values.
    </p>

    <h2>Continuous Variables in Practice</h2>

    <p>
      Many scientific and engineering measurements are modeled as continuous variables.
    </p>

    <ul class="bullets">

      <li>Temperature</li>

      <li>Pressure</li>

      <li>Distance</li>

      <li>Time</li>

      <li>Speed</li>

      <li>Voltage</li>

    </ul>

    <p>
      Continuous models often provide accurate approximations even when measurements are recorded with finite precision.
    </p>

    <h2>The Normal Distribution Example</h2>

    <p>
      One of the most famous continuous distributions is the normal distribution.
    </p>

    <p>
      It produces the familiar bell-shaped curve.
    </p>

    <p>
      Many naturally occurring measurements are approximately normal.
    </p>

    <p>
      Later lessons will examine this distribution in detail.
    </p>

    <h2>Continuous Variables and Data Science</h2>

    <p>
      Continuous random variables appear throughout data science and analytics.
    </p>

    <div class="example-box">

      <p>
        Customer spending
      </p>

      <p>
        Response times
      </p>

      <p>
        Sensor measurements
      </p>

      <p>
        Financial returns
      </p>

    </div>

    <p>
      Continuous probability models help describe uncertainty in these measurements.
    </p>

    <h2>A Different Probability Mindset</h2>

    <p>
      Discrete probability focuses on individual outcomes.
    </p>

    <p>
      Continuous probability focuses on intervals and areas.
    </p>

    <p>
      This conceptual shift is one of the most important transitions in probability theory.
    </p>

    <h2>Connecting Discrete and Continuous Variables</h2>

    <p>
      Both discrete and continuous random variables describe uncertainty.
    </p>

    <p>
      The difference lies in the set of possible values and the way probabilities are represented.
    </p>

    <p>
      Understanding both types is essential before studying probability distributions more deeply.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      We now understand the two major categories of random variables.
    </p>

    <p>
      The next lesson introduces the cumulative distribution function (CDF),
      a tool that applies to both discrete and continuous random variables and provides a unified way to describe probabilities.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Continuous random variables represent measurements</li>

        <li>They can take infinitely many values within intervals</li>

        <li>Individual values have probability zero</li>

        <li>Probabilities are assigned to ranges of values</li>

        <li>Continuous variables use probability density functions (PDFs)</li>

        <li>Probability corresponds to area under a density curve</li>

        <li>The total area under a PDF equals one</li>

        <li>Continuous models are widely used in science, engineering, and data science</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/random-variables/discrete-random-variables/">
         ← Previous: Discrete Random Variables
      </a>

      <a class="btn"
         href="/probability/random-variables/cumulative-distribution-function/">
         Next: Cumulative Distribution Function →
      </a>

    </div>

  </div>

</section>