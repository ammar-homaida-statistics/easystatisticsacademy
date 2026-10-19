---
layout: default
title: Least Squares
description: Learn how the least-squares method fits a regression line by minimizing prediction errors and why it is the foundation of ordinary linear regression.
permalink: /modeling/simple-linear-regression/least-squares/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_simple_linear_regression_lesson_v0";

  try {
  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/simple-linear-regression/least-squares/",
    label: "Least Squares",
    ts: Date.now()
  }));
  } catch (_) {
    // The lesson remains usable when browser storage is blocked.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 2</span>
      <span class="badge">Simple Linear Regression</span>
      <span class="badge">Least Squares</span>
    </div>

    <h1>Least Squares</h1>

    <p class="lead">
      A regression line is not chosen arbitrarily.
    </p>

    <p class="lead">
      The least-squares method selects the line that minimizes overall prediction error, making it the standard approach for fitting linear regression models.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/simple-linear-regression/residuals/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/r-squared/">
         Next: R-Squared →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why We Need a Fitting Method</h2>

    <p>
      Suppose we have a scatterplot showing the relationship between two variables.
    </p>

    <p>
      Many different lines could be drawn through the data.
    </p>

    <p>
      The question becomes:
    </p>

    <div class="example-box">

      <p>
        Which line should we choose?
      </p>
    </div>

    <p>
      The least-squares method provides a mathematical answer.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Least squares chooses the regression line that minimizes the total squared residuals.
      </p>

    </div>

    <h2>Recall: What Is a Residual?</h2>

    <p>
      A residual measures prediction error:
    </p>

    

    <p>
      Residuals indicate how far observations are from the fitted regression line.
    </p>

    <p>
      Smaller residuals imply better predictions.
    </p>

    <h2>Why Not Minimize Raw Residuals?</h2>

    <p>
      If we simply added residuals together, positive and negative values would cancel.
    </p>

    <p>
      For example:
    </p>

    <div class="example-box">

      <p>
        +5 + (−5) = 0
      </p>
    </div>

    <p>
      A total of zero would incorrectly suggest perfect predictions.
    </p>

    <p>
      We need a way to measure error that avoids cancellation.
    </p>

    <h2>Squaring Residuals</h2>

    <p>
      Least squares solves this problem by squaring every residual.
    </p>

    <p>
      Squaring produces two benefits:
    </p>

    <ul class="bullets">

      <li>All values become nonnegative</li>

      <li>Large errors receive greater penalties</li>

    </ul>

    <p>
      For example:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Residual</th>
            <th>Squared Residual</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>2</td>
            <td>4</td>
          </tr>

          <tr>
            <td>5</td>
            <td>25</td>
          </tr>

          <tr>
            <td>-5</td>
            <td>25</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Large mistakes contribute much more to the total error.
    </p>

    <h2>The Least-Squares Criterion</h2>

    <p>
      The regression line is chosen to minimize:
    </p>

    \[
    \operatorname{RSS}(b_0,b_1)=\sum_{i=1}^{n}\left[y_i-(b_0+b_1x_i)\right]^2
    \]

    <p>For a line with an intercept and distinct predictor values, the minimizing coefficients are:</p>
    \[
    \hat b_1=\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}{\sum_i(x_i-\bar x)^2},
    \qquad \hat b_0=\bar y-\hat b_1\bar x.
    \]

    <p>
      This quantity is called the Sum of Squared Residuals (SSR) or Residual Sum of Squares (RSS).
    </p>

    <p>
      The best-fitting line is the one with the smallest possible value.
    </p>

    <h2>What Does This Mean Geometrically?</h2>

    <p>
      Imagine drawing vertical distances from every data point to the regression line.
    </p>

    <p>
      Each vertical distance is a residual.
    </p>

    <p>
      Least squares finds the line that makes the combined squared distances as small as possible.
    </p>


    <section class="example-box" id="esa-ols-explorer" aria-labelledby="esa-ols-title">
      <h2 id="esa-ols-title">Interactive Least-Squares Regression Explorer</h2>
      <p>Edit five observed (x, y) pairs. The fitted line minimizes the residual sum of squares among lines with an intercept; compare its fit with any alternative intercept and slope.</p>
      <div class="esa-ols-points" role="group" aria-label="Five editable observed data points">
        <label>Point 1 x <input type="number" id="esa-ols-x1" step="any" value="1"></label>
        <label>Point 1 y <input type="number" id="esa-ols-y1" step="any" value="2"></label>
        <label>Point 2 x <input type="number" id="esa-ols-x2" step="any" value="2"></label>
        <label>Point 2 y <input type="number" id="esa-ols-y2" step="any" value="4"></label>
        <label>Point 3 x <input type="number" id="esa-ols-x3" step="any" value="3"></label>
        <label>Point 3 y <input type="number" id="esa-ols-y3" step="any" value="5"></label>
        <label>Point 4 x <input type="number" id="esa-ols-x4" step="any" value="4"></label>
        <label>Point 4 y <input type="number" id="esa-ols-y4" step="any" value="4"></label>
        <label>Point 5 x <input type="number" id="esa-ols-x5" step="any" value="5"></label>
        <label>Point 5 y <input type="number" id="esa-ols-y5" step="any" value="5"></label>
      </div>
      <fieldset class="esa-ols-alternative">
        <legend>Comparison line (not fitted)</legend>
        <label>Alternative intercept <input type="number" step="any" value="1" id="esa-ols-alt-intercept"></label>
        <label>Alternative slope <input type="number" step="any" value="1" id="esa-ols-alt-slope"></label>
      </fieldset>
      <p id="esa-ols-error" role="alert" hidden></p>
      <svg id="esa-ols-chart" width="440" height="260" viewBox="0 0 440 260" role="img"
           aria-label="Five data points, least-squares fitted line, comparison line, and vertical residual gaps">
        <line x1="44" x2="410" y1="222" y2="222" stroke="currentColor"></line>
        <line x1="44" x2="44" y1="22" y2="222" stroke="currentColor"></line>
        <text x="412" y="241" text-anchor="end" fill="currentColor" font-size="12">x</text>
        <text x="20" y="20" fill="currentColor" font-size="12">y</text>
        <g id="esa-ols-plot"></g>
      </svg>
      <p class="muted-mini"><strong>Graph key:</strong> teal = fitted line; dashed gray = alternative line; circles = observed values; vertical strokes = fitted residuals. The axes rescale for the entered data. Only five points are modeled.</p>
      <div class="esa-ols-results" role="status" aria-live="polite" aria-atomic="true">
        <p>Fitted intercept b₀ = <output id="esa-ols-b0">2.2000</output>;
           fitted slope b₁ = <output id="esa-ols-b1">0.6000</output>.</p>
        <p>Fitted residual sum of squares = <output id="esa-ols-rss">2.4000</output>;
           comparison-line RSS = <output id="esa-ols-alt-rss">4.0000</output>.</p>
        <p>Fitted R² = <output id="esa-ols-r2">0.6000</output>.
           <span id="esa-ols-fit-explanation">The fitted line minimizes in-sample RSS for these observations.</span></p>
      </div>
      <div class="table-wrap">
        <table>
          <caption>Per-observation fitted predictions and residuals (observed y − fitted y)</caption>
          <thead><tr><th scope="col">Point</th><th scope="col">Fitted y</th><th scope="col">Residual</th><th scope="col">Residual²</th></tr></thead>
          <tbody>
            <tr><th scope="row">1</th><td><output id="esa-ols-fit1">2.800</output></td><td><output id="esa-ols-res1">−0.800</output></td><td><output id="esa-ols-sq1">0.640</output></td></tr>
            <tr><th scope="row">2</th><td><output id="esa-ols-fit2">3.400</output></td><td><output id="esa-ols-res2">0.600</output></td><td><output id="esa-ols-sq2">0.360</output></td></tr>
            <tr><th scope="row">3</th><td><output id="esa-ols-fit3">4.000</output></td><td><output id="esa-ols-res3">1.000</output></td><td><output id="esa-ols-sq3">1.000</output></td></tr>
            <tr><th scope="row">4</th><td><output id="esa-ols-fit4">4.600</output></td><td><output id="esa-ols-res4">−0.600</output></td><td><output id="esa-ols-sq4">0.360</output></td></tr>
            <tr><th scope="row">5</th><td><output id="esa-ols-fit5">5.200</output></td><td><output id="esa-ols-res5">−0.200</output></td><td><output id="esa-ols-sq5">0.040</output></td></tr>
          </tbody>
        </table>
      </div>
      <div class="esa-ols-actions">
        <button type="button" class="btn btn-outline" id="esa-ols-reset">Reset example</button>
        <button type="button" class="btn btn-outline" id="esa-ols-outlier">Try an unusual observation</button>
      </div>
      <p class="muted-mini">Requires at least two distinct x values. R² uses 1 − RSS/TSS and is undefined when all y values are identical. Least-squares optimality is in sample; causal interpretation and predictive reliability require additional assumptions.</p>
    </section>
    <style>
      #esa-ols-explorer{box-sizing:border-box;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-ols-explorer .esa-ols-points{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:9px 14px;max-width:530px}
      #esa-ols-explorer label{display:flex;flex-direction:column;gap:4px;font-weight:600;min-width:0}
      #esa-ols-explorer input{box-sizing:border-box;width:100%;max-width:100%;min-width:0;padding:7px;font:inherit}
      #esa-ols-explorer .esa-ols-alternative{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;max-width:530px;min-width:0;border:1px solid var(--border-strong);border-radius:9px;padding:12px;margin:16px 0}
      #esa-ols-explorer .esa-ols-alternative legend{font-weight:700;padding:0 6px}
      #esa-ols-explorer svg{width:100%;height:auto;max-width:550px;display:block;margin:12px auto}
      #esa-ols-explorer svg[hidden],#esa-ols-explorer [hidden]{display:none!important}
      #esa-ols-explorer .esa-ols-actions{display:flex;flex-wrap:wrap;gap:10px}
      #esa-ols-explorer p{margin:11px 0}
      @media print{#esa-ols-explorer .esa-ols-points,#esa-ols-explorer .esa-ols-alternative,#esa-ols-explorer button{display:none}}
    </style>
    <script>
    (function () {
      "use strict";
      const root=document.getElementById("esa-ols-explorer");
      if(!root) return;
      const get=id=>root.querySelector("#esa-ols-"+id);
      const xs=[1,2,3,4,5].map(i=>get("x"+i)),ys=[1,2,3,4,5].map(i=>get("y"+i));
      const altIntercept=get("alt-intercept"),altSlope=get("alt-slope"),err=get("error"),chart=get("chart");
      const outputs=["b0","b1","rss","alt-rss","r2",...Array.from({length:5},(_,i)=>["fit"+(i+1),"res"+(i+1),"sq"+(i+1)]).flat()];
      const svgNS="http://www.w3.org/2000/svg";
      function element(name,attributes) {
        const node=document.createElementNS(svgNS,name);
        Object.entries(attributes).forEach(([key,value])=>node.setAttribute(key,String(value)));
        return node;
      }
      function invalid(message){
        err.hidden=false;err.textContent=message;chart.setAttribute("hidden","");
        outputs.forEach(key=>get(key).textContent="—");
        get("fit-explanation").textContent="Correct the inputs to fit a regression line.";
      }
      function number(input) {
        return input.value.trim()===""?NaN:Number(input.value);
      }
      function update(){
        const x=xs.map(number),y=ys.map(number);
        const a=number(altIntercept),b=number(altSlope);
        if([...x,...y,a,b].some(v=>!Number.isFinite(v)||Math.abs(v)>100)) {
          invalid("Enter finite values between −100 and 100 in every field.");
          return;
        }
        const n=x.length, xbar=x.reduce((s,v)=>s+v,0)/n,ybar=y.reduce((s,v)=>s+v,0)/n;
        const sxx=x.reduce((s,v)=>s+(v-xbar)**2,0);
        if(sxx<=1e-10){
          invalid("At least two clearly different x values are required; slope is undefined for identical or nearly identical x values.");
          return;
        }
        const slope=x.reduce((s,v,i)=>s+(v-xbar)*(y[i]-ybar),0)/sxx;
        const intercept=ybar-slope*xbar;
        const fitted=x.map(v=>intercept+slope*v),residuals=y.map((v,i)=>v-fitted[i]);
        const rss=residuals.reduce((s,v)=>s+v*v,0);
        const altRSS=x.reduce((s,v,i)=>s+(y[i]-a-b*v)**2,0);
        const tss=y.reduce((s,v)=>s+(v-ybar)**2,0);
        const r2=tss<=1e-10?NaN:Math.max(0,Math.min(1,1-rss/tss));
        err.hidden=true;err.textContent="";chart.removeAttribute("hidden");
        get("b0").textContent=intercept.toFixed(4);
        get("b1").textContent=slope.toFixed(4);
        get("rss").textContent=rss.toFixed(4);
        get("alt-rss").textContent=altRSS.toFixed(4);
        get("r2").textContent=Number.isFinite(r2)?r2.toFixed(4):"undefined";
        get("fit-explanation").textContent=Number.isFinite(r2)?
          "OLS has the smallest possible in-sample RSS among intercept-and-slope lines.":
          "The outcomes are constant, so R² is undefined because TSS = 0.";
        for(let i=0;i<n;i++){
          get("fit"+(i+1)).textContent=fitted[i].toFixed(3);
          get("res"+(i+1)).textContent=residuals[i].toFixed(3);
          get("sq"+(i+1)).textContent=(residuals[i]**2).toFixed(3);
        }
        const xMin=Math.min(...x),xMax=Math.max(...x);
        const rawY=[...y,...fitted,...x.map(v=>a+b*v)];
        let yMin=Math.min(...rawY),yMax=Math.max(...rawY);
        const xPad=Math.max((xMax-xMin)*0.1,0.2),yPad=Math.max((yMax-yMin)*0.12,0.4);
        const left=xMin-xPad,right=xMax+xPad;
        yMin-=yPad;yMax+=yPad;
        const X=v=>44+(v-left)/(right-left)*366;
        const Y=v=>222-(v-yMin)/(yMax-yMin)*195;
        const marks=[];
        marks.push(element("line",{x1:X(left),x2:X(right),y1:Y(intercept+slope*left),y2:Y(intercept+slope*right),
                                   stroke:"#0d9488","stroke-width":3}));
        marks.push(element("line",{x1:X(left),x2:X(right),y1:Y(a+b*left),y2:Y(a+b*right),
                                   stroke:"#64748b","stroke-dasharray":"7 5","stroke-width":2}));
        for(let i=0;i<n;i++){
          marks.push(element("line",{x1:X(x[i]),x2:X(x[i]),y1:Y(y[i]),y2:Y(fitted[i]),stroke:"#0d9488","stroke-width":1.5}));
          const point=element("circle",{cx:X(x[i]),cy:Y(y[i]),r:4.5,fill:"#0d9488",stroke:"currentColor","stroke-width":0.5});
          marks.push(point);
        }
        get("plot").replaceChildren(...marks);
        chart.setAttribute("aria-label","Five observed data points with OLS fitted line, alternative line and residual gaps. Fitted intercept "+
          intercept.toFixed(3)+", slope "+slope.toFixed(3)+", RSS "+rss.toFixed(3)+
          ", comparison RSS "+altRSS.toFixed(3)+".");
      }
      [...xs,...ys,altIntercept,altSlope].forEach(input=>input.addEventListener("input",update));
      function preset(values) {
        values.forEach(([x,y],i)=>{xs[i].value=String(x);ys[i].value=String(y)});
        altIntercept.value="1";altSlope.value="1";update();
      }
      get("reset").addEventListener("click",()=>preset([[1,2],[2,4],[3,5],[4,4],[5,5]]));
      get("outlier").addEventListener("click",()=>preset([[1,2],[2,4],[3,5],[4,4],[5,16]]));
      update();
    })();
    </script>

    <h2>A Visual Interpretation</h2>

    <p>
      Think of every residual as a tiny prediction mistake.
    </p>

    <p>
      Least squares seeks the line that makes the overall collection of mistakes as small as possible.
    </p>

    <p>
      This provides a principled definition of the "best" line.
    </p>

    <h2>Why Large Errors Matter More</h2>

    <p>
      Because errors are squared, large residuals contribute disproportionately.
    </p>

    <p>
      Compare:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Residual</th>
            <th>Squared Value</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>2</td>
            <td>4</td>
          </tr>

          <tr>
            <td>10</td>
            <td>100</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      A residual five times larger produces twenty-five times more squared error.
    </p>

    <p>
      This strongly discourages large prediction mistakes.
    </p>

    <h2>Ordinary Least Squares (OLS)</h2>

    <p>
      The standard regression-fitting method is called Ordinary Least Squares (OLS).
    </p>

    <p>
      OLS estimates the slope and intercept that minimize the residual sum of squares.
    </p>

    <p>
      Most introductory regression analysis is based on OLS.
    </p>

    <h2>How the Regression Line Is Determined</h2>

    <p>
      OLS simultaneously chooses:
    </p>

    <ul class="bullets">

      <li>The intercept</li>

      <li>The slope</li>

    </ul>

    <p>
      so that the total squared residuals become as small as possible.
    </p>

    <p>
      Once these values are found, the regression line is fully determined.
    </p>

    <h2>Why Least Squares Became Popular</h2>

    <p>
      Least squares has several desirable properties:
    </p>

    <ul class="bullets">

      <li>Mathematically tractable</li>

      <li>Computationally efficient</li>

      <li>Produces interpretable estimates</li>

      <li>Works well under many conditions</li>

    </ul>

    <p>
      These advantages have made it the dominant linear regression fitting method.
    </p>

    <h2>Least Squares and Prediction</h2>

    <p>
      Because least squares minimizes prediction errors within the observed sample, it often produces strong predictive performance.
    </p>

    <p>
      However, minimizing training error alone does not guarantee perfect performance on future data.
    </p>

    <p>
      Generalization remains an important consideration.
    </p>

    <h2>Residuals After Fitting</h2>

    <p>
      Once the least-squares line is fitted:
    </p>

    <ul class="bullets">

      <li>Residuals can be calculated</li>

      <li>Model assumptions can be checked</li>

      <li>Prediction quality can be evaluated</li>

      <li>Model fit can be summarized</li>

    </ul>

    <p>
      Much of regression analysis builds upon these residuals.
    </p>

    <h2>Least Squares Does Not Guarantee Perfection</h2>

    <p>
      The least-squares line is the best line according to the least-squares criterion.
    </p>

    <p>
      It does not mean:
    </p>

    <ul class="bullets">

      <li>Predictions are perfect</li>

      <li>The relationship is strong</li>

      <li>The model is causal</li>

      <li>The line explains all variation</li>

    </ul>

    <p>
      It simply means no other straight line produces a smaller total squared residual.
    </p>

    <div class="concept-box">

      <strong>Important distinction:</strong>

      <p>
        Least squares identifies the best-fitting line among linear candidates, not necessarily a perfect model of reality.
      </p>

    </div>

    <h2>Connecting Least Squares to Model Fit</h2>

    <p>
      Smaller residual sums generally indicate better fit.
    </p>

    <p>
      However, analysts often want a standardized measure of fit that is easier to interpret.
    </p>

    <p>
      This leads naturally to one of the most common regression metrics: R-squared.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Least squares provides the mathematical foundation of ordinary linear regression.
    </p>

    <p>
      By minimizing the total squared residuals, it determines the line that best balances prediction errors across all observations.
    </p>

    <p>
      Understanding least squares is essential because it explains how regression models are fitted and why the resulting line looks the way it does.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The least-squares method fits a regression line by minimizing the sum of squared residuals. This produces the ordinary least-squares regression line, the standard approach used in simple linear regression.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      After fitting a regression line, analysts want to know how much variation in the outcome has been explained.
    </p>

    <p>
      One of the most widely used measures for answering this question is R-squared.
    </p>

    <p>
      The next lesson introduces R-squared and explains how it summarizes model fit.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Least squares is the standard method for fitting linear regression models</li>

        <li>Residuals measure prediction errors</li>

        <li>Residuals are squared to prevent cancellation and emphasize large errors</li>

        <li>The least-squares line minimizes the sum of squared residuals</li>

        <li>Ordinary Least Squares (OLS) is the most common regression-fitting method</li>

        <li>OLS determines both the slope and intercept simultaneously</li>

        <li>The least-squares line is the best-fitting line under the squared-error criterion</li>

        <li>Least squares forms the mathematical foundation of linear regression</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/residuals/">
         ← Previous: Residuals
      </a>

      <a class="btn"
         href="/modeling/simple-linear-regression/r-squared/">
         Next: R-Squared →
      </a>

    </div>

  </div>

</section>