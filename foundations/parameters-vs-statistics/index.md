---
layout: default
title: Parameters vs Statistics
description: A clear comparison between parameters and statistics, common student errors, and why confusing them breaks statistical inference.
permalink: /foundations/parameters-vs-statistics/
section: foundations
lesson_order: 19
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="Parameters vs Statistics">
<meta name="esa-lesson-url" content="/foundations/parameters-vs-statistics/">

<a class="btn btn-primary" href="/foundations/statistics/">
  Previous: Statistics
</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Parameters vs Statistics</h1>

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — Visual comparison diagram will be added.
    </div>

    <p class="lead">
      Parameters and statistics are fundamentally different concepts.
      Confusing them removes uncertainty and breaks statistical inference.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 19
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>The conceptual difference between parameters and statistics.</li>
      <li>Why one is fixed and the other varies.</li>
      <li>Common student errors when distinguishing them.</li>
      <li>Why inference depends on keeping them separate.</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>The core distinction</h2>

    <div style="margin:24px 0;">
      <div style="max-width:900px; margin:auto; overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; background:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 4px 10px rgba(0,0,0,0.05); font-size:14px;">
          <thead style="background:#f1f3f5;">
            <tr>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Parameter</th>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Statistic</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Describes a population</td>
              <td style="padding:12px 16px;">Describes a sample</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Fixed (given the population)</td>
              <td style="padding:12px 16px;">Random (depends on the sample)</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Usually unknown</td>
              <td style="padding:12px 16px;">Observed and computable</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Target of inference</td>
              <td style="padding:12px 16px;">Tool used for inference</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <p style="font-weight:600;">
      Parameter → Fixed but unknown  
      Statistic → Variable but observable
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why students confuse them</h2>

    <ul class="bullets">
      <li>Both are numerical summaries.</li>
      <li>Both may use similar formulas.</li>
      <li>Notation sometimes looks similar.</li>
      <li>Textbooks often move quickly between the two.</li>
    </ul>

    <p>
      Because the numbers may look similar,
      the conceptual difference is often overlooked.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Common student errors</h2>

    <p>
      Referring to a sample mean as “the true average.”
    </p>

    <p>
      Believing that one statistic equals the parameter exactly.
    </p>

    <p>
      Ignoring sampling variability when interpreting results.
    </p>

    <p>
      Assuming larger samples remove all uncertainty.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why confusing them breaks inference</h2>

    <p>
      Statistical inference depends on uncertainty.
    </p>

    <p>
      If a statistic is treated as if it were the parameter,
      uncertainty disappears incorrectly.
    </p>

    <p>
      Without recognizing variability,
      concepts such as confidence intervals
      and hypothesis testing lose meaning.
    </p>

    <p>
      Inference exists precisely because
      statistics are not parameters.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>The logic of inference</h2>

    <p>
      We observe a statistic.
    </p>

    <p>
      We acknowledge it varies.
    </p>

    <p>
      We use probability to describe its variability.
    </p>

    <p>
      We draw conclusions about the fixed parameter.
    </p>
  </div>
</section>



<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      Parameters are population truths.
      Statistics are sample-based evidence.
      Inference connects the two.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      A parameter is fixed but unknown.
      A statistic is observable but variable.
      Confusing the two eliminates uncertainty
      and undermines statistical reasoning.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson explains the difference between
      <strong>data collection</strong> and <strong>data analysis</strong>,
      and why poor data collection cannot be fixed by analysis.
    </p>

    <a class="btn btn-primary" href="/foundations/data-collection-vs-data-analysis/">
      Next: Data Collection vs Data Analysis
    </a>
  </div>
</section>
