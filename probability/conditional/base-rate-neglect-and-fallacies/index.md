---
layout: default
title: "6. Base-Rate Neglect & Common Fallacies"
description: "Understand why intuition fails in conditional probability and how ignoring base rates leads to serious reasoning errors."
permalink: /probability/conditional/base-rate-neglect-and-fallacies/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 establishes the conceptual reasoning structure. Numerical case studies,
        visuals, and simulations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 2 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_conditional_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/conditional/base-rate-neglect-and-fallacies/",
      label: "Lesson 6 — Base-Rate Neglect & Common Fallacies",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Lesson 6</span>
        <span class="badge">Reasoning errors</span>
        <span class="badge">Bayesian logic</span>
      </div>

      <h1>6. Base-Rate Neglect & Common Fallacies</h1>
      <p class="lead">
        Many probability errors are not mathematical — they are cognitive.
        This lesson explains why conditional reasoning fails intuitively
        and how to correct it using structured probability rules.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/conditional/">Back to Block 2</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Most mistakes come from ignoring prior probabilities.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should:
    </p>
  </div>

  <ul class="bullets">
    <li>Understand what base-rate neglect is</li>
    <li>Recognize common conditional probability fallacies</li>
    <li>Use Bayes’ theorem to correct intuitive errors</li>
    <li>Develop a structured debugging mindset</li>
  </ul>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Evidence is not enough — prior probability matters.</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What is base-rate neglect?</h2>
    <p>
      Base-rate neglect occurs when people ignore the prior probability of an event
      and focus only on new evidence.
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Prior probability = baseline prevalence</li>
      <li>Likelihood = strength of evidence</li>
      <li>Posterior = updated probability</li>
    </ul>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Ignoring the base rate means ignoring P(A) in Bayes’ formula.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Classic confusion: P(A|B) vs P(B|A)</h2>
    <p>
      One of the most common reasoning errors is confusing:
    </p>
  </div>

  <div class="card">
    <p><strong>P(Disease | Positive test)</strong></p>
    <p>with</p>
    <p><strong>P(Positive test | Disease)</strong></p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Important</h2>
      <p style="margin:0;">
        A highly accurate test (high likelihood) does not imply
        a high probability of disease if the disease is rare.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Why intuition fails</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Human reasoning is causal</h3>
      <p>
        We think: “If disease causes positive test, then positive test implies disease.”
        But probabilistically, the reverse direction is different.
      </p>
    </div>

    <div class="card">
      <h3>Small probabilities are hard to reason about</h3>
      <p>
        Rare events distort intuition.
        Even strong evidence may not overcome a very low prior.
      </p>
    </div>

    <div class="card">
      <h3>Ignoring denominator P(B)</h3>
      <p>
        People rarely compute the full denominator using total probability.
        They stop at the likelihood.
      </p>
    </div>

    <div class="card">
      <h3>Overconfidence bias</h3>
      <p>
        High-sounding percentages lead to deterministic thinking.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) How to correct the error</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Always write Bayes’ formula explicitly</li>
      <li>Compute the denominator using total probability</li>
      <li>Interpret posterior as weighted evidence</li>
      <li>Check whether the prior is small</li>
    </ul>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Debugging strategy</h2>
      <p style="margin:0;">
        When a probability feels surprisingly high,
        check whether you forgot to include the base rate.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Other common fallacies</h2>
  </div>

  <div class="card">
    <h3>The prosecutor’s fallacy</h3>
    <p>
      Confusing P(Evidence | Innocent) with P(Innocent | Evidence).
    </p>
  </div>

  <div class="card">
    <h3>Ignoring conditional structure</h3>
    <p>
      Treating dependent events as independent.
    </p>
  </div>

  <div class="card">
    <h3>Selection bias</h3>
    <p>
      Conditioning on an event without recognizing that conditioning occurred.
    </p>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 2</h2>
      <ul class="bullets">
        <li>Compute conditional probabilities correctly</li>
        <li>Apply multiplication and total probability rules</li>
        <li>Use Bayes’ theorem properly</li>
        <li>Avoid base-rate neglect and reasoning fallacies</li>
        <li>Be ready for Block 3 — Random Variables</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        We now move from events to numerical quantities defined on events:
        random variables.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/random-variables/">
          Continue to Block 3 — Random Variables →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/conditional/tree-diagrams/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 5: Tree Diagrams
          </a>
        </div>
      </div>
    </div>
  </div>
</section>