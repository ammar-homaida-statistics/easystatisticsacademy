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

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — This lesson is being expanded with more examples, table-based comparisons, and a simple diagram that links units → variables → values.
    </div>

    <p class="lead">
      Variables describe what is measured on each observational unit.
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
      <li>How variables relate to observational units (rows) and measurements (columns).</li>
      <li>Conceptual roles such as predictors/outcomes and independent/dependent variables.</li>
      <li>Why variables are defined by choices, not discovered as facts.</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Why this topic matters</h2>

    <p>
      Once the observational unit is defined, the next question is:
      <strong>What is measured on each unit?</strong>
      The answer defines the variables.
    </p>

    <p>
      Many disagreements in analysis come from different variable definitions,
      not from different calculations. Two analysts can use the same raw records,
      but operationalize the concepts differently.
    </p>

    <p>
      Treating variables as choices reduces false certainty and clarifies what
      conclusions actually mean.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>What a variable is</h2>

    <p>
      A <strong>variable</strong> is a characteristic that can take different values across observational units.
      In a dataset, a variable typically appears as a <strong>column</strong>, and each row is the value of that variable
      for one unit.
    </p>

    <p>
      Age, income, temperature, category labels, and test scores are all variables
      if they vary across observations.
    </p>

    <p>
      Statistics exists because of variation. If there is no variation, many statistical
      questions become meaningless.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Units → Variables → Values (mental model)</h2>

    <div style="margin:22px 0; text-align:center;">
      <svg width="100%" height="260" viewBox="0 0 980 260" xmlns="http://www.w3.org/2000/svg">
        <text x="490" y="28" text-anchor="middle" font-size="18" font-weight="700" fill="#1c1c1c">
          How Variables Appear in a Dataset
        </text>

        <rect x="50" y="60" width="260" height="70" rx="12" fill="#e6fcf5" stroke="#099268" stroke-width="2"/>
        <text x="180" y="92" text-anchor="middle" font-size="16" font-weight="700" fill="#1c1c1c">Observational Units</text>
        <text x="180" y="112" text-anchor="middle" font-size="13" fill="#333">Rows (e.g., students)</text>

        <rect x="360" y="60" width="260" height="70" rx="12" fill="#fff3bf" stroke="#f08c00" stroke-width="2"/>
        <text x="490" y="92" text-anchor="middle" font-size="16" font-weight="700" fill="#1c1c1c">Variables</text>
        <text x="490" y="112" text-anchor="middle" font-size="13" fill="#333">Columns (e.g., age)</text>

        <rect x="670" y="60" width="260" height="70" rx="12" fill="#eef2ff" stroke="#3b5bdb" stroke-width="2"/>
        <text x="800" y="92" text-anchor="middle" font-size="16" font-weight="700" fill="#1c1c1c">Values</text>
        <text x="800" y="112" text-anchor="middle" font-size="13" fill="#333">Entries (e.g., 20, 21, 22)</text>

        <line x1="310" y1="95" x2="360" y2="95" stroke="#555" stroke-width="2" marker-end="url(#arrow)"/>
        <line x1="620" y1="95" x2="670" y2="95" stroke="#555" stroke-width="2" marker-end="url(#arrow)"/>

        <rect x="210" y="160" width="560" height="80" rx="12" fill="#f8f9fa" stroke="#333" stroke-width="2"/>
        <text x="490" y="188" text-anchor="middle" font-size="16" font-weight="700" fill="#1c1c1c">Dataset</text>
        <text x="490" y="210" text-anchor="middle" font-size="13" fill="#333">Rows = units • Columns = variables • Cells = values</text>

        <defs>
          <marker id="arrow" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
            <path d="M0,0 L0,6 L9,3 z" fill="#555" />
          </marker>
        </defs>
      </svg>

      <p style="font-size:14px; color:#666; margin-top:10px;">
        Figure. A variable is a rule that assigns a value to each observational unit.
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Variable vs constant</h2>

    <p>
      A <strong>variable</strong> changes across observational units.
      A <strong>constant</strong> does not.
    </p>

    <p>
      Constants may be important context, but they do not explain differences across units
      because they show no variation.
    </p>

    <div style="margin:24px 0;">
      <div style="max-width:850px; margin:auto; overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; background:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 4px 10px rgba(0,0,0,0.05);">
          <thead style="background:#f1f3f5;">
            <tr>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Variable</th>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Constant</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Differs across units</td>
              <td style="padding:12px 16px;">Same for all units (in this dataset)</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Can explain differences</td>
              <td style="padding:12px 16px;">Provides context but not variation</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Age, score, blood pressure</td>
              <td style="padding:12px 16px;">Exam date (same for all students)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <p>
      A “constant” can become a variable if the unit changes.
      For example, exam date is constant within one class (one exam session),
      but becomes a variable if your units are multiple exam sessions across a semester.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Simple example</h2>

    <p>
      Imagine a class of students taking the same exam.
    </p>

    <p>
      The <strong>exam score</strong> is a <strong>variable</strong> because it differs from student to student.
      The <strong>exam date</strong> is a <strong>constant</strong> because everyone took it on the same day.
    </p>

    <p>
      The exam date provides context, but it does not help explain why some students scored higher
      because it does not vary across students.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Variable roles depend on the question</h2>

    <p>
      Variables are often described using roles such as
      <strong>predictor/outcome</strong> or <strong>independent/dependent</strong>.
      These roles are not fixed properties of the variable; they depend on the question being asked.
    </p>

    <p>
      The same variable can be an outcome in one analysis and a predictor in another.
    </p>

    <div style="margin:24px 0;">
      <div style="max-width:850px; margin:auto; overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; background:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 4px 10px rgba(0,0,0,0.05);">
          <thead style="background:#f1f3f5;">
            <tr>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Role language</th>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Meaning (conceptual)</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;"><strong>Outcome / Response / Dependent</strong></td>
              <td style="padding:12px 16px;">What you want to explain or predict</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;"><strong>Predictor / Explanatory / Independent</strong></td>
              <td style="padding:12px 16px;">What you think is related to changes in the outcome</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Simple example of roles</h2>

    <p>
      Suppose a teacher wants to understand why some students score higher than others.
    </p>

    <p>
      <strong>Hours studied</strong> may be treated as a <strong>predictor</strong> (independent variable),
      and <strong>exam score</strong> as the <strong>outcome</strong> (dependent variable).
    </p>

    <p>
      If the question changes—for example, “Does exam difficulty change study time?”—then
      the roles can change as well.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Why variables are choices, not facts</h2>

    <p>
      Variables do not exist independently of measurement and definition.
      Analysts decide how concepts are turned into recorded variables.
    </p>

    <p>
      For example, the concept “health” could be operationalized as blood pressure,
      BMI, a symptom score, a diagnosis category, or a composite index.
      Each choice produces a different variable and supports different conclusions.
    </p>

    <p>
      Choices about definitions, categories, scales, units, and transformations
      directly affect results. Treating variables as choices encourages transparency.
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
      A variable is a characteristic that varies across observational units.
      Variables differ from constants, their roles depend on the question,
      and their meaning depends on how we choose to define and measure them.
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
