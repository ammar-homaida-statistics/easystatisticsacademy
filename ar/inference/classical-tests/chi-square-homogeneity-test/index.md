---
layout: default
title: اختبار كاي تربيع للتجانس
description: شرح عربي لاختبار كاي تربيع للتجانس لمقارنة توزيع متغير فئوي بين عدة مجتمعات مستقلة، مع التكرارات المتوقعة والبواقي المعدّلة ومختبر تفاعلي.
permalink: /ar/inference/classical-tests/chi-square-homogeneity-test/
lang: ar
sidebar: false
learning_resource: true
translation_pair: chi-square-homogeneity
---
<section class="hero hero-section"><div class="hero-card">
<h1>اختبار كاي تربيع للتجانس</h1>
<p class="lead">هل تتوزع فئات متغير واحد بالنسب نفسها في عدة مجتمعات مستقلة؟ يوضح هذا الدرس كيف يقارن اختبار بيرسون للتجانس (Pearson chi-square test of homogeneity) التكرارات المشاهدة بالتكرارات المتوقعة عند تساوي التوزيعات، وكيف نحدد الخلايا التي تقود الفرق بالبواقي المعدّلة.</p>
<p><a href="/inference/classical-tests/chi-square-homogeneity-test/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/classical-tests/chi-square-independence-test/">الدرس السابق: اختبار كاي تربيع للاستقلال</a></p>
</div></section>
<section><div class="content-narrow">
<h2>1. سؤال البحث</h2>
<p>لنفترض أننا سحبنا عينة مستقلة من العملاء في كل من ثلاث مدن، وسألنا كل عميل عن المنتج الذي يفضّله من بين ثلاثة منتجات A وB وC. السؤال: هل نسب تفضيل المنتجات متماثلة في المدن الثلاث، أم أن توزيع التفضيل يختلف من مدينة إلى أخرى؟</p>
<h2>2. التجانس مقابل الاستقلال</h2>
<p>تُحسب إحصائية بيرسون بالصيغة نفسها في الاختبارين، لكن <strong>تصميم المعاينة</strong> مختلف:</p>
<ul class="bullets"><li>في <a href="/ar/inference/classical-tests/chi-square-independence-test/">اختبار الاستقلال</a> نسحب عينة واحدة ونصنف كل فرد وفق متغيرين؛ فمجاميع الصفوف والأعمدة كلاهما عشوائي.</li><li>في <strong>اختبار التجانس</strong> نسحب عينات مستقلة من مجتمعات محددة مسبقًا (المدن هنا)، فتكون أحجام العينات (مجاميع الصفوف) ثابتة بالتصميم، ونقارن توزيع متغير واحد بينها.</li></ul>
<p>لذلك تختلف صياغة الفرضيتين وتفسير النتيجة، رغم تطابق الحساب.</p>
<h2>3. الفرضيتان الإحصائيتان</h2>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="فرضيتا اختبار التجانس">
\[
H_0:\ p_{1j}=p_{2j}=\cdots=p_{rj}\ \text{for every category } j
\qquad\text{vs}\qquad
H_a:\ \text{at least one population differs.}
\]</div>
<p>الفرضية الصفرية \(H_0\): توزيع الفئات واحد في جميع المجتمعات. الفرضية البديلة \(H_a\): يختلف توزيع الفئات في مجتمع واحد على الأقل. لا تحدد \(H_a\) أي المجتمعات أو الفئات تختلف.</p>
<h2>4. مثال محلول: ثلاث مدن</h2>
<div class="table-wrap"><table><caption>التكرارات المشاهدة</caption><thead><tr><th scope="col">المدينة</th><th scope="col">المنتج A</th><th scope="col">المنتج B</th><th scope="col">المنتج C</th><th scope="col">المجموع</th></tr></thead><tbody><tr><th scope="row">المدينة 1</th><td>40</td><td>35</td><td>25</td><td>100</td></tr><tr><th scope="row">المدينة 2</th><td>30</td><td>45</td><td>25</td><td>100</td></tr><tr><th scope="row">المدينة 3</th><td>50</td><td>30</td><td>20</td><td>100</td></tr><tr><th scope="row">المجموع</th><td>120</td><td>110</td><td>70</td><td>300</td></tr></tbody></table></div>
<h2>5. التكرارات المتوقعة</h2>
<p>إذا كانت التوزيعات متساوية، فإن أفضل تقدير لنسبة كل فئة هو نسبتها في العينات مجتمعة، ومن ثم:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="صيغة التكرار المتوقع">
\[
E_{ij}=\frac{R_i\,C_j}{N},\qquad E_{\text{City 1},A}=\frac{100\times120}{300}=40,\quad E_{\text{City 1},B}=\frac{100\times110}{300}\approx36.667.
\]</div>
<p>ولأن مجاميع الصفوف متساوية هنا، فالتكرارات المتوقعة في كل مدينة هي \(40\) و\(36.667\) و\(23.333\).</p>
<h2>6. إحصائية بيرسون ودرجات الحرية</h2>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="إحصائية اختبار التجانس">
\[
\chi^2=\sum_{i=1}^{r}\sum_{j=1}^{c}\frac{(O_{ij}-E_{ij})^2}{E_{ij}},\qquad df=(r-1)(c-1)=(3-1)(3-1)=4.
\]</div>
<p>بجمع مساهمات الخلايا التسع نحصل على:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="نتيجة المثال">
\[
\chi^2\approx8.8961,\qquad df=4,\qquad P(\chi^2_4\ge8.8961)\approx0.0637.
\]</div>
<p>عند مستوى دلالة \(\alpha=0.05\) <strong>لا نرفض</strong> فرضية تساوي التوزيعات، لأن \(0.0637>0.05\). وهذا لا يثبت أن التوزيعات متطابقة؛ بل يعني أن البيانات لم تقدم دليلًا كافيًا ضد التجانس عند هذا المستوى. والقيمة الاحتمالية تقريبية تعتمد على توزيع كاي تربيع للعينات الكبيرة، دون تصحيح للاستمرارية.</p>
<h2>7. أي الخلايا تقود الفرق؟ البواقي المعيارية المعدّلة</h2>
<p>لا يحدد الاختبار الكلي مواضع الاختلاف. لهذا نحسب لكل خلية البواقي المعيارية المعدّلة (Haberman, 1973):</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="البواقي المعدلة">
\[
r_{ij}=\frac{O_{ij}-E_{ij}}{\sqrt{E_{ij}\left(1-\frac{R_i}{N}\right)\left(1-\frac{C_j}{N}\right)}}.
\]</div>
<p>تحت \(H_0\) يتبع كل \(r_{ij}\) تقريبًا التوزيع الطبيعي المعياري في العينات الكبيرة، لذا تشير القيمة \(|r_{ij}|>2\) إلى خلية تختلف فيها التكرارات المشاهدة بوضوح عن المتوقعة. في مثالنا: \(r=-2.5\) للمدينة 2 مع المنتج A، و\(r\approx2.118\) للمدينة 2 مع المنتج B، و\(r=2.5\) للمدينة 3 مع المنتج A.</p>
<p><strong>تنبيه مهم:</strong> ظهور ثلاث خلايا بقيمة \(|r|>2\) رغم أن الاختبار الكلي غير دال (\(p\approx0.064\)) ليس تناقضًا. فالبواقي مؤشرات <strong>وصفية</strong> لا اختبارات دلالة مستقلة، ومع تسع خلايا قد تتجاوز بعض القيم 2 بالصدفة؛ وتصحيح من نوع بونفيروني يكون أشد صرامة.</p>
<h2>8. مختبر التجانس التفاعلي</h2>
<section id="esa-homogeneity-lab" class="concept-box" data-locale="ar" aria-labelledby="esa-hom-title">
<h3 id="esa-hom-title">مختبر كاي تربيع التفاعلي للتجانس</h3>
<noscript><p class="esa-noscript" role="note">يتطلب هذا المختبر التفاعلي تفعيل JavaScript. من دونه تبقى الأرقام المعروضة هي المثال المحلول الثابت، وتظل الصيغ والتفسير في الدرس متاحة.</p></noscript>
<p>أدخل جدول توافق: كل سطر مجتمع، وكل عمود فئة. افصل بين الأعداد الصحيحة غير السالبة بفاصلة إنجليزية، وابدأ سطرًا جديدًا لكل مجتمع (2–5 صفوف، و2–5 أعمدة).</p>
<label for="esa-hom-input">التكرارات المشاهدة في جدول المجتمع × الفئة</label>
<textarea id="esa-hom-input" dir="ltr" rows="4" spellcheck="false" aria-describedby="esa-hom-error esa-hom-warning" aria-invalid="false">40, 35, 25
30, 45, 25
50, 30, 20</textarea>
<div class="esa-hom-controls">
<button type="button" class="btn btn-outline" id="esa-hom-cities">مثال المدن الثلاث</button>
<button type="button" class="btn btn-outline" id="esa-hom-balanced">نسب متساوية</button>
<button type="button" class="btn btn-outline" id="esa-hom-unequal">أحجام مجموعات غير متساوية</button>
<button type="button" class="btn btn-outline" id="esa-hom-sparse">تكرارات قليلة</button>
</div>
<p id="esa-hom-error" role="alert" hidden></p>
<section id="esa-hom-results" aria-live="polite" aria-atomic="true" aria-label="نتائج اختبار كاي تربيع للتجانس">
<h4>النسب المئوية للفئات داخل كل مجتمع</h4>
<svg id="esa-hom-chart" viewBox="0 0 620 210" role="img" aria-label="النسب المئوية للفئات داخل كل مجتمع"></svg>
<p class="muted-mini">تعرض كل مجموعة أعمدة حصة فئة واحدة <strong>داخل كل مجتمع</strong>؛ وتميّز الألوان المجتمعات 1–5 (أخضر مزرق، رمادي، بنفسجي، برتقالي، أزرق). مقارنة النسب، لا الأعداد الخام، هي التي تكشف الفروق عندما تختلف أحجام المجموعات.</p>
<div class="table-wrap"><table id="esa-hom-table" aria-label="التكرارات المشاهدة والمتوقعة ومساهمات كاي تربيع"></table></div>
<p><strong>الحجم الكلي N:</strong> <output id="esa-hom-n" dir="ltr">300</output>.
<strong>إحصائية بيرسون χ²:</strong> <output id="esa-hom-chi" dir="ltr">8.896104</output>.
<strong>درجات الحرية:</strong> <output id="esa-hom-df" dir="ltr">4</output>.
<strong>القيمة الاحتمالية للطرف الأيمن:</strong> <output id="esa-hom-p" dir="ltr">0.063750</output>.</p>
<p id="esa-hom-warning" role="status" aria-live="polite">جميع التكرارات المتوقعة لا تقل عن 5.</p>
<p id="esa-hom-decision">عند α = 0.05 لا نرفض تساوي توزيعات الفئات.</p>
<h4>أي الخلايا تقود الفرق؟ البواقي المعدّلة</h4>
<div class="table-wrap"><table id="esa-hom-residuals"></table></div>
<p id="esa-hom-residual-note">3 من 9 خلايا لها |r| &gt; 2.</p>
</section>
<p class="muted-mini">التكرار المتوقع للخلية <strong>(i,j)</strong> هو <strong>(مجموع الصف × مجموع العمود) / N</strong>، ودرجات الحرية <strong>(الصفوف − 1)(الأعمدة − 1)</strong>. القيمة الاحتمالية هي الطرف الأيمن التقريبي دون تصحيح ييتس. تُرفض الجداول التي فيها صف أو عمود أصفاره كاملة لأن التكرارات المتوقعة تنعدم.</p>
</section>
<h2>9. الافتراضات والقيود</h2>
<ul class="bullets"><li>عينات مستقلة من المجتمعات، ومشاهدات مستقلة داخل كل عينة.</li><li>فئات متنافية وشاملة، وكل مشاهدة تُعدّ مرة واحدة.</li><li>تكرارات متوقعة كافية؛ والقاعدة الشائعة \(E_{ij}\ge5\) إرشادية لا شرطًا رياضيًا مطلقًا. ينبّه المختبر إلى الخلايا الصغيرة ولا يحذفها.</li><li>رفض \(H_0\) لا يثبت السببية، ولا يحدد وحده كل مجتمع مختلف.</li></ul>
<p><a href="/ar/inference/classical-tests/chi-square-independence-test/">اختبار كاي تربيع للاستقلال</a> · <a href="/ar/inference/classical-tests/chi-square-goodness-of-fit/">اختبار كاي تربيع لحسن المطابقة</a></p>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets"><li>يقارن التجانس توزيع متغير فئوي واحد بين عدة مجتمعات مستقلة.</li><li>\(E_{ij}=R_iC_j/N\)، و\(\chi^2=\sum(O_{ij}-E_{ij})^2/E_{ij}\) بدرجات حرية \((r-1)(c-1)\).</li><li>الحساب مطابق لاختبار الاستقلال، لكن تصميم المعاينة والتفسير مختلفان.</li><li>البواقي المعدّلة تحدد مواضع الاختلاف وصفيًا، ولا تحل محل الاختبار الكلي.</li><li>عدم رفض \(H_0\) لا يثبت تطابق التوزيعات.</li></ul></div>
</div></section>
<style>
#esa-homogeneity-lab{box-sizing:border-box;max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-homogeneity-lab label{display:block;font-weight:650;margin-bottom:8px}
#esa-homogeneity-lab textarea{display:block;box-sizing:border-box;width:100%;max-width:100%;min-width:0;padding:10px;font:inherit;color:var(--text);background:var(--surface);border:1px solid var(--border);border-radius:8px;resize:vertical}
#esa-homogeneity-lab .esa-hom-controls{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
#esa-homogeneity-lab .esa-hom-controls button{max-width:100%;white-space:normal}
#esa-homogeneity-lab [hidden]{display:none!important}
#esa-homogeneity-lab #esa-hom-error{color:#b42318;font-weight:650}
#esa-homogeneity-lab #esa-hom-warning{font-weight:600}
#esa-homogeneity-lab #esa-hom-chart{display:block;width:100%;height:auto;max-width:650px;margin:auto;direction:ltr}
#esa-homogeneity-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-homogeneity-lab table{font-variant-numeric:tabular-nums}
#esa-homogeneity-lab .esa-hom-flag{font-weight:700}
#esa-homogeneity-lab output{unicode-bidi:isolate}
#esa-homogeneity-lab :is(textarea,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-long-math{max-width:100%;overflow-x:auto;direction:ltr}
@media(max-width:650px){#esa-homogeneity-lab .esa-hom-controls{flex-direction:column;align-items:stretch}}
</style>
<script defer src="/js/chi-square-homogeneity-explorer.js"></script>
