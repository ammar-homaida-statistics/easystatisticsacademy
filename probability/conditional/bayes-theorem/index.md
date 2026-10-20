---
layout: default
title: Bayes' Theorem
description: Learn how Bayes' theorem updates probabilities when new evidence becomes available and understand one of the most important ideas in statistics.
permalink: /probability/conditional/bayes-theorem/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_conditional_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/conditional/bayes-theorem/",
    label: "Bayes' Theorem",
    ts: Date.now()
    }));
  } catch (_) {
    // Persisting progress is optional; unavailable storage must not interrupt lessons.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 2</span>
      <span class="badge">Conditional Probability</span>
      <span class="badge">Bayesian Thinking</span>
    </div>

    <h1>Bayes' Theorem</h1>

    <p class="lead">
      Bayes' theorem provides a systematic way to update probabilities when new evidence becomes available.
    </p>

    <p class="lead">
      It is one of the most influential ideas in probability, statistics, machine learning, medicine, and decision-making.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/conditional/law-of-total-probability/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/conditional/tree-diagrams/">
         Next: Tree Diagrams →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Central Question</h2>

    <p>
      Many probability questions involve reversing a conditional probability.
    </p>

    <div class="example-box">

      <p>
        If a person has a disease,
        what is the probability of a positive test?
      </p>
    </div>

    <p>
      This probability may be known.
    </p>

    <p>
      However,
      a more practical question is often:
    </p>

    <div class="example-box">

      <p>
        If the test is positive,
        what is the probability that the person has the disease?
      </p>
    </div>

    <p>
      These are not the same probability.
    </p>

    <p>
      Bayes' theorem provides the connection between them.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Bayes' theorem updates beliefs about a cause after observing evidence.
      </p>

    </div>

    <h2>Why Bayes' Theorem Is Needed</h2>

    <p>
      Conditional probabilities have direction.
    </p>

    <div class="example-box">

      <p>
        Probability of Evidence given Cause
      </p>
    </div>

    <p>
      is generally different from:
    </p>

    <div class="example-box">

      <p>
        Probability of Cause given Evidence
      </p>
    </div>

    <p>
      Bayes' theorem allows us to move from one direction to the other.
    </p>

    <h2>Starting from Conditional Probability</h2>

    <p>
      Recall the conditional probability formula for events \(A\) and \(B\), provided that \(P(B)>0\).
    </p>

    \[
P(A\mid B)=\frac{P(A\cap B)}{P(B)},\qquad P(B)>0
\]

    <p>
      We can also write:
    </p>

    \[
P(B\mid A)=\frac{P(A\cap B)}{P(A)},\qquad P(A)>0
\]

    <p>
      Both expressions describe the same intersection probability, \(P(A\cap B)\), but their denominators differ. They are valid only when the relevant conditioning event has positive probability.
    </p>

    <h2>Deriving Bayes' Theorem</h2>

    <p>
      From the multiplication rule:
    </p>

    \[
P(A\cap B)=P(B\mid A)\,P(A)
\]

    <p>
      Substituting into the conditional probability formula gives:
    </p>

    \[
P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B)}
\]

    <p>
      This is Bayes' theorem for \(P(B)>0\), obtained by substituting the multiplication rule into the definition of conditional probability.
    </p>

    <h2>The Bayes Formula</h2>

    \[
\underbrace{P(A\mid B)}_{\text{posterior}}
=\frac{\overbrace{P(B\mid A)}^{\text{likelihood}}\,
\overbrace{P(A)}^{\text{prior}}}
{\underbrace{P(B)}_{\text{evidence}}}
\]

    <p>
      Although the formula appears simple,
      it is one of the most powerful results in probability.
    </p>

    <h2>Understanding the Components</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Term</th>
            <th>Meaning</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>P(A)</td>
            <td>Prior probability</td>
          </tr>

          <tr>
            <td>P(B|A)</td>
            <td>Likelihood</td>
          </tr>

          <tr>
            <td>P(B)</td>
            <td>Overall probability of evidence</td>
          </tr>

          <tr>
            <td>P(A|B)</td>
            <td>Posterior probability</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Bayesian Update Process</h2>

    <p>
      Bayes' theorem combines:
    </p>

    <ul class="bullets">

      <li>What we believed before seeing evidence.</li>

      <li>The evidence that was observed.</li>

      <li>The strength of the relationship between the evidence and the event.</li>

    </ul>

    <p>
      The result is an updated probability.
    </p>

    <h2>A Medical Testing Example</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        Disease prevalence = 1%
      </p>

      <p>
        Test sensitivity = 95%
      </p>

      <p>
        Overall positive-test probability across the whole population = 5% (not a 5% false-positive rate)
      </p>

    </div>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        D = Disease
      </p>

      <p>
        + = Positive test
      </p>

    </div>

    <p>
      Bayes' theorem becomes:
    </p>

    \[
P(D\mid +)=\frac{P(+\mid D)\,P(D)}{P(+)}
=\frac{0.95\times0.01}{0.05}
=0.19=19\%
\]

    <p>
      Therefore 19% of people who test positive have the disease under these illustrative assumptions. The result is not the 95% sensitivity: \(P(D\mid +)\) and \(P(+\mid D)\) condition on different events.
    </p>

    <p>
      For internal consistency, these three inputs imply a false-positive rate of \(P(+\mid D^{c})=(0.05-0.95\times0.01)/0.99\approx0.0409\), or about 4.09%. This is distinct from the overall 5% positive-test probability.
    </p>

    <section class="concept-box" id="esa-bayes-lab" aria-labelledby="esa-bayes-title" style="min-width:0;overflow-wrap:anywhere">
  <h2 id="esa-bayes-title">Interactive Bayes' Theorem and Base-Rate Explorer</h2>
  <p>For a <strong>fictional binary screening test</strong>, change the prevalence, sensitivity P(+ | D), and specificity P(− | not D). The tool computes P(D | +) and P(D | −) using Bayes' rule and the law of total probability. It is an educational probability model, not medical advice or a validated test.</p>
  <div style="display:flex;flex-wrap:wrap;gap:1rem;align-items:end">
    <label for="esa-bayes-prev">Prevalence (%)
      <input id="esa-bayes-prev" type="number" min="0" max="100" step="any" value="1" inputmode="decimal" style="max-width:9rem">
    </label>
    <label for="esa-bayes-sens">Sensitivity (%)
      <input id="esa-bayes-sens" type="number" min="0" max="100" step="any" value="90" inputmode="decimal" style="max-width:9rem">
    </label>
    <label for="esa-bayes-spec">Specificity (%)
      <input id="esa-bayes-spec" type="number" min="0" max="100" step="any" value="95" inputmode="decimal" style="max-width:9rem">
    </label>
    <button id="esa-bayes-run" class="btn" type="button">Calculate</button>
    <button id="esa-bayes-reset" class="btn btn-outline" type="button">Reset example</button>
  </div>
  <p id="esa-bayes-status" role="status" aria-live="polite"></p>
  <p><strong>Posterior after a positive result, P(D | +):</strong> <output id="esa-bayes-pos">—</output></p>
  <p><strong>Posterior after a negative result, P(D | −):</strong> <output id="esa-bayes-neg">—</output></p>
  <p><strong>Probability of a positive result:</strong> <output id="esa-bayes-plus-prob">—</output>; <strong>of a negative result:</strong> <output id="esa-bayes-minus-prob">—</output>.</p>
  <div class="table-wrap"><table>
    <caption>Expected outcomes per 10,000 hypothetical individuals (may be fractional)</caption>
    <thead><tr><th>Actual condition</th><th>Positive result</th><th>Negative result</th></tr></thead>
    <tbody>
      <tr><th scope="row">Condition present</th><td><output id="esa-bayes-tp">—</output></td><td><output id="esa-bayes-fn">—</output></td></tr>
      <tr><th scope="row">Condition absent</th><td><output id="esa-bayes-fp">—</output></td><td><output id="esa-bayes-tn">—</output></td></tr>
    </tbody>
  </table></div>
  <p><strong>Reference benchmark:</strong> At prevalence 1%, sensitivity 90%, and specificity 95%, P(D | +) = 0.009/(0.009 + 0.0495) ≈ <strong>15.38%</strong>. A 90% sensitivity does not mean that 90% of positive results reflect the condition.</p>
  <p><strong>Boundary rule:</strong> A posterior conditioned on a result with probability zero is undefined, not 0%. Invalid percentages are rejected. All computations are local to your browser; no data are saved or transmitted.</p>
</section>

<h2>The Role of the Prior</h2>

    <p>
      The prior probability represents our belief before observing new evidence.
    </p>

    <div class="example-box">

      <p>
        Probability of disease before testing.
      </p>
    </div>

    <p>
      Priors often come from:
    </p>

    <ul class="bullets">

      <li>Historical data</li>

      <li>Past studies</li>

      <li>Expert knowledge</li>

      <li>Population statistics</li>

    </ul>

    <h2>The Role of the Likelihood</h2>

    <p>
      The likelihood measures how consistent the observed evidence is with a particular explanation.
    </p>

    <div class="example-box">

      <p>
        How likely is a positive test if the disease is actually present?
      </p>
    </div>

    <p>
      Strong evidence produces larger updates.
    </p>

    <h2>The Posterior Probability</h2>

    <p>
      The posterior probability is the updated belief after incorporating evidence.
    </p>

    <p>
      It represents what we believe now,
      not what we believed initially.
    </p>

    <div class="concept-box">

      <strong>Bayesian thinking:</strong>

      <p>
        Prior belief + Evidence → Updated belief
      </p>

    </div>

    <h2>The Importance of Base Rates</h2>

    <p>
      Bayes' theorem explains why base rates matter.
    </p>

    <p>
      Rare events remain rare even when evidence appears convincing.
    </p>

    <p>
      Ignoring base rates often leads to incorrect conclusions.
    </p>

    <div class="example-box">

      <p>
        A highly accurate test can still produce many false alarms when a condition is extremely rare.
      </p>
    </div>

    <h2>The Connection to the Law of Total Probability</h2>

    <p>
      The denominator in Bayes' theorem is often found using the Law of Total Probability.
    </p>

    <p>
      For example:
    </p>

    \[
P(+)=P(+\mid D)\,P(D)+P(+\mid D^{c})\,P(D^{c})
\]

    <p>
      Here \(D^{c}\) denotes not having the disease. The two mutually exclusive cases, disease and no disease, exhaust the population; their contributions add to the overall positive-test probability.
    </p>

    <h2>Applications of Bayes' Theorem</h2>

    <p>
      Bayes' theorem appears throughout modern science and technology.
    </p>

    <ul class="bullets">

      <li>Medical diagnosis</li>

      <li>Spam filtering</li>

      <li>Machine learning</li>

      <li>Artificial intelligence</li>

      <li>Risk assessment</li>

      <li>Search engines</li>

      <li>Fraud detection</li>

      <li>Scientific inference</li>

    </ul>

    <p>
      Many modern predictive systems are built on Bayesian ideas.
    </p>

    <h2>A Common Misunderstanding</h2>

    <p>
      Students often assume:
    </p>

    <div class="example-box">

      <p>
        P(A|B) = P(B|A)
      </p>
    </div>

    <p>
      This is usually false.
    </p>

    <p>
      Bayes' theorem exists precisely because these probabilities differ.
    </p>

    <h2>The Big Picture</h2>

    <p>
      Bayes' theorem transforms probability from a static description of uncertainty into a dynamic system for learning from evidence.
    </p>

    <p>
      Every time new information becomes available,
      Bayes' theorem provides a principled method for updating probabilities.
    </p>

    <h2>Preparing for Tree Diagrams</h2>

    <p>
      Many conditional probability problems involve multiple stages and pathways.
    </p>

    <p>
      Visual tools can make these problems easier to understand.
    </p>

    <p>
      Tree diagrams provide one of the most useful ways to organize conditional probabilities,
      multiplication rules,
      and Bayesian calculations.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The next lesson introduces tree diagrams,
      a graphical method for representing sequential probability processes and organizing complex probability calculations.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Bayes' theorem updates probabilities using new evidence</li>

        <li>P(A|B) and P(B|A) are generally different probabilities</li>

        <li>Bayes' theorem connects these two conditional probabilities</li>

        <li>The theorem combines prior information and observed evidence</li>

        <li>The result is an updated posterior probability</li>

        <li>Base rates play an important role in Bayesian reasoning</li>

        <li>Bayes' theorem is one of the foundations of modern statistics and machine learning</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/conditional/law-of-total-probability/">
         ← Previous: Law of Total Probability
      </a>

      <a class="btn"
         href="/probability/conditional/tree-diagrams/">
         Next: Tree Diagrams →
      </a>

    </div>

  </div>

</section>
<script src="/js/bayes-evidence-lab.js" defer></script>
