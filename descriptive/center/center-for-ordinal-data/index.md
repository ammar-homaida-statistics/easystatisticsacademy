---
layout: default
title: Center for Ordinal Data
description: Learn how measures of center apply to ordinal variables and why the median is usually preferred over the mean for ordered categories.
permalink: /descriptive/center/center-for-ordinal-data/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_center_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/center/center-for-ordinal-data/",
    label: "Center for Ordinal Data",
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
      <span class="badge">Ordinal Data</span>
    </div>

    <h1>Center for Ordinal Data</h1>

    <p class="lead">
      Not all data are numerical.
    </p>

    <p class="lead">
      Many variables consist of ordered categories rather than measurable quantities.
      These variables require special consideration when choosing an appropriate measure of center.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/center/winsorized-mean/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/center/reporting-center-properly/">
         Next: Reporting Center Properly →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is Ordinal Data?</h2>

    <p>
      Ordinal variables contain categories that have a natural order.
    </p>

    <p>
      Unlike numerical variables,
      the distances between categories are not necessarily meaningful or measurable.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Poor, Fair, Good, Excellent</li>

      <li>Small, Medium, Large</li>

      <li>Strongly Disagree to Strongly Agree</li>

      <li>Education levels</li>

      <li>Customer satisfaction ratings</li>

    </ul>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Ordinal data provide order, but not meaningful numerical distances between categories.
      </p>

    </div>

    <h2>Why the Mean Is Usually Inappropriate</h2>

    <p>
      The arithmetic mean requires meaningful numerical values.
    </p>

    <p>
      Ordinal categories do not provide this information.
    </p>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        Poor, Fair, Good, Excellent
      </p>

    </div>

    <p>
      We know the order,
      but we do not know whether the distance between Poor and Fair is equal to the distance between Good and Excellent.
    </p>

    <p>
      Because of this,
      calculating an average category is generally not meaningful.
    </p>

    <h2>A Common Mistake</h2>

    <p>
      Researchers sometimes assign numbers to ordinal categories:
    </p>

    <div class="example-box">

      <p>
        Poor = 1<br>
        Fair = 2<br>
        Good = 3<br>
        Excellent = 4
      </p>

    </div>

    <p>
      While this creates numerical codes,
      it does not automatically create a true numerical scale.
    </p>

    <p>
      The numbers merely represent order.
    </p>

    <p>
      Treating them as precise measurements can be misleading.
    </p>

    <h2>The Median Is Usually Preferred</h2>

    <p>
      The median depends on order rather than numerical distances.
    </p>

    <p>
      Since ordinal data possess a meaningful order,
      the median can usually be calculated and interpreted.
    </p>

    <p>
      This makes the median the most common measure of center for ordinal variables.
    </p>

    <h2>An Example</h2>

    <p>
      Suppose customer satisfaction responses are:
    </p>

    <div class="example-box">

      <p>
        Poor, Fair, Fair, Good, Good, Good, Excellent
      </p>

    </div>

    <p>
      The observations are already ordered.
    </p>

    <p>
      The middle observation is:
    </p>

    <div class="example-box">

      <p>
        Good
      </p>

    </div>

    <p>
      Therefore:
    </p>

    <div class="example-box">

      <p>
        Median = Good
      </p>

    </div>

    <p>
      This tells us where the center of the responses lies.
    </p>

    <h2>The Mode Is Also Useful</h2>

    <p>
      The mode works with any type of categorical data.
    </p>

    <p>
      For ordinal variables,
      it identifies the most frequently occurring category.
    </p>

    <p>
      In the previous example:
    </p>

    <div class="example-box">

      <p>
        Mode = Good
      </p>

    </div>

    <p>
      because Good appears most often.
    </p>

    <h2>Median vs Mode for Ordinal Data</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Measure</th>
            <th>Can Be Used?</th>
            <th>Why?</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Mean</td>
            <td>Usually No</td>
            <td>Requires meaningful numerical distances</td>
          </tr>

          <tr>
            <td>Median</td>
            <td>Yes</td>
            <td>Uses ordering information</td>
          </tr>

          <tr>
            <td>Mode</td>
            <td>Yes</td>
            <td>Uses frequencies only</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Likert Scales</h2>

    <p>
      One of the most common ordinal measurements is the Likert scale.
    </p>

    <p>
      Examples include:
    </p>

    <div class="example-box">

      <p>
        Strongly Disagree<br>
        Disagree<br>
        Neutral<br>
        Agree<br>
        Strongly Agree
      </p>

    </div>

    <p>
      These responses are ordered,
      making medians and modes appropriate summaries.
    </p>

    <p>
      Whether means should be reported for Likert scales remains a topic of discussion among researchers.
    </p>

    <h2>Why Order Matters</h2>

    <p>
      The ability to rank observations gives ordinal data more structure than nominal data.
    </p>

    <p>
      Because of this order,
      concepts such as middle position become meaningful.
    </p>

    <p>
      This is exactly why the median can be used.
    </p>

    <h2>Nominal vs Ordinal Data</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Nominal</th>
            <th>Ordinal</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Categories</td>
            <td>Yes</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Natural Order</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Median Possible</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Mode Possible</td>
            <td>Yes</td>
            <td>Yes</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Reporting Ordinal Center</h2>

    <p>
      When reporting center for ordinal variables,
      statisticians often state:
    </p>

    <ul class="bullets">

      <li>The median category</li>

      <li>The modal category</li>

      <li>Category frequencies or percentages</li>

    </ul>

    <p>
      These summaries preserve the meaning of the original scale.
    </p>

    <h2>Real-World Examples</h2>

    <p>
      Measures of center for ordinal data appear in:
    </p>

    <ul class="bullets">

      <li>Customer satisfaction surveys</li>

      <li>Employee evaluations</li>

      <li>Educational assessments</li>

      <li>Opinion polls</li>

      <li>Healthcare questionnaires</li>

    </ul>

    <p>
      Many social science datasets rely heavily on ordinal measurements.
    </p>

    <h2>The Importance of Measurement Scales</h2>

    <p>
      This lesson highlights a broader statistical principle:
    </p>

    <div class="concept-box">

      <strong>Important principle:</strong>

      <p>
        The appropriate measure of center depends on the measurement scale of the variable.
      </p>

    </div>

    <p>
      Statistical methods should always match the type of data being analyzed.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Knowing how to calculate a measure of center is only part of good statistical practice.
    </p>

    <p>
      The next lesson focuses on how measures of center should be reported and communicated clearly and accurately.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Ordinal data contain ordered categories</li>

        <li>Ordinal scales provide order but not meaningful numerical distances</li>

        <li>The median is usually the preferred measure of center for ordinal data</li>

        <li>The mode is also appropriate for ordinal variables</li>

        <li>The mean is generally inappropriate for purely ordinal measurements</li>

        <li>Likert-scale responses are common examples of ordinal data</li>

        <li>The choice of measure of center depends on the measurement scale</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/center/winsorized-mean/">
         ← Previous: Winsorized Mean
      </a>

      <a class="btn"
         href="/descriptive/center/reporting-center-properly/">
         Next: Reporting Center Properly →
      </a>

    </div>

  </div>

</section>