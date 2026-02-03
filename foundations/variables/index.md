---
layout: default
title: Variables
description: A conceptual introduction to variables, how they differ from constants, common variable roles, and why variables are choices rather than facts.
permalink: /foundations/variables/
section: foundations
lesson_order: 7
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="Variables">
<meta name="esa-lesson-url" content="/foundations/variables/">

<a class="btn btn-primary" href="/foundations/observational-units/">Previous: Observational Units</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Variables</h1>

    <p class="lead">
      Variables describe what is measured on each observational unit.<br>
      This lesson explains what variables are, how they are defined, and why they are analytical choices rather than facts.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 7
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>What a variable is in statistics.</li>
      <li>The difference between a variable and a constant.</li>
      <li>Conceptual roles such as independent and dependent variables.</li>
      <li>Why variables are defined by choices, not discovered as facts.</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Why this topic matters</h2>

    <p>
      Once the observational unit is defined, the next question is what is measured on that unit.
      The answer to that question defines the variables.
    </p>

    <p>
      Many disagreements in analysis come from different variable definitions, not from different calculations.
      Two analysts can use the same data but define variables differently.
    </p>

    <p>
      Understanding variables as choices helps prevent false certainty and clarifies what conclusions actually mean.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>What a variable is</h2>

    <p>
      A variable is a characteristic that can take different values across observational units.
      Each variable records one type of information for each unit.
    </p>

    <p>
      For example, age, income, temperature, category labels, and test scores are all variables
      if they vary across observations.
    </p>

    <p>
      Variables describe variation. Without variation, statistical analysis is not possible.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Variable vs constant</h2>

    <p>
      A variable changes across observational units.
      A constant does not.
    </p>

    <p>
      Constants may be important context, but they do not contribute information for statistical analysis
      because they show no variation.
    </p>

    <p>
      Confusing constants with variables can lead to meaningless summaries or unnecessary calculations.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h3>Simple example</h3>

    <p>
      Imagine a class of students taking the same exam.
    </p>

    <p>
      The <strong>exam score</strong> is a <strong>variable</strong> because it differs from one student to another.
    </p>

    <p>
      The <strong>exam date</strong> is a <strong>constant</strong> because every student took the exam on the same day.
    </p>

    <p>
      The exam date provides context, but it does not help explain differences in scores because it does not vary.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Independent and dependent (conceptual)</h2>

    <p>
      In many discussions, variables are described using roles such as independent and dependent.
      These terms describe how variables are thought about, not how they are mathematically modeled.
    </p>

    <p>
      An independent variable is typically viewed as an input or explanatory factor,
      while a dependent variable is viewed as an outcome or response.
    </p>

    <p>
      These roles are conceptual and depend on the question being asked, not on the data alone.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h3>Simple example</h3>

    <p>
      Suppose a teacher wants to understand why some students score higher than others.
    </p>

    <p>
      <strong>Hours studied</strong> is treated as the <strong>independent variable</strong> because it is considered a possible explanation.
    </p>

    <p>
      <strong>Exam score</strong> is treated as the <strong>dependent variable</strong> because it is the outcome of interest.
    </p>

    <p>
      These roles depend on the question being asked and are not fixed properties of the variables themselves.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Predictors and outcomes</h2>

    <p>
      In practice, analysts often use terms like predictors and outcomes instead of independent and dependent variables.
      This language emphasizes interpretation rather than formal modeling.
    </p>

    <p>
      A predictor is a variable used to help understand or explain variation in another variable.
      An outcome is the variable of primary interest.
    </p>

    <p>
      The same variable can be a predictor in one analysis and an outcome in another.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Why variables are choices, not facts</h2>

    <p>
      Variables do not exist independently of measurement and definition.
      Analysts decide how concepts are turned into variables.
    </p>

    <p>
      Choices about definitions, categories, scales, and transformations all affect what a variable represents.
    </p>

    <p>
      Treating variables as choices encourages transparency and reminds us that results depend on how variables are defined.
    </p>
  </div>
</section>

<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      Variables describe what is measured on each observational unit.
      They are defined by analytical choices, not discovered as objective facts.
    </p>
  </div>
</section>

<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      A variable is a characteristic that varies across observations.
      Variables differ from constants, play different conceptual roles, and are shaped by how we choose to measure and define them.
    </p>
  </div>
</section>

<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson introduces <strong>datasets as structures</strong>—how rows and columns organize variables
      and why structure determines what analyses are possible.
    </p>

    <a class="btn btn-primary" href="/foundations/datasets-as-structures/">
      Next: Datasets as Structures
    </a>
  </div>
</section>

<script>
  try {
    localStorage.setItem("esa:lastLesson", window.location.pathname);
  } catch (e) {}
</script>
