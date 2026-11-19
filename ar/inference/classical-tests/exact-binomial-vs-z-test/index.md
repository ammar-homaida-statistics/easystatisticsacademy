---
layout: default
title: الاختبار الحدّاني الدقيق مقابل اختبار Z لنسبة واحدة
description: "شرح عربي للمقارنة بين القيمة الاحتمالية الحدّانية الدقيقة وتقريب Z الطبيعي لنسبة واحدة، مع ترتيب الاحتمالات للاختبار ثنائي الطرف ومختبر تفاعلي."
permalink: /ar/inference/classical-tests/exact-binomial-vs-z-test/
lang: ar
sidebar: false
math: true
learning_resource: true
translation_pair: exact-binomial
---
<section class="hero hero-section"><div class="hero-card">
<h1>الاختبار الحدّاني الدقيق مقابل اختبار Z لنسبة واحدة</h1>
{% include lab-noscript.html %}
<p class="lead">ماذا يتغيّر عندما يحلّ اختبار دقيق متقطع محلّ التقريب الطبيعي، خاصة مع العينات الصغيرة والنسب المتطرفة؟</p>
<p><a href="/inference/classical-tests/exact-binomial-vs-z-test/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/classical-tests/one-proportion-z-test/">راجع درس اختبار Z لنسبة واحدة</a></p>
</div></section>
<section><div class="content-narrow">
<h2>1. ما الذي يفترضه الاختباران؟</h2>
<p>تحت الفرضية الصفرية يُنمذَج عدد النجاحات بالتوزيع \(X\sim\mathrm{Binomial}(n,p_0)\)، وهذا يتطلب مشاهدات برنولي مستقلة لها احتمال النجاح نفسه. يستخدم <strong>الاختبار الحدّاني الدقيق</strong> هذا التوزيع المتقطع دون تقريب طبيعي. أما <strong>اختبار Z المعتاد لنسبة واحدة</strong> فيستخدم الخطأ المعياري المبني على الفرضية الصفرية \(\sqrt{p_0(1-p_0)/n}\)، ويقرّب توزيع المعاينة تحت الفرضية الصفرية بالتوزيع الطبيعي المعياري.</p>
<h2>2. تعريف القيمة الاحتمالية الدقيقة ثنائية الطرف</h2>
<p>للاختبارات الحدّانية الدقيقة ثنائية الطرف عدة اصطلاحات مقبولة. يستخدم هذا المختبر <strong>ترتيب الاحتمالات</strong>، كما في الإعداد الافتراضي لدالة <code dir="ltr">scipy.stats.binomtest</code>: نجمع احتمالات جميع النتائج التي لا يزيد احتمالها تحت الفرضية الصفرية على احتمال العدد المشاهد، مع تسامح عددي صغير للتساوي فقط. وهذه القيمة <strong>ليست</strong> دائمًا ضعف أصغر قيمة أحادية الطرف.</p>
<div class="esa-eb-equation" dir="ltr" tabindex="0" role="region" aria-label="القيمة الاحتمالية الحدّانية الدقيقة بترتيب الاحتمالات">
\[
P_{\mathrm{exact}}=\sum_{\{k:\Pr_{p_0}(X=k)\leq\Pr_{p_0}(X=x)\}}\Pr_{p_0}(X=k).
\]
</div>
<p>للبديل «أكبر» نستخدم \(\Pr_{p_0}(X\ge x)\)، وللبديل «أصغر» نستخدم \(\Pr_{p_0}(X\le x)\). ويستخدم اختبار Z التقريبي الأطراف المقابلة من التوزيع الطبيعي المعياري. وقد تجعل التكرارات المتوقعة الصغيرة \(np_0\) أو \(n(1-p_0)\) هذا التقريب غير موثوق.</p>
<h2>3. مقارنة تفاعلية بين الدقيق والتقريبي</h2>
<section id="esa-exact-binomial-lab" class="concept-box" data-locale="ar" aria-labelledby="esa-eb-heading">
<h3 id="esa-eb-heading">قارن قيمتين احتماليتين بالفرضيتين نفسيهما</h3>
<p>تقتصر الحسابات الدقيقة على \(n\le 2{,}000\) لسرعة الاستجابة في المتصفح. لا تغادر أي قيمة متصفحك.</p>
<div class="esa-eb-grid">
<label for="esa-eb-x">عدد النجاحات المشاهد \(x\)<input id="esa-eb-x" dir="ltr" type="number" min="0" step="1" value="2" aria-invalid="false" aria-describedby="esa-eb-error"></label>
<label for="esa-eb-n">حجم العينة \(n\) (من 1 إلى 2000)<input id="esa-eb-n" dir="ltr" type="number" min="1" max="2000" step="1" value="10" aria-invalid="false" aria-describedby="esa-eb-error"></label>
<label for="esa-eb-p0">الاحتمال تحت الفرضية الصفرية \(p_0\)<input id="esa-eb-p0" dir="ltr" type="number" min="0" max="1" step="any" value="0.5" aria-invalid="false" aria-describedby="esa-eb-error"></label>
<label for="esa-eb-side">الفرضية البديلة<select id="esa-eb-side"><option value="two-sided">ثنائية الطرف</option><option value="greater">أكبر</option><option value="less">أصغر</option></select></label>
</div>
<button id="esa-eb-reset" class="btn btn-outline" type="button">إعادة المثال</button>
<p id="esa-eb-error" role="alert" hidden></p>
<div id="esa-eb-results" aria-live="polite" aria-atomic="true">
<div class="table-wrap"><table><caption>القيمتان الاحتماليتان الدقيقة والتقريبية تحت الفرضية نفسها</caption><thead><tr><th scope="col">الطريقة</th><th scope="col">القيمة الاحتمالية</th></tr></thead><tbody>
<tr><th scope="row">الحدّاني الدقيق</th><td><output id="esa-eb-exact" dir="ltr"></output></td></tr>
<tr><th scope="row">تقريب Z الطبيعي، دون تصحيح الاستمرارية</th><td><output id="esa-eb-approx" dir="ltr"></output></td></tr>
<tr><th scope="row">الفرق المطلق</th><td><output id="esa-eb-difference" dir="ltr"></output></td></tr>
</tbody></table></div>
<p id="esa-eb-counts" dir="ltr"></p>
<svg id="esa-eb-plot" viewBox="0 0 620 125" role="img" dir="ltr" aria-label="مقارنة قيمتين احتماليتين" style="display:block;width:100%;max-width:100%;height:auto"></svg>
<p id="esa-eb-warning" role="status"></p><p id="esa-eb-interpret"></p>
</div></section>
<h2>4. مثال عددي محلول</h2>
<p>عندما \(x=2\) و\(n=10\) و\(p_0=0.5\)، تكون القيمة الاحتمالية الدقيقة ثنائية الطرف بترتيب الاحتمالات \(0.109375\)، لأن النتائج التي لا يزيد احتمالها على \(\Pr(X=2)\) هي \(\{0,1,2,8,9,10\}\)، ومجموع احتمالاتها \(112/1024\). أما تقريب Z فيعطي \(z=(0.2-0.5)/\sqrt{0.025}\)، أي \(z\approx-1.897\)، وقيمة احتمالية \(\approx0.057780\)، أي نحو نصف القيمة الدقيقة، لأن حجم العينة صغير. وزيادة \(n\) وتجنّب التكرارات المتوقعة الصغيرة يحسّنان التقريب غالبًا، لكنهما لا يجعلان التعريفين متطابقين لكل نتيجة متقطعة.</p>
<p>لمقارنة <strong>مجموعتين مستقلتين</strong> راجع <a href="/ar/inference/classical-tests/two-proportion-z-test/">اختبار Z لنسبتين</a> و<a href="/ar/inference/classical-tests/fisher-exact-vs-chi-square/">اختبار فيشر الدقيق مقابل كاي تربيع لجداول 2×2</a>. فالاختبار الحدّاني الدقيق لنسبة واحدة ليس بديلًا عن هذين التصميمين المختلفين.</p>
<h2>5. حدود التفسير</h2>
<p>الحساب الدقيق دقيق <em>بشرط صحة نموذج حدّاني مستقل</em>؛ فهو لا يعالج تحيّز الملاحظة، ولا البيانات العنقودية، ولا الاعتماد بين المشاهدات، ولا اختيار الفرضيات غير المخطط له. ولا تقيس أيّ القيمتين احتمال أن تكون الفرضية الصفرية صحيحة. وينبغي النظر في طرق فترات الثقة بشكل منفصل.</p>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>يستخدم الاختبار الدقيق التوزيع الحدّاني نفسه، ويستخدم اختبار Z تقريبًا طبيعيًا.</li>
<li>القيمة الدقيقة ثنائية الطرف هنا مبنية على ترتيب الاحتمالات، لا على مضاعفة طرف واحد.</li>
<li>مع العينات الصغيرة أو النسب المتطرفة قد يختلف الاختباران اختلافًا كبيرًا.</li>
<li>كلاهما يفترض مشاهدات مستقلة باحتمال نجاح ثابت.</li>
</ul></div>
<div class="lesson-nav">
<a class="btn btn-outline" href="/ar/inference/classical-tests/one-proportion-z-test/">→ اختبار Z لنسبة واحدة</a>
<a class="btn" href="/ar/inference/classical-tests/">الاختبارات الكلاسيكية ←</a>
</div>
</div></section>
<style>
#esa-exact-binomial-lab{box-sizing:border-box;min-width:0;max-width:100%;overflow-wrap:anywhere}
#esa-exact-binomial-lab .esa-eb-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:14px 0}
#esa-exact-binomial-lab label{display:block;min-width:0;font-weight:600}
#esa-exact-binomial-lab :is(input,select){display:block;width:100%;min-width:0;max-width:100%;box-sizing:border-box;font:inherit;padding:9px;border:1px solid var(--border);border-radius:8px;background:var(--surface);color:var(--text)}
#esa-exact-binomial-lab [hidden]{display:none!important}
#esa-exact-binomial-lab .table-wrap{display:block;max-width:100%;overflow-x:auto}
#esa-exact-binomial-lab :is(input,select,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-eb-equation{max-width:100%;overflow-x:auto;padding:8px 0}
@media(max-width:650px){#esa-exact-binomial-lab .esa-eb-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/one-proportion-z-explorer.js"></script>
<script defer src="/js/exact-binomial-vs-z.js"></script>
