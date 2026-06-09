---
layout: default
title: Outcomes, Sample Spaces, and Events
description: Learn the fundamental building blocks of probability: outcomes, sample spaces, and events.
permalink: /probability/basics/outcomes-sample-spaces-events/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_basics_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/basics/outcomes-sample-spaces-events/",
    label: "Outcomes, Sample Spaces, and Events",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 1</span>
      <span class="badge">Basics</span>
      <span class="badge">Foundations</span>
    </div>

    <h1>Outcomes, Sample Spaces, and Events</h1>

    <p class="lead">
      Probability begins by identifying what can happen.
    </p>

    <p class="lead">
      Before assigning probabilities, we must define the possible outcomes of an experiment, organize them into a sample space, and specify the events we are interested in studying.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/basics/what-is-probability/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/basics/probability-axioms-and-basic-rules/">
         Next: Probability Axioms and Basic Rules →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>Why We Need Structure</h2>

    <p>
      Probability studies uncertainty,
      but uncertainty must be described precisely.
    </p>

    <p>
      To calculate probabilities,
      we first need to identify what outcomes are possible.
    </p>

    <p>
      This leads to three foundational concepts:
    </p>

    <ul class="bullets">

      <li>Outcomes</li>

      <li>Sample Spaces</li>

      <li>Events</li>

    </ul>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Every probability problem begins by defining possible outcomes and the events of interest.
      </p>

    </div>

    <h2>What Is an Outcome?</h2>

    <p>
      An <strong>outcome</strong> is a single possible result of a random experiment.
    </p>

    <p>
      It represents one specific thing that could happen.
    </p>

    <div class="example-box">

      <strong>Rolling a die</strong>

      <p>
        Possible outcomes:
      </p>

      <p>
        1, 2, 3, 4, 5, 6
      </p>

    </div>

    <p>
      Each number is an individual outcome.
    </p>

    <h2>Examples of Outcomes</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Experiment</th>
            <th>Example Outcome</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Coin toss</td>
            <td>Heads</td>
          </tr>

          <tr>
            <td>Rolling a die</td>
            <td>4</td>
          </tr>

          <tr>
            <td>Drawing a card</td>
            <td>Ace of Spades</td>
          </tr>

          <tr>
            <td>Weather tomorrow</td>
            <td>Rain</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Outcomes are the smallest units considered in probability models.
    </p>

    <h2>What Is a Sample Space?</h2>

    <p>
      The <strong>sample space</strong> is the set of all possible outcomes of an experiment.
    </p>

    <p>
      It contains every outcome that could occur.
    </p>

    <p>
      Sample spaces are commonly denoted by the symbol:
    </p>

    <div class="example-box">

      <p>
        S
      </p>
    </div>

    <h2>Sample Space for a Coin Toss</h2>

    <p>
      Consider a single coin toss.
    </p>

    <p>
      The possible outcomes are:
    </p>

    <div class="example-box">

      <p>
        S = {Heads, Tails}
      </p>
    </div>

    <p>
      Since every possible result is included,
      this is the complete sample space.
    </p>

    <h2>Sample Space for a Die Roll</h2>

    <p>
      For a six-sided die:
    </p>

    <div class="example-box">

      <p>
        S = {1, 2, 3, 4, 5, 6}
      </p>
    </div>

    <p>
      Every possible outcome appears exactly once in the sample space.
    </p>

    <h2>The Sample Space Must Be Complete</h2>

    <p>
      A sample space should include every possible outcome.
    </p>

    <p>
      Missing outcomes lead to incorrect probability calculations.
    </p>

    <div class="example-box">

      <p>
        Incorrect:
      </p>

      <p>
        S = {1, 2, 3, 4, 5}
      </p>
    </div>

    <p>
      The outcome 6 has been omitted,
      so this is not a valid sample space for a die roll.
    </p>

    <h2>What Is an Event?</h2>

    <p>
      An <strong>event</strong> is a collection of one or more outcomes from the sample space.
    </p>

    <p>
      Events represent situations we are interested in studying.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Outcomes are individual results. Events are groups of outcomes.
      </p>

    </div>

    <h2>Example: Rolling an Even Number</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        S = {1, 2, 3, 4, 5, 6}
      </p>
    </div>

    <p>
      The event:
    </p>

    <div class="example-box">

      <p>
        E = {2, 4, 6}
      </p>
    </div>

    <p>
      represents rolling an even number.
    </p>

    <p>
      The event contains multiple outcomes.
    </p>

    <h2>Example: Rolling a Number Greater Than 4</h2>

    <div class="example-box">

      <p>
        E = {5, 6}
      </p>
    </div>

    <p>
      This event occurs whenever either outcome 5 or outcome 6 is observed.
    </p>

    <h2>Simple Events and Compound Events</h2>

    <p>
      Events can contain one outcome or many outcomes.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Type</th>
            <th>Example</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Simple Event</td>
            <td>{3}</td>
          </tr>

          <tr>
            <td>Compound Event</td>
            <td>{2, 4, 6}</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      A simple event contains one outcome.
    </p>

    <p>
      A compound event contains multiple outcomes.
    </p>

    <h2>The Relationship Between Outcomes and Events</h2>

    <p>
      Outcomes are the building blocks of events.
    </p>

    <p>
      Every event is made up of outcomes from the sample space.
    </p>

    <div class="example-box">

      <p>
        Sample Space:
      </p>

      <p>
        S = {1, 2, 3, 4, 5, 6}
      </p>

      <p>
        Event:
      </p>

      <p>
        E = {1, 3, 5}
      </p>

    </div>

    <p>
      The event is simply a subset of the sample space.
    </p>

    <h2>Events as Sets</h2>

    <p>
      Probability uses ideas from set theory.
    </p>

    <p>
      Sample spaces and events are often treated as sets.
    </p>

    <p>
      This approach allows us to apply mathematical operations to events.
    </p>

    <p>
      Later lessons will explore unions,
      intersections,
      and complements of events.
    </p>

    <h2>The Certain Event</h2>

    <p>
      An event containing every outcome in the sample space is called the certain event.
    </p>

    <div class="example-box">

      <p>
        S = {1, 2, 3, 4, 5, 6}
      </p>

    </div>

    <p>
      Since one of these outcomes must occur,
      the probability of the sample space is always 1.
    </p>

    <h2>The Impossible Event</h2>

    <p>
      The impossible event contains no outcomes.
    </p>

    <p>
      It is called the empty set.
    </p>

    <div class="example-box">

      <p>
        ∅
      </p>
    </div>

    <p>
      The probability of the impossible event is always 0.
    </p>

    <h2>A Complete Example</h2>

    <p>
      Consider rolling a die.
    </p>

    <div class="example-box">

      <p>
        Sample Space:
      </p>

      <p>
        S = {1, 2, 3, 4, 5, 6}
      </p>

      <p>
        Event A:
      </p>

      <p>
        A = {2, 4, 6}
      </p>

      <p>
        Event B:
      </p>

      <p>
        B = {5, 6}
      </p>

    </div>

    <p>
      Here:
    </p>

    <ul class="bullets">

      <li>The sample space contains all outcomes</li>

      <li>Event A represents even numbers</li>

      <li>Event B represents numbers greater than 4</li>

    </ul>

    <p>
      This structure forms the basis of probability calculations.
    </p>

    <h2>Why These Concepts Matter</h2>

    <p>
      Every probability problem begins with:
    </p>

    <ol>

      <li>Defining the experiment</li>

      <li>Identifying outcomes</li>

      <li>Constructing the sample space</li>

      <li>Defining events of interest</li>

    </ol>

    <p>
      Once these pieces are in place,
      probabilities can be assigned and analyzed.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Now that we understand outcomes,
      sample spaces,
      and events,
      we can begin assigning probabilities to them.
    </p>

    <p>
      The next lesson introduces the fundamental rules that every probability model must satisfy:
      the probability axioms and basic probability rules.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>An outcome is a single possible result of an experiment</li>

        <li>A sample space contains all possible outcomes</li>

        <li>An event is a collection of outcomes</li>

        <li>Events are subsets of the sample space</li>

        <li>Simple events contain one outcome</li>

        <li>Compound events contain multiple outcomes</li>

        <li>Probability calculations begin with outcomes, sample spaces, and events</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/basics/what-is-probability/">
         ← Previous: What Is Probability?
      </a>

      <a class="btn"
         href="/probability/basics/probability-axioms-and-basic-rules/">
         Next: Probability Axioms and Basic Rules →
      </a>

    </div>

  </div>

</section>