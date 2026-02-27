---
layout: default
title: Discrete vs Continuous Data
description: Understanding the difference between discrete and continuous data, how measurement differs from conceptual continuity, and why this matters for statistical methods.
permalink: /foundations/discrete-vs-continuous-data/
section: foundations
lesson_order: 10
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="Discrete vs Continuous Data">
<meta name="esa-lesson-url" content="/foundations/discrete-vs-continuous-data/">

<a class="btn btn-primary" href="/foundations/types-of-data/">
  Previous: Types of Data
</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Discrete vs Continuous Data</h1>

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — Visual illustrations and applied examples will be added.
    </div>

    <p class="lead">
      Numerical variables can behave in fundamentally different ways.
      Some arise from counting. Others arise from measurement.
      This distinction affects modeling, visualization, and interpretation.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 10
    </p>
  </div>
</section>


<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>What discrete data are and how they arise.</li>
      <li>What continuous data are and how they differ conceptually.</li>
      <li>Why rounding does not make continuous data discrete.</li>
      <li>Why statistical methods depend on this distinction.</li>
    </ul>
  </div>
</section>


<section class="section">
  <div class="content-narrow">
    <h2>The core distinction</h2>

    <div style="margin:24px 0;">
      <div style="max-width:900px; margin:auto; overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; background:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 4px 10px rgba(0,0,0,0.05);">
          <thead style="background:#f1f3f5;">
            <tr>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Discrete Data</th>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Continuous Data</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Arise from counting</td>
              <td style="padding:12px 16px;">Arise from measurement</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Take separate, distinct values</td>
              <td style="padding:12px 16px;">Can take any value within a range</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Gaps exist between possible values</td>
              <td style="padding:12px 16px;">No conceptual gaps between values</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Example: number of customers</td>
              <td style="padding:12px 16px;">Example: height, time, temperature</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</section>


<section class="section">
  <div class="content-narrow">
    <h2>Visual intuition</h2>

    <div style="margin:20px 0; text-align:center;">
      <svg width="100%" height="260" viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg">

        <text x="220" y="30" text-anchor="middle" font-size="18" font-weight="700">
          Discrete
        </text>

        <line x1="60" y1="150" x2="380" y2="150" stroke="#333" stroke-width="2"/>

        <circle cx="120" cy="150" r="6" fill="#1c7ed6"/>
        <circle cx="200" cy="150" r="6" fill="#1c7ed6"/>
        <circle cx="280" cy="150" r="6" fill="#1c7ed6"/>

        <text x="680" y="30" text-anchor="middle" font-size="18" font-weight="700">
          Continuous
        </text>

        <line x1="520" y1="150" x2="840" y2="150" stroke="#f08c00" stroke-width="4"/>

      </svg>

      <p style="font-size:14px; color:#666; margin-top:10px;">
        Discrete values appear as separate points.
        Continuous values form an unbroken line.
      </p>
    </div>

  </div>
</section>


<section class="section">
  <div class="content-narrow">
    <h2>Measurement vs rounding</h2>

    <p>
      Continuous variables are often recorded with limited precision.
      For example, height may be recorded as 172 cm.
    </p>

    <p>
      However, rounding does not make the underlying variable discrete.
      Height remains conceptually continuous.
    </p>

    <p>
      The distinction depends on the nature of the phenomenon,
      not on how many decimal places are recorded.
    </p>
  </div>
</section>


<section class="section">
  <div class="content-narrow">
    <h2>Why this matters for statistical methods</h2>

    <ul class="bullets">
      <li>Count data often use probability models like Binomial or Poisson.</li>
      <li>Continuous data often use Normal-based models.</li>
      <li>Visualization differs (bar charts vs histograms).</li>
      <li>Interpretation differs (counts vs measured magnitudes).</li>
    </ul>

    <p>
      Choosing a method that does not match the data type
      can produce misleading conclusions even if calculations are correct.
    </p>
  </div>
</section>


<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      Discrete data arise from counting.
      Continuous data arise from measurement.
      The distinction is conceptual and determines valid analysis methods.
    </p>
  </div>
</section>


<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Discrete values are separate and countable.
      Continuous values form an unbroken range.
      Understanding this difference is essential for statistical modeling.
    </p>
  </div>
</section>


<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson focuses on <strong>binary data</strong>,
      explaining why binary variables are a special case
      and how they are treated in statistical analysis.
    </p>

    <a class="btn btn-primary" href="/foundations/binary-data/">
      Next: Binary Data
    </a>
  </div>
</section>
