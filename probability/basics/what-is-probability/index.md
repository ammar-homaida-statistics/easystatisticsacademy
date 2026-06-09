---
layout: default
title: What Is Probability (and What It Is Not)?
description: Learn what probability measures, what uncertainty means, and common misconceptions about chance, randomness, and prediction.
permalink: /probability/basics/what-is-probability/
parent: /probability/basics/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  localStorage.setItem(
    "esa_continue_probability_basics_lesson_v0",
    JSON.stringify({
      url: "/probability/basics/what-is-probability/",
      label: "What Is Probability (and What It Is Not)?",
      ts: Date.now()
    })
  );

})();
</script>

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 1</span>
      <span class="badge">Lesson 1</span>
    </div>

    <h1>What Is Probability (and What It Is Not)?</h1>

    <p class="lead">
      Probability is the mathematical language of uncertainty.
      It provides a way to describe how likely events are before we know what will happen.
    </p>

    <div class="hero-actions">

      <a class="btn btn-outline"
         href="/probability/basics/">
         Back to Block
      </a>

      <a class="btn"
         href="/probability/basics/outcomes-sample-spaces-events/">
         Next Lesson
      </a>

    </div>

  </div>

</section>

<section class="section">

  <div class="section-head">

    <h2>Learning goals</h2>

  </div>

  <ul class="bullets">

    <li>Understand what probability measures</li>

    <li>Interpret probabilities correctly</li>

    <li>Distinguish uncertainty from certainty</li>

    <li>Recognize common misconceptions about randomness</li>

    <li>Prepare for sample spaces and events</li>

  </ul>

</section>

<section class="section">

  <h2>Why probability exists</h2>

  <p>
    Many situations involve uncertainty.
    Before a coin is flipped, a card is drawn, a patient receives a test result,
    or tomorrow's weather arrives, we do not know the outcome.
  </p>

  <p>
    Probability provides a systematic way to quantify that uncertainty.
    Instead of saying an event is simply "possible" or "impossible,"
    probability tells us how likely it is.
  </p>

  <div class="callout">

    <div class="callout-copy">

      <strong>Key idea</strong>

      <p>
        Probability measures uncertainty before the outcome is known.
      </p>

    </div>

  </div>

</section>

<section class="section">

  <h2>What probability means</h2>

  <p>
    A probability is a number between 0 and 1.
  </p>

  <div class="table-wrap">

    <table>

      <thead>
        <tr>
          <th>Probability</th>
          <th>Interpretation</th>
        </tr>
      </thead>

      <tbody>

        <tr>
          <td>0</td>
          <td>Impossible event</td>
        </tr>

        <tr>
          <td>0.25</td>
          <td>Occurs about 25% of the time in repeated situations</td>
        </tr>

        <tr>
          <td>0.50</td>
          <td>Equally likely to occur or not occur</td>
        </tr>

        <tr>
          <td>0.90</td>
          <td>Very likely</td>
        </tr>

        <tr>
          <td>1</td>
          <td>Certain event</td>
        </tr>

      </tbody>

    </table>

  </div>

</section>

<section class="section">

  <h2>Probability is not prediction</h2>

  <p>
    A common mistake is to think probability predicts exactly what will happen.
    It does not.
  </p>

  <p>
    If a fair coin has probability 0.5 of landing heads,
    that does not mean every second flip will be heads.
    It means that over many flips, about half are expected to be heads.
  </p>

  <div class="callout">

    <div class="callout-copy">

      <strong>Important</strong>

      <p>
        Probability describes long-run behavior, not guaranteed outcomes.
      </p>

    </div>

  </div>

</section>

<section class="section">

  <h2>Probability and randomness</h2>

  <p>
    Randomness does not mean chaos.
    A random process can still have predictable probabilities.
  </p>

  <p>
    For example:
  </p>

  <ul class="bullets">

    <li>The next coin flip is uncertain.</li>

    <li>The probability of heads is known.</li>

    <li>The exact outcome is random.</li>

    <li>The long-run pattern is predictable.</li>

  </ul>

  <p>
    Probability studies this balance between uncertainty and regularity.
  </p>

</section>

<section class="section">

  <h2>Three common interpretations of probability</h2>

  <div class="table-wrap">

    <table>

      <thead>

        <tr>
          <th>Interpretation</th>
          <th>Main idea</th>
        </tr>

      </thead>

      <tbody>

        <tr>
          <td>Classical</td>
          <td>Based on equally likely outcomes</td>
        </tr>

        <tr>
          <td>Frequentist</td>
          <td>Based on long-run relative frequency</td>
        </tr>

        <tr>
          <td>Bayesian</td>
          <td>Based on degree of belief given evidence</td>
        </tr>

      </tbody>

    </table>

  </div>

  <p>
    Throughout this course, we will primarily use the frequentist framework
    while also introducing Bayesian ideas later.
  </p>

</section>

<section class="section">

  <h2>Common misconceptions</h2>

  <div class="grid grid-2">

    <div class="card">

      <h3>Misconception 1</h3>

      <p>
        "A 70% chance means the event will happen."
      </p>

      <p>
        Incorrect. A 70% probability still allows the event to fail.
      </p>

    </div>

    <div class="card">

      <h3>Misconception 2</h3>

      <p>
        "Random means unpredictable forever."
      </p>

      <p>
        Individual outcomes are unpredictable, but long-run patterns are not.
      </p>

    </div>

    <div class="card">

      <h3>Misconception 3</h3>

      <p>
        "Probability tells us exactly what will happen next."
      </p>

      <p>
        Probability describes likelihood, not certainty.
      </p>

    </div>

    <div class="card">

      <h3>Misconception 4</h3>

      <p>
        "After several heads, tails becomes due."
      </p>

      <p>
        This is the gambler's fallacy. Past independent outcomes do not force future outcomes.
      </p>

    </div>

  </div>

</section>

<section class="section">

  <h2>Example</h2>

  <div class="callout">

    <div class="callout-copy">

      <p>
        A weather forecast says there is a 30% chance of rain tomorrow.
      </p>

      <p>
        This does not mean it will rain for 30% of the day.
        It means that under similar conditions,
        rain occurs about 30% of the time.
      </p>

    </div>

  </div>

</section>

<section class="section">

  <h2>Key takeaways</h2>

  <ul class="bullets">

    <li>Probability quantifies uncertainty.</li>

    <li>Probabilities range from 0 to 1.</li>

    <li>Probability does not guarantee outcomes.</li>

    <li>Randomness can still produce predictable long-run patterns.</li>

    <li>Probability is the foundation of all later statistical inference.</li>

  </ul>

</section>

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline"
       href="/probability/basics/">
       ← Back to Block 1
    </a>

    <a class="btn"
       href="/probability/basics/outcomes-sample-spaces-events/">
       Next Lesson →
    </a>

  </div>

</section>