---
layout: default
title: Pie Charts
description: Learn what pie charts are, when they should be used, their limitations, and why statisticians often prefer bar charts.
permalink: /descriptive/visualization/pie-charts/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_visualization_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/visualization/pie-charts/",
    label: "Pie Charts",
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
      <span class="badge">Categorical Data</span>
    </div>

    <h1>Pie Charts</h1>

    <p class="lead">
      Pie charts are designed to show how a whole is divided into parts.
    </p>

    <p class="lead">
      They are among the most recognizable statistical graphics,
      but they are also among the most debated.
      Understanding both their strengths and weaknesses is important for effective data visualization.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/visualization/bar-charts/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/visualization/histograms/">
         Next: Histograms →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is a Pie Chart?</h2>

    <p>
      A <strong>pie chart</strong>
      represents a complete whole as a circle.
    </p>

    <p>
      The circle is divided into slices,
      with each slice representing a category.
    </p>

    <p>
      Larger categories receive larger slices.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Pie charts emphasize parts of a whole.
      </p>

    </div>

    <h2>A Simple Example</h2>

    <p>
      Suppose a survey asks students about their preferred mode of transportation.
    </p>

    0

    <p>
      The chart immediately shows how the total group is divided among categories.
    </p>

    <h2>When Should Pie Charts Be Used?</h2>

    <p>
      Pie charts work best when:
    </p>

    <ul class="bullets">

      <li>The variable is categorical</li>

      <li>Categories form a meaningful whole</li>

      <li>The number of categories is small</li>

      <li>The goal is to show proportions</li>

    </ul>

    <p>
      Common examples include:
    </p>

    <ul class="bullets">

      <li>Market share</li>

      <li>Budget allocation</li>

      <li>Survey responses</li>

      <li>Population composition</li>

      <li>Product sales distribution</li>

    </ul>

    <h2>The Total Must Represent a Whole</h2>

    <p>
      Pie charts only make sense when all categories together
      represent a complete total.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>100% of survey responses</li>

      <li>100% of a budget</li>

      <li>100% of customers</li>

    </ul>

    <p>
      If categories do not form a meaningful whole,
      a pie chart may be inappropriate.
    </p>

    <h2>Percentages Are Commonly Used</h2>

    <p>
      Pie charts usually display:
    </p>

    <ul class="bullets">

      <li>Percentages</li>

      <li>Proportions</li>

      <li>Shares</li>

    </ul>

    <p>
      Because the entire circle represents 100%,
      each slice shows its contribution to the whole.
    </p>

    <h2>Interpreting a Pie Chart</h2>

    <p>
      When viewing a pie chart,
      ask:
    </p>

    <ul class="bullets">

      <li>Which category is largest?</li>

      <li>Which category is smallest?</li>

      <li>How dominant is the largest category?</li>

      <li>Are categories relatively balanced?</li>

      <li>How much of the whole does each slice represent?</li>

    </ul>

    <p>
      These questions help identify important patterns.
    </p>

    <h2>The Main Strength of Pie Charts</h2>

    <p>
      Pie charts are intuitive.
    </p>

    <p>
      Most people immediately understand that:
    </p>

    <ul class="bullets">

      <li>The whole circle equals 100%</li>

      <li>Large slices represent large shares</li>

      <li>Small slices represent small shares</li>

    </ul>

    <p>
      This makes pie charts popular in reports,
      dashboards,
      and media publications.
    </p>

    <h2>The Main Weakness of Pie Charts</h2>

    <p>
      Humans compare lengths more accurately than angles.
    </p>

    <p>
      Because pie charts rely on angles and areas,
      precise comparisons can be difficult.
    </p>

    <p>
      For example,
      distinguishing between:
    </p>

    <ul class="bullets">

      <li>22%</li>

      <li>24%</li>

      <li>26%</li>

    </ul>

    <p>
      is often harder in a pie chart than in a bar chart.
    </p>

    <h2>Why Many Statisticians Prefer Bar Charts</h2>

    <p>
      For category comparisons,
      bar charts are usually easier to interpret.
    </p>

    <p>
      Consider:
    </p>

    <ul class="bullets">

      <li>Bar lengths are easier to compare</li>

      <li>Small differences are more visible</li>

      <li>Ranking categories is easier</li>

      <li>Large numbers of categories are easier to display</li>

    </ul>

    <p>
      As a result,
      many analysts choose bar charts whenever comparison is the primary goal.
    </p>

    <h2>Too Many Categories Cause Problems</h2>

    <p>
      Pie charts become difficult to read when there are many slices.
    </p>

    <p>
      Problems include:
    </p>

    <ul class="bullets">

      <li>Overlapping labels</li>

      <li>Tiny slices</li>

      <li>Difficult comparisons</li>

      <li>Visual clutter</li>

    </ul>

    <p>
      A pie chart with more than five or six categories often becomes ineffective.
    </p>

    <h2>Bad Pie Chart Example</h2>

    <p>
      A pie chart with:
    </p>

    <ul class="bullets">

      <li>12 categories</li>

      <li>Several very small slices</li>

      <li>Long labels</li>

      <li>Nearly equal proportions</li>

    </ul>

    <p>
      can be difficult to interpret accurately.
    </p>

    <p>
      A bar chart would usually communicate the same information more clearly.
    </p>

    <h2>Common Mistake: Using Raw Counts Without Context</h2>

    <p>
      Pie charts represent proportions,
      not simply counts.
    </p>

    <p>
      The relationship to the total should always be clear.
    </p>

    <p>
      Readers should understand:
    </p>

    <ul class="bullets">

      <li>What the total represents</li>

      <li>How percentages were calculated</li>

      <li>Whether categories sum to the whole</li>

    </ul>

    <h2>Pie Charts and Percentages</h2>

    <p>
      Every slice corresponds to:
    </p>

    1

    <p>
      The size of the slice reflects this percentage.
    </p>

    <h2>Good Statistical Practice</h2>

    <p>
      Before creating a pie chart,
      verify:
    </p>

    <ul class="bullets">

      <li>The data are categorical</li>

      <li>Categories form a meaningful whole</li>

      <li>The number of categories is small</li>

      <li>Percentages sum to approximately 100%</li>

      <li>A pie chart communicates better than a bar chart</li>

    </ul>

    <p>
      If these conditions are not met,
      another graph may be more effective.
    </p>

    <h2>Pie Charts in Modern Statistics</h2>

    <p>
      Pie charts remain widely used because they are familiar and intuitive.
    </p>

    <p>
      However,
      professional analysts increasingly favor bar charts when precise comparisons are important.
    </p>

    <p>
      The key is choosing the graph that best answers the statistical question.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Pie charts show how a whole is divided into parts</li>

        <li>They are most appropriate for categorical data</li>

        <li>The entire pie represents 100% of the total</li>

        <li>Pie charts work best with a small number of categories</li>

        <li>Large numbers of categories reduce readability</li>

        <li>Bar charts are often better for precise comparisons</li>

        <li>The graph should always match the statistical purpose</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/visualization/bar-charts/">
         ← Previous: Bar Charts
      </a>

      <a class="btn"
         href="/descriptive/visualization/histograms/">
         Next: Histograms →
      </a>

    </div>

  </div>

</section>