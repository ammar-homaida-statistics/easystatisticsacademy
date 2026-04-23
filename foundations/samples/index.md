---
layout: default
title: Samples
description: Understanding what a sample is, why samples are necessary, how samples approximate populations, and intuitive ideas about sample size.
permalink: /foundations/samples/
section: foundations
lesson_order: 15
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="Samples">
<meta name="esa-lesson-url" content="/foundations/samples/">

<a class="btn btn-primary" href="/foundations/populations/">
  Previous: Populations
</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Samples</h1>

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — Visual illustrations and simulation examples will be added.
    </div>

    <p class="lead">
      Because populations are usually unreachable,
      statistical reasoning relies on samples.
      A sample is not the population—it is an approximation.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 15
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>What a sample is in statistical reasoning.</li>
      <li>Why sampling is necessary in practice.</li>
      <li>How samples relate to populations.</li>
      <li>How to think intuitively about sample size.</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Definition of a sample</h2>

    <p>
      A <strong>sample</strong> is a subset of a population
      that is actually observed and measured.
    </p>

    <p>
      It is the data we have access to,
      used to learn about a broader population.
    </p>

    <p>
      Every sample is linked to a population,
      whether that population is finite or conceptual.
    </p>

    <p>
  The goal of sampling is to use <strong>sample statistics</strong>
  to estimate <strong>population parameters</strong>.
</p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why samples are necessary</h2>

    <ul class="bullets">
      <li>Full population measurement is often too costly.</li>
      <li>Some populations are extremely large or infinite.</li>
      <li>Populations may change over time.</li>
      <li>Ethical or practical limits may restrict access.</li>
    </ul>

    <p>
      Sampling allows us to make informed conclusions
      without observing every unit.
    </p>

    <p>
      Statistics exists because complete observation
      is usually impossible.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Samples vs populations</h2>

    <div style="margin:24px 0;">
      <div style="max-width:900px; margin:auto; overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; background:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 4px 10px rgba(0,0,0,0.05); font-size:14px;">
          <thead style="background:#f1f3f5;">
            <tr>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Population</th>
              <th style="padding:14px 16px; text-align:left; font-weight:600;">Sample</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Entire set of units of interest</td>
              <td style="padding:12px 16px;">Subset that is observed</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Described by parameters</td>
              <td style="padding:12px 16px;">Described by statistics</td>
            </tr>
            <tr style="border-top:1px solid #e9ecef;">
              <td style="padding:12px 16px;">Usually unknown</td>
              <td style="padding:12px 16px;">Observed and measurable</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <p>
      A <strong>parameter</strong> describes a population.
      A <strong>statistic</strong> describes a sample.
    </p>

    <p>
  In practice, we use statistics to make inferences about parameters.
</p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Samples as approximations</h2>

    <p>
      A sample does not reproduce a population exactly.
      Instead, it provides an estimate of population values.
    </p>

    <p>
      If we take different samples from the same population,
      we will get different results.
    </p>

    <p>
      This natural variation is called <strong>sampling error</strong>.
      It is not a mistake — it is an inherent part of using samples.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Example</h2>

    <p>
      Suppose the true average height of all students in a university is unknown.
    </p>

    <p>
      We take a sample of 50 students and compute:
    </p>

    <ul class="bullets">
      <li>Sample mean = 168 cm</li>
    </ul>

    <p>
      If we take another sample, we might get:
    </p>

    <ul class="bullets">
      <li>Sample mean = 171 cm</li>
    </ul>

    <p>
      Both are estimates of the same population value,
      but they differ due to sampling variability.
    </p>
  </div>
</section>


<section class="section">
  <div class="content-narrow">
    <h2>Intuition about sample size</h2>

    <p>
      Larger samples tend to produce more stable estimates.
    </p>

    <p>
      Small samples fluctuate more due to random variation.
    </p>

    <p>
      However, increasing sample size reduces variability
      but never removes uncertainty entirely.
    </p>

    <p style="font-weight:600;">
  Larger samples reduce variability, but do not eliminate uncertainty.
</p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Representativeness</h2>

    <p>
      Sample size alone is not enough.
      A large but biased sample can still produce misleading conclusions.
    </p>

    <p>
      How the sample is selected matters as much as how large it is.
    </p>

    <p>
      Representativeness is central to reliable inference.
    </p>

    <p>
  A biased sample leads to <strong>systematic error</strong>,
  which cannot be fixed by increasing sample size.
</p>
  </div>
</section>



<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      A sample is a necessary approximation of a population.
      It introduces uncertainty, but makes inference possible.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Samples are subsets of populations used for learning.
      They provide estimates of unknown population parameters.
      Sampling introduces variability but enables statistical reasoning.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson introduces <strong>sampling variability</strong>,
      explaining why different samples produce different results
      and how randomness differs from error.
    </p>

    <a class="btn btn-primary" href="/foundations/sampling-variability/">
      Next: Sampling Variability
    </a>
  </div>
</section>
