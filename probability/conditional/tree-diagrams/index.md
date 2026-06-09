---
layout: default
title: Tree Diagrams
description: Learn how tree diagrams organize sequential probability problems and simplify conditional probability calculations.
permalink: /probability/conditional/tree-diagrams/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_conditional_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/conditional/tree-diagrams/",
    label: "Tree Diagrams",
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
      <span class="badge">Visualization</span>
    </div>

    <h1>Tree Diagrams</h1>

    <p class="lead">
      Conditional probability problems often involve multiple stages and possible pathways.
    </p>

    <p class="lead">
      Tree diagrams provide a visual framework for organizing these pathways and applying the multiplication rule systematically.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/conditional/bayes-theorem/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/conditional/base-rate-neglect-and-fallacies/">
         Next: Base-Rate Neglect and Fallacies →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Tree Diagrams Matter</h2>

    <p>
      Many probability problems involve a sequence of events.
    </p>

    <div class="example-box">

      <p>
        Toss a coin twice.
      </p>

      <p>
        Draw two cards from a deck.
      </p>

      <p>
        Take a medical test after screening.
      </p>

    </div>

    <p>
      As the number of stages increases,
      it becomes difficult to keep track of all possible outcomes mentally.
    </p>

    <p>
      Tree diagrams help organize the possibilities.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        A tree diagram displays all possible pathways through a sequential process.
      </p>

    </div>

    <h2>What Is a Tree Diagram?</h2>

    <p>
      A tree diagram is a branching structure used to represent possible outcomes.
    </p>

    <p>
      Each branch corresponds to a possible result at a particular stage.
    </p>

    <p>
      Following a path from the start to an endpoint represents one complete outcome sequence.
    </p>

    <h2>A Simple Coin Toss Example</h2>

    <p>
      Suppose a fair coin is tossed twice.
    </p>

    <p>
      The first toss can produce:
    </p>

    <ul class="bullets">

      <li>Heads</li>

      <li>Tails</li>

    </ul>

    <p>
      From each of these outcomes,
      the second toss can again produce heads or tails.
    </p>

    <div class="example-box">

      <p>
        HH
      </p>

      <p>
        HT
      </p>

      <p>
        TH
      </p>

      <p>
        TT
      </p>

    </div>

    <p>
      These four paths form the complete sample space.
    </p>

    <h2>Reading a Tree Diagram</h2>

    <p>
      Each level of the tree corresponds to a stage of the experiment.
    </p>

    <p>
      Each branch represents a possible outcome at that stage.
    </p>

    <p>
      The endpoints represent complete outcome sequences.
    </p>

    <h2>Assigning Probabilities to Branches</h2>

    <p>
      Every branch receives a probability.
    </p>

    <p>
      For a fair coin:
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
      These probabilities are written on the corresponding branches.
    </p>

    <h2>Multiplying Along a Path</h2>

    <p>
      The multiplication rule applies naturally to tree diagrams.
    </p>

    <p>
      To find the probability of a complete path:
    </p>

    <ul class="bullets">

      <li>Multiply the probabilities along that path.</li>

    </ul>

    <p>
      For example:
    </p>

    <div class="example-box">

      <p>
        HH
      </p>
    </div>

    <p>
      has probability:
    </p>

    0

    <h2>Why Multiplication Works</h2>

    <p>
      Each branch represents a conditional probability.
    </p>

    <p>
      The probability of the entire sequence equals the probability of moving through every branch in the path.
    </p>

    <p>
      This is exactly the multiplication rule.
    </p>

    <h2>Adding Across Paths</h2>

    <p>
      Sometimes an event can occur through multiple pathways.
    </p>

    <p>
      In that case:
    </p>

    <ul class="bullets">

      <li>Calculate the probability of each path.</li>

      <li>Add the path probabilities.</li>

    </ul>

    <p>
      This idea comes directly from the Law of Total Probability.
    </p>

    <div class="concept-box">

      <strong>Memory rule:</strong>

      <p>
        Multiply along branches. Add across paths.
      </p>

    </div>

    <h2>Example: At Least One Head</h2>

    <p>
      For two coin tosses:
    </p>

    <div class="example-box">

      <p>
        HH
      </p>

      <p>
        HT
      </p>

      <p>
        TH
      </p>

      <p>
        TT
      </p>

    </div>

    <p>
      The event "at least one head" includes:
    </p>

    <div class="example-box">

      <p>
        HH, HT, TH
      </p>

    </div>

    <p>
      Therefore:
    </p>

    1

    <p>
      The probability is 0.75.
    </p>

    <h2>Tree Diagrams and Conditional Probability</h2>

    <p>
      Tree diagrams become even more useful when probabilities change from stage to stage.
    </p>

    <p>
      This often occurs when events are dependent.
    </p>

    <div class="example-box">

      <p>
        Drawing cards without replacement
      </p>
    </div>

    <p>
      The probability of the second draw depends on the first draw.
    </p>

    <h2>Example: Drawing Two Cards</h2>

    <p>
      Suppose a deck contains:
    </p>

    <ul class="bullets">

      <li>4 aces</li>

      <li>48 non-aces</li>

    </ul>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        A = Ace
      </p>

      <p>
        N = Non-ace
      </p>

    </div>

    <p>
      After drawing an ace,
      the probabilities for the second draw change.
    </p>

    <p>
      Tree diagrams display these changing probabilities clearly.
    </p>

    <h2>Visualizing Bayes' Theorem</h2>

    <p>
      Tree diagrams are frequently used to solve Bayesian problems.
    </p>

    <p>
      A tree can represent:
    </p>

    <ul class="bullets">

      <li>Disease or no disease</li>

      <li>Positive or negative test</li>

    </ul>

    <p>
      Path probabilities are then combined to calculate posterior probabilities.
    </p>

    <p>
      Many Bayes' theorem problems become easier when drawn as trees.
    </p>

    <h2>Tree Diagrams and Partitions</h2>

    <p>
      Recall that the Law of Total Probability partitions the sample space into pathways.
    </p>

    <p>
      Tree diagrams provide a visual representation of those pathways.
    </p>

    <p>
      Every branch represents a possible route through the experiment.
    </p>

    <h2>Advantages of Tree Diagrams</h2>

    <ul class="bullets">

      <li>Organize complex probability problems</li>

      <li>Display conditional probabilities clearly</li>

      <li>Reduce calculation mistakes</li>

      <li>Support Bayes' theorem calculations</li>

      <li>Provide visual intuition</li>

    </ul>

    <p>
      They are especially useful when several stages are involved.
    </p>

    <h2>A Common Mistake</h2>

    <p>
      Students sometimes add branch probabilities when they should multiply.
    </p>

    <p>
      Remember:
    </p>

    <div class="example-box">

      <p>
        Branch probabilities represent sequential events.
      </p>
    </div>

    <p>
      Sequential events require multiplication.
    </p>

    <p>
      Addition is used only when combining separate pathways leading to the same event.
    </p>

    <h2>When Should You Draw a Tree?</h2>

    <p>
      Tree diagrams are particularly useful when:
    </p>

    <ul class="bullets">

      <li>Several stages occur in sequence.</li>

      <li>Conditional probabilities are involved.</li>

      <li>Many possible pathways exist.</li>

      <li>Bayesian reasoning is required.</li>

    </ul>

    <p>
      In these situations,
      drawing a tree often simplifies the entire problem.
    </p>

    <h2>The Big Picture</h2>

    <p>
      Tree diagrams combine three major ideas:
    </p>

    <ul class="bullets">

      <li>Conditional probability</li>

      <li>The multiplication rule</li>

      <li>The Law of Total Probability</li>

    </ul>

    <p>
      They provide a visual framework for understanding how these concepts work together.
    </p>

    <h2>Preparing for Probability Fallacies</h2>

    <p>
      Even when calculations are correct,
      human intuition often misinterprets probabilities.
    </p>

    <p>
      People frequently ignore base rates,
      misunderstand conditional probabilities,
      and draw incorrect conclusions from evidence.
    </p>

    <p>
      These mistakes are called probability fallacies.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The next lesson examines one of the most common reasoning errors in probability:
      base-rate neglect.
    </p>

    <p>
      We will also explore several probability fallacies that affect decision-making in everyday life,
      science,
      medicine,
      and business.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Tree diagrams represent sequential probability processes</li>

        <li>Each branch corresponds to a possible outcome</li>

        <li>Complete paths represent full outcome sequences</li>

        <li>Probabilities are multiplied along branches</li>

        <li>Probabilities are added across relevant paths</li>

        <li>Tree diagrams simplify conditional probability calculations</li>

        <li>Tree diagrams are particularly useful for Bayes' theorem problems</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/conditional/bayes-theorem/">
         ← Previous: Bayes' Theorem
      </a>

      <a class="btn"
         href="/probability/conditional/base-rate-neglect-and-fallacies/">
         Next: Base-Rate Neglect and Fallacies →
      </a>

    </div>

  </div>

</section>