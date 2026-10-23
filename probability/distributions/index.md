---
layout: default
title: Block 5 — Common Distributions
description: Learn the most important probability distributions, how to recognize them, interpret their parameters, and use them to model real-world uncertainty.
permalink: /probability/distributions/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_probability_last_block_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/",
    label: "Block 5 — Common Distributions",
    ts: Date.now()
    }));
  } catch (_) {
    // Storage may be disabled; the page still works without saved progress.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card hero-split">

    <!-- LEFT -->

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Probability</span>
        <span class="badge">Block 5</span>
        <span class="badge">Distributions</span>
        <span class="badge">Modeling</span>
      </div>

      <h1>Block 5 — Common Distributions</h1>

      <p class="lead">
        Probability distributions are reusable models of uncertainty.
      </p>

      <p class="lead">
        This block introduces the most important discrete and continuous
        probability distributions used throughout statistics,
        machine learning, engineering, economics, and science.
      </p>

      <p class="muted-mini">
        12 lessons • Applied probability modeling • Builds on Expectation & Variability • Prepares for LLN & CLT
      </p>

      <div class="hero-actions">

        <a class="btn" href="#lessons">
          Open Lessons
        </a>

        <a class="btn btn-outline" href="/probability/">
          Back to Probability
        </a>

      </div>

      <div class="hero-highlight">

        <div class="hero-highlight-icon">
          📊
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            Most real-world probability problems are solved using probability
            distributions. Learning to recognize the correct distribution is one
            of the most valuable skills in probability and statistics.
          </p>

        </div>

      </div>

    </div>

    <!-- RIGHT -->

    <div class="hero-panel">

      <div class="panel-card">

        <h2 class="panel-title">Block overview</h2>

        <div class="mini">
          <div class="mini-title">Lessons</div>
          <div class="mini-body">12 structured lessons</div>
        </div>

        <div class="mini">
          <div class="mini-title">Level</div>
          <div class="mini-body">Applied probability</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Match distributions to real situations
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Next block</div>
          <div class="mini-body">
            Law of Large Numbers & CLT
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-probability-distributions"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-probability-distributions-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-probability-distributions-btn"
        href="#"
      >
        Continue
      </a>

    </div>

  </div>

</section>


<!-- INTERACTIVE DISTRIBUTION SELECTION GUIDE -->
<section class="section" id="esa-distribution-guide" aria-labelledby="esa-distribution-guide-heading">
  <div class="content-narrow">
    <h2 id="esa-distribution-guide-heading">Find a Distribution to Study</h2>
    <p>Start with what your random variable measures, then review the suggested
       model's assumptions. This educational guide does not infer a distribution
       from data or guarantee any model fits a real situation.</p>
    <div class="concept-box esa-distribution-guide-card">
      <label for="esa-distribution-scenario"><strong>What best describes your random outcome?</strong></label>
      <select id="esa-distribution-scenario" aria-controls="esa-distribution-recommendation">
        <option value="">Choose a scenario to see a possible model</option>
        <optgroup label="Discrete outcomes">
          <option value="bernoulli">One success-or-failure observation</option>
          <option value="binomial">Number of successes in a fixed number of trials</option>
          <option value="geometric">Trial number of the first success</option>
          <option value="negative-binomial">Trial number of the r-th success</option>
          <option value="poisson">Count of events over a fixed interval or exposure</option>
          <option value="hypergeometric">Success count sampled without replacement</option>
        </optgroup>
        <optgroup label="Continuous outcomes">
          <option value="uniform">Any value in a finite range with constant density</option>
          <option value="exponential">Time until the next event with constant event rate</option>
          <option value="gamma">Positive waiting time until multiple Poisson events</option>
          <option value="beta">Continuous proportion strictly between 0 and 1</option>
          <option value="normal">Unbounded, symmetric bell-shaped measurement</option>
          <option value="lognormal">Positive, multiplicative, right-skewed measurement</option>
        </optgroup>
      </select>
      <div id="esa-distribution-recommendation" role="status" aria-live="polite" aria-atomic="true">
        <h3 id="esa-distribution-model">Choose a scenario</h3>
        <p id="esa-distribution-reason">Select a question above to see a candidate distribution and the assumptions you must evaluate.</p>
        <p><strong>Necessary assumptions:</strong> <span id="esa-distribution-assumptions">Not yet assessed.</span></p>
        <p><strong>Parameters and convention:</strong> <span id="esa-distribution-parameters">Select a scenario.</span></p>
        <p id="esa-distribution-caveat">Different models can describe similar outcomes. Study the data-generating process, independence, sampling design, and alternative models before choosing.</p>
      </div>
      <a id="esa-distribution-lesson-link" class="btn btn-outline" href="#" hidden>Open matching lesson</a>
    </div>
  </div>
</section>
<style>
  #esa-distribution-guide .esa-distribution-guide-card{min-width:0;max-width:100%;overflow-wrap:anywhere}
  #esa-distribution-guide label{display:block;margin-bottom:8px}
  #esa-distribution-scenario{display:block;width:100%;max-width:100%;min-width:0;box-sizing:border-box;
    background:var(--surface);color:var(--text);border:1px solid var(--border-strong);
    border-radius:8px;padding:12px;font:inherit}
  #esa-distribution-scenario:focus-visible,#esa-distribution-lesson-link:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  #esa-distribution-recommendation{min-width:0;margin:16px 0;overflow-wrap:anywhere}
  #esa-distribution-guide #esa-distribution-model{margin:0 0 8px}
  #esa-distribution-guide [hidden]{display:none!important}
</style>


<!-- LESSONS -->

<section class="section" id="lessons">

  <div class="section-head">

    <h2>Lessons</h2>

    <p>
      These distributions appear repeatedly throughout probability,
      statistical inference, machine learning, operations research,
      and applied data analysis.
    </p>

  </div>

  <!-- DISCRETE -->

  <h3>Discrete Distributions</h3>

  <div class="grid grid-2">

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/bernoulli-distribution/">
          Bernoulli Distribution
        </a>
      </h3>

      <p>
        Model a single success-or-failure trial,
        the foundation of many probability models.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Bernoulli</span>
        <span class="pill">Binary</span>
        <span class="pill">Success</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/bernoulli-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/binomial-distribution/">
          Binomial Distribution
        </a>
      </h3>

      <p>
        Count the number of successes in a fixed number
        of independent Bernoulli trials.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Binomial</span>
        <span class="pill">Counts</span>
        <span class="pill">Trials</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/binomial-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/geometric-distribution/">
          Geometric Distribution
        </a>
      </h3>

      <p>
        Model the waiting time until the first success occurs.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Geometric</span>
        <span class="pill">Waiting Time</span>
        <span class="pill">Memoryless</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/geometric-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/negative-binomial-distribution/">
          Negative Binomial Distribution
        </a>
      </h3>

      <p>
        Generalize geometric waiting times to the occurrence
        of multiple successes.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Negative Binomial</span>
        <span class="pill">Waiting Time</span>
        <span class="pill">Counts</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/negative-binomial-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/poisson-distribution/">
          Poisson Distribution
        </a>
      </h3>

      <p>
        Model counts of events occurring randomly through time,
        distance, area, or volume.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Poisson</span>
        <span class="pill">Counts</span>
        <span class="pill">Rate</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/poisson-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/hypergeometric-distribution/">
          Hypergeometric Distribution
        </a>
      </h3>

      <p>
        Model sampling without replacement and compare it
        with the binomial model.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Hypergeometric</span>
        <span class="pill">Sampling</span>
        <span class="pill">Without Replacement</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/hypergeometric-distribution/">
         Open lesson
      </a>

    </div>

  </div>

  <!-- CONTINUOUS -->

  <h3 style="margin-top:2rem;">
    Continuous Distributions
  </h3>

  <div class="grid grid-2">

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/uniform-distribution/">
          Uniform Distribution
        </a>
      </h3>

      <p>
        Model situations where all values within an interval
        are equally plausible.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Uniform</span>
        <span class="pill">Continuous</span>
        <span class="pill">Equal Density</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/uniform-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/exponential-distribution/">
          Exponential Distribution
        </a>
      </h3>

      <p>
        Model waiting times between events and explore
        the memoryless property.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Exponential</span>
        <span class="pill">Waiting Time</span>
        <span class="pill">Memoryless</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/exponential-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/gamma-distribution/">
          Gamma Distribution
        </a>
      </h3>

      <p>
        Extend exponential models into a flexible family
        of waiting-time distributions.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Gamma</span>
        <span class="pill">Waiting Time</span>
        <span class="pill">Flexible</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/gamma-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/beta-distribution/">
          Beta Distribution
        </a>
      </h3>

      <p>
        Model probabilities themselves and build foundations
        for Bayesian statistics.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Beta</span>
        <span class="pill">Probabilities</span>
        <span class="pill">Bayesian</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/beta-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/normal-distribution/">
          Normal Distribution
        </a>
      </h3>

      <p>
        Study the most important distribution in statistics,
        including standardization and approximation.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Normal</span>
        <span class="pill">Gaussian</span>
        <span class="pill">Standardization</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/normal-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/lognormal-distribution/">
          Lognormal Distribution
        </a>
      </h3>

      <p>
        Model positively skewed quantities generated through
        multiplicative processes.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Lognormal</span>
        <span class="pill">Skewed</span>
        <span class="pill">Growth</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/lognormal-distribution/">
         Open lesson
      </a>

    </div>

  </div>

</section>

<!-- BLOCK MAP -->

<section class="section section-slim">

  <div class="callout">

    <div class="callout-copy">

      <h2>How this block fits into probability</h2>

      <p>
        Previous blocks developed probability tools.
        This block introduces the probability models that repeatedly appear
        throughout applied statistics and scientific analysis.
      </p>

      <div class="table-wrap">

        <table>

          <thead>

            <tr>
              <th>Distribution Family</th>
              <th>Typical Use</th>
            </tr>

          </thead>

          <tbody>

            <tr>
              <td>Bernoulli / Binomial</td>
              <td>Successes and failures</td>
            </tr>

            <tr>
              <td>Geometric / Negative Binomial</td>
              <td>Waiting times for successes</td>
            </tr>

            <tr>
              <td>Poisson</td>
              <td>Event counts</td>
            </tr>

            <tr>
              <td>Uniform</td>
              <td>Equal plausibility</td>
            </tr>

            <tr>
              <td>Exponential / Gamma</td>
              <td>Continuous waiting times</td>
            </tr>

            <tr>
              <td>Beta</td>
              <td>Modeling probabilities</td>
            </tr>

            <tr>
              <td>Normal</td>
              <td>Natural variation and inference</td>
            </tr>

            <tr>
              <td>Lognormal</td>
              <td>Multiplicative growth processes</td>
            </tr>

          </tbody>

        </table>

      </div>

    </div>

  </div>

</section>

<!-- GOALS -->

<section class="section section-slim">

  <div class="callout">

    <div class="callout-copy">

      <h2>Goal of this block</h2>

      <ul class="bullets">

        <li>Recognize common probability distributions from context</li>

        <li>Interpret parameters correctly</li>

        <li>Understand discrete and continuous distribution families</li>

        <li>Compute probabilities using PMFs, PDFs, and CDFs</li>

        <li>Understand relationships between distributions</li>

        <li>Recognize approximation patterns between models</li>

        <li>Prepare for the Law of Large Numbers and Central Limit Theorem</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next block</div>

        <div class="mini-body">
          Continue to <strong>Law of Large Numbers & CLT</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          Distributions are reusable mathematical models of uncertainty.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Big transition</div>

        <div class="mini-body">
          These models become the building blocks of inference.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/probability/expectation-variance/">
      ← Previous Block: Expectation & Variability
    </a>

    <a class="btn" href="/probability/lln-clt/">
      Next Block: Law of Large Numbers & CLT →
    </a>

  </div>

</section>

<!-- DISTRIBUTION GUIDE BEHAVIOR: LESSON CARDS ALREADY IN DOM -->
<script>
(function () {
  const selector = document.getElementById("esa-distribution-scenario");
  const title = document.getElementById("esa-distribution-model");
  const reason = document.getElementById("esa-distribution-reason");
  const assumptions = document.getElementById("esa-distribution-assumptions");
  const parameters = document.getElementById("esa-distribution-parameters");
  const caveat = document.getElementById("esa-distribution-caveat");
  const link = document.getElementById("esa-distribution-lesson-link");
  if (!selector || !title || !reason || !assumptions || !parameters || !caveat || !link) return;
  // Match only lessons already published in this exact block, never user-provided links.
  const published = new Set(
    Array.from(document.querySelectorAll("#lessons .lesson-card h3 a[href]"),
      a => a.getAttribute("href"))
      .filter(url => typeof url === "string" &&
        /^\/probability\/distributions\/[a-z0-9-]+\/$/.test(url))
  );
  const models = Object.freeze({
    "bernoulli": {
      name:"Bernoulli distribution",
      path:"/probability/distributions/bernoulli-distribution/",
      why:"A single binary trial coded 1 for success and 0 for failure.",
      assumptions:"Exactly two outcomes for one trial; specify which outcome is a success. Repeated observations need not be independent to be Bernoulli individually.",
      parameters:"p = P(success), 0 ≤ p ≤ 1.",
      caution:"If you instead count successes across several trials, investigate the binomial or Poisson-binomial distributions."
    },
    "binomial": {
      name:"Binomial distribution",
      path:"/probability/distributions/binomial-distribution/",
      why:"Counts successes in a fixed number of binary trials.",
      assumptions:"Predetermined number of trials n; independent Bernoulli outcomes; the same success probability p for every trial.",
      parameters:"n = positive integer trial count; p = common success probability (0 ≤ p ≤ 1).",
      caution:"Sampling without replacement can favor hypergeometric; unequal success probabilities or dependence generally invalidate the binomial PMF."
    },
    "geometric": {
      name:"Geometric distribution",
      path:"/probability/distributions/geometric-distribution/",
      why:"Counts the trial number on which the first success occurs.",
      assumptions:"Independent binary trials with constant p > 0, continuing until the first success.",
      parameters:"p = chance of success per trial; X ∈ {1,2,3,…} counts trials INCLUDING the successful trial.",
      caution:"Another geometric convention counts failures before the first success and starts at zero. This lesson uses the trials-counted convention."
    },
    "negative-binomial": {
      name:"Negative binomial distribution",
      path:"/probability/distributions/negative-binomial-distribution/",
      why:"Counts trials needed to reach the r-th success.",
      assumptions:"Independent binary trials with a constant chance p > 0 of success, continued until r successes.",
      parameters:"r = positive integer target successes; p = per-trial success probability; X ≥ r counts trials INCLUDING the r-th successful trial.",
      caution:"Some sources parameterize failures before r successes; this lesson uses the number of trials instead. Negative-binomial count-regression models may use another parameterization."
    },
    "poisson": {
      name:"Poisson distribution",
      path:"/probability/distributions/poisson-distribution/",
      why:"Counts events across a fixed interval, area or exposure.",
      assumptions:"A Poisson-process interpretation requires independent increments and a constant event rate; events do not cluster beyond the model.",
      parameters:"λ ≥ 0 is the expected event count over the stated exposure; counts X = 0,1,2,… .",
      caution:"Overdispersion, temporal dependence or changing intensity may require a different count model. Always define the exposure."
    },
    "hypergeometric": {
      name:"Hypergeometric distribution",
      path:"/probability/distributions/hypergeometric-distribution/",
      why:"Counts selected successes in a fixed-size draw without replacement from a finite population.",
      assumptions:"The finite population contains N items, K labeled successes, and a simple random sample of n items is drawn without replacement.",
      parameters:"N = population size; K = successes in population; n = draw count; X = successes in the draw.",
      caution:"Without replacement, draws are dependent. With replacement and constant p, the binomial distribution may be appropriate instead."
    },
    "uniform": {
      name:"Continuous uniform distribution",
      path:"/probability/distributions/uniform-distribution/",
      why:"Models values with constant probability density across a bounded interval.",
      assumptions:"The outcome is continuous and its density is constant between two finite endpoints a and b.",
      parameters:"a < b; support [a,b]; density 1/(b−a) inside this interval.",
      caution:"Equal density does not mean every precise real-valued outcome has positive probability. Endpoint values have probability zero for continuous models."
    },
    "exponential": {
      name:"Exponential distribution",
      path:"/probability/distributions/exponential-distribution/",
      why:"Models positive waiting time until the next event in a homogeneous Poisson process.",
      assumptions:"Continuous waiting time with constant hazard/rate; the memoryless property is appropriate.",
      parameters:"λ > 0 is the event rate; mean waiting time is 1/λ.",
      caution:"A nonconstant hazard or time-varying event intensity calls for other models."
    },
    "gamma": {
      name:"Gamma distribution",
      path:"/probability/distributions/gamma-distribution/",
      why:"Models a positive waiting time to accumulated events; integer shapes give Erlang waiting times.",
      assumptions:"A Gamma-shaped positive outcome is plausible; waiting for multiple Poisson events additionally assumes independent, homogeneous increments.",
      parameters:"α > 0 is the shape and λ > 0 is the RATE (not scale); mean = α/λ. For integer α, event-waiting interpretation is direct.",
      caution:"The alternative scale parameter is θ = 1/λ; check whether a source uses rate or scale before comparing formulas."
    },
    "beta": {
      name:"Beta distribution",
      path:"/probability/distributions/beta-distribution/",
      why:"Models a continuous proportion or probability on the unit interval.",
      assumptions:"The quantity is continuously distributed between 0 and 1 (typically without point masses at exactly 0 or 1).",
      parameters:"α > 0 and β > 0 are the two shape parameters.",
      caution:"Observed exact zeros/ones, repeated categorical counts or proportions with different denominators may need a different model."
    },
    "normal": {
      name:"Normal distribution",
      path:"/probability/distributions/normal-distribution/",
      why:"Models approximately symmetric, bell-shaped variation on the whole real line.",
      assumptions:"An unbounded, continuous symmetric model is credible; measurements or errors should be checked for skewness, outliers and inappropriate negative tails.",
      parameters:"μ is the mean; σ > 0 is the standard deviation.",
      caution:"Normality is an assumption to evaluate, not a consequence of measuring a continuous variable."
    },
    "lognormal": {
      name:"Lognormal distribution",
      path:"/probability/distributions/lognormal-distribution/",
      why:"Models positive quantities with right-skewed behavior and multiplicative variation.",
      assumptions:"The measurement is strictly positive and its logarithm is approximately normally distributed.",
      parameters:"log(X) is Normal(μ,σ²), with σ > 0; μ and σ refer to LOG-scale location and spread.",
      caution:"Zeros, negative values or unusually heavy positive tails can invalidate a simple lognormal model."
    }
  });
  function render() {
    const model = Object.prototype.hasOwnProperty.call(models,selector.value)
      ? models[selector.value] : null;
    if (!model || !published.has(model.path)) {
      title.textContent = "Choose a scenario";
      reason.textContent = "Select a question above to see a candidate distribution and the assumptions you must evaluate.";
      assumptions.textContent = "Not yet assessed.";
      parameters.textContent = "Select a scenario.";
      caveat.textContent = "Different models can describe similar outcomes. Study the data-generating process, independence, sampling design, and alternative models before choosing.";
      link.hidden = true;
      link.removeAttribute("href");
      return;
    }
    title.textContent = model.name;
    reason.textContent = model.why;
    assumptions.textContent = model.assumptions;
    parameters.textContent = model.parameters;
    caveat.textContent = model.caution + " This guide is a candidate, not a validated model selection.";
    link.href = model.path;
    link.textContent = "Read the " + model.name + " lesson";
    link.hidden = false;
  }
  selector.addEventListener("change",render);
  selector.addEventListener("input",render);
  render();
})();
</script>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  try {
    const KEY = "esa_continue_probability_distributions_lesson_v0";
    const raw = localStorage.getItem(KEY);
    if (!raw) return;
    const data = JSON.parse(raw);
    // Match only exact, published lesson hrefs belonging to this block.
    // Prefix matches are insufficient: queries, fragments, traversal and other blocks are rejected.
    const published = new Set(
      Array.from(document.querySelectorAll("#lessons .lesson-card h3 a[href]"),
        link => link.getAttribute("href"))
        .filter(url => typeof url === "string" &&
          /^\/probability\/distributions\/[a-z0-9-]+\/$/.test(url))
    );
    if (!data || typeof data.url !== "string" || typeof data.label !== "string" ||
        !published.has(data.url)) return;
    // Require the exact published label, not an arbitrary stored string.
    const lesson = Array.from(document.querySelectorAll("#lessons .lesson-card h3 a[href]"))
      .find(link => link.getAttribute("href") === data.url);
    if (!lesson || data.label !== lesson.textContent.trim()) return;
    // Older progress without ts remains supported; malformed, stale-formatted,
    // and implausibly future timestamps must never resume.
    if (Object.prototype.hasOwnProperty.call(data, "ts") &&
        (!Number.isSafeInteger(data.ts) || data.ts <= 0 ||
         data.ts > Date.now() + 5 * 60 * 1000)) return;

    const wrap = document.getElementById("continue-reading-probability-distributions");
    const label = document.getElementById("continue-reading-probability-distributions-label");
    const btn = document.getElementById("continue-reading-probability-distributions-btn");
    if (!wrap || !label || !btn) return;
    const strong = document.createElement("strong");
    strong.textContent = data.label;
    label.replaceChildren("You last visited: ", strong);
    btn.href = data.url;
    wrap.style.display = "block";
  } catch (_) {
    // Malformed saved data and denied storage must never prevent navigation.
  }
})();
</script>
