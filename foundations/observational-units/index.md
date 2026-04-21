---
layout: default
title: Observational Units
description: Understand what observational units are and how they define the structure of your data.
permalink: /foundations/observational-units/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Foundations</span>
      <span class="badge">Data structure</span>
      <span class="badge">Core concept</span>
    </div>

    <h1>Observational Units</h1>

    <p class="lead">
      Learn what observational units are and how they define what each row in your dataset represents.
    </p>

    <div class="hero-actions">
      <a class="btn" href="#content">Start lesson</a>
      <a class="btn btn-outline" href="/foundations/">Back to Foundations</a>
    </div>

  </div>
</section>

<!-- CONTENT -->
<section class="section" id="content">

  <!-- DEFINITION -->
  <div class="section-block">
    <h2>What Is an Observational Unit?</h2>

    <p>
      An observational unit is the entity (object, person, event, or item)
      on which data is collected.
    </p>

    <p>
      In simple terms:
      <strong>it is "what each row represents" in your dataset.</strong>
    </p>
  </div>

  <!-- SIMPLE EXAMPLES -->
  <div class="section-block">
    <h2>Examples</h2>

    <ul class="bullets">
      <li>Students → if you collect exam scores</li>
      <li>Patients → if you collect medical data</li>
      <li>Products → if you analyze sales</li>
      <li>Days → if you record temperature</li>
    </ul>

    <p>
      Each of these becomes one row in your dataset.
    </p>
  </div>

  <!-- TABLE EXAMPLE -->
  <div class="section-block">
    <h2>Dataset Example</h2>

    <table style="width:100%; border-collapse:collapse; margin-top:10px;">
      <thead>
        <tr style="background:#f3f4f6;">
          <th style="padding:10px; border:1px solid #ddd;">Student</th>
          <th style="padding:10px; border:1px solid #ddd;">Height</th>
          <th style="padding:10px; border:1px solid #ddd;">Score</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">A</td>
          <td style="padding:10px; border:1px solid #ddd;">170</td>
          <td style="padding:10px; border:1px solid #ddd;">75</td>
        </tr>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">B</td>
          <td style="padding:10px; border:1px solid #ddd;">165</td>
          <td style="padding:10px; border:1px solid #ddd;">80</td>
        </tr>
      </tbody>
    </table>

    <p>
      Here:
    </p>

    <ul class="bullets">
      <li>Observational unit = <strong>Student</strong></li>
      <li>Each row = one student</li>
    </ul>
  </div>

  <!-- IMPORTANT INSIGHT -->
  <div class="section-block">
    <h2>Key Insight</h2>

    <p>
      The observational unit determines:
    </p>

    <ul class="bullets">
      <li>What your dataset represents</li>
      <li>What conclusions you can make</li>
      <li>What statistical methods are valid</li>
    </ul>

    <p>
      If you misunderstand the unit, your entire analysis can be wrong.
    </p>
  </div>

  <!-- DIFFERENT LEVELS -->
  <div class="section-block">
    <h2>Same Data, Different Units</h2>

    <p>
      The same real-world situation can be analyzed using different units.
    </p>

    <p><strong>Example: School data</strong></p>

    <ul class="bullets">
      <li>Students → individual-level data</li>
      <li>Classes → group-level data</li>
      <li>Schools → aggregated data</li>
    </ul>

    <p>
      Changing the unit changes the meaning of the analysis.
    </p>
  </div>

  <!-- COMMON MISTAKES -->
  <div class="section-block">
    <h2>Common Mistakes</h2>

    <ul class="bullets">
      <li>Confusing variables with observational units ❌</li>
      <li>Mixing multiple units in the same dataset ❌</li>
      <li>Not clearly defining what each row represents ❌</li>
    </ul>

    <p>
      Example mistake:
    </p>

    <ul class="bullets">
      <li>Rows represent both students and schools → incorrect structure</li>
    </ul>
  </div>

  <!-- NUMERICAL EXAMPLE -->
  <div class="section-block">
    <h2>Numerical Example</h2>

    <p>
      Suppose we record daily temperatures:
    </p>

    <p><strong>22, 24, 19, 21</strong></p>

    <p>
      What is the observational unit?
    </p>

    <ul class="bullets">
      <li>Each <strong>day</strong> is an observational unit</li>
    </ul>

    <p>
      Not the temperature itself — but the entity being measured.
    </p>
  </div>

  <!-- WHY IMPORTANT -->
  <div class="section-block">
    <h2>Why This Matters</h2>

    <p>
      Observational units define the structure of your dataset.
    </p>

    <p>
      Without this clarity:
    </p>

    <ul class="bullets">
      <li>analysis becomes inconsistent</li>
      <li>results become misleading</li>
      <li>interpretation becomes wrong</li>
    </ul>

    <p>
      Good statistical practice always starts with:
      <strong>clearly identifying the observational unit.</strong>
    </p>
  </div>

  <!-- CONNECTION -->
  <div class="section-block">
    <h2>What Comes Next?</h2>

    <p>
      Once we know the observational unit, the next question is:
    </p>

    <ul class="bullets">
      <li>What are we measuring about each unit?</li>
    </ul>

    <p>
      These measurements are called <strong>variables</strong>.
    </p>
  </div>

</section>

<!-- NAVIGATION -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next steps</h2>

      <div class="hero-actions">

        <a class="btn btn-outline" href="/foundations/what-is-data/">
          ← Previous: What Is Data
        </a>

        <a class="btn btn-outline" href="/foundations/">
          Foundations Home
        </a>

        <a class="btn" href="/foundations/variables/">
          Next: Variables →
        </a>

      </div>

    </div>

  </div>
</section>