---
layout: default
title: What Is a Hypothesis Test?
description: Learn the purpose of hypothesis testing, why it differs from estimation, and how statisticians use data to evaluate claims about populations.
permalink: /inference/hypothesis-testing/what-is-a-hypothesis-test/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_hypothesis_testing_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/hypothesis-testing/what-is-a-hypothesis-test/",
    label: "What Is a Hypothesis Test?",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 3</span>
      <span class="badge">Hypothesis Testing</span>
      <span class="badge">Foundations</span>
    </div>

    <h1>What Is a Hypothesis Test?</h1>

    <p class="lead">
      Confidence intervals focus on estimation. Hypothesis tests focus on evidence.
    </p>

    <p class="lead">
      A hypothesis test provides a systematic framework for evaluating whether observed data are consistent with a proposed claim about a population.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/hypothesis-testing/">
         ← Block Home
      </a>

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/null-and-alternative/">
         Next: Null and Alternative Hypotheses →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Hypothesis Testing Exists</h2>

    <p>
      In statistical inference, researchers often want to evaluate claims rather than simply estimate parameters.
    </p>

    <div class="example-box">

      <p>
        Does a new drug improve recovery rates?
      </p>

      <p>
        Does a teaching method increase exam scores?
      </p>

      <p>
        Has a manufacturing process changed?
      </p>

      <p>
        Is voter support above 50%?
      </p>

    </div>

    <p>
      These questions involve evidence for or against a claim.
    </p>

    <h2>From Estimation to Decision-Making</h2>

    <p>
      Confidence intervals answer:
    </p>

    <div class="example-box">

      <p>
        What values are plausible for the parameter?
      </p>

    </div>

    <p>
      Hypothesis tests answer:
    </p>

    <div class="example-box">

      <p>
        Are the data inconsistent enough with a particular claim that we should doubt it?
      </p>

    </div>

    <h2>The Core Idea</h2>

    <div class="concept-box">

      <strong>Hypothesis Test:</strong>

      <p>
        A hypothesis test evaluates whether observed data would be unusual if a specific claim about a population were true.
      </p>

    </div>

    <p>
      The logic is indirect.
    </p>

    <p>
      We temporarily assume a claim is true and ask whether the observed sample would be surprising under that assumption.
    </p>

    <h2>An Everyday Analogy</h2>

    <p>
      Imagine a coin that is claimed to be fair.
    </p>

    <p>
      You flip it 100 times and observe 90 heads.
    </p>

    <p>
      You might ask:
    </p>

    <div class="example-box">

      <p>
        Would 90 heads be plausible if the coin were truly fair?
      </p>

    </div>

    <p>
      If such an outcome is extremely unlikely under the fairness assumption,
      the claim becomes difficult to believe.
    </p>

    <p>
      This reasoning is the essence of hypothesis testing.
    </p>

    <h2>The General Logic</h2>

    <p>
      Every hypothesis test follows the same structure:
    </p>

    <ol>

      <li>State a claim about a population.</li>

      <li>Assume the claim is true.</li>

      <li>Determine what outcomes would be expected.</li>

      <li>Compare the observed sample to those expectations.</li>

      <li>Assess whether the observed result is unusually far from expectation.</li>

    </ol>

    <h2>The Role of Random Sampling</h2>

    <p>
      Samples naturally vary from one draw to another.
    </p>

    <p>
      Therefore an observed difference does not automatically imply that a claim is false.
    </p>

    <p>
      The key question is:
    </p>

    <div class="example-box">

      <p>
        Is the observed difference larger than would reasonably occur through random sampling alone?
      </p>

    </div>

    <h2>Evidence, Not Proof</h2>

    <p>
      Hypothesis tests do not provide mathematical proof.
    </p>

    <p>
      Instead they quantify the strength of evidence against a proposed claim.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Statistical tests support decisions under uncertainty. They do not establish certainty.
      </p>

    </div>

    <h2>A Simple Example</h2>

    <p>
      Suppose a manufacturer claims that a machine fills bottles with an average of:
    </p>

    0

    <p>
      A quality-control analyst collects a sample and finds an average of:
    </p>

    1

    <p>
      The question becomes:
    </p>

    <div class="example-box">

      <p>
        Could random sampling reasonably explain an average this far from 500 mL?
      </p>

    </div>

    <p>
      A hypothesis test helps answer that question.
    </p>

    <h2>The Two Possible Explanations</h2>

    <p>
      Whenever data differ from a claim,
      there are generally two explanations:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Explanation</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Random Variation</td>
            <td>The claim is true and sampling variability created the difference</td>
          </tr>

          <tr>
            <td>Real Effect</td>
            <td>The claim is false and a genuine difference exists</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Hypothesis testing evaluates which explanation is more plausible.
    </p>

    <h2>The Language of Hypotheses</h2>

    <p>
      Statistical tests are built around competing statements called hypotheses.
    </p>

    <p>
      These hypotheses formalize:
    </p>

    <ul class="bullets">

      <li>The claim being challenged</li>

      <li>The competing explanation</li>

    </ul>

    <p>
      The next lesson develops these ideas in detail.
    </p>

    <h2>Why Hypothesis Tests Are So Common</h2>

    <p>
      Hypothesis testing appears throughout science and decision-making.
    </p>

    <ul class="bullets">

      <li>Clinical trials</li>

      <li>Psychology experiments</li>

      <li>Economics research</li>

      <li>Manufacturing quality control</li>

      <li>A/B testing</li>

      <li>Public-health studies</li>

    </ul>

    <p>
      Whenever evidence must be evaluated formally,
      hypothesis testing often plays a central role.
    </p>

    <h2>What Hypothesis Tests Do Not Do</h2>

    <p>
      Hypothesis tests do not:
    </p>

    <ul class="bullets">

      <li>Prove hypotheses true</li>

      <li>Eliminate uncertainty</li>

      <li>Guarantee correct decisions</li>

      <li>Measure practical importance by themselves</li>

    </ul>

    <p>
      They are tools for evaluating evidence,
      not machines for producing certainty.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Confidence intervals and hypothesis tests are the two major pillars of classical statistical inference.
    </p>

    <p>
      Confidence intervals emphasize estimation.
    </p>

    <p>
      Hypothesis tests emphasize evidence and decision-making.
    </p>

    <p>
      Both rely on sampling distributions, probability models, and uncertainty.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        A hypothesis test evaluates whether observed data would be unusually inconsistent with a specific claim about a population. The more unusual the data appear under that claim, the stronger the evidence against it.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Every hypothesis test begins with two competing statements.
    </p>

    <p>
      One represents the claim being evaluated.
    </p>

    <p>
      The other represents the competing explanation.
    </p>

    <p>
      The next lesson introduces null hypotheses and alternative hypotheses, the foundation of all classical hypothesis tests.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Hypothesis tests evaluate claims about populations</li>

        <li>They assess whether observed data are unusual under a proposed assumption</li>

        <li>Testing focuses on evidence rather than estimation</li>

        <li>Random sampling variability is central to the logic</li>

        <li>Statistical tests compare observed outcomes to expected outcomes</li>

        <li>Tests provide evidence, not proof</li>

        <li>Every test involves competing explanations for observed data</li>

        <li>Null and alternative hypotheses form the foundation of hypothesis testing</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/">
         ← Block Home
      </a>

      <a class="btn"
         href="/inference/hypothesis-testing/null-and-alternative/">
         Next: Null and Alternative Hypotheses →
      </a>

    </div>

  </div>

</section>