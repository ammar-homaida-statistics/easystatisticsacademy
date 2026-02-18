---
layout: default
title: "4. Bayes’ Theorem"
description: "Reverse conditional probability and update beliefs using prior information and new evidence."
permalink: /probability/conditional/bayes-theorem/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 establishes the correct conceptual and mathematical structure.
        Numerical examples, case studies, and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 2 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_conditional_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/conditional/bayes-theorem/",
      label: "Lesson 4 — Bayes’ Theorem",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">Updating</span>
        <span class="badge">Posterior reasoning</span>
      </div>

      <h1>4. Bayes’ Theorem</h1>
      <p class="lead">
        Bayes’ theorem allows us to reverse conditional probability.
        It provides a formal rule for updating uncertainty when new evidence arrives.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/conditional/">Back to Block 2</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Bayes’ theorem is not new mathematics—it is the multiplication rule plus total probability.
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
    <li>Derive Bayes’ theorem from earlier rules</li>
    <li>Interpret prior, likelihood, and posterior correctly</li>
    <li>Recognize why P(A|B) and P(B|A) are not the same</li>
    <li>Understand how base-rate neglect occurs</li>
  </ul>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Posterior = (Likelihood × Prior) / Evidence</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) The formula</h2>
    <p>
      Starting from the multiplication rule:
    </p>
  </div>

  <div class="card">
    <p><strong>P(A ∩ B) = P(A|B)P(B) = P(B|A)P(A)</strong></p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p>
      Rearranging gives:
    </p>
    <p style="font-size:1.1rem; margin:0;">
      <strong>P(A | B) = [P(B | A) · P(A)] / P(B)</strong>
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This is Bayes’ theorem.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) The components explained</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Prior: P(A)</h3>
      <p>
        The probability of A before observing evidence B.
        Represents baseline knowledge.
      </p>
    </div>

    <div class="card">
      <h3>Likelihood: P(B | A)</h3>
      <p>
        Probability of observing evidence B if A is true.
        Measures how compatible the evidence is with A.
      </p>
    </div>

    <div class="card">
      <h3>Evidence: P(B)</h3>
      <p>
        Overall probability of observing B across all possibilities.
        Acts as a normalization factor.
      </p>
    </div>

    <div class="card">
      <h3>Posterior: P(A | B)</h3>
      <p>
        Updated probability of A after observing B.
        This is the result of Bayesian updating.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Using the law of total probability in Bayes</h2>
    <p>
      The denominator P(B) is usually computed using the law of total probability.
    </p>
  </div>

  <div class="card">
    <p>
      If {A, Aᶜ} partitions the sample space:
    </p>
    <p>
      <strong>P(B) = P(B|A)P(A) + P(B|Aᶜ)P(Aᶜ)</strong>
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Bayes’ theorem always depends on partitioning the world into alternative explanations.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Why Bayes’ theorem matters</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Medical testing</h3>
      <p>
        A positive test does not automatically mean high disease probability.
        The prior prevalence matters.
      </p>
    </div>

    <div class="card">
      <h3>Machine learning</h3>
      <p>
        Many classifiers estimate posterior probabilities:
        P(Class | Features).
      </p>
    </div>

    <div class="card">
      <h3>Decision-making</h3>
      <p>
        Rational decisions require updating beliefs with new evidence.
      </p>
    </div>

    <div class="card">
      <h3>Statistical inference</h3>
      <p>
        Bayesian statistics formalizes inference using repeated application of Bayes’ rule.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Base-rate neglect (preview)</h2>
    <p>
      People often ignore P(A) (the prior) and focus only on P(B|A).
      This leads to severe misinterpretations.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core warning</h2>
      <p style="margin:0;">
        A rare event can still produce common evidence.
        Always include the prior probability.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Confusing P(A|B) with P(B|A)</li>
        <li>Ignoring the prior probability</li>
        <li>Forgetting to compute P(B) using total probability</li>
        <li>Assuming high likelihood implies high posterior</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Derive Bayes’ theorem from earlier rules</li>
        <li>Interpret prior, likelihood, evidence, posterior</li>
        <li>Recognize the role of base rates</li>
        <li>Be ready for visual reasoning using tree diagrams</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we represent conditional structures visually using tree diagrams.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/conditional/tree-diagrams/">
          Next lesson: 5. Tree Diagrams →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/conditional/law-of-total-probability/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Law of Total Probability
          </a>
        </div>
      </div>
    </div>
  </div>
</section>