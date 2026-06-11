---
layout: default
title: Populations, Parameters, and Targets
description: Learn the fundamental inferential concepts of populations, parameters, samples, and statistical targets.
permalink: /inference/foundations/populations-parameters-target/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_foundations_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/foundations/populations-parameters-target/",
    label: "Populations, Parameters, and Targets",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 1</span>
      <span class="badge">Foundations</span>
      <span class="badge">Core Concepts</span>
    </div>

    <h1>Populations, Parameters, and Targets</h1>

    <p class="lead">
      Statistical inference begins with a simple question: what exactly are we trying to learn?
    </p>

    <p class="lead">
      To answer that question, we must clearly distinguish populations, samples, parameters, and inferential targets.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/foundations/what-is-statistical-inference/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/foundations/statistics-as-random-variables/">
         Next: Statistics as Random Variables →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Goal of Inference</h2>

    <p>
      Statistical inference is not primarily about the sample.
    </p>

    <p>
      The sample is a source of information.
    </p>

    <p>
      The real goal is learning something about a larger population.
    </p>

    <div class="concept-box">

      <strong>Core idea:</strong>

      <p>
        Samples provide evidence. Populations are the true objects of interest.
      </p>

    </div>

    <h2>What Is a Population?</h2>

    <p>
      A population is the complete collection of units, individuals, events, or measurements that we want to study.
    </p>

    <div class="example-box">

      <p>
        All voters in a country
      </p>

      <p>
        All products from a factory
      </p>

      <p>
        All customers of a business
      </p>

      <p>
        All patients with a disease
      </p>

    </div>

    <p>
      The population defines the scope of the research question.
    </p>

    <h2>Populations Are Often Too Large</h2>

    <p>
      In most real-world situations,
      observing an entire population is impractical.
    </p>

    <div class="example-box">

      <p>
        Millions of voters
      </p>

      <p>
        Years of future transactions
      </p>

      <p>
        Entire national health records
      </p>

    </div>

    <p>
      This limitation motivates sampling.
    </p>

    <h2>What Is a Sample?</h2>

    <p>
      A sample is a subset of observations taken from the population.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A sample is the data actually collected and analyzed.
      </p>

    </div>

    <p>
      Statistical inference uses sample information to learn about the population.
    </p>

    <h2>Population vs Sample</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Population</th>
            <th>Sample</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Entire group of interest</td>
            <td>Subset of the population</td>
          </tr>

          <tr>
            <td>Usually inaccessible</td>
            <td>Directly observed</td>
          </tr>

          <tr>
            <td>Contains parameters</td>
            <td>Contains statistics</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>What Is a Parameter?</h2>

    <p>
      A parameter is a numerical characteristic of a population.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A parameter is a fixed but unknown quantity describing a population.
      </p>

    </div>

    <h2>Common Population Parameters</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Parameter</th>
            <th>Meaning</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>μ</td>
            <td>Population mean</td>
          </tr>

          <tr>
            <td>p</td>
            <td>Population proportion</td>
          </tr>

          <tr>
            <td>σ²</td>
            <td>Population variance</td>
          </tr>

          <tr>
            <td>σ</td>
            <td>Population standard deviation</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Parameters exist whether or not we know their values.
    </p>

    <h2>Why Parameters Are Important</h2>

    <p>
      Most inferential questions are actually questions about parameters.
    </p>

    <div class="example-box">

      <p>
        What is the average income?
      </p>

      <p>
        What proportion supports the policy?
      </p>

      <p>
        What is the true defect rate?
      </p>

    </div>

    <p>
      These are parameter questions.
    </p>

    <h2>Parameters Are Fixed</h2>

    <p>
      A population parameter does not change when a different sample is collected.
    </p>

    <p>
      The parameter has one true value.
    </p>

    <p>
      What changes is our estimate of that value.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Parameters are fixed. Estimates are variable.
      </p>

    </div>

    <h2>What Is the Inferential Target?</h2>

    <p>
      The inferential target is the quantity we ultimately want to learn about.
    </p>

    <div class="example-box">

      <p>
        Population mean income
      </p>

      <p>
        Treatment effect
      </p>

      <p>
        Difference between groups
      </p>

      <p>
        Population proportion
      </p>

    </div>

    <p>
      Every statistical analysis should begin by identifying its target.
    </p>

    <h2>Examples of Inferential Targets</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Research Question</th>
            <th>Target</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>How much do customers spend?</td>
            <td>Population mean</td>
          </tr>

          <tr>
            <td>Who supports a candidate?</td>
            <td>Population proportion</td>
          </tr>

          <tr>
            <td>Does a treatment work?</td>
            <td>Treatment effect</td>
          </tr>

          <tr>
            <td>Are groups different?</td>
            <td>Difference in parameters</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Statistics Are Not Parameters</h2>

    <p>
      A common mistake is confusing sample statistics with population parameters.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Population Quantity</th>
            <th>Sample Quantity</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>μ</td>
            <td>x̄</td>
          </tr>

          <tr>
            <td>p</td>
            <td>p̂</td>
          </tr>

          <tr>
            <td>σ²</td>
            <td>s²</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Statistics estimate parameters,
      but they are not the same thing.
    </p>

    <h2>The Population-to-Sample Framework</h2>

    <p>
      Nearly every inferential procedure follows the same structure:
    </p>

    <ol>

      <li>Define a population.</li>

      <li>Identify the parameter of interest.</li>

      <li>Collect a sample.</li>

      <li>Calculate a statistic.</li>

      <li>Use the statistic to learn about the parameter.</li>

    </ol>

    <h2>Why Clear Targets Matter</h2>

    <p>
      Poorly defined targets often lead to poor analyses.
    </p>

    <p>
      Before computing formulas,
      statisticians first clarify:
    </p>

    <div class="example-box">

      <p>
        What population?
      </p>

      <p>
        Which parameter?
      </p>

      <p>
        What question?
      </p>

    </div>

    <p>
      These decisions determine the entire inferential strategy.
    </p>

    <h2>The Foundation of All Inference</h2>

    <p>
      Statistical inference can be summarized as:
    </p>

    <div class="concept-box">

      <strong>Framework:</strong>

      <p>
        Use sample statistics to learn about population parameters that represent the inferential target.
      </p>

    </div>

    <p>
      Everything else in inference builds on this idea.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Population parameters are fixed but unknown.
    </p>

    <p>
      Statistics are calculated from samples and therefore vary from sample to sample.
    </p>

    <p>
      The next lesson explores why statistics themselves are random variables and why this fact makes statistical inference possible.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>A population is the complete group of interest</li>

        <li>A sample is the subset that is actually observed</li>

        <li>Parameters are fixed but unknown characteristics of populations</li>

        <li>Statistics are calculated from samples</li>

        <li>Inferential targets are the quantities researchers want to learn about</li>

        <li>Most inferential questions focus on population parameters</li>

        <li>Statistics estimate parameters but are not parameters themselves</li>

        <li>Inference uses sample statistics to learn about population targets</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/foundations/what-is-statistical-inference/">
         ← Previous: What Is Statistical Inference?
      </a>

      <a class="btn"
         href="/inference/foundations/statistics-as-random-variables/">
         Next: Statistics as Random Variables →
      </a>

    </div>

  </div>

</section>