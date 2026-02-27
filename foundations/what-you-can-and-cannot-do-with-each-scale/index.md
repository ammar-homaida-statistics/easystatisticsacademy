---
layout: default
title: What You Can and Cannot Do With Each Scale
description: Understanding valid comparisons, invalid operations, and common misuse of measurement scales in statistical analysis.
permalink: /foundations/what-you-can-and-cannot-do-with-each-scale/
section: foundations
lesson_order: 13
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="What You Can and Cannot Do With Each Scale">
<meta name="esa-lesson-url" content="/foundations/what-you-can-and-cannot-do-with-each-scale/">

<a class="btn btn-primary" href="/foundations/measurement-scales/">
  Previous: Measurement Scales
</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>What You Can and Cannot Do With Each Scale</h1>

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — Applied case studies and interactive examples will be added.
    </div>

    <p class="lead">
      Measurement scales define which statistical operations are meaningful.
      Many analytical errors arise not from incorrect formulas,
      but from applying valid mathematics to invalid scales.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 13
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>Which comparisons are valid for each scale.</li>
      <li>Which operations are invalid and why.</li>
      <li>Why software does not protect against misuse.</li>
      <li>Common real-world analytical mistakes.</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Allowed vs not allowed operations</h2>

    <div style="margin:24px 0;">
      <div style="max-width:1100px; margin:auto; overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; background:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 4px 10px rgba(0,0,0,0.05); font-size:14px;">
          <thead style="background:#f1f3f5;">
            <tr>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Scale</th>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Valid Operations</th>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Invalid Operations</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;"><strong>Nominal</strong></td>
              <td style="padding:12px 16px;">Equality, frequency, proportions</td>
              <td style="padding:12px 16px;">Averaging, ordering, ratios</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;"><strong>Ordinal</strong></td>
              <td style="padding:12px 16px;">Ranking, median, percentiles</td>
              <td style="padding:12px 16px;">Meaningful differences, ratios</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;"><strong>Interval</strong></td>
              <td style="padding:12px 16px;">Addition, subtraction, mean</td>
              <td style="padding:12px 16px;">Meaningful ratios</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;"><strong>Ratio</strong></td>
              <td style="padding:12px 16px;">All arithmetic operations</td>
              <td style="padding:12px 16px;">—</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Common invalid examples</h2>

    <h3>1. Averaging category codes</h3>
    <p>
      Suppose job categories are coded as:
      1 = Teacher, 2 = Engineer, 3 = Doctor.
    </p>
    <p>
      The mean of these codes has no meaningful interpretation.
    </p>

    <h3>2. Averaging ordinal satisfaction scores</h3>
    <p>
      Satisfaction levels (1–5) are ordinal.
      The difference between 1 and 2 may not equal the difference between 4 and 5.
    </p>
    <p>
      Means are often used, but interpretation must be cautious.
    </p>

    <h3>3. Ratio interpretation of temperature</h3>
    <p>
      20°C is not “twice as hot” as 10°C,
      because Celsius is an interval scale with arbitrary zero.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why software allows misuse</h2>

    <p>
      Statistical software performs numerical operations
      without understanding scale meaning.
    </p>

    <p>
      If ordinal values are stored as numbers,
      software will calculate means and correlations automatically.
    </p>

    <p>
      Valid interpretation depends on the analyst,
      not on the tool.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Conceptual principle</h2>

    <p>
      The rule is simple:
    </p>

    <p style="font-weight:600;">
      Mathematical possibility does not guarantee meaningful interpretation.
    </p>

    <p>
      Statistical reasoning requires understanding
      what numbers represent before operating on them.
    </p>
  </div>
</section>



<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      Not every numerical calculation is meaningful.
      Measurement scale determines what comparisons and operations
      are valid.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Nominal allows classification.
      Ordinal allows ranking.
      Interval allows meaningful differences.
      Ratio allows meaningful ratios.
      Violating these limits leads to invalid analysis.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson introduces <strong>populations</strong>,
      explaining why the population is often conceptual,
      rarely fully observed, and central to statistical inference.
    </p>

    <a class="btn btn-primary" href="/foundations/populations/">
      Next: Populations
    </a>
  </div>
</section>
