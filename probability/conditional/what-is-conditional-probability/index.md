---
layout: default
title: "1. What Is Conditional Probability?"
description: "How new information changes probability by restricting the sample space."
permalink: /probability/conditional/what-is-conditional-probability/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5;border:2px solid #ff9800;padding:2rem;border-radius:12px;">
    <h2 style="margin-top:0;color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>Version 0 focuses on conceptual clarity. Visuals and simulations will be added later.</p>
  </div>
</section>

<script>
(function(){
  var KEY="esa_continue_probability_conditional_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/probability/conditional/what-is-conditional-probability/",
    label:"Lesson 1 — What Is Conditional Probability?",
    ts:Date.now()
  }));
})();
</script>

<section class="section">
<h2>Core Idea</h2>
<p>
Conditional probability measures the probability of an event
given that another event has already occurred.
</p>

<p><strong>P(A | B) = P(A ∩ B) / P(B)</strong> (if P(B) &gt; 0)</p>

<p>
Conditioning restricts the sample space to B.
All probabilities are recalculated within that restricted universe.
</p>
</section>

<section class="section">
<h2>Key Insight</h2>
<ul class="bullets">
<li>Probability is always defined relative to assumptions</li>
<li>“Given” signals restriction</li>
<li>Conditional probability is not symmetric</li>
</ul>
</section>

<section class="section section-slim">
<div class="callout">
<h2>Next Lesson</h2>
<a class="btn" href="/probability/conditional/multiplication-rule/">
2. The Multiplication Rule →
</a>
</div>
</section>