---
layout: default
title: Union, Intersection, and Venn Thinking
description: Learn how events can be combined using unions and intersections, and how Venn diagrams help visualize probability relationships.
permalink: /probability/basics/union-intersection-and-venn-thinking/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_basics_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/basics/union-intersection-and-venn-thinking/",
    label: "Union, Intersection, and Venn Thinking",
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
      <span class="badge">Events</span>
    </div>

    <h1>Union, Intersection, and Venn Thinking</h1>

    <p class="lead">
      Probability often involves combining events.
    </p>

    <p class="lead">
      We may want to know the probability that one event occurs, another event occurs, or that both occur together. Unions, intersections, and Venn diagrams provide a powerful framework for thinking about these relationships.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/basics/probability-axioms-and-basic-rules/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/basics/equally-likely-and-counting-intuition/">
         Next: Equally Likely and Counting Intuition →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>Why Combine Events?</h2>

    <p>
      Many probability questions involve more than one event.
    </p>

    <div class="example-box">

      <p>
        What is the probability of drawing a heart or a king?
      </p>

      <p>
        What is the probability that a student studies and passes?
      </p>

      <p>
        What is the probability of rain and strong winds?
      </p>

    </div>

    <p>
      To answer questions like these,
      we need methods for combining events.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Unions describe "or" situations. Intersections describe "and" situations.
      </p>

    </div>

    <h2>Introducing Event A and Event B</h2>

    <p>
      Throughout probability,
      events are commonly represented by capital letters.
    </p>

    <div class="example-box">

      <p>
        A = Rolling an even number
      </p>

      <p>
        B = Rolling a number greater than 3
      </p>

    </div>

    <p>
      We can study each event individually or examine how they relate to one another.
    </p>

    <h2>What Is a Union?</h2>

    <p>
      The <strong>union</strong> of two events contains outcomes that belong to Event A,
      Event B,
      or both.
    </p>

    <p>
      The union is written as:
    </p>

    0

    <p>
      The symbol ∪ can be interpreted as "or."
    </p>

    <h2>Union Example</h2>

    <p>
      Suppose a die is rolled.
    </p>

    <div class="example-box">

      <p>
        A = {2,4,6}
      </p>

      <p>
        B = {4,5,6}
      </p>

    </div>

    <p>
      The union contains every outcome appearing in either event.
    </p>

    <div class="example-box">

      <p>
        A ∪ B = {2,4,5,6}
      </p>

    </div>

    <p>
      Notice that outcomes are listed only once.
    </p>

    <h2>What Is an Intersection?</h2>

    <p>
      The <strong>intersection</strong> of two events contains outcomes shared by both events.
    </p>

    <p>
      The intersection is written as:
    </p>

    1

    <p>
      The symbol ∩ can be interpreted as "and."
    </p>

    <h2>Intersection Example</h2>

    <p>
      Using the previous events:
    </p>

    <div class="example-box">

      <p>
        A = {2,4,6}
      </p>

      <p>
        B = {4,5,6}
      </p>

    </div>

    <p>
      The shared outcomes are:
    </p>

    <div class="example-box">

      <p>
        A ∩ B = {4,6}
      </p>

    </div>

    <p>
      These outcomes belong to both events simultaneously.
    </p>

    <h2>Understanding "Or"</h2>

    <p>
      In probability,
      "or" usually means inclusive or.
    </p>

    <p>
      This means:
    </p>

    <ul class="bullets">

      <li>Event A occurs</li>

      <li>Event B occurs</li>

      <li>Both events occur</li>

    </ul>

    <p>
      All three possibilities belong to the union.
    </p>

    <h2>Understanding "And"</h2>

    <p>
      The word "and" is much more restrictive.
    </p>

    <p>
      The outcome must satisfy both events simultaneously.
    </p>

    <p>
      Only outcomes in the overlap belong to the intersection.
    </p>

    <h2>Venn Diagrams</h2>

    <p>
      Venn diagrams provide a visual way to represent events.
    </p>

    <p>
      Each circle represents an event,
      while the surrounding rectangle represents the sample space.
    </p>

    <div class="example-box">

      <p>
        Rectangle → Sample Space
      </p>

      <p>
        Circle A → Event A
      </p>

      <p>
        Circle B → Event B
      </p>

    </div>

    <p>
      The overlap between circles represents the intersection.
    </p>

    <h2>Visualizing the Union</h2>

    <p>
      In a Venn diagram,
      the union includes all regions covered by either circle.
    </p>

    <p>
      This includes:
    </p>

    <ul class="bullets">

      <li>A only</li>

      <li>B only</li>

      <li>The overlap</li>

    </ul>

    <p>
      Everything inside either circle belongs to the union.
    </p>

    <h2>Visualizing the Intersection</h2>

    <p>
      In a Venn diagram,
      the intersection is only the overlapping region.
    </p>

    <p>
      This region contains outcomes belonging to both events simultaneously.
    </p>

    <h2>Mutually Exclusive Events</h2>

    <p>
      Some events have no overlap.
    </p>

    <p>
      Such events are called mutually exclusive.
    </p>

    <div class="example-box">

      <p>
        A = Rolling a 1
      </p>

      <p>
        B = Rolling a 6
      </p>

    </div>

    <p>
      These events cannot occur together.
    </p>

    <p>
      Their intersection is empty.
    </p>

    2

    <h2>Union Rule for Mutually Exclusive Events</h2>

    <p>
      When events cannot occur together,
      probabilities simply add.
    </p>

    3

    <p>
      This rule was introduced in the previous lesson.
    </p>

    <h2>When Events Overlap</h2>

    <p>
      Most events are not mutually exclusive.
    </p>

    <p>
      When overlap exists,
      simply adding probabilities counts the overlap twice.
    </p>

    <p>
      Therefore,
      a correction is needed.
    </p>

    <h2>The Addition Rule</h2>

    <p>
      For any two events:
    </p>

    4

    <p>
      The overlap is subtracted once to avoid double counting.
    </p>

    <h2>Why Subtract the Intersection?</h2>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        P(A) = 0.50
      </p>

      <p>
        P(B) = 0.40
      </p>

      <p>
        P(A ∩ B) = 0.10
      </p>

    </div>

    <p>
      If we simply add:
    </p>

    <div class="example-box">

      <p>
        0.50 + 0.40 = 0.90
      </p>

    </div>

    <p>
      The overlap is counted twice.
    </p>

    <p>
      Applying the addition rule:
    </p>

    5

    <p>
      The correct probability is 0.80.
    </p>

    <h2>Complement Regions in Venn Diagrams</h2>

    <p>
      Venn diagrams also help visualize complements.
    </p>

    <p>
      The complement of Event A consists of everything outside Circle A but still inside the sample space.
    </p>

    <p>
      This idea connects directly to the complement rule introduced earlier.
    </p>

    <h2>Thinking in Regions</h2>

    <p>
      Venn diagrams encourage a useful habit:
      thinking about events as regions of the sample space.
    </p>

    <p>
      Probability then becomes the amount of probability assigned to those regions.
    </p>

    <p>
      This perspective will be extremely useful in later topics.
    </p>

    <h2>Why Venn Thinking Matters</h2>

    <p>
      Many important probability concepts rely on event relationships.
    </p>

    <p>
      These include:
    </p>

    <ul class="bullets">

      <li>Conditional probability</li>

      <li>Independence</li>

      <li>Bayes' theorem</li>

      <li>Contingency tables</li>

      <li>Statistical inference</li>

    </ul>

    <p>
      Venn diagrams provide an intuitive foundation for all of them.
    </p>

    <h2>A Quick Summary</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Symbol</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>A ∪ B</td>
            <td>A or B or both</td>
          </tr>

          <tr>
            <td>A ∩ B</td>
            <td>A and B</td>
          </tr>

          <tr>
            <td>Aᶜ</td>
            <td>Not A</td>
          </tr>

          <tr>
            <td>∅</td>
            <td>Impossible event</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      We now understand how events are defined and combined.
    </p>

    <p>
      The next question is:
      how do we actually count outcomes and assign probabilities?
    </p>

    <p>
      The next lesson introduces equally likely outcomes and counting intuition,
      which form the basis for many classical probability calculations.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The union of events represents "A or B"</li>

        <li>The intersection of events represents "A and B"</li>

        <li>Venn diagrams visualize relationships between events</li>

        <li>Mutually exclusive events have no overlap</li>

        <li>The addition rule accounts for overlapping events</li>

        <li>Complements represent outcomes outside an event</li>

        <li>Venn thinking is foundational for later probability topics</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/basics/probability-axioms-and-basic-rules/">
         ← Previous: Probability Axioms and Basic Rules
      </a>

      <a class="btn"
         href="/probability/basics/equally-likely-and-counting-intuition/">
         Next: Equally Likely and Counting Intuition →
      </a>

    </div>

  </div>

</section>