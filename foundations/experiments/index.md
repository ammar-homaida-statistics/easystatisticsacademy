---
layout: default
title: Experiments
description: Understanding experiments, manipulation and control, treatments and outcomes, random assignment, and why experiments provide strong causal evidence.
permalink: /foundations/experiments/
section: foundations
lesson_order: 23
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="Experiments">
<meta name="esa-lesson-url" content="/foundations/experiments/">

<a class="btn btn-primary" href="/foundations/observational-studies/">
  Previous: Observational Studies
</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Experiments</h1>

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — Real-world randomized experiments and A/B testing examples will be added.
    </div>

    <p class="lead">
      Experiments are designed to identify cause-and-effect relationships.
      By actively controlling conditions and using random assignment,
      they provide stronger evidence than observational studies.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 23
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>What defines an experiment in statistics.</li>
      <li>The role of manipulation and control.</li>
      <li>What treatments and outcomes are.</li>
      <li>Why random assignment is essential.</li>
      <li>Why experiments provide strong causal evidence.</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why this topic matters</h2>

    <p>
      Many important questions involve cause and effect:
      Does a treatment work? Does a policy change behavior?
    </p>

    <p>
      Observational data alone cannot answer these questions reliably.
    </p>

    <p>
      Experiments provide a structured way to isolate causes
      and produce more credible conclusions.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What defines an experiment</h2>

    <p>
      An experiment is a study in which researchers actively
      assign conditions to observational units.
    </p>

    <p>
      Unlike observational studies, experiments involve intervention.
    </p>

    <p>
      The goal is to create conditions where differences in outcomes
      can be attributed to the treatment itself.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Manipulation and control</h2>

    <p>
      Experiments involve <strong>manipulation</strong>:
      researchers decide which treatment each unit receives.
    </p>

    <p>
      They also involve <strong>control</strong>:
      keeping other factors as similar as possible across groups.
    </p>

    <p>
      This combination reduces the influence of confounding variables
      that are common in observational studies.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Treatments and outcomes</h2>

    <p>
      A <strong>treatment</strong> is the condition applied
      to an experimental unit.
    </p>

    <p>
      An <strong>outcome</strong> is the response measured
      after the treatment is applied.
    </p>

    <h3>Example</h3>

    <p>
      In a medical experiment:
    </p>

    <ul class="bullets">
      <li>Treatment: receiving a new drug vs a placebo</li>
      <li>Outcome: improvement in health</li>
    </ul>

    <p>
      Experiments compare outcomes across treatment groups
      to assess effects.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Random assignment</h2>

    <p>
      Random assignment means that units are assigned
      to treatments by chance.
    </p>

    <p>
      This ensures that, on average,
      treatment groups are similar before the treatment is applied.
    </p>

    <p>
      Both known and unknown factors
      are balanced across groups.
    </p>

    <p style="font-weight:600;">
      This is the key mechanism that allows causal interpretation.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why experiments support causation</h2>

    <p>
      Because treatments are assigned and conditions are controlled,
      differences in outcomes can be linked to the treatment.
    </p>

    <p>
      Random assignment removes systematic differences
      between groups.
    </p>

    <p>
      This allows experiments to rule out many alternative explanations,
      such as confounding or reverse causation.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Limitations of experiments</h2>

    <ul class="bullets">
      <li>Some experiments are unethical (e.g., harmful exposures).</li>
      <li>Some are impractical or too expensive.</li>
      <li>Results may not generalize beyond the study setting.</li>
    </ul>

    <p>
      Even strong experimental results must be interpreted carefully.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Common misunderstandings</h2>

    <ul class="bullets">
      <li>Confusing random assignment with random sampling.</li>
      <li>Assuming all experiments are perfectly controlled.</li>
      <li>Believing experiments eliminate all uncertainty.</li>
    </ul>

    <p>
      Experiments improve causal inference,
      but they do not produce absolute certainty.
    </p>
  </div>
</section>



<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      Experiments support causal conclusions
      because they combine control with random assignment.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Experiments manipulate conditions, assign treatments,
      and measure outcomes.
      By using random assignment, they provide strong evidence
      about cause-and-effect relationships.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson introduces <strong>ethical considerations</strong>,
      explaining consent, privacy, and why ethical constraints
      shape how data can be collected.
    </p>

    <a class="btn btn-primary" href="/foundations/ethical-considerations-in-data-collection/">
      Next: Ethical Considerations in Data Collection
    </a>
  </div>
</section>

<script>
  try {
    localStorage.setItem("esa:lastLesson", window.location.pathname);
  } catch (e) {}
</script>
