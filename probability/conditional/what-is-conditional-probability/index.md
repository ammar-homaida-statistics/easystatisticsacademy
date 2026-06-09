---
layout: default
title: What Is Conditional Probability?
description: Learn how probabilities change when new information becomes available and discover the foundation of conditional probability.
permalink: /probability/conditional/what-is-conditional-probability/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_conditional_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/conditional/what-is-conditional-probability/",
    label: "What Is Conditional Probability?",
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
      <span class="badge">Foundations</span>
    </div>

    <h1>What Is Conditional Probability?</h1>

    <p class="lead">
      Many probability questions change when new information becomes available.
    </p>

    <p class="lead">
      Conditional probability provides a mathematical framework for updating probabilities when some information is already known.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/conditional/">
         ← Conditional Probability Home
      </a>

      <a class="btn btn-outline"
         href="/probability/conditional/multiplication-rule/">
         Next: Multiplication Rule →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Conditional Probability Exists</h2>

    <p>
      In many situations,
      we receive information before making probability calculations.
    </p>

    <p>
      Once new information becomes available,
      probabilities often change.
    </p>

    <div class="example-box">

      <p>
        What is the probability that a randomly selected card is a king?
      </p>

    </div>

    <p>
      Now suppose we learn that the card is a face card.
    </p>

    <div class="example-box">

      <p>
        What is the probability that the card is a king given that it is a face card?
      </p>

    </div>

    <p>
      The second question uses additional information,
      so the answer changes.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Conditional probability measures the probability of an event after certain information is known.
      </p>

    </div>

    <h2>The Meaning of "Given"</h2>

    <p>
      The word <strong>given</strong> is the most important word in conditional probability.
    </p>

    <p>
      It means that some information has already been revealed.
    </p>

    <div class="example-box">

      <p>
        Probability of rain tomorrow.
      </p>
    </div>

    <p>
      versus
    </p>

    <div class="example-box">

      <p>
        Probability of rain tomorrow given that dark storm clouds are present.
      </p>
    </div>

    <p>
      The second probability incorporates additional information.
    </p>

    <h2>How Information Changes the Sample Space</h2>

    <p>
      Conditional probability works by restricting attention to outcomes consistent with the known information.
    </p>

    <p>
      In effect,
      the sample space becomes smaller.
    </p>

    <div class="example-box">

      <p>
        Original sample space:
      </p>

      <p>
        All 52 cards in a deck
      </p>

    </div>

    <p>
      If we learn the card is a face card,
      the relevant sample space becomes:
    </p>

    <div class="example-box">

      <p>
        12 face cards
      </p>

    </div>

    <p>
      We ignore outcomes that are no longer possible.
    </p>

    <h2>The Notation for Conditional Probability</h2>

    <p>
      Conditional probability is written using a vertical bar.
    </p>

    0

    <p>
      This is read as:
    </p>

    <div class="example-box">

      <p>
        Probability of A given B
      </p>
    </div>

    <p>
      Event B represents the information already known.
    </p>

    <h2>An Intuitive Example</h2>

    <p>
      Consider a standard deck of 52 cards.
    </p>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        A = Card is a king
      </p>

      <p>
        B = Card is a face card
      </p>

    </div>

    <p>
      There are:
    </p>

    <ul class="bullets">

      <li>12 face cards</li>

      <li>4 kings</li>

    </ul>

    <p>
      Once we know the card is a face card,
      only those 12 cards remain relevant.
    </p>

    <p>
      Therefore:
    </p>

    1

    <h2>The Formal Definition</h2>

    <p>
      Conditional probability is defined mathematically as:
    </p>

    2

    <p>
      provided that:
    </p>

    3

    <p>
      This formula is one of the most important formulas in probability.
    </p>

    <h2>Understanding the Formula</h2>

    <p>
      The formula asks:
    </p>

    <ul class="bullets">

      <li>How much probability belongs to both A and B?</li>

      <li>Out of all probability belonging to B?</li>

    </ul>

    <p>
      In other words,
      we zoom into Event B and examine what proportion also belongs to Event A.
    </p>

    <h2>A Venn Diagram Perspective</h2>

    <p>
      Imagine a Venn diagram containing Events A and B.
    </p>

    <p>
      Once we know B has occurred,
      everything outside B becomes irrelevant.
    </p>

    <p>
      The probability calculation is performed only within the B region.
    </p>

    <p>
      This visual interpretation is often helpful.
    </p>

    <h2>Example Using Probabilities</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        P(A ∩ B) = 0.20
      </p>

      <p>
        P(B) = 0.50
      </p>

    </div>

    <p>
      Then:
    </p>

    4

    <p>
      Given that B occurred,
      the probability of A is 0.40.
    </p>

    <h2>Conditional Probability Can Increase</h2>

    <p>
      Sometimes new information makes an event more likely.
    </p>

    <div class="example-box">

      <p>
        Probability of carrying an umbrella.
      </p>

      <p>
        Probability of carrying an umbrella given that it is raining.
      </p>

    </div>

    <p>
      The second probability is usually much larger.
    </p>

    <h2>Conditional Probability Can Decrease</h2>

    <p>
      Information can also reduce probabilities.
    </p>

    <div class="example-box">

      <p>
        Probability a student missed class.
      </p>

      <p>
        Probability a student missed class given that attendance was mandatory and recorded.
      </p>

    </div>

    <p>
      Additional information may make the event less likely.
    </p>

    <h2>Conditional Probability Can Stay the Same</h2>

    <p>
      Sometimes information changes nothing.
    </p>

    <p>
      This occurs when events are independent.
    </p>

    <div class="example-box">

      <p>
        First coin toss is heads.
      </p>

      <p>
        Second coin toss is heads.
      </p>

    </div>

    <p>
      Knowing the first toss does not affect the second.
    </p>

    <p>
      Therefore:
    </p>

    5

    <p>
      when events are independent.
    </p>

    <h2>Why Conditional Probability Is Important</h2>

    <p>
      Conditional probability appears throughout science,
      business,
      medicine,
      engineering,
      economics,
      and artificial intelligence.
    </p>

    <div class="example-box">

      <p>
        Probability of disease given a test result
      </p>

      <p>
        Probability of loan default given income information
      </p>

      <p>
        Probability of rain given weather conditions
      </p>

    </div>

    <p>
      All of these are conditional probability questions.
    </p>

    <h2>The Foundation for Future Topics</h2>

    <p>
      Conditional probability is not just another probability rule.
    </p>

    <p>
      It is the foundation for:
    </p>

    <ul class="bullets">

      <li>The multiplication rule</li>

      <li>Independence</li>

      <li>Tree diagrams</li>

      <li>Bayes' theorem</li>

      <li>Statistical inference</li>

      <li>Machine learning</li>

    </ul>

    <p>
      Many advanced ideas can be traced back to this concept.
    </p>

    <h2>A New Way of Thinking</h2>

    <p>
      Unconditional probability asks:
    </p>

    <div class="example-box">

      <p>
        How likely is Event A?
      </p>
    </div>

    <p>
      Conditional probability asks:
    </p>

    <div class="example-box">

      <p>
        How likely is Event A now that I know Event B occurred?
      </p>
    </div>

    <p>
      This shift in perspective is one of the most important transitions in probability theory.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The conditional probability formula immediately leads to another powerful result.
    </p>

    <p>
      By rearranging the formula,
      we can calculate probabilities of events occurring together.
    </p>

    <p>
      The next lesson introduces the multiplication rule,
      one of the most useful tools in probability.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Conditional probability incorporates additional information</li>

        <li>The word "given" indicates known information</li>

        <li>Conditional probability changes the effective sample space</li>

        <li>P(A|B) means probability of A given B</li>

        <li>Conditional probability is defined as P(A∩B)/P(B)</li>

        <li>Information can increase, decrease, or leave probabilities unchanged</li>

        <li>Conditional probability is the foundation of many advanced probability topics</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/conditional/">
         Conditional Probability Home
      </a>

      <a class="btn"
         href="/probability/conditional/multiplication-rule/">
         Next: Multiplication Rule →
      </a>

    </div>

  </div>

</section>