---
layout: default
title: Binary Data
description: Understanding binary variables as a special case, why binary data are not simple, and how they are commonly misused in analysis.
permalink: /foundations/binary-data/
section: foundations
lesson_order: 11
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="Binary Data">
<meta name="esa-lesson-url" content="/foundations/binary-data/">

<a class="btn btn-primary" href="/foundations/discrete-vs-continuous-data/">
  Previous: Discrete vs Continuous Data
</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Binary Data</h1>

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — Applied examples and modeling connections will be expanded.
    </div>

    <p class="lead">
      Binary variables take only two possible values.
      Despite their simplicity, they form the foundation of many
      statistical models and require careful interpretation.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 11
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>What binary data are and how they arise.</li>
      <li>Why binary variables are categorical but numerically coded.</li>
      <li>How proportions summarize binary outcomes.</li>
      <li>Common analytical mistakes with binary variables.</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What is a binary variable?</h2>

    <p>
      A binary variable takes exactly two possible values.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">
      <li>Yes / No</li>
      <li>Success / Failure</li>
      <li>Pass / Fail</li>
      <li>Purchased / Not purchased</li>
      <li>Survived / Did not survive</li>
    </ul>

    <p>
      Binary variables are a special case of categorical data.
      They represent membership in one of two categories.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Binary coding: 0 and 1</h2>

    <p>
      Binary outcomes are often stored numerically as 0 and 1.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">
      <li>0 = No</li>
      <li>1 = Yes</li>
    </ul>

    <p>
      Although stored as numbers, these values represent categories,
      not quantities.
    </p>

    <p>
      The numbers 0 and 1 allow mathematical modeling,
      but their meaning is still categorical.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why binary data are statistically powerful</h2>

    <p>
      Despite having only two values, binary variables support
      rich statistical concepts.
    </p>

    <ul class="bullets">
      <li>The mean of a binary variable equals the proportion of 1s.</li>
      <li>Variance depends on the proportion.</li>
      <li>Probability models (e.g., Binomial) are built on binary outcomes.</li>
    </ul>

    <p>
      For example, if 70% of students pass an exam,
      the mean of the binary variable (1 = pass) equals 0.70.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Binary vs continuous comparison</h2>

    <div style="margin:24px 0;">
      <div style="max-width:900px; margin:auto; overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; background:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 4px 10px rgba(0,0,0,0.05);">
          <thead style="background:#f1f3f5;">
            <tr>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Binary Data</th>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Continuous Data</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Two possible outcomes</td>
              <td style="padding:12px 16px;">Infinite possible values</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Summarized by proportions</td>
              <td style="padding:12px 16px;">Summarized by mean and variance</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Modeled with Binomial-type models</td>
              <td style="padding:12px 16px;">Modeled with Normal-type models</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Common mistakes</h2>

    <ul class="bullets">
      <li>Treating binary data as continuous measurements.</li>
      <li>Using inappropriate correlation measures without considering interpretation.</li>
      <li>Ignoring base rates (proportions).</li>
      <li>Interpreting 0 and 1 as quantities rather than categories.</li>
    </ul>

    <p>
      The simplicity of binary data often leads to overconfidence.
      Proper analysis requires understanding what the variable represents.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why binary variables are foundational</h2>

    <p>
      Many statistical frameworks are built on binary outcomes:
    </p>

    <ul class="bullets">
      <li>Probability theory</li>
      <li>Hypothesis testing</li>
      <li>Logistic regression</li>
      <li>Machine learning classification</li>
    </ul>

    <p>
      Understanding binary data correctly prepares you for
      advanced statistical modeling.
    </p>
  </div>
</section>



<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      Binary variables take two values, but they are not trivial.
      They are categorical variables encoded numerically
      and form the basis of many statistical methods.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Binary data represent two categories.
      They are often coded as 0 and 1,
      summarized using proportions,
      and modeled using probability-based methods.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson introduces <strong>measurement scales</strong>,
      explaining nominal, ordinal, interval, and ratio scales
      and why scale determines valid statistical operations.
    </p>

    <a class="btn btn-primary" href="/foundations/measurement-scales/">
      Next: Measurement Scales
    </a>
  </div>
</section>
