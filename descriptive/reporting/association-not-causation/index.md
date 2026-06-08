---
layout: default
title: Association Is Not Causation
description: Learn the difference between association and causation, why relationships between variables can be misleading, and how to avoid one of the most common statistical errors.
permalink: /descriptive/reporting/association-not-causation/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_reporting_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/reporting/association-not-causation/",
    label: "Association Is Not Causation",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 7</span>
      <span class="badge">Reporting</span>
      <span class="badge">Interpretation</span>
    </div>

    <h1>Association Is Not Causation</h1>

    <p class="lead">
      One of the most important principles in statistics is that a relationship between two variables does not automatically imply that one causes the other.
    </p>

    <p class="lead">
      Misinterpreting association as causation can lead to incorrect conclusions,
      poor decisions,
      and misleading reports.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/reporting/reporting-graphs-properly/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/reporting/outliers-and-exclusions/">
         Next: Outliers and Exclusions →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is Association?</h2>

    <p>
      An <strong>association</strong> exists when two variables tend to vary together.
    </p>

    <p>
      Changes in one variable are accompanied by changes in another variable.
    </p>

    <p>
      Association simply describes a relationship that can be observed in data.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Association means variables are related. It does not explain why they are related.
      </p>

    </div>

    <h2>What Is Causation?</h2>

    <p>
      <strong>Causation</strong> means that changes in one variable directly produce changes in another variable.
    </p>

    <p>
      A causal relationship involves cause and effect.
    </p>

    <div class="example-box">

      <p>
        Taking a pain-relief medication may reduce pain.
      </p>
    </div>

    <p>
      In this situation,
      the medication is intended to cause the reduction in pain.
    </p>

    <h2>The Critical Difference</h2>

    <p>
      Association answers:
    </p>

    <div class="example-box">

      <p>
        "Are these variables related?"
      </p>
    </div>

    <p>
      Causation answers:
    </p>

    <div class="example-box">

      <p>
        "Does one variable produce changes in the other?"
      </p>
    </div>

    <p>
      These are very different questions.
    </p>

    <h2>A Common Mistake</h2>

    <p>
      People often observe a relationship and immediately assume causation.
    </p>

    <div class="example-box">

      <p>
        Students who study more tend to earn higher grades.
      </p>
    </div>

    <p>
      This observation suggests an association.
    </p>

    <p>
      It may indicate causation,
      but the data alone do not prove it.
    </p>

    <h2>Why Associations Can Be Misleading</h2>

    <p>
      Several different explanations can produce an observed relationship.
    </p>

    <ul class="bullets">

      <li>Direct causation</li>

      <li>Reverse causation</li>

      <li>Coincidence</li>

      <li>Confounding variables</li>

      <li>Measurement issues</li>

    </ul>

    <p>
      Without additional evidence,
      we cannot determine which explanation is correct.
    </p>

    <h2>Confounding Variables</h2>

    <p>
      A <strong>confounding variable</strong> is a third variable that influences both variables being studied.
    </p>

    <p>
      Confounders can create the appearance of a direct relationship even when none exists.
    </p>

    <div class="example-box">

      <p>
        Ice cream sales increase during summer.
      </p>

      <p>
        Drowning incidents also increase during summer.
      </p>

    </div>

    <p>
      This does not mean ice cream causes drowning.
    </p>

    <p>
      Temperature acts as a confounding variable because it affects both.
    </p>

    <h2>Reverse Causation</h2>

    <p>
      Sometimes the direction of influence is opposite to what is initially assumed.
    </p>

    <div class="example-box">

      <p>
        Stress and poor sleep are associated.
      </p>
    </div>

    <p>
      Does stress cause poor sleep?
    </p>

    <p>
      Does poor sleep increase stress?
    </p>

    <p>
      Both possibilities may be true.
    </p>

    <p>
      Association alone cannot determine direction.
    </p>

    <h2>Coincidental Relationships</h2>

    <p>
      Some variables appear related purely by chance.
    </p>

    <p>
      Large datasets often contain relationships that occur accidentally.
    </p>

    <p>
      Not every observed association reflects a meaningful process.
    </p>

    <h2>Scatterplots Show Association</h2>

    <p>
      Scatterplots are frequently used to visualize relationships between numerical variables.
    </p>

    <p>
      A scatterplot can reveal:
    </p>

    <ul class="bullets">

      <li>Positive associations</li>

      <li>Negative associations</li>

      <li>No association</li>

      <li>Unusual observations</li>

    </ul>

    <p>
      However,
      a scatterplot cannot prove causation.
    </p>

    <h2>Positive Association</h2>

    <p>
      In a positive association,
      larger values of one variable tend to occur with larger values of another variable.
    </p>

    <div class="example-box">

      <p>
        Study time and exam scores often show a positive association.
      </p>
    </div>

    <p>
      This relationship may suggest a possible causal mechanism,
      but additional evidence is needed.
    </p>

    <h2>Negative Association</h2>

    <p>
      In a negative association,
      larger values of one variable tend to occur with smaller values of another variable.
    </p>

    <div class="example-box">

      <p>
        Vehicle age and resale value often show a negative association.
      </p>
    </div>

    <p>
      Again,
      the association alone does not establish causation.
    </p>

    <h2>What Descriptive Statistics Can Do</h2>

    <p>
      Descriptive statistics help identify patterns and relationships.
    </p>

    <p>
      They can show:
    </p>

    <ul class="bullets">

      <li>Whether variables appear related</li>

      <li>How strong a relationship appears</li>

      <li>Whether unusual observations exist</li>

    </ul>

    <p>
      Descriptive statistics do not prove cause-and-effect relationships.
    </p>

    <h2>Why Experiments Matter</h2>

    <p>
      Establishing causation often requires carefully designed experiments.
    </p>

    <p>
      Experiments attempt to control confounding variables and isolate causal effects.
    </p>

    <p>
      This topic becomes important later in inferential statistics and research design.
    </p>

    <h2>Reporting Associations Correctly</h2>

    <p>
      Statistical reports should use cautious language when discussing relationships.
    </p>

    <div class="example-box">

      <p>
        Preferred:
      </p>

      <p>
        "Higher study time was associated with higher exam scores."
      </p>
    </div>

    <div class="example-box">

      <p>
        Avoid:
      </p>

      <p>
        "Studying more caused higher exam scores."
      </p>
    </div>

    <p>
      Unless causal evidence exists,
      association language is usually more appropriate.
    </p>

    <h2>Words That Suggest Association</h2>

    <p>
      Useful reporting terms include:
    </p>

    <ul class="bullets">

      <li>Associated with</li>

      <li>Related to</li>

      <li>Linked to</li>

      <li>Correlated with</li>

      <li>Tended to occur with</li>

    </ul>

    <p>
      These terms describe relationships without making unsupported causal claims.
    </p>

    <h2>Words That Suggest Causation</h2>

    <p>
      Causal language should be used carefully.
    </p>

    <ul class="bullets">

      <li>Caused</li>

      <li>Produced</li>

      <li>Resulted in</li>

      <li>Led to</li>

      <li>Created</li>

    </ul>

    <p>
      Such terms imply evidence beyond simple observation.
    </p>

    <h2>A Professional Reporting Example</h2>

    <div class="example-box">

      <p>
        "Income and education level were positively associated. Individuals with higher levels of education tended to report higher incomes."
      </p>
    </div>

    <p>
      This statement describes the relationship without claiming causation.
    </p>

    <h2>Why This Principle Matters</h2>

    <p>
      Many statistical misunderstandings arise from confusing association with causation.
    </p>

    <p>
      Applying this principle helps analysts:
    </p>

    <ul class="bullets">

      <li>Avoid incorrect conclusions</li>

      <li>Communicate responsibly</li>

      <li>Interpret results accurately</li>

      <li>Maintain scientific credibility</li>

    </ul>

    <p>
      It is one of the most important habits in statistical thinking.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Another important reporting decision involves unusual observations.
    </p>

    <p>
      Analysts sometimes remove observations from analyses,
      but such decisions must be justified carefully.
    </p>

    <p>
      The next lesson examines outliers,
      exclusions,
      and responsible handling of unusual data.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Association means variables are related</li>

        <li>Causation means one variable directly influences another</li>

        <li>Association does not automatically imply causation</li>

        <li>Confounding variables can create misleading relationships</li>

        <li>Scatterplots reveal associations but do not prove causality</li>

        <li>Professional reporting should distinguish association from causation</li>

        <li>Careful interpretation is essential for accurate statistical communication</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/reporting/reporting-graphs-properly/">
         ← Previous: Reporting Graphs Properly
      </a>

      <a class="btn"
         href="/descriptive/reporting/outliers-and-exclusions/">
         Next: Outliers and Exclusions →
      </a>

    </div>

  </div>

</section>