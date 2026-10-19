---
layout: default
title: Histograms
description: Learn how histograms display the distribution of numerical data and reveal shape, center, spread, gaps, clusters, and outliers.
permalink: /descriptive/visualization/histograms/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_visualization_lesson_v0";

  try {
  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/visualization/histograms/",
    label: "Histograms",
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
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 3</span>
      <span class="badge">Visualization</span>
      <span class="badge">Numerical Data</span>
    </div>

    <h1>Histograms</h1>

    <p class="lead">
      Histograms are one of the most important tools for understanding numerical data.
    </p>

    <p class="lead">
      Unlike bar charts, which compare categories,
      histograms reveal the shape of a distribution,
      helping us understand where observations occur,
      how spread out they are,
      and whether unusual patterns exist.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/visualization/pie-charts/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/visualization/density-curves/">
         Next: Density Curves →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is a Histogram?</h2>

    <p>
      A <strong>histogram</strong>
      is a graph used to display the distribution of numerical data.
    </p>

    <p>
      Instead of showing individual values,
      observations are grouped into intervals called
      <strong>bins</strong> or <strong>classes</strong>.
    </p>

    <p>
      The height of each bar represents the frequency
      of observations within that interval.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Histograms show how numerical values are distributed across intervals.
      </p>

      <p>
  Although histograms use bars, they are fundamentally different from bar charts.
  Histograms display distributions of numerical values,
  whereas bar charts compare categories.
</p>

    </div>

    <div class="concept-box">

  <strong>Important insight:</strong>

  <p>
    Many important characteristics of data become visible in a histogram
    before any numerical summary is calculated.
  </p>

</div>

    <h2>Why Histograms Matter</h2>

    <p>
      Looking at raw numerical values can be overwhelming.
    </p>

    <p>
      A histogram summarizes hundreds or thousands of observations
      into a visual representation of the distribution.
    </p>

    <p>
      This allows us to see:
    </p>

    <ul class="bullets">

      <li>Where most observations occur</li>

      <li>How spread out values are</li>

      <li>Whether multiple peaks exist</li>

      <li>Whether outliers are present</li>

      <li>Whether the distribution is symmetric or skewed</li>

    </ul>

    <h2>Example: Exam Scores</h2>

    <p>
      Suppose exam scores are grouped into intervals:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Score Range</th>
            <th>Frequency</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>40–49</td>
            <td>2</td>
          </tr>

          <tr>
            <td>50–59</td>
            <td>5</td>
          </tr>

          <tr>
            <td>60–69</td>
            <td>10</td>
          </tr>

          <tr>
            <td>70–79</td>
            <td>15</td>
          </tr>

          <tr>
            <td>80–89</td>
            <td>12</td>
          </tr>

          <tr>
            <td>90–99</td>
            <td>6</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      A histogram would transform this table into a visual display
      of the score distribution.
    </p>

    <h2>Histogram Example</h2>

    <img src="{{ 'descriptive/images/exam-scores-histogram.png' | relative_url }}"
     alt="Histogram of exam scores"
     style="margin-top:15px; max-width:100%; height:auto;">

    <p>
      The tallest bar identifies the interval containing the largest number of observations.
    </p>

    <h2>Histograms Are Different from Bar Charts</h2>

    <p>
      Histograms and bar charts may look similar,
      but they serve different purposes.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Histogram</th>
            <th>Bar Chart</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Numerical data</td>
            <td>Categorical data</td>
          </tr>

          <tr>
            <td>Distribution shape</td>
            <td>Category comparison</td>
          </tr>

          <tr>
            <td>Intervals (bins)</td>
            <td>Categories</td>
          </tr>

          <tr>
            <td>Bars touch</td>
            <td>Bars separated</td>
          </tr>

        </tbody>

      </table>

    </div>

    <img src="{{ 'descriptive/images/histogram-vs-bar-chart.png' | relative_url }}"
     alt="Histogram compared with bar chart"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Although both use bars, histograms display numerical distributions while bar charts compare categories.
</p>

    <h2>Understanding Bins</h2>

    <p>
      Histograms group nearby values together.
    </p>

    <p>
      These groups are called bins.
    </p>

    <p>
      Example:
    </p>

    <ul class="bullets">

      <li>0–9</li>

      <li>10–19</li>

      <li>20–29</li>

      <li>30–39</li>

    </ul>

    <p>
      Choosing bin widths is an important part of histogram construction.
    </p>

    <p>
  Different bin widths can produce very different-looking histograms,
  even when the underlying data remain unchanged.
</p>


    <!-- Interactive Histogram Bin-Width Explorer -->
    <section id="esa-histogram-lab" class="example-box" aria-labelledby="esa-histogram-title">
      <h2 id="esa-histogram-title">Interactive Histogram and Bin-Width Explorer</h2>
      <p>These raw scores are an independent illustrative dataset, <strong>not reconstructed</strong> from the preceding grouped frequency table. Change the bin count to compare different summaries of the same data.</p>
      <label for="esa-histogram-data"><strong>Raw numerical observations</strong> (comma-separated)</label>
      <textarea id="esa-histogram-data" spellcheck="false" rows="3">42, 48, 54, 56, 59, 61, 62, 63, 67, 69, 70, 72, 73, 75, 78, 79, 82, 84, 87, 93</textarea>
      <div class="esa-histogram-controls">
        <label>Number of bins <input id="esa-histogram-bins" type="number" min="2" max="12" step="1" value="5"></label>
        <button type="button" class="btn btn-outline" id="esa-histogram-reset">Reset histogram example</button>
      </div>
      <p role="alert" id="esa-histogram-error" hidden></p>
      <svg id="esa-histogram-chart" viewBox="0 0 460 270" width="460" height="270"
           role="img" aria-label="Equal-width histogram with twenty numerical observations">
        <line x1="45" y1="218" x2="425" y2="218" stroke="currentColor"></line>
        <line x1="45" y1="218" x2="45" y2="22" stroke="currentColor"></line>
        <text x="20" y="22" fill="currentColor" font-size="12">n</text>
        <text x="425" y="261" text-anchor="end" fill="currentColor" font-size="12">Score</text>
        <g id="esa-histogram-bars"></g>
      </svg>
      <div role="status" aria-live="polite" aria-atomic="true">
        <p>Observation count: <output id="esa-histogram-n">20</output>.
          Bin width: <output id="esa-histogram-width">10.2000</output>.
          Total bin frequency: <output id="esa-histogram-sum">20</output>.</p>
      </div>
      <div class="table-wrap">
        <table>
          <caption>Bin intervals and counts</caption>
          <thead><tr><th scope="col">Numerical interval</th><th scope="col">Frequency</th></tr></thead>
          <tbody id="esa-histogram-frequency-table"></tbody>
        </table>
      </div>
      <p class="muted-mini">All bins have equal widths. Each interval is left-inclusive and right-exclusive, except the final interval, which also includes the sample maximum. Identical observations are displayed in a centered interval of width one. Bars touch because the intervals are contiguous.</p>
    </section>
    <style>
      #esa-histogram-lab{max-width:100%;min-width:0;box-sizing:border-box;overflow-wrap:anywhere}
      #esa-histogram-lab label{display:flex;flex-direction:column;gap:6px;min-width:0}
      #esa-histogram-lab textarea,#esa-histogram-lab input{width:100%;max-width:100%;min-width:0;box-sizing:border-box;font:inherit;padding:8px}
      #esa-histogram-lab .esa-histogram-controls{display:flex;flex-wrap:wrap;align-items:end;gap:12px;margin:12px 0}
      #esa-histogram-lab .esa-histogram-controls label{flex:0 1 180px}
      #esa-histogram-lab svg{display:block;width:100%;height:auto;max-width:540px;margin:12px auto}
      #esa-histogram-lab [hidden]{display:none!important}
      #esa-histogram-lab p{margin:11px 0}
    </style>
    <script>
    (function(){
      "use strict";
      const root=document.getElementById("esa-histogram-lab");if(!root)return;
      const get=id=>root.querySelector("#esa-histogram-"+id);
      const sample="42, 48, 54, 56, 59, 61, 62, 63, 67, 69, 70, 72, 73, 75, 78, 79, 82, 84, 87, 93";
      const input=get("data"),binInput=get("bins"),chart=get("chart"),err=get("error");
      const ns="http://www.w3.org/2000/svg";
      function svgElement(tag,attributes,content){
        const e=document.createElementNS(ns,tag);
        Object.entries(attributes).forEach(([k,v])=>e.setAttribute(k,String(v)));
        if(content!==undefined)e.textContent=String(content);
        return e;
      }
      function invalid(reason){
        err.hidden=false;err.textContent=reason;chart.setAttribute("hidden","");
        ["n","width","sum"].forEach(k=>get(k).textContent="—");
        get("frequency-table").replaceChildren();
      }
      function update(){
        const tokens=input.value.split(",").map(s=>s.trim());
        const nums=tokens.map(s=>s===""?NaN:Number(s)),bins=Number(binInput.value);
        if(tokens.length<2||tokens.length>100||nums.some(v=>!Number.isFinite(v)||Math.abs(v)>1000000)||
           binInput.value.trim()===""||!Number.isInteger(bins)||bins<2||bins>12){
          invalid("Provide 2–100 comma-separated finite values between −1,000,000 and 1,000,000, and 2–12 integer bins.");
          return;
        }
        let min=Math.min(...nums),max=Math.max(...nums);
        if(min===max){min-=0.5;max+=0.5;}
        const width=(max-min)/bins;
        if(!Number.isFinite(width)||width<=0){invalid("Invalid bin width; adjust the data.");return;}
        const frequencies=Array(bins).fill(0);
        nums.forEach(value=>{
          const position=Math.min(bins-1,Math.max(0,Math.floor((value-min)/width)));
          frequencies[position]++;
        });
        const sum=frequencies.reduce((a,b)=>a+b,0);
        err.hidden=true;err.textContent="";chart.removeAttribute("hidden");
        get("n").textContent=String(nums.length);get("width").textContent=width.toFixed(4);
        get("sum").textContent=String(sum);
        const marks=[],rows=[],w=380/bins,maxFrequency=Math.max(1,...frequencies);
        for(let i=0;i<bins;i++){
          const lower=min+i*width,upper=i===bins-1?max:min+(i+1)*width;
          const h=185*frequencies[i]/maxFrequency;
          const bar=svgElement("rect",{x:45+i*w,y:218-h,width:w,height:h,fill:"#0d9488",stroke:"currentColor","stroke-width":0.4});
          bar.appendChild(svgElement("title",{},"Bin "+(i+1)+" frequency "+frequencies[i]));
          marks.push(bar);
          const row=document.createElement("tr"),head=document.createElement("th"),cell=document.createElement("td");
          head.scope="row";head.textContent="["+lower.toFixed(3)+", "+upper.toFixed(3)+(i===bins-1?"]":")");
          cell.textContent=String(frequencies[i]);row.append(head,cell);rows.push(row);
        }
        marks.push(svgElement("text",{x:45,y:244,fill:"currentColor","font-size":11},min.toFixed(2)));
        marks.push(svgElement("text",{x:425,y:244,fill:"currentColor","font-size":11,"text-anchor":"end"},max.toFixed(2)));
        get("bars").replaceChildren(...marks);
        get("frequency-table").replaceChildren(...rows);
        chart.setAttribute("aria-label","Histogram of "+nums.length+" observations in "+bins+
          " equal-width bins; frequencies: "+frequencies.join(", ")+".");
      }
      input.addEventListener("input",update);binInput.addEventListener("input",update);
      get("reset").addEventListener("click",()=>{input.value=sample;binInput.value="5";update()});
      update();
    })();
    </script>

    <h2>Too Few Bins</h2>

    <p>
      If there are too few bins,
      important structure may disappear.
    </p>

    <p>
      The histogram becomes overly simplified
      and may hide meaningful patterns.
    </p>

    <h2>Too Many Bins</h2>

    <img src="{{ 'descriptive/images/bin-width-comparison.png' | relative_url }}"
     alt="Too few bins versus too many bins"
     style="margin-top:15px; max-width:100%; height:auto;">

    <p>
      If there are too many bins,
      the graph becomes noisy.
    </p>

    <p>
      Random variation may appear more important than it really is.
    </p>

    <p>
      Good histograms balance detail and simplicity.
    </p>

    <h2>What Histograms Reveal</h2>

    <p>
      Histograms help identify several important characteristics of a distribution.
    </p>

    <div class="grid grid-2">

      <div class="card">

        <h3>Center</h3>

        <p>
          Where most observations occur.
        </p>

      </div>

      <div class="card">

        <h3>Spread</h3>

        <p>
          How dispersed the values are.
        </p>

      </div>

      <div class="card">

        <h3>Shape</h3>

        <p>
          Symmetric, skewed, or multimodal.
        </p>

      </div>

      <div class="card">

        <h3>Outliers</h3>

        <p>
          Unusual observations far from most data.
        </p>

      </div>

    </div>

    <h2>Symmetric Distributions</h2>

    <p>
      Some histograms appear balanced around a center.
    </p>

    <p>
      In a symmetric distribution:
    </p>

    <ul class="bullets">

      <li>Left and right sides look similar</li>

      <li>The center is clearly visible</li>

      <li>Extreme values occur on both sides</li>

    </ul>

    <p>
      Many natural measurements are approximately symmetric.
    </p>

    <h2>Skewed Distributions</h2>

    <img src="{{ 'descriptive/images/symmetric-vs-skewed-histograms.png' | relative_url }}"
     alt="Symmetric and skewed histograms"
     style="margin-top:15px; max-width:100%; height:auto;">

    <p>
      Not all distributions are symmetric.
    </p>

    <p>
      A histogram may have:
    </p>

    <ul class="bullets">

      <li>Long right tail (right-skewed)</li>

      <li>Long left tail (left-skewed)</li>

    </ul>

    <p>
      Income data is a classic example of a right-skewed distribution.
    </p>

    <h2>Multiple Peaks</h2>

    <img src="{{ 'descriptive/images/bimodal-histogram.png' | relative_url }}"
     alt="Histogram with multiple peaks"
     style="margin-top:15px; max-width:100%; height:auto;">

    <p>
      Some histograms contain more than one peak.
    </p>

    <p>
      This may indicate:
    </p>

    <ul class="bullets">

      <li>Multiple groups in the data</li>

      <li>Different populations combined together</li>

      <li>Underlying structure worth investigating</li>

    </ul>

    <p>
      Histograms often reveal patterns that summary statistics cannot.
    </p>

    <h2>Histograms and Outliers</h2>

    <p>
      Outliers may appear as isolated bars
      separated from the main body of the distribution.
    </p>

    <p>
  However, histograms are only a screening tool.
  Unusual observations should be investigated further
  before being classified as outliers.
</p>

    <p>
      Detecting unusual observations
      is one of the major benefits of visualization.
    </p>

    <h2>Histograms and Statistical Thinking</h2>

    <p>
      Histograms encourage statisticians to think about distributions
      rather than individual observations.
    </p>

    <p>
      Much of modern statistics is built upon understanding
      how distributions behave.
    </p>

    <h2>Histograms and Summary Statistics</h2>

<p>
  Two datasets can have similar means and standard deviations
  while having very different histogram shapes.
</p>

<p>
  This is why visualizing a distribution is often as important
  as calculating numerical summaries.
</p>

    <h2>Applications of Histograms</h2>

    <p>
      Histograms are widely used in:
    </p>

    <ul class="bullets">

      <li>Research studies</li>

      <li>Quality control</li>

      <li>Business analytics</li>

      <li>Medicine</li>

      <li>Engineering</li>

      <li>Machine learning</li>

    </ul>

    <p>
      They are among the most important graphs in all of statistics.
    </p>

    <div class="concept-box">

  <strong>Key insight:</strong>

  <p>
    Histograms help statisticians think about distributions,
    and understanding distributions is central to statistical reasoning.
  </p>

</div>

<h2>Optional: Creating Histograms in SPSS</h2>

<ul class="bullets">

  <li>Graphs → Chart Builder</li>

  <li>Select Histogram</li>

  <li>Assign the numerical variable</li>

  <li>Review the chosen bin structure</li>

</ul>

<p>
  Always inspect the distribution visually before proceeding with further analysis.
</p>

<h3>Python Example</h3>

<p>
This example creates a histogram for numerical data.
</p>

<pre><code>import matplotlib.pyplot as plt

scores = [55,58,60,62,65,67,68,70,
          72,74,75,77,80,82,85,
          88,90,92,95]

plt.hist(scores)
plt.show()
</code></pre>

<h3>R Example</h3>

<p>
This example creates a histogram for numerical data.
</p>

<pre><code>scores <- c(55,58,60,62,65,67,68,70,
            72,74,75,77,80,82,85,
            88,90,92,95)

hist(scores)
</code></pre>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Histograms display distributions of numerical variables</li>

        <li>Values are grouped into intervals called bins</li>

        <li>Histograms reveal center, spread, shape, and outliers</li>

        <li>Histograms differ fundamentally from bar charts</li>

        <li>Bin selection affects interpretation</li>

        <li>Histograms help identify skewness and multiple peaks</li>

        <li>Understanding distributions is a central goal of statistics</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/visualization/pie-charts/">
         ← Previous: Pie Charts
      </a>

      <a class="btn"
         href="/descriptive/visualization/density-curves/">
         Next: Density Curves →
      </a>

    </div>

  </div>

</section>
