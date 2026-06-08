---
layout: default
title: Choosing the Right Graph
description: Learn a systematic approach for selecting the most appropriate graph for any dataset and statistical question.
permalink: /descriptive/visualization/choosing-the-right-graph/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_visualization_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/visualization/choosing-the-right-graph/",
    label: "Choosing the Right Graph",
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
      <span class="badge">Final Lesson</span>
    </div>

    <h1>Choosing the Right Graph</h1>

    <p class="lead">
      A graph is only useful if it helps answer a statistical question.
    </p>

    <p class="lead">
      Throughout this block you learned many visualization tools.
      The final challenge is knowing which graph to use,
      when to use it,
      and why.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/visualization/misleading-graphs/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/center/">
         Next Block: Center →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>The Most Important Rule</h2>

    <p>
      Never choose a graph because it looks attractive.
    </p>

    <p>
      Choose a graph because it answers the statistical question clearly.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The correct graph depends on the type of data and the purpose of the analysis.
      </p>

    </div>

    <h2>Start With the Question</h2>

    <p>
      Before creating any graph,
      ask:
    </p>

    <ul class="bullets">

      <li>What am I trying to learn?</li>

      <li>What type of variable do I have?</li>

      <li>How many variables are involved?</li>

      <li>Am I comparing, describing, or exploring relationships?</li>

    </ul>

    <p>
      These questions usually determine the best visualization.
    </p>

    <h2>Step 1: Identify the Variable Type</h2>

    <p>
      Visualization begins with understanding the data.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Variable Type</th>
            <th>Examples</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Categorical</td>
            <td>Blood type, major, gender</td>
          </tr>

          <tr>
            <td>Numerical</td>
            <td>Age, income, height</td>
          </tr>

          <tr>
            <td>Time-based</td>
            <td>Monthly sales, stock prices</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Different variable types require different visualizations.
    </p>

    <h2>Graphs for Categorical Variables</h2>

    <p>
      If the variable is categorical,
      the primary goal is usually comparison.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Goal</th>
            <th>Recommended Graph</th>
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

        </tbody>

      </table>

    </div>

    <p>
      In most situations,
      statisticians prefer bar charts because comparisons are easier.
    </p>

    <h2>Graphs for Numerical Variables</h2>

    <p>
      If the variable is numerical,
      the goal is often understanding the distribution.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Goal</th>
            <th>Recommended Graph</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Distribution shape</td>
            <td>Histogram</td>
          </tr>

          <tr>
            <td>Smoothed distribution</td>
            <td>Density curve</td>
          </tr>

          <tr>
            <td>Compact summary</td>
            <td>Boxplot</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Graphs for Relationships</h2>

    <p>
      If two numerical variables are being studied,
      the goal is usually understanding association.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Question</th>
            <th>Recommended Graph</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Relationship between two variables</td>
            <td>Scatterplot</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Scatterplots reveal direction,
      strength,
      clusters,
      and outliers.
    </p>

    <h2>Graphs for Time-Based Data</h2>

    <p>
      When time is involved,
      preserving order becomes essential.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Question</th>
            <th>Recommended Graph</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Change over time</td>
            <td>Line chart</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Line charts reveal trends,
      seasonality,
      cycles,
      and unusual events.
    </p>

    <h2>A Practical Decision Guide</h2>

    <div class="grid grid-2">

      <div class="card">

        <h3>One Categorical Variable</h3>

        <ul class="bullets">
          <li>Bar chart</li>
          <li>Pie chart</li>
        </ul>

      </div>

      <div class="card">

        <h3>One Numerical Variable</h3>

        <ul class="bullets">
          <li>Histogram</li>
          <li>Density curve</li>
          <li>Boxplot</li>
        </ul>

      </div>

      <div class="card">

        <h3>Two Numerical Variables</h3>

        <ul class="bullets">
          <li>Scatterplot</li>
        </ul>

      </div>

      <div class="card">

        <h3>Time Series</h3>

        <ul class="bullets">
          <li>Line chart</li>
        </ul>

      </div>

    </div>

    <h2>The Same Data Can Have Different Graphs</h2>

    <p>
      A single dataset may be visualized in multiple ways.
    </p>

    <p>
      Example:
    </p>

    <ul class="bullets">

      <li>Histogram → detailed shape</li>

      <li>Density curve → smooth shape</li>

      <li>Boxplot → concise summary</li>

    </ul>

    <p>
      The best choice depends on what you want to communicate.
    </p>

    <h2>Think About the Audience</h2>

    <p>
      Different audiences need different visualizations.
    </p>

    <ul class="bullets">

      <li>Researchers may prefer detailed distributions</li>

      <li>Managers may prefer concise summaries</li>

      <li>General audiences may prefer simple comparisons</li>

    </ul>

    <p>
      Effective communication considers the reader.
    </p>

    <h2>Common Mistakes in Graph Selection</h2>

    <ul class="bullets">

      <li>Using pie charts with many categories</li>

      <li>Using bar charts for continuous distributions</li>

      <li>Using line charts for unordered categories</li>

      <li>Using scatterplots for categorical data</li>

      <li>Choosing a graph for appearance rather than clarity</li>

    </ul>

    <p>
      These mistakes often make interpretation more difficult.
    </p>

    <h2>There Is Rarely a Perfect Graph</h2>

    <p>
      Visualization involves trade-offs.
    </p>

    <p>
      Some graphs emphasize:
    </p>

    <ul class="bullets">

      <li>Detail</li>

      <li>Simplicity</li>

      <li>Comparison</li>

      <li>Distribution shape</li>

      <li>Relationships</li>

    </ul>

    <p>
      The goal is selecting the graph that best serves the purpose of the analysis.
    </p>

    <h2>The Statistical Workflow</h2>

    <p>
      The lessons in this block reflect a common workflow:
    </p>

    <ul class="bullets">

      <li>Understand the data</li>

      <li>Create tables</li>

      <li>Create visualizations</li>

      <li>Explore patterns</li>

      <li>Summarize the distribution</li>

      <li>Draw conclusions</li>

    </ul>

    <p>
      Good graph selection is a critical step in this process.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Visualization helps us see distributions,
      but statisticians also need numerical summaries.
    </p>

    <p>
      The next block introduces measures of center,
      including:
    </p>

    <ul class="bullets">

      <li>Mean</li>

      <li>Median</li>

      <li>Mode</li>

    </ul>

    <p>
      These measures help quantify where data tend to be located.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Block 3 Takeaways</h2>

      <ul class="bullets">

        <li>Graph choice depends on the statistical question</li>

        <li>Variable type is the starting point for graph selection</li>

        <li>Bar charts compare categories</li>

        <li>Histograms, density curves, and boxplots describe distributions</li>

        <li>Scatterplots reveal relationships</li>

        <li>Line charts reveal changes through time</li>

        <li>Good visualizations communicate information clearly and honestly</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/visualization/misleading-graphs/">
         ← Previous: Misleading Graphs
      </a>

      <a class="btn"
         href="/descriptive/center/">
         Next Block: Center →
      </a>

    </div>

  </div>

</section>