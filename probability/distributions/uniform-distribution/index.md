---
layout: default
title: Uniform Distribution
description: Learn how the uniform distribution models situations where all outcomes within a range are equally likely.
permalink: /probability/distributions/uniform-distribution/
sidebar: false
translation_pair: uniform-distribution
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/uniform-distribution/",
    label: "Uniform Distribution",
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
      <span class="badge">Continuous</span>
    </div>

    <h1>Uniform Distribution</h1>
    <p><a href="/ar/probability/distributions/uniform-distribution/" lang="ar" dir="rtl">العربية — التوزيع المنتظم</a></p>

    <p class="lead">
      Many distributions assign different probabilities to different values.
    </p>

    <p class="lead">
      In a continuous uniform distribution, every equal-length interval within the range has equal probability. Individual values have probability zero.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/hypergeometric-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/exponential-distribution/">
         Next: Exponential Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Uniform Distribution?</h2>

    <p>
      A uniform distribution describes a random variable whose values are equally likely within a specified interval.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        In a continuous uniform distribution, the probability density is constant throughout a nondegenerate interval (a, b) with a &lt; b.
      </p>

    </div>

    <h2>A Simple Example</h2>

    <p>
      Suppose a random number is selected uniformly between 0 and 10.
    </p>

    <p>
      The density is equal everywhere in the interval, so equal-length subintervals have equal probabilities. Individual points still have probability zero.
    </p>

    <div class="example-box">

      <p>
        2.3 is just as likely as 7.8
      </p>

      <p>
        0.5 is just as likely as 9.2
      </p>

    </div>

    <p>
      No region is favored over another.
    </p>

    <h2>Continuous Uniform Distribution</h2>

    <p>
      The most common version is the continuous uniform distribution.
    </p>

    <p>
      It is defined on an interval:
    </p>

    
    \[
    a\le X\le b,\qquad a<b
    \]


    <p>
      where:
    </p>

    <ul class="bullets">

      <li>a = lower bound</li>

      <li>b = upper bound</li>

    </ul>

    <h2>Notation</h2>

    <p>
      A continuous uniform random variable is written as:
    </p>

    <div class="example-box">

      <p>
        X ~ Uniform(a,b)
      </p>

    </div>

    <p>
      The interval boundaries completely determine the distribution.
    </p>

    <h2>The Probability Density Function</h2>

    <p>
      The probability density is constant throughout the interval.
    </p>

    
    \[
    f_X(x)=\frac{1}{b-a}
    \]


    <p>
      for:
    </p>

    
    \[
    a\le x\le b
    \]


    <p>
      and zero elsewhere.
    </p>

    <h2>Why the Density Is Constant</h2>

    <p>
      Since the probability density is constant,
      its graph is a horizontal line over the interval.
    </p>

    <p>
      The total area under the curve must equal one.
    </p>

    <p>
      Therefore the height must be:
    </p>

    
    \[
    \text{density height}=\frac{1}{b-a}
    \]


    <h2>The Shape</h2>

    <p>
      The probability density graph forms a rectangle.
    </p>

    <div class="example-box">

      <p>
        Equal height everywhere
      </p>

      <p>
        No peaks
      </p>

      <p>
        No skewness
      </p>

    </div>

    <p>
      This simple shape explains the name "uniform."
    </p>

    <h2>Probabilities as Areas</h2>

    <p>
      For continuous distributions,
      probabilities correspond to areas under the density curve.
    </p>

    <p>
      Therefore:
    </p>

    
    \[
    P(c\le X\le d)=\frac{d-c}{b-a},\quad a\le c\le d\le b
    \]


    <p>
      whenever c and d lie inside the interval.
    </p>

    <h2>Example: Probability in a Subinterval</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        X ~ Uniform(0,10)
      </p>

    </div>

    <p>
      What is:
    </p>

    <div class="example-box">

      <p>
        P(2 ≤ X ≤ 5)
      </p>

    </div>

    <p>
      Using the interval-length rule:
    </p>

    
    \[
    P(2\le X\le5)=\frac{5-2}{10-0}=0.30
    \]


    <p>
      The probability equals 0.3.
    </p>


    <!-- UNIFORM PROBABILITY AREA EXPLORER -->
    <div class="concept-box esa-uniform-lab" id="esa-uniform-area-explorer"
         role="group" aria-labelledby="esa-uniform-lab-heading">
      <h2 id="esa-uniform-lab-heading">Interactive Uniform Probability Area Explorer</h2>
      <p>Adjust the interval limits a and b, then select a subinterval from c to d.
         The shaded rectangle shows probability as an <strong>area</strong>:
         its width is d − c and its height is the density 1/(b − a).
         A density value by itself is not a probability.</p>
      <div class="esa-uniform-fields">
        <div>
          <label for="esa-uniform-a"><strong>Lower distribution bound a:
            <output for="esa-uniform-a" id="esa-uniform-a-value">0</output></strong></label>
          <input id="esa-uniform-a" type="range" min="0" max="9" step="1" value="0">
        </div>
        <div>
          <label for="esa-uniform-b"><strong>Upper distribution bound b:
            <output for="esa-uniform-b" id="esa-uniform-b-value">10</output></strong></label>
          <input id="esa-uniform-b" type="range" min="1" max="20" step="1" value="10">
        </div>
        <div>
          <label for="esa-uniform-c"><strong>Subinterval start c:
            <output for="esa-uniform-c" id="esa-uniform-c-value">2</output></strong></label>
          <input id="esa-uniform-c" type="range" min="0" max="10" step="0.5" value="2">
        </div>
        <div>
          <label for="esa-uniform-d"><strong>Subinterval end d:
            <output for="esa-uniform-d" id="esa-uniform-d-value">5</output></strong></label>
          <input id="esa-uniform-d" type="range" min="2" max="10" step="0.5" value="5">
        </div>
      </div>
      <svg id="esa-uniform-area-plot" viewBox="0 0 360 180" width="360" height="180"
           role="img" aria-label="Uniform density from 0 to 10; shaded probability between 2 and 5 equals 0.30">
        <line x1="36" y1="140" x2="341" y2="140" stroke="currentColor" stroke-width="1.5"/>
        <line x1="36" y1="140" x2="36" y2="24" stroke="currentColor" stroke-width="1.5"/>
        <rect x="50" y="40" width="280" height="100" fill="#94a3b8" fill-opacity=".17"
              stroke="#64748b" stroke-width="1.6"/>
        <rect id="esa-uniform-highlight" x="106" y="40" width="84" height="100"
              fill="#0d9488" fill-opacity=".65"/>
        <text id="esa-uniform-left-label" x="50" y="157" font-size="11" fill="currentColor" text-anchor="middle">0</text>
        <text id="esa-uniform-right-label" x="330" y="157" font-size="11" fill="currentColor" text-anchor="middle">10</text>
        <text x="37" y="18" font-size="11" fill="currentColor">Density</text>
        <text x="340" y="157" font-size="11" fill="currentColor">X</text>
      </svg>
      <div class="esa-uniform-results" role="status" aria-live="polite" aria-atomic="true">
        <p>Selected interval: <strong id="esa-uniform-interval">[2, 5]</strong>.
           Width: <output id="esa-uniform-width">3.00</output>.</p>
        <p>Constant density: <strong><output id="esa-uniform-density">0.1000</output></strong>.
           Shaded area / probability: <strong><output id="esa-uniform-probability">0.3000</output></strong>.</p>
        <p>Mean E[X] = <output id="esa-uniform-mean">5.00</output>.
           Variance Var(X) = <output id="esa-uniform-variance">8.3333</output>.
           Standard deviation = <output id="esa-uniform-sd">2.8868</output>.</p>
        <p><strong>Point probability:</strong> P(X = c) = 0 for every individual point,
           including both endpoints. Endpoints do not change an interval probability.</p>
      </div>
      <button type="button" class="btn btn-outline" id="esa-uniform-reset">Reset uniform example</button>
      <p class="muted-mini">Valid inputs satisfy 0 ≤ a &lt; b ≤ 20 and a ≤ c ≤ d ≤ b.
        The graph rescales the x-axis to the selected distribution interval.
        All calculations describe a continuous uniform variable.</p>
    </div>
    <style>
      #esa-uniform-area-explorer {box-sizing:border-box;width:100%;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-uniform-area-explorer .esa-uniform-fields {
        display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));
        gap:12px;margin:14px 0
      }
      #esa-uniform-area-explorer .esa-uniform-fields>div {min-width:0}
      #esa-uniform-area-explorer label {display:block;margin-bottom:8px}
      #esa-uniform-area-explorer input[type="range"] {
        display:block;box-sizing:border-box;width:100%;max-width:100%;
        min-width:0;margin:0;padding:0
      }
      #esa-uniform-area-explorer svg {
        display:block;width:100%;max-width:520px;height:auto;margin:12px auto;
        overflow:visible
      }
      #esa-uniform-area-explorer .esa-uniform-results p {margin:10px 0}
    </style>
    <script src="{{ '/js/uniform-area-explorer.js' | relative_url }}" defer></script>


    <h2>Single Values Have Zero Probability</h2>

    <p>
      Continuous random variables behave differently from discrete variables.
    </p>

    <p>
      For any specific value:
    </p>

    
    \[
    P(X=x)=0\quad\text{for any fixed real }x
    \]


    <p>
      because individual points have zero area.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Continuous distributions assign probability to intervals, not individual values.
      </p>

    </div>

    <h2>The Mean</h2>

    <p>
      The expected value is:
    </p>

    
    \[
    E[X]=\frac{a+b}{2}
    \]


    <p>
      This is simply the midpoint of the interval.
    </p>

    <h2>Example of the Mean</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        X ~ Uniform(0,10)
      </p>

    </div>

    <p>
      Then:
    </p>

    
    \[
    E[X]=\frac{0+10}{2}=5
    \]


    <p>
      The center lies exactly in the middle.
    </p>

    <h2>The Variance</h2>

    <p>
      The variance of a continuous uniform distribution is:
    </p>

    
    \[
    \operatorname{Var}(X)=\frac{(b-a)^2}{12}
    \]


    <p>
      The spread depends only on the interval width.
    </p>

    <h2>Standard Deviation</h2>

    <p>
      Taking the square root gives:
    </p>

    
    \[
    \operatorname{SD}(X)=\sqrt{\operatorname{Var}(X)}=\frac{b-a}{\sqrt{12}}
    \]


    <p>
      Wider intervals produce larger variability.
    </p>

    <h2>Common Applications</h2>

    <ul class="bullets">

      <li>Random number generation</li>

      <li>Simulation studies</li>

      <li>Randomized experiments</li>

      <li>Computer games</li>

      <li>Modeling equally likely arrival times</li>

    </ul>

    <p>
      Uniform distributions are fundamental in simulation and computational statistics.
    </p>

    <h2>Uniform Distribution in Simulation</h2>

    <p>
      Most random-number generators begin by producing values from a uniform distribution.
    </p>

    <p>
      Other probability distributions are often generated from uniform random numbers.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The uniform distribution serves as the foundation of modern simulation methods.
      </p>

    </div>

    <h2>Discrete Versus Continuous Uniform</h2>

    <p>
      There is also a discrete uniform distribution.
    </p>

    <div class="example-box">

      <p>
        Rolling a fair die
      </p>

      <p>
        Drawing a random day of the week
      </p>

    </div>

    <p>
      In this lesson,
      we focus on the continuous version,
      which is more important for continuous probability models.
    </p>

    <h2>Why the Uniform Distribution Matters</h2>

    <p>
      The uniform distribution is the simplest continuous distribution.
    </p>

    <p>
      It introduces key ideas such as:
    </p>

    <ul class="bullets">

      <li>Probability density functions</li>

      <li>Area-based probabilities</li>

      <li>Continuous random variables</li>

      <li>Interval probabilities</li>

    </ul>

    <p>
      These ideas form the basis for many advanced continuous distributions.
    </p>

    <h2>The Limitation</h2>

    <p>
      Uniform distributions assume all values are equally likely.
    </p>

    <p>
      Many real-world waiting-time problems do not behave this way.
    </p>

    <div class="example-box">

      <p>
        Time until the next customer arrives
      </p>

      <p>
        Time until a machine fails
      </p>

      <p>
        Time until a phone call occurs
      </p>

    </div>

    <p>
      These waiting-time problems are often modeled by the exponential distribution.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The exponential distribution is one of the most important continuous probability distributions.
    </p>

    <p>
      It models waiting times between random events and possesses a remarkable memoryless property.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The uniform distribution assigns equal probability density throughout an interval</li>

        <li>Its density is constant and equal to 1/(b − a)</li>

        <li>Probabilities are determined by interval lengths</li>

        <li>Single points have probability zero</li>

        <li>The mean equals (a + b)/2</li>

        <li>The variance equals (b − a)²/12</li>

        <li>The uniform distribution is fundamental to simulation and continuous probability theory</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/hypergeometric-distribution/">
         ← Previous: Hypergeometric Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/exponential-distribution/">
         Next: Exponential Distribution →
      </a>

    </div>

  </div>

</section>