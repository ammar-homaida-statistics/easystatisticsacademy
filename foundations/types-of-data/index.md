---
layout: default
title: Types of Data
description: An introduction to qualitative and quantitative data, why this distinction is fundamental, and how misclassification leads to errors.
permalink: /foundations/types-of-data/
section: foundations
lesson_order: 9
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="Types of Data">
<meta name="esa-lesson-url" content="/foundations/types-of-data/">

<a class="btn btn-primary" href="/foundations/datasets-as-structures/">
  Previous: Datasets as Structures
</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Types of Data</h1>

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — This lesson will later include visual summaries and classification diagrams.
    </div>

    <p class="lead">
      Every variable must be classified correctly before analysis.
      The most fundamental distinction is between qualitative (categorical)
      and quantitative (numerical) data.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 9
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>What qualitative (categorical) data are.</li>
      <li>What quantitative (numerical) data are.</li>
      <li>Subtypes within each category.</li>
      <li>Why misclassification leads to invalid analysis.</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why this topic matters</h2>

    <p>
      Statistical methods are not interchangeable.
      The type of data determines what operations are meaningful.
    </p>

    <p>
      Averages, differences, correlations, and regressions require numerical meaning.
      Frequency tables and proportions are appropriate for categorical meaning.
    </p>

    <p>
      If data are misclassified, conclusions can be mathematically correct
      but conceptually meaningless.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>The two fundamental types</h2>

    <div style="margin:24px 0;">
      <div style="max-width:900px; margin:auto; overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; background:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 4px 10px rgba(0,0,0,0.05);">
          <thead style="background:#f1f3f5;">
            <tr>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Qualitative (Categorical)</th>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Quantitative (Numerical)</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Represents categories or labels</td>
              <td style="padding:12px 16px;">Represents numerical quantities</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Describes type or group membership</td>
              <td style="padding:12px 16px;">Describes magnitude or amount</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Cannot be meaningfully averaged</td>
              <td style="padding:12px 16px;">Arithmetic operations are meaningful</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Examples: country, color, gender</td>
              <td style="padding:12px 16px;">Examples: age, income, height</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Qualitative data (categorical)</h2>

    <p>
      Qualitative data classify observations into groups.
      They answer the question: <em>What type?</em>
    </p>

    <h3>Two common subtypes</h3>

    <ul class="bullets">
      <li><strong>Nominal:</strong> Categories with no natural order (e.g., blood type, country).</li>
      <li><strong>Ordinal:</strong> Categories with an order but no measurable distance (e.g., low, medium, high).</li>
    </ul>

    <p>
      Even when ordinal categories are coded with numbers,
      the numbers represent order—not quantity.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Quantitative data (numerical)</h2>

    <p>
      Quantitative data measure amount or magnitude.
      They answer the question: <em>How much? How many?</em>
    </p>

    <p>
      Numerical values allow arithmetic operations such as
      addition, subtraction, and averaging.
    </p>

    <p>
      Quantitative data can be further divided into discrete and continuous types,
      which will be discussed in the next lesson.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Common misclassification errors</h2>

    <ul class="bullets">
      <li>Using averages for coded categories (e.g., averaging satisfaction scores 1–5 without caution).</li>
      <li>Treating identification numbers as numerical measurements.</li>
      <li>Confusing order with quantity in ordinal data.</li>
      <li>Ignoring the meaning behind how numbers are assigned.</li>
    </ul>

    <p>
      The key principle:
      <strong>Classification depends on meaning, not on how data are stored.</strong>
    </p>
  </div>
</section>



<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      The type of data determines which statistical summaries and methods are valid.
      Correct classification is a conceptual decision, not a formatting detail.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Data are either categorical or numerical.
      Categorical data describe types.
      Numerical data describe amounts.
      Misclassifying them leads to invalid conclusions.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson explores <strong>discrete and continuous data</strong>,
      clarifying how numerical variables differ in structure
      and why this distinction matters for statistical modeling.
    </p>

    <a class="btn btn-primary" href="/foundations/discrete-vs-continuous-data/">
      Next: Discrete vs Continuous Data
    </a>
  </div>
</section>
