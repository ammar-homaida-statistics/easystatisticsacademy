---
layout: default
title: "1. What Is Conditional Probability?"
description: "Conditional probability as probability under new information: how conditioning restricts the sample space and how to compute P(A|B) correctly."
permalink: /probability/conditional/what-is-conditional-probability/
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
      url: "/probability/conditional/what-is-conditional-probability/",
      label: "Lesson 1 — What Is Conditional Probability?",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Lesson 1</span>
        <span class="badge">Conditioning</span>
        <span class="badge">Updating</span>
      </div>

      <h1>1. What Is Conditional Probability?</h1>
      <p class="lead">
        Conditional probability is probability after you learn new information. This lesson explains the idea
        precisely: conditioning <strong>restricts the sample space</strong> and forces you to recompute probabilities
        inside that restricted universe.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/conditional/">Back to Block 2</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Version 0: correct structure first. Visuals and software examples will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to interpret conditioning correctly, compute
      <strong>P(A | B)</strong> using the definition, and avoid the most common conceptual mistakes
      (especially confusing <strong>P(A|B)</strong> with <strong>P(B|A)</strong>).
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Conditional probability is ordinary probability computed in a reduced sample space.</strong>
        The phrase “given B” means: “restrict attention to outcomes where B happened.”
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Intuition: probability after learning information</h2>
    <p>
      Before you observe anything, many outcomes are possible. When you learn that some event <strong>B</strong>
      occurred, you remove all outcomes incompatible with <strong>B</strong>. You then recompute probabilities on what remains.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Unconditional probability</h3>
      <p>
        Unconditional probability is what you compute using the full sample space.
        It answers: “How likely is A with no extra information?”
      </p>
      <ul class="bullets">
        <li>Full universe: S</li>
        <li>Question: P(A)</li>
        <li>Model defined on all outcomes</li>
      </ul>
    </div>

    <div class="card">
      <h3>Conditional probability</h3>
      <p>
        Conditional probability answers: “How likely is A <em>after</em> we know B happened?”
      </p>
      <ul class="bullets">
        <li>New universe: only outcomes in B</li>
        <li>Question: P(A | B)</li>
        <li>Same model, but restricted to B</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Formal definition</h2>
    <p>
      If <strong>P(B) &gt; 0</strong>, the conditional probability of A given B is defined by:
    </p>
  </div>

  <div class="card">
    <p style="font-size:1.1rem; margin:0;">
      <strong>P(A | B) = P(A ∩ B) / P(B)</strong>
    </p>
  </div>

  <div class="grid grid-2" style="margin-top:1rem;">
    <div class="card">
      <h3>What the numerator means</h3>
      <p>
        <strong>P(A ∩ B)</strong> is the probability that both A and B occur.
        This is the “overlap” of A and B.
      </p>
    </div>

    <div class="card">
      <h3>Why we divide by P(B)</h3>
      <p>
        When we condition on B, we are working inside B. The total probability mass inside B is <strong>P(B)</strong>.
        Dividing rescales so that “B becomes the whole universe” (probability 1 within the conditional world).
      </p>
    </div>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Minimum condition</h2>
      <p style="margin:0;">
        You can only define <strong>P(A|B)</strong> if <strong>P(B) &gt; 0</strong>.  
        If B is impossible under the model, “given B” has no meaning.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Conditioning as “shrinking the sample space”</h2>
    <p>
      The cleanest mental model is this:
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Start with the full sample space <strong>S</strong>.</li>
      <li>Learn that <strong>B</strong> occurred → remove all outcomes not in B.</li>
      <li>Now compute probabilities inside the reduced space <strong>B</strong>.</li>
      <li>A becomes “A within B”, i.e., <strong>A ∩ B</strong>.</li>
    </ul>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Translation rule</h2>
      <p style="margin:0;">
        “Probability of A given B” = “Among outcomes where B happened, how often does A also happen?”
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Conditional probability is NOT symmetric</h2>
    <p>
      A core error (and the reason Bayes’ theorem is needed later) is assuming:
      <strong>P(A|B) = P(B|A)</strong>. This is usually false.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Why people confuse them</h3>
      <p>
        The language “given” feels like it should not matter which side it is on.
        But mathematically, conditioning changes the universe — and changing the universe changes the probability.
      </p>
    </div>

    <div class="card">
      <h3>Correct mindset</h3>
      <p>
        <strong>P(A|B)</strong> asks: “inside B, how often is A true?”  
        <strong>P(B|A)</strong> asks: “inside A, how often is B true?”  
        These are different questions.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Independence connection (preview)</h2>
    <p>
      Independence is a special case of conditional probability:
      learning B does not change the probability of A.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      If A and B are independent, then:
      <strong>P(A | B) = P(A)</strong> and <strong>P(B | A) = P(B)</strong>.
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    We will use this idea repeatedly when building the multiplication rule and Bayes’ theorem.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Treating “given” as a minor detail (it changes the sample space)</li>
        <li>Forgetting the condition <strong>P(B) &gt; 0</strong></li>
        <li>Confusing <strong>P(A|B)</strong> with <strong>P(B|A)</strong></li>
        <li>Assuming independence without justification</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Interpret conditioning as restricting the sample space</li>
        <li>Use the definition <strong>P(A|B)=P(A∩B)/P(B)</strong> correctly</li>
        <li>Recognize that conditional probability is not symmetric</li>
        <li>Be ready to derive the multiplication rule next</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we derive the multiplication rule, which lets us compute joint probabilities using conditional pieces.
      </p>
      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/conditional/multiplication-rule/">
          Next lesson: 2. The Multiplication Rule →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/basics/modeling-randomness-mini-cases/" style="color:#1a73e8; text-decoration:underline;">
            Block 1 — Lesson 8: Modeling Randomness (Mini Cases)
          </a>
        </div>
      </div>
    </div>
  </div>
</section>