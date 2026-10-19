---
layout: default
title: Boxplots
description: Learn how boxplots summarize distributions using the five-number summary and help identify spread, skewness, and outliers.
permalink: /descriptive/visualization/boxplots/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_visualization_lesson_v0";

  try {
  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/visualization/boxplots/",
    label: "Boxplots",
    ts: Date.now()
  }));
  } catch (_) {
    // A blocked browser storage API must not interrupt this lesson.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 3</span>
      <span class="badge">Visualization</span>
      <span class="badge">Numerical Data</span>
    </div>

    <h1>Boxplots</h1>

    <p class="lead">
      Histograms show the overall shape of a distribution.
    </p>

    <p class="lead">
      Boxplots provide a compact summary of a distribution using only a few key numbers.
      They are especially useful for comparing groups,
      detecting outliers,
      and understanding the spread of data.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/visualization/density-curves/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/visualization/scatterplots/">
         Next: Scatterplots →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is a Boxplot?</h2>

    <p>
      A <strong>boxplot</strong>
      (also called a box-and-whisker plot)
      is a graphical summary of a numerical distribution.
    </p>

    <p>
      Rather than displaying every observation,
      it summarizes the data using key descriptive statistics.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        A boxplot compresses an entire distribution into a small visual summary.
      </p>

    </div>

    <div class="concept-box">

  <strong>Important insight:</strong>

  <p>
    Boxplots summarize distributions using only a few numbers,
    making them much more compact than histograms.
  </p>

</div>

<img src="{{ 'descriptive/images/boxplot-anatomy.png' | relative_url }}"
     alt="Anatomy of a boxplot"
     style="margin-top:15px; max-width:100%; height:auto;">

    <h2>The Five-Number Summary</h2>

    <p>
      Boxplots are built from the
      <strong>five-number summary</strong>.
    </p>

    <p>
      These values describe the location and spread of the data.
    </p>

    <p>
  Because quartiles divide the data into four equal parts,
  the interval from Q1 to Q3 always contains the middle 50%
  of observations.
</p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Statistic</th>
            <th>Description</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Minimum</td>
            <td>Smallest observation</td>
          </tr>

          <tr>
            <td>Q1</td>
            <td>First quartile (25th percentile)</td>
          </tr>

          <tr>
            <td>Median</td>
            <td>50th percentile</td>
          </tr>

          <tr>
            <td>Q3</td>
            <td>Third quartile (75th percentile)</td>
          </tr>

          <tr>
            <td>Maximum</td>
            <td>Largest observation</td>
          </tr>

        </tbody>

      </table>

    </div>

    <img src="{{ 'descriptive/images/five-number-summary-boxplot.png' | relative_url }}"
     alt="Five-number summary visualized with a boxplot"
     style="margin-top:15px; max-width:100%; height:auto;">

    <h2>Understanding Quartiles</h2>

    <p>
      Quartiles divide ordered data into four equal parts.
    </p>

    <ul class="bullets">

      <li>25% of observations fall below Q1</li>

      <li>50% fall below the median</li>

      <li>75% fall below Q3</li>

    </ul>

    <p>
      These values help describe where observations are concentrated.
    </p>

    <p>
  Because quartiles divide the data into four equal parts,
  the interval from Q1 to Q3 always contains the middle 50%
  of observations.
</p>

    <h2>A Numerical Example</h2>

    <p>
      Consider the ordered dataset:
    </p>

    <div class="example-box">

      <p>
        5, 7, 8, 10, 12, 13, 15, 17, 20
      </p>

    </div>

    <p>
      The five-number summary is:
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Minimum</th>
            <th>Q1</th>
            <th>Median</th>
            <th>Q3</th>
            <th>Maximum</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>5</td>
            <td>7.5</td>
            <td>12</td>
            <td>16</td>
            <td>20</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      A boxplot visualizes these five values.
    </p>


    <section class="example-box" id="esa-boxplot-lab" aria-labelledby="esa-boxplot-title">
      <h2 id="esa-boxplot-title">Interactive Boxplot and Outlier Explorer</h2>
      <p>Enter 4 to 60 numerical observations separated by commas, spaces or line breaks.
         Quartiles use the <strong>median of each half, excluding the overall median for odd n</strong>.
         Whiskers reach the most extreme observations inside the 1.5 × IQR fences;
         flagged values are plotted individually.</p>
      <label for="esa-boxplot-data"><strong>Observed data</strong></label>
      <textarea id="esa-boxplot-data" rows="3" style="box-sizing:border-box;width:100%;max-width:590px;font:inherit"
                spellcheck="false">5, 7, 8, 10, 12, 13, 15, 17, 20</textarea>
      <p id="esa-boxplot-error" role="alert" hidden></p>
      <svg id="esa-boxplot-figure" role="img" aria-label="Boxplot showing quartiles, whiskers, and outliers"
           viewBox="0 0 500 180" style="display:block;width:100%;max-width:590px;height:auto">
        <line x1="35" x2="465" y1="143" y2="143" stroke="currentColor"></line>
        <g id="esa-boxplot-marks"></g>
        <text x="35" y="165" fill="currentColor" font-size="12">Minimum</text>
        <text x="465" y="165" text-anchor="end" fill="currentColor" font-size="12">Maximum</text>
      </svg>
      <div role="status" aria-live="polite" aria-atomic="true">
        <p>n = <output id="esa-boxplot-n">9</output>;
           min = <output id="esa-boxplot-min">5</output>;
           Q1 = <output id="esa-boxplot-q1">7.5</output>;
           median = <output id="esa-boxplot-median">12</output>;
           Q3 = <output id="esa-boxplot-q3">16</output>;
           max = <output id="esa-boxplot-max">20</output>.</p>
        <p>IQR = <output id="esa-boxplot-iqr">8.5</output>;
           lower/upper fences = <output id="esa-boxplot-fences">−5.25 / 28.75</output>.</p>
        <p>Whisker endpoints = <output id="esa-boxplot-whiskers">5 / 20</output>;
           flagged outliers = <output id="esa-boxplot-outliers">none</output>.</p>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:10px">
        <button id="esa-boxplot-reset" type="button" class="btn btn-outline">Reset example</button>
        <button id="esa-boxplot-extreme" type="button" class="btn btn-outline">Add extreme observation (120)</button>
      </div>
      <p class="muted-mini">Tukey-style fences flag potentially unusual observations; they
         do not prove mistakes or justify automatic removal. Quartile conventions vary by
         software; this lesson's example gives Q1 = 7.5 and Q3 = 16 for the nine values above.
         These whiskers are <em>not</em> necessarily the overall minimum and maximum.</p>
    </section>
    <script>
    (() => {
      "use strict";
      const root=document.getElementById("esa-boxplot-lab");if(!root)return;
      const get=id=>root.querySelector("#esa-boxplot-"+id),data=get("data");
      const ns="http://www.w3.org/2000/svg";
      const make=(name,atts)=>{
        const e=document.createElementNS(ns,name);
        Object.entries(atts).forEach(([k,v])=>e.setAttribute(k,String(v)));
        return e;
      };
      const median=a=>a.length%2?a[(a.length-1)/2]:
        (a[a.length/2-1]+a[a.length/2])/2;
      const fmt=v=>Number.isInteger(v)?String(v):Number(v.toFixed(6)).toString();
      function invalid(msg){
        get("error").hidden=false;get("error").textContent=msg;
        get("figure").setAttribute("hidden","");
        for(const id of ["n","min","q1","median","q3","max","iqr","fences","whiskers","outliers"])
          get(id).textContent="—";
      }
      function render(){
        const input=data.value.trim();
        const fields=input.split(/[\s,;]+/).filter(Boolean);
        const values=fields.map(v=>Number(v));
        if(fields.length<4||fields.length>60||fields.some(v=>v==="")||
           values.some(v=>!Number.isFinite(v)||Math.abs(v)>1000000)){
          invalid("Enter 4 to 60 finite numerical values (absolute value at most 1,000,000).");
          return;
        }
        values.sort((a,b)=>a-b);
        const n=values.length,k=Math.floor(n/2);
        const low=values.slice(0,k),high=values.slice(n-k);
        const q1=median(low),q2=median(values),q3=median(high);
        const iqr=q3-q1,lower=q1-1.5*iqr,upper=q3+1.5*iqr;
        const inside=values.filter(v=>v>=lower-1e-10&&v<=upper+1e-10);
        if(!inside.length){invalid("There are no valid whisker endpoints.");return}
        const outliers=values.filter(v=>v<lower-1e-10||v>upper+1e-10);
        const vmin=values[0],vmax=values[n-1],wlo=inside[0],whi=inside[inside.length-1];
        get("error").hidden=true;get("error").textContent="";
        get("figure").removeAttribute("hidden");
        const list={n,min:vmin,q1,median:q2,q3,max:vmax,iqr,
          fences:fmt(lower)+" / "+fmt(upper),whiskers:fmt(wlo)+" / "+fmt(whi),
          outliers:outliers.length?outliers.map(fmt).join(", "):"none"};
        for(const [key,val] of Object.entries(list))
          get(key).textContent=typeof val==="number"?fmt(val):String(val);
        const delta=vmax-vmin;
        const margin=delta>0?delta*0.1:1;
        const x=v=>35+430*(v-(vmin-margin))/(delta+2*margin);
        const line=(x1,y1,x2,y2,width=2)=>make("line",{x1,y1,x2,y2,stroke:"#0d9488","stroke-width":width});
        const parts=[
          line(x(wlo),75,x(q1),75),line(x(q3),75,x(whi),75),
          line(x(wlo),57,x(wlo),93),line(x(whi),57,x(whi),93),
          make("rect",{x:x(q1),y:48,width:Math.max(0.8,x(q3)-x(q1)),height:54,
            stroke:"#0d9488","stroke-width":2,fill:"#0d9488","fill-opacity":0.18}),
          line(x(q2),48,x(q2),102,3)
        ];
        outliers.forEach((v,i)=>parts.push(make("circle",{
          cx:x(v),cy:75+(i%3-1)*6,r:5,fill:"#b45309",stroke:"currentColor","stroke-width":0.6
        })));
        get("marks").replaceChildren(...parts);
        get("figure").setAttribute("aria-label","Boxplot of "+n+" values. Q1 "+fmt(q1)+
          ", median "+fmt(q2)+", Q3 "+fmt(q3)+", whiskers "+fmt(wlo)+" to "+fmt(whi)+
          ", "+outliers.length+" flagged outliers.");
      }
      data.addEventListener("input",render);
      get("reset").addEventListener("click",()=>{
        data.value="5, 7, 8, 10, 12, 13, 15, 17, 20";render();
      });
      get("extreme").addEventListener("click",()=>{
        const parts=data.value.trim().split(/[\s,;]+/).filter(Boolean);
        if(parts.length>=60){invalid("Maximum 60 observations; remove one before adding.");return;}
        data.value=data.value.trim().replace(/[,\s;]+$/,"")+", 120";render();
      });
      render();
    })();
    </script>
    <style>
      #esa-boxplot-lab[hidden],#esa-boxplot-lab [hidden]{display:none!important}
      #esa-boxplot-lab button{max-width:100%;white-space:normal}
      #esa-boxplot-lab p{overflow-wrap:anywhere}
      @media print{#esa-boxplot-lab textarea,#esa-boxplot-lab button{display:none}}
    </style>

    <h2>The Box</h2>

    <p>
      The box itself extends from:
    </p>

    <ul class="bullets">

      <li>Q1 (left side)</li>

      <li>Q3 (right side)</li>

    </ul>

    <p>
      This region contains the middle 50% of observations.
    </p>

    <p>
      The width of the box reflects the spread of the central portion of the data.
    </p>

    <h2>The Median Line</h2>

    <p>
      A line inside the box marks the median.
    </p>

    <p>
      This line divides the data into two equal halves.
    </p>

    <p>
      Its position can reveal asymmetry in the distribution.
    </p>

    <h2>The Whiskers</h2>

    <p>
      Lines extending from the box are called whiskers.
    </p>

    <p>
      They connect the box to observations outside the middle 50%.
    </p>

    <p>
      Whiskers help show the overall range of the data.
    </p>

    <p>
  In many boxplots, whiskers extend only to the most extreme
  non-outlier observations rather than to the absolute minimum
  and maximum values.
</p>

    <h2>The Interquartile Range (IQR)</h2>

    <p>
      One of the most important measures in a boxplot is the
      <strong>interquartile range</strong>.
    </p>

    <p>
  The IQR measures the distance between the first and third quartiles,
  capturing the spread of the middle 50% of observations.
</p>

    <p>
      The IQR measures the spread of the middle 50% of observations.
    </p>

    <p>
      It is resistant to extreme values and widely used in statistics.
    </p>

    <h2>Detecting Outliers</h2>

    <img src="{{ 'descriptive/images/boxplot-outlier-example.png' | relative_url }}"
     alt="Boxplot showing an outlier"
     style="margin-top:15px; max-width:100%; height:auto;">

    <p>
      Boxplots are famous for identifying outliers.
    </p>

    <p>
      A common rule classifies observations as potential outliers if they lie beyond:
    </p>

    <p>
  Observations outside these boundaries are commonly flagged
  as potential outliers.
</p>

    <p>
      Such observations are often displayed as individual points.
    </p>

    <h2>What Boxplots Reveal</h2>

    <p>
      Boxplots provide information about:
    </p>

    <ul class="bullets">

      <li>Center</li>

      <li>Spread</li>

      <li>Skewness</li>

      <li>Outliers</li>

      <li>Variability</li>

    </ul>

    <p>
      All of this information is displayed in a compact form.
    </p>

    <h2>Recognizing Skewness</h2>

    <img src="{{ 'descriptive/images/symmetric-vs-skewed-boxplots.png' | relative_url }}"
     alt="Symmetric and skewed boxplots"
     style="margin-top:15px; max-width:100%; height:auto;">

    <p>
      A boxplot may suggest skewness when:
    </p>

    <ul class="bullets">

      <li>The median is not centered within the box</li>

      <li>One whisker is noticeably longer than the other</li>

      <li>Outliers appear mainly on one side</li>

    </ul>

    <p>
      These features help identify asymmetric distributions.
    </p>

    <h2>Comparing Groups</h2>

    <img src="{{ 'descriptive/images/group-comparison-boxplots.png' | relative_url }}"
     alt="Comparing groups using boxplots"
     style="margin-top:15px; max-width:100%; height:auto;">

    <p>
      One of the greatest strengths of boxplots
      is comparing multiple distributions simultaneously.
    </p>

    <p>
      Example applications:
    </p>

    <ul class="bullets">

      <li>Exam scores across classrooms</li>

      <li>Income across regions</li>

      <li>Recovery times across treatments</li>

      <li>Sales across stores</li>

    </ul>

    <p>
      Multiple boxplots can reveal differences quickly.
    </p>

    <p>
  Comparing several boxplots side by side is often easier
  than comparing several histograms.
</p>

    <h2>Boxplots vs Histograms</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Boxplot</th>
            <th>Histogram</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Compact summary</td>
            <td>Detailed shape</td>
          </tr>

          <tr>
            <td>Five-number summary</td>
            <td>Distribution frequencies</td>
          </tr>

          <tr>
            <td>Good for comparisons</td>
            <td>Good for shape analysis</td>
          </tr>

          <tr>
            <td>Highlights outliers</td>
            <td>Shows clusters and peaks</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The two graphs complement one another.
    </p>

    <h2>Histograms and Boxplots Together</h2>

    <img src="{{ 'descriptive/images/histogram-vs-boxplot.png' | relative_url }}"
     alt="Histogram and boxplot comparison"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
  Analysts often examine both a histogram and a boxplot
  for the same dataset.
</p>

<p>
  The histogram reveals detailed shape,
  while the boxplot provides a compact summary.
</p>

    <h2>Limitations of Boxplots</h2>

    <p>
      Boxplots do not show every feature of a distribution.
    </p>

    <p>
      For example,
      they may hide:
    </p>

    <ul class="bullets">

      <li>Multiple peaks</li>

      <li>Detailed distribution shape</li>

      <li>Small clusters</li>

    </ul>

    <p>
      Histograms often provide more detail,
      while boxplots provide greater simplicity.
    </p>

    <h2>Why Boxplots Are Important</h2>

    <p>
      Boxplots are widely used because they:
    </p>

    <ul class="bullets">

      <li>Summarize data efficiently</li>

      <li>Handle large datasets well</li>

      <li>Support group comparisons</li>

      <li>Highlight outliers</li>

      <li>Connect directly to descriptive statistics</li>

    </ul>

    <p>
      They are a standard tool throughout statistics and data science.
    </p>

    <div class="concept-box">

  <strong>Key insight:</strong>

  <p>
    Boxplots summarize center, spread, and potential outliers
    in a compact visual form, making them especially useful
    for comparing groups.
  </p>

</div>

<h2>Creating Boxplots in SPSS</h2>

<ul class="bullets">

  <li>Graphs → Chart Builder</li>

  <li>Select Boxplot</li>

  <li>Assign the numerical variable</li>

  <li>SPSS automatically identifies potential outliers</li>

</ul>

<div style="flex:1; min-width:300px;">
    <img src="{{ '/descriptive/images/spss_boxplot_output.png' | relative_url }}"
         alt="SPSS boxplot output"
         style="width:100%; height:auto;">
    <p style="text-align:center;">
      Boxplot showing spread and potential outlier
    </p>
  </div>

<p>
  Boxplots are commonly used as an initial screening tool
  during exploratory data analysis.
</p>

<h3>Python Example</h3>

<p>
This example creates a boxplot for numerical data.
</p>

<pre><code>import matplotlib.pyplot as plt

scores = [55,58,60,62,65,67,68,70,
          72,74,75,77,80,82,85,
          88,90,92,95,120]

plt.boxplot(scores)

plt.show()
</code></pre>

<h3>R Example</h3>

<p>
This example creates a boxplot for numerical data.
</p>

<pre><code>scores <- c(55,58,60,62,65,67,68,70,
            72,74,75,77,80,82,85,
            88,90,92,95,120)

boxplot(scores)
</code></pre>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Boxplots summarize distributions using the five-number summary</li>

        <li>The box contains the middle 50% of observations</li>

        <li>The median is displayed inside the box</li>

        <li>The interquartile range measures central spread</li>

        <li>Boxplots are useful for identifying outliers</li>

        <li>They are excellent for comparing multiple groups</li>

        <li>Boxplots complement histograms rather than replace them</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/visualization/density-curves/">
         ← Previous: Density Curves
      </a>

      <a class="btn"
         href="/descriptive/visualization/scatterplots/">
         Next: Scatterplots →
      </a>

    </div>

  </div>

</section>
