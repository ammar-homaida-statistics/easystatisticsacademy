---
layout: default
title: Observational Studies
description: Understanding observational studies, passive data collection, lack of control, and the difference between association and causation.
permalink: /foundations/observational-studies/
section: foundations
lesson_order: 22
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="Observational Studies">
<meta name="esa-lesson-url" content="/foundations/observational-studies/">

<a class="btn btn-primary" href="/foundations/surveys/">
  Previous: Surveys
</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Observational Studies</h1>

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — Real-world causal vs non-causal examples will be added.
    </div>

    <p class="lead">
      Observational studies collect data without intervention.
      They are powerful for discovering patterns,
      but they cannot by themselves establish causation.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 22
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>What observational studies are.</li>
      <li>What passive data collection means.</li>
      <li>Why lack of control limits conclusions.</li>
      <li>The critical difference between association and causation.</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why this topic matters</h2>

    <p>
      Many real-world datasets come from observational studies,
      not controlled experiments.
    </p>

    <p>
      These data are often used to make claims about causes,
      even when the study design does not support such conclusions.
    </p>

    <p>
      Misinterpreting observational results is one of the most common
      and serious errors in statistics.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What observational studies are</h2>

    <p>
      An observational study collects data
      without actively controlling or assigning conditions.
    </p>

    <p>
      Researchers observe what naturally occurs,
      rather than manipulating variables.
    </p>

    <p>
      The goal is to identify patterns,
      relationships, and differences in real-world data.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Passive data collection</h2>

    <p>
      Observational studies rely on <strong>passive data collection</strong>.
    </p>

    <p>
      This means the researcher does not control:
    </p>

    <ul class="bullets">
      <li>Who receives which condition</li>
      <li>Which factors influence outcomes</li>
      <li>How variables interact in the real world</li>
    </ul>

    <p>
      Data may come from surveys, records, logs,
      or naturally occurring processes.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Lack of control and confounding</h2>

    <p>
      Because conditions are not controlled,
      many factors may influence the observed relationship.
    </p>

    <p>
      These are called <strong>confounding variables</strong>—
      variables that affect both the predictor and the outcome.
    </p>

    <h3>Example</h3>

    <p>
      Ice cream sales and drowning incidents
      may increase at the same time.
    </p>

    <p>
      The confounding variable is temperature,
      not a causal link between the two.
    </p>

    <p>
      Without control, these effects cannot be separated clearly.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Association vs causation</h2>

    <p>
      Observational studies can identify <strong>associations</strong>—
      patterns or relationships between variables.
    </p>

    <p>
      However, association does not imply causation.
    </p>

    <h3>Key distinction</h3>

    <ul class="bullets">
      <li><strong>Association:</strong> variables move together.</li>
      <li><strong>Causation:</strong> one variable directly affects another.</li>
    </ul>

    <p>
      Observational data alone cannot rule out:
    </p>

    <ul class="bullets">
      <li>Confounding variables</li>
      <li>Reverse causation</li>
      <li>Coincidental relationships</li>
    </ul>

    <p style="font-weight:600;">
      Observational studies suggest relationships.  
      They do not prove causes.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>When observational studies are useful</h2>

    <p>
      Observational studies are essential when experiments
      are not possible.
    </p>

    <p>
      This includes situations where experiments would be:
    </p>

    <ul class="bullets">
      <li>Unethical (e.g., harmful exposures)</li>
      <li>Impractical (e.g., large populations)</li>
      <li>Too expensive or time-consuming</li>
    </ul>

    <p>
      They are valuable for:
    </p>

    <ul class="bullets">
      <li>Describing patterns</li>
      <li>Identifying associations</li>
      <li>Generating hypotheses</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Common misuse</h2>

    <ul class="bullets">
      <li>Claiming causation from correlation.</li>
      <li>Ignoring confounding variables.</li>
      <li>Overgeneralizing results.</li>
      <li>Treating observational results as experimental evidence.</li>
    </ul>

    <p>
      These mistakes are common in media, reports,
      and automated analyses.
    </p>
  </div>
</section>



<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      Observational studies reveal patterns,
      but they do not establish causation.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Observational studies collect data without intervention.
      They are useful for identifying relationships,
      but they cannot determine cause-and-effect on their own.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson introduces <strong>experiments</strong>,
      explaining manipulation, control, random assignment,
      and why experiments provide stronger causal evidence.
    </p>

    <a class="btn btn-primary" href="/foundations/experiments/">
      Next: Experiments
    </a>
  </div>
</section>

<script>
  try {
    localStorage.setItem("esa:lastLesson", window.location.pathname);
  } catch (e) {}
</script>
