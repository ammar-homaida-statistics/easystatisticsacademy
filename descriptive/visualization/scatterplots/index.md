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

  <strong>Important insight:</strong>

  <p>
    Each point represents one observation.
    For example, a point might represent one student's study hours and exam score,
    or one person's height and weight.
  </p>

</div>

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

    <p>
      The pattern suggests that students who study more tend to achieve higher scores.
    </p>

    <img src="{{ 'descriptive/images/study-hours-scatterplot.png' | relative_url }}"
     alt="Scatterplot of study hours and exam scores"
     style="margin-top:15px; max-width:100%; height:auto;">

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

    <img src="{{ 'descriptive/images/types-of-association.png' | relative_url }}"
     alt="Positive, negative, and no association"
     style="margin-top:15px; max-width:100%; height:auto;">

    <h2>Direction of Association</h2>

    <div class="example-box">

  <p>
    A quick rule:
  </p>

  <ul class="bullets">
    <li>Upward trend → positive association</li>
    <li>Downward trend → negative association</li>
    <li>No visible trend → little or no association</li>
  </ul>

</div>

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

    <img src="{{ 'descriptive/images/strong-vs-weak-association.png' | relative_url }}"
     alt="Strong and weak associations"
     style="margin-top:15px; max-width:100%; height:auto;">

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

    <h2>Form of the Relationship</h2>

<p>
  In addition to direction and strength,
  statisticians examine the form of a relationship.
</p>

<ul class="bullets">
  <li>Linear patterns follow an approximate straight line</li>
  <li>Nonlinear patterns follow a curve or changing trend</li>
</ul>

<p>
  Identifying the form helps determine which statistical methods are appropriate.
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

    <img src="{{ 'descriptive/images/linear-vs-nonlinear.png' | relative_url }}"
     alt="Linear and nonlinear relationships"
     style="margin-top:15px; max-width:100%; height:auto;">

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

    <img src="{{ 'descriptive/images/scatterplot-clusters.png' | relative_url }}"
     alt="Clusters in a scatterplot"
     style="margin-top:15px; max-width:100%; height:auto;">

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

    <img src="{{ 'descriptive/images/scatterplot-outlier.png' | relative_url }}"
     alt="Outlier in a scatterplot"
     style="margin-top:15px; max-width:100%; height:auto;">

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
  For example,
  ice cream sales and drowning incidents may both increase during summer.
  The association exists,
  but ice cream does not cause drowning.
</p>

    <p>
      Even if two variables move together,
      this does not prove that one causes the other.
    </p>

    <p>
      Additional evidence is needed before causal conclusions can be made.
    </p>

    <h2>Scatterplots and Correlation</h2>

    <img src="{{ 'descriptive/images/correlation-preview.png' | relative_url }}"
     alt="Scatterplot showing strong positive correlation"
     style="margin-top:15px; max-width:100%; height:auto;">

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
  Scatterplots often provide the first indication that one variable may help predict another.
</p>

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

    <div class="concept-box">

  <strong>When interpreting a scatterplot, look for:</strong>

  <ul class="bullets">
    <li>Direction</li>
    <li>Strength</li>
    <li>Form</li>
    <li>Outliers</li>
  </ul>

</div>

<div class="example-box">

  <h3>SPSS Application</h3>

  <p>
    To create a scatterplot in SPSS:
  </p>

  <ol>
    <li>Click <strong>Graphs → Chart Builder</strong></li>
    <li>Select <strong>Scatter/Dot</strong></li>
    <li>Choose <strong>Simple Scatter</strong></li>
    <li>Drag one variable to the X-axis</li>
    <li>Drag the second variable to the Y-axis</li>
    <li>Click <strong>OK</strong></li>
  </ol>

  <p>
    SPSS will generate a scatterplot showing the relationship between the two variables.
  </p>

</div>

 <div style="flex:1; min-width:300px;">
    <img src="{{ '/descriptive/images/spss_scatterplot_output.png' | relative_url }}"
         alt="SPSS scatterplot output"
         style="width:100%; height:auto;">
    <p style="text-align:center;">
      Scatterplot showing the relationship between study hours and exam scores
    </p>
  </div>

  <h3>Python Example</h3>

<p>
This example creates a scatterplot of study hours and exam scores.
</p>

<pre><code>import matplotlib.pyplot as plt

hours = [1,2,2,3,4,4,5,6,7,8]
scores = [55,60,63,65,70,72,78,82,88,92]

plt.scatter(hours, scores)

plt.xlabel("Study Hours")
plt.ylabel("Exam Score")

plt.show()
</code></pre>

<h3>R Example</h3>

<p>
This example creates a scatterplot of study hours and exam scores.
</p>

<pre><code>hours <- c(1,2,2,3,4,4,5,6,7,8)
scores <- c(55,60,63,65,70,72,78,82,88,92)

plot(hours,
     scores,
     xlab = "Study Hours",
     ylab = "Exam Score")
</code></pre>

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
