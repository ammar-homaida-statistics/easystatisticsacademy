---
layout: default
title: الاختبارات الإحصائية الكلاسيكية
description: "دليل عربي للاختبارات الإحصائية الكلاسيكية: اختبارات Z وt وكاي تربيع وتحليل التباين، مع أداة لاختيار الاختبار المناسب والمختبرات التفاعلية المرافقة."
permalink: /ar/inference/classical-tests/
lang: ar
sidebar: false
learning_resource: true
translation_pair: classical-tests-hub
---
<section class="hero hero-section"><div class="hero-card">
<h1>الاختبارات الإحصائية الكلاسيكية</h1>
<p class="lead">الاختبارات الكلاسيكية هي الأدوات المعيارية لتقييم الفرضيات حول المتوسطات والنسب وتوزيعات الفئات. يجمع هذا القسم الدروس العربية المتاحة بترتيب التعلّم المقترح، مع أداة تساعدك على اختيار الاختبار المناسب لسؤالك البحثي.</p>
<p><a href="/inference/classical-tests/" lang="en" dir="ltr">English version</a> · <a href="/ar/">الصفحة العربية الرئيسية</a></p>
</div></section>
<section class="section" id="ar-test-guide-section" aria-labelledby="ar-test-guide-heading"><div class="content-narrow">
<h2 id="ar-test-guide-heading">اختر الاختبار الإحصائي المناسب</h2>
<p>النتيجة نقطة انطلاق فقط: تحقق دائمًا من تصميم الدراسة والاستقلال وافتراضات التوزيع وحجم العينة.</p>
<div class="card" id="esa-ar-test-guide">
<label for="esa-ar-test-outcome"><strong>ما نوع النتيجة التي تحللها؟</strong></label>
<select id="esa-ar-test-outcome">
<option value="mean">قياس كمي / متوسط المجتمع</option>
<option value="binary">نتيجة ثنائية (نعم/لا) / نسبة المجتمع</option>
<option value="categorical">تكرارات فئوية / توزيع الفئات</option>
</select>
<label for="esa-ar-test-design"><strong>ما تصميم الدراسة أو السؤال؟</strong></label>
<select id="esa-ar-test-design">
<option value="one">عينة واحدة مقارنة بقيمة مرجعية</option>
<option value="paired">مشاهدات مزدوجة / متطابقة</option>
<option value="independent">عينتان أو مجموعتان مستقلتان</option>
<option value="multiple">ثلاث مجموعات مستقلة أو أكثر</option>
<option value="association">ارتباط بين متغيرين فئويين</option>
</select>
<div id="esa-ar-test-sigma-wrapper">
<label for="esa-ar-test-sigma"><strong>لمتوسط عينة واحدة: هل σ السكاني معلوم؟</strong></label>
<select id="esa-ar-test-sigma">
<option value="unknown">لا — استخدم الانحراف المعياري للعينة</option>
<option value="known">نعم — σ معلوم فعلًا</option>
</select>
</div>
<div id="esa-ar-test-result" role="status" aria-live="polite" aria-atomic="true">اختر نوع النتيجة والتصميم لعرض التوصية.</div>
</div>
<noscript><p class="esa-noscript" role="note">تتطلب أداة اختيار الاختبار تفعيل JavaScript. يمكنك استخدام قائمة الدروس أدناه لمقارنة الاختبارات وافتراضاتها.</p></noscript>
</div></section>
<section class="section" id="lessons" aria-labelledby="ar-lessons-heading"><div class="content-narrow">
<h2 id="ar-lessons-heading">الدروس بترتيب التعلّم</h2>
<ol class="bullets esa-ar-hub-list">
  <li><a href="/ar/inference/classical-tests/decision-framework-and-assumptions/">إطار اتخاذ القرار والافتراضات</a></li>
  <li><a href="/ar/inference/classical-tests/one-sample-z-test-for-mean/">اختبار Z لعينة واحدة لمتوسط المجتمع</a></li>
  <li><a href="/ar/inference/classical-tests/one-sample-t-test-for-mean/">اختبار t لعينة واحدة لمتوسط المجتمع</a></li>
  <li><a href="/ar/inference/classical-tests/paired-t-test/">اختبار t للعينات المزدوجة</a></li>
  <li><a href="/ar/inference/classical-tests/two-sample-t-test-independent/">اختبار t لعينتين مستقلتين</a></li>
  <li><a href="/ar/inference/classical-tests/one-proportion-z-test/">اختبار Z لنسبة مجتمع واحد</a></li>
  <li><a href="/ar/inference/classical-tests/two-proportion-z-test/">اختبار Z لنسبتين مستقلتين</a></li>
  <li><a href="/ar/inference/classical-tests/chi-square-goodness-of-fit/">اختبار كاي تربيع لحسن المطابقة</a></li>
  <li><a href="/ar/inference/classical-tests/chi-square-independence-test/">اختبار كاي تربيع للاستقلال</a></li>
  <li><a href="/ar/inference/classical-tests/chi-square-homogeneity-test/">اختبار كاي تربيع للتجانس</a></li>
  <li><a href="/ar/inference/classical-tests/one-way-anova-f-test/">تحليل التباين الأحادي (اختبار F)</a></li>
  <li><a href="/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/" hreflang="en">الاختبارات البعدية والمقارنات المتعددة</a> <span class="muted-mini">(بالإنجليزية)</span></li>
</ol>
<h2 id="ar-labs-heading">المختبرات المرافقة</h2>
<ul class="bullets esa-ar-hub-list">
  <li><a href="/ar/inference/classical-tests/mcnemar-test/">اختبار ماكنمار للنسب المزدوجة</a></li>
  <li><a href="/inference/classical-tests/fisher-exact-vs-chi-square/" hreflang="en">اختبار فيشر الدقيق مقابل كاي تربيع</a> <span class="muted-mini">(بالإنجليزية)</span></li>
  <li><a href="/inference/classical-tests/exact-binomial-vs-z-test/" hreflang="en">اختبار ذات الحدين الدقيق مقابل اختبار Z</a> <span class="muted-mini">(بالإنجليزية)</span></li>
  <li><a href="/inference/classical-tests/welch-pooled-monte-carlo/" hreflang="en">مختبر مونت كارلو: ويلش مقابل التباين المشترك</a> <span class="muted-mini">(بالإنجليزية)</span></li>
  <li><a href="/ar/inference/classical-tests/cohens-kappa/">معامل كوهين كابا لاتفاق المقيّمين</a></li>
</ul>
<p class="muted-mini">الروابط المشار إليها بـ(بالإنجليزية) تنقلك إلى الدرس الإنجليزي حتى تتوفر نسخته العربية.</p>
</div></section>
<style>
#esa-ar-test-guide select{display:block;box-sizing:border-box;width:100%;max-width:100%;padding:10px;margin:8px 0 16px;font:inherit}
#esa-ar-test-guide [hidden]{display:none!important}
#esa-ar-test-result{padding:12px;border:1px solid currentColor;border-radius:8px;margin-top:12px;overflow-wrap:anywhere}
#esa-ar-test-guide :is(select,a):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-ar-hub-list li{margin:6px 0}
</style>
<script>
(function () {
  "use strict";
  const guide = document.getElementById("esa-ar-test-guide");
  if (!guide) return;
  const outcome = guide.querySelector("#esa-ar-test-outcome");
  const design = guide.querySelector("#esa-ar-test-design");
  const sigma = guide.querySelector("#esa-ar-test-sigma");
  const sigmaWrapper = guide.querySelector("#esa-ar-test-sigma-wrapper");
  const result = guide.querySelector("#esa-ar-test-result");
  // Same recommendation table as the English hub; [url, name, note, arabicAvailable].
  const methods = {
 "mean-one-unknown": [
  "/ar/inference/classical-tests/one-sample-t-test-for-mean/",
  "اختبار t لعينة واحدة لمتوسط المجتمع",
  "عندما تكون المشاهدات مستقلة والانحراف المعياري السكاني σ مجهولًا. الدقة في العينات الصغيرة تفترض توزيعًا طبيعيًا تقريبًا.",
  true
 ],
 "mean-one-known": [
  "/ar/inference/classical-tests/one-sample-z-test-for-mean/",
  "اختبار Z لعينة واحدة لمتوسط المجتمع",
  "يتطلب σ معلومًا فعلًا، ومشاهدات مستقلة، وتوزيع معاينة طبيعيًا للمتوسط.",
  true
 ],
 "mean-paired": [
  "/ar/inference/classical-tests/paired-t-test/",
  "اختبار t للعينات المزدوجة",
  "يحلل الفروق داخل الأزواج؛ يجب أن تكون الأزواج مستقلة، والاستدلال في العينات الصغيرة يفترض فروقًا طبيعية تقريبًا.",
  true
 ],
 "mean-independent": [
  "/ar/inference/classical-tests/two-sample-t-test-independent/",
  "اختبار t لعينتين مستقلتين (ويلش)",
  "لمجموعتين مستقلتين؛ يقدّر اختبار ويلش تباينًا منفصلًا لكل مجموعة. تحقق من الاستقلال وشكل التوزيع.",
  true
 ],
 "mean-multiple": [
  "/ar/inference/classical-tests/one-way-anova-f-test/",
  "تحليل التباين الأحادي",
  "لمقارنة متوسطات ثلاث مجموعات مستقلة أو أكثر؛ يفترض أخطاء مستقلة وتوزيعًا طبيعيًا تقريبًا وتباينات متقاربة.",
  true
 ],
 "binary-one": [
  "/ar/inference/classical-tests/one-proportion-z-test/",
  "اختبار Z لنسبة مجتمع واحد",
  "لمحاولات ثنائية مستقلة مع عدد كافٍ من النجاحات والإخفاقات المتوقعة تحت الفرضية الصفرية.",
  true
 ],
 "binary-paired": [
  "/ar/inference/classical-tests/mcnemar-test/",
  "اختبار ماكنمار للنسب المزدوجة",
  "عندما تعطي الوحدات نفسها نتيجة ثنائية مرتين (قبل/بعد، أو مقيّمان، أو اختباران تشخيصيان). الأزواج المتغيّرة وحدها تحمل المعلومة؛ فضّل القيمة الدقيقة عند قلة هذه الأزواج.",
  true
 ],
 "binary-independent": [
  "/ar/inference/classical-tests/two-proportion-z-test/",
  "اختبار Z لنسبتين مستقلتين",
  "لمقارنة نسب مجموعتين مستقلتين عندما تبرر التكرارات المتوقعة التقريب الطبيعي؛ العينات الصغيرة قد تحتاج طرقًا دقيقة.",
  true
 ],
 "categorical-one": [
  "/ar/inference/classical-tests/chi-square-goodness-of-fit/",
  "اختبار كاي تربيع لحسن المطابقة",
  "لمقارنة تكرارات فئات متغير واحد بتوزيع احتمالي محدد مسبقًا؛ مشاهدات مستقلة وتكرارات متوقعة كافية.",
  true
 ],
 "categorical-independent": [
  "/ar/inference/classical-tests/chi-square-homogeneity-test/",
  "اختبار كاي تربيع للتجانس",
  "لمقارنة توزيعات فئوية بين مجتمعات أو مجموعات سُحبت منها عينات مستقلة.",
  true
 ],
 "categorical-association": [
  "/ar/inference/classical-tests/chi-square-independence-test/",
  "اختبار كاي تربيع للاستقلال",
  "لاختبار الارتباط بين متغيرين فئويين مُقاسين على عينة واحدة من مشاهدات مستقلة.",
  true
 ]
};
  function update() {
    sigmaWrapper.hidden = !(outcome.value === "mean" && design.value === "one");
    const suffix = outcome.value === "mean" && design.value === "one" ? "-" + sigma.value : "";
    const choice = methods[outcome.value + "-" + design.value + suffix];
    result.replaceChildren();
    if (!choice) {
      result.textContent = "هذا الجمع يحتاج إلى طريقة مختلفة خاصة بالتصميم. راجع نوع النتيجة وبنية المعاينة، واطّلع على الدروس أدناه أو على مرجع إحصائي.";
      return;
    }
    const heading = document.createElement("strong");
    heading.textContent = "نقطة انطلاق مقترحة: ";
    const link = document.createElement("a");
    link.href = choice[0];
    link.textContent = choice[1] + (choice[3] ? "" : " (بالإنجليزية)");
    const explanation = document.createElement("p");
    explanation.textContent = choice[2];
    result.append(heading, link, explanation);
  }
  outcome.addEventListener("change", update);
  design.addEventListener("change", update);
  sigma.addEventListener("change", update);
  update();
})();
</script>
