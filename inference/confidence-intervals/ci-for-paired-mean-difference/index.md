---
layout: default
title: Confidence Interval for a Paired Mean Difference
description: Learn how to construct and interpret confidence intervals for paired data such as before-and-after studies and matched observations.
permalink: /inference/confidence-intervals/ci-for-paired-mean-difference/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_confidence_intervals_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/confidence-intervals/ci-for-paired-mean-difference/",
    label: "Confidence Interval for a Paired Mean Difference",
    ts: Date.now()
  }));
  } catch (_) {
    // Gracefully continue when the browser denies persistent storage.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 2</span>
      <span class="badge">Confidence Intervals</span>
      <span class="badge">Paired Data</span>
    </div>

    <h1>Confidence Interval for a Paired Mean Difference</h1>

    <p class="lead">
      Not all comparisons involve independent groups.
    </p>

    <p class="lead">
      Many studies collect paired observations, where measurements naturally belong together. In these situations, inference focuses on the differences within pairs rather than comparing two separate groups.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-difference-of-proportions/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/width-and-precision-what-controls/">
         Next: Width and Precision — What Controls Them? →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is Paired Data?</h2>

    <p>
      Paired data arise when observations are naturally linked.
    </p>

    <div class="example-box">

      <p>
        Before-treatment and after-treatment measurements
      </p>

      <p>
        Weight before and after a diet program
      </p>

      <p>
        Blood pressure before and after medication
      </p>

      <p>
        Matched twins receiving different treatments
      </p>

    </div>

    <p>
      Each pair represents two measurements connected to the same subject or matched unit.
    </p>

    <h2>Why Independent Methods Fail</h2>

    <p>
      Paired observations are not independent.
    </p>

    <p>
      Measurements from the same person are usually related.
    </p>

    <p>
      Treating paired data as independent ignores this relationship and can produce incorrect uncertainty estimates.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The pair is the unit of analysis, not the individual measurements.
      </p>

    </div>

    <h2>The Main Strategy</h2>

    <p>
      Instead of analyzing two variables separately,
      we convert each pair into a single difference.
    </p>

    <p>
      For each subject:
    </p>

    
    \[
    d_i=\text{after}_i-\text{before}_i
    \]


    <p>
      The analysis then proceeds using these differences.
    </p>

    <h2>The Parameter of Interest</h2>

    <p>
      Let:
    </p>

    
    \[
    \mu_d=\operatorname{E}(D)
    \]


    <p>
      denote the population mean difference.
    </p>

    <p>
      This parameter represents the average change across all paired observations.
    </p>

    <h2>The Estimator</h2>

    <p>
      The sample estimate is:
    </p>

    
    \[
    \bar d=\frac{1}{n}\sum_{i=1}^{n}d_i
    \]


    <p>
      the average of the observed differences.
    </p>

    <h2>Example Data</h2>

    <p>
      Suppose five individuals participate in a fitness program.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Person</th>
            <th>Before</th>
            <th>After</th>
            <th>Difference</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>1</td>
            <td>180</td>
            <td>172</td>
            <td>-8</td>
          </tr>

          <tr>
            <td>2</td>
            <td>165</td>
            <td>160</td>
            <td>-5</td>
          </tr>

          <tr>
            <td>3</td>
            <td>190</td>
            <td>182</td>
            <td>-8</td>
          </tr>

          <tr>
            <td>4</td>
            <td>175</td>
            <td>169</td>
            <td>-6</td>
          </tr>

          <tr>
            <td>5</td>
            <td>200</td>
            <td>191</td>
            <td>-9</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The confidence interval will be built from the differences:
    </p>

    <div class="example-box">

      <p>
        -8, -5, -8, -6, -9
      </p>

    </div>

    <h2>The Standard Error</h2>

    <p>
      Once differences are computed,
      the problem becomes a one-sample mean problem.
    </p>

    <p>
      The estimated standard error is:
    </p>

    
    \[
    \widehat{\operatorname{SE}}(\bar d)=\frac{s_d}{\sqrt n}
    \]


    <p>
      where:
    </p>

    <ul class="bullets">

      <li>s<sub>d</sub> = sample standard deviation of the differences</li>

      <li>n = number of pairs</li>

    </ul>

    <h2>The Confidence Interval Formula</h2>

    <p>
      Since population variability is usually unknown,
      a t interval is used:
    </p>

    
    \[
    \bar d\pm t_{1-\alpha/2,\,n-1}\frac{s_d}{\sqrt n}
    \]


    <p>
      This is the standard confidence interval for a paired mean difference.
    </p>

    <h2>Degrees of Freedom</h2>

    <p>
      As with a one-sample t interval:
    </p>

    
    \[
    \nu=n-1
    \]


    <p>
      where n refers to the number of pairs.
    </p>

    <h2>Example Setup</h2>

    <p>
      The following summary-data example is separate from the five-person table above; its mean difference, standard deviation, and sample size are not calculated from those five observations.
    </p>
    <p>
      Suppose a study produces:
    </p>

    <div class="example-box">

      <p>
        Mean difference = -4.5
      </p>

      <p>
        Standard deviation of differences = 8
      </p>

      <p>
        Number of pairs = 36
      </p>

      <p>
        Confidence level = 95%
      </p>

    </div>

    <h2>Step 1: Compute the Standard Error</h2>

    <p>
      Using:
    </p>

    
    \[
    \widehat{\operatorname{SE}}=\frac{8}{\sqrt{36}}
    \]


    <p>
      gives:
    </p>

    
    \[
    \widehat{\operatorname{SE}}=\frac{8}{6}\approx1.3333
    \]


    <h2>Step 2: Find the Critical Value</h2>

    <p>
      Degrees of freedom:
    </p>

    
    \[
    \nu=36-1=35
    \]


    <p>
      For 95% confidence:
    </p>

    <div class="example-box">

      <p>
        t* ≈ 2.03
      </p>

    </div>

    <h2>Step 3: Compute the Margin of Error</h2>

    <p>
      Margin of error:
    </p>

    
    \[
    \text{Margin of error}\approx 2.03(1.3333)\approx2.71
    \]


    <h2>Step 4: Construct the Interval</h2>

    <p>
      Therefore:
    </p>

    
    \[
    -4.5\pm2.71\approx(-7.21,\,-1.79)
    \]


    <p>
      yielding:
    </p>

    <div class="example-box">

      <p>
        (-7.21, -1.79)
      </p>

    </div>

    <h2>Interpreting the Interval</h2>

    <p>
      Plausible values for the average population change lie between:
    </p>

    <div class="example-box">

      <p>
        -7.21 and -1.79
      </p>

    </div>

    <p>
      The negative values suggest the treatment tends to reduce the measured outcome.
    </p>

    <h2>The Importance of Zero</h2>

    <p>
      As with other difference intervals,
      zero has special meaning.
    </p>

    <div class="concept-box">

      <strong>Zero difference:</strong>

      <p>
        A mean difference of zero indicates no average change.
      </p>

    </div>

    <h2>When Zero Is Not in the Interval</h2>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        (-7.21, -1.79)
      </p>

    </div>

    <p>
      Since zero is not contained in the interval,
      the data suggest a real average change may exist.
    </p>

    <h2>When Zero Is in the Interval</h2>

    <p>
      Suppose instead:
    </p>

    <div class="example-box">

      <p>
        (-3, 2)
      </p>

    </div>

    <p>
      Since zero lies inside the interval,
      no change remains a plausible possibility.
    </p>

    <h2>Advantages of Pairing</h2>

    <p>
      Pairing often reduces variability because each subject acts as their own control.
    </p>

    <p>
      This can produce:
    </p>

    <ul class="bullets">

      <li>Smaller standard errors</li>

      <li>Narrower confidence intervals</li>

      <li>Greater statistical precision</li>

    </ul>


    <!-- INTERACTIVE PAIRED VS INDEPENDENT STANDARD ERROR EXPLORER -->
    <section class="section" id="esa-ci-design-explorer" aria-labelledby="esa-ci-design-heading">
      <h2 id="esa-ci-design-heading">Explore Paired versus Independent Standard Errors</h2>
      <p>Compare the standard error of two independent sample means (n observations per group)
        with the standard error of n matched within-pair differences. Both measurements
        have the same marginal standard deviations in the comparison; only the pairing
        correlation changes.</p>
      <div class="concept-box esa-ci-design-card">
        <div class="esa-ci-design-fields">
          <div><label for="esa-ci-sigma-a"><strong>Standard deviation of measurement A</strong></label>
            <input id="esa-ci-sigma-a" type="number" min="0.01" max="100000" step="any" value="10"></div>
          <div><label for="esa-ci-sigma-b"><strong>Standard deviation of measurement B</strong></label>
            <input id="esa-ci-sigma-b" type="number" min="0.01" max="100000" step="any" value="10"></div>
          <div><label for="esa-ci-n"><strong>Number of pairs / observations per group</strong></label>
            <input id="esa-ci-n" type="number" min="2" max="10000" step="1" value="25"></div>
          <div><label for="esa-ci-rho"><strong>Within-pair correlation (ρ): <output id="esa-ci-rho-value" for="esa-ci-rho">0.70</output></strong></label>
            <input id="esa-ci-rho" type="range" min="-0.9" max="0.9" step="0.1" value="0.7"></div>
        </div>
        <p id="esa-ci-design-error" role="alert" hidden></p>
        <div class="esa-ci-design-results" role="status" aria-live="polite">
          <p><strong>Independent-group standard error:</strong> <output id="esa-ci-independent-se">2.8284</output></p>
          <p><strong>Paired-difference standard error:</strong> <output id="esa-ci-paired-se">1.5492</output></p>
          <p><strong>Paired SE / Independent SE:</strong> <output id="esa-ci-se-ratio">0.5477</output></p>
          <p id="esa-ci-design-interpretation">Positive within-pair correlation reduces the paired standard error.</p>
        </div>
        <button class="btn btn-outline" id="esa-ci-design-reset" type="button">Reset example</button>
        <p class="muted-mini">These are estimated standard-error illustrations—not complete t confidence intervals.
          The independent case assumes independence within and between groups. The paired case assumes
          independence across pairs, meaningful matched measurements, and common within-pair correlation.
          Actual CI widths also depend on critical values and degrees of freedom.
          Pairing does not always improve precision.</p>
      </div>
    </section>
    <style>
      #esa-ci-design-explorer, #esa-ci-design-explorer .esa-ci-design-card {min-width:0;max-width:100%;overflow-wrap:anywhere}
      #esa-ci-design-explorer .esa-ci-design-fields {display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:14px}
      #esa-ci-design-explorer label {display:block;margin-bottom:7px}
      #esa-ci-design-explorer input {display:block;box-sizing:border-box;width:100%;max-width:100%;min-width:0;padding:9px;margin:0}
      #esa-ci-design-explorer input[type="range"] {padding:0;cursor:pointer}
      #esa-ci-design-explorer .esa-ci-design-results {margin:12px 0}
      #esa-ci-design-explorer .esa-ci-design-results p {margin:6px 0}
      #esa-ci-design-explorer #esa-ci-design-error {color:#b42318}
      #esa-ci-design-explorer [hidden] {display:none!important}
    </style>
    <script>
    (function () {
      "use strict";
      const root=document.getElementById("esa-ci-design-explorer");
      if (!root) return;
      const field=id=>root.querySelector("#"+id);
      const sigmaA=field("esa-ci-sigma-a"), sigmaB=field("esa-ci-sigma-b"),
            n=field("esa-ci-n"), rho=field("esa-ci-rho");
      const error=field("esa-ci-design-error");
      const outputs=["esa-ci-independent-se","esa-ci-paired-se","esa-ci-se-ratio"].map(field);
      function update() {
        const a=Number(sigmaA.value),b=Number(sigmaB.value),
              m=Number(n.value),c=Number(rho.value);
        field("esa-ci-rho-value").textContent=c.toFixed(2);
        const valid=sigmaA.value.trim()!=="" && sigmaB.value.trim()!=="" && n.value.trim()!=="" &&
          Number.isFinite(a) && a>0 && a<=100000 &&
          Number.isFinite(b) && b>0 && b<=100000 &&
          Number.isInteger(m) && m>=2 && m<=10000 &&
          Number.isFinite(c) && c>=-1 && c<=1;
        if (!valid) {
          error.textContent="Enter positive standard deviations no greater than 100,000 and an integer sample size from 2 to 10,000.";
          error.hidden=false;
          outputs.forEach(node=>node.textContent="—");
          field("esa-ci-design-interpretation").textContent="Correct the input values to see valid standard errors.";
          return;
        }
        error.hidden=true;error.textContent="";
        const vi=(a*a+b*b)/m;
        const vp=Math.max(0,a*a+b*b-2*c*a*b)/m;
        const sei=Math.sqrt(vi),sep=Math.sqrt(vp);
        outputs[0].textContent=sei.toFixed(4);
        outputs[1].textContent=sep.toFixed(4);
        outputs[2].textContent=(sep/sei).toFixed(4);
        field("esa-ci-design-interpretation").textContent=
          c>0.000001?"Positive within-pair correlation reduces the paired standard error.":
          c< -0.000001?"Negative within-pair correlation increases the paired standard error.":
          "At zero correlation, the standard errors agree under these equal-size assumptions.";
      }
      [sigmaA,sigmaB,n,rho].forEach(input=>input.addEventListener("input",update));
      field("esa-ci-design-reset").addEventListener("click",()=>{
        sigmaA.value="10";sigmaB.value="10";n.value="25";rho.value="0.7";update();
      });
      update();
    })();
    </script>

    <h2>Conditions for the Interval</h2>

    <ul class="bullets">

      <li>Pairs are randomly selected or randomly assigned</li>

      <li>Differences are independent across pairs</li>

      <li>The distribution of differences is approximately normal, or the sample size is large enough for the CLT</li>

    </ul>

    <p>
      Notice that we check assumptions on the differences, not on the original measurements.
    </p>

    <h2>Independent vs Paired Designs</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Design</th>
            <th>Analyzes</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Independent Samples</td>
            <td>Difference between group means</td>
          </tr>

          <tr>
            <td>Paired Samples</td>
            <td>Mean of paired differences</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The formulas differ because the study designs differ.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        For paired data, inference is performed on the differences within pairs. A paired confidence interval is simply a one-sample t interval applied to those differences.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      We have now seen several confidence interval formulas.
    </p>

    <p>
      A natural question remains:
    </p>

    <div class="example-box">

      <p>
        Why are some intervals wide while others are narrow?
      </p>

    </div>

    <p>
      The next lesson examines the factors that control confidence interval width and statistical precision.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Paired observations are naturally linked measurements</li>

        <li>Inference focuses on differences within pairs</li>

        <li>The parameter of interest is μ<sub>d</sub></li>

        <li>The estimator is d̄</li>

        <li>The interval formula is d̄ ± t*SE</li>

        <li>Zero represents no average change</li>

        <li>Pairing often improves precision by reducing variability</li>

        <li>A paired interval is fundamentally a one-sample t interval applied to differences</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/ci-for-difference-of-proportions/">
         ← Previous: CI for Difference of Proportions
      </a>

      <a class="btn"
         href="/inference/confidence-intervals/width-and-precision-what-controls/">
         Next: Width and Precision — What Controls Them? →
      </a>

    </div>

  </div>

</section>