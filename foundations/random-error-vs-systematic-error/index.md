---
layout: default
title: Random Error vs Systematic Error
description: Understanding the difference between random error and systematic error, noise versus bias, and why increasing sample size affects them differently.
permalink: /foundations/random-error-vs-systematic-error/
section: foundations
lesson_order: 26
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="Random Error vs Systematic Error">
<meta name="esa-lesson-url" content="/foundations/random-error-vs-systematic-error/">

<a class="btn btn-primary" href="/foundations/bias/">
  Previous: Bias
</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Random Error vs Systematic Error</h1>

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — Visual diagrams (target analogy, accuracy vs precision) will be added.
    </div>

    <p class="lead">
      Not all error behaves the same way.
      Some error creates variability.
      Other error creates consistent distortion.
      Understanding this difference is essential for interpreting data correctly.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 26
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>The difference between random error and systematic error.</li>
      <li>How noise differs from bias.</li>
      <li>Why increasing sample size reduces random error.</li>
      <li>Why systematic error persists regardless of sample size.</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why this topic matters</h2>

    <p>
      Many data problems are described simply as “error,”
      but different types of error behave in fundamentally different ways.
    </p>

    <p>
      Confusing these types leads to incorrect conclusions,
      especially when interpreting large datasets.
    </p>

    <p>
      Understanding this distinction is essential
      for evaluating reliability and accuracy.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Random error</h2>

    <p>
      Random error refers to unpredictable variation
      that changes from observation to observation.
    </p>

    <p>
      It arises from natural variability,
      measurement imprecision, and chance.
    </p>

    <p>
      Random error produces <strong>noise</strong>—
      variation without a consistent direction.
    </p>

    <p>
      Over many observations, random error tends to cancel out.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Systematic error</h2>

    <p>
      Systematic error consistently shifts results
      in a particular direction.
    </p>

    <p>
      It arises from bias in sampling,
      measurement, or study design.
    </p>

    <p>
      Systematic error produces <strong>bias</strong>—
      directional distortion away from the truth.
    </p>

    <p>
      Unlike random error, it does not cancel out.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Noise vs bias</h2>

    <ul class="bullets">
      <li><strong>Noise (random error):</strong> variability without direction</li>
      <li><strong>Bias (systematic error):</strong> consistent shift in one direction</li>
    </ul>

    <p>
      Both affect results,
      but they affect them in fundamentally different ways.
    </p>

    <p style="font-weight:600;">
      Noise makes results unstable.  
      Bias makes results wrong.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Accuracy vs precision</h2>

    <p>
      Random error and systematic error relate closely
      to two important ideas:
    </p>

    <ul class="bullets">
      <li><strong>Precision:</strong> how consistent results are</li>
      <li><strong>Accuracy:</strong> how close results are to the truth</li>
    </ul>

    <p>
      Random error reduces precision.
      Systematic error reduces accuracy.
    </p>

    <p>
      A result can be very precise but still inaccurate
      if it is biased.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why sample size helps only one</h2>

    <p>
      Increasing sample size reduces random error
      by averaging out fluctuations.
    </p>

    <p>
      This makes results more stable and precise.
    </p>

    <p>
      However, systematic error remains unchanged.
    </p>

    <p style="font-weight:600;">
      More data can make a biased result
      more confidently wrong.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Conceptual example</h2>

    <p>
      Imagine measuring weight with a scale:
    </p>

    <ul class="bullets">
      <li>A slightly imprecise scale produces random variation.</li>
      <li>A miscalibrated scale produces systematic error.</li>
    </ul>

    <p>
      Repeating measurements reduces random variation,
      but does not fix miscalibration.
    </p>
  </div>
</section>



<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      More data reduce noise.
      They do not remove bias.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Random error creates variability and decreases with larger samples.
      Systematic error creates bias and remains regardless of sample size.
      Both must be understood to interpret data correctly.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson introduces <strong>missing data</strong>,
      explaining why data are missing, why ignoring missingness is dangerous,
      and why simple fixes often fail.
    </p>

    <a class="btn btn-primary" href="/foundations/missing-data/">
      Next: Missing Data
    </a>
  </div>
</section>

<script>
  try {
    localStorage.setItem("esa:lastLesson", window.location.pathname);
  } catch (e) {}
</script>
