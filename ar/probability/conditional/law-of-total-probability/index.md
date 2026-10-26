---
layout: default
title: قانون الاحتمال الكلي
description: شرح عربي لقانون الاحتمال الكلي وتقسيم فضاء العينة ومخططات الاحتمالات ومثال ثلاث مجموعات ومختبر تفاعلي.
permalink: /ar/probability/conditional/law-of-total-probability/
lang: ar
sidebar: false
math: true
translation_pair: law-of-total-probability
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">التقسيم إلى مجموعات</span><span class="badge">نظرية بايز</span></div>
<h1>قانون الاحتمال الكلي (Law of Total Probability)</h1>
<p><a href="/probability/conditional/law-of-total-probability/" lang="en" dir="ltr">English — Law of Total Probability</a></p>
<p class="lead">نستخدم قانون الاحتمال الكلي عندما يمكن أن يحدث الحدث A عبر مسارات مختلفة وشاملة، فنحسب مساهمة كل مسار ثم نجمعها.</p>
</div></section>
<section class="section"><div class="content-narrow">
<h2>تقسيم فضاء العينة</h2>
<p>نفترض أن الأحداث B₁ وB₂ وB₃ تشكل تقسيمًا صحيحًا: فهي متنافية زوجيًا، واتحادها هو فضاء العينة كله، ومجموع احتمالاتها يساوي 1. لا يُجمع حدث مرتين، ولا تُستبعد نتائج ممكنة.</p>
<div dir="ltr" class="esa-tp-math">\[
B_i\cap B_j=\varnothing\ (i\ne j),\qquad \bigcup_{i=1}^{3}B_i=\Omega,\qquad \sum_{i=1}^{3}P(B_i)=1.
\]</div>
<h2>اشتقاق القانون</h2>
<p>يمكن تجزئة الحدث A إلى تقاطعاته مع المجموعات المتنافية، لذلك يساوي احتمال A مجموع احتمالات تلك التقاطعات. وبقاعدة الضرب نستنتج:</p>
<div dir="ltr" class="esa-tp-math">\[
P(A)=\sum_{i=1}^{3}P(A\cap B_i)
     =\sum_{i=1}^{3}P(A\mid B_i)P(B_i).
\]</div>
<p>يشترط تعريف P(A|Bᵢ) بالصيغة الابتدائية أن يكون P(Bᵢ) موجبًا. إذا كان وزن إحدى المجموعات صفرًا فهي لا تسهم في المجموع؛ ويمكن حذفها من الصيغة الشرطية دون تغيير P(A).</p>
<h2>مثال محلول: ثلاث مجموعات</h2>
<p>نفترض أن السكان ينقسمون إلى ثلاث مجموعات بأوزان 0.2 و0.3 و0.5، وأن احتمال وقوع A داخل كل مجموعة يساوي 0.1 و0.5 و0.8 على الترتيب. إذن مساهمات المجموعات هي:</p>
<div dir="ltr" class="esa-tp-math">\[
P(A)=0.2(0.1)+0.3(0.5)+0.5(0.8)
=0.02+0.15+0.40=0.57.
\]</div>
<h2>الفهم باستخدام شجرة احتمالات</h2>
<p>في شجرة احتمالات متعددة المسارات، نضرب احتمال الدخول إلى الفرع في احتمال وقوع A بشرط ذلك الفرع. وتُجمع نهايات الفروع المتنافية التي تؤدي إلى A. يؤدي نسيان وزن المجموعة أو جمع احتمالاتها الشرطية دون أوزان إلى جواب غير صحيح.</p>
<h2>تعميم القانون على مجموعات أكثر</h2>
<p>إذا كان لدينا تقسيم إلى k مجموعات متنافية وشاملة، فإن القانون يعمم إلى:</p>
<div dir="ltr" class="esa-tp-math">\[
P(A)=\sum_{i=1}^{k}P(B_i)P(A\mid B_i).
\]</div>
<p>عند كون المجموعات ذات أوزان صفرية، تُستخدم الصيغة المكافئة بمساهمات التقاطعات، أو تُحذف هذه المجموعات من مجموع الاحتمالات الشرطية غير المعرفة.</p>
<h2>صلة القانون بنظرية بايز</h2>
<p>يساعد القانون في حساب المقام في نظرية بايز، حيث نحسب احتمال الدليل عبر جميع أسبابه المحتملة قبل معرفة احتمال سبب بعينه بعد مشاهدة الدليل:</p>
<div dir="ltr" class="esa-tp-math">\[
P(B_j\mid A)=\frac{P(A\mid B_j)P(B_j)}
{\sum_i P(A\mid B_i)P(B_i)},\qquad P(A)>0.
\]</div>
<h2>الأخطاء الشائعة</h2>
<ul class="bullets"><li>جمع الاحتمالات الشرطية مباشرة دون وزنها باحتمالات المجموعات.</li>
<li>استخدام مجموعات متداخلة أو غير شاملة دون تصحيح أو تفصيل.</li>
<li>الخلط بين احتمال A داخل مجموعة واحتمال انتماء الملاحظة إلى تلك المجموعة.</li>
<li>اعتبار الصفر في مجموع أوزان المجموعات حالة عادية لتقسيم صحيح.</li></ul>
</div></section>
<section class="section"><div class="content-narrow"><!-- Batch #74: same shared calculation engine across Arabic and English -->
<section class="concept-box" id="esa-total-probability-lab" aria-labelledby="esa-tp-heading">
<h2 id="esa-tp-heading">مختبر قانون الاحتمال الكلي: ثلاث مجموعات</h2>
<p>افترض أن المجموعات الثلاث متنافية وشاملة لكل الحالات. عيّن وزن كل مجموعة واحتمال الحدث A داخلها. يجب أن يكون مجموع الأوزان 1.</p>
<div class="esa-tp-grid">
<div><label for="esa-tp-w1">وزن المجموعة 1</label><input id="esa-tp-w1" dir="ltr" type="number" min="0" max="1" step="any" value="0.2"></div>
<div><label for="esa-tp-w2">وزن المجموعة 2</label><input id="esa-tp-w2" dir="ltr" type="number" min="0" max="1" step="any" value="0.3"></div>
<div><label for="esa-tp-w3">وزن المجموعة 3</label><input id="esa-tp-w3" dir="ltr" type="number" min="0" max="1" step="any" value="0.5"></div>
<div><label for="esa-tp-p1">احتمال A | المجموعة 1</label><input id="esa-tp-p1" dir="ltr" type="number" min="0" max="1" step="any" value="0.1"></div>
<div><label for="esa-tp-p2">احتمال A | المجموعة 2</label><input id="esa-tp-p2" dir="ltr" type="number" min="0" max="1" step="any" value="0.5"></div>
<div><label for="esa-tp-p3">احتمال A | المجموعة 3</label><input id="esa-tp-p3" dir="ltr" type="number" min="0" max="1" step="any" value="0.8"></div>
</div>
<button type="button" class="btn btn-outline" id="esa-tp-reset">استعادة القيم الأصلية</button>
<p id="esa-tp-error" role="alert" aria-live="assertive" hidden></p>
<section id="esa-tp-results" aria-live="polite" aria-label="نتائج قانون الاحتمال الكلي">
<div class="table-wrap"><table><caption>مساهمات المجموعات (ست منازل عشرية)</caption><tbody>
<tr><th scope="row">مجموع الأوزان</th><td id="esa-tp-sum">—</td></tr>
<tr><th scope="row">مساهمة المجموعة 1</th><td id="esa-tp-c1">—</td></tr>
<tr><th scope="row">مساهمة المجموعة 2</th><td id="esa-tp-c2">—</td></tr>
<tr><th scope="row">مساهمة المجموعة 3</th><td id="esa-tp-c3">—</td></tr>
<tr><th scope="row">الاحتمال الكلي P(A)</th><td id="esa-tp-total">—</td></tr>
</tbody></table></div>
<svg id="esa-tp-chart" role="img" viewBox="0 0 610 270" dir="ltr" aria-label="رسم مساهمات المجموعات الثلاث"></svg>
<p id="esa-tp-explain"></p>
<p class="muted-mini">المجموعة ذات الوزن الصفري لا تساهم في النتيجة، ويجب عدم تفسير احتمالها الشرطي على أنه احتمال مشتق من بيانات مجموعة فارغة.</p>
</section>
</section>
<style>
#esa-total-probability-lab,#esa-total-probability-lab *{box-sizing:border-box}
#esa-total-probability-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-total-probability-lab .esa-tp-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:12px 0}
#esa-total-probability-lab label{display:block;font-weight:650}
#esa-total-probability-lab input{display:block;margin-top:5px;padding:10px;border:1px solid #777;border-radius:7px;font:inherit;width:100%;min-width:0}
#esa-total-probability-lab [hidden]{display:none!important}
#esa-total-probability-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-total-probability-lab svg{display:block;max-width:100%;height:auto;width:100%}
#esa-total-probability-lab :is(button,input):focus-visible{outline:2px solid #0f766e;outline-offset:3px}
@media(max-width:600px){#esa-total-probability-lab .esa-tp-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/total-probability-explorer.js"></script>
<style>.esa-tp-math{direction:ltr;max-width:100%;overflow-x:auto}.esa-tp-math mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}</style>
<h2>خلاصة</h2>
<p>الاحتمال الكلي هو متوسط مرجح لاحتمالات الحدث داخل مجموعات متنافية وشاملة. وهو حلقة أساسية بين الاحتمال الشرطي ونظرية بايز.</p>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/conditional/bayes-theorem/">التالي: نظرية بايز</a>
<a class="btn" href="/probability/conditional/law-of-total-probability/" lang="en" dir="ltr">English lesson →</a></div>
</div></section>