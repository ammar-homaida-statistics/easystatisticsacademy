---
layout: default
title: "5. Tree Diagrams & Structured Reasoning"
description: "Use tree diagrams to visualize conditional probability, sequential events, and Bayesian updating clearly and correctly."
permalink: /probability/conditional/tree-diagrams/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 establishes the structural reasoning method. Full diagrams,
        numerical examples, and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 2 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_conditional_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/conditional/tree-diagrams/",
      label: "Lesson 5 — Tree Diagrams & Structured Reasoning",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Lesson 5</span>
        <span class="badge">Visualization</span>
        <span class="badge">Structure</span>
      </div>

      <h1>5. Tree Diagrams & Structured Reasoning</h1>
      <p class="lead">
        Tree diagrams translate conditional probability into a visual structure.
        They make sequential reasoning transparent and reduce algebraic mistakes.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/conditional/">Back to Block 2</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Trees are not decoration — they enforce correct multiplication and summation.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to:
    </p>
  </div>

  <ul class="bullets">
    <li>Construct a probability tree for sequential events</li>
    <li>Multiply probabilities along branches</li>
    <li>Sum probabilities across terminal nodes</li>
    <li>Use trees to simplify Bayes and total probability problems</li>
  </ul>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Multiply along branches. Sum across paths.</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What is a tree diagram?</h2>
    <p>
      A tree diagram represents a multi-step experiment as branching paths.
      Each branch corresponds to a conditional probability.
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Start with the first event</li>
      <li>From each branch, extend to the next conditional event</li>
      <li>Continue until all outcomes are represented</li>
    </ul>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Each complete path from root to leaf represents a joint event.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Multiplication along branches</h2>
    <p>
      Each branch carries a conditional probability.
      The probability of a complete path is the product of its branches.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      <strong>P(A ∩ B) = P(A) · P(B | A)</strong>
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This is exactly the multiplication rule in visual form.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Summation across terminal nodes</h2>
    <p>
      If an event can happen through multiple paths,
      add the probabilities of those paths.
    </p>
  </div>

  <div class="card">
    <p>
      Example structure:
    </p>
    <ul class="bullets">
      <li>Path 1 leads to A</li>
      <li>Path 2 also leads to A</li>
      <li>Total P(A) = P(path 1) + P(path 2)</li>
    </ul>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Connection</h2>
      <p style="margin:0;">
        Summing across branches implements the law of total probability.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Why tree diagrams prevent mistakes</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Forces correct conditioning</h3>
      <p>
        Every branch explicitly states the condition.
        You cannot silently assume independence.
      </p>
    </div>

    <div class="card">
      <h3>Prevents double counting</h3>
      <p>
        Each path represents a distinct joint event.
        Overlaps are visually separated.
      </p>
    </div>

    <div class="card">
      <h3>Clarifies partitions</h3>
      <p>
        Trees make partitions explicit.
        Each first-level branch represents a case.
      </p>
    </div>

    <div class="card">
      <h3>Supports Bayes’ reasoning</h3>
      <p>
        Posterior probabilities can be read directly from branch ratios.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) When should you use a tree?</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Sequential experiments (step 1 → step 2)</li>
      <li>Conditional structures (test → disease status)</li>
      <li>Multi-stage decisions</li>
      <li>Bayes problems</li>
      <li>Sampling without replacement</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Writing unconditional probabilities on conditional branches</li>
        <li>Forgetting to multiply along a path</li>
        <li>Adding probabilities without checking disjointness</li>
        <li>Leaving out one branch (incomplete tree)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Construct a correct probability tree</li>
        <li>Apply multiplication rule visually</li>
        <li>Apply total probability visually</li>
        <li>Prepare for real-world Bayesian reasoning</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Finally, we examine common reasoning errors such as base-rate neglect.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/conditional/base-rate-neglect-and-fallacies/">
          Next lesson: 6. Base-Rate Neglect & Common Fallacies →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/conditional/bayes-theorem/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Bayes’ Theorem
          </a>
        </div>
      </div>
    </div>
  </div>
</section>