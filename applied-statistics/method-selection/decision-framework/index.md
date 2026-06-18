---
layout: default
title: Decision Framework
description: Learn a practical framework for selecting statistical methods by combining research questions, variable types, study goals, and analytical objectives.
permalink: /applied-statistics/method-selection/decision-framework/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_applied_statistics_method_selection_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/applied-statistics/method-selection/decision-framework/",
    label: "Decision Framework",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Applied Statistics</span>
      <span class="badge">Block 1</span>
      <span class="badge">Method Selection</span>
      <span class="badge">Decision Making</span>
    </div>

    <h1>Decision Framework</h1>

    <p class="lead">
      By now, you have seen that method selection depends on research questions, variable types, study goals, and analytical objectives.
    </p>

    <p class="lead">
      Rather than memorizing individual statistical tests, analysts often rely on a structured decision-making process.
    </p>

    <p class="lead">
      A decision framework helps move systematically from a research question to an appropriate statistical method.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/applied-statistics/method-selection/common-tests/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/applied-statistics/study-design/">
         Next: Study Design →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Use a Framework?</h2>

    <p>
      New analysts often ask:
    </p>

    <div class="example-box">

      <p>
        Which statistical test should I use?
      </p>
    </div>

    <p>
      Unfortunately, there is rarely a simple answer.
    </p>

    <p>
      Statistical methods depend on multiple factors, and choosing a method without considering those factors can lead to incorrect conclusions.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Method selection is most effective when approached as a structured decision process rather than a memorization exercise.
      </p>

    </div>

    <h2>The Four Key Questions</h2>

    <p>
      A practical decision framework begins with four questions:
    </p>

    <ol>

      <li>What is the research question?</li>

      <li>What types of variables are involved?</li>

      <li>Am I comparing groups or studying relationships?</li>

      <li>What assumptions are reasonable?</li>

    </ol>

    <p>
      These questions often narrow the range of appropriate methods considerably.
    </p>

    <h2>Step 1: Clarify the Question</h2>

    <p>
      Statistical methods are designed to answer specific types of questions.
    </p>

    <p>
      Common objectives include:
    </p>

    <ul class="bullets">

      <li>Description</li>

      <li>Comparison</li>

      <li>Association</li>

      <li>Prediction</li>

      <li>Explanation</li>

    </ul>

    <p>
      Defining the objective is the first step in choosing a method.
    </p>

    <h2>Step 2: Identify Variable Types</h2>

    <p>
      Next, determine whether variables are:
    </p>

    <ul class="bullets">

      <li>Categorical</li>

      <li>Ordinal</li>

      <li>Binary</li>

      <li>Discrete</li>

      <li>Continuous</li>

    </ul>

    <p>
      Variable types strongly influence which methods are appropriate.
    </p>

    <h2>Step 3: Determine the Analytical Goal</h2>

    <p>
      Ask whether the analysis focuses primarily on:
    </p>

    <ul class="bullets">

      <li>Differences between groups</li>

      <li>Relationships between variables</li>

    </ul>

    <p>
      This distinction often separates comparison methods from relationship methods.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Many statistical methods can be grouped according to whether they analyze differences or associations.
      </p>

    </div>

    <h2>Step 4: Consider Assumptions</h2>

    <p>
      Every statistical procedure relies on assumptions.
    </p>

    <p>
      Common assumptions include:
    </p>

    <ul class="bullets">

      <li>Independent observations</li>

      <li>Normality</li>

      <li>Equal variances</li>

      <li>Linearity</li>

    </ul>

    <p>
      Methods should be selected with these assumptions in mind.
    </p>

    <h2>A Simple Decision Path</h2>

    <p>
      Consider the following workflow:
    </p>

    <div class="example-box">

      <p>
        Research Question
        <br>
        ↓
        <br>
        Variable Types
        <br>
        ↓
        <br>
        Comparison or Relationship
        <br>
        ↓
        <br>
        Assumptions
        <br>
        ↓
        <br>
        Statistical Method
      </p>
    </div>

    <p>
      This sequence provides a useful roadmap for many introductory analyses.
    </p>

    <h2>Example: Comparing Two Groups</h2>

    <p>
      Suppose the question is:
    </p>

    <div class="example-box">

      <p>
        Do two teaching methods produce different exam scores?
      </p>
    </div>

    <p>
      Applying the framework:
    </p>

    <ul class="bullets">

      <li>Question type → Comparison</li>

      <li>Grouping variable → Categorical</li>

      <li>Outcome variable → Continuous</li>

      <li>Common method → t-test</li>

    </ul>

    <p>
      The framework naturally leads toward an appropriate procedure.
    </p>

    <h2>Example: Studying a Relationship</h2>

    <p>
      Suppose the question is:
    </p>

    <div class="example-box">

      <p>
        Is study time related to exam performance?
      </p>
    </div>

    <p>
      Applying the framework:
    </p>

    <ul class="bullets">

      <li>Question type → Relationship</li>

      <li>Study time → Continuous</li>

      <li>Exam score → Continuous</li>

      <li>Common methods → Correlation or Regression</li>

    </ul>

    <p>
      Again, the framework narrows the choices.
    </p>

    <h2>Example: Binary Outcomes</h2>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        Can age and exercise habits predict disease status?
      </p>
    </div>

    <p>
      Applying the framework:
    </p>

    <ul class="bullets">

      <li>Question type → Prediction</li>

      <li>Outcome → Binary</li>

      <li>Predictors → Numerical and categorical</li>

      <li>Common method → Logistic Regression</li>

    </ul>

    <p>
      Outcome type becomes especially important in these situations.
    </p>

    <h2>Decision Trees for Method Selection</h2>

    <p>
      Many textbooks and software packages provide statistical decision trees.
    </p>

    <p>
      These tools use a series of questions to guide method selection.
    </p>

    <p>
      Although useful, they work best when users understand the underlying reasoning.
    </p>

    <h2>Why Memorization Is Not Enough</h2>

    <p>
      Memorizing lists of tests can be helpful initially.
    </p>

    <p>
      However, real-world analyses often involve:
    </p>

    <ul class="bullets">

      <li>Complex designs</li>

      <li>Multiple variables</li>

      <li>Violations of assumptions</li>

      <li>Mixed data types</li>

    </ul>

    <p>
      Flexible reasoning is more valuable than memorization alone.
    </p>

    <h2>The Importance of Context</h2>

    <p>
      Statistical methods should never be chosen in isolation from the research context.
    </p>

    <p>
      Analysts should always consider:
    </p>

    <ul class="bullets">

      <li>Study objectives</li>

      <li>Data quality</li>

      <li>Measurement processes</li>

      <li>Practical constraints</li>

    </ul>

    <p>
      Good method selection combines statistical knowledge with subject-matter understanding.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        Method selection is not about finding the most advanced technique. It is about finding the most appropriate technique for the question and data.
      </p>

    </div>

    <h2>A Reusable Workflow</h2>

    <p>
      The framework introduced in this lesson can be applied repeatedly:
    </p>

    <ol>

      <li>Define the question.</li>

      <li>Identify variable types.</li>

      <li>Determine the analytical goal.</li>

      <li>Review assumptions.</li>

      <li>Select an appropriate method.</li>

      <li>Evaluate results.</li>

    </ol>

    <p>
      This process remains useful even as analyses become more sophisticated.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Method selection is one of the most important decisions in applied statistics.
    </p>

    <p>
      Analysts who use a structured decision framework are more likely to choose suitable methods, avoid common mistakes, and produce reliable conclusions.
    </p>

    <p>
      A strong framework transforms method selection from guesswork into a logical process.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Effective method selection follows a structured process that considers research questions, variable types, analytical goals, and assumptions. This framework helps analysts move logically from questions to appropriate statistical methods.
      </p>

    </div>

    <h2>Completing the Method Selection Block</h2>

    <p>
      You have now completed the Method Selection block.
    </p>

    <p>
      In this block, you learned how research questions, variable types, analytical goals, and common statistical methods fit together.
    </p>

    <p>
      These concepts provide the foundation for choosing appropriate analyses and understanding why particular methods are used.
    </p>

    <p>
      The next block shifts focus from method selection to study design, where you will learn how data are generated, how studies are structured, and how design decisions influence statistical conclusions.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Method selection should follow a structured decision process</li>

        <li>Research questions guide analytical choices</li>

        <li>Variable types strongly influence method selection</li>

        <li>Comparison and relationship questions often require different approaches</li>

        <li>Assumptions must be considered before selecting a method</li>

        <li>Decision frameworks reduce method-selection errors</li>

        <li>Context and study goals are essential considerations</li>

        <li>Appropriate methods are more important than complex methods</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/applied-statistics/method-selection/common-tests/">
         ← Previous: Common Tests
      </a>

      <a class="btn"
         href="/applied-statistics/study-design/">
         Next: Study Design →
      </a>

    </div>

  </div>

</section>