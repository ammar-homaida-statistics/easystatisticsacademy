---
layout: default
title: Negative Binomial Distribution
description: Learn how the negative binomial distribution models the number of trials required to achieve a specified number of successes.
permalink: /probability/distributions/negative-binomial-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/negative-binomial-distribution/",
    label: "Negative Binomial Distribution",
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

    <h1>Negative Binomial Distribution</h1>

    <p class="lead">
      The geometric distribution models the waiting time until the first success.
    </p>

    <p class="lead">
      The negative binomial distribution generalizes this idea by modeling the waiting time until a specified number of successes occurs.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/geometric-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/poisson-distribution/">
         Next: Poisson Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Negative Binomial Distribution?</h2>

    <p>
      A negative binomial distribution describes the number of trials required to obtain a fixed number of successes in independent Bernoulli trials.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Here X is the total number of trials up to and including the r-th success, with positive integer r and constant success probability 0 &lt; p &le; 1. The failures-before-success convention is a different parameterization.
      </p>

    </div>

    <h2>The Main Question</h2>

    <p>
      Instead of asking:
    </p>

    <div class="example-box">

      <p>
        How long until the first success?
      </p>

    </div>

    <p>
      we ask:
    </p>

    <div class="example-box">

      <p>
        How long until the fifth success?
      </p>

      <p>
        How many customers until the third purchase?
      </p>

      <p>
        How many inspections until the tenth defect?
      </p>

    </div>

    <p>
      These are negative binomial questions.
    </p>

    <h2>Conditions for a Negative Binomial Model</h2>

    <p>
      A negative binomial distribution applies when:
    </p>

    <ul class="bullets">

      <li>Trials are independent.</li>

      <li>Each trial has two outcomes.</li>

      <li>The success probability remains constant.</li>

      <li>We continue until r successes occur.</li>

    </ul>

    <h2>Notation</h2>

    <p>
      A negative binomial random variable is commonly written as:
    </p>

    
    \[
    X\sim\operatorname{NegBin}(r,p),\quad r=1,2,\ldots,\ 0<p\le1
    \]


    <p>
      where:
    </p>

    <ul class="bullets">

      <li>r = required number of successes</li>

      <li>p = probability of success</li>

    </ul>

    <h2>Possible Values</h2>

    <p>
      At least r trials are needed to obtain r successes.
    </p>

    <p>
      Therefore:
    </p>

    
    \[
    X\in\{r,r+1,r+2,\ldots\}
    \]


    <p>
      are the possible values of X.
    </p>

    <h2>The Probability Formula</h2>

    <p>
      The probability that the r-th success occurs on trial k is:
    </p>

    
    \[
    P(X=k)=\binom{k-1}{r-1}p^r(1-p)^{k-r},\quad k=r,r+1,\ldots
    \]


    <p>
      where:
    </p>

    <ul class="bullets">

      <li>k ≥ r</li>

      <li>The final trial must be a success.</li>

      <li>The previous k−1 trials contain exactly r−1 successes.</li>

    </ul>

    <h2>Understanding the Formula</h2>

    <p>
      To have the r-th success occur on trial k:
    </p>

    <div class="example-box">

      <p>
        Trial k must be a success.
      </p>

      <p>
        The first k−1 trials must contain exactly r−1 successes.
      </p>

    </div>

    <p>
      The combination term counts all possible arrangements of those earlier successes.
    </p>

    <h2>Relationship to the Geometric Distribution</h2>

    <p>
      The geometric distribution is actually a special case of the negative binomial distribution.
    </p>

    <p>
      When:
    </p>

    
    \[
    r=1\quad\Longrightarrow\quad P(X=k)=(1-p)^{k-1}p
    \]


    <p>
      the negative binomial formula reduces to the geometric distribution.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        The geometric distribution is the negative binomial distribution with one required success.
      </p>

    </div>

    <h2>Example: Waiting for Three Heads</h2>

    <p>
      Suppose a fair coin is tossed repeatedly.
    </p>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = Trial on which the third head appears
      </p>

    </div>

    <p>
      Then:
    </p>

    <div class="example-box">

      <p>
        r = 3
      </p>

      <p>
        p = 0.5
      </p>

    </div>

    <p>
      X follows a negative binomial distribution.
    </p>

    <p>
      It models the waiting time until three heads have occurred.
    </p>

    <h2>The Mean</h2>

    <p>
      The expected value is:
    </p>

    
    \[
    E[X]=\frac rp
    \]


    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        The average number of trials required grows with the number of required successes and decreases as success becomes more likely.
      </p>

    </div>

    <h2>Example of the Mean</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        r = 5
      </p>

      <p>
        p = 0.25
      </p>

    </div>

    <p>
      Then:
    </p>

    
    \[
    E[X]=\frac{5}{0.25}=20
    \]


    <p>
      On average,
      twenty trials are needed to obtain five successes.
    </p>

    <h2>The Variance</h2>

    <p>
      The variance is:
    </p>

    
    \[
    \operatorname{Var}(X)=\frac{r(1-p)}{p^2}
    \]


    <p>
      Variability increases when successes become rarer.
    </p>


    <!-- INTERACTIVE NEGATIVE BINOMIAL WAITING-TIME EXPLORER -->
    <div class="concept-box esa-negbin-lab" id="esa-negbin-wait-explorer"
         role="group" aria-labelledby="esa-negbin-lab-heading">
      <h2 id="esa-negbin-lab-heading">Interactive Negative Binomial Waiting-Time Explorer</h2>
      <p>Model independent Bernoulli trials with constant success probability
         <strong>0 &lt; p &le; 1</strong>. Here X counts <strong>all trials,
         including the final successful trial</strong>, until the r-th success:
         k &ge; r. This differs from the failures-before-r-successes convention.</p>
      <div class="esa-negbin-fields">
        <div>
          <label for="esa-negbin-r">Required successes r:
            <output for="esa-negbin-r" id="esa-negbin-r-value">3</output></label>
          <input type="range" min="1" max="6" step="1" value="3" id="esa-negbin-r"/>
        </div>
        <div>
          <label for="esa-negbin-p">Success probability p:
            <output for="esa-negbin-p" id="esa-negbin-p-value">0.50</output></label>
          <input type="range" min="0.05" max="1" step="0.05" value="0.5" id="esa-negbin-p"/>
        </div>
        <div>
          <label for="esa-negbin-k">Trial of r-th success k:
            <output for="esa-negbin-k" id="esa-negbin-k-value">5</output></label>
          <input type="range" min="3" max="30" step="1" value="5" id="esa-negbin-k"/>
        </div>
      </div>
      <h3>Possible completion trials (from r through r + 11)</h3>
      <svg id="esa-negbin-chart" viewBox="0 0 360 176" role="img"
           aria-label="Probability of third success on successive trials; success chance 0.50; selected trial 5"
           width="360" height="176">
        <line x1="30" y1="135" x2="347" y2="135" stroke="currentColor" stroke-width="1.4"/>
        <line x1="30" y1="135" x2="30" y2="16" stroke="currentColor" stroke-width="1.4"/>
        <text x="8" y="15" fill="currentColor" font-size="10">PMF</text>
        <g id="esa-negbin-bars"></g>
        <text x="344" y="159" fill="currentColor" font-size="10">k</text>
      </svg>
      <p class="muted-mini">Bars display only 12 possible completion trials.
         Probabilities after the displayed trials remain included in the
         CDF and tail calculations; bar heights use an absolute 0–1 scale.</p>
      <div class="esa-negbin-results" role="status" aria-live="polite" aria-atomic="true">
        <p><strong>Exact:</strong> P(X = k) =
          <output id="esa-negbin-pmf">0.187500</output>.</p>
        <p><strong>By trial k:</strong> P(X &le; k) =
          <output id="esa-negbin-cdf">0.500000</output>.</p>
        <p><strong>After trial k:</strong> P(X &gt; k) =
          <output id="esa-negbin-tail">0.500000</output>.</p>
        <p><strong>Mean:</strong> E[X] = r/p =
          <output id="esa-negbin-mean">6.0000</output> trials.
          <strong>Variance:</strong> r(1 − p)/p² =
          <output id="esa-negbin-variance">6.0000</output> trials².</p>
        <p id="esa-negbin-special">When r = 1, this is exactly the
          geometric trials-to-first-success distribution.</p>
      </div>
      <div class="esa-negbin-presets">
        <button type="button" class="btn btn-outline" id="esa-negbin-reset">Reset example</button>
        <button type="button" class="btn btn-outline" id="esa-negbin-geometric">Geometric: r = 1</button>
      </div>
      <p class="muted-mini">The general PMF is
         P(X = k) = C(k − 1, r − 1) p<sup>r</sup>(1 − p)<sup>k − r</sup>.
         Cumulative probability is summed over k = r, ..., selected k.
         At p = 1 all probability is concentrated at k = r.</p>
    </div>
    <style>
      #esa-negbin-wait-explorer {box-sizing:border-box;width:100%;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-negbin-wait-explorer .esa-negbin-fields {
        display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,185px),1fr));
        gap:14px;margin:16px 0
      }
      #esa-negbin-wait-explorer .esa-negbin-fields>div {min-width:0}
      #esa-negbin-wait-explorer label {display:block;margin-bottom:8px}
      #esa-negbin-wait-explorer input[type="range"] {
        display:block;box-sizing:border-box;width:100%;max-width:100%;
        min-width:0;margin:0;padding:0
      }
      #esa-negbin-wait-explorer h3 {font-size:1.05em;margin:16px 0 10px}
      #esa-negbin-wait-explorer svg {display:block;width:100%;height:auto;max-width:520px;margin:0 auto;overflow:visible}
      #esa-negbin-wait-explorer .esa-negbin-results p {margin:11px 0}
      #esa-negbin-wait-explorer .esa-negbin-presets {display:flex;flex-wrap:wrap;gap:8px}
    </style>
    <script>
    (function () {
      "use strict";
      const root=document.getElementById("esa-negbin-wait-explorer");
      if (!root) return;
      const byId=id=>root.querySelector("#"+id);
      const rInput=byId("esa-negbin-r"),pInput=byId("esa-negbin-p"),
            kInput=byId("esa-negbin-k");
      const CHART_BASE=135;
      function choose(n,k) {
        if (k<0 || k>n) return 0;
        const count=Math.min(k,n-k);
        let result=1;
        for(let i=1;i<=count;i++)result*= (n-count+i)/i;
        return result;
      }
      function mass(k,r,p) {
        if(k<r) return 0;
        return choose(k-1,r-1)*Math.pow(p,r)*Math.pow(1-p,k-r);
      }
      function update() {
        const r=Number(rInput.value),p=Number(pInput.value);
        // Set current feasibility constraints before obtaining/assigning k:
        // native range inputs otherwise clamp against obsolete bounds.
        kInput.min=String(r);
        const k=Math.max(r,Math.min(30,Number(kInput.value)));
        kInput.value=String(k);
        let cdf=0;
        for(let j=r;j<=k;j++)cdf+=mass(j,r,p);
        cdf=Math.max(0,Math.min(1,cdf));
        const tail=Math.max(0,1-cdf);
        const pmf=mass(k,r,p);
        byId("esa-negbin-r-value").textContent=String(r);
        byId("esa-negbin-p-value").textContent=p.toFixed(2);
        byId("esa-negbin-k-value").textContent=String(k);
        byId("esa-negbin-pmf").textContent=pmf.toFixed(6);
        byId("esa-negbin-cdf").textContent=cdf.toFixed(6);
        byId("esa-negbin-tail").textContent=tail.toFixed(6);
        byId("esa-negbin-mean").textContent=(r/p).toFixed(4);
        byId("esa-negbin-variance").textContent=(r*(1-p)/(p*p)).toFixed(4);
        byId("esa-negbin-special").textContent=r===1?
          "With r = 1, this is exactly the geometric trials-to-first-success distribution.":
          "For r > 1, the completion trial includes all r successful trials; set r = 1 to recover the geometric distribution.";
        const chart=byId("esa-negbin-bars");
        const svgNS="http://www.w3.org/2000/svg";
        const newElements=[];
        for(let j=r;j<r+12;j++){
          const x=40+(j-r)*24;
          const height=110*mass(j,r,p);
          const bar=document.createElementNS(svgNS,"rect");
          bar.setAttribute("x",String(x));bar.setAttribute("width","17");
          bar.setAttribute("y",String(CHART_BASE-height));
          bar.setAttribute("height",String(height));
          bar.setAttribute("fill",j===k?"#0d9488":"#64748b");
          bar.setAttribute("data-trial",String(j));
          newElements.push(bar);
          if(j===r||j===r+5||j===r+11){
            const label=document.createElementNS(svgNS,"text");
            label.setAttribute("x",String(x+8.5));label.setAttribute("y","152");
            label.setAttribute("fill","currentColor");
            label.setAttribute("font-size","10");
            label.setAttribute("text-anchor","middle");
            label.textContent=String(j);newElements.push(label);
          }
        }
        chart.replaceChildren(...newElements);
        byId("esa-negbin-chart").setAttribute("aria-label",
          "Negative binomial completion-trial PMF for r = "+r+
          " successes with p = "+p.toFixed(2)+
          ". Selected trial k = "+k+", P(X = k) = "+pmf.toFixed(6)+
          ". Twelve displayed bars, with all trials included in cumulative results.");
      }
      [rInput,pInput,kInput].forEach(input=>input.addEventListener("input",update));
      function preset(r,p,k) {
        rInput.value=String(r);pInput.value=String(p);
        kInput.min=String(r);kInput.value=String(k);
        update();
      }
      byId("esa-negbin-reset").addEventListener("click",()=>preset(3,0.5,5));
      byId("esa-negbin-geometric").addEventListener("click",()=>preset(1,0.5,3));
      update();
    })();
    </script>

    <h2>Comparing Geometric and Negative Binomial</h2>

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
            <td>Geometric</td>
            <td>Waiting time for first success</td>
          </tr>

          <tr>
            <td>Negative Binomial</td>
            <td>Waiting time for r successes</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Why It Is Called "Negative Binomial"</h2>

    <p>
      The name originates from an algebraic expansion involving negative exponents.
    </p>

    <p>
      Historically,
      this distribution emerged from the negative binomial series in mathematics.
    </p>

    <p>
      The term does not imply negative probabilities or negative counts.
    </p>

    <h2>Applications in Practice</h2>

    <ul class="bullets">

      <li>Calls required before multiple sales occur</li>

      <li>Patients screened before several positive cases are found</li>

      <li>Network transmissions until several successful packets are received</li>

      <li>Production inspections until multiple defects are observed</li>

      <li>Sports attempts required before multiple successful outcomes</li>

    </ul>

    <p>
      The distribution is useful whenever repeated successes are the focus.
    </p>

    <h2>Connection to Counting Processes</h2>

    <p>
      Binomial distributions count successes within a fixed number of trials.
    </p>

    <p>
      Negative binomial distributions reverse the perspective.
    </p>

    <div class="example-box">

      <p>
        Binomial:
        Fixed trials → Count successes
      </p>

      <p>
        Negative Binomial:
        Fixed successes → Count trials
      </p>

    </div>

    <p>
      These distributions are closely related but answer different questions.
    </p>

    <h2>The Shape of the Distribution</h2>

    <p>
      Negative binomial distributions are generally right-skewed.
    </p>

    <p>
      Most waiting times are relatively short,
      but occasionally much longer waiting times occur.
    </p>

    <p>
      The skewness becomes more pronounced when success probabilities are small.
    </p>

    <h2>The Limitation</h2>

    <p>
      Bernoulli,
      binomial,
      geometric,
      and negative binomial distributions all arise from repeated success-or-failure trials.
    </p>

    <p>
      Many real-world events do not naturally fit that framework.
    </p>

    <div class="example-box">

      <p>
        Number of emails received today
      </p>

      <p>
        Number of accidents this week
      </p>

      <p>
        Number of website visits this hour
      </p>

    </div>

    <p>
      These counts are often modeled using the Poisson distribution.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The Poisson distribution is one of the most important distributions in statistics.
    </p>

    <p>
      It models counts of events occurring over time, space, or other continuous domains and is widely used in science, engineering, business, and data analytics.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The negative binomial distribution models waiting time until r successes occur</li>

        <li>It generalizes the geometric distribution</li>

        <li>The geometric distribution is the special case r = 1</li>

        <li>The mean equals r/p</li>

        <li>The variance equals r(1 − p)/p²</li>

        <li>It arises from repeated independent Bernoulli trials</li>

        <li>It is useful for multi-success waiting-time problems</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/geometric-distribution/">
         ← Previous: Geometric Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/poisson-distribution/">
         Next: Poisson Distribution →
      </a>

    </div>

  </div>

</section>