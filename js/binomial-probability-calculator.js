/* Shared English/Arabic Binomial calculator: same numerical algorithm. */
(function () {
      const form = document.getElementById("esa-binomial-calculator-form");
      const isArabic = document.documentElement.lang === "ar";
      if (!form) return;
      const nInput = document.getElementById("esa-binomial-n");
      const pInput = document.getElementById("esa-binomial-p");
      const kInput = document.getElementById("esa-binomial-k");
      const exact = document.getElementById("esa-binomial-exact");
      const cumulative = document.getElementById("esa-binomial-cdf");
      const upper = document.getElementById("esa-binomial-upper");
      const mean = document.getElementById("esa-binomial-mean");
      const variance = document.getElementById("esa-binomial-variance");
      const explanation = document.getElementById("esa-binomial-explanation");
      const error = document.getElementById("esa-binomial-error");
      const outputs = [exact,cumulative,upper,mean,variance];

      function format(x) {
        if (x === 0) return "0";
        if (Math.abs(x) < 1e-8) return x.toExponential(8);
        return Number(x.toPrecision(12)).toLocaleString("en-US",{maximumFractionDigits:12});
      }
      function inclusiveLogSum(logTerms, start, end) {
        let peak = -Infinity;
        for (let i = start; i <= end; ++i) peak = Math.max(peak,logTerms[i]);
        let total = 0;
        for (let i = start; i <= end; ++i) total += Math.exp(logTerms[i] - peak);
        return Math.min(1, Math.max(0, Math.exp(peak) * total));
      }
      function render() {
        const n = Number(nInput.value);
        const p = Number(pInput.value);
        const k = Number(kInput.value);
        let problem = "";
        if (!nInput.value.trim() || !Number.isSafeInteger(n) || n < 1 || n > 1000) {
          problem = isArabic ? "أدخل عددًا صحيحًا للتجارب من 1 إلى 1000." : "Enter a whole number of trials from 1 to 1,000.";
        } else if (!pInput.value.trim() || !Number.isFinite(p) || p < 0 || p > 1) {
          problem = isArabic ? "أدخل احتمال نجاح بين 0 و1 شاملًا الطرفين." : "Enter a success probability between 0 and 1 inclusive.";
        } else if (!kInput.value.trim() || !Number.isSafeInteger(k) || k < 0 || k > n) {
          problem = isArabic ? "أدخل عددًا صحيحًا للنجاحات بين 0 وn شاملًا الطرفين." : "Enter a whole number of successes between 0 and n inclusive.";
        }
        if (problem) {
          outputs.forEach(out => { out.textContent = "—"; });
          explanation.textContent = "";
          error.textContent = problem;
          error.hidden = false;
          return;
        }
        error.textContent = "";
        error.hidden = true;
        let px, lower, greater;
        if (p === 0 || p === 1) {
          const determined = p === 0 ? 0 : n;
          px = k === determined ? 1 : 0;
          lower = determined <= k ? 1 : 0;
          greater = determined >= k ? 1 : 0;
        } else {
          // Log factorials and log-sum-exp keep inclusive tails stable even
          // when subtracting from 1 would lose the small tail probability.
          const logFactorial = [0];
          for (let j = 1; j <= n; ++j)
            logFactorial[j] = logFactorial[j-1] + Math.log(j);
          const logP = Math.log(p), logQ = Math.log1p(-p);
          const terms = [];
          for (let j = 0; j <= n; ++j) {
            terms[j] = logFactorial[n] - logFactorial[j] - logFactorial[n-j] +
                       j*logP + (n-j)*logQ;
          }
          px = Math.exp(terms[k]);
          lower = inclusiveLogSum(terms, 0, k);
          greater = inclusiveLogSum(terms, k, n);
        }
        exact.textContent = format(px);
        cumulative.textContent = format(lower);
        upper.textContent = format(greater);
        mean.textContent = format(n*p);
        variance.textContent = format(n*p*(1-p));
        explanation.textContent = isArabic
          ? "عند n = " + n + " وp = " + p + "، احتمال الحصول على " + k +
            " نجاحات بالضبط هو " + format(px) +
            ". يشمل P(X ≤ " + k + ") جميع الأعداد حتى " + k +
            "، ويشمل P(X ≥ " + k + ") العدد " + k +
            " وما فوقه. هذه احتمالات لا تنبؤات مضمونة."
          : "For " + n + " trials with p = " + p +
            ", the chance of exactly " + k + " successes is " + format(px) +
            ". P(X ≤ " + k + ") includes up to " + k +
            " successes; P(X ≥ " + k + ") includes " + k +
            " and larger counts. These are probabilities, not predictions of a guaranteed count.";
      }
      form.addEventListener("input",render);
      form.addEventListener("change",render);
      form.addEventListener("submit",e => { e.preventDefault(); render(); });
      render();
    })();
