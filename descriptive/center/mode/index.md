---
layout: default
title: Mode
description: Learn what the mode is, how it is determined, and when it provides useful information about the most common value in a dataset.
permalink: /descriptive/center/mode/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_center_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/center/mode/",
    label: "Mode",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 4</span>
      <span class="badge">Center</span>
      <span class="badge">Mode</span>
    </div>

    <h1>Mode</h1>

    <p class="lead">
      The mean describes the balance point of a distribution,
      and the median identifies its middle position.
    </p>

    <p class="lead">
      The mode takes a different approach.
      Instead of focusing on averages or positions,
      it identifies the value that occurs most frequently.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/center/median/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/center/mean-vs-median/">
         Next: Mean vs Median →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is the Mode?</h2>

    <p>
      The <strong>mode</strong>
      is the value that appears most frequently in a dataset.
    </p>

    <p>
      Unlike the mean and median,
      the mode focuses entirely on frequency.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The mode is the most commonly occurring value in a dataset.
      </p>

    </div>

    <h2>A Simple Example</h2>

    <p>
      Consider the dataset:
    </p>

    <div class="example-box">

      <p>
        2, 4, 4, 5, 7
      </p>

    </div>

    <p>
      The value 4 appears twice,
      while every other value appears only once.
    </p>

    <p>
      Therefore:
    </p>

    <div class="example-box">

      <p>
        Mode = 4
      </p>

    </div>

    <h2>Another Example</h2>

    <div class="example-box">

      <p>
        10, 10, 10, 15, 20, 25
      </p>

    </div>

    <p>
      Since 10 appears three times,
      it is the most frequent value.
    </p>

    <div class="example-box">

      <p>
        Mode = 10
      </p>

    </div>

    <h2>The Mode Does Not Need Ordering</h2>

    <p>
      Unlike the median,
      the mode does not require observations to be sorted.
    </p>

    <p>
      Only the frequencies matter.
    </p>

    <p>
      Whether the data are ordered or unordered,
      the mode remains the same.
    </p>

    <h2>Datasets Can Have No Mode</h2>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        1, 2, 3, 4, 5
      </p>

    </div>

    <p>
      Every value appears exactly once.
    </p>

    <p>
      No value occurs more frequently than the others.
    </p>

    <p>
      Therefore,
      this dataset has no mode.
    </p>

    <h2>Datasets Can Have More Than One Mode</h2>

    <p>
      It is possible for multiple values to share the highest frequency.
    </p>

    <p>
      Example:
    </p>

    <div class="example-box">

      <p>
        2, 2, 5, 5, 8, 9
      </p>

    </div>

    <p>
      Both 2 and 5 occur twice.
    </p>

    <p>
      Therefore:
    </p>

    <div class="example-box">

      <p>
        Modes = 2 and 5
      </p>

    </div>

    <h2>Bimodal Distributions</h2>

    <p>
      A dataset with two modes is called
      <strong>bimodal</strong>.
    </p>

    <p>
      Bimodal distributions often indicate:
    </p>

    <ul class="bullets">

      <li>Two distinct groups</li>

      <li>Different populations combined together</li>

      <li>Interesting underlying structure</li>

    </ul>

    <p>
      Histograms frequently reveal bimodal patterns.
    </p>

    <h2>Multimodal Distributions</h2>

    <p>
      Some datasets contain more than two modes.
    </p>

    <p>
      These are called
      <strong>multimodal distributions</strong>.
    </p>

    <p>
      Multiple modes may suggest several subpopulations within the data.
    </p>

    <h2>The Mode and Categorical Data</h2>

    <p>
      One major advantage of the mode is that it works for categorical variables.
    </p>

    <p>
      Consider favorite colors:
    </p>

    <div class="example-box">

      <p>
        Blue, Red, Blue, Green, Blue, Red
      </p>

    </div>

    <p>
      The most common category is:
    </p>

    <div class="example-box">

      <p>
        Mode = Blue
      </p>

    </div>

    <p>
      Neither the mean nor the median can be computed meaningfully for such data.
    </p>

    <h2>Why the Mode Is Unique</h2>

    <p>
      Among the three major measures of center:
    </p>

    <ul class="bullets">

      <li>The mean uses arithmetic calculations</li>

      <li>The median uses position</li>

      <li>The mode uses frequency</li>

    </ul>

    <p>
      This makes the mode fundamentally different from the other measures.
    </p>

    <h2>Mode and Typicality</h2>

    <p>
      The mode is often interpreted as the most common observation.
    </p>

    <p>
      However,
      the most common value is not always representative of the entire dataset.
    </p>

    <p>
      A dataset may have a clear mode while most observations are spread across many values.
    </p>

    <h2>Strengths of the Mode</h2>

    <ul class="bullets">

      <li>Easy to identify</li>

      <li>Works with categorical data</li>

      <li>Unaffected by extreme values</li>

      <li>Useful for identifying popular categories</li>

      <li>Can reveal multiple groups in data</li>

    </ul>

    <h2>Limitations of the Mode</h2>

    <ul class="bullets">

      <li>Some datasets have no mode</li>

      <li>Some datasets have several modes</li>

      <li>May not represent the center well</li>

      <li>Uses only frequency information</li>

      <li>Ignores much of the dataset</li>

    </ul>

    <h2>Mode vs Mean and Median</h2>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        1, 2, 2, 3, 10
      </p>

    </div>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Measure</th>
            <th>Value</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Mode</td>
            <td>2</td>
          </tr>

          <tr>
            <td>Median</td>
            <td>2</td>
          </tr>

          <tr>
            <td>Mean</td>
            <td>3.6</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Notice that the three measures do not necessarily produce the same result.
    </p>

    <h2>When Is the Mode Most Useful?</h2>

    <p>
      The mode is especially useful when:
    </p>

    <ul class="bullets">

      <li>Studying categorical variables</li>

      <li>Identifying the most popular option</li>

      <li>Analyzing consumer preferences</li>

      <li>Investigating repeated values</li>

      <li>Exploring distribution shape</li>

    </ul>

    <h2>Real-World Examples</h2>

    <p>
      Common applications include:
    </p>

    <ul class="bullets">

      <li>Most purchased product</li>

      <li>Most common blood type</li>

      <li>Most popular major</li>

      <li>Most frequently reported symptom</li>

      <li>Most common transportation method</li>

    </ul>

    <p>
      In these situations,
      the mode often provides meaningful information.
    </p>

    <h2>The Three Measures Together</h2>

    <p>
      Mean,
      median,
      and mode each capture different aspects of center.
    </p>

    <p>
      No single measure is always best.
    </p>

    <p>
      Skilled statisticians choose the measure that best fits the data and the question being asked.
    </p>

    <p>
      The next lesson directly compares the mean and median,
      helping determine when each should be preferred.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The mode is the most frequently occurring value</li>

        <li>A dataset may have one mode, multiple modes, or no mode</li>

        <li>The mode works with both numerical and categorical data</li>

        <li>The mode is not affected by outliers</li>

        <li>Bimodal and multimodal patterns may reveal hidden groups</li>

        <li>The mode focuses on frequency rather than position or arithmetic averages</li>

        <li>The mode is often most useful for categorical variables and popularity questions</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/center/median/">
         ← Previous: Median
      </a>

      <a class="btn"
         href="/descriptive/center/mean-vs-median/">
         Next: Mean vs Median →
      </a>

    </div>

  </div>

</section>