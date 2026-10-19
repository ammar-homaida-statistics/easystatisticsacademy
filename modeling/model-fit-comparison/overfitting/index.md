---
layout: default
title: Overfitting
description: Learn what overfitting is, why it occurs, how it affects predictive performance, and why balancing fit and generalization is essential in statistical modeling.
permalink: /modeling/model-fit-comparison/overfitting/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_model_fit_lesson_v0";

  try { localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/model-fit-comparison/overfitting/",
    label: "Overfitting",
    ts: Date.now()
  })); } catch (error) { /* Browsing without storage remains functional. */ }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 6</span>
      <span class="badge">Model Fit & Comparison</span>
      <span class="badge">Overfitting</span>
    </div>

    <h1>Overfitting</h1>

    <p class="lead">
      A model can fit existing data extremely well and still perform poorly on new observations.
    </p>

    <p class="lead">
      This problem is known as overfitting and is one of the most important challenges in statistical modeling and machine learning.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/model-fit-comparison/adjusted-r-squared/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/underfitting/">
         Next: Underfitting →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is Overfitting?</h2>

    <p>
      Overfitting occurs when a model learns not only the underlying signal in the data but also random noise and chance fluctuations.
    </p>

    <p>
      As a result, the model becomes excessively tailored to the specific dataset used for estimation.
    </p>

    <p>
      While performance may appear excellent on the training data, performance often deteriorates on new data.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Overfitting happens when a model captures noise instead of just the meaningful patterns that generalize to future observations.
      </p>

    </div>

    <h2>Why Overfitting Matters</h2>

    <p>
      Most statistical models are built to learn relationships that extend beyond the current dataset.
    </p>

    <p>
      If a model memorizes peculiarities of one sample, it may fail when applied elsewhere.
    </p>

    <p>
      This reduces its practical usefulness.
    </p>

    <h2>An Everyday Analogy</h2>

    <p>
      Imagine a student preparing for an exam by memorizing every answer from one practice test.
    </p>

    <p>
      The student may perform perfectly on that exact practice test.
    </p>

    <p>
      However, performance may be poor when confronted with new questions.
    </p>

    <p>
      Overfitted models behave similarly.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Overfitting is often a form of memorization rather than genuine learning.
      </p>

    </div>

    <h2>Signal Versus Noise</h2>

    <p>
      Every dataset contains:
    </p>

    <ul class="bullets">

      <li>Signal (real patterns)</li>

      <li>Noise (random variation)</li>

    </ul>

    <p>
      Good models capture signal.
    </p>

    <p>
      Overfitted models begin treating noise as if it were signal.
    </p>

    <h2>What Causes Overfitting?</h2>

    <p>
      Several factors increase the risk of overfitting.
    </p>

    <ul class="bullets">

      <li>Too many predictors</li>

      <li>Excessively complex models</li>

      <li>Small sample sizes</li>

      <li>Repeated model tuning on the same dataset</li>

      <li>Including irrelevant variables</li>

    </ul>

    <p>
      These conditions allow models to adapt too closely to random fluctuations.
    </p>

    <h2>A Regression Example</h2>

    <p>
      Suppose a dataset contains a modest linear relationship.
    </p>

    <p>
      One model fits a simple regression line.
    </p>

    <p>
      Another model includes numerous polynomial terms that twist and curve through nearly every point.
    </p>

    <p>
      The second model may fit the training data better but often generalizes worse.
    </p>

    <h2>Training Fit vs Future Performance</h2>

    <p>
      Overfitted models typically show:
    </p>

    <ul class="bullets">

      <li>Excellent training performance</li>

      <li>Poor performance on new data</li>

    </ul>

    <p>
      This difference is one of the primary indicators of overfitting.
    </p>

    <h2>How Overfitting Appears</h2>

    <p>
      When overfitting occurs:
    </p>

    <ul class="bullets">

      <li>R-squared may become very high</li>

      <li>Residuals on training data become very small</li>

      <li>Predictions on future data worsen</li>

    </ul>

    <p>
      Apparent success can therefore be misleading.
    </p>

    <div class="concept-box">

      <strong>Important warning:</strong>

      <p>
        A model that performs extremely well on training data is not automatically a good model.
      </p>

    </div>

    <h2>The Complexity Trade-Off</h2>

    <p>
      Increasing model complexity often improves fit to observed data.
    </p>

    <p>
      However, beyond a certain point, additional complexity primarily captures noise.
    </p>

    <p>
      This creates a trade-off between fit and generalization.
    </p>

    <h2>Generalization</h2>

    <p>
      Generalization refers to how well a model performs on new observations that were not used during model fitting.
    </p>

    <p>
      Good models generalize effectively.
    </p>

    <p>
      Overfitted models often fail to generalize.
    </p>

    <h2>Why More Variables Are Not Always Better</h2>

    <p>
      Adding predictors almost always improves training fit.
    </p>

    <p>
      However, some predictors may contribute little genuine information.
    </p>

    <p>
      Including too many weak predictors can increase overfitting risk.
    </p>

    <h2>Sample Size Matters</h2>

    <p>
      Larger datasets often reduce overfitting risk.
    </p>

    <p>
      With more observations:
    </p>

    <ul class="bullets">

      <li>Random fluctuations average out</li>

      <li>Patterns become more stable</li>

      <li>Model estimates become more reliable</li>

    </ul>

    <p>
      Small datasets are particularly vulnerable to overfitting.
    </p>

    <h2>Detecting Overfitting</h2>

    <p>
      Analysts often compare performance on:
    </p>

    <ul class="bullets">

      <li>Training data</li>

      <li>Validation data</li>

      <li>Test data</li>

    </ul>

    <p>
      Large performance drops outside the training data often indicate overfitting.
    </p>

    <h2>Cross-Validation</h2>

    <p>
      One of the most effective tools for detecting overfitting is cross-validation.
    </p>

    <p>
      The data are repeatedly divided into training and validation subsets.
    </p>

    <p>
      This provides a more realistic assessment of predictive performance.
    </p>

    <h2>Preventing Overfitting</h2>

    <p>
      Several strategies help reduce overfitting risk.
    </p>

    <ul class="bullets">

      <li>Collect more data</li>

      <li>Reduce unnecessary predictors</li>

      <li>Use simpler models</li>

      <li>Apply cross-validation</li>

      <li>Use regularization methods</li>

    </ul>

    <p>
      These approaches encourage better generalization.
    </p>

    <h2>Overfitting and Interpretability</h2>

    <p>
      Highly complex models are often more difficult to interpret.
    </p>

    <p>
      Simpler models may provide slightly worse fit while offering greater transparency and reliability.
    </p>

    <p>
      This is another reason analysts often prefer parsimonious models.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        The goal is not to maximize fit at all costs. The goal is to learn patterns that remain useful beyond the current dataset.
      </p>

    </div>

    <h2>Overfitting in Practice</h2>

    <p>
      Overfitting is common in many fields:
    </p>

    <ul class="bullets">

      <li>Business forecasting</li>

      <li>Medical prediction models</li>

      <li>Social science research</li>

      <li>Machine learning applications</li>

    </ul>

    <p>
      Awareness of overfitting is essential whenever models are used for prediction or decision-making.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Statistical modeling is not simply about explaining existing data.
    </p>

    <p>
      It is about discovering relationships that persist beyond the sample used for analysis.
    </p>

    <p>
      Overfitting occurs when a model loses sight of this goal and begins learning noise instead of meaningful structure.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Overfitting occurs when a model becomes overly tailored to a specific dataset and learns random noise as if it were a real pattern. Such models often perform well on training data but poorly on new observations.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Overfitting represents one extreme of model complexity.
    </p>

    <p>
      The opposite problem occurs when a model is too simple to capture important patterns in the data.
    </p>

    <p>
      The next lesson explores underfitting and explains why overly simple models can be just as problematic as overly complex ones.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Overfitting occurs when a model learns noise rather than just meaningful patterns</li>

        <li>Overfitted models often perform well on training data but poorly on new data</li>

        <li>Excessive complexity increases overfitting risk</li>

        <li>Small samples are particularly vulnerable to overfitting</li>

        <li>High R-squared values do not guarantee good generalization</li>

        <li>Cross-validation is a powerful tool for detecting overfitting</li>

        <li>Simpler models often generalize better than unnecessarily complex models</li>

        <li>The goal of modeling is generalization, not memorization</li>

      </ul>

    </div>

    
<!-- POLYNOMIAL GENERALIZATION EXPLORER -->
<section class="section section-slim" aria-labelledby="esa-overfit-title"><div class="container"><div class="card" id="esa-overfit-lab" style="min-width:0;overflow-wrap:anywhere">
<h2 id="esa-overfit-title">Interactive Model Complexity Explorer</h2>
<p>Fit a polynomial to eight fixed training observations and compare predictions on six <strong>independent, held-out</strong> illustrative test observations. The data remain fixed when you change degree; use test performance here to understand generalization, not as a final unbiased model-selection estimate.</p>
<label for="esa-overfit-degree">Polynomial degree</label> <select id="esa-overfit-degree"><option>0</option><option selected>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option></select>
<button class="btn" id="esa-overfit-reset" type="button">Reset</button>
<p id="esa-overfit-status" role="status" aria-live="polite"></p>
<svg id="esa-overfit-plot" role="img" aria-label="Training points, test points and fitted polynomial curve" viewBox="0 0 640 300" style="width:100%;max-width:640px;display:block"></svg>
<p><small>Blue circles: training; orange squares: held-out test; dark line: fitted polynomial. MSE is the average squared prediction error on each set. High-degree interpolation can reduce training error while increasing test error. Real workflows select complexity using training/validation data and reserve the test set for final evaluation.</small></p>
</div></div></section>
<script>
(function(){
"use strict";const root=document.getElementById("esa-overfit-lab");if(!root)return;const degree=document.getElementById("esa-overfit-degree"),status=document.getElementById("esa-overfit-status"),svg=document.getElementById("esa-overfit-plot"),ns="http://www.w3.org/2000/svg";
const train=[[-1,.8],[-.7,.4],[-.45,.1],[-.15,-.4],[.15,.2],[.45,.7],[.7,.5],[1,1.3]],test=[[-.9,.2],[-.6,.1],[-.3,-.1],[.3,.4],[.6,.8],[.9,.9]];
function element(tag,attrs){const e=document.createElementNS(ns,tag);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,String(v)));svg.appendChild(e);return e;}
function solve(A,b){const n=b.length;for(let k=0;k<n;k++){let p=k;for(let i=k+1;i<n;i++)if(Math.abs(A[i][k])>Math.abs(A[p][k]))p=i;if(Math.abs(A[p][k])<1e-11)throw Error("Polynomial fit is numerically singular.");[A[p],A[k]]=[A[k],A[p]];[b[p],b[k]]=[b[k],b[p]];const d=A[k][k];for(let j=k;j<n;j++)A[k][j]/=d;b[k]/=d;for(let i=0;i<n;i++)if(i!==k){const f=A[i][k];for(let j=k;j<n;j++)A[i][j]-=f*A[k][j];b[i]-=f*b[k];}}return b;}
function fit(d){const n=d+1,A=Array.from({length:n},()=>Array(n).fill(0)),b=Array(n).fill(0);train.forEach(([x,y])=>{const powers=Array.from({length:2*d+1},(_,i)=>x**i);for(let i=0;i<n;i++){b[i]+=powers[i]*y;for(let j=0;j<n;j++)A[i][j]+=powers[i+j];}});return solve(A,b);}
function predict(c,x){return c.reduce((s,v,i)=>s+v*x**i,0);}
function mse(c,points){return points.reduce((s,[x,y])=>s+(predict(c,x)-y)**2,0)/points.length;}
function render(){try{const d=Number(degree.value),c=fit(d),tr=mse(c,train),te=mse(c,test);status.textContent="Degree "+d+" · Training MSE: "+tr.toFixed(5)+" · Test MSE: "+te.toFixed(5);while(svg.firstChild)svg.removeChild(svg.firstChild);const curve=Array.from({length:161},(_,i)=>[-1+i/80,predict(c,-1+i/80)]),ys=[...train,...test,...curve].map(p=>p[1]),ymin=Math.min(...ys)-.2,ymax=Math.max(...ys)+.2;const X=x=>35+(x+1)*285,Y=y=>275-(y-ymin)/(ymax-ymin)*245;let points=curve.map(([x,y])=>X(x)+","+Y(y)).join(" ");element("polyline",{points,fill:"none",stroke:"#334155","stroke-width":2.5});train.forEach(([x,y])=>element("circle",{cx:X(x),cy:Y(y),r:5,fill:"#2563eb"}));test.forEach(([x,y])=>element("rect",{x:X(x)-5,y:Y(y)-5,width:10,height:10,fill:"#ea580c"}));}catch(e){status.textContent=e.message;}}
degree.addEventListener("change",render);document.getElementById("esa-overfit-reset").addEventListener("click",()=>{degree.value="1";render();});render();
})();
</script>

<!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/adjusted-r-squared/">
         ← Previous: Adjusted R-Squared
      </a>

      <a class="btn"
         href="/modeling/model-fit-comparison/underfitting/">
         Next: Underfitting →
      </a>

    </div>

  </div>

</section>