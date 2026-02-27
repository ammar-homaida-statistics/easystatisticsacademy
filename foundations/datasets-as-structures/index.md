---
layout: default
title: Datasets as Structures
description: Understanding datasets as structured collections of rows and columns, and why structure determines what analysis is possible.
permalink: /foundations/datasets-as-structures/
section: foundations
lesson_order: 8
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="Datasets as Structures">
<meta name="esa-lesson-url" content="/foundations/datasets-as-structures/">

<a class="btn btn-primary" href="/foundations/variables/">
  Previous: Variables
</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Datasets as Structures</h1>

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — This lesson is being expanded with structural diagrams and format comparisons.
    </div>

    <p class="lead">
      A dataset is not just a collection of values.
      It is a structured system of rows and columns.
      That structure determines what analysis is possible.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 8
    </p>
  </div>
</section>


<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>How datasets are organized using rows and columns.</li>
      <li>The conceptual difference between wide and long structures.</li>
      <li>How structure encodes assumptions about units and variables.</li>
      <li>Why dataset structure limits or enables statistical methods.</li>
    </ul>
  </div>
</section>


<section class="section">
  <div class="content-narrow">
    <h2>Rows and columns define structure</h2>

    <p>
      In most statistical contexts, a dataset follows a simple structural rule:
    </p>

    <ul class="bullets">
      <li><strong>Rows represent observational units.</strong></li>
      <li><strong>Columns represent variables.</strong></li>
      <li><strong>Cells contain values.</strong></li>
    </ul>

    <p>
      This structure is conceptual. It exists whether the data are stored
      in Excel, SPSS, R, Python, or a database.
    </p>

    <p>
      When rows or columns are misaligned with the research question,
      statistical interpretation becomes invalid.
    </p>
  </div>
</section>


<section class="section">
  <div class="content-narrow">
    <h2>Wide vs Long structures</h2>

    <p>
      The same information can often be organized in different structural formats.
      Two common formats are <strong>wide</strong> and <strong>long</strong>.
    </p>

    <div style="margin:24px 0;">
      <div style="max-width:900px; margin:auto; overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; background:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 4px 10px rgba(0,0,0,0.05);">
          <thead style="background:#f1f3f5;">
            <tr>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Wide Format</th>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Long Format</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Multiple measurements stored in separate columns</td>
              <td style="padding:12px 16px;">Measurements stored in one column</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Each row = one unit</td>
              <td style="padding:12px 16px;">Each row = one unit at one time/condition</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Good for simple summaries</td>
              <td style="padding:12px 16px;">Required for many statistical models</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</section>


<section class="section">
  <div class="content-narrow">
    <h2>Visual example</h2>

    <div style="margin:20px 0; text-align:center;">
      <svg width="100%" height="300" viewBox="0 0 1000 300" xmlns="http://www.w3.org/2000/svg">

        <text x="250" y="30" text-anchor="middle" font-size="18" font-weight="700">
          Wide Format
        </text>

        <rect x="80" y="60" width="340" height="160" rx="10" fill="#e7f5ff" stroke="#1c7ed6" stroke-width="2"/>
        <text x="250" y="100" text-anchor="middle" font-size="14">Student | Exam1 | Exam2</text>
        <text x="250" y="125" text-anchor="middle" font-size="14">A | 80 | 85</text>
        <text x="250" y="150" text-anchor="middle" font-size="14">B | 75 | 88</text>

        <text x="750" y="30" text-anchor="middle" font-size="18" font-weight="700">
          Long Format
        </text>

        <rect x="580" y="60" width="340" height="160" rx="10" fill="#fff4e6" stroke="#f08c00" stroke-width="2"/>
        <text x="750" y="100" text-anchor="middle" font-size="14">Student | Exam | Score</text>
        <text x="750" y="125" text-anchor="middle" font-size="14">A | 1 | 80</text>
        <text x="750" y="145" text-anchor="middle" font-size="14">A | 2 | 85</text>
        <text x="750" y="165" text-anchor="middle" font-size="14">B | 1 | 75</text>
        <text x="750" y="185" text-anchor="middle" font-size="14">B | 2 | 88</text>

        <line x1="430" y1="140" x2="570" y2="140" stroke="#333" stroke-width="2" marker-end="url(#arrow)" />

        <defs>
          <marker id="arrow" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
            <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
          </marker>
        </defs>

      </svg>

      <p style="font-size:14px; color:#666; margin-top:10px;">
        The same information can be represented in different structural forms.
      </p>
    </div>

  </div>
</section>


<section class="section">
  <div class="content-narrow">
    <h2>Structure determines analysis</h2>

    <p>
      Statistical methods assume specific dataset structures.
      For example:
    </p>

    <ul class="bullets">
      <li>Regression assumes one row per unit.</li>
      <li>Time series analysis assumes ordered observations over time.</li>
      <li>Repeated-measures models require long format structure.</li>
    </ul>

    <p>
      If the structure does not match the assumptions of the method,
      results may be misleading even if calculations are correct.
    </p>
  </div>
</section>


<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      A dataset is a structured system.
      Structure encodes assumptions about units, variables, and relationships.
      Analysis is valid only when structure matches the question.
    </p>
  </div>
</section>


<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Datasets are not neutral containers of numbers.
      Their structure determines what statistical questions can be answered
      and what methods are appropriate.
    </p>
  </div>
</section>


<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson introduces <strong>types of data</strong>,
      explaining qualitative and quantitative variables
      and why this distinction is fundamental.
    </p>

    <a class="btn btn-primary" href="/foundations/types-of-data/">
      Next: Types of Data
    </a>
  </div>
</section>
