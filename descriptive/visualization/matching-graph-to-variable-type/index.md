---
layout: default
title: Matching Graph to Variable Type
description: Learn how the type of variable determines which graph should be used and why choosing the wrong graph can mislead interpretation.
permalink: /descriptive/visualization/matching-graph-to-variable-type/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_visualization_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/visualization/matching-graph-to-variable-type/",
    label: "Matching Graph to Variable Type",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->
<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 3</span>
      <span class="badge">Visualization</span>
      <span class="badge">Graph Selection</span>
    </div>

    <h1>Matching Graph to Variable Type</h1>

    <p class="lead">
      One of the most important decisions in data visualization
      is choosing the correct graph.
    </p>

    <p class="lead">
      The best graph depends primarily on the type of variable being analyzed.
      Using the wrong graph can hide patterns,
      distort comparisons,
      and create misleading conclusions.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/visualization/why-visualization-matters/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/visualization/bar-charts/">
         Next: Bar Charts →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>Why Graph Selection Matters</h2>

    <p>
      Every graph emphasizes certain features of data.
    </p>

    <p>
      Some graphs are designed for:
    </p>

    <ul class="bullets">

      <li>Comparisons</li>

      <li>Distributions</li>

      <li>Trends</li>

      <li>Relationships</li>

      <li>Composition</li>

    </ul>

    <p>
      Selecting an appropriate graph begins with understanding
      the variable being displayed.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Variable type should guide graph choice.
      </p>

    </div>

    <p>
  Variable type is the starting point,
  but the purpose of the analysis also matters.
</p>

<p>
  The same variable may be displayed differently
  depending on whether the goal is comparison,
  distribution analysis,
  or trend detection.
</p>

    <h2>Start With the Variable Type</h2>

    <p>
      Earlier lessons introduced:
    </p>

    <ul class="bullets">

      <li>Categorical variables</li>

      <li>Numerical variables</li>

      <li>Discrete variables</li>

      <li>Continuous variables</li>

    </ul>

    <p>
      Different variable types require different visualizations.
    </p>

    <img src="{{ 'descriptive/images/variable-type-graph-selection.png' | relative_url }}"
     alt="Choosing graphs based on variable type"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Variable type provides the starting point for selecting an appropriate graph.
</p>

    <div class="concept-box">

  <strong>Important insight:</strong>

  <p>
    Good graph selection begins with understanding
    both the data type and the question being asked.
  </p>

</div>

    <h2>Categorical Variables</h2>

    <p>
      Categorical variables classify observations into groups.
    </p>

    <p>
      Examples:
    </p>

    <ul class="bullets">

      <li>Blood type</li>

      <li>Political party</li>

      <li>Major field of study</li>

      <li>Favorite sport</li>

    </ul>

    <p>
      The goal is usually to compare category frequencies or percentages.
    </p>

    <p>
      Common graphs:
    </p>

    <ul class="bullets">

      <li>Bar charts</li>

      <li>Pie charts</li>

    </ul>

    <h2>Example: Categorical Data</h2>

    <p>
      Student majors:
    </p>

    0

    <p>
      A bar chart clearly compares category sizes.
    </p>

    <h2>Numerical Variables</h2>

    <p>
      Numerical variables represent measurable quantities.
    </p>

    <p>
      Examples:
    </p>

    <ul class="bullets">

      <li>Age</li>

      <li>Income</li>

      <li>Height</li>

      <li>Weight</li>

      <li>Exam score</li>

    </ul>

    <p>
      The goal is often to understand how values are distributed.
    </p>

    <p>
      Common graphs:
    </p>

    <ul class="bullets">

      <li>Histograms</li>

      <li>Boxplots</li>

      <li>Dot plots</li>

    </ul>

    <h2>Discrete Numerical Variables</h2>

    <p>
      Discrete variables take separate countable values.
    </p>

    <p>
      Examples:
    </p>

    <ul class="bullets">

      <li>Number of children</li>

      <li>Number of defects</li>

      <li>Number of books owned</li>

    </ul>

    <p>
      Graph choices often include:
    </p>

    <ul class="bullets">

      <li>Bar charts</li>

      <li>Histograms</li>

    </ul>

    <p>
      The best choice depends on the number of distinct values.
    </p>

    <p>
  When only a few distinct values exist,
  bar charts are often easier to interpret.
  Histograms become more useful when many numerical values are present.
</p>

    <h2>Continuous Numerical Variables</h2>

    <p>
      Continuous variables can take many possible values.
    </p>

    <p>
      Examples:
    </p>

    <ul class="bullets">

      <li>Height</li>

      <li>Weight</li>

      <li>Reaction time</li>

      <li>Temperature</li>

    </ul>

    <p>
      Common graphs:
    </p>

    <ul class="bullets">

      <li>Histograms</li>

      <li>Density plots</li>

      <li>Boxplots</li>

    </ul>

    <p>
      These graphs focus on distribution shape.
    </p>

    <h2>Time-Based Variables</h2>

    <p>
      When observations are collected over time,
      preserving order becomes important.
    </p>

    <p>
      Examples:
    </p>

    <ul class="bullets">

      <li>Monthly sales</li>

      <li>Daily temperatures</li>

      <li>Annual population growth</li>

    </ul>

    <p>
      The most common graph is:
    </p>

    <ul class="bullets">
      <li>Line chart</li>
    </ul>

    <p>
      Line charts emphasize change through time.
    </p>

    <h2>Example: Time Series Data</h2>

    1

    <h2>Two Numerical Variables</h2>

    <p>
      Sometimes we want to study relationships between variables.
    </p>

    <p>
      Examples:
    </p>

    <ul class="bullets">

      <li>Height and weight</li>

      <li>Advertising and sales</li>

      <li>Study hours and exam score</li>

    </ul>

    <p>
      The standard graph is:
    </p>

    <ul class="bullets">
      <li>Scatterplot</li>
    </ul>

    <p>
      Scatterplots reveal relationships,
      trends,
      and clusters.
    </p>

    <h2>Composition Data</h2>

    <p>
      Sometimes the goal is to show parts of a whole.
    </p>

    <p>
      Examples:
    </p>

    <ul class="bullets">

      <li>Market share</li>

      <li>Budget allocation</li>

      <li>Survey response proportions</li>

    </ul>

    <p>
      Common graphs:
    </p>

    <ul class="bullets">

      <li>Pie charts</li>

      <li>Stacked bar charts</li>

    </ul>

    <p>
      However,
      many statisticians prefer bar charts because comparisons are easier.
    </p>

    <p>
  Pie charts can become difficult to interpret
  when many categories are displayed.
</p>

    <h2>A Simple Graph Selection Guide</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Goal</th>
            <th>Common Graph</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Compare categories</td>
            <td>Bar chart</td>
          </tr>

          <tr>
            <td>Show parts of a whole</td>
            <td>Pie chart</td>
          </tr>

          <tr>
            <td>Show a distribution</td>
            <td>Histogram</td>
          </tr>

          <tr>
            <td>Show change over time</td>
            <td>Line chart</td>
          </tr>

          <tr>
            <td>Show relationships</td>
            <td>Scatterplot</td>
          </tr>

          <tr>
            <td>Summarize spread</td>
            <td>Boxplot</td>
          </tr>

        </tbody>

      </table>

    </div>

    <img src="{{ 'descriptive/images/common-graph-types-overview.png' | relative_url }}"
     alt="Common graph types overview"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Different graphs are designed to answer different statistical questions.
</p>

    <h2>Common Mistake: Choosing Based on Appearance</h2>

    <p>
      Beginners often choose graphs because they look attractive.
    </p>

    <p>
      Good visualization is not about decoration.
    </p>

    <p>
      It is about communicating information accurately.
    </p>

    <p>
      The best graph is the one that answers the statistical question most clearly.
    </p>

    <img src="{{ 'descriptive/images/wrong-vs-correct-graph-choice.png' | relative_url }}"
     alt="Wrong versus correct graph choice"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
The same data can be easier or harder to interpret depending on graph selection.
</p>

    <h2>Think About the Question First</h2>

    <p>
      Before creating a graph,
      ask:
    </p>

    <ul class="bullets">

      <li>What type of variable do I have?</li>

      <li>What pattern am I trying to see?</li>

      <li>What comparison matters most?</li>

      <li>Who will read this graph?</li>

    </ul>

    <p>
      Answering these questions usually points to the correct visualization.
    </p>

    <div class="concept-box">

  <strong>Key insight:</strong>

  <p>
    There is no universally best graph.
    The best graph depends on the variable,
    the question,
    and the message being communicated.
  </p>

</div>

<h2>Optional: Choosing Graphs in SPSS</h2>

<ul class="bullets">
  <li>Graphs → Chart Builder</li>
  <li>SPSS recommends graph types based on selected variables</li>
  <li>Analysts should still verify that the graph matches the statistical question</li>
</ul>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Variable type is the primary factor in graph selection</li>

        <li>Categorical variables are commonly displayed with bar charts</li>

        <li>Numerical variables are often displayed with histograms and boxplots</li>

        <li>Time-based data is usually displayed with line charts</li>

        <li>Relationships between numerical variables are shown with scatterplots</li>

        <li>Different graphs answer different statistical questions</li>

        <li>The best graph communicates information clearly and accurately</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/visualization/why-visualization-matters/">
         ← Previous: Why Visualization Matters
      </a>

      <a class="btn"
         href="/descriptive/visualization/bar-charts/">
         Next: Bar Charts →
      </a>

    </div>

  </div>

</section>
