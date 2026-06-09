---
layout: default
title: Probability Axioms and Basic Rules
description: Learn the fundamental axioms of probability and the basic rules that every probability calculation must follow.
permalink: /probability/basics/probability-axioms-and-basic-rules/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_basics_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/basics/probability-axioms-and-basic-rules/",
    label: "Probability Axioms and Basic Rules",
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
      <span class="badge">Core Rules</span>
    </div>

    <h1>Probability Axioms and Basic Rules</h1>

    <p class="lead">
      Every probability calculation is built on a small set of fundamental principles.
    </p>

    <p class="lead">
      These principles, called probability axioms, define what probability is and establish the rules that all valid probability models must obey.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/basics/outcomes-sample-spaces-events/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/basics/union-intersection-and-venn-thinking/">
         Next: Union, Intersection, and Venn Thinking →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>Why Do We Need Rules?</h2>

    <p>
      Probability is not just intuition.
    </p>

    <p>
      It is a mathematical system governed by precise rules.
    </p>

    <p>
      Without these rules,
      probability calculations could become inconsistent or contradictory.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The probability axioms define the foundation upon which all probability theory is built.
      </p>

    </div>

    <h2>The Three Probability Axioms</h2>

    <p>
      Modern probability theory is based on three fundamental axioms introduced by the mathematician
      0.
    </p>

    <p>
      Every valid probability model must satisfy these axioms.
    </p>

    <h2>Axiom 1: Probabilities Cannot Be Negative</h2>

    <p>
      The probability of any event must be greater than or equal to zero.
    </p>

    1

    <p>
      Negative probabilities are not meaningful.
    </p>

    <div class="example-box">

      <p>
        Valid: 0.25
      </p>

      <p>
        Valid: 0.80
      </p>

      <p>
        Invalid: -0.15
      </p>

    </div>

    <h2>Axiom 2: The Sample Space Has Probability 1</h2>

    <p>
      The probability that some outcome from the sample space occurs is always 1.
    </p>

    2

    <p>
      Since the sample space contains all possible outcomes,
      something in the sample space must occur.
    </p>

    <div class="example-box">

      <p>
        Rolling a die:
      </p>

      <p>
        S = {1,2,3,4,5,6}
      </p>

      <p>
        P(S) = 1
      </p>

    </div>

    <h2>Axiom 3: Addition for Mutually Exclusive Events</h2>

    <p>
      If two events cannot occur at the same time,
      their probabilities add.
    </p>

    3

    <p>
      This rule applies only when the events are mutually exclusive.
    </p>

    <div class="example-box">

      <p>
        Rolling a die:
      </p>

      <p>
        A = rolling a 1
      </p>

      <p>
        B = rolling a 2
      </p>

    </div>

    <p>
      Since both outcomes cannot happen on the same roll,
      the probabilities can be added directly.
    </p>

    <h2>What Is a Mutually Exclusive Event?</h2>

    <p>
      Two events are mutually exclusive if they cannot occur simultaneously.
    </p>

    <div class="example-box">

      <p>
        Rolling a die:
      </p>

      <p>
        Event A = {1}
      </p>

      <p>
        Event B = {2}
      </p>

    </div>

    <p>
      One roll cannot produce both outcomes,
      so the events are mutually exclusive.
    </p>

    <h2>The Probability Scale</h2>

    <p>
      The first two axioms imply an important rule.
    </p>

    <p>
      Every probability must lie between 0 and 1.
    </p>

    4

    <p>
      This rule applies to every event.
    </p>

    <h2>Impossible Events</h2>

    <p>
      An impossible event has probability zero.
    </p>

    <div class="example-box">

      <p>
        Rolling a 7 on a standard six-sided die.
      </p>
    </div>

    <p>
      Since the outcome cannot occur:
    </p>

    5

    <h2>Certain Events</h2>

    <p>
      A certain event has probability one.
    </p>

    <div class="example-box">

      <p>
        Rolling a number between 1 and 6 on a standard die.
      </p>
    </div>

    <p>
      Since this event must occur:
    </p>

    6

    <h2>Probabilities of All Outcomes Must Add to 1</h2>

    <p>
      For a complete sample space,
      the probabilities of all possible outcomes sum to 1.
    </p>

    <div class="example-box">

      <p>
        Fair die:
      </p>

      <p>
        1/6 + 1/6 + 1/6 + 1/6 + 1/6 + 1/6 = 1
      </p>

    </div>

    <p>
      This rule follows directly from the axioms.
    </p>

    <h2>Example: Fair Coin</h2>

    <p>
      Sample space:
    </p>

    <div class="example-box">

      <p>
        S = {H, T}
      </p>
    </div>

    <p>
      Since the coin is fair:
    </p>

    <div class="example-box">

      <p>
        P(H) = 0.5
      </p>

      <p>
        P(T) = 0.5
      </p>

    </div>

    <p>
      Notice:
    </p>

    7

    <h2>The Complement Rule</h2>

    <p>
      Every event has a complement.
    </p>

    <p>
      The complement consists of all outcomes not contained in the event.
    </p>

    <div class="example-box">

      <p>
        Event:
      </p>

      <p>
        Rolling an even number.
      </p>

      <p>
        Complement:
      </p>

      <p>
        Rolling an odd number.
      </p>

    </div>

    <p>
      Probabilities of an event and its complement must sum to 1.
    </p>

    8

    <h2>Complement Example</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        P(Rain) = 0.30
      </p>
    </div>

    <p>
      Then:
    </p>

    9

    <p>
      The probability of no rain is 0.70.
    </p>

    <h2>Why the Complement Rule Is Useful</h2>

    <p>
      Sometimes it is easier to calculate the complement than the event itself.
    </p>

    <p>
      This idea becomes especially important in later probability problems.
    </p>

    <h2>Checking Probability Calculations</h2>

    <p>
      The axioms provide a simple way to verify calculations.
    </p>

    <p>
      Ask:
    </p>

    <ul class="bullets">

      <li>Is every probability between 0 and 1?</li>

      <li>Do probabilities sum correctly?</li>

      <li>Does the sample space have probability 1?</li>

      <li>Does the complement rule hold?</li>

    </ul>

    <p>
      If not,
      something is wrong.
    </p>

    <h2>The Foundation of Everything Ahead</h2>

    <p>
      The probability axioms may seem simple,
      but nearly every probability formula comes from them.
    </p>

    <p>
      Conditional probability,
      Bayes' theorem,
      random variables,
      probability distributions,
      and statistical inference all rely on these foundational rules.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Events can be combined in different ways.
    </p>

    <p>
      We may want the probability that one event occurs,
      another event occurs,
      or both occur together.
    </p>

    <p>
      The next lesson introduces unions,
      intersections,
      and Venn diagrams,
      which provide a visual framework for reasoning about events.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Probability theory is built on three fundamental axioms</li>

        <li>Probabilities can never be negative</li>

        <li>The sample space always has probability 1</li>

        <li>Mutually exclusive event probabilities can be added</li>

        <li>Every probability lies between 0 and 1</li>

        <li>The complement rule states that P(Aᶜ) = 1 − P(A)</li>

        <li>All later probability concepts are built upon these basic rules</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/basics/outcomes-sample-spaces-events/">
         ← Previous: Outcomes, Sample Spaces, and Events
      </a>

      <a class="btn"
         href="/probability/basics/union-intersection-and-venn-thinking/">
         Next: Union, Intersection, and Venn Thinking →
      </a>

    </div>

  </div>

</section>