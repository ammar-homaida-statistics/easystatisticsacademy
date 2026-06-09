---
layout: default
title: Law of Total Probability
description: Learn how to calculate probabilities by combining multiple possible pathways that lead to an event.
permalink: /probability/conditional/law-of-total-probability/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_conditional_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/conditional/law-of-total-probability/",
    label: "Law of Total Probability",
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
      <span class="badge">Core Theorem</span>
    </div>

    <h1>Law of Total Probability</h1>

    <p class="lead">
      Many events can occur through several different pathways.
    </p>

    <p class="lead">
      The Law of Total Probability provides a systematic method for combining those pathways and calculating the overall probability of an event.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/conditional/multiplication-rule/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/conditional/bayes-theorem/">
         Next: Bayes' Theorem →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why We Need the Law of Total Probability</h2>

    <p>
      Sometimes an event can happen in more than one way.
    </p>

    <div class="example-box">

      <p>
        A customer may purchase a product after seeing an online advertisement.
      </p>

      <p>
        Another customer may purchase without seeing the advertisement.
      </p>

    </div>

    <p>
      Both pathways contribute to the total probability of a purchase.
    </p>

    <p>
      The Law of Total Probability allows us to combine such pathways into a single probability.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Total probability equals the sum of probabilities from all mutually exclusive pathways leading to an event.
      </p>

    </div>

    <h2>Partitioning the Sample Space</h2>

    <p>
      The law begins by dividing the sample space into non-overlapping events.
    </p>

    <p>
      These events are called a partition.
    </p>

    <div class="example-box">

      <p>
        Student studies
      </p>

      <p>
        Student does not study
      </p>

    </div>

    <p>
      Every student belongs to exactly one of these categories.
    </p>

    <p>
      Together they cover the entire sample space.
    </p>

    <h2>A Simple Two-Group Version</h2>

    <p>
      Suppose Event B and its complement divide the sample space.
    </p>

    <p>
      Then any occurrence of Event A must happen through one of two possibilities:
    </p>

    <ul class="bullets">

      <li>A occurs together with B</li>

      <li>A occurs together with Bᶜ</li>

    </ul>

    <p>
      Therefore:
    </p>

    0

    <h2>Applying the Multiplication Rule</h2>

    <p>
      Using the multiplication rule:
    </p>

    1

    <p>
      This is the simplest form of the Law of Total Probability.
    </p>

    <h2>Interpreting the Formula</h2>

    <p>
      The formula says:
    </p>

    <ul class="bullets">

      <li>Consider each possible pathway.</li>

      <li>Find the probability of the pathway.</li>

      <li>Find the conditional probability of the event within that pathway.</li>

      <li>Add the resulting probabilities.</li>

    </ul>

    <p>
      The sum gives the overall probability.
    </p>

    <h2>Example: Passing an Exam</h2>

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

      <p>
        P(Pass | No Study) = 0.40
      </p>

    </div>

    <p>
      Also:
    </p>

    <div class="example-box">

      <p>
        P(No Study) = 0.40
      </p>

    </div>

    <p>
      Applying the law:
    </p>

    2

    <p>
      Therefore:
    </p>

    3

    <p>
      The overall probability of passing is 0.70.
    </p>

    <h2>A Tree Diagram Interpretation</h2>

    <p>
      The Law of Total Probability is often visualized using a tree diagram.
    </p>

    <p>
      Each branch represents a pathway through the sample space.
    </p>

    <p>
      Multiplication gives probabilities along branches,
      while addition combines branches leading to the same outcome.
    </p>

    <div class="concept-box">

      <strong>Useful memory rule:</strong>

      <p>
        Multiply along branches. Add across branches.
      </p>

    </div>

    <h2>More Than Two Pathways</h2>

    <p>
      Real problems often involve several pathways.
    </p>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        B₁, B₂, B₃, ..., Bₙ
      </p>

    </div>

    <p>
      form a partition of the sample space.
    </p>

    <p>
      Then:
    </p>

    4

    <p>
      This is the general form of the Law of Total Probability.
    </p>

    <h2>Example: Customer Purchases</h2>

    <p>
      Customers may arrive from three marketing channels:
    </p>

    <ul class="bullets">

      <li>Email campaign</li>

      <li>Social media</li>

      <li>Direct website visit</li>

    </ul>

    <p>
      Each channel has its own probability of producing a purchase.
    </p>

    <p>
      The overall purchase probability is found by combining all channels using the Law of Total Probability.
    </p>

    <h2>Why the Law Works</h2>

    <p>
      The partition divides the sample space into non-overlapping pieces.
    </p>

    <p>
      Since every occurrence of Event A must belong to exactly one piece,
      adding the probabilities from all pieces gives the total probability of A.
    </p>

    <p>
      No outcomes are omitted and none are counted twice.
    </p>

    <h2>Connection to Venn Diagrams</h2>

    <p>
      In a Venn diagram,
      the event A may overlap several different regions.
    </p>

    <p>
      The Law of Total Probability simply adds the probability contained in each region of overlap.
    </p>

    <p>
      This provides a geometric interpretation of the formula.
    </p>

    <h2>A Common Mistake</h2>

    <p>
      Students sometimes average conditional probabilities directly.
    </p>

    <p>
      This is incorrect because pathways often have different probabilities.
    </p>

    <div class="example-box">

      <p>
        A pathway that occurs frequently should contribute more to the final probability than a rare pathway.
      </p>

    </div>

    <p>
      The weighting is provided automatically by the factors P(Bᵢ).
    </p>

    <h2>Relationship to the Multiplication Rule</h2>

    <p>
      The Law of Total Probability is built directly from the multiplication rule.
    </p>

    <p>
      First:
    </p>

    <ul class="bullets">

      <li>Use multiplication to compute probabilities along pathways.</li>

      <li>Use addition to combine pathways.</li>

    </ul>

    <p>
      Together these ideas form the foundation of many probability calculations.
    </p>

    <h2>Applications</h2>

    <p>
      The Law of Total Probability appears in:
    </p>

    <ul class="bullets">

      <li>Medical testing</li>

      <li>Risk analysis</li>

      <li>Insurance models</li>

      <li>Machine learning</li>

      <li>Reliability engineering</li>

      <li>Bayesian statistics</li>

    </ul>

    <p>
      It is one of the most widely used tools in probability.
    </p>

    <h2>The Bridge to Bayes' Theorem</h2>

    <p>
      The Law of Total Probability becomes especially powerful when combined with conditional probability.
    </p>

    <p>
      In fact,
      it provides the denominator in one of the most important formulas in statistics:
      Bayes' theorem.
    </p>

    <p>
      Bayes' theorem allows us to reverse conditional probabilities and update beliefs when new evidence becomes available.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      We have learned how to compute overall probabilities by combining multiple pathways.
    </p>

    <p>
      The next lesson introduces Bayes' theorem,
      which uses conditional probability and the Law of Total Probability to answer one of the most important questions in probability:
    </p>

    <div class="example-box">

      <p>
        Given new evidence,
        how should we update what we believe?
      </p>
    </div>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The Law of Total Probability combines multiple pathways leading to an event</li>

        <li>It requires a partition of the sample space</li>

        <li>Probabilities are found by multiplying along pathways and adding across pathways</li>

        <li>The two-group form uses an event and its complement</li>

        <li>The general form uses a collection of mutually exclusive events</li>

        <li>The law prevents missing or double-counting outcomes</li>

        <li>The Law of Total Probability is a key ingredient of Bayes' theorem</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/conditional/multiplication-rule/">
         ← Previous: Multiplication Rule
      </a>

      <a class="btn"
         href="/probability/conditional/bayes-theorem/">
         Next: Bayes' Theorem →
      </a>

    </div>

  </div>

</section>