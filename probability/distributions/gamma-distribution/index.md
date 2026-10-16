---
layout: default
title: Gamma Distribution
description: Learn how the gamma distribution generalizes the exponential distribution and models waiting times until multiple events occur.
permalink: /probability/distributions/gamma-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/gamma-distribution/",
    label: "Gamma Distribution",
    ts: Date.now()
    }));
  } catch (_) {
    // Storage may be disabled; the page still works without saved progress.
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

    <h1>Gamma Distribution</h1>

    <p class="lead">
      The exponential distribution models waiting for a single event.
    </p>

    <p class="lead">
      The gamma distribution extends this idea and models waiting times until multiple events occur.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/exponential-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/beta-distribution/">
         Next: Beta Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Gamma Distribution?</h2>

    <p>
      A gamma distribution with a positive integer shape models the waiting time until that many events occur in a homogeneous Poisson process. More generally, gamma shapes can be any positive real number.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        For integer shape, a gamma random variable gives the waiting time until the corresponding event in a Poisson process. For arbitrary positive shape, it is a continuous positive distribution without requiring an integer event count.
      </p>

    </div>

    <h2>The Main Idea</h2>

    <p>
      Suppose events occur randomly over time.
    </p>

    <div class="example-box">

      <p>
        Time until the first customer arrives
      </p>

      <p>
        Time until the fifth customer arrives
      </p>

      <p>
        Time until the tenth phone call
      </p>

      <p>
        Time until the third machine failure
      </p>

    </div>

    <p>
      The exponential distribution handles the first event.
    </p>

    <p>
      The gamma distribution handles multiple events.
    </p>

    <h2>Connection to the Exponential Distribution</h2>

    <p>
      If waiting times between events are exponential,
      then the sum of several such waiting times follows a gamma distribution.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        For positive integer shape r, a gamma distribution with rate λ is the sum of r independent Exponential(λ) waiting times (the Erlang case).
      </p>

    </div>

    <h2>The Parameters</h2>

    <p>
      A gamma distribution is commonly defined using:
    </p>

    <ul class="bullets">

      <li>α (shape parameter)</li>

      <li>λ (rate parameter)</li>

    </ul>

    <p>
      When α is a positive integer, the shape is the number of events waited for in a Poisson process. The general Gamma model also permits noninteger α.
    </p>

    <p>
      The rate parameter controls how frequently events occur.
    </p>

    <h2>Notation</h2>

    <p>
      A gamma random variable is often written as:
    </p>

    <div class="example-box">

      <p>
        X ~ Gamma(α, λ)
      </p>

    </div>

    <h2>The Probability Density Function</h2>

    <p>
      The gamma density function is:
    </p>

    
    \[
    f_X(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x}
    \]


    <p>
      for:
    </p>

    
    \[
    x>0,\qquad\alpha>0,\ \lambda>0\quad(\lambda\text{ is the rate})
    \]


    <p>
      where Γ(α) is the gamma function.
    </p>

    <h2>The Gamma Function</h2>

    <p>
      The gamma function extends the factorial function to non-integer values.
    </p>

    <p>
      For positive integers:
    </p>

    
    \[
    \Gamma(n)=(n-1)!\quad\text{for positive integers }n
    \]


    <p>
      This connection explains the name of the distribution.
    </p>

    <h2>A Special Case</h2>

    <p>
      When:
    </p>

    
    \[
    \alpha=1
    \]


    <p>
      the gamma distribution becomes:
    </p>

    
    \[
    f_X(x)=\lambda e^{-\lambda x},\quad x\ge0
    \]


    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        The exponential distribution is a special case of the gamma distribution.
      </p>

    </div>

    <h2>Interpreting the Shape Parameter</h2>

    <p>
      For positive integer α, the shape determines the number of Poisson-process events being waited for. For noninteger α, the event-count interpretation does not apply.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Shape α</th>
            <th>Interpretation</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>1</td>
            <td>Wait for first event</td>
          </tr>

          <tr>
            <td>2</td>
            <td>Wait for second event</td>
          </tr>

          <tr>
            <td>5</td>
            <td>Wait for fifth event</td>
          </tr>

          <tr>
            <td>10</td>
            <td>Wait for tenth event</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Mean</h2>

    <p>
      The expected value is:
    </p>

    
    \[
    E[X]=\frac{\alpha}{\lambda}
    \]


    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        Expected waiting time increases with the number of required events and decreases as the event rate increases.
      </p>

    </div>

    <h2>Example of the Mean</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        α = 4
      </p>

      <p>
        λ = 2
      </p>

    </div>

    <p>
      Then:
    </p>

    
    \[
    E[X]=\frac{4}{2}=2\ \text{time units}
    \]


    <p>
      The average waiting time equals 2 time units.
    </p>

    <h2>The Variance</h2>

    <p>
      The variance is:
    </p>

    
    \[
    \operatorname{Var}(X)=\frac{\alpha}{\lambda^2}
    \]


    <p>
      Greater shape values increase variability,
      while larger rates decrease it.
    </p>

    <h2>The Shape of the Distribution</h2>

    <p>
      The gamma distribution can take many forms.
    </p>

    <div class="example-box">

      <p>
        Small α → highly right-skewed
      </p>

      <p>
        Moderate α → smoother peak
      </p>

      <p>
        Large α → increasingly bell-shaped
      </p>

    </div>

    <p>
      This flexibility makes the gamma distribution extremely useful.
    </p>


    <!-- INTERACTIVE GAMMA ERLANG WAITING TIME EXPLORER -->
    <div class="concept-box esa-erlang-lab" id="esa-erlang-wait-explorer"
         role="group" aria-labelledby="esa-erlang-lab-heading">
      <h2 id="esa-erlang-lab-heading">Interactive Gamma/Erlang Waiting-Time Explorer</h2>
      <p>In a homogeneous Poisson process, the time until the
         <strong>r-th event</strong> follows a Gamma distribution with
         <strong>integer shape r</strong> and <strong>rate λ</strong>.
         This integer-shape case is called the Erlang distribution. General
         Gamma distributions can have noninteger positive shape, but only
         integer shapes have the direct r-th-event interpretation used here.</p>
      <div class="esa-erlang-fields">
        <div>
          <label for="esa-erlang-r">Event count / shape r:
            <output id="esa-erlang-r-value" for="esa-erlang-r">4</output></label>
          <input type="range" min="1" max="7" step="1" value="4" id="esa-erlang-r"/>
        </div>
        <div>
          <label for="esa-erlang-rate">Event rate λ:
            <output id="esa-erlang-rate-value" for="esa-erlang-rate">2.00</output></label>
          <input type="range" min="0.5" max="4" step="0.5" value="2" id="esa-erlang-rate"/>
        </div>
        <div>
          <label for="esa-erlang-time">Elapsed time t:
            <output id="esa-erlang-time-value" for="esa-erlang-time">2.00</output></label>
          <input type="range" min="0" max="12" step="0.25" value="2" id="esa-erlang-time"/>
        </div>
      </div>
      <h3>Erlang density and shaded probability P(T ≤ t)</h3>
      <svg id="esa-erlang-chart" viewBox="0 0 360 174" width="360" height="174"
           role="img" aria-label="Gamma Erlang density with shape 4, rate 2, shaded area from time 0 to 2">
        <line x1="34" y1="137" x2="339" y2="137" stroke="currentColor" stroke-width="1.4"/>
        <line x1="34" y1="137" x2="34" y2="15" stroke="currentColor" stroke-width="1.4"/>
        <path id="esa-erlang-shade" fill="#0d9488" fill-opacity=".45" d="M34 137 L34 137 Z"/>
        <path id="esa-erlang-density-path" fill="none" stroke="#64748b" stroke-width="2" d="M34 137"/>
        <line id="esa-erlang-time-marker" x1="83.3" y1="16" x2="83.3" y2="137"
              stroke="#0d9488" stroke-dasharray="4 3" stroke-width="1.2"/>
        <text x="34" y="153" font-size="10" fill="currentColor" text-anchor="middle">0</text>
        <text x="331" y="153" font-size="10" fill="currentColor" text-anchor="middle">12</text>
        <text x="337" y="164" font-size="10" fill="currentColor">t</text>
        <text x="8" y="14" font-size="10" fill="currentColor">PDF</text>
      </svg>
      <div class="esa-erlang-results" role="status" aria-live="polite" aria-atomic="true">
        <p><strong>Density at t:</strong> f(t) = <output id="esa-erlang-pdf">0.39073</output>
           per time unit. Density is not a probability.</p>
        <p><strong>By time t:</strong> P(T ≤ t) =
          <output id="esa-erlang-cdf">0.566530</output>.</p>
        <p><strong>Later than t:</strong> P(T &gt; t) =
          <output id="esa-erlang-survival">0.433470</output>.</p>
        <p><strong>Mean:</strong> E[T] = r/λ =
          <output id="esa-erlang-mean">2.0000</output> time units.
          <strong>Variance:</strong> r/λ² =
          <output id="esa-erlang-variance">1.0000</output> time units².</p>
        <p><strong>Scale:</strong> θ = 1/λ =
          <output id="esa-erlang-scale">0.5000</output> time units.</p>
        <p id="esa-erlang-special">When r = 1, the Gamma/Erlang model becomes
          the Exponential distribution with rate λ.</p>
      </div>
      <div class="esa-erlang-presets">
        <button type="button" class="btn btn-outline" id="esa-erlang-reset">Reset Erlang example</button>
        <button type="button" class="btn btn-outline" id="esa-erlang-exponential">Exponential: shape 1</button>
      </div>
      <p class="muted-mini">For positive integer r, the exact survival
         probability is e<sup>−λt</sup> multiplied by
         Σ<sub>j=0</sub><sup>r−1</sup>(λt)<sup>j</sup>/j!.
         Thus P(T ≤ t) = 1 − P(T &gt; t) with no numerical integration.
         The density chart's vertical scale adapts to the parameters.
         The continuous distribution has P(T = t) = 0.</p>
    </div>
    <style>
      #esa-erlang-wait-explorer {box-sizing:border-box;width:100%;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-erlang-wait-explorer .esa-erlang-fields {
        display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,185px),1fr));
        gap:14px;margin:16px 0
      }
      #esa-erlang-wait-explorer .esa-erlang-fields>div {min-width:0}
      #esa-erlang-wait-explorer label {display:block;margin-bottom:8px}
      #esa-erlang-wait-explorer input[type="range"] {
        display:block;box-sizing:border-box;width:100%;max-width:100%;
        min-width:0;margin:0;padding:0
      }
      #esa-erlang-wait-explorer h3 {font-size:1.05em;margin:15px 0 10px}
      #esa-erlang-wait-explorer svg {display:block;width:100%;height:auto;max-width:520px;margin:0 auto;overflow:visible}
      #esa-erlang-wait-explorer .esa-erlang-results p {margin:11px 0}
      #esa-erlang-wait-explorer .esa-erlang-presets {display:flex;flex-wrap:wrap;gap:8px}
    </style>
    <script>
    (function () {
      "use strict";
      const root=document.getElementById("esa-erlang-wait-explorer");
      if (!root) return;
      const byId=id=>root.querySelector("#"+id);
      const rInput=byId("esa-erlang-r"),rateInput=byId("esa-erlang-rate"),
            timeInput=byId("esa-erlang-time");
      const maxTime=12, xToPx=t=>34+296*t/maxTime;
      function factorial(n){
        let result=1;
        for(let j=2;j<=n;j++)result*=j;
        return result;
      }
      function density(t,r,lambda) {
        if(t<0) return 0;
        if(t===0) return r===1?lambda:0;
        return Math.pow(lambda,r)*Math.pow(t,r-1)*
          Math.exp(-lambda*t)/factorial(r-1);
      }
      function survival(t,r,lambda) {
        if(t<=0)return 1;
        const z=lambda*t;
        let term=1,sum=1;
        for(let j=1;j<r;j++){
          term*=z/j;
          sum+=term;
        }
        return Math.min(1,Math.max(0,Math.exp(-z)*sum));
      }
      function update() {
        const r=Number(rInput.value),lambda=Number(rateInput.value),
              t=Number(timeInput.value);
        const s=survival(t,r,lambda),c=Math.max(0,Math.min(1,1-s)),
              pdf=density(t,r,lambda);
        byId("esa-erlang-r-value").textContent=String(r);
        byId("esa-erlang-rate-value").textContent=lambda.toFixed(2);
        byId("esa-erlang-time-value").textContent=t.toFixed(2);
        byId("esa-erlang-pdf").textContent=pdf.toFixed(5);
        byId("esa-erlang-cdf").textContent=c.toFixed(6);
        byId("esa-erlang-survival").textContent=s.toFixed(6);
        byId("esa-erlang-mean").textContent=(r/lambda).toFixed(4);
        byId("esa-erlang-variance").textContent=(r/(lambda*lambda)).toFixed(4);
        byId("esa-erlang-scale").textContent=(1/lambda).toFixed(4);
        byId("esa-erlang-special").textContent=r===1?
          "Shape 1 is exactly the Exponential distribution with rate λ.":
          "With positive integer shape r = "+r+
          ", this is waiting for the r-th event in a Poisson process.";
        const samples=120,all=[];
        let maximum=0;
        for(let i=0;i<=samples;i++){
          const time=maxTime*i/samples;
          const value=density(time,r,lambda);
          all.push({time,value});
          maximum=Math.max(maximum,value);
        }
        const yToPx=value=>137-110*value/Math.max(maximum,0.000001);
        const path=all.map((pt,i)=>(i===0?"M":"L")+
          xToPx(pt.time).toFixed(3)+" "+yToPx(pt.value).toFixed(3)).join(" ");
        byId("esa-erlang-density-path").setAttribute("d",path);
        const shaded=all.filter(pt=>pt.time<t);
        shaded.push({time:t,value:pdf});
        const coordinates=shaded.map((pt,i)=>(i===0?"L":"L")+
          xToPx(pt.time).toFixed(3)+" "+yToPx(pt.value).toFixed(3)).join(" ");
        byId("esa-erlang-shade").setAttribute("d",
          "M34 137 "+coordinates+" L"+xToPx(t).toFixed(3)+" 137 Z");
        byId("esa-erlang-time-marker").setAttribute("x1",String(xToPx(t)));
        byId("esa-erlang-time-marker").setAttribute("x2",String(xToPx(t)));
        byId("esa-erlang-chart").setAttribute("aria-label",
          "Gamma/Erlang density, shape "+r+", rate "+lambda.toFixed(2)+
          ", shaded probability from time 0 to "+t.toFixed(2)+
          " equals "+c.toFixed(6)+". Survival probability "+s.toFixed(6));
      }
      [rInput,rateInput,timeInput].forEach(input=>input.addEventListener("input",update));
      function preset(r,rate,t) {
        rInput.value=String(r);
        rateInput.value=String(rate);
        timeInput.value=String(t);
        update();
      }
      byId("esa-erlang-reset").addEventListener("click",()=>preset(4,2,2));
      byId("esa-erlang-exponential").addEventListener("click",()=>preset(1,2,2));
      update();
    })();
    </script>

    <h2>The Erlang Distribution</h2>

    <p>
      When the shape parameter is a positive integer,
      the gamma distribution is often called an Erlang distribution.
    </p>

    <p>
      Erlang models are widely used in queueing theory and telecommunications.
    </p>

    <h2>Applications of the Gamma Distribution</h2>

    <ul class="bullets">

      <li>Waiting for multiple customer arrivals</li>

      <li>Reliability engineering</li>

      <li>Queueing systems</li>

      <li>Insurance claim modeling</li>

      <li>Rainfall and environmental processes</li>

      <li>Service-time analysis</li>

    </ul>

    <p>
      Gamma models appear throughout operations research and applied statistics.
    </p>

    <h2>Relationship to Other Distributions</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Distribution</th>
            <th>Relationship</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Exponential</td>
            <td>Gamma with α = 1</td>
          </tr>

          <tr>
            <td>Erlang</td>
            <td>Gamma with integer α</td>
          </tr>

          <tr>
            <td>Chi-Square</td>
            <td>Special gamma distribution</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Why the Gamma Distribution Matters</h2>

    <p>
      The gamma distribution is one of the most flexible continuous distributions.
    </p>

    <p>
      It generalizes the exponential distribution and provides realistic models for many waiting-time processes.
    </p>

    <p>
      Its mathematical properties also make it important in Bayesian statistics and statistical inference.
    </p>

    <h2>The Limitation</h2>

    <p>
      Gamma distributions model positive continuous quantities such as waiting times.
    </p>

    <p>
      Sometimes we are interested in proportions and probabilities instead.
    </p>

    <div class="example-box">

      <p>
        Conversion rate
      </p>

      <p>
        Probability of success
      </p>

      <p>
        Market share
      </p>

      <p>
        Fraction of defective items
      </p>

    </div>

    <p>
      Values like these are naturally restricted between 0 and 1.
    </p>

    <p>
      Such situations are often modeled using the beta distribution.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The beta distribution is one of the most important distributions for modeling probabilities and proportions.
    </p>

    <p>
      It plays a central role in Bayesian statistics and uncertainty quantification.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The gamma distribution models waiting times until multiple events occur</li>

        <li>It generalizes the exponential distribution</li>

        <li>The exponential distribution is the special case α = 1</li>

        <li>The mean equals α/λ</li>

        <li>The variance equals α/λ²</li>

        <li>The gamma function extends factorials to non-integer values</li>

        <li>Gamma distributions are widely used in reliability, queueing, and Bayesian statistics</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/exponential-distribution/">
         ← Previous: Exponential Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/beta-distribution/">
         Next: Beta Distribution →
      </a>

    </div>

  </div>

</section>