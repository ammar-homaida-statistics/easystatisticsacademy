---
layout: default
title: "3. Law of Total Probability"
description: "Compute probabilities by partitioning the sample space into cases and summing conditional contributions."
permalink: /probability/conditional/law-of-total-probability/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the structure and the correct conceptual flow.
        Numerical examples, diagrams, and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 2 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_conditional_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/conditional/law-of-total-probability/",
      label: "Lesson 3 — Law of Total Probability",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Lesson 3</span>
        <span class="badge">Partition</span>
        <span class="badge">Case analysis</span>
      </div>

      <h1>3. Law of Total Probability</h1>
      <p class="lead">
        Complex probability problems become simple when you break the world into cases.
        The law of total probability formalizes this idea using partitions of the sample space.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/conditional/">Back to Block 2</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Think in cases. Sum their contributions.
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
    <li>Define a partition of the sample space</li>
    <li>Use the law of total probability to compute P(A)</li>
    <li>Recognize when case-by-case decomposition simplifies a problem</li>
    <li>Prepare for Bayes’ theorem in the next lesson</li>
  </ul>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>If you can divide the sample space into mutually exclusive and exhaustive cases,
        you can compute probabilities by summing conditional contributions across those cases.</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What is a partition?</h2>
    <p>
      A collection of events <strong>B₁, B₂, ..., Bₙ</strong> forms a partition of the sample space S if:
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>They are mutually exclusive (no overlap): Bᵢ ∩ Bⱼ = ∅ for i ≠ j</li>
      <li>They cover the whole space: B₁ ∪ B₂ ∪ ... ∪ Bₙ = S</li>
      <li>Each has positive probability: P(Bᵢ) &gt; 0</li>
    </ul>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    In plain language: a partition is a complete and non-overlapping list of cases.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) The law of total probability (formula)</h2>
    <p>
      If B₁, ..., Bₙ form a partition of S, then for any event A:
    </p>
  </div>

  <div class="card">
    <p style="font-size:1.1rem; margin:0;">
      <strong>P(A) = Σ P(A | Bᵢ) · P(Bᵢ)</strong>
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Read it carefully</h3>
    <ul class="bullets">
      <li>Inside each case Bᵢ, compute the conditional probability P(A | Bᵢ)</li>
      <li>Weight it by how likely that case is: P(Bᵢ)</li>
      <li>Sum over all cases</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Why this works (conceptual reasoning)</h2>
    <p>
      The event A can happen through different scenarios (cases). Each case contributes some probability mass.
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>A = (A ∩ B₁) ∪ (A ∩ B₂) ∪ ... ∪ (A ∩ Bₙ)</li>
      <li>These intersections are disjoint because the Bᵢ are disjoint</li>
      <li>So we can add their probabilities</li>
    </ul>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Connection to multiplication rule</h2>
      <p style="margin:0;">
        Each term P(A ∩ Bᵢ) can be written as P(A | Bᵢ) P(Bᵢ).
        The law of total probability is simply the multiplication rule applied across cases.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) When should you use it?</h2>
    <p>
      Use the law of total probability when:
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Different subpopulations</h3>
      <ul class="bullets">
        <li>Different groups (e.g., factories, hospitals, regions)</li>
        <li>Different prior conditions</li>
        <li>Mixture models</li>
      </ul>
    </div>

    <div class="card">
      <h3>Hidden causes</h3>
      <ul class="bullets">
        <li>An event depends on an unobserved factor</li>
        <li>First condition on the factor, then average</li>
      </ul>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    In statistics and machine learning, this often appears as “marginalizing over a latent variable.”
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Strategic thinking pattern</h2>
    <p>
      When facing a complicated probability:
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Can I split the world into clean, disjoint cases?</li>
      <li>Can I compute P(A | case)?</li>
      <li>Do I know the probability of each case?</li>
      <li>Then sum weighted contributions.</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Using overlapping events as a partition</li>
        <li>Forgetting that the cases must cover the entire sample space</li>
        <li>Confusing P(A|Bᵢ) with P(Bᵢ|A)</li>
        <li>Leaving out one case (incomplete partition)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define a valid partition of the sample space</li>
        <li>Apply the formula P(A)=ΣP(A|Bᵢ)P(Bᵢ)</li>
        <li>Recognize total probability as weighted averaging</li>
        <li>Be ready for Bayes’ theorem (reversing conditioning)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we reverse conditional probability using Bayes’ theorem
        and formally update beliefs with evidence.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/conditional/bayes-theorem/">
          Next lesson: 4. Bayes’ Theorem →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/conditional/multiplication-rule/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: The Multiplication Rule
          </a>
        </div>
      </div>
    </div>
  </div>
</section>