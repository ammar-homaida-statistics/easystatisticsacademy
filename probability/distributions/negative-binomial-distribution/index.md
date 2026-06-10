---
layout: default
title: Negative Binomial Distribution
description: Learn how the negative binomial distribution models the number of trials required to achieve a specified number of successes.
permalink: /probability/distributions/negative-binomial-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/negative-binomial-distribution/",
    label: "Negative Binomial Distribution",
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
      <span class="badge">Waiting Times</span>
    </div>

    <h1>Negative Binomial Distribution</h1>

    <p class="lead">
      The geometric distribution models the waiting time until the first success.
    </p>

    <p class="lead">
      The negative binomial distribution generalizes this idea by modeling the waiting time until a specified number of successes occurs.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/geometric-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/poisson-distribution/">
         Next: Poisson Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Negative Binomial Distribution?</h2>

    <p>
      A negative binomial distribution describes the number of trials required to obtain a fixed number of successes in independent Bernoulli trials.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A negative binomial random variable counts how many trials are needed to achieve r successes.
      </p>

    </div>

    <h2>The Main Question</h2>

    <p>
      Instead of asking:
    </p>

    <div class="example-box">

      <p>
        How long until the first success?
      </p>

    </div>

    <p>
      we ask:
    </p>

    <div class="example-box">

      <p>
        How long until the fifth success?
      </p>

      <p>
        How many customers until the third purchase?
      </p>

      <p>
        How many inspections until the tenth defect?
      </p>

    </div>

    <p>
      These are negative binomial questions.
    </p>

    <h2>Conditions for a Negative Binomial Model</h2>

    <p>
      A negative binomial distribution applies when:
    </p>

    <ul class="bullets">

      <li>Trials are independent.</li>

      <li>Each trial has two outcomes.</li>

      <li>The success probability remains constant.</li>

      <li>We continue until r successes occur.</li>

    </ul>

    <h2>Notation</h2>

    <p>
      A negative binomial random variable is commonly written as:
    </p>

    0

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>r = required number of successes</li>

      <li>p = probability of success</li>

    </ul>

    <h2>Possible Values</h2>

    <p>
      At least r trials are needed to obtain r successes.
    </p>

    <p>
      Therefore:
    </p>

    1

    <p>
      are the possible values of X.
    </p>

    <h2>The Probability Formula</h2>

    <p>
      The probability that the r-th success occurs on trial k is:
    </p>

    2

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>k ≥ r</li>

      <li>The final trial must be a success.</li>

      <li>The previous k−1 trials contain exactly r−1 successes.</li>

    </ul>

    <h2>Understanding the Formula</h2>

    <p>
      To have the r-th success occur on trial k:
    </p>

    <div class="example-box">

      <p>
        Trial k must be a success.
      </p>

      <p>
        The first k−1 trials must contain exactly r−1 successes.
      </p>

    </div>

    <p>
      The combination term counts all possible arrangements of those earlier successes.
    </p>

    <h2>Relationship to the Geometric Distribution</h2>

    <p>
      The geometric distribution is actually a special case of the negative binomial distribution.
    </p>

    <p>
      When:
    </p>

    3

    <p>
      the negative binomial formula reduces to the geometric distribution.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        The geometric distribution is the negative binomial distribution with one required success.
      </p>

    </div>

    <h2>Example: Waiting for Three Heads</h2>

    <p>
      Suppose a fair coin is tossed repeatedly.
    </p>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = Trial on which the third head appears
      </p>

    </div>

    <p>
      Then:
    </p>

    <div class="example-box">

      <p>
        r = 3
      </p>

      <p>
        p = 0.5
      </p>

    </div>

    <p>
      X follows a negative binomial distribution.
    </p>

    <p>
      It models the waiting time until three heads have occurred.
    </p>

    <h2>The Mean</h2>

    <p>
      The expected value is:
    </p>

    4

    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        The average number of trials required grows with the number of required successes and decreases as success becomes more likely.
      </p>

    </div>

    <h2>Example of the Mean</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        r = 5
      </p>

      <p>
        p = 0.25
      </p>

    </div>

    <p>
      Then:
    </p>

    5

    <p>
      On average,
      twenty trials are needed to obtain five successes.
    </p>

    <h2>The Variance</h2>

    <p>
      The variance is:
    </p>

    6

    <p>
      Variability increases when successes become rarer.
    </p>

    <h2>Comparing Geometric and Negative Binomial</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Distribution</th>
            <th>Models</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Geometric</td>
            <td>Waiting time for first success</td>
          </tr>

          <tr>
            <td>Negative Binomial</td>
            <td>Waiting time for r successes</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Why It Is Called "Negative Binomial"</h2>

    <p>
      The name originates from an algebraic expansion involving negative exponents.
    </p>

    <p>
      Historically,
      this distribution emerged from the negative binomial series in mathematics.
    </p>

    <p>
      The term does not imply negative probabilities or negative counts.
    </p>

    <h2>Applications in Practice</h2>

    <ul class="bullets">

      <li>Calls required before multiple sales occur</li>

      <li>Patients screened before several positive cases are found</li>

      <li>Network transmissions until several successful packets are received</li>

      <li>Production inspections until multiple defects are observed</li>

      <li>Sports attempts required before multiple successful outcomes</li>

    </ul>

    <p>
      The distribution is useful whenever repeated successes are the focus.
    </p>

    <h2>Connection to Counting Processes</h2>

    <p>
      Binomial distributions count successes within a fixed number of trials.
    </p>

    <p>
      Negative binomial distributions reverse the perspective.
    </p>

    <div class="example-box">

      <p>
        Binomial:
        Fixed trials → Count successes
      </p>

      <p>
        Negative Binomial:
        Fixed successes → Count trials
      </p>

    </div>

    <p>
      These distributions are closely related but answer different questions.
    </p>

    <h2>The Shape of the Distribution</h2>

    <p>
      Negative binomial distributions are generally right-skewed.
    </p>

    <p>
      Most waiting times are relatively short,
      but occasionally much longer waiting times occur.
    </p>

    <p>
      The skewness becomes more pronounced when success probabilities are small.
    </p>

    <h2>The Limitation</h2>

    <p>
      Bernoulli,
      binomial,
      geometric,
      and negative binomial distributions all arise from repeated success-or-failure trials.
    </p>

    <p>
      Many real-world events do not naturally fit that framework.
    </p>

    <div class="example-box">

      <p>
        Number of emails received today
      </p>

      <p>
        Number of accidents this week
      </p>

      <p>
        Number of website visits this hour
      </p>

    </div>

    <p>
      These counts are often modeled using the Poisson distribution.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The Poisson distribution is one of the most important distributions in statistics.
    </p>

    <p>
      It models counts of events occurring over time, space, or other continuous domains and is widely used in science, engineering, business, and data analytics.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The negative binomial distribution models waiting time until r successes occur</li>

        <li>It generalizes the geometric distribution</li>

        <li>The geometric distribution is the special case r = 1</li>

        <li>The mean equals r/p</li>

        <li>The variance equals r(1 − p)/p²</li>

        <li>It arises from repeated independent Bernoulli trials</li>

        <li>It is useful for multi-success waiting-time problems</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/geometric-distribution/">
         ← Previous: Geometric Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/poisson-distribution/">
         Next: Poisson Distribution →
      </a>

    </div>

  </div>

</section>