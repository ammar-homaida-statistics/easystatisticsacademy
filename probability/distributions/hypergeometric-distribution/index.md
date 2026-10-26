---
layout: default
title: Hypergeometric Distribution
description: Learn how the hypergeometric distribution models sampling without replacement from a finite population.
permalink: /probability/distributions/hypergeometric-distribution/
sidebar: false
translation_pair: hypergeometric-distribution
math: true
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/hypergeometric-distribution/",
    label: "Hypergeometric Distribution",
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
      <span class="badge">Sampling</span>
    </div>

    <h1>Hypergeometric Distribution</h1>
<p><a lang="ar" dir="rtl" href="/ar/probability/distributions/hypergeometric-distribution/">اقرأ هذا الدرس بالعربية</a></p>

    <p class="lead">
      Many probability models assume independent trials with replacement.
    </p>

    <p class="lead">
      The hypergeometric distribution handles a different situation: sampling without replacement from a finite population.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/poisson-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/uniform-distribution/">
         Next: Uniform Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Hypergeometric Distribution?</h2>

    <p>
      A hypergeometric distribution models the number of successes obtained when drawing a sample from a finite population without replacement.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A hypergeometric random variable counts the number of successes in a sample drawn without replacement from a finite population.
      </p>

    </div>

    <h2>The Key Difference</h2>

    <p>
      Unlike the binomial distribution,
      sampling is performed without replacement.
    </p>

    <p>
      As a result,
      probabilities change after each draw.
    </p>

    <div class="example-box">

      <p>
        Draw one card from a deck.
      </p>

      <p>
        The deck composition changes before the next draw.
      </p>

    </div>

    <p>
      This creates dependence between observations.
    </p>

    <h2>A Classic Example</h2>

    <p>
      Consider a standard deck of 52 cards.
    </p>

    <p>
      Suppose we draw 5 cards.
    </p>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = Number of aces drawn
      </p>

    </div>

    <p>
      Since cards are not replaced,
      X follows a hypergeometric distribution.
    </p>

    <h2>The Four Parameters</h2>

    <p>
      A hypergeometric distribution has three parameters (N, K, n);
      x is a possible observed value of the random variable X.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Parameter</th>
            <th>Meaning</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>N</td>
            <td>Total population size</td>
          </tr>

          <tr>
            <td>K</td>
            <td>Number of successes in population</td>
          </tr>

          <tr>
            <td>n</td>
            <td>Sample size</td>
          </tr>

          <tr>
            <td>x</td>
            <td>Observed successes in sample</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Notation</h2>

    <p>
      A hypergeometric random variable is commonly written as:
    </p>

    <div class="example-box">

      <p>
        X ~ Hypergeometric(N, K, n)
      </p>

    </div>

    <p>
      The parameters N, K, and n describe the population and sampling
      design, with integer N ≥ 1, 0 ≤ K ≤ N, and 0 ≤ n ≤ N.
    </p>

    <h2>Understanding the Population</h2>

    <p>
      Imagine a population containing:
    </p>

    <div class="example-box">

      <p>
        K successes
      </p>

      <p>
        N − K failures
      </p>

    </div>

    <p>
      We draw n items without replacement and count successes.
    </p>

    <h2>The Probability Formula</h2>

    <p>
      The probability of observing exactly x successes is:
    </p>

    \[
P(X=x)=\frac{\binom{K}{x}\binom{N-K}{n-x}}{\binom{N}{n}},
\qquad \max(0,n-(N-K))\le x\le\min(n,K)
\]

    <p>
      This is the hypergeometric probability mass function. The possible
      values of x are integers within the displayed limits; values
      outside this support have probability zero.
    </p>

    <h2>Interpreting the Formula</h2>

    <p>
      The numerator counts favorable samples.
    </p>

    <ul class="bullets">

      <li>Select x successes from K available successes.</li>

      <li>Select n − x failures from N − K failures.</li>

    </ul>

    <p>
      The denominator counts all possible samples of size n.
    </p>

    <h2>Example: Defective Products</h2>

    <p>
      Suppose a shipment contains:
    </p>

    <div class="example-box">

      <p>
        N = 100 products
      </p>

      <p>
        K = 10 defective products
      </p>

    </div>

    <p>
      A sample of:
    </p>

    <div class="example-box">

      <p>
        n = 5 products
      </p>

    </div>

    <p>
      is selected without replacement.
    </p>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = Number of defective products found
      </p>

    </div>

    <p>
      X follows a hypergeometric distribution.
    </p>

    <h2>Possible Values</h2>

    <p>
      The number of successes cannot exceed:
    </p>

    <ul class="bullets">

      <li>The sample size</li>

      <li>The number of successes available</li>

    </ul>

    <p>
      A sample must also contain at least n − (N − K) successes if too few
      failures are available. Thus the valid integer support is
      max(0, n − (N − K)) through min(n, K).
    </p>

    <h2>The Mean</h2>

    <p>
      The expected value is:
    </p>

    \[
\operatorname{E}(X)=n\frac{K}{N}
\]

    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        The expected number of successes equals the sample size multiplied by the population success proportion.
      </p>

    </div>

    <h2>Example of the Mean</h2>

    <p>
      Using:
    </p>

    <div class="example-box">

      <p>
        N = 100
      </p>

      <p>
        K = 10
      </p>

      <p>
        n = 5
      </p>

    </div>

    <p>
      We obtain:
    </p>

    \[
\operatorname{E}(X)=5\left(\frac{10}{100}\right)=0.5
\]

    <p>
      The expected count is 0.5 defective products per sample across
      repeated draws; an individual sample still contains a whole-number count.
    </p>

    <h2>The Variance</h2>

    <p>
      The variance is:
    </p>

    \[
\operatorname{Var}(X)=n\frac{K}{N}\left(1-\frac{K}{N}\right)
\frac{N-n}{N-1},\qquad N>1
\]

    <p>
      The final fraction, (N − n)/(N − 1), is the finite population
      correction factor for this count variance when N &gt; 1.
      For N = 1 the draw count is deterministic and its variance is zero.
    </p>

    <h2>The Finite Population Correction</h2>

    <p>
      Because sampling occurs without replacement,
      observations become dependent.
    </p>

    <p>
      This dependence reduces variability.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        For the same n and success fraction K/N, hypergeometric variance is
        no greater than binomial variance. It is strictly smaller when
        1 &lt; n ≤ N and 0 &lt; K &lt; N (with N &gt; 1);
        at n = 1 the two variances agree.
      </p>

    </div>

    <h2>Hypergeometric Versus Binomial</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Binomial</th>
            <th>Hypergeometric</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Replacement</td>
            <td>With replacement</td>
            <td>Without replacement</td>
          </tr>

          <tr>
            <td>Independence</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Probability Constant?</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Population Size</td>
            <td>Effectively infinite</td>
            <td>Finite</td>
          </tr>

        </tbody>

      </table>

    </div>

    <!-- Batch #60: verified hypergeometric sampling laboratory -->
    <section class="concept-box" id="esa-hypergeom-explorer" role="group"
             aria-labelledby="esa-hg-title" style="max-width:100%;min-width:0;overflow-x:clip;overflow-wrap:anywhere">
      <h2 id="esa-hg-title">Interactive Sampling-Without-Replacement Explorer</h2>
      <p>Choose a finite population of <strong>N</strong> items with <strong>K</strong> successes,
      draw <strong>n</strong> uniformly at random without replacement, and find the probability
      of observing <strong>x</strong> successes. Compare the exact hypergeometric model with
      a binomial approximation based on independent draws with <span dir="ltr">p = K/N</span>.</p>
      <div class="esa-hg-grid">
        <div><label for="esa-hg-N">Population size N (1–1000)</label>
        <input id="esa-hg-N" type="number" min="1" max="1000" step="1" value="100" inputmode="numeric"></div>
        <div><label for="esa-hg-K">Population successes K (0–N)</label>
        <input id="esa-hg-K" type="number" min="0" max="1000" step="1" value="10" inputmode="numeric"></div>
        <div><label for="esa-hg-n">Sample size n (0–min(N, 100))</label>
        <input id="esa-hg-n" type="number" min="0" max="100" step="1" value="5" inputmode="numeric"></div>
        <div><label for="esa-hg-x">Observed successes x (0–n)</label>
        <input id="esa-hg-x" type="number" min="0" max="100" step="1" value="1" inputmode="numeric"></div>
      </div>
      <button type="button" class="btn btn-outline" id="esa-hg-reset">Reset example</button>
      <p id="esa-hg-status" role="status" aria-live="polite"></p>
      <div class="table-wrap"><table>
        <caption>Probabilities and distribution summaries (six decimal places)</caption>
        <tbody>
          <tr><th scope="row">Feasible success counts</th><td id="esa-hg-support">—</td></tr>
          <tr><th scope="row">Exact probability P(X = x)</th><td id="esa-hg-exact">—</td></tr>
          <tr><th scope="row">Binomial approximation P(Y = x)</th><td id="esa-hg-approx">—</td></tr>
          <tr><th scope="row">Absolute probability difference</th><td id="esa-hg-difference">—</td></tr>
          <tr><th scope="row">Expected successes E(X)</th><td id="esa-hg-mean">—</td></tr>
          <tr><th scope="row">Variance Var(X)</th><td id="esa-hg-variance">—</td></tr>
          <tr><th scope="row">Exact probabilities summed</th><td id="esa-hg-total">—</td></tr>
          <tr><th scope="row">Sampling fraction n/N</th><td id="esa-hg-sampling-fraction">—</td></tr>
        </tbody>
      </table></div>
      <p class="muted-mini">Teal: exact probability without replacement. Amber: binomial approximation with replacement.
      The same horizontal scale shows the success count <span dir="ltr">x = 0, …, n</span>.</p>
      <svg id="esa-hg-chart" viewBox="0 0 720 250" role="img"
           aria-label="Comparison of hypergeometric and binomial probabilities"
           style="display:block;width:100%;height:auto;max-width:100%;overflow:hidden">
        <g id="esa-hg-bars"></g>
      </svg>
      <p class="muted-mini">The exact distribution has integer support
      <span dir="ltr">max(0, n − (N − K)) ≤ x ≤ min(n, K)</span>.
      Outside this interval its probability is zero. The binomial comparison is
      an approximation; the 5% sampling-fraction guideline is a heuristic, not a guarantee.</p>
      <div class="example-box"><strong>Independent reference check:</strong>
        for <span dir="ltr">N = 10, K = 3, n = 2, x = 1</span>,
        the exact probability is <span dir="ltr">C(3,1)C(7,1)/C(10,2) = 21/45 ≈ 0.466667</span>,
        versus a binomial approximation of <span dir="ltr">2(0.3)(0.7) = 0.420000</span>.
        The exact variance is <span dir="ltr">2(0.3)(0.7)(8/9) ≈ 0.373333</span>.
      </div>
    </section>
    <style>
      @media(max-width:760px) {
        #main-content .content-narrow{width:100%;max-width:100%;min-width:0;overflow-x:clip}
        #main-content .content-narrow .table-wrap{display:block;width:100%;max-width:100%;overflow-x:auto}
      }
      #esa-hypergeom-explorer, #esa-hypergeom-explorer * {box-sizing:border-box}
      #esa-hypergeom-explorer .esa-hg-grid {display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,205px),1fr));gap:1rem;margin:1rem 0}
      #esa-hypergeom-explorer .esa-hg-grid>div {min-width:0}
      #esa-hypergeom-explorer label {display:block;font-weight:650;margin-bottom:.35rem}
      #esa-hypergeom-explorer input {display:block;width:100%;min-width:0;padding:.65rem;
        border:1px solid #888;border-radius:.35rem;color:inherit;background:var(--surface,#fff);font:inherit}
      #esa-hypergeom-explorer .table-wrap {max-width:100%;overflow-x:auto}
      #esa-hypergeom-explorer td {font-variant-numeric:tabular-nums}
      #esa-hypergeom-explorer #esa-hg-status {overflow-wrap:anywhere}
      @media(max-width:760px) {
        #esa-hypergeom-explorer .esa-hg-grid{grid-template-columns:minmax(0,1fr)}
      }
    </style>
    <script src="/js/hypergeometric-explorer.js" defer></script>

    <h2>When Binomial Is a Good Approximation</h2>

    <p>
      If the population is very large relative to the sample:
    </p>

    <div class="example-box">

      <p>
        Sample size is less than about 5% of the population.
      </p>

    </div>

    <p>
      Then the hypergeometric distribution is often well approximated by a binomial distribution.
    </p>

    <p>
      In that case,
      dependence becomes negligible.
    </p>

    <h2>Applications of the Hypergeometric Distribution</h2>

    <ul class="bullets">

      <li>Quality control sampling</li>

      <li>Card games</li>

      <li>Election auditing</li>

      <li>Inventory inspection</li>

      <li>Biological sampling</li>

      <li>Survey analysis</li>

    </ul>

    <p>
      Any finite-population sampling problem without replacement may involve a hypergeometric model.
    </p>

    <h2>The Shape of the Distribution</h2>

    <p>
      Hypergeometric distributions can be symmetric or skewed depending on:
    </p>

    <ul class="bullets">

      <li>Population size</li>

      <li>Success proportion</li>

      <li>Sample size</li>

    </ul>

    <p>
      Their shapes often resemble binomial distributions when populations are large.
    </p>

    <h2>Why This Distribution Matters</h2>

    <p>
      The hypergeometric distribution provides a realistic model for many sampling situations because real-world sampling often occurs without replacement.
    </p>

    <p>
      It bridges probability theory and practical statistical sampling.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      So far,
      we have focused primarily on discrete distributions.
    </p>

    <p>
      The next lesson introduces the uniform distribution,
      one of the simplest continuous probability distributions and the starting point for continuous probability models.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The hypergeometric distribution models sampling without replacement</li>

        <li>It counts successes drawn from a finite population</li>

        <li>The distribution depends on N, K, and n</li>

        <li>The mean equals n(K/N)</li>

        <li>The variance includes a finite population correction factor</li>

        <li>Sampling without replacement creates dependence between observations</li>

        <li>Hypergeometric models are widely used in quality control and survey sampling</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/poisson-distribution/">
         ← Previous: Poisson Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/uniform-distribution/">
         Next: Uniform Distribution →
      </a>

    </div>

  </div>

</section>