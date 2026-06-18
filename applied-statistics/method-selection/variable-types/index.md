---
layout: default
title: Variable Types
description: Learn how different variable types influence statistical analysis and why identifying variable types is one of the most important steps in method selection.
permalink: /applied-statistics/method-selection/variable-types/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_applied_statistics_method_selection_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/applied-statistics/method-selection/variable-types/",
    label: "Variable Types",
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
      <span class="badge">Variables</span>
    </div>

    <h1>Variable Types</h1>

    <p class="lead">
      Once a research question has been defined, one of the first tasks is identifying the types of variables involved.
    </p>

    <p class="lead">
      Variable type strongly influences which statistical methods can be used and how results should be interpreted.
    </p>

    <p class="lead">
      Many method-selection decisions begin with understanding whether variables are categorical, numerical, binary, ordinal, or continuous.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/applied-statistics/method-selection/research-questions/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/applied-statistics/method-selection/comparisons-vs-relationships/">
         Next: Comparisons vs Relationships →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Variable Types Matter</h2>

    <p>
      Statistical methods are designed for particular types of data.
    </p>

    <p>
      A method that works well for numerical measurements may be inappropriate for categories or rankings.
    </p>

    <p>
      Before choosing a statistical procedure, analysts must determine what kind of variables they have.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Correctly identifying variable types is one of the most important steps in selecting an appropriate statistical method.
      </p>

    </div>

    <h2>What Is a Variable?</h2>

    <p>
      A variable is any characteristic that can differ across observations.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Age</li>

      <li>Income</li>

      <li>Height</li>

      <li>Gender</li>

      <li>Education level</li>

      <li>Blood pressure</li>

    </ul>

    <p>
      Variables provide the information that statistical analyses use to answer research questions.
    </p>

    <h2>The Two Broad Categories</h2>

    <p>
      Most variables can be placed into two broad groups:
    </p>

    <ul class="bullets">

      <li>Categorical variables</li>

      <li>Numerical variables</li>

    </ul>

    <p>
      Many additional classifications are refinements of these two fundamental categories.
    </p>

    <h2>Categorical Variables</h2>

    <p>
      Categorical variables classify observations into groups or categories.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Country</li>

      <li>Blood type</li>

      <li>Marital status</li>

      <li>Political party</li>

    </ul>

    <p>
      The values represent labels rather than numerical quantities.
    </p>

    <h2>Nominal Variables</h2>

    <p>
      Nominal variables are categorical variables with no natural ordering.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Eye color</li>

      <li>Nationality</li>

      <li>Product category</li>

      <li>Blood type</li>

    </ul>

    <p>
      No category is inherently larger or smaller than another.
    </p>

    <h2>Ordinal Variables</h2>

    <p>
      Ordinal variables have categories with a meaningful order.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Education level</li>

      <li>Customer satisfaction ratings</li>

      <li>Socioeconomic status categories</li>

      <li>Survey agreement scales</li>

    </ul>

    <p>
      The categories can be ranked, but the spacing between categories may not be equal.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Ordinal variables contain more information than nominal variables because the ordering carries meaning.
      </p>

    </div>

    <h2>Binary Variables</h2>

    <p>
      Binary variables contain only two possible categories.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Yes / No</li>

      <li>Pass / Fail</li>

      <li>Disease / No Disease</li>

      <li>Purchased / Not Purchased</li>

    </ul>

    <p>
      Binary variables are extremely common in applied statistics.
    </p>

    <h2>Numerical Variables</h2>

    <p>
      Numerical variables represent quantities that can be measured or counted.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Age</li>

      <li>Income</li>

      <li>Weight</li>

      <li>Exam score</li>

    </ul>

    <p>
      Arithmetic operations on these values are meaningful.
    </p>

    <h2>Discrete Variables</h2>

    <p>
      Discrete variables take separate countable values.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Number of children</li>

      <li>Number of purchases</li>

      <li>Number of accidents</li>

      <li>Number of visits</li>

    </ul>

    <p>
      These variables often represent counts.
    </p>

    <h2>Continuous Variables</h2>

    <p>
      Continuous variables can theoretically take any value within a range.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Height</li>

      <li>Weight</li>

      <li>Temperature</li>

      <li>Reaction time</li>

    </ul>

    <p>
      Continuous measurements are common in scientific research.
    </p>

    <h2>Examples of Variable Classification</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Variable</th>
            <th>Type</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Gender</td>
            <td>Binary Categorical</td>
          </tr>

          <tr>
            <td>Income</td>
            <td>Continuous Numerical</td>
          </tr>

          <tr>
            <td>Customer Rating (1–5)</td>
            <td>Ordinal</td>
          </tr>

          <tr>
            <td>Number of Purchases</td>
            <td>Discrete Numerical</td>
          </tr>

          <tr>
            <td>Blood Type</td>
            <td>Nominal</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Variable Types and Method Selection</h2>

    <p>
      The types of variables involved often determine which methods are appropriate.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Variables</th>
            <th>Possible Methods</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Categorical vs Categorical</td>
            <td>Chi-square tests</td>
          </tr>

          <tr>
            <td>Numerical vs Numerical</td>
            <td>Correlation, Regression</td>
          </tr>

          <tr>
            <td>Categorical vs Numerical</td>
            <td>t-tests, ANOVA</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      This is why identifying variable types is such an important first step.
    </p>

    <h2>Research Questions and Variables</h2>

    <p>
      Consider the question:
    </p>

    <div class="example-box">

      <p>
        Do exam scores differ between teaching methods?
      </p>
    </div>

    <p>
      Variables:
    </p>

    <ul class="bullets">

      <li>Teaching method → Categorical</li>

      <li>Exam score → Numerical</li>

    </ul>

    <p>
      The combination of variable types helps determine which methods are suitable.
    </p>

    <h2>Common Classification Mistakes</h2>

    <p>
      Analysts sometimes misclassify variables.
    </p>

    <p>
      Common examples include:
    </p>

    <ul class="bullets">

      <li>Treating categories as continuous measurements</li>

      <li>Ignoring ordinal structure</li>

      <li>Assuming numerical codes imply numerical meaning</li>

    </ul>

    <p>
      Variable coding and variable type are not always the same thing.
    </p>

    <div class="concept-box">

      <strong>Important warning:</strong>

      <p>
        A variable coded as numbers is not automatically a numerical variable.
      </p>

    </div>

    <h2>Thinking About Outcomes and Predictors</h2>

    <p>
      In many analyses, variables are also classified by their role.
    </p>

    <ul class="bullets">

      <li>Outcome variable</li>

      <li>Predictor variable</li>

    </ul>

    <p>
      Method selection often depends on both the type of variable and its role in the analysis.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Variable types provide a roadmap for statistical analysis.
    </p>

    <p>
      They determine which summaries are meaningful, which visualizations are useful, and which statistical methods are appropriate.
    </p>

    <p>
      Analysts who correctly identify variable types are far more likely to choose suitable analytical techniques.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Variable types are central to method selection. Understanding whether variables are categorical, ordinal, binary, discrete, or continuous helps analysts choose appropriate statistical procedures and interpret results correctly.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      After identifying variable types, the next step is determining what kind of question is being asked.
    </p>

    <p>
      Some analyses compare groups, while others examine relationships between variables.
    </p>

    <p>
      The next lesson explores the distinction between comparisons and relationships and shows how this distinction guides statistical method selection.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Variable type is one of the most important factors in method selection</li>

        <li>Variables are broadly classified as categorical or numerical</li>

        <li>Nominal variables have categories without order</li>

        <li>Ordinal variables contain meaningful rankings</li>

        <li>Binary variables contain two categories</li>

        <li>Numerical variables may be discrete or continuous</li>

        <li>Variable type helps determine appropriate statistical methods</li>

        <li>Correct classification improves analysis quality and interpretation</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/applied-statistics/method-selection/research-questions/">
         ← Previous: Research Questions
      </a>

      <a class="btn"
         href="/applied-statistics/method-selection/comparisons-vs-relationships/">
         Next: Comparisons vs Relationships →
      </a>

    </div>

  </div>

</section>