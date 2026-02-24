---
layout: default
title: "1. What Is a Hypothesis Test?"
description: "Understand hypothesis testing as a structured decision rule under uncertainty: null model, evidence, test statistic, and p-value logic."
permalink: /inference/hypothesis-testing/what-is-a-hypothesis-test/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 locks the conceptual structure of hypothesis testing.
        Worked examples, visuals, and software demonstrations will be added later without changing the lesson order.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Inference Block 3 -->
<script>
  (function () {
    var KEY = "esa_continue_inference_hypothesis_testing_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/hypothesis-testing/what-is-a-hypothesis-test/",
      label: "Lesson 1 — What Is a Hypothesis Test?",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/hypothesis-testing/",
      label: "Block 3 — Hypothesis Testing",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Lesson 1</span>
        <span class="badge">Testing</span>
        <span class="badge">Decision</span>
      </div>

      <h1>1. What Is a Hypothesis Test?</h1>

      <p class="lead">
        A hypothesis test is a formal method to make a decision under uncertainty.
        We compare observed data to a <strong>null model</strong> and measure how surprising the data would be
        if that model were true.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/">Back to Block 3</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: structure first. Examples and software come after the logic is stable.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to describe a hypothesis test as a decision procedure,
      identify the roles of the null and alternative, and explain what “evidence against the null” means.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Testing is not “proving”.</strong> A hypothesis test quantifies how compatible the observed data
        are with a specific reference model (the null). It provides a rule for action, not a proof of truth.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) The problem: decisions with uncertainty</h2>
    <p>
      In real problems, data vary because of random sampling, measurement noise, and natural variability.
      Hypothesis testing gives a disciplined way to decide whether an observed pattern is plausibly due to chance
      (under a reference model) or is too extreme to ignore.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Typical decision questions</h3>
      <ul class="bullets">
        <li>Is a new treatment better than the standard?</li>
        <li>Is the mean different from a target value?</li>
        <li>Are two groups different?</li>
        <li>Is there an association between two variables?</li>
      </ul>
      <p class="muted-mini">
        A test is used when you need a <strong>decision rule</strong>, not just an estimate.
      </p>
    </div>

    <div class="card">
      <h3>What testing does (and does not) do</h3>
      <ul class="bullets">
        <li><strong>Does:</strong> quantify evidence vs a null model</li>
        <li><strong>Does:</strong> control false-positive risk via \(\alpha\)</li>
        <li><strong>Does not:</strong> prove a hypothesis is true</li>
        <li><strong>Does not:</strong> measure practical importance by itself</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) The null model (the reference world)</h2>
    <p>
      A hypothesis test starts by specifying a <strong>null hypothesis</strong> \(H_0\):
      a reference statement that represents “no effect”, “no difference”, or “nothing interesting”.
      Under \(H_0\), we can describe how the data (or a test statistic) should behave.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      <strong>Null hypothesis \(H_0\):</strong> a specific reference claim used to generate a probability model
      for what we would expect to see if “nothing new” is happening.
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    The null is not “what you believe”. It is the baseline model you challenge.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) The alternative hypothesis (the direction of challenge)</h2>
    <p>
      The <strong>alternative hypothesis</strong> \(H_1\) (or \(H_a\)) describes what kind of departure from \(H_0\)
      you are prepared to detect: a difference, a positive effect, a negative effect, or any non-zero effect.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Two-sided alternative</h3>
      <p style="margin:0;">
        Detects departures in both directions (difference without specifying sign).
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Example form: \(H_1:\ \mu \neq \mu_0\)
      </p>
    </div>

    <div class="card">
      <h3>One-sided alternative</h3>
      <p style="margin:0;">
        Detects departures in one direction only (increase or decrease).
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Example form: \(H_1:\ \mu &gt; \mu_0\) or \(H_1:\ \mu &lt; \mu_0\)
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Choosing one-sided vs two-sided is a design decision and should be made <strong>before</strong> seeing data.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) The test statistic (evidence in standard error units)</h2>
    <p>
      We compress the data into a single number called a <strong>test statistic</strong>.
      It is designed to be large (in magnitude) when the data are inconsistent with \(H_0\).
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      <strong>General idea:</strong>
      \[
      \text{test statistic} \;=\; \frac{\text{estimate} - \text{null value}}{\text{standard error}}
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This is the same “signal measured in uncertainty units” logic you saw in confidence intervals.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) The p-value (surprise under \(H_0\))</h2>
    <p>
      Once we compute the test statistic from the observed sample, we ask:
      <strong>how likely is it to see a result at least this extreme if \(H_0\) were true?</strong>
      That probability is the p-value.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      <strong>p-value:</strong> probability (under \(H_0\)) of getting a test statistic as extreme or more extreme
      than what we observed (in the direction(s) specified by \(H_1\)).
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Important interpretation</h2>
      <p style="margin:0;">
        The p-value is <strong>not</strong> \(P(H_0 \text{ is true})\).
        It is computed assuming \(H_0\) is true, and it measures how surprising the data would be in that world.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Decision rule (preview)</h2>
    <p>
      To convert evidence into a decision, we choose a <strong>significance level</strong> \(\alpha\)
      (like 0.05). Then we compare the p-value to \(\alpha\).
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>If p-value ≤ \(\alpha\)</h3>
      <p style="margin:0;">
        Reject \(H_0\) (data are sufficiently inconsistent with the null model).
      </p>
    </div>

    <div class="card">
      <h3>If p-value &gt; \(\alpha\)</h3>
      <p style="margin:0;">
        Fail to reject \(H_0\) (data are not extreme enough to rule out the null model).
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    “Fail to reject” does not mean “accept” — it means the data do not provide strong enough evidence against \(H_0\)
    at the chosen \(\alpha\).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>7) Common traps (and how to avoid them)</h2>
    <p>
      Hypothesis testing has a few classic interpretation errors that appear everywhere in real reporting.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Trap A: “p is the probability the null is true”</h3>
      <p>
        Wrong. p is computed under the assumption \(H_0\) is true; it measures surprise, not truth probability.
      </p>
    </div>

    <div class="card">
      <h3>Trap B: “Non-significant means no effect”</h3>
      <p>
        Wrong. It can mean low power, high noise, or small sample size.
      </p>
    </div>

    <div class="card">
      <h3>Trap C: Changing the hypothesis after seeing data</h3>
      <p>
        Decide \(H_0\), \(H_1\), and \(\alpha\) before analysis. Post-hoc choices inflate false positives.
      </p>
    </div>

    <div class="card">
      <h3>Trap D: Confusing statistical and practical importance</h3>
      <p>
        A tiny effect can be statistically significant with large n. Practical meaning requires effect size and context.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Explain hypothesis testing as a decision procedure</li>
        <li>Define \(H_0\) as a reference model and \(H_1\) as a structured challenge</li>
        <li>Describe test statistics as “evidence in SE units”</li>
        <li>Interpret the p-value correctly as surprise under \(H_0\)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we define the null and alternative hypotheses more precisely,
        including equality in \(H_0\) and directional vs non-directional alternatives.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/hypothesis-testing/null-and-alternative/">
          Next lesson: 2. Null and Alternative Hypotheses →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Back to block</div>
        <div class="mini-body">
          <a href="/inference/hypothesis-testing/" style="color:#1a73e8; text-decoration:underline;">
            Block 3: Hypothesis Testing
          </a>
        </div>
      </div>
    </div>

  </div>
</section>