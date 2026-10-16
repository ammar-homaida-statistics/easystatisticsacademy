---
layout: default
title: Geometric Distribution
description: "Learn how the geometric distribution models waiting times and answers the question: how many trials are needed until the first success occurs?"
permalink: /probability/distributions/geometric-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/geometric-distribution/",
    label: "Geometric Distribution",
    ts: Date.now()
    }));
  } catch (_) {
    // Storage may be disabled; the lesson must still load and remain navigable.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 5</span>
      <span class="badge">Distributions</span>
      <span class="badge">Waiting Times</span>
    </div>

    <h1>Geometric Distribution</h1>

    <p class="lead">
      The binomial distribution counts how many successes occur in a fixed number of trials.
    </p>

    <p class="lead">
      The geometric distribution answers a different question: how many trials are required until the first success occurs?
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/binomial-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/negative-binomial-distribution/">
         Next: Negative Binomial Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Geometric Distribution?</h2>

    <p>
      A geometric distribution models the number of trials needed to obtain the first success in a sequence of independent Bernoulli trials.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Here the geometric random variable counts the trial on which the first success occurs, <strong>including the successful trial</strong>. It does not count only the failures before success.
      </p>

    </div>

    <h2>The Main Question</h2>

    <p>
      Unlike the binomial distribution,
      which counts successes,
      the geometric distribution measures waiting time.
    </p>

    <div class="example-box">

      <p>
        How many coin tosses until the first head?
      </p>

      <p>
        How many customers until the first purchase?
      </p>

      <p>
        How many calls until the first sale?
      </p>

      <p>
        How many inspections until the first defect?
      </p>

    </div>

    <h2>Conditions for a Geometric Distribution</h2>

    <p>
      A geometric model applies when:
    </p>

    <ul class="bullets">

      <li>Trials are independent.</li>

      <li>Each trial has two outcomes.</li>

      <li>The probability of success remains constant.</li>

      <li>We are interested in the first success.</li>

    </ul>

    <p>
      These conditions are very similar to those of the binomial distribution.
    </p>

    <h2>Notation</h2>

    <p>
      A geometric random variable is commonly written as:
    </p>

    
    \[
    X\sim\operatorname{Geom}(p),\qquad 0<p\le1
    \]


    <p>
      where p is the constant success probability on each independent trial, with 0 &lt; p &le; 1. We use the <strong>trials-until-first-success</strong> convention throughout; the alternative failures-before-success convention has support beginning at zero.
    </p>

    <h2>Possible Values</h2>

    <p>
      The first success may occur:
    </p>

    <div class="example-box">

      <p>
        On trial 1
      </p>

      <p>
        On trial 2
      </p>

      <p>
        On trial 3
      </p>

      <p>
        And so on...
      </p>

    </div>

    <p>
      Therefore the possible values are:
    </p>

    
    \[
    X\in\{1,2,3,\ldots\}
    \]


    <h2>The Probability Formula</h2>

    <p>
      The probability that the first success occurs on trial k is:
    </p>

    
    \[
    P(X=k)=(1-p)^{k-1}p,\quad k=1,2,\ldots
    \]


    <p>
      This formula contains two parts:
    </p>

    <ul class="bullets">

      <li>k − 1 failures</li>

      <li>One success on trial k</li>

    </ul>

    <h2>Understanding the Formula</h2>

    <p>
      To achieve the first success on trial k:
    </p>

    <div class="example-box">

      <p>
        Trial 1: Failure
      </p>

      <p>
        Trial 2: Failure
      </p>

      <p>
        ...
      </p>

      <p>
        Trial k − 1: Failure
      </p>

      <p>
        Trial k: Success
      </p>

    </div>

    <p>
      Multiplying those probabilities gives the geometric formula.
    </p>

    <h2>Example: Coin Tosses</h2>

    <p>
      Suppose a fair coin is tossed repeatedly.
    </p>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = Trial on which the first head appears
      </p>

    </div>

    <p>
      Since:
    </p>

    
    \[
    p=P(\text{Head})=\frac12
    \]


    <p>
      The probability that the first head occurs on toss 3 is:
    </p>

    
    \[
    P(X=3)=\left(1-\frac12\right)^{2}\frac12=\frac18=0.125
    \]


    <p>
      Two tails followed by one head.
    </p>


    <!-- GEOMETRIC WAITING TIME EXPLORER -->
    <div class="concept-box esa-geometric-lab" id="esa-geometric-wait-explorer"
         role="group" aria-labelledby="esa-geometric-lab-heading">
      <h2 id="esa-geometric-lab-heading">Interactive Geometric Waiting-Time Explorer</h2>
      <p>Choose a constant success probability p and the trial number k.
         This lesson counts the <strong>number of trials up to and including
         the first success</strong>, so k starts at 1. Every trial is an
         independent Bernoulli trial. The failures-before-success convention
         uses X − 1 and starts at zero instead.</p>
      <div class="esa-geometric-fields">
        <div>
          <label for="esa-geom-p"><strong>Success probability p:
            <output id="esa-geom-p-value" for="esa-geom-p">0.25</output></strong></label>
          <input id="esa-geom-p" type="range" min="0.05" max="1" step="0.05" value="0.25">
        </div>
        <div>
          <label for="esa-geom-k"><strong>Trial number k:
            <output id="esa-geom-k-value" for="esa-geom-k">3</output></strong></label>
          <input id="esa-geom-k" type="range" min="1" max="20" step="1" value="3">
        </div>
      </div>
      <h3>First-success probability by trial (first 12 trials)</h3>
      <svg id="esa-geom-pmf-plot" viewBox="0 0 360 175" width="360" height="175"
           role="img" aria-label="Geometric probabilities for the first 12 trials, p = 0.25; selected k = 3">
        <line x1="31" y1="136" x2="343" y2="136" stroke="currentColor" stroke-width="1.4"/>
        <line x1="31" y1="136" x2="31" y2="17" stroke="currentColor" stroke-width="1.4"/>
        <text x="8" y="15" font-size="10" fill="currentColor">P(X=j)</text>
        <text x="343" y="158" font-size="10" fill="currentColor">Trial</text>
        <g id="esa-geom-bars">
          <rect data-trial="1" x="40" width="17" y="108.5" height="27.5" fill="#64748b"/>
          <rect data-trial="2" x="64" width="17" y="115.375" height="20.625" fill="#64748b"/>
          <rect data-trial="3" x="88" width="17" y="120.53125" height="15.46875" fill="#0d9488"/>
          <rect data-trial="4" x="112" width="17" y="124.3984375" height="11.6015625" fill="#64748b"/>
          <rect data-trial="5" x="136" width="17" y="127.298828125" height="8.701171875" fill="#64748b"/>
          <rect data-trial="6" x="160" width="17" y="129.474121094" height="6.525878906" fill="#64748b"/>
          <rect data-trial="7" x="184" width="17" y="131.10559082" height="4.89440918" fill="#64748b"/>
          <rect data-trial="8" x="208" width="17" y="132.32919312" height="3.67080688" fill="#64748b"/>
          <rect data-trial="9" x="232" width="17" y="133.24689484" height="2.75310516" fill="#64748b"/>
          <rect data-trial="10" x="256" width="17" y="133.93517113" height="2.06482887" fill="#64748b"/>
          <rect data-trial="11" x="280" width="17" y="134.45137835" height="1.54862165" fill="#64748b"/>
          <rect data-trial="12" x="304" width="17" y="134.83853376" height="1.16146624" fill="#64748b"/>
        </g>
        <text x="48" y="151" text-anchor="middle" font-size="10" fill="currentColor">1</text>
        <text x="95" y="151" text-anchor="middle" font-size="10" fill="currentColor">3</text>
        <text x="191" y="151" text-anchor="middle" font-size="10" fill="currentColor">7</text>
        <text x="311" y="151" text-anchor="middle" font-size="10" fill="currentColor">12</text>
      </svg>
      <p class="muted-mini">Bar heights show actual probability (the y-axis spans 0 to 1).
         The selected trial is highlighted when k ≤ 12.
         Remaining probability beyond trial 12 is not displayed as a bar.</p>
      <div class="esa-geometric-results" role="status" aria-live="polite" aria-atomic="true">
        <p><strong>Exactly trial k:</strong>
          P(X = k) = (1 − p)^(k − 1)p =
          <output id="esa-geom-pmf">0.140625</output>.</p>
        <p><strong>At or before trial k:</strong>
          P(X ≤ k) = 1 − (1 − p)^k =
          <output id="esa-geom-cdf">0.578125</output>.</p>
        <p><strong>Later than trial k:</strong>
          P(X &gt; k) = (1 − p)^k =
          <output id="esa-geom-tail">0.421875</output>.</p>
        <p>Expected trials E[X] = 1/p = <output id="esa-geom-mean">4.0000</output>.
           Variance Var(X) = (1 − p)/p² = <output id="esa-geom-variance">12.0000</output>.</p>
        <p><strong>Memorylessness:</strong> After ten failures, the conditional
           probability of success on the next trial is
           <output id="esa-geom-memoryless-next">0.2500</output>.
           The conditional probability of waiting more than three further
           trials is <output id="esa-geom-memoryless-tail">0.421875</output>.</p>
        <p id="esa-geom-memoryless-note" hidden>
          At p = 1, ten previous failures have probability zero; a conditional
          probability given that impossible history is undefined.
          An unconditional success on the next trial still has probability 1.</p>
      </div>
      <button type="button" class="btn btn-outline" id="esa-geom-reset">Reset geometric example</button>
      <p class="muted-mini">Probabilities use the full infinite geometric distribution.
         Displaying the first twelve bars does not truncate, renormalize,
         or alter the reported cumulative and tail probabilities.</p>
    </div>
    <style>
      #esa-geometric-wait-explorer {box-sizing:border-box;width:100%;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-geometric-wait-explorer .esa-geometric-fields {
        display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));
        gap:12px;margin:15px 0
      }
      #esa-geometric-wait-explorer .esa-geometric-fields>div {min-width:0}
      #esa-geometric-wait-explorer label {display:block;margin-bottom:8px}
      #esa-geometric-wait-explorer input[type="range"] {
        display:block;box-sizing:border-box;width:100%;max-width:100%;min-width:0;
        margin:0;padding:0
      }
      #esa-geometric-wait-explorer svg {
        display:block;width:100%;max-width:520px;height:auto;margin:10px auto;
        overflow:visible
      }
      #esa-geometric-wait-explorer h3 {font-size:1.05em;margin:13px 0 9px}
      #esa-geometric-wait-explorer .esa-geometric-results p {margin:11px 0}
      #esa-geometric-wait-explorer [hidden] {display:none!important}
    </style>
    <script>
    (function () {
      "use strict";
      const root=document.getElementById("esa-geometric-wait-explorer");
      if (!root) return;
      const el=id=>root.querySelector("#"+id);
      const probability=el("esa-geom-p"),trial=el("esa-geom-k");
      function update() {
        const p=Number(probability.value),k=Number(trial.value);
        const q=1-p,pmf=Math.pow(q,k-1)*p,tail=Math.pow(q,k);
        const cdf=1-tail;
        el("esa-geom-p-value").textContent=p.toFixed(2);
        el("esa-geom-k-value").textContent=String(k);
        el("esa-geom-pmf").textContent=pmf.toFixed(6);
        el("esa-geom-cdf").textContent=cdf.toFixed(6);
        el("esa-geom-tail").textContent=tail.toFixed(6);
        el("esa-geom-mean").textContent=(1/p).toFixed(4);
        el("esa-geom-variance").textContent=(q/(p*p)).toFixed(4);
        const historyPossible=p<1;
        el("esa-geom-memoryless-next").textContent=historyPossible?p.toFixed(4):"Undefined";
        el("esa-geom-memoryless-tail").textContent=historyPossible?
          Math.pow(q,3).toFixed(6):"Undefined";
        el("esa-geom-memoryless-note").hidden=historyPossible;
        for(const bar of root.querySelectorAll("#esa-geom-bars rect[data-trial]")) {
          const j=Number(bar.getAttribute("data-trial"));
          const pj=Math.pow(q,j-1)*p;
          const height=110*pj;
          bar.setAttribute("y",String(136-height));
          bar.setAttribute("height",String(height));
          bar.setAttribute("fill",j===k?"#0d9488":"#64748b");
        }
        el("esa-geom-pmf-plot").setAttribute("aria-label",
          "Geometric probability of first success on each of the first twelve trials, p = "+
          p.toFixed(2)+", selected trial k = "+k+
          ", P(X=k) = "+pmf.toFixed(6)+
          ". Cumulative and tail calculations use all possible trials.");
      }
      [probability,trial].forEach(input=>input.addEventListener("input",update));
      el("esa-geom-reset").addEventListener("click",()=>{
        probability.value="0.25";trial.value="3";update();
      });
      update();
    })();
    </script>


    <h2>The Mean of a Geometric Distribution</h2>

    <p>
      The expected value is:
    </p>

    
    \[
    E[X]=\frac1p
    \]


    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        The expected waiting time until the first success equals the reciprocal of the success probability.
      </p>

    </div>

    <h2>Example of the Mean</h2>

    <p>
      If:
    </p>

    <div class="example-box">

      <p>
        p = 0.25
      </p>

    </div>

    <p>
      Then:
    </p>

    
    \[
    E[X]=\frac{1}{0.25}=4
    \]


    <p>
      On average,
      four trials are needed before the first success.
    </p>

    <h2>The Variance</h2>

    <p>
      The variance of a geometric distribution is:
    </p>

    
    \[
    \operatorname{Var}(X)=\frac{1-p}{p^2}
    \]


    <p>
      Variability increases as successes become rarer.
    </p>

    <h2>Rare Successes Mean Longer Waiting Times</h2>

    <p>
      As p decreases:
    </p>

    <ul class="bullets">

      <li>The mean increases.</li>

      <li>The variance increases.</li>

      <li>The distribution becomes more spread out.</li>

    </ul>

    <p>
      Rare events require longer waits on average.
    </p>

    <h2>The Memoryless Property</h2>

    <p>
      The geometric distribution has a remarkable property called memorylessness.
    </p>

    <div class="concept-box">

      <strong>Memoryless Property:</strong>

      <p>
        Past failures do not affect future waiting times.
      </p>

    </div>

    <h2>What Memoryless Means</h2>

    <p>
      Suppose you have already observed ten failures.
    </p>

    <p>
      The probability of success on the next trial remains:
    </p>

    
    \[
    P(\text{Head on next toss}\mid\text{10 previous tails})=\frac12=p
    \]


    <p>
      exactly as before, because independent trials have no memory. Here the conditioning event has positive probability (p = 0.5); for p = 1, a previous failure has probability zero and that conditional probability is undefined.
    </p>

    <p>
      Previous failures provide no additional information about future success.
    </p>

    <h2>A Common Misconception</h2>

    <p>
      People often believe that after many failures,
      success becomes "due."
    </p>

    <div class="example-box">

      <p>
        "The coin has landed tails ten times.
        Heads must come soon."
      </p>

    </div>

    <p>
      This is known as the gambler's fallacy.
    </p>

    <p>
      For independent trials,
      the probability remains unchanged.
    </p>

    <h2>Geometric Versus Binomial</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Distribution</th>
            <th>Question Answered</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Binomial</td>
            <td>How many successes occur?</td>
          </tr>

          <tr>
            <td>Geometric</td>
            <td>How long until the first success?</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Both distributions arise from repeated Bernoulli trials but answer different questions.
    </p>

    <h2>Applications of the Geometric Distribution</h2>

    <ul class="bullets">

      <li>Waiting for the first customer purchase</li>

      <li>Waiting for the first equipment failure</li>

      <li>Waiting for the first successful network transmission</li>

      <li>Waiting for the first disease detection</li>

      <li>Waiting for the first sales conversion</li>

    </ul>

    <p>
      Any first-success waiting problem may be modeled geometrically.
    </p>

    <h2>The Shape of the Distribution</h2>

    <p>
      For 0 &lt; p &lt; 1 the trial-count geometric mass decreases with k, producing a right-tailed distribution. At p = 1, success occurs on the first trial with certainty (a degenerate distribution).
    </p>

    <p>
      Small waiting times are common,
      while very long waiting times become progressively less likely.
    </p>

    <p>
      The probability decreases exponentially as the number of trials increases.
    </p>

    <h2>The Limitation</h2>

    <p>
      The geometric distribution focuses on the first success only.
    </p>

    <p>
      Sometimes we want to know:
    </p>

    <div class="example-box">

      <p>
        How many trials are needed until the fifth success?
      </p>

      <p>
        How many customers until the third purchase?
      </p>

    </div>

    <p>
      This broader waiting-time problem leads to the negative binomial distribution.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The negative binomial distribution generalizes the geometric distribution.
    </p>

    <p>
      Instead of waiting for the first success,
      it models the number of trials required to achieve a specified number of successes.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The geometric distribution models waiting time until the first success</li>

        <li>It arises from repeated independent Bernoulli trials</li>

        <li>The probability formula is P(X = k) = (1 − p)<sup>k−1</sup>p</li>

        <li>The mean equals 1/p</li>

        <li>The variance equals (1 − p)/p²</li>

        <li>The geometric distribution is memoryless</li>

        <li>It is commonly used for first-success waiting-time problems</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/binomial-distribution/">
         ← Previous: Binomial Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/negative-binomial-distribution/">
         Next: Negative Binomial Distribution →
      </a>

    </div>

  </div>

</section>