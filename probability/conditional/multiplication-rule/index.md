---
layout: default
title: "2. The Multiplication Rule"
description: "Compute joint probabilities using conditional probability: P(A ∩ B)=P(A|B)P(B), chain rule for multiple events, and the correct meaning of independence."
permalink: /probability/conditional/multiplication-rule/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the structure and the correct conceptual flow. Examples, graphs,
        and software demonstrations will be added later without changing the lesson order.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 2 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_conditional_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/conditional/multiplication-rule/",
      label: "Lesson 2 — The Multiplication Rule",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">Joint probability</span>
        <span class="badge">Chain rule</span>
      </div>

      <h1>2. The Multiplication Rule</h1>
      <p class="lead">
        Conditional probability is not only a definition—it is a tool. This lesson shows how to compute
        <strong>joint probabilities</strong> by multiplying conditional pieces in the correct order.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/conditional/">Back to Block 2</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Version 0: core structure first. Worked examples and software demos will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to compute joint probabilities using conditional probability,
      apply the chain rule for multiple events, and understand how independence simplifies the multiplication rule.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Joint probability factors into a conditional probability times a marginal probability.</strong>
        This is the mathematical form of “do it step-by-step.”
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) The multiplication rule (two events)</h2>
    <p>
      Starting from the definition of conditional probability:
      <strong>P(A | B) = P(A ∩ B) / P(B)</strong> (when P(B)&gt;0),
      rearrange to get the multiplication rule:
    </p>
  </div>

  <div class="card">
    <p style="font-size:1.1rem; margin:0;">
      <strong>P(A ∩ B) = P(A | B) · P(B)</strong>
    </p>
  </div>

  <div class="grid grid-2" style="margin-top:1rem;">
    <div class="card">
      <h3>Interpretation</h3>
      <p>
        “Probability that both A and B happen” equals:
      </p>
      <ul class="bullets">
        <li>Probability that B happens, and then</li>
        <li>Within B, probability that A also happens</li>
      </ul>
      <p class="muted-mini">
        The order shown here is: B first, then A within B.
      </p>
    </div>

    <div class="card">
      <h3>Equivalent form</h3>
      <p>
        You can also write:
      </p>
      <p style="margin:0;">
        <strong>P(A ∩ B) = P(B | A) · P(A)</strong>
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Same joint event, but a different “first condition.”
      </p>
    </div>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Practical tip</h2>
      <p style="margin:0;">
        Choose the direction that makes probabilities easiest to compute:
        start with the event you can evaluate directly, then condition on it.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Sequential thinking: “first… then…”</h2>
    <p>
      Many real problems are naturally sequential: test results, sampling without replacement, multi-step decisions.
      The multiplication rule is exactly the probability version of “compute step-by-step.”
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Example template (no numbers yet)</h3>
      <ul class="bullets">
        <li><strong>B:</strong> “First step outcome”</li>
        <li><strong>A:</strong> “Second step outcome”</li>
      </ul>
      <p>
        Then:
        <strong>P(A ∩ B) = P(B) · P(A|B)</strong>
      </p>
    </div>

    <div class="card">
      <h3>Why the order matters</h3>
      <p>
        The conditional term depends on what you already know.
        Conditioning is not a decoration—it changes the probability.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) The chain rule (three or more events)</h2>
    <p>
      The multiplication rule generalizes. For three events A, B, C:
    </p>
  </div>

  <div class="card">
    <p style="font-size:1.1rem; margin:0;">
      <strong>P(A ∩ B ∩ C) = P(A) · P(B | A) · P(C | A ∩ B)</strong>
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>General form (n events)</h3>
    <p style="margin:0;">
      <strong>
        P(A₁ ∩ A₂ ∩ ... ∩ Aₙ)
        = P(A₁) · P(A₂ | A₁) · P(A₃ | A₁ ∩ A₂) · ... · P(Aₙ | A₁ ∩ ... ∩ Aₙ₋₁)
      </strong>
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    You do not need to memorize this. Read it as: “multiply along a sequence, conditioning on everything that came before.”
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Independence as a simplification</h2>
    <p>
      Independence is exactly the condition that removes the need to condition.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Definition (in conditional form)</h3>
      <p>
        A and B are independent if:
      </p>
      <p style="margin:0;">
        <strong>P(A|B) = P(A)</strong> (and similarly P(B|A)=P(B))
      </p>
    </div>

    <div class="card">
      <h3>Multiplication under independence</h3>
      <p>
        If A and B are independent, then:
      </p>
      <p style="margin:0;">
        <strong>P(A ∩ B) = P(A) · P(B)</strong>
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        This is not a general rule. It is a special case.
      </p>
    </div>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Critical warning</h2>
      <p style="margin:0;">
        Do not multiply probabilities unless independence is justified by the model or the context.
        “Seems unrelated” is not a proof of independence.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Debugging checklist for multiplication problems</h2>
    <p>
      Use this checklist before you multiply anything.
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Did I define the events clearly?</li>
      <li>Am I computing a joint probability (A ∩ B) or a conditional probability (A|B)?</li>
      <li>Have I chosen an order that makes the conditionals easy to compute?</li>
      <li>Am I assuming independence? If yes, what is the justification?</li>
      <li>Did I condition on the correct earlier events (for 3+ steps)?</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Multiplying P(A)·P(B) without independence</li>
        <li>Forgetting that conditioning changes the probability</li>
        <li>Using the wrong order and creating hard conditional terms</li>
        <li>Confusing joint probability with conditional probability</li>
        <li>For 3+ events: conditioning on too little (forgetting earlier events)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Use <strong>P(A ∩ B)=P(A|B)P(B)</strong> correctly</li>
        <li>Apply the chain rule for multiple events</li>
        <li>Understand independence as the condition that simplifies multiplication</li>
        <li>Be ready for the law of total probability next</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we compute probabilities by splitting the world into cases (a partition). This is the law of total probability.
      </p>
      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/conditional/law-of-total-probability/">
          Next lesson: 3. Law of Total Probability →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/conditional/what-is-conditional-probability/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: What Is Conditional Probability?
          </a>
        </div>
      </div>
    </div>
  </div>
</section>