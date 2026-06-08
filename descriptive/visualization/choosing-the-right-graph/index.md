---
layout: default
title: Choosing the Right Graph
description: Learn how statisticians select appropriate graphs based on variable types, analytical goals, and the message they want to communicate.
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
      <span class="badge">Decision Making</span>
    </div>

    <h1>Choosing the Right Graph</h1>

    <p class="lead">
      Creating a graph is easy.
      Choosing the correct graph is the real statistical skill.
    </p>

    <p class="lead">
      Every graph highlights certain aspects of data and hides others.
      Good statisticians select visualizations based on the question being asked,
      the type of data available,
      and the message they want to communicate.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/visualization/misleading-graphs/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/center/why-center-matters/">
         Next Block: Center →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>The Goal Comes First</h2>

    <p>
      Many beginners start by asking:
    </p>

    <div class="example-box">
      <p>
        "Which graph should I make?"
      </p>
    </div>

    <p>
      Statisticians ask a different question:
    </p>

    <div class="example-box">
      <p>
        "What am I trying to learn from the data?"
      </p>
    </div>

    <p>
      The purpose of the analysis should always guide the choice of graph.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Choose the graph that best answers the statistical question.
      </p>

    </div>

    <h2>Step 1: Identify the Variable Type</h2>

    <p>
      The first step is determining what type of data you have.
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
            <td>Blood type, major, country</td>
          </tr>

          <tr>
            <td>Numerical</td>
            <td>Height, age, income</td>
          </tr>

          <tr>
            <td>Time Series</td>
            <td>Monthly sales, stock prices</td>
          </tr>

          <tr>
            <td>Two Numerical Variables</td>
            <td>Height and weight</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Variable type immediately narrows the appropriate graph choices.
    </p>

    <h2>Step 2: Identify the Goal</h2>

    <p>
      Different graphs answer different questions.
    </p>

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
            <td>Show proportions</td>
            <td>Pie chart</td>
          </tr>

          <tr>
            <td>Show distribution</td>
            <td>Histogram</td>
          </tr>

          <tr>
            <td>Summarize distribution</td>
            <td>Boxplot</td>
          </tr>

          <tr>
            <td>Show relationship</td>
            <td>Scatterplot</td>
          </tr>

          <tr>
            <td>Show change over time</td>
            <td>Line chart</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Graph Selection Framework</h2>

    <p>
      A useful way to think about graph selection is:
    </p>

    <div class="grid grid-2">

      <div class="card">

        <h3>What Data?</h3>

        <ul class="bullets">
          <li>Categorical?</li>
          <li>Numerical?</li>
          <li>Time-based?</li>
        </ul>

      </div>

      <div class="card">

        <h3>What Goal?</h3>

        <ul class="bullets">
          <li>Compare?</li>
          <li>Describe?</li>
          <li>Explore?</li>
          <li>Communicate?</li>
        </ul>

      </div>

    </div>

    <p>
      Once these questions are answered,
      the correct graph is often obvious.
    </p>

    <h2>When to Use a Bar Chart</h2>

    <p>
      Bar charts are ideal when:
    </p>

    <ul class="bullets">

      <li>Variables are categorical</li>

      <li>Comparisons are important</li>

      <li>Categories are independent</li>

      <li>Exact differences matter</li>

    </ul>

    <p>
      Examples:
    </p>

    <ul class="bullets">

      <li>Students by major</li>

      <li>Votes by candidate</li>

      <li>Products by sales category</li>

    </ul>

    <h2>When to Use a Pie Chart</h2>

    <p>
      Pie charts are appropriate when:
    </p>

    <ul class="bullets">

      <li>Categories form a meaningful whole</li>

      <li>Percentages sum to 100%</li>

      <li>There are few categories</li>

    </ul>

    <p>
      Example:
    </p>

    <ul class="bullets">

      <li>Budget allocation</li>

      <li>Market share</li>

      <li>Survey response percentages</li>

    </ul>

    <p>
      If precise comparison is important,
      bar charts are usually preferable.
    </p>

    <h2>When to Use a Histogram</h2>

    <p>
      Histograms are designed for numerical distributions.
    </p>

    <p>
      Use them when you want to understand:
    </p>

    <ul class="bullets">

      <li>Shape</li>

      <li>Spread</li>

      <li>Center</li>

      <li>Outliers</li>

      <li>Clusters</li>

    </ul>

    <p>
      Histograms answer:
    </p>

    <div class="example-box">
      <p>
        "How are the values distributed?"
      </p>
    </div>

    <h2>When to Use a Boxplot</h2>

    <p>
      Boxplots are useful when:
    </p>

    <ul class="bullets">

      <li>Comparing several groups</li>

      <li>Looking for outliers</li>

      <li>Summarizing distributions compactly</li>

    </ul>

    <p>
      They provide less detail than histograms
      but are often easier to compare across groups.
    </p>

    <h2>When to Use a Scatterplot</h2>

    <p>
      Scatterplots should be used when:
    </p>

    <ul class="bullets">

      <li>Two numerical variables exist</li>

      <li>You want to examine relationships</li>

      <li>You want to detect trends or clusters</li>

    </ul>

    <p>
      Scatterplots answer:
    </p>

    <div class="example-box">
      <p>
        "How do these variables move together?"
      </p>
    </div>

    <h2>When to Use a Line Chart</h2>

    <p>
      Line charts are best when:
    </p>

    <ul class="bullets">

      <li>Data are ordered through time</li>

      <li>Trends are important</li>

      <li>Change is the primary focus</li>

    </ul>

    <p>
      They answer:
    </p>

    <div class="example-box">
      <p>
        "How does this variable change over time?"
      </p>
    </div>

    <h2>A Practical Decision Table</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>If You Want To...</th>
            <th>Use...</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Compare categories</td>
            <td>Bar chart</td>
          </tr>

          <tr>
            <td>Show percentages of a whole</td>
            <td>Pie chart</td>
          </tr>

          <tr>
            <td>See a distribution</td>
            <td>Histogram</td>
          </tr>

          <tr>
            <td>Summarize a distribution</td>
            <td>Boxplot</td>
          </tr>

          <tr>
            <td>Study a relationship</td>
            <td>Scatterplot</td>
          </tr>

          <tr>
            <td>Track change over time</td>
            <td>Line chart</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>There Is Rarely One Perfect Graph</h2>

    <p>
      Multiple graphs may be useful for the same dataset.
    </p>

    <p>
      Example:
    </p>

    <ul class="bullets">

      <li>Histogram for shape</li>

      <li>Boxplot for summary</li>

      <li>Table for exact values</li>

    </ul>

    <p>
      Good statistical analysis often combines several tools.
    </p>

    <h2>The Best Graph Is the One That Answers the Question</h2>

    <p>
      Attractive graphics are not necessarily informative graphics.
    </p>

    <p>
      The best visualization:
    </p>

    <ul class="bullets">

      <li>Matches the variable type</li>

      <li>Matches the analytical goal</li>

      <li>Communicates clearly</li>

      <li>Avoids distortion</li>

      <li>Supports accurate interpretation</li>

    </ul>

    <p>
      Effective statistical communication always prioritizes understanding.
    </p>

    <h2>Completing the Visualization Block</h2>

    <p>
      You have now studied the major graphical tools used in descriptive statistics:
    </p>

    <ul class="bullets">

      <li>Bar charts</li>

      <li>Pie charts</li>

      <li>Histograms</li>

      <li>Density curves</li>

      <li>Boxplots</li>

      <li>Scatterplots</li>

      <li>Line charts</li>

      <li>Graph evaluation principles</li>

    </ul>

    <p>
      The next block moves from visual descriptions to numerical descriptions,
      beginning with measures of center.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Graph selection depends on both data type and analytical goal</li>

        <li>Bar charts compare categories</li>

        <li>Pie charts show parts of a whole</li>

        <li>Histograms display numerical distributions</li>

        <li>Boxplots summarize distributions efficiently</li>

        <li>Scatterplots reveal relationships between variables</li>

        <li>Line charts show changes through time</li>

        <li>The best graph is the one that answers the statistical question clearly</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/visualization/misleading-graphs/">
         ← Previous: Misleading Graphs
      </a>

      <a class="btn"
         href="/descriptive/center/why-center-matters/">
         Next Block: Why Center Matters →
      </a>

    </div>

  </div>

</section>