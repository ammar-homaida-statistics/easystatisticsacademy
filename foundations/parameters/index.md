---
layout: default
title: Parameters
description: Understanding what parameters are, why they are fixed but unknown, and why parameters cannot be directly observed.
permalink: /foundations/parameters/
section: foundations
lesson_order: 17
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="Parameters">
<meta name="esa-lesson-url" content="/foundations/parameters/">

<a class="btn btn-primary" href="/foundations/sampling-variability/">
  Previous: Sampling Variability
</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Parameters</h1>

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — Formal notation examples will be added.
    </div>

    <p class="lead">
      A parameter is a numerical characteristic of a population.
      It is fixed for a given population, but typically unknown.
      Statistical inference exists to estimate parameters.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 17
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>What a parameter represents in statistical reasoning.</li>
      <li>Why parameters are fixed but unknown.</li>
      <li>Common examples of population parameters.</li>
      <li>Why parameters cannot be directly observed.</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why this topic matters</h2>

    <p>
      Statistical analysis is not primarily about describing samples.
      It is about learning about populations.
    </p>

    <p>
      The quantities we truly care about are population characteristics.
      These are called parameters.
    </p>

    <p>
      Confusing parameters with sample results leads to
      overconfidence and incorrect interpretation.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What a parameter is</h2>

    <p>
      A <strong>parameter</strong> is a numerical summary
      describing a population.
    </p>

    <p>
      It refers to the entire set of units,
      not just the observed sample.
    </p>

    <p>
      Parameters exist conceptually even when they are not measured exactly.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Fixed but unknown</h2>

    <p>
      For a given population, a parameter has one true value.
    </p>

    <p>
      That value does not change from sample to sample.
    </p>

    <p>
      What changes is our estimate of it,
      not the parameter itself.
    </p>

    <p style="font-weight:600;">
      Parameter → Fixed  
      Statistic → Variable
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Examples of parameters</h2>

    <div style="margin:24px 0;">
      <div style="max-width:900px; margin:auto; overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; background:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 4px 10px rgba(0,0,0,0.05); font-size:14px;">
          <thead style="background:#f1f3f5;">
            <tr>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Parameter</th>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Meaning</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Population mean</td>
              <td style="padding:12px 16px;">Average value across entire population</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Population proportion</td>
              <td style="padding:12px 16px;">True fraction with a given characteristic</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Population variance</td>
              <td style="padding:12px 16px;">True variability within the population</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <p>
      These parameters summarize properties of the entire population,
      even when we do not know their exact values.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why parameters are not directly observed</h2>

    <p>
      Observing a parameter exactly would require measuring
      every unit in the population.
    </p>

    <p>
      In most real-world situations, this is impossible
      due to cost, time, or conceptual infinity.
    </p>

    <p>
      Therefore, parameters remain unknown
      and must be estimated using samples.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Conceptual distinction</h2>

    <p>
      Parameters belong to populations.
    </p>

    <p>
      Statistics belong to samples.
    </p>

    <p>
      Inference connects the two.
    </p>
  </div>
</section>



<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      A parameter is a fixed but unknown numerical characteristic
      of a population.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Parameters describe populations.
      They do not change from sample to sample,
      but they are usually unknown.
      Statistical methods aim to estimate them.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson introduces <strong>statistics</strong>,
      explaining how sample summaries vary and how they are used
      to estimate unknown parameters.
    </p>

    <a class="btn btn-primary" href="/foundations/statistics/">
      Next: Statistics
    </a>
  </div>
</section>
