---
layout: default
title: Bias
description: Understanding what bias is, common forms of bias, and why bias is systematic rather than random.
permalink: /foundations/bias/
section: foundations
lesson_order: 25
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="Bias">
<meta name="esa-lesson-url" content="/foundations/bias/">

<a class="btn btn-primary" href="/foundations/ethical-considerations-in-data-collection/">
  Previous: Ethical Considerations in Data Collection
</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Bias</h1>

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — Real-world bias examples (polling errors, algorithmic bias, survey bias) will be added.
    </div>

    <p class="lead">
      Bias is one of the most important and most misunderstood concepts in statistics.
      It is not random noise—it is systematic distortion that pushes results away from the truth.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 25
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>What bias means in statistical reasoning.</li>
      <li>Why bias is systematic rather than random.</li>
      <li>Common forms: sampling, measurement, and selection bias.</li>
      <li>Why more data does not fix bias.</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why this topic matters</h2>

    <p>
      Bias affects conclusions before any analysis begins.
    </p>

    <p>
      A biased dataset can produce precise,
      consistent, and completely misleading results.
    </p>

    <p>
      Understanding bias is essential for deciding
      whether results should be trusted at all.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What bias is</h2>

    <p>
      Bias is a <strong>systematic deviation</strong>
      between a result and the true value it aims to estimate.
    </p>

    <p>
      It is not random variation.
      It pushes results consistently in a particular direction.
    </p>

    <p>
      Bias can lead to:
    </p>

    <ul class="bullets">
      <li>Consistent overestimation</li>
      <li>Consistent underestimation</li>
      <li>Distorted relationships between variables</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Bias vs variability</h2>

    <p>
      It is important to distinguish bias from variability.
    </p>

    <ul class="bullets">
      <li><strong>Variability:</strong> results change randomly from sample to sample</li>
      <li><strong>Bias:</strong> results are consistently shifted in one direction</li>
    </ul>

    <p>
      A result can be:
    </p>

    <ul class="bullets">
      <li>Unbiased but variable</li>
      <li>Biased but consistent</li>
      <li>Both biased and variable</li>
    </ul>

    <p style="font-weight:600;">
      Consistency does not imply correctness.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Sampling bias</h2>

    <p>
      Sampling bias occurs when some members of the population
      are more likely to be included than others.
    </p>

    <p>
      The sample then systematically differs
      from the population.
    </p>

    <p>
      Example:
      surveying only online users excludes those without internet access.
    </p>

    <p style="font-weight:600;">
      A large biased sample is still biased.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Measurement bias</h2>

    <p>
      Measurement bias occurs when the way data are collected
      systematically distorts values.
    </p>

    <p>
      Sources include:
    </p>

    <ul class="bullets">
      <li>Leading or unclear survey questions</li>
      <li>Faulty instruments</li>
      <li>Consistent reporting errors</li>
    </ul>

    <p>
      Measurement bias affects the data itself,
      not just the analysis.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Selection bias</h2>

    <p>
      Selection bias occurs when inclusion in a study
      depends on factors related to the outcome.
    </p>

    <p>
      This creates misleading relationships between variables.
    </p>

    <p>
      It is especially common in:
    </p>

    <ul class="bullets">
      <li>Voluntary participation studies</li>
      <li>Observational data</li>
      <li>Incomplete datasets</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why bias does not disappear</h2>

    <p>
      Random error tends to cancel out with larger samples.
    </p>

    <p>
      Bias does not.
    </p>

    <p>
      Increasing sample size only makes biased results
      more precise—not more accurate.
    </p>

    <p style="font-weight:600;">
      More data can reinforce bias rather than fix it.
    </p>
  </div>
</section>



<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      Bias is systematic distortion.
      It cannot be fixed by increasing sample size or using more advanced methods.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Bias causes results to differ from the truth in a consistent direction.
      It arises from flawed sampling, measurement, or selection,
      and it remains even with large datasets.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson explains the difference between
      <strong>random error</strong> and <strong>systematic error</strong>,
      and why increasing sample size affects them differently.
    </p>

    <a class="btn btn-primary" href="/foundations/random-error-vs-systematic-error/">
      Next: Random Error vs Systematic Error
    </a>
  </div>
</section>

<script>
  try {
    localStorage.setItem("esa:lastLesson", window.location.pathname);
  } catch (e) {}
</script>
