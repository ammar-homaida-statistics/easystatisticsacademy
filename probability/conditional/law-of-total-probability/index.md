---
layout: default
title: Law of Total Probability
description: Learn how to calculate probabilities by combining multiple possible pathways that lead to an event.
permalink: /probability/conditional/law-of-total-probability/
sidebar: false
translation_pair: law-of-total-probability
math: true
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_conditional_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/conditional/law-of-total-probability/",
    label: "Law of Total Probability",
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
      <span class="badge">Core Theorem</span>
    </div>

    <h1>Law of Total Probability</h1>
<p><a href="/ar/probability/conditional/law-of-total-probability/" lang="ar" dir="rtl">اقرأ الدرس باللغة العربية</a></p>

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

    \[
P(A)=P(A\cap B)+P(A\cap B^{c})
\]

    <h2>Applying the Multiplication Rule</h2>

    <p>
      Using the multiplication rule:
    </p>

    \[
P(A)=P(A\mid B)P(B)+P(A\mid B^{c})P(B^{c})
\]

    <p>
      This is the simplest form of the Law of Total Probability.
      The conditional probabilities require P(B) &gt; 0 and
      P(Bᶜ) &gt; 0; a zero-probability pathway contributes zero
      and should be omitted from the conditional-probability sum.
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

    \[
P(\text{Pass})=P(\text{Pass}\mid\text{Study})P(\text{Study})
+P(\text{Pass}\mid\text{No Study})P(\text{No Study})
\]

    <p>
      Therefore:
    </p>

    \[
P(\text{Pass})=0.90(0.60)+0.40(0.40)=0.54+0.16=0.70
\]

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

    <!-- Batch #74: same shared calculation engine across Arabic and English -->
<section class="concept-box" id="esa-total-probability-lab" aria-labelledby="esa-tp-heading">
<h2 id="esa-tp-heading">Interactive Law of Total Probability: Three Groups</h2>
<p>Model a mutually exclusive, exhaustive partition into three groups. Set each group weight P(Bᵢ) and its conditional event probability P(A|Bᵢ). All group weights must sum to 1.</p>
<div class="esa-tp-grid">
<div><label for="esa-tp-w1">Group 1 weight</label><input id="esa-tp-w1" dir="ltr" type="number" min="0" max="1" step="any" value="0.2"></div>
<div><label for="esa-tp-w2">Group 2 weight</label><input id="esa-tp-w2" dir="ltr" type="number" min="0" max="1" step="any" value="0.3"></div>
<div><label for="esa-tp-w3">Group 3 weight</label><input id="esa-tp-w3" dir="ltr" type="number" min="0" max="1" step="any" value="0.5"></div>
<div><label for="esa-tp-p1">P(A | Group 1)</label><input id="esa-tp-p1" dir="ltr" type="number" min="0" max="1" step="any" value="0.1"></div>
<div><label for="esa-tp-p2">P(A | Group 2)</label><input id="esa-tp-p2" dir="ltr" type="number" min="0" max="1" step="any" value="0.5"></div>
<div><label for="esa-tp-p3">P(A | Group 3)</label><input id="esa-tp-p3" dir="ltr" type="number" min="0" max="1" step="any" value="0.8"></div>
</div>
<button type="button" class="btn btn-outline" id="esa-tp-reset">Restore worked example</button>
<p id="esa-tp-error" role="alert" aria-live="assertive" hidden></p>
<section id="esa-tp-results" aria-live="polite" aria-label="Total probability results">
<div class="table-wrap"><table><caption>Three contributions (six decimal places)</caption><tbody>
<tr><th scope="row">Sum of partition weights</th><td id="esa-tp-sum">—</td></tr>
<tr><th scope="row">Group 1 contribution</th><td id="esa-tp-c1">—</td></tr>
<tr><th scope="row">Group 2 contribution</th><td id="esa-tp-c2">—</td></tr>
<tr><th scope="row">Group 3 contribution</th><td id="esa-tp-c3">—</td></tr>
<tr><th scope="row">Total probability P(A)</th><td id="esa-tp-total">—</td></tr>
</tbody></table></div>
<svg id="esa-tp-chart" role="img" viewBox="0 0 610 270" dir="ltr" aria-label="Three probability contributions"></svg>
<p id="esa-tp-explain"></p>
<p class="muted-mini">A group with zero weight contributes zero; its within-group probability is treated as an illustrative model input, not estimated from observations in an empty group.</p>
</section>
</section>
<style>
#esa-total-probability-lab,#esa-total-probability-lab *{box-sizing:border-box}
#esa-total-probability-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-total-probability-lab .esa-tp-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:12px 0}
#esa-total-probability-lab label{display:block;font-weight:650}
#esa-total-probability-lab input{display:block;margin-top:5px;padding:10px;border:1px solid #777;border-radius:7px;font:inherit;width:100%;min-width:0}
#esa-total-probability-lab [hidden]{display:none!important}
#esa-total-probability-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-total-probability-lab svg{display:block;max-width:100%;height:auto;width:100%}
#esa-total-probability-lab :is(button,input):focus-visible{outline:2px solid #0f766e;outline-offset:3px}
@media(max-width:600px){#esa-total-probability-lab .esa-tp-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/total-probability-explorer.js"></script>
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
      form a partition of the sample space: they are mutually exclusive
      and collectively exhaustive. For the conditional form shown,
      assume P(Bᵢ) &gt; 0 for each included pathway; omit
      zero-probability pathways.
    </p>

    <p>
      Then:
    </p>

    \[
P(A)=\sum_{i=1}^{m}P(A\mid B_i)P(B_i)
\]

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