---
layout: default
title: Scatterplots
description: Learn how scatterplots visualize relationships between two numerical variables and help identify associations, trends, clusters, and outliers.
permalink: /descriptive/visualization/scatterplots/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_visualization_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/visualization/scatterplots/",
    label: "Scatterplots",
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
      <span class="badge">Relationships</span>
    </div>

    <h1>Scatterplots</h1>

    <p class="lead">
      Many statistical questions involve understanding relationships between variables.
    </p>

    <p class="lead">
      Scatterplots are the primary graphical tool for examining how two numerical variables move together,
      revealing patterns that may not be visible in tables or summary statistics.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/visualization/boxplots/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/visualization/time-series-line-charts/">
         Next: Time Series and Line Charts →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is a Scatterplot?</h2>

    <p>
      A <strong>scatterplot</strong>
      is a graph used to display the relationship between two numerical variables.
    </p>

    <p>
      Each observation is represented by a single point.
    </p>

    <p>
      The position of the point depends on the values of the two variables.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Every point represents one observation measured on two numerical variables.
      </p>

    </div>

    <h2>A Simple Example</h2>

    <p>
      Suppose we record study hours and exam scores for several students.
    </p>

    0

    <p>
      The pattern suggests that students who study more tend to achieve higher scores.
    </p>

    <h2>The Two Axes</h2>

    <p>
      Scatterplots contain two numerical axes.
    </p>

    <ul class="bullets">

      <li>Horizontal axis (x-axis)</li>

      <li>Vertical axis (y-axis)</li>

    </ul>

    <p>
      Each observation receives one value on each axis.
    </p>

    <p>
      Together,
      these values determine the point's location.
    </p>

    <h2>Why Scatterplots Matter</h2>

    <p>
      Many important statistical questions involve relationships.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Height and weight</li>

      <li>Age and income</li>

      <li>Advertising and sales</li>

      <li>Rainfall and crop yield</li>

      <li>Exercise and blood pressure</li>

    </ul>

    <p>
      Scatterplots allow these relationships to be visualized directly.
    </p>

    <h2>Positive Association</h2>

    <p>
      A <strong>positive association</strong>
      occurs when larger values of one variable tend to occur with larger values of another.
    </p>

    <p>
      Example:
    </p>

    <ul class="bullets">

      <li>Study time and exam score</li>

      <li>Experience and salary</li>

      <li>Advertising spending and sales</li>

    </ul>

    <p>
      Points tend to move upward as you move from left to right.
    </p>

    <h2>Negative Association</h2>

    <p>
      A <strong>negative association</strong>
      occurs when larger values of one variable tend to occur with smaller values of another.
    </p>

    <p>
      Examples:
    </p>

    <ul class="bullets">

      <li>Product price and demand</li>

      <li>Vehicle age and resale value</li>

      <li>Distance from signal source and signal strength</li>

    </ul>

    <p>
      Points tend to move downward as you move from left to right.
    </p>

    <h2>No Apparent Association</h2>

    <p>
      Sometimes variables show little or no visible relationship.
    </p>

    <p>
      In such cases,
      points appear scattered without any obvious pattern.
    </p>

    <p>
      Not all variables are related.
    </p>

    <h2>Direction of Association</h2>

    <p>
      Scatterplots help answer:
    </p>

    <ul class="bullets">

      <li>Is the relationship positive?</li>

      <li>Is the relationship negative?</li>

      <li>Is there no relationship?</li>

    </ul>

    <p>
      This is called the <strong>direction</strong> of association.
    </p>

    <h2>Strength of Association</h2>

    <p>
      Relationships may be:
    </p>

    <ul class="bullets">

      <li>Strong</li>

      <li>Moderate</li>

      <li>Weak</li>

    </ul>

    <p>
      Strong relationships produce points that cluster closely around a pattern.
    </p>

    <p>
      Weak relationships show much more scatter.
    </p>

    <h2>Linear Relationships</h2>

    <p>
      Many relationships approximately follow a straight-line pattern.
    </p>

    <p>
      These are called
      <strong>linear relationships</strong>.
    </p>

    <p>
      Linear patterns are particularly important because many statistical methods are built around them.
    </p>

    <h2>Nonlinear Relationships</h2>

    <p>
      Not all relationships are linear.
    </p>

    <p>
      Some relationships curve,
      level off,
      or change direction.
    </p>

    <p>
      Scatterplots are valuable because they reveal these patterns visually.
    </p>

    <h2>Clusters</h2>

    <p>
      Sometimes points form separate groups.
    </p>

    <p>
      These groups are called
      <strong>clusters</strong>.
    </p>

    <p>
      Clusters may indicate:
    </p>

    <ul class="bullets">

      <li>Different populations</li>

      <li>Hidden categories</li>

      <li>Important subgroups</li>

    </ul>

    <h2>Outliers</h2>

    <p>
      Scatterplots are excellent tools for detecting outliers.
    </p>

    <p>
      An outlier appears as a point far from the overall pattern.
    </p>

    <p>
      Outliers may result from:
    </p>

    <ul class="bullets">

      <li>Measurement errors</li>

      <li>Data entry mistakes</li>

      <li>Rare observations</li>

      <li>Important real-world events</li>

    </ul>

    <h2>Association Does Not Imply Causation</h2>

    <p>
      One of the most important principles in statistics is:
    </p>

    <div class="example-box">

      <strong>Association does not imply causation.</strong>

    </div>

    <p>
      Even if two variables move together,
      this does not prove that one causes the other.
    </p>

    <p>
      Additional evidence is needed before causal conclusions can be made.
    </p>

    <h2>Scatterplots and Correlation</h2>

    <p>
      Later lessons will introduce
      <strong>correlation</strong>,
      a numerical measure that quantifies the strength of a linear relationship.
    </p>

    <p>
      Scatterplots provide the visual foundation for understanding correlation.
    </p>

    <h2>When Should Scatterplots Be Used?</h2>

    <p>
      Use a scatterplot when:
    </p>

    <ul class="bullets">

      <li>You have two numerical variables</li>

      <li>You want to explore relationships</li>

      <li>You want to identify trends</li>

      <li>You want to detect clusters or outliers</li>

      <li>You want to assess association visually</li>

    </ul>

    <h2>Common Mistakes</h2>

    <p>
      Common scatterplot mistakes include:
    </p>

    <ul class="bullets">

      <li>Using categorical variables</li>

      <li>Overcrowding with too many points</li>

      <li>Ignoring outliers</li>

      <li>Assuming causation from association</li>

      <li>Using inappropriate scales</li>

    </ul>

    <p>
      Careful interpretation is essential.
    </p>

    <h2>Why Scatterplots Are Important</h2>

    <p>
      Scatterplots are among the most important visualizations in statistics.
    </p>

    <p>
      They provide direct insight into relationships,
      which are central to prediction,
      modeling,
      scientific research,
      and decision-making.
    </p>

    <p>
      Much of modern data analysis begins with a scatterplot.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Scatterplots display relationships between two numerical variables</li>

        <li>Each point represents one observation</li>

        <li>Scatterplots reveal direction and strength of association</li>

        <li>Relationships may be positive, negative, or absent</li>

        <li>Patterns may be linear or nonlinear</li>

        <li>Scatterplots help identify clusters and outliers</li>

        <li>Association alone does not prove causation</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/visualization/boxplots/">
         ← Previous: Boxplots
      </a>

      <a class="btn"
         href="/descriptive/visualization/time-series-line-charts/">
         Next: Time Series and Line Charts →
      </a>

    </div>

  </div>

</section>