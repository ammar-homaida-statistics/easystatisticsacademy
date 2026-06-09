---
layout: default
title: Multiplication Rule
description: Learn how to calculate the probability that multiple events occur together using the multiplication rule.
permalink: /probability/conditional/multiplication-rule/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_conditional_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/conditional/multiplication-rule/",
    label: "Multiplication Rule",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 2</span>
      <span class="badge">Conditional Probability</span>
      <span class="badge">Core Rule</span>
    </div>

    <h1>Multiplication Rule</h1>

    <p class="lead">
      Conditional probability allows us to calculate the probability of events occurring together.
    </p>

    <p class="lead">
      The multiplication rule is one of the most important results in probability because it connects conditional probabilities with intersections of events.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/conditional/what-is-conditional-probability/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/conditional/law-of-total-probability/">
         Next: Law of Total Probability →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why We Need the Multiplication Rule</h2>

    <p>
      Many probability questions involve events occurring together.
    </p>

    <div class="example-box">

      <p>
        What is the probability of drawing two aces in a row?
      </p>

      <p>
        What is the probability that a student studies and passes?
      </p>

      <p>
        What is the probability that it rains and traffic is heavy?
      </p>

    </div>

    <p>
      These questions involve intersections of events.
    </p>

    <p>
      The multiplication rule provides a systematic way to calculate such probabilities.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The multiplication rule converts conditional probabilities into probabilities of joint events.
      </p>

    </div>

    <h2>Starting with Conditional Probability</h2>

    <p>
      Recall the definition of conditional probability.
    </p>

    0

    <p>
      This formula describes the probability of A given that B has occurred.
    </p>

    <h2>Rearranging the Formula</h2>

    <p>
      Multiplying both sides by P(B) gives:
    </p>

    1

    <p>
      This is the multiplication rule.
    </p>

    <p>
      It tells us how to calculate the probability that both A and B occur.
    </p>

    <h2>An Equivalent Version</h2>

    <p>
      Because the roles of A and B can be reversed,
      another equivalent form is:
    </p>

    2

    <p>
      Both forms are correct.
    </p>

    <p>
      The choice depends on which conditional probability is easier to determine.
    </p>

    <h2>Understanding the Logic</h2>

    <p>
      Think of the multiplication rule as a two-step process.
    </p>

    <ol>

      <li>Probability that Event B occurs.</li>

      <li>Probability that Event A occurs after B has occurred.</li>

    </ol>

    <p>
      Multiplying these probabilities gives the probability that both events occur.
    </p>

    <h2>Example: Drawing Two Aces</h2>

    <p>
      A standard deck contains 52 cards.
    </p>

    <p>
      Suppose two cards are drawn without replacement.
    </p>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        A = First card is an ace
      </p>

      <p>
        B = Second card is an ace
      </p>

    </div>

    <p>
      First:
    </p>

    3

    <p>
      After one ace has been removed:
    </p>

    4

    <p>
      Therefore:
    </p>

    5

    <p>
      The multiplication rule gives the probability of drawing two aces consecutively.
    </p>

    <h2>Independent Events</h2>

    <p>
      A particularly important special case occurs when events are independent.
    </p>

    <p>
      For independent events:
    </p>

    6

    <p>
      The occurrence of B does not affect A.
    </p>

    <h2>Multiplication Rule for Independent Events</h2>

    <p>
      Substituting independence into the multiplication rule gives:
    </p>

    7

    <p>
      This is the familiar independence formula introduced earlier.
    </p>

    <h2>Example: Two Coin Tosses</h2>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        A = First toss is heads
      </p>

      <p>
        B = Second toss is heads
      </p>

    </div>

    <p>
      Since coin tosses are independent:
    </p>

    <div class="example-box">

      <p>
        P(A) = 0.5
      </p>

      <p>
        P(B) = 0.5
      </p>

    </div>

    <p>
      Therefore:
    </p>

    8

    <h2>Dependent Events</h2>

    <p>
      Many real-world events are not independent.
    </p>

    <p>
      In these situations,
      the conditional probability must be used explicitly.
    </p>

    <div class="example-box">

      <p>
        Drawing cards without replacement
      </p>

      <p>
        Medical diagnoses
      </p>

      <p>
        Weather-related events
      </p>

    </div>

    <p>
      The occurrence of one event changes the probability of the other.
    </p>

    <h2>Example: Students and Passing</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        P(Study) = 0.60
      </p>

      <p>
        P(Pass | Study) = 0.90
      </p>

    </div>

    <p>
      Then:
    </p>

    9

    <p>
      The probability that a student studies and passes is 0.54.
    </p>

    <h2>Extending to Three Events</h2>

    <p>
      The multiplication rule can be extended beyond two events.
    </p>

    <p>
      For three events:
    </p>

    10

    <p>
      Each step conditions on the events that have already occurred.
    </p>

    <h2>A Sequential View</h2>

    <p>
      The multiplication rule is especially useful for processes that occur in stages.
    </p>

    <div class="example-box">

      <p>
        Draw a card.
      </p>

      <p>
        Draw another card.
      </p>

      <p>
        Draw a third card.
      </p>

    </div>

    <p>
      Each stage contributes another conditional probability.
    </p>

    <h2>A Tree Diagram Interpretation</h2>

    <p>
      Tree diagrams provide a visual representation of the multiplication rule.
    </p>

    <p>
      Each branch represents a conditional probability.
    </p>

    <p>
      Multiplying probabilities along a path gives the probability of the entire sequence.
    </p>

    <p>
      Tree diagrams will become important in later lessons.
    </p>

    <h2>A Useful Checklist</h2>

    <p>
      When applying the multiplication rule:
    </p>

    <ol>

      <li>Identify the events.</li>

      <li>Determine whether they are independent.</li>

      <li>Find any required conditional probabilities.</li>

      <li>Multiply the appropriate probabilities.</li>

    </ol>

    <p>
      This approach works for many probability problems.
    </p>

    <h2>Why the Multiplication Rule Matters</h2>

    <p>
      The multiplication rule appears throughout probability and statistics.
    </p>

    <ul class="bullets">

      <li>Conditional probability</li>

      <li>Bayes' theorem</li>

      <li>Tree diagrams</li>

      <li>Joint distributions</li>

      <li>Machine learning</li>

      <li>Statistical inference</li>

    </ul>

    <p>
      It is one of the central tools of probability theory.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The multiplication rule helps us calculate probabilities of events occurring together.
    </p>

    <p>
      Another important question is how to calculate probabilities when several different pathways can lead to the same outcome.
    </p>

    <p>
      The next lesson introduces the Law of Total Probability,
      which provides a powerful method for combining probabilities across multiple scenarios.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The multiplication rule calculates probabilities of joint events</li>

        <li>P(A ∩ B) = P(A|B)P(B)</li>

        <li>An equivalent form is P(A ∩ B) = P(B|A)P(A)</li>

        <li>Independent events satisfy P(A ∩ B) = P(A)P(B)</li>

        <li>Dependent events require conditional probabilities</li>

        <li>The multiplication rule extends naturally to multiple events</li>

        <li>The rule forms a foundation for many advanced probability methods</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/conditional/what-is-conditional-probability/">
         ← Previous: What Is Conditional Probability?
      </a>

      <a class="btn"
         href="/probability/conditional/law-of-total-probability/">
         Next: Law of Total Probability →
      </a>

    </div>

  </div>

</section>