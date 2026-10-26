---
layout: default
title: ما الاحتمال الشرطي؟
description: شرح عربي للاحتمال الشرطي من خلال تقاطع الأحداث وتضييق فضاء العينة والاستقلال ومختبر تفاعلي لجداول التكرار.
permalink: /ar/probability/conditional/what-is-conditional-probability/
lang: ar
sidebar: false
translation_pair: conditional-probability-intro
math: true
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">الأحداث</span><span class="badge">المعلومات المشروطة</span></div>
<h1>ما الاحتمال الشرطي؟</h1>
<p><a href="/probability/conditional/what-is-conditional-probability/" lang="en" dir="ltr">English — What Is Conditional Probability?</a></p>
<p class="lead">الاحتمال الشرطي يصف احتمال وقوع حدث حين نعرف مسبقًا أن حدثًا آخر قد وقع. وتتغير مجموعة النتائج التي نحسب داخلها، فتتغير معها الاحتمالات أحيانًا.</p>
</div></section>
<section class="section"><div class="content-narrow">
<h2>ماذا يعني «بشرط أن»؟</h2>
<p>نفترض وجود حدثين A وB في فضاء عينة له نموذج احتمالي واضح. إذا علمنا تحقق B، فإننا ننظر فقط إلى النتائج المنتمية إلى B، ونسأل عن الجزء الذي ينتمي في الوقت نفسه إلى A.</p>
<div dir="ltr" class="esa-cp-math">\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)},\qquad P(B)>0.
\]</div>
<p>الرمز \(A\cap B\) يدل على تقاطع الحدثين، و\(P(B)>0\) شرط جوهري: إذا كان احتمال B يساوي صفرًا فلا تُعرِّف هذه الصيغة \(P(A\mid B)\) باستخدام التعريف الابتدائي للأحداث.</p>
<h2>مثال عملي</h2>
<p>في مجموعة تتكون من 100 نتيجة متساوية الوزن، تحقق A وB معًا في 20 نتيجة، وحدث A وحده في 10، وحدث B وحده في 30، ولم يحدث أي منهما في 40. إذن:</p>
<div dir="ltr" class="esa-cp-math">\[
P(A)=\frac{30}{100}=0.30,\quad
P(B)=\frac{50}{100}=0.50,\quad
P(A\cap B)=\frac{20}{100}=0.20.
\]</div>
<div dir="ltr" class="esa-cp-math">\[
P(A\mid B)=\frac{20}{50}=0.40,\qquad
P(B\mid A)=\frac{20}{30}\approx0.666667.
\]</div>
<p>تختلف \(P(A\mid B)\) عن \(P(B\mid A)\) عادةً؛ فتبديل الحدث الذي اشترطنا حدوثه يغيّر المقام والسؤال. ولا يجوز عكس الاحتمالات الشرطية بمجرد تغيير ترتيب الرموز.</p>
<h2>الاستقلال والاحتمال الشرطي</h2>
<p>إذا كان الحدثان مستقلين، فإن معرفتنا بتحقق B لا تغيّر احتمال A عندما يكون احتمال B موجبًا. يكافئ الاستقلال شرط تقاطع الأحداث:</p>
<div dir="ltr" class="esa-cp-math">\[
P(A\cap B)=P(A)P(B).
\]</div>
<p>في المثال أعلاه نحصل على \(0.20\ne0.30\times0.50\)، ولذلك لا يحقق جدول التكرارات شرط الاستقلال. لا ينبغي تعميم ذلك إلى مجتمع أوسع دون دراسة تصميم العينة وعدم اليقين.</p>
<h2>ملاحظات للتفسير الصحيح</h2>
<ul class="bullets">
<li>الاحتمال الشرطي ليس احتمال السبب بعد مشاهدة النتيجة إلا إذا حُدِّد الاتجاه المطلوب بدقة.</li>
<li>قد تزيد المعلومة احتمال حدث، أو تقلله، أو تتركه دون تغيير.</li>
<li>المساواة بين انعدام وقوع الحدث في جدول وبين استحالة وقوعه في المجتمع ليست صحيحة دائمًا؛ المختبر أدناه يستخدم التوزيع التجريبي المحدد بمدخلاته.</li>
<li>العلاقة الإحصائية لا تثبت سببيةً بمفردها.</li>
</ul>
</div></section>
<section class="section"><div class="content-narrow"><!-- Batch #73 — exact 2 × 2 conditional probability lab -->
<section class="concept-box" id="esa-conditional-lab" aria-labelledby="esa-cp-heading">
<h2 id="esa-cp-heading">مختبر الاحتمال الشرطي بجدول 2 × 2</h2>
<p>أدخل عدد المشاهدات في كل خلية من جدول الحدثين A وB. تمثل التكرارات مجتمعًا تجريبيًا من النتائج المتساوية الوزن؛ تُحسب الاحتمالات من النسب داخل الصفوف والأعمدة.</p>
<div class="esa-cp-grid">
<div><label for="esa-cp-ab">الحدثان A وB معًا</label><input id="esa-cp-ab" type="number" min="0" max="1000000" step="1" value="20" dir="ltr"></div>
<div><label for="esa-cp-aonly">A دون B</label><input id="esa-cp-aonly" type="number" min="0" max="1000000" step="1" value="10" dir="ltr"></div>
<div><label for="esa-cp-bonly">B دون A</label><input id="esa-cp-bonly" type="number" min="0" max="1000000" step="1" value="30" dir="ltr"></div>
<div><label for="esa-cp-neither">لا A ولا B</label><input id="esa-cp-neither" type="number" min="0" max="1000000" step="1" value="40" dir="ltr"></div>
</div>
<button type="button" class="btn btn-outline" id="esa-cp-reset">استعادة المثال</button>
<p role="status" aria-live="polite" id="esa-cp-warning" hidden></p>
<section id="esa-cp-results" aria-live="polite" aria-label="نتائج جدول الاحتمالات الشرطية">
<div class="table-wrap"><table>
<caption>جدول التقاطع الحصري للحدثين A وB</caption>
<thead><tr><th scope="col">الحدث A</th><th scope="col">B</th><th scope="col">ليس B</th></tr></thead>
<tbody><tr><th scope="row">A</th><td id="esa-cp-cell-ab">20</td><td id="esa-cp-cell-aonly">10</td></tr>
<tr><th scope="row">ليس A</th><td id="esa-cp-cell-bonly">30</td><td id="esa-cp-cell-neither">40</td></tr></tbody>
</table></div>
<div class="table-wrap"><table>
<caption>الاحتمالات والتكرارات (ست منازل عشرية)</caption>
<tbody><tr><th scope="row">المجموع N</th><td id="esa-cp-total">100</td></tr>
<tr><th scope="row">عدد A</th><td id="esa-cp-nA">30</td></tr>
<tr><th scope="row">عدد B</th><td id="esa-cp-nB">50</td></tr>
<tr><th scope="row">P(A)</th><td id="esa-cp-pa">0.300000</td></tr>
<tr><th scope="row">P(B)</th><td id="esa-cp-pb">0.500000</td></tr>
<tr><th scope="row">P(A ∩ B)</th><td id="esa-cp-pab">0.200000</td></tr>
<tr><th scope="row">P(A|B)</th><td id="esa-cp-agivenb">0.400000</td></tr>
<tr><th scope="row">P(B|A)</th><td id="esa-cp-bgivena">0.666667</td></tr>
</tbody></table></div>
<p id="esa-cp-interpretation"></p>
</section>
<p class="muted-mini">تساوي تكرارات أحد أحداث الشرط صفرًا يجعل الاحتمال المشروط عليه غير معرّف، وليس صفرًا. لا يُفسَّر هذا المثال بحد ذاته على أنه دليل على السببية أو الاستقلال الإحصائي في مجتمع أوسع.</p>
</section>
<style>
#esa-conditional-lab,#esa-conditional-lab *{box-sizing:border-box}
#esa-conditional-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-conditional-lab .esa-cp-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:12px 0}
#esa-conditional-lab label{display:block;font-weight:650}
#esa-conditional-lab input{display:block;width:100%;min-width:0;margin-top:5px;padding:10px;border:1px solid #777;border-radius:7px;font:inherit}
#esa-conditional-lab [hidden]{display:none!important}
#esa-conditional-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-conditional-lab td{font-variant-numeric:tabular-nums}
#esa-conditional-lab :is(input,button):focus-visible{outline:2px solid #0f766e;outline-offset:3px}
@media(max-width:620px){#esa-conditional-lab .esa-cp-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/conditional-frequency-explorer.js"></script>
<style>.esa-cp-math{max-width:100%;overflow-x:auto;direction:ltr}.esa-cp-math mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}</style>
<h2>الخلاصة</h2>
<p>يحسب الاحتمال الشرطي نسبة التقاطع داخل الحدث الذي نعرف وقوعه. ويتطلب تحديد الحدث الذي اشترطناه والتمييز بين الاحتمالين \(P(A\mid B)\) و\(P(B\mid A)\)، والتحقق من أن احتمال الحدث المشروط عليه موجب.</p>
<div class="lesson-nav">
<a class="btn btn-outline" href="/ar/probability/conditional/bayes-theorem/">التالي: نظرية بايز</a>
<a class="btn" href="/probability/conditional/what-is-conditional-probability/" lang="en" dir="ltr">English lesson →</a>
</div></div></section>