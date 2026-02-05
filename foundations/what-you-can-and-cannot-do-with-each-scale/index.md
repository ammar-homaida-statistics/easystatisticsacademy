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

    <p class="lead">
      This lesson explains which comparisons and operations are valid for each
      measurement scale, why invalid operations are common, and how misuse
      appears in real-world analysis.
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
      <li>What comparisons are valid for each measurement scale.</li>
      <li>Which operations are invalid and why.</li>
      <li>Why statistical software allows invalid operations.</li>
      <li>Common real-world examples of misuse.</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Why this topic matters</h2>

    <p>
      Measurement scales determine what can be meaningfully compared or calculated.
    </p>

    <p>
      Many statistical errors occur not because calculations are incorrect,
      but because inappropriate operations are applied to the data.
    </p>

    <p>
      Understanding these limits helps prevent false conclusions
      even when results appear numerical and precise.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Valid comparisons</h2>

    <p>
      Each measurement scale supports specific types of comparisons.
    </p>

    <p>
      Nominal data allow equality or difference only,
      ordinal data allow ranking,
      interval data allow comparison of differences,
      and ratio data allow comparison of ratios.
    </p>

    <p>
      Using comparisons outside these limits removes
      the meaning of the results.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Invalid operations</h2>

    <p>
      Some operations are mathematically possible
      but statistically meaningless.
    </p>

    <p>
      Examples include averaging category codes,
      taking ratios of interval data,
      or interpreting rank differences as equal distances.
    </p>

    <p>
      Invalid operations produce numbers
      that have no real-world interpretation.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Why software allows invalid operations</h2>

    <p>
      Statistical software operates on numbers,
      not on the meaning of data.
    </p>

    <p>
      If values are stored numerically,
      software will often perform any requested calculation.
    </p>

    <p>
      Responsibility for validity therefore lies with the analyst,
      not the tool.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Real-world examples of misuse</h2>

    <p>
      Common examples include averaging satisfaction ratings,
      correlating ID numbers, or comparing temperature ratios.
    </p>

    <p>
      These practices are widespread in reports,
      dashboards, and automated analyses.
    </p>

    <p>
      Recognizing misuse requires understanding
      what the scale actually represents.
    </p>
  </div>
</section>

<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      Not everything that can be calculated
      should be calculated.
    </p>
  </div>
</section>

<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Measurement scales determine which comparisons
      and operations are meaningful.
      Ignoring these limits leads to invalid analysis.
    </p>
  </div>
</section>

<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson introduces <strong>populations</strong>,
      explaining what a population is, why populations are usually
      unreachable, and how this shapes statistical reasoning.
    </p>

    <a class="btn btn-primary" href="/foundations/populations/">
      Next: Populations
    </a>
  </div>
</section>