---
layout: default
title: Chi-Square Test of Independence
description: Learn how the chi-square test of independence evaluates whether two categorical variables are associated.
permalink: /inference/classical-tests/chi-square-independence-test/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_classical_tests_lesson_v0";

  try {
  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/chi-square-independence-test/",
    label: "Chi-Square Test of Independence",
    ts: Date.now()
  }));
  } catch (_) {
    // Disabled browser storage must not interrupt the lesson.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 4</span>
      <span class="badge">Classical Tests</span>
      <span class="badge">Categorical Association</span>
    </div>

    <h1>Chi-Square Test of Independence</h1>

    <p class="lead">
      Many studies seek to determine whether two categorical variables are related.
    </p>

    <p class="lead">
      The chi-square test of independence evaluates whether an observed association between categorical variables is stronger than would be expected from random variation alone.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/chi-square-goodness-of-fit/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/classical-tests/chi-square-homogeneity-test/">
         Next: Chi-Square Test of Homogeneity →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Research Question</h2>

    <p>
      Suppose researchers collect data on:
    </p>

    <ul class="bullets">

      <li>Gender and product preference</li>

      <li>Smoking status and disease occurrence</li>

      <li>Education level and voting behavior</li>

      <li>Device type and website conversion</li>

    </ul>

    <p>
      The question becomes:
    </p>

    <div class="example-box">

      <p>
        Are these variables related?
      </p>
    </div>

    <p>
      This is the purpose of the chi-square test of independence.
    </p>

    <h2>What Does Independence Mean?</h2>

    <div class="concept-box">

      <strong>Independence:</strong>

      <p>
        Two variables are independent if knowledge of one variable provides no information about the other.
      </p>

    </div>

    <p>
      Under independence, category proportions remain the same across groups.
    </p>

    <h2>The Null and Alternative Hypotheses</h2>

    <div class="example-box">

      <p>
        H₀: The variables are independent.
      </p>

      <p>
        Hₐ: The variables are associated.
      </p>

    </div>

    <p>
      The test does not specify the nature of the association.
    </p>

    <p>
      It only evaluates whether evidence of a relationship exists.
    </p>

    <h2>Contingency Tables</h2>

    <p>
      Data are organized into a contingency table.
    </p>

    <p>
      Example:
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th></th>
            <th>Prefers A</th>
            <th>Prefers B</th>
            <th>Total</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Male</td>
            <td>40</td>
            <td>60</td>
            <td>100</td>
          </tr>

          <tr>
            <td>Female</td>
            <td>70</td>
            <td>30</td>
            <td>100</td>
          </tr>

          <tr>
            <td>Total</td>
            <td>110</td>
            <td>90</td>
            <td>200</td>
          </tr>

        </tbody>

      </table>

    </div>


    <!-- Interactive 2 x 2 Pearson chi-square teaching explorer. -->
    <section class="example-box" id="esa-chi-independence-lab" aria-labelledby="esa-chi-heading">
      <h2 id="esa-chi-heading">Interactive 2 × 2 Independence Explorer</h2>
      <p>Change the four observed frequencies to see how independence predicts each cell, and how cell discrepancies add to Pearson’s chi-square statistic. The table starts with the worked example above.</p>
      <div class="esa-chi-input-grid">
        <label>Male, Prefers A <input id="esa-chi-a" type="number" min="0" max="10000000" step="1" value="40" inputmode="numeric"></label>
        <label>Male, Prefers B <input id="esa-chi-b" type="number" min="0" max="10000000" step="1" value="60" inputmode="numeric"></label>
        <label>Female, Prefers A <input id="esa-chi-c" type="number" min="0" max="10000000" step="1" value="70" inputmode="numeric"></label>
        <label>Female, Prefers B <input id="esa-chi-d" type="number" min="0" max="10000000" step="1" value="30" inputmode="numeric"></label>
      </div>
      <p id="esa-chi-error" role="alert" hidden></p>
      <div class="table-wrap">
        <table>
          <caption>Expected cell counts and contributions (Observed → Expected; χ² contribution)</caption>
          <thead><tr><th scope="col">Group</th><th scope="col">Prefers A</th><th scope="col">Prefers B</th></tr></thead>
          <tbody>
            <tr><th scope="row">Male</th><td><output id="esa-chi-cell-a">40 → 55.000; 4.0909</output></td><td><output id="esa-chi-cell-b">60 → 45.000; 5.0000</output></td></tr>
            <tr><th scope="row">Female</th><td><output id="esa-chi-cell-c">70 → 55.000; 4.0909</output></td><td><output id="esa-chi-cell-d">30 → 45.000; 5.0000</output></td></tr>
          </tbody>
        </table>
      </div>
      <div class="esa-chi-results" role="status" aria-live="polite" aria-atomic="true">
        <p>Pearson χ² = <output id="esa-chi-stat">18.181818</output>;
           degrees of freedom = <output id="esa-chi-df">1</output>.</p>
        <p>Upper-tail p-value (asymptotic, no continuity correction) =
           <output id="esa-chi-p">2.008e-5</output>.</p>
        <p>Cramér’s V = <output id="esa-chi-v">0.301511</output>.
           For a 2 × 2 table, V = √(χ²/N).</p>
      </div>
      <p id="esa-chi-warning">All expected frequencies are at least 5 for the initial example.</p>
      <p class="muted-mini">The chi-square p-value uses the χ² distribution with 1 degree of freedom, not Fisher’s exact test. Observations must be independent, and sparse expected cells can invalidate the large-sample approximation. Association is not evidence of causation.</p>
      <button type="button" class="btn btn-outline" id="esa-chi-reset">Reset worked example</button>
    </section>
    <style>
      #esa-chi-independence-lab{box-sizing:border-box;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-chi-independence-lab .esa-chi-input-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,180px),1fr));gap:12px;margin:14px 0}
      #esa-chi-independence-lab label{display:flex;flex-direction:column;gap:6px;min-width:0;font-weight:600}
      #esa-chi-independence-lab input{box-sizing:border-box;max-width:100%;width:100%;font:inherit;padding:8px}
      #esa-chi-independence-lab td{min-width:0;overflow-wrap:anywhere}
      #esa-chi-independence-lab p{margin:10px 0}
      #esa-chi-independence-lab [role="alert"]{font-weight:700}
      @media print{#esa-chi-independence-lab button,#esa-chi-independence-lab .esa-chi-input-grid{display:none}}
    </style>
    <script>
    (function () {
      "use strict";
      const root=document.getElementById("esa-chi-independence-lab");
      if(!root) return;
      const find=id=>root.querySelector("#"+id);
      const ids=["a","b","c","d"], inputs=ids.map(id=>find("esa-chi-"+id));
      const resultIds=["esa-chi-stat","esa-chi-p","esa-chi-v",...ids.map(id=>"esa-chi-cell-"+id)];
      // Abramowitz-Stegun 7.1.26, maximum absolute erfc error approximately 1.5e-7.
      function erfc(x) {
        const t=1/(1+0.3275911*x);
        const polynomial=t*(0.254829592+t*(-0.284496736+
          t*(1.421413741+t*(-1.453152027+t*1.061405429))));
        return polynomial*Math.exp(-x*x);
      }
      function clear(message) {
        find("esa-chi-error").hidden=false;
        find("esa-chi-error").textContent=message;
        resultIds.forEach(id=>find(id).textContent="—");
        find("esa-chi-warning").textContent="Correct the inputs to evaluate the large-sample conditions.";
      }
      function update() {
        const values=inputs.map(input=>input.value.trim()===""?NaN:Number(input.value));
        if(values.some(n=>!Number.isSafeInteger(n)||n<0||n>10000000)) {
          clear("Enter a whole-number count from 0 to 10,000,000 in every cell.");
          return;
        }
        const [a,b,c,d]=values, rows=[a+b,c+d],cols=[a+c,b+d];
        const N=a+b+c+d;
        if(N===0||rows.some(n=>n===0)||cols.some(n=>n===0)) {
          clear("Both row totals and both column totals must be positive; zero margins make the independence statistic undefined.");
          return;
        }
        find("esa-chi-error").hidden=true;
        find("esa-chi-error").textContent="";
        const expected=[rows[0]*cols[0]/N,rows[0]*cols[1]/N,
          rows[1]*cols[0]/N,rows[1]*cols[1]/N];
        const contributions=values.map((o,i)=>(o-expected[i])**2/expected[i]);
        const chi=contributions.reduce((sum,x)=>sum+x,0);
        // With df=1, chi-square survival = erfc(sqrt(chi / 2)).
        const p=Math.min(1,Math.max(0,erfc(Math.sqrt(chi/2))));
        ids.forEach((id,i)=>find("esa-chi-cell-"+id).textContent=
          values[i]+" → "+expected[i].toFixed(3)+"; "+contributions[i].toFixed(4));
        find("esa-chi-stat").textContent=chi.toFixed(6);
        find("esa-chi-p").textContent=p<1e-12?"< 1e-12":(p<0.0001?p.toExponential(3):p.toFixed(6));
        find("esa-chi-v").textContent=Math.sqrt(chi/N).toFixed(6);
        const small=expected.filter(n=>n<5).length;
        find("esa-chi-warning").textContent=small?
          small+" of 4 expected frequencies are below 5. The chi-square approximation may be unreliable; consider Fisher’s exact test and the sampling design.":
          "All four expected frequencies are at least 5. Independence of observations must still be checked from the study design.";
      }
      inputs.forEach(input=>input.addEventListener("input",update));
      find("esa-chi-reset").addEventListener("click",()=>{
        [40,60,70,30].forEach((n,i)=>inputs[i].value=String(n));
        update();
      });
      update();
    })();
    </script>

    <h2>Observed Counts</h2>

    <p>
      The entries inside the table are the observed counts:
    </p>

    
    \[
    O_{ij}=\text{observed count in row }i\text{ and column }j
    \]


    <p>
      These are the actual frequencies recorded in the sample.
    </p>

    <h2>Expected Counts Under Independence</h2>

    <p>
      If the variables are independent, expected counts can be calculated from the row and column totals.
    </p>

    <p>
      The formula is:
    </p>

    
    \[
    E_{ij}=\frac{(\text{row }i\text{ total})(\text{column }j\text{ total})}{N}
    \]


    <h2>Example Expected Count</h2>

    <p>
      For the Male–Prefers A cell:
    </p>

    
    \[
    E_{\text{Male, Prefers A}}=\frac{100\times110}{200}=55
    \]


    <p>
      Under independence, we would expect 55 observations in that cell.
    </p>

    <h2>Observed vs Expected</h2>

    <p>
      The observed count was:
    </p>

    <div class="example-box">

      <p>
        40
      </p>
    </div>

    <p>
      The expected count was:
    </p>

    <div class="example-box">

      <p>
        55
      </p>
    </div>

    <p>
      This discrepancy contributes to the test statistic.
    </p>

    <h2>The Chi-Square Statistic</h2>

    <p>
      The test statistic is:
    </p>

    
    \[
    \chi^2=\sum_{i=1}^{r}\sum_{j=1}^{c}\frac{(O_{ij}-E_{ij})^2}{E_{ij}}
    \]


    <p>
      The sum is taken across every cell in the contingency table.
    </p>

    <h2>Interpreting χ²</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>χ² Value</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Small</td>
            <td>Observed counts close to independence expectations</td>
          </tr>

          <tr>
            <td>Large</td>
            <td>Evidence of association</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Chi-Square Distribution</h2>

    <p>
      Under:
    </p>

    
    \[
    H_0:\ \text{the categorical variables are independent}
    \]


    <p>
      the test statistic follows a chi-square distribution approximately.
    </p>

    <p>
      Larger χ² values produce smaller p-values.
    </p>

    <h2>Degrees of Freedom</h2>

    <p>
      For a contingency table with:
    </p>

    <ul class="bullets">

      <li>r rows</li>

      <li>c columns</li>

    </ul>

    <p>
      the degrees of freedom are:
    </p>

    
    \[
    \operatorname{df}=(r-1)(c-1)
    \]


    <h2>Example</h2>

    <p>
      For a:
    </p>

    <div class="example-box">

      <p>
        2 × 2 table
      </p>
    </div>

    <p>
      we have:
    </p>

    
    \[
    \operatorname{df}=(2-1)(2-1)=1
    \]


    <h2>The p-Value</h2>

    <p>
      Once:
    </p>

    <ul class="bullets">

      <li>χ² is computed</li>

      <li>Degrees of freedom are determined</li>

    </ul>

    <p>
      the p-value is obtained from the chi-square distribution.
    </p>

    <h2>Decision Rule</h2>

    <div class="concept-box">

      <strong>Decision Rule:</strong>

      <p>
        Reject H₀ if p ≤ α.
      </p>

      <p>
        Fail to reject H₀ if p > α.
      </p>

    </div>

    <h2>What Does Rejection Mean?</h2>

    <p>
      Rejecting:
    </p>

    
    \[
    H_0:\ \text{the two categorical variables are independent}
    \]


    <p>
      means the data provide evidence that the variables are associated.
    </p>

    <p>
      It does not establish causation.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Association does not imply causation.
      </p>

    </div>

    <h2>Assumptions</h2>

    <ul class="bullets">

      <li>Random sampling</li>

      <li>Independent observations</li>

      <li>Categorical variables</li>

      <li>Sufficiently large expected counts</li>

    </ul>

    <h2>Expected Count Guideline</h2>

    <p>
      A common recommendation is:
    </p>

    <div class="example-box">

      <p>
        All expected counts should generally be at least 5.
      </p>
    </div>

    <p>
      This helps ensure a reliable chi-square approximation.
    </p>

    <h2>Applications</h2>

    <div class="example-box">

      <p>
        Marketing research
      </p>

      <p>
        Medical studies
      </p>

      <p>
        Social-science surveys
      </p>

      <p>
        Political polling
      </p>

      <p>
        User-behavior analysis
      </p>

    </div>

    <h2>Independence vs Goodness-of-Fit</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Goodness-of-Fit</th>
            <th>Independence Test</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Variables</td>
            <td>One</td>
            <td>Two</td>
          </tr>

          <tr>
            <td>Question</td>
            <td>Matches expected distribution?</td>
            <td>Variables associated?</td>
          </tr>

          <tr>
            <td>Expected counts from</td>
            <td>Hypothesized probabilities</td>
            <td>Row and column totals</td>
          </tr>

          <tr>
            <td>Table structure</td>
            <td>Single categorical variable</td>
            <td>Contingency table</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Measuring Association Strength</h2>

    <p>
      A significant chi-square result indicates that an association exists.
    </p>

    <p>
      However, significance alone does not describe the strength of the relationship.
    </p>

    <p>
      Additional measures such as Cramér's V are often used to quantify association strength.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      The chi-square test of independence is one of the most important methods for categorical data analysis.
    </p>

    <p>
      It allows researchers to investigate relationships between variables without requiring numerical measurements.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The chi-square test of independence evaluates whether two categorical variables are associated. It compares observed counts to the counts expected under independence and determines whether discrepancies are larger than expected by chance.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      The chi-square test of independence analyzes association within a single population.
    </p>

    <p>
      A closely related procedure compares categorical distributions across multiple populations or groups.
    </p>

    <p>
      The next lesson introduces the chi-square test of homogeneity.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The test evaluates whether two categorical variables are independent</li>

        <li>Data are organized in contingency tables</li>

        <li>Expected counts are computed from row and column totals</li>

        <li>The chi-square statistic measures discrepancies between observed and expected counts</li>

        <li>Degrees of freedom equal (r − 1)(c − 1)</li>

        <li>Rejecting H₀ suggests an association exists</li>

        <li>Association does not imply causation</li>

        <li>The test is widely used across social sciences, medicine, business, and public policy</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/chi-square-goodness-of-fit/">
         ← Previous: Chi-Square Goodness-of-Fit Test
      </a>

      <a class="btn"
         href="/inference/classical-tests/chi-square-homogeneity-test/">
         Next: Chi-Square Test of Homogeneity →
      </a>

    </div>

  </div>

</section>