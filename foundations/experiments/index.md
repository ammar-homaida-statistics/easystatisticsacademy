---
layout: default
title: Experiments
description: Learn how experiments establish causation using control, treatments, and random assignment.
permalink: /foundations/experiments/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Causation</span>
      <span class="badge">Control</span>
      <span class="badge">Randomization</span>
    </div>

    <h1>Experiments</h1>

    <p class="lead">
      Experiments allow us to establish causation by controlling conditions and using random assignment.
    </p>

    <div class="hero-actions">
      <a class="btn" href="#content">Start lesson</a>
      <a class="btn btn-outline" href="/foundations/">Back to Foundations</a>
    </div>

  </div>
</section>

<!-- CONTENT -->
<section class="section" id="content">

  <!-- WHAT IS -->
  <div class="section-block">
    <h2>What Is an Experiment?</h2>

    <p>
      An experiment is a study where researchers actively control and manipulate variables.
    </p>

    <ul class="bullets">
      <li>Introduce a treatment</li>
      <li>Control conditions</li>
      <li>Observe outcomes</li>
    </ul>

    <p>
      Unlike observational studies, experiments involve intervention.
    </p>
  </div>

  <!-- KEY COMPONENTS -->
  <div class="section-block">
    <h2>Key Components</h2>

    <p><strong>1. Treatment</strong></p>
    <ul class="bullets">
      <li>The condition applied (e.g., drug, method, intervention)</li>
    </ul>

    <p><strong>2. Control Group</strong></p>
    <ul class="bullets">
      <li>Group that does not receive the treatment</li>
    </ul>

    <p><strong>3. Experimental Group</strong></p>
    <ul class="bullets">
      <li>Group that receives the treatment</li>
    </ul>

    <p><strong>4. Outcome Variable</strong></p>
    <ul class="bullets">
      <li>The result being measured</li>
    </ul>
  </div>

  <!-- RANDOM ASSIGNMENT -->
  <div class="section-block">
    <h2>Random Assignment (Critical)</h2>

    <p>
      Participants are randomly assigned to groups.
    </p>

    <ul class="bullets">
      <li>Reduces bias</li>
      <li>Balances hidden variables</li>
      <li>Creates comparable groups</li>
    </ul>

    <p>
  This is what allows causal conclusions under proper experimental design.
</p>
  </div>

  <div class="section-block">
  <h2>Random Assignment vs Random Sampling</h2>

  <p>
    These are two different ideas:
  </p>

  <ul class="bullets">
    <li><strong>Random sampling:</strong> how participants are selected</li>
    <li><strong>Random assignment:</strong> how participants are placed into groups</li>
  </ul>

  <p>
    Random assignment enables causal conclusions.
    Random sampling enables generalization to a population.
  </p>
</div>

  <div class="section-block">
  <h2>Example</h2>

  <p>
    A new drug is tested using an experiment:
  </p>

  <ul class="bullets">
    <li>Participants are randomly assigned to two groups</li>
    <li>Group A → receives the drug</li>
    <li>Group B → receives a placebo</li>
  </ul>

  <p>
    Because assignment is random, the groups are comparable.
  </p>

  <p>
    If outcomes differ, we can attribute the difference
    to the treatment rather than other factors.
  </p>
</div>

<div class="section-block">
  <h2>Example: A/B Test</h2>

  <p>
    A company wants to test two versions of a website:
  </p>

  <ul class="bullets">
    <li>Group A → sees the original version</li>
    <li>Group B → sees a new design</li>
  </ul>

  <p>
    Users are randomly assigned to each version.
  </p>

  <p>
    The company compares outcomes such as:
  </p>

  <ul class="bullets">
    <li>Click rate</li>
    <li>Purchase rate</li>
  </ul>

  <p>
    Because assignment is random, differences in outcomes
    can be attributed to the design change.
  </p>
</div>

<img src="{{ '/foundations/images/experiment-random-assignment.png' | relative_url }}" 
     alt="Random assignment diagram" 
     style="margin-top:15px; max-width:100%; height:auto;">

     <p>
Participants are randomly assigned to groups, ensuring comparability.
</p>

  <!-- WHY CAUSATION -->
  <div class="section-block">
    <h2>Why Experiments Show Causation</h2>

    <ul class="bullets">
      <li>Control removes external influences</li>
      <li>Randomization removes confounding</li>
      <li>Comparison isolates the effect</li>
    </ul>

    <p>
  This is why well-designed experiments are considered the gold standard for causal inference.
</p>
  </div>

  <!-- LIMITATIONS -->
  <div class="section-block">
    <h2>Limitations</h2>

    <ul class="bullets">
      <li>May be expensive</li>
      <li>May be unethical (e.g., harmful exposure)</li>
      <li>Sometimes not feasible</li>
      <li>Results may not generalize beyond the study setting</li>
    </ul>
  </div>

  <div class="section-block">
  <h2>Internal vs External Validity</h2>

  <p>
    Experiments are strong in <strong>internal validity</strong>
    (causal conclusions within the study).
  </p>

  <p>
    But they may be weaker in <strong>external validity</strong>
    (generalizing results to other populations or settings).
  </p>
</div>

  <!-- OBSERVATIONAL VS EXPERIMENT -->
  <div class="section-block">
  <h2>Observational vs Experimental</h2>

  <ul class="bullets">
    <li>Observational → identifies associations</li>
    <li>Experimental → allows causal inference under proper design</li>
  </ul>

  <p>
    The choice depends on feasibility, ethics, and research goals.
  </p>
</div>

  <!-- COMMON MISTAKE -->
  <div class="section-block">
    <h2>Common Mistake</h2>

    <p>
      Assuming causation without an experiment.
    </p>

    <p>
      Many real-world claims are based only on observational data.
    </p>
  </div>

  <!-- BIG IDEA -->
  <div class="section-block">
    <h2>The Big Idea</h2>

    <p>
      To claim causation, you must control the system.
    </p>

    <p>
      Without control, you only observe patterns.
    </p>
  </div>

  <div class="section-block">
  <h2>Key Insight</h2>

  <p>
    Causation requires careful design, not just data.
  </p>

  <p>
    Without randomization, conclusions about cause and effect are uncertain.
  </p>
</div>

  <!-- NEXT -->
  <div class="section-block">
    <h2>What Comes Next?</h2>

    <p>
      Even experiments are not perfect.
    </p>

    <p>
      Next, we study:
    </p>

    <ul class="bullets">
      <li>Bias</li>
      <li>Systematic errors</li>
      <li>Why results can still be wrong</li>
    </ul>
  </div>

</section>

<!-- NAVIGATION -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next steps</h2>

      <div class="hero-actions">

        <a class="btn btn-outline" href="/foundations/observational-studies/">
          ← Previous: Observational Studies
        </a>

        <a class="btn btn-outline" href="/foundations/">
          Foundations Home
        </a>

        <a class="btn" href="/foundations/bias/">
          Next: Bias →
        </a>

      </div>

    </div>

  </div>
</section>
