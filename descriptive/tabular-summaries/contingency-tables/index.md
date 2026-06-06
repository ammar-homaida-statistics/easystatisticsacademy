---
layout: default
title: Contingency Tables
description: Learn how contingency tables summarize relationships between two categorical variables and form the foundation of categorical data analysis.
permalink: /descriptive/tabular-summaries/contingency-tables/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_tabular_summaries_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/tabular-summaries/contingency-tables/",
    label: "Contingency Tables",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->
<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 2</span>
      <span class="badge">Categorical Data</span>
      <span class="badge">Cross Tabulation</span>
    </div>

    <h1>Contingency Tables</h1>

    <p class="lead">
      Frequency tables summarize one variable.
    </p>

    <p class="lead">
      But many statistical questions involve relationships between
      two categorical variables.
      Contingency tables provide a structured way to examine
      those relationships and compare groups.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/tabular-summaries/grouped-frequency-tables/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/tabular-summaries/choosing-the-right-percentage/">
         Next: Choosing the Right Percentage
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->
<section class="section">

  <div class="content-narrow">

    <h2>From One Variable to Two Variables</h2>

    <p>
      A frequency table summarizes a single variable.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">
      <li>Blood type frequencies</li>
      <li>Favorite color frequencies</li>
      <li>Education level frequencies</li>
    </ul>

    <p>
      But many real-world questions involve comparing two variables simultaneously.
    </p>

    <p>
      Examples:
    </p>

    <ul class="bullets">
      <li>Gender and smoking status</li>
      <li>Education level and employment status</li>
      <li>Treatment group and recovery outcome</li>
      <li>Political party and voting preference</li>
    </ul>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Contingency tables summarize the joint distribution
        of two categorical variables.
      </p>

    </div>

    <p>
  A joint distribution describes how observations are distributed
  across combinations of categories from two variables.
</p>

    <h2>What Is a Contingency Table?</h2>

    <p>
      A <strong>contingency table</strong>
      (also called a cross-tabulation or cross-tab)
      displays frequencies for combinations of categories.
    </p>

    <p>
      One variable forms the rows,
      and the other forms the columns.
    </p>

    <p>
      Each cell contains a frequency count.
    </p>

    <img src="{{ '/descriptive/images/contingency-table-structure.png' | relative_url }}"
     alt="Structure of a contingency table"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Rows represent categories of one variable,
columns represent categories of a second variable,
and cells contain frequencies for category combinations.
</p>

    <h2>Example: Smoking and Gender</h2>

    <p>
      Suppose a survey records smoking status and gender.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th></th>
            <th>Smoker</th>
            <th>Non-Smoker</th>
            <th>Total</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Male</td>
            <td>30</td>
            <td>70</td>
            <td>100</td>
          </tr>

          <tr>
            <td>Female</td>
            <td>20</td>
            <td>80</td>
            <td>100</td>
          </tr>

          <tr>
            <td><strong>Total</strong></td>
            <td><strong>50</strong></td>
            <td><strong>150</strong></td>
            <td><strong>200</strong></td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      This table summarizes how two categorical variables
occur together in the same dataset.
    </p>

    <h2>Understanding the Cells</h2>

    <p>
      Each cell represents a combination of categories.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">
      <li>30 males are smokers</li>
      <li>70 males are non-smokers</li>
      <li>20 females are smokers</li>
      <li>80 females are non-smokers</li>
    </ul>

    <p>
      The table provides much richer information
      than separate frequency tables.
    </p>

    <p>
  Raw cell counts alone do not always reveal meaningful differences.
  Percentages are often needed for proper comparison.
</p>

    <h2>Row Totals and Column Totals</h2>

    <p>
      Contingency tables often include totals.
    </p>

    <div class="grid grid-2">

      <div class="card">

        <h3>Row Totals</h3>

        <p>
          Summarize each row category.
        </p>

        <p>
          Example:
          Total males = 100.
        </p>

      </div>

      <div class="card">

        <h3>Column Totals</h3>

        <p>
          Summarize each column category.
        </p>

        <p>
          Example:
          Total smokers = 50.
        </p>

      </div>

    </div>

    <p>
      Totals help calculate percentages and comparisons.
    </p>

    <div class="concept-box">

  <strong>Important insight:</strong>

  <p>
    Contingency tables do not simply summarize categories.
    They summarize relationships between categories.
  </p>

</div>

    <h2>Why Contingency Tables Are Useful</h2>

    <p>
      They allow us to investigate whether variables appear related.
    </p>

    <p>
      Looking at the example:
    </p>

    <ul class="bullets">
      <li>30% of males smoke</li>
      <li>20% of females smoke</li>
    </ul>

    <p>
      This suggests possible differences between groups.
    </p>

    <img src="{{ '/descriptive/images/counts-vs-percentages-crosstab.png' | relative_url }}"
     alt="Counts versus percentages in a contingency table"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Percentages often reveal group differences more clearly than raw counts.
</p>

    <p>
  However, comparisons should usually be based on percentages
  rather than raw counts.
</p>

    <p>
      Later statistical methods will help determine
      whether such differences are meaningful.
    </p>

    <h2>Contingency Tables Do Not Prove Causation</h2>

    <p>
      A contingency table only describes observed relationships.
    </p>

    <p>
      It cannot prove:
    </p>

    <ul class="bullets">
      <li>Cause and effect</li>
      <li>Direction of influence</li>
      <li>Underlying mechanisms</li>
    </ul>

    <p>
      It is a descriptive tool,
      not a causal analysis tool.
    </p>

    <h2>Contingency Tables Are Common in Research</h2>

    <p>
      They appear frequently in:
    </p>

    <ul class="bullets">
      <li>Medical studies</li>
      <li>Survey research</li>
      <li>Marketing analysis</li>
      <li>Education research</li>
      <li>Public policy studies</li>
      <li>Social science investigations</li>
    </ul>

    <p>
      Whenever two categorical variables are analyzed together,
      contingency tables are often the starting point.
    </p>

    <h2>Two-Way Tables and Beyond</h2>

    <p>
      Most introductory statistics focuses on two-way tables,
      involving two variables.
    </p>

    <p>
      More advanced analyses may involve:
    </p>

    <ul class="bullets">
      <li>Three-way tables</li>
      <li>Multi-way tables</li>
      <li>Higher-dimensional categorical structures</li>
    </ul>

    <p>
      The underlying idea remains the same:
      summarizing combinations of categories.
    </p>

    <h2>Contingency Tables Lead to Statistical Testing</h2>

    <p>
      Later in statistics,
      contingency tables become the foundation for:
    </p>

    <ul class="bullets">
      <li>Chi-square tests</li>
      <li>Tests of independence</li>
      <li>Association measures</li>
      <li>Categorical modeling</li>
    </ul>

    <p>
      Understanding the table itself comes before understanding those methods.
    </p>

    <h2>The Most Important Question</h2>

    <p>
      When viewing a contingency table,
      always ask:
    </p>

    <div class="example-box">

      <p>
        Are the proportions similar across groups,
        or do important differences appear?
      </p>

    </div>

    <p>
      This question drives much of categorical data analysis.
    </p>

    <div class="concept-box">

  <strong>Key insight:</strong>

  <p>
    Frequency tables describe one variable,
    while contingency tables describe how two variables
    are related within a dataset.
  </p>

</div>

<h2>Optional: Contingency Tables in SPSS</h2>

<ul class="bullets">
  <li>Analyze → Descriptive Statistics → Crosstabs</li>
  <li>Rows and columns are assigned to categorical variables</li>
  <li>SPSS can display counts, percentages, and chi-square statistics</li>
</ul>

<div style="display:flex; gap:20px; flex-wrap:wrap;">

  <div style="flex:1; min-width:300px;">
    <img src="{{ 'descriptive/images/spss_crosstab_data.png' | relative_url }}"
         alt="SPSS data view"
         style="width:100%; height:auto;">
    <p style="text-align:center;">
      Data entered in SPSS
    </p>
  </div>

  <div style="flex:1; min-width:300px;">
    <img src="{{ 'descriptive/images/spss_crosstabs_output.png' | relative_url }}"
         alt="SPSS crosstabs output"
         style="width:100%; height:auto;">
    <p style="text-align:center;">
      Crosstabs output
    </p>
  </div>

</div>

<h3>Python Example</h3>

<p>
This example creates a contingency table for gender and smoking status.
</p>

<pre><code>import pandas as pd

data = pd.DataFrame({
    "Gender": ["Male", "Male", "Female", "Female"],
    "Smoking": ["Yes", "No", "No", "Yes"]
})

print(pd.crosstab(data["Gender"], data["Smoking"]))
</code></pre>

<h3>R Example</h3>

<p>
This example creates a contingency table for gender and smoking status.
</p>

<pre><code>gender <- c("Male", "Male", "Female", "Female")
smoking <- c("Yes", "No", "No", "Yes")

table(gender, smoking)
</code></pre>

<div style="display:flex; gap:20px; align-items:flex-start; flex-wrap:wrap;">

  <div style="flex:1; min-width:300px;">
    <img src="{{ 'descriptive/images/spss_crosstab_data.png' | relative_url }}"
         alt="SPSS data view for contingency table"
         style="width:100%; height:auto;">

    <p style="text-align:center;">
      Data entered in SPSS
    </p>
  </div>

  <div style="flex:1; min-width:300px;">
    <img src="{{ 'descriptive/images/spss_crosstabs_output.png' | relative_url }}"
         alt="SPSS crosstabs output"
         style="width:100%; height:auto;">

    <p style="text-align:center;">
      Crosstabs output
    </p>
  </div>

</div>

    <!-- TAKEAWAYS -->
    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Contingency tables summarize two categorical variables simultaneously</li>

        <li>Rows and columns represent categories of different variables</li>

        <li>Cells contain frequencies for category combinations</li>

        <li>Totals help support interpretation and percentage calculations</li>

        <li>Contingency tables reveal patterns and group differences</li>

        <li>They describe relationships but do not establish causation</li>

        <li>They form the foundation for later categorical statistical methods</li>

      </ul>

    </div>

    <!-- NAVIGATION -->
    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/tabular-summaries/grouped-frequency-tables/">
         ← Previous: Grouped Frequency Tables
      </a>

      <a class="btn"
         href="/descriptive/tabular-summaries/choosing-the-right-percentage/">
         Next: Choosing the Right Percentage →
      </a>

    </div>

  </div>

</section>
