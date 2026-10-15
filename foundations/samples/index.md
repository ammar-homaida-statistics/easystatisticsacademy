---
layout: default
title: Samples
description: Understand what a sample is, why sampling is necessary, and how samples relate to populations in statistical analysis.
permalink: /foundations/samples/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Foundations</span>
      <span class="badge">Core concept</span>
      <span class="badge">Inference base</span>
    </div>

    <h1>Samples</h1>

    <p class="lead">
      Learn what a sample is and why we use samples instead of entire populations —
      the starting point of all statistical analysis.
    </p>

    <div class="hero-actions">
      <a class="btn" href="#content">Start lesson</a>
      <a class="btn btn-outline" href="/foundations/">Back to Foundations</a>
    </div>

  </div>
</section>

<!-- CONTENT -->
<section class="section" id="content">

  <!-- CORE IDEA -->
  <div class="section-block">
    <h2>The Core Idea</h2>

    <p>
      A <strong>sample</strong> is a subset of the population.
    </p>

    <p>
      It answers the question:
    </p>

    <ul class="bullets">
      <li>What part of the population do we actually observe?</li>
    </ul>

    <p>
      In practice, we almost always work with samples — not full populations.
    </p>
  </div>

  <!-- EXAMPLES -->
  <div class="section-block">
    <h2>Examples of Samples</h2>

    <p><strong>Population:</strong> All students in a university</p>

    <p><strong>Sample:</strong> 100 selected students</p>

    <hr style="margin:20px 0;">

    <p><strong>Population:</strong> All voters in a country</p>

    <p><strong>Sample:</strong> 1,000 surveyed voters</p>
  </div>

  <!-- WHY SAMPLES -->
  <div class="section-block">
    <h2>Why Do We Use Samples?</h2>

    <p>
      Because studying the full population is usually:
    </p>

    <ul class="bullets">
      <li>Too expensive</li>
      <li>Too time-consuming</li>
      <li>Sometimes impossible</li>
    </ul>

    <p>
      Sampling allows us to make conclusions efficiently.
    </p>
  </div>

  <!-- GOAL -->
  <div class="section-block">
    <h2>The Goal of Sampling</h2>

    <p>
      First define the <strong>target population</strong>: the group we want
      to describe. The way participants are selected matters because it
      determines which parts of that population can enter the sample.
    </p>

    <p>
      A useful sampling design aims to:
    </p>

    <ul class="bullets">
      <li>Give relevant members of the target population a suitable chance to be included</li>
      <li>Capture important differences among those members</li>
      <li>Support conclusions with clearly stated assumptions and limitations</li>
    </ul>

    <p>
      A poorly matched selection process can produce <strong>selection bias</strong>;
      representativeness is not determined by sample size alone.
    </p>
  </div>

  <!-- NUMERICAL EXAMPLE -->
  <div class="section-block">
    <h2>Example</h2>

    <p>
      Suppose the population average height is unknown.
    </p>

    <p>
      We collect a sample:
    </p>

    <ul class="bullets">
      <li>Heights: 170, 172, 168, 171, 169</li>
    </ul>

    <p>
      Sample mean:
    </p>

    <p>
      (170 + 172 + 168 + 171 + 169) / 5 = 170
    </p>

    <p>
      This is used to estimate the population average.
    </p>
  </div>

  <!-- REPRESENTATIVENESS -->
  <div class="section-block">
    <h2>Representativeness</h2>

    <p>
      Whether a sample is representative depends on the <strong>target population</strong>,
      the characteristic being measured, and the <strong>selection mechanism</strong>.
    </p>

    <p><strong>Example:</strong> Suppose we want to estimate the average height
      of <em>all university students</em> but recruit only athletes.
      If athletes differ systematically in height from other students,
      this selection can bias our estimate of the university-wide mean.
      The direction and size of any bias depend on the population and selection process;
      bias is a risk, not an automatic certainty.
    </p>

    <p>
      If our target population is <em>university athletes</em> instead,
      recruiting athletes may be appropriate, provided the recruitment method
      adequately represents that target group.
    </p>
  </div>

  <!-- SAMPLE SIZE -->
  <div class="section-block">
    <h2>Sample Size</h2>

    <p>
      With a suitable sampling design, larger samples generally reduce
      <strong>random sampling variability</strong> and improve precision.
      This does not guarantee accuracy if the sample is systematically unrepresentative.
    </p>

    <ul class="bullets">
      <li>Sample size mainly affects random sampling error under appropriate assumptions</li>
      <li>Selection bias can remain even in a very large sample</li>
      <li>Address potential bias by improving the selection process, not only by recruiting more people</li>
    </ul>
  </div>

  <!-- KEY INSIGHT -->
  <div class="section-block">
    <h2>Key Insight</h2>

    <p>
      A sample is our window into the population.
    </p>

    <p>
      Everything we conclude depends on how that sample was obtained.
    </p>
  </div>

  <!-- NEXT -->
  <div class="section-block">
    <h2>What Comes Next?</h2>

    <p>
      Even good samples vary.
    </p>

    <p>
      Next, we study:
    </p>

    <ul class="bullets">
      <li>Sampling variability</li>
    </ul>

    <p>
      This explains why different samples give different results.
    </p>
  </div>

</section>

<!-- NAVIGATION -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next steps</h2>

      <div class="hero-actions">

        <a class="btn btn-outline" href="/foundations/populations/">
          ← Previous: Populations
        </a>

        <a class="btn btn-outline" href="/foundations/">
          Foundations Home
        </a>

        <a class="btn" href="/foundations/sampling-variability/">
          Next: Sampling Variability →
        </a>

      </div>

    </div>

  </div>
</section>
