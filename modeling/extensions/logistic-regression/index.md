---
layout: default
title: Logistic Regression
description: Learn what logistic regression is, why it is used for binary outcomes, and how it extends regression ideas beyond continuous outcomes.
permalink: /modeling/extensions/logistic-regression/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_extensions_lesson_v0";

  try {
  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/extensions/logistic-regression/",
    label: "Logistic Regression",
    ts: Date.now()
  }));
  } catch (_) {
    // Browser storage may be denied; keep the interactive lesson available.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 7</span>
      <span class="badge">Extensions</span>
      <span class="badge">Logistic Regression</span>
    </div>

    <h1>Logistic Regression</h1>

    <p class="lead">
      Many important questions involve outcomes with only two possible categories.
    </p>

    <p class="lead">
      Examples include whether a customer makes a purchase, whether a patient survives treatment, or whether a loan defaults.
    </p>

    <p class="lead">
      Logistic regression extends regression modeling to handle these binary outcomes appropriately.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/extensions/why-extensions/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/extensions/probability-vs-logit/">
         Next: Probability vs Logit →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is Logistic Regression?</h2>

    <p>
      Logistic regression is a statistical model used when the outcome variable has two possible categories.
    </p>

    <p>
      These categories are often coded as:
    </p>

    <ul class="bullets">

      <li>0 = No</li>

      <li>1 = Yes</li>

    </ul>

    <p>
      The model estimates the probability that an observation belongs to one of the categories.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Logistic regression models the probability of a binary outcome using predictor variables.
      </p>

    </div>

    <h2>Why Not Use Linear Regression?</h2>

    <p>
      Suppose we want to predict whether a customer will make a purchase.
    </p>

    <p>
      A probability must always lie between 0 and 1.
    </p>

    <p>
      Ordinary linear regression does not guarantee this.
    </p>

    <p>
      It can produce impossible predictions such as:
    </p>

    <div class="example-box">

      <p>
        Probability = -0.15
      </p>

      <p>
        Probability = 1.27
      </p>

    </div>

    <p>
      Because these values are not valid probabilities, a different approach is needed.
    </p>

    <h2>Binary Outcomes Are Everywhere</h2>

    <p>
      Logistic regression is widely used because many real-world outcomes are binary.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Disease vs no disease</li>

      <li>Pass vs fail</li>

      <li>Click vs no click</li>

      <li>Default vs no default</li>

      <li>Purchase vs no purchase</li>

    </ul>

    <p>
      These situations naturally lead to probability modeling.
    </p>

    <h2>The Goal of Logistic Regression</h2>

    <p>
      Rather than predicting the outcome directly, logistic regression predicts:
    </p>

    <div class="example-box">

      <p>
        The probability that the outcome equals 1
      </p>
    </div>

    <p>
      This probability can then be used to classify observations or estimate risk.
    </p>

    <h2>A Probability-Based Model</h2>

    <p>
      Imagine predicting whether a student passes an exam.
    </p>

    <p>
      Instead of predicting:
    </p>

    <div class="example-box">

      <p>
        Pass = 0.82
      </p>
    </div>

    <p>
      the model predicts:
    </p>

    <div class="example-box">

      <p>
        Probability of passing = 82%
      </p>
    </div>

    <p>
      This interpretation is more meaningful for binary outcomes.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Logistic regression focuses on probabilities rather than directly predicting category labels.
      </p>

    </div>

    <h2>The Logistic Curve</h2>

    <p>
      Logistic regression uses an S-shaped relationship known as the logistic curve.
    </p>

    <p>
      This curve has two important properties:
    </p>

    <ul class="bullets">

      <li>Predicted probabilities remain between 0 and 1</li>

      <li>Changes in predictors can have nonlinear effects on probability</li>

    </ul>

    <p>
      These properties make logistic regression suitable for probability modeling.
    </p>


    <!-- Interactive Logistic Regression Explorer -->
    <section id="esa-logistic-lab" class="example-box" aria-labelledby="esa-logistic-title">
      <h2 id="esa-logistic-title">Interactive Logistic Regression Explorer</h2>
      <p>Adjust a hypothetical binary-response model. Coefficients are teaching examples, not estimates from observations.</p>
      \[
      \eta=\beta_0+\beta_1x
      \]
      \[
      p(x)=\frac{1}{1+\exp(-\eta)}
      \]
      \[
      \mathrm{odds}(x)=\exp(\eta)
      \]
      <div class="esa-logistic-controls">
        <label>Intercept β₀ <input id="esa-logistic-b0" type="number" min="-10" max="10" step="0.1" value="-2"></label>
        <label>Slope β₁ <input id="esa-logistic-b1" type="number" min="-10" max="10" step="0.1" value="1"></label>
        <label>Predictor x <input id="esa-logistic-x" type="number" min="-8" max="8" step="0.5" value="2"></label>
        <label>Classification threshold <input id="esa-logistic-threshold" type="number" min="0" max="1" step="0.05" value="0.5"></label>
      </div>
      <p id="esa-logistic-error" role="alert" hidden></p>
      <svg id="esa-logistic-chart" viewBox="0 0 440 255" width="440" height="255" role="img"
           aria-label="Logistic probability curve, selected predictor and classification threshold">
        <line x1="44" y1="210" x2="414" y2="210" stroke="currentColor"></line>
        <line x1="44" y1="20" x2="44" y2="210" stroke="currentColor"></line>
        <text x="15" y="25" font-size="12" fill="currentColor">p</text>
        <text x="414" y="240" font-size="12" text-anchor="end" fill="currentColor">x</text>
        <text x="44" y="229" font-size="11" fill="currentColor">−8</text>
        <text x="229" y="229" font-size="11" text-anchor="middle" fill="currentColor">0</text>
        <text x="414" y="229" font-size="11" text-anchor="end" fill="currentColor">8</text>
        <path id="esa-logistic-curve" stroke="#0d9488" stroke-width="2.5" fill="none"></path>
        <line id="esa-logistic-threshold-line" x1="44" x2="414" stroke="#64748b" stroke-dasharray="6 4"></line>
        <line id="esa-logistic-selected-line" stroke="#0d9488" stroke-dasharray="3 4"></line>
        <circle id="esa-logistic-selected-dot" r="5" fill="#0d9488"></circle>
      </svg>
      <p class="muted-mini">Teal: probability and selected predictor. Horizontal dashed line: threshold used to convert a probability to a classification.</p>
      <div role="status" aria-live="polite" aria-atomic="true">
        <p>Log-odds η: <output id="esa-logistic-eta">0.000000</output>;
          predicted probability p: <output id="esa-logistic-prob">0.500000</output>.</p>
        <p>Odds: <output id="esa-logistic-odds">1.000000</output>;
          odds ratio per one-unit increase in x: <output id="esa-logistic-or">2.718282</output>.</p>
        <p>Threshold classification: <strong><output id="esa-logistic-class">1 (positive)</output></strong>.</p>
      </div>
      <button type="button" class="btn btn-outline" id="esa-logistic-reset">Reset logistic example</button>
      <p class="muted-mini">Odds ratios describe multiplicative changes in odds, not changes in risk or probability. This threshold is illustrative; it has not been optimized. Associations are not automatically causal.</p>
    </section>
    <style>
      #esa-logistic-lab{max-width:100%;min-width:0;box-sizing:border-box;overflow-wrap:anywhere}
      #esa-logistic-lab .esa-logistic-controls{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,150px),1fr));gap:12px;margin:14px 0}
      #esa-logistic-lab label{display:flex;flex-direction:column;min-width:0;gap:6px;font-weight:600}
      #esa-logistic-lab input{box-sizing:border-box;width:100%;max-width:100%;min-width:0;padding:8px;font:inherit}
      #esa-logistic-lab svg{display:block;max-width:540px;width:100%;height:auto;margin:12px auto}
      #esa-logistic-lab [hidden]{display:none!important}
      #esa-logistic-lab p{margin:11px 0}
    </style>
    <script>
    (function () {
      "use strict";
      const root=document.getElementById("esa-logistic-lab");if(!root)return;
      const get=id=>root.querySelector("#esa-logistic-"+id);
      const inputs=["b0","b1","x","threshold"].map(get);
      const logistic=z=>z>=0?1/(1+Math.exp(-z)):Math.exp(z)/(1+Math.exp(z));
      const X=v=>44+(v+8)*370/16,Y=p=>210-188*p;
      function update(){
        const values=inputs.map(i=>i.value.trim()===""?NaN:Number(i.value));
        const [b0,b1,x,t]=values;
        if(!values.every(Number.isFinite)||Math.abs(b0)>10||Math.abs(b1)>10||x< -8||x>8||t<0||t>1){
          get("error").textContent="Enter finite intercept and slope between −10 and 10, x from −8 to 8, and threshold from 0 to 1.";
          get("error").hidden=false;get("chart").setAttribute("hidden","");
          ["eta","prob","odds","or","class"].forEach(k=>get(k).textContent="—");
          return;
        }
        const eta=b0+b1*x,p=logistic(eta),odds=Math.exp(eta),OR=Math.exp(b1);
        get("error").hidden=true;get("error").textContent="";get("chart").removeAttribute("hidden");
        get("eta").textContent=eta.toFixed(6);get("prob").textContent=p.toFixed(6);
        get("odds").textContent=odds>=1000000||odds<0.00001?odds.toExponential(4):odds.toFixed(6);
        get("or").textContent=OR.toFixed(6);get("class").textContent=p>=t?"1 (positive)":"0 (negative)";
        let d="";
        for(let i=0;i<=160;i++){
          const xx=-8+i/10;
          d+=(i?" L ":"M ")+X(xx).toFixed(2)+" "+Y(logistic(b0+b1*xx)).toFixed(2);
        }
        get("curve").setAttribute("d",d);
        get("threshold-line").setAttribute("y1",Y(t));get("threshold-line").setAttribute("y2",Y(t));
        get("selected-line").setAttribute("x1",X(x));get("selected-line").setAttribute("x2",X(x));
        get("selected-line").setAttribute("y1",Y(p));get("selected-line").setAttribute("y2",210);
        get("selected-dot").setAttribute("cx",X(x));get("selected-dot").setAttribute("cy",Y(p));
        get("chart").setAttribute("aria-label","Logistic model: at x "+x+", probability "+
          p.toFixed(6)+", odds "+odds.toPrecision(5)+", threshold "+t+
          ", classified "+(p>=t?"positive":"negative")+".");
      }
      inputs.forEach(i=>{i.addEventListener("input",update);i.addEventListener("change",update)});
      get("reset").addEventListener("click",()=>{
        [-2,1,2,0.5].forEach((v,i)=>inputs[i].value=String(v));update();
      });
      update();
    })();
    </script>

    <h2>Probabilities Change Gradually</h2>

    <p>
      As predictor values increase, predicted probabilities typically move smoothly between:
    </p>

    <ul class="bullets">

      <li>Near 0</li>

      <li>Near 1</li>

    </ul>

    <p>
      The transition occurs gradually rather than abruptly.
    </p>

    <h2>Inputs and Outputs</h2>

    <p>
      Logistic regression uses predictor variables in much the same way as ordinary regression.
    </p>

    <p>
      Inputs might include:
    </p>

    <ul class="bullets">

      <li>Age</li>

      <li>Income</li>

      <li>Education</li>

      <li>Study hours</li>

    </ul>

    <p>
      The output is a probability rather than a continuous numerical prediction.
    </p>

    <h2>A Medical Example</h2>

    <p>
      Researchers may wish to predict whether a patient develops a disease.
    </p>

    <p>
      Predictors might include:
    </p>

    <ul class="bullets">

      <li>Age</li>

      <li>Blood pressure</li>

      <li>Smoking status</li>

      <li>Body mass index</li>

    </ul>

    <p>
      Logistic regression estimates the probability of disease for each patient.
    </p>

    <h2>A Business Example</h2>

    <p>
      A company may wish to predict whether a customer will purchase a product.
    </p>

    <p>
      Predictors might include:
    </p>

    <ul class="bullets">

      <li>Previous purchases</li>

      <li>Website activity</li>

      <li>Customer demographics</li>

      <li>Marketing exposure</li>

    </ul>

    <p>
      The model produces a purchase probability for each customer.
    </p>

    <h2>How Predictions Become Decisions</h2>

    <p>
      Predicted probabilities can be converted into classifications.
    </p>

    <p>
      For example:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Predicted Probability</th>
            <th>Classification</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>0.90</td>
            <td>Likely Yes</td>
          </tr>

          <tr>
            <td>0.70</td>
            <td>Likely Yes</td>
          </tr>

          <tr>
            <td>0.45</td>
            <td>Likely No</td>
          </tr>

          <tr>
            <td>0.10</td>
            <td>Likely No</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Classification rules are often based on probability thresholds.
    </p>

    <h2>Logistic Regression Still Uses Predictors and Coefficients</h2>

    <p>
      Despite being designed for binary outcomes, logistic regression retains many familiar regression concepts.
    </p>

    <ul class="bullets">

      <li>Predictors</li>

      <li>Coefficients</li>

      <li>Model fitting</li>

      <li>Prediction</li>

      <li>Inference</li>

    </ul>

    <p>
      This makes it a natural extension of ordinary regression.
    </p>

    <h2>Common Applications</h2>

    <p>
      Logistic regression is used extensively in:
    </p>

    <ul class="bullets">

      <li>Medicine</li>

      <li>Public health</li>

      <li>Finance</li>

      <li>Marketing</li>

      <li>Social science</li>

      <li>Machine learning</li>

    </ul>

    <p>
      It remains one of the most widely used classification models.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        Logistic regression is often the first model analysts consider when dealing with binary outcomes because it combines interpretability with strong predictive performance.
      </p>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      Logistic regression extends the core ideas of regression to situations where outcomes have only two categories.
    </p>

    <p>
      By modeling probabilities rather than continuous outcomes, it solves a problem that ordinary linear regression cannot handle effectively.
    </p>

    <p>
      This makes it one of the most important and widely applied extensions in modern statistics.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Logistic regression is a regression-based method for modeling binary outcomes. It predicts probabilities that remain between 0 and 1 and provides a principled way to analyze yes/no, success/failure, and similar outcomes.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Logistic regression predicts probabilities, but the model itself is built around a transformed quantity called the logit.
    </p>

    <p>
      Understanding the distinction between probability and logit is essential for interpreting logistic regression coefficients.
    </p>

    <p>
      The next lesson introduces the relationship between probabilities and logits and explains why this transformation is used.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Logistic regression is designed for binary outcomes</li>

        <li>It predicts probabilities rather than continuous outcomes</li>

        <li>Predicted probabilities always remain between 0 and 1</li>

        <li>It solves problems that linear regression cannot handle properly</li>

        <li>Binary outcomes are common in many real-world applications</li>

        <li>Probabilities can be converted into classifications</li>

        <li>Logistic regression retains many familiar regression concepts</li>

        <li>It is one of the most widely used statistical modeling techniques</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/extensions/why-extensions/">
         ← Previous: Why Extensions?
      </a>

      <a class="btn"
         href="/modeling/extensions/probability-vs-logit/">
         Next: Probability vs Logit →
      </a>

    </div>

  </div>

</section>