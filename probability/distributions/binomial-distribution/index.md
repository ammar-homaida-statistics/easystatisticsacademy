---
layout: default
title: Binomial Distribution
description: Learn how the binomial distribution models the number of successes in a fixed number of independent Bernoulli trials.
permalink: /probability/distributions/binomial-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/binomial-distribution/",
    label: "Binomial Distribution",
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
      <span class="badge">Discrete</span>
    </div>

    <h1>Binomial Distribution</h1>

    <p class="lead">
      The Bernoulli distribution models a single success-or-failure trial.
    </p>

    <p class="lead">
      The binomial distribution extends this idea to multiple independent trials and counts the total number of successes.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/bernoulli-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/geometric-distribution/">
         Next: Geometric Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Binomial Distribution?</h2>

    <p>
      A binomial distribution describes the number of successes in a fixed number of independent, identically distributed Bernoulli trials with common success probability p. Differing success probabilities lead to a Poisson-binomial model, and dependence generally requires a different model.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A binomial random variable counts successes in n independent trials, each with exactly two outcomes and the same success probability p (0 ≤ p ≤ 1). The count is a sum of n Bernoulli indicators.
      </p>

    </div>

    <h2>The Four Conditions</h2>

    <p>
      A situation follows a binomial distribution when all four conditions are satisfied.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Condition</th>
            <th>Description</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Fixed Number of Trials</td>
            <td>The number of trials is predetermined.</td>
          </tr>

          <tr>
            <td>Independent Trials</td>
            <td>One outcome does not affect another.</td>
          </tr>

          <tr>
            <td>Two Outcomes</td>
            <td>Success or failure.</td>
          </tr>

          <tr>
            <td>Constant Probability</td>
            <td>The success probability remains the same.</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>A Coin Toss Example</h2>

    <p>
      Suppose a fair coin is tossed 10 times.
    </p>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = Number of heads
      </p>
    </div>

    <p>
      Then X follows a binomial distribution because:
    </p>

    <ul class="bullets">

      <li>There are 10 trials.</li>

      <li>Each toss is independent.</li>

      <li>Each toss results in heads or tails.</li>

      <li>The probability of heads remains 0.5.</li>

    </ul>

    <h2>Notation</h2>

    <p>
      A binomial random variable is written as:
    </p>

    \[
X\sim\operatorname{Binomial}(n,p)
\]

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>n = number of trials</li>

      <li>p = probability of success</li>

    </ul>

    <h2>Possible Values</h2>

    <p>
      A binomial variable can take values:
    </p>

    \[
X\in\{0,1,\ldots,n\}
\]

    <p>
      because counts from zero to n are the mathematical range. When p = 0 or p = 1, however, only one endpoint count has positive probability.
    </p>

    <h2>The Probability Formula</h2>

    <p>
      The probability of observing exactly k successes is:
    </p>

    \[
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k},\quad k=0,\ldots,n
\]

    <p>
      This is called the binomial probability mass function.
    </p>

    <h2>Understanding the Formula</h2>

    <p>
      For 0 < p < 1, the formula contains three factors. At p = 0 or p = 1 the distribution is degenerate (all failures or all successes), which is handled directly by its limiting probabilities.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Part</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>n choose k</td>
            <td>Number of possible arrangements</td>
          </tr>

          <tr>
            <td>p<sup>k</sup></td>
            <td>Probability of k successes</td>
          </tr>

          <tr>
            <td>(1-p)<sup>n-k</sup></td>
            <td>Probability of remaining failures</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Combination Term</h2>

    <p>
      The notation:
    </p>

    \[
\binom{n}{k}=\frac{n!}{k!(n-k)!}
\]

    <p>
      counts the number of ways k successes can be placed among n trials.
    </p>

    <p>
      It is read as:
    </p>

    <div class="example-box">

      <p>
        "n choose k"
      </p>

    </div>

    <h2>Example: Exactly Two Heads</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        n = 3
      </p>

      <p>
        p = 0.5
      </p>

    </div>

    <p>
      What is the probability of exactly two heads?
    </p>

    <p>
      Applying the formula:
    </p>

    \[
P(X=2)=\binom{3}{2}(0.5)^2(0.5)^{3-2}
\]

    <p>
      Since:
    </p>

    \[
\binom{3}{2}=3
\]

    <p>
      the probability becomes:
    </p>

    \[
P(X=2)=3(0.5)^3=0.375
\]

    <h2>Mean of a Binomial Distribution</h2>

    <p>
      The expected value is:
    </p>

    \[
\operatorname{E}(X)=np
\]

    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        The expected number of successes equals the number of trials multiplied by the success probability.
      </p>

    </div>

    <h2>Example of the Mean</h2>

    <p>
      If:
    </p>

    <div class="example-box">

      <p>
        n = 100
      </p>

      <p>
        p = 0.2
      </p>

    </div>

    <p>
      Then:
    </p>

    \[
\operatorname{E}(X)=100(0.2)=20
\]

    <p>
      The expected count is exactly 20; any observed count still varies from sample to sample.
    </p>

    <h2>Variance of a Binomial Distribution</h2>

    <p>
      The variance is:
    </p>

    \[
\operatorname{Var}(X)=np(1-p)
\]

    <p>
      The standard deviation is:
    </p>

    \[
\operatorname{SD}(X)=\sqrt{np(1-p)}
\]

    <h2>Why the Formula Makes Sense</h2>

    <p>
      A binomial variable is the sum of n independent Bernoulli variables.
    </p>

    <p>
      Since each Bernoulli trial has:
    </p>

    \[
\operatorname{Var}(I_i)=p(1-p)
\]

    <p>
      the variances add together:
    </p>

    \[
\operatorname{Var}(X)=\operatorname{Var}\!\left(\sum_{i=1}^{n}I_i\right)=\sum_{i=1}^{n}\operatorname{Var}(I_i)=np(1-p)
\]


    <!-- INTERACTIVE BINOMIAL PROBABILITY CALCULATOR -->
    <section class="concept-box" id="esa-binomial-calculator"
             aria-labelledby="esa-binomial-calculator-heading">
      <h2 id="esa-binomial-calculator-heading">Interactive Binomial Probability Calculator</h2>
      <p>For <strong>n independent, identically distributed Bernoulli trials</strong>
         with common success probability p, calculate exact and inclusive tail probabilities
         for the number of successes X. The calculator supports 1 to 1,000 trials.</p>
      <form id="esa-binomial-calculator-form" novalidate>
        <div class="esa-binomial-input-grid">
          <div>
            <label for="esa-binomial-n">Number of trials (n)</label>
            <input type="number" id="esa-binomial-n" inputmode="numeric"
                   min="1" max="1000" step="1" value="3" required>
          </div>
          <div>
            <label for="esa-binomial-p">Success probability (p)</label>
            <input type="number" id="esa-binomial-p" inputmode="decimal"
                   min="0" max="1" step="any" value="0.5" required>
          </div>
          <div>
            <label for="esa-binomial-k">Success count (k)</label>
            <input type="number" id="esa-binomial-k" inputmode="numeric"
                   min="0" max="1000" step="1" value="2" required>
          </div>
        </div>
        <p class="esa-binomial-math-note"><strong>Probability rule:</strong>
          P(X = k) = C(n,k) × p<sup>k</sup> × (1 − p)<sup>n−k</sup>.
          Both cumulative results include k.
        </p>
        <div class="example-box" id="esa-binomial-result-region" role="status" aria-live="polite">
          <div class="esa-binomial-result-grid">
            <p>P(X = k): <strong><output id="esa-binomial-exact">0.375</output></strong></p>
            <p>P(X ≤ k): <strong><output id="esa-binomial-cdf">0.875</output></strong></p>
            <p>P(X ≥ k): <strong><output id="esa-binomial-upper">0.5</output></strong></p>
            <p>Mean (np): <strong><output id="esa-binomial-mean">1.5</output></strong></p>
            <p>Variance (np(1−p)): <strong><output id="esa-binomial-variance">0.75</output></strong></p>
          </div>
          <p id="esa-binomial-explanation">With n = 3, p = 0.5 and k = 2, exactly two successes have probability 0.375.</p>
        </div>
        <p id="esa-binomial-error" role="alert" hidden></p>
      </form>
      <p class="muted-mini"><strong>Assumptions and limits:</strong>
        n is a fixed positive integer, every trial is binary, trials are independent,
        and p stays constant. When n = 1 this is exactly a Bernoulli distribution.
        At p = 0 all counts are zero; at p = 1 all counts equal n.
        The three probabilities are computed by log-space summation, avoiding
        subtracting near-one cumulative probabilities. Values smaller than the
        floating-point representation limit may display as zero.
        Dependent trials or independent trials with different probabilities generally
        require a different model.
      </p>
    </section>
    <style>
      #esa-binomial-calculator{max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-binomial-calculator .esa-binomial-input-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:16px 0}
      #esa-binomial-calculator .esa-binomial-input-grid>div{min-width:0}
      #esa-binomial-calculator label{display:block;font-weight:650;margin:0 0 6px}
      #esa-binomial-calculator input[type="number"]{display:block;width:100%;max-width:100%;min-width:0;box-sizing:border-box;background:var(--surface);color:var(--text);border:1px solid var(--border-strong);border-radius:8px;padding:10px;font:inherit}
      #esa-binomial-calculator input:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
      #esa-binomial-calculator .esa-binomial-result-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 16px}
      #esa-binomial-calculator .esa-binomial-result-grid>*{min-width:0;margin:4px 0}
      #esa-binomial-calculator .esa-binomial-math-note{overflow-wrap:anywhere}
      #esa-binomial-calculator #esa-binomial-error{color:#b42318;font-weight:650}
      @media(max-width:620px){
        #esa-binomial-calculator .esa-binomial-input-grid{grid-template-columns:minmax(0,1fr)}
        #esa-binomial-calculator .esa-binomial-result-grid{grid-template-columns:minmax(0,1fr)}
      }
    </style>
    <script>
    (function () {
      const form = document.getElementById("esa-binomial-calculator-form");
      if (!form) return;
      const nInput = document.getElementById("esa-binomial-n");
      const pInput = document.getElementById("esa-binomial-p");
      const kInput = document.getElementById("esa-binomial-k");
      const exact = document.getElementById("esa-binomial-exact");
      const cumulative = document.getElementById("esa-binomial-cdf");
      const upper = document.getElementById("esa-binomial-upper");
      const mean = document.getElementById("esa-binomial-mean");
      const variance = document.getElementById("esa-binomial-variance");
      const explanation = document.getElementById("esa-binomial-explanation");
      const error = document.getElementById("esa-binomial-error");
      const outputs = [exact,cumulative,upper,mean,variance];

      function format(x) {
        if (x === 0) return "0";
        if (Math.abs(x) < 1e-8) return x.toExponential(8);
        return Number(x.toPrecision(12)).toLocaleString("en-US",{maximumFractionDigits:12});
      }
      function inclusiveLogSum(logTerms, start, end) {
        let peak = -Infinity;
        for (let i = start; i <= end; ++i) peak = Math.max(peak,logTerms[i]);
        let total = 0;
        for (let i = start; i <= end; ++i) total += Math.exp(logTerms[i] - peak);
        return Math.min(1, Math.max(0, Math.exp(peak) * total));
      }
      function render() {
        const n = Number(nInput.value);
        const p = Number(pInput.value);
        const k = Number(kInput.value);
        let problem = "";
        if (!nInput.value.trim() || !Number.isSafeInteger(n) || n < 1 || n > 1000) {
          problem = "Enter a whole number of trials from 1 to 1,000.";
        } else if (!pInput.value.trim() || !Number.isFinite(p) || p < 0 || p > 1) {
          problem = "Enter a success probability between 0 and 1 inclusive.";
        } else if (!kInput.value.trim() || !Number.isSafeInteger(k) || k < 0 || k > n) {
          problem = "Enter a whole number of successes between 0 and n inclusive.";
        }
        if (problem) {
          outputs.forEach(out => { out.textContent = "—"; });
          explanation.textContent = "";
          error.textContent = problem;
          error.hidden = false;
          return;
        }
        error.textContent = "";
        error.hidden = true;
        let px, lower, greater;
        if (p === 0 || p === 1) {
          const determined = p === 0 ? 0 : n;
          px = k === determined ? 1 : 0;
          lower = determined <= k ? 1 : 0;
          greater = determined >= k ? 1 : 0;
        } else {
          // Log factorials and log-sum-exp keep inclusive tails stable even
          // when subtracting from 1 would lose the small tail probability.
          const logFactorial = [0];
          for (let j = 1; j <= n; ++j)
            logFactorial[j] = logFactorial[j-1] + Math.log(j);
          const logP = Math.log(p), logQ = Math.log1p(-p);
          const terms = [];
          for (let j = 0; j <= n; ++j) {
            terms[j] = logFactorial[n] - logFactorial[j] - logFactorial[n-j] +
                       j*logP + (n-j)*logQ;
          }
          px = Math.exp(terms[k]);
          lower = inclusiveLogSum(terms, 0, k);
          greater = inclusiveLogSum(terms, k, n);
        }
        exact.textContent = format(px);
        cumulative.textContent = format(lower);
        upper.textContent = format(greater);
        mean.textContent = format(n*p);
        variance.textContent = format(n*p*(1-p));
        explanation.textContent = "For " + n + " trials with p = " + p +
          ", the chance of exactly " + k + " successes is " + format(px) +
          ". P(X ≤ " + k + ") includes up to " + k +
          " successes; P(X ≥ " + k + ") includes " + k +
          " and larger counts. These are probabilities, not predictions of a guaranteed count.";
      }
      form.addEventListener("input",render);
      form.addEventListener("change",render);
      form.addEventListener("submit",e => { e.preventDefault(); render(); });
      render();
    })();
    </script>

    <h2>Shape of the Distribution</h2>

    <p>
      The shape depends on p.
    </p>

    <div class="example-box">

      <p>
        p = 0.5 → symmetric
      </p>

      <p>
        p &lt; 0.5 → right-skewed
      </p>

      <p>
        p &gt; 0.5 → left-skewed
      </p>

    </div>

    <p>
      As n grows, a normal approximation may become useful when both np and n(1 − p) are sufficiently large. Increasing n alone does not guarantee an approximately symmetric bell shape, especially if p is near 0 or 1.
    </p>

    <h2>Real-World Applications</h2>

    <ul class="bullets">

      <li>Number of customers who purchase a product</li>

      <li>Number of defective items in a batch</li>

      <li>Number of successful sales calls</li>

      <li>Number of patients responding to treatment</li>

      <li>Number of voters supporting a candidate</li>

    </ul>

    <p>
      Repeated success/failure outcomes follow a binomial count model only if the number of trials is fixed, each trial is binary, trials are independent, and all share the same success probability.
    </p>

    <h2>Bernoulli Versus Binomial</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Distribution</th>
            <th>Models</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Bernoulli</td>
            <td>One trial</td>
          </tr>

          <tr>
            <td>Binomial</td>
            <td>Multiple trials</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The binomial distribution is the sum of independent Bernoulli trials with the same p. With n = 1, the binomial distribution is exactly Bernoulli(p). With unequal probabilities, even independent trials generally have a different success-count distribution.
    </p>

    <h2>The Limitation</h2>

    <p>
      The binomial distribution answers:
    </p>

    <div class="example-box">

      <p>
        How many successes occur in n trials?
      </p>

    </div>

    <p>
      Sometimes we are interested in a different question:
    </p>

    <div class="example-box">

      <p>
        How long must we wait until the first success occurs?
      </p>

    </div>

    <p>
      This leads to the geometric distribution.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The geometric distribution models the number of trials required to obtain the first success.
    </p>

    <p>
      It introduces waiting-time models, an important class of probability distributions.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>A binomial distribution counts successes in n independent Bernoulli trials</li>

        <li>Binomial variables are written as Bin(n,p)</li>

        <li>The probability formula uses combinations and success probabilities</li>

        <li>The mean equals np</li>

        <li>The variance equals np(1 − p)</li>

        <li>The binomial distribution is built from repeated Bernoulli trials</li>

        <li>It is widely used for modeling repeated success/failure experiments</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/bernoulli-distribution/">
         ← Previous: Bernoulli Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/geometric-distribution/">
         Next: Geometric Distribution →
      </a>

    </div>

  </div>

</section>