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

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/conditional/multiplication-rule/",
    label: "Multiplication Rule",
    ts: Date.now()
    }));
  } catch (_) {
    // Persisting progress is optional; unavailable storage must not interrupt lessons.
  }

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
      Recall the definition of conditional probability; the condition P(B) must have positive probability.
    </p>

    
    \[
    P(A\mid B)=\frac{P(A\cap B)}{P(B)},\quad P(B)>0
    \]


    <p>
      This formula describes the probability of A given that B has occurred.
    </p>

    <h2>Rearranging the Formula</h2>

    <p>
      Multiplying both sides by P(B) gives:
    </p>

    
    \[
    P(A\cap B)=P(A\mid B)P(B),\quad P(B)>0
    \]


    <p>
      This is the multiplication rule.
    </p>

    <p>
      It tells us how to calculate the probability that both A and B occur.
    </p>

    <h2>An Equivalent Version</h2>

    <p>
      When P(A) is positive, the roles of A and B can be reversed to give:
    </p>

    
    \[
    P(A\cap B)=P(B\mid A)P(A),\quad P(A)>0
    \]


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

    
    \[
    P(A)=\frac{4}{52}=\frac{1}{13}
    \]


    <p>
      After one ace has been removed:
    </p>

    
    \[
    P(B\mid A)=\frac{3}{51}=\frac{1}{17}
    \]


    <p>
      Therefore:
    </p>

    
    \[
    P(A\cap B)=\frac{4}{52}\cdot\frac{3}{51}=\frac{1}{221}\approx0.004525
    \]


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

    
    \[
    P(A\mid B)=P(A)\quad\text{when }P(B)>0
    \]


    <p>
      The occurrence of B does not affect A.
    </p>

    <h2>Multiplication Rule for Independent Events</h2>

    <p>
      Substituting independence into the multiplication rule gives:
    </p>

    
    \[
    P(A\cap B)=P(A)P(B)
    \]


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

    
    \[
    P(A\cap B)=0.5\times0.5=0.25
    \]


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

    
    \[
    P(\mathrm{Study}\cap\mathrm{Pass})=P(\mathrm{Study})P(\mathrm{Pass}\mid\mathrm{Study})=0.60(0.90)=0.54
    \]


    <p>
      The probability that a student studies and passes is 0.54.
    </p>


    <!-- INTERACTIVE CONDITIONAL PROBABILITY TREE -->
    <div class="concept-box esa-conditional-tree" id="esa-conditional-tree-explorer"
         role="group" aria-labelledby="esa-conditional-tree-heading">
      <h2 id="esa-conditional-tree-heading">Interactive Conditional Probability Tree</h2>
      <p>Explore a hypothetical population of students. A student either studies or does not study,
         and then either passes or does not pass. Multiply down a branch, add disjoint
         passing branches, and use Bayes' theorem to reverse a conditional probability.</p>
      <div class="esa-conditional-tree-fields">
        <div>
          <label for="esa-tree-study"><strong>Probability of studying:
            <output id="esa-tree-study-value" for="esa-tree-study">0.60</output></strong></label>
          <input id="esa-tree-study" type="range" min="0.05" max="0.95" step="0.05" value="0.6">
        </div>
        <div>
          <label for="esa-tree-pass-study"><strong>Probability of passing given studying:
            <output id="esa-tree-pass-study-value" for="esa-tree-pass-study">0.90</output></strong></label>
          <input id="esa-tree-pass-study" type="range" min="0" max="1" step="0.05" value="0.9">
        </div>
        <div>
          <label for="esa-tree-pass-no-study"><strong>Probability of passing given no studying:
            <output id="esa-tree-pass-no-study-value" for="esa-tree-pass-no-study">0.40</output></strong></label>
          <input id="esa-tree-pass-no-study" type="range" min="0" max="1" step="0.05" value="0.4">
        </div>
      </div>
      <p class="muted-mini">All three sliders describe illustrative probabilities, not causal effects.
         Each second-stage split has complementary pass and fail probabilities. The first-stage
         branches have positive probability, so the input conditional probabilities are defined.</p>
      <div class="esa-tree-results" role="status" aria-live="polite" aria-atomic="true">
        <h3>Two-stage probability tree</h3>
        <ul class="esa-tree-root">
          <li>
            <strong>Studies — P(Study) = <output id="esa-tree-p-study">0.6000</output></strong>
            <ul>
              <li>Pass: P(Pass | Study) = <output id="esa-tree-p-pass-study">0.9000</output>
                <span class="esa-tree-path">Joint P(Study and Pass) = <output id="esa-tree-joint-study-pass">0.5400</output></span>
              </li>
              <li>No pass: P(No Pass | Study) = <output id="esa-tree-p-fail-study">0.1000</output>
                <span class="esa-tree-path">Joint P(Study and No Pass) = <output id="esa-tree-joint-study-fail">0.0600</output></span>
              </li>
            </ul>
          </li>
          <li>
            <strong>No study — P(No Study) = <output id="esa-tree-p-no-study">0.4000</output></strong>
            <ul>
              <li>Pass: P(Pass | No Study) = <output id="esa-tree-p-pass-no-study">0.4000</output>
                <span class="esa-tree-path">Joint P(No Study and Pass) = <output id="esa-tree-joint-no-study-pass">0.1600</output></span>
              </li>
              <li>No pass: P(No Pass | No Study) = <output id="esa-tree-p-fail-no-study">0.6000</output>
                <span class="esa-tree-path">Joint P(No Study and No Pass) = <output id="esa-tree-joint-no-study-fail">0.2400</output></span>
              </li>
            </ul>
          </li>
        </ul>
        <h3>Follow the paths</h3>
        <p><strong>Multiply:</strong> P(Study and Pass) = P(Study) × P(Pass | Study) =
          <output id="esa-tree-multiply">0.5400</output>.</p>
        <p><strong>Add:</strong> P(Pass) = P(Study and Pass) + P(No Study and Pass) =
          <output id="esa-tree-total-pass">0.7000</output>.</p>
        <p><strong>Bayes:</strong> P(Study | Pass) = P(Study and Pass) / P(Pass) =
          <output id="esa-tree-bayes">0.7714</output>.</p>
        <p id="esa-tree-undefined-note" hidden>
          A reverse conditional probability given Pass is undefined when P(Pass) = 0:
          an event with zero probability cannot be used as the conditioning event.</p>
      </div>
      <button id="esa-tree-reset" class="btn btn-outline" type="button">Reset probability tree</button>
      <p class="muted-mini">The four final joint probabilities sum to 1 (apart from displayed rounding).
         This same example appears in the <a href="/probability/conditional/law-of-total-probability/">Law of Total Probability</a> lesson.
         See <a href="/probability/conditional/bayes-theorem/">Bayes' Theorem</a> to interpret the reverse conditional.</p>
    </div>
    <style>
      #esa-conditional-tree-explorer {box-sizing:border-box;width:100%;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-conditional-tree-explorer .esa-conditional-tree-fields {
        display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,225px),1fr));gap:14px;
        margin:16px 0
      }
      #esa-conditional-tree-explorer .esa-conditional-tree-fields>div {min-width:0}
      #esa-conditional-tree-explorer label {display:block;margin-bottom:10px}
      #esa-conditional-tree-explorer input[type="range"] {box-sizing:border-box;display:block;width:100%;max-width:100%;min-width:0}
      #esa-conditional-tree-explorer .esa-tree-root,
      #esa-conditional-tree-explorer .esa-tree-root ul {list-style:none;padding:0;margin:12px 0}
      #esa-conditional-tree-explorer .esa-tree-root>li {margin:14px 0;padding-left:12px;border-left:3px solid #64748b}
      #esa-conditional-tree-explorer .esa-tree-root>li>ul {padding-left:12px;margin:8px 0;border-left:2px solid #0d9488}
      #esa-conditional-tree-explorer .esa-tree-root>li>ul>li {margin:10px 0;padding-left:8px}
      #esa-conditional-tree-explorer .esa-tree-path {display:block;font-size:.94em}
      #esa-conditional-tree-explorer .esa-tree-results h3 {font-size:1.05em;margin:12px 0 6px}
      #esa-conditional-tree-explorer .esa-tree-results p {margin:10px 0}
      #esa-conditional-tree-explorer [hidden] {display:none!important}
    </style>
    <script>
    (function () {
      "use strict";
      const root=document.getElementById("esa-conditional-tree-explorer");
      if (!root) return;
      const field=id=>root.querySelector("#"+id);
      const study=field("esa-tree-study");
      const passStudy=field("esa-tree-pass-study");
      const passNoStudy=field("esa-tree-pass-no-study");
      const display=(id,value)=>{field(id).textContent=value.toFixed(4);};
      function update() {
        const s=Number(study.value),q1=Number(passStudy.value),q0=Number(passNoStudy.value);
        field("esa-tree-study-value").textContent=s.toFixed(2);
        field("esa-tree-pass-study-value").textContent=q1.toFixed(2);
        field("esa-tree-pass-no-study-value").textContent=q0.toFixed(2);
        const ns=1-s;
        const sp=s*q1,sf=s*(1-q1),np=ns*q0,nf=ns*(1-q0);
        const overall=sp+np;
        const cells=[
          ["esa-tree-p-study",s],["esa-tree-p-no-study",ns],
          ["esa-tree-p-pass-study",q1],["esa-tree-p-fail-study",1-q1],
          ["esa-tree-p-pass-no-study",q0],["esa-tree-p-fail-no-study",1-q0],
          ["esa-tree-joint-study-pass",sp],["esa-tree-joint-study-fail",sf],
          ["esa-tree-joint-no-study-pass",np],["esa-tree-joint-no-study-fail",nf],
          ["esa-tree-multiply",sp],["esa-tree-total-pass",overall]
        ];
        cells.forEach(([id,value])=>display(id,value));
        field("esa-tree-bayes").textContent=overall>0?(sp/overall).toFixed(4):"Undefined";
        field("esa-tree-undefined-note").hidden=overall>0;
      }
      [study,passStudy,passNoStudy].forEach(control=>control.addEventListener("input",update));
      field("esa-tree-reset").addEventListener("click",()=>{
        study.value="0.6";passStudy.value="0.9";passNoStudy.value="0.4";update();
      });
      update();
    })();
    </script>

    <h2>Extending to Three Events</h2>

    <p>
      The multiplication rule can be extended beyond two events.
    </p>

    <p>
      For three events:
    </p>

    
    \[
    P(A\cap B\cap C)=P(A)\,P(B\mid A)\,P(C\mid A\cap B)
    \]


    <p>
      Each step conditions on the events that have already occurred. The displayed conditional factors require P(A) &gt; 0 and P(A ∩ B) &gt; 0. If a conditioning event has probability zero, use an appropriate unconditional formulation instead.
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