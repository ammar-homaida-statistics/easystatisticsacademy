---
layout: default
title: Bayes' Theorem
description: Learn how Bayes' theorem updates probabilities when new evidence becomes available and understand one of the most important ideas in statistics.
permalink: /probability/conditional/bayes-theorem/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_conditional_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/conditional/bayes-theorem/",
    label: "Bayes' Theorem",
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
      <span class="badge">Bayesian Thinking</span>
    </div>

    <h1>Bayes' Theorem</h1>

    <p class="lead">
      Bayes' theorem provides a systematic way to update probabilities when new evidence becomes available.
    </p>

    <p class="lead">
      It is one of the most influential ideas in probability, statistics, machine learning, medicine, and decision-making.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/conditional/law-of-total-probability/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/conditional/tree-diagrams/">
         Next: Tree Diagrams →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Central Question</h2>

    <p>
      Many probability questions involve reversing a conditional probability.
    </p>

    <div class="example-box">

      <p>
        If a person has a disease,
        what is the probability of a positive test?
      </p>
    </div>

    <p>
      This probability may be known.
    </p>

    <p>
      However,
      a more practical question is often:
    </p>

    <div class="example-box">

      <p>
        If the test is positive,
        what is the probability that the person has the disease?
      </p>
    </div>

    <p>
      These are not the same probability.
    </p>

    <p>
      Bayes' theorem provides the connection between them.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Bayes' theorem updates beliefs about a cause after observing evidence.
      </p>

    </div>

    <h2>Why Bayes' Theorem Is Needed</h2>

    <p>
      Conditional probabilities have direction.
    </p>

    <div class="example-box">

      <p>
        Probability of Evidence given Cause
      </p>
    </div>

    <p>
      is generally different from:
    </p>

    <div class="example-box">

      <p>
        Probability of Cause given Evidence
      </p>
    </div>

    <p>
      Bayes' theorem allows us to move from one direction to the other.
    </p>

    <h2>Starting from Conditional Probability</h2>

    <p>
      Recall the conditional probability formula.
    </p>

    0

    <p>
      We can also write:
    </p>

    1

    <p>
      Both formulas involve the same intersection probability.
    </p>

    <h2>Deriving Bayes' Theorem</h2>

    <p>
      From the multiplication rule:
    </p>

    2

    <p>
      Substituting into the conditional probability formula gives:
    </p>

    3

    <p>
      This is Bayes' theorem.
    </p>

    <h2>The Bayes Formula</h2>

    4

    <p>
      Although the formula appears simple,
      it is one of the most powerful results in probability.
    </p>

    <h2>Understanding the Components</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Term</th>
            <th>Meaning</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>P(A)</td>
            <td>Prior probability</td>
          </tr>

          <tr>
            <td>P(B|A)</td>
            <td>Likelihood</td>
          </tr>

          <tr>
            <td>P(B)</td>
            <td>Overall probability of evidence</td>
          </tr>

          <tr>
            <td>P(A|B)</td>
            <td>Posterior probability</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Bayesian Update Process</h2>

    <p>
      Bayes' theorem combines:
    </p>

    <ul class="bullets">

      <li>What we believed before seeing evidence.</li>

      <li>The evidence that was observed.</li>

      <li>The strength of the relationship between the evidence and the event.</li>

    </ul>

    <p>
      The result is an updated probability.
    </p>

    <h2>A Medical Testing Example</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        Disease prevalence = 1%
      </p>

      <p>
        Test sensitivity = 95%
      </p>

      <p>
        Positive-test probability = 5%
      </p>

    </div>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        D = Disease
      </p>

      <p>
        + = Positive test
      </p>

    </div>

    <p>
      Bayes' theorem becomes:
    </p>

    5

    <p>
      This calculation updates the probability of disease after observing a positive test result.
    </p>

    <h2>The Role of the Prior</h2>

    <p>
      The prior probability represents our belief before observing new evidence.
    </p>

    <div class="example-box">

      <p>
        Probability of disease before testing.
      </p>
    </div>

    <p>
      Priors often come from:
    </p>

    <ul class="bullets">

      <li>Historical data</li>

      <li>Past studies</li>

      <li>Expert knowledge</li>

      <li>Population statistics</li>

    </ul>

    <h2>The Role of the Likelihood</h2>

    <p>
      The likelihood measures how consistent the observed evidence is with a particular explanation.
    </p>

    <div class="example-box">

      <p>
        How likely is a positive test if the disease is actually present?
      </p>
    </div>

    <p>
      Strong evidence produces larger updates.
    </p>

    <h2>The Posterior Probability</h2>

    <p>
      The posterior probability is the updated belief after incorporating evidence.
    </p>

    <p>
      It represents what we believe now,
      not what we believed initially.
    </p>

    <div class="concept-box">

      <strong>Bayesian thinking:</strong>

      <p>
        Prior belief + Evidence → Updated belief
      </p>

    </div>

    <h2>The Importance of Base Rates</h2>

    <p>
      Bayes' theorem explains why base rates matter.
    </p>

    <p>
      Rare events remain rare even when evidence appears convincing.
    </p>

    <p>
      Ignoring base rates often leads to incorrect conclusions.
    </p>

    <div class="example-box">

      <p>
        A highly accurate test can still produce many false alarms when a condition is extremely rare.
      </p>
    </div>

    <h2>The Connection to the Law of Total Probability</h2>

    <p>
      The denominator in Bayes' theorem is often found using the Law of Total Probability.
    </p>

    <p>
      For example:
    </p>

    6

    <p>
      This calculation accounts for all ways the evidence could occur.
    </p>

    <h2>Applications of Bayes' Theorem</h2>

    <p>
      Bayes' theorem appears throughout modern science and technology.
    </p>

    <ul class="bullets">

      <li>Medical diagnosis</li>

      <li>Spam filtering</li>

      <li>Machine learning</li>

      <li>Artificial intelligence</li>

      <li>Risk assessment</li>

      <li>Search engines</li>

      <li>Fraud detection</li>

      <li>Scientific inference</li>

    </ul>

    <p>
      Many modern predictive systems are built on Bayesian ideas.
    </p>

    <h2>A Common Misunderstanding</h2>

    <p>
      Students often assume:
    </p>

    <div class="example-box">

      <p>
        P(A|B) = P(B|A)
      </p>
    </div>

    <p>
      This is usually false.
    </p>

    <p>
      Bayes' theorem exists precisely because these probabilities differ.
    </p>

    <h2>The Big Picture</h2>

    <p>
      Bayes' theorem transforms probability from a static description of uncertainty into a dynamic system for learning from evidence.
    </p>

    <p>
      Every time new information becomes available,
      Bayes' theorem provides a principled method for updating probabilities.
    </p>

    <h2>Preparing for Tree Diagrams</h2>

    <p>
      Many conditional probability problems involve multiple stages and pathways.
    </p>

    <p>
      Visual tools can make these problems easier to understand.
    </p>

    <p>
      Tree diagrams provide one of the most useful ways to organize conditional probabilities,
      multiplication rules,
      and Bayesian calculations.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The next lesson introduces tree diagrams,
      a graphical method for representing sequential probability processes and organizing complex probability calculations.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Bayes' theorem updates probabilities using new evidence</li>

        <li>P(A|B) and P(B|A) are generally different probabilities</li>

        <li>Bayes' theorem connects these two conditional probabilities</li>

        <li>The theorem combines prior information and observed evidence</li>

        <li>The result is an updated posterior probability</li>

        <li>Base rates play an important role in Bayesian reasoning</li>

        <li>Bayes' theorem is one of the foundations of modern statistics and machine learning</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/conditional/law-of-total-probability/">
         ← Previous: Law of Total Probability
      </a>

      <a class="btn"
         href="/probability/conditional/tree-diagrams/">
         Next: Tree Diagrams →
      </a>

    </div>

  </div>

</section>