---
layout: default
title: اختبار كاي تربيع للاستقلال
description: شرح عربي لاختبار كاي تربيع للاستقلال بين متغيرين فئويين، مع جدول التوافق والتكرارات المتوقعة ومعامل كرامر ومختبر تفاعلي 2 × 2.
permalink: /ar/inference/classical-tests/chi-square-independence-test/
lang: ar
sidebar: false
learning_resource: true
translation_pair: chi-square-independence
---
<section class="hero hero-section"><div class="hero-card">
<h1>اختبار كاي تربيع للاستقلال</h1>
<p class="lead">هل يرتبط متغيران فئويان، أم أن معرفة أحدهما لا تقدم أي معلومات عن الآخر؟ يوضح هذا الدرس كيف يقارن اختبار بيرسون للاستقلال (Pearson chi-square test of independence) التكرارات المشاهدة في جدول التوافق بالتكرارات المتوقعة عند الاستقلال، وكيف نفسّر النتيجة بحذر.</p>
<p><a href="/inference/classical-tests/chi-square-independence-test/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/classical-tests/chi-square-goodness-of-fit/">الدرس السابق: اختبار كاي تربيع لحسن المطابقة</a></p>
</div></section>
<section><div class="content-narrow">
<h2>1. سؤال البحث</h2>
<p>كثيرًا ما نجمع بيانات عن متغيرين فئويين للأفراد أنفسهم، مثل الجنس وتفضيل منتج معين، أو حالة التدخين والإصابة بمرض، أو نوع الجهاز وإتمام الشراء على موقع إلكتروني. السؤال الإحصائي هو: هل يرتبط المتغيران في المجتمع، أم أن الفروق الظاهرة في العينة يمكن تفسيرها بالتباين العشوائي وحده؟</p>
<p>يختلف هذا الاختبار عن <a href="/ar/inference/classical-tests/chi-square-goodness-of-fit/">حسن المطابقة</a> الذي يدرس متغيرًا فئويًا <strong>واحدًا</strong> مقابل توزيع محدد مسبقًا؛ أما هنا فندرس <strong>متغيرين</strong> مُقاسين على عينة واحدة.</p>
<h2>2. معنى الاستقلال والفرضيتان</h2>
<p>يكون المتغيران مستقلين إذا كان الاحتمال المشترك لكل خلية يساوي حاصل ضرب الاحتمالين الهامشيين: \(\pi_{ij}=\pi_{i\cdot}\,\pi_{\cdot j}\). وبعبارة أبسط، تبقى نسب فئات أحد المتغيرين كما هي في جميع فئات المتغير الآخر.</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="فرضيتا اختبار الاستقلال">
\[
H_0:\ \pi_{ij}=\pi_{i\cdot}\,\pi_{\cdot j}\ \text{for all } i,j
\qquad\text{vs}\qquad
H_a:\ \pi_{ij}\ne\pi_{i\cdot}\,\pi_{\cdot j}\ \text{for some } i,j.
\]</div>
<p>الفرضية الصفرية \(H_0\): المتغيران مستقلان. الفرضية البديلة \(H_a\): يوجد ارتباط بينهما. لا تحدد الفرضية البديلة اتجاه الارتباط أو شكله؛ فالاختبار يقيّم وجود دليل على الارتباط فقط.</p>
<h2>3. جدول التوافق: مثال محلول</h2>
<p>سُئل 200 شخص (100 ذكر و100 أنثى) عن تفضيلهم بين منتجين A وB، فكانت التكرارات المشاهدة \(O_{ij}\) كما يلي:</p>
<div class="table-wrap"><table><caption>التكرارات المشاهدة</caption><thead><tr><th scope="col">المجموعة</th><th scope="col">يفضّل A</th><th scope="col">يفضّل B</th><th scope="col">المجموع</th></tr></thead><tbody><tr><th scope="row">ذكور</th><td>40</td><td>60</td><td>100</td></tr><tr><th scope="row">إناث</th><td>70</td><td>30</td><td>100</td></tr><tr><th scope="row">المجموع</th><td>110</td><td>90</td><td>200</td></tr></tbody></table></div>
<h2>4. التكرارات المتوقعة عند الاستقلال</h2>
<p>إذا صحت فرضية الاستقلال، يُقدَّر التكرار المتوقع لكل خلية من مجموع صفها \(R_i\) ومجموع عمودها \(C_j\) والحجم الكلي \(N\):</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="صيغة التكرار المتوقع">
\[
E_{ij}=\frac{R_i\,C_j}{N},\qquad E_{11}=\frac{100\times110}{200}=55,\quad E_{12}=\frac{100\times90}{200}=45.
\]</div>
<p>وبالمثل \(E_{21}=55\) و\(E_{22}=45\). لاحظ أن مجموع التكرارات المتوقعة في كل صف وعمود يساوي المجموع المشاهد نفسه.</p>
<h2>5. إحصائية بيرسون ودرجات الحرية</h2>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="إحصائية اختبار الاستقلال">
\[
\chi^2=\sum_{i=1}^{r}\sum_{j=1}^{c}\frac{(O_{ij}-E_{ij})^2}{E_{ij}},\qquad df=(r-1)(c-1).
\]</div>
<p>في المثال: \(r=c=2\)، إذن \(df=1\). مساهمات الخلايا هي \(225/55\approx4.0909\) لكل خلية في العمود A و\(225/45=5\) لكل خلية في العمود B، ومن ثم:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="حساب المثال">
\[
\chi^2=2\left(\frac{225}{55}+\frac{225}{45}\right)=\frac{200}{11}\approx18.1818,\qquad
P(\chi^2_1\ge18.1818)\approx2.008\times10^{-5}.
\]</div>
<p>عند مستوى دلالة \(\alpha=0.05\) نرفض فرضية الاستقلال: تقدم البيانات دليلًا قويًا على ارتباط الجنس بالتفضيل في هذا المجتمع، <strong>بشرط</strong> صحة الافتراضات أدناه. هذه القيمة الاحتمالية تقريبية تعتمد على توزيع كاي تربيع للعينات الكبيرة، دون تصحيح ييتس للاستمرارية.</p>
<h2>6. قوة الارتباط: معامل كرامر V</h2>
<p>القيمة الاحتمالية الصغيرة لا تعني ارتباطًا قويًا؛ فهي تتأثر بحجم العينة. لقياس قوة الارتباط نستخدم معامل كرامر:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="معامل كرامر">
\[
V=\sqrt{\frac{\chi^2}{N\,(\min(r,c)-1)}},\qquad V_{2\times2}=\sqrt{\frac{\chi^2}{N}}=\sqrt{\frac{18.1818}{200}}\approx0.3015.
\]</div>
<p>تتراوح \(V\) بين 0 (لا ارتباط في العينة) و1. ويعتمد الحكم على كون القيمة «صغيرة» أو «كبيرة» على مجال البحث وعدد الفئات، لا على قاعدة عامة ثابتة.</p>
<h2>7. مختبر الاستقلال التفاعلي 2 × 2</h2>
<section class="example-box" id="esa-chi-independence-lab" data-locale="ar" aria-labelledby="esa-chi-heading">
<h3 id="esa-chi-heading">مختبر الاستقلال التفاعلي لجدول 2 × 2</h3>
<p>غيّر التكرارات الأربعة المشاهدة لترى كيف يتنبأ الاستقلال بكل خلية، وكيف تتجمع مساهمات الخلايا في إحصائية بيرسون. يبدأ الجدول بالمثال المحلول أعلاه. <a href="/inference/classical-tests/fisher-exact-vs-chi-square/">قارن مع اختبار فيشر الدقيق للجداول الصغيرة (بالإنجليزية)</a>.</p>
<div class="esa-chi-input-grid">
<label>ذكور، يفضّل A <input id="esa-chi-a" dir="ltr" aria-describedby="esa-chi-error esa-chi-warning" type="number" min="0" max="10000000" step="1" value="40" inputmode="numeric" aria-invalid="false"></label>
<label>ذكور، يفضّل B <input id="esa-chi-b" dir="ltr" aria-describedby="esa-chi-error esa-chi-warning" type="number" min="0" max="10000000" step="1" value="60" inputmode="numeric" aria-invalid="false"></label>
<label>إناث، يفضّل A <input id="esa-chi-c" dir="ltr" aria-describedby="esa-chi-error esa-chi-warning" type="number" min="0" max="10000000" step="1" value="70" inputmode="numeric" aria-invalid="false"></label>
<label>إناث، يفضّل B <input id="esa-chi-d" dir="ltr" aria-describedby="esa-chi-error esa-chi-warning" type="number" min="0" max="10000000" step="1" value="30" inputmode="numeric" aria-invalid="false"></label>
</div>
<p id="esa-chi-error" role="alert" hidden></p>
<div class="table-wrap"><table><caption>التكرارات المتوقعة والمساهمات (المشاهد → المتوقع؛ مساهمة χ²)</caption><thead><tr><th scope="col">المجموعة</th><th scope="col">يفضّل A</th><th scope="col">يفضّل B</th></tr></thead><tbody>
<tr><th scope="row">ذكور</th><td><output id="esa-chi-cell-a" dir="ltr">40 → 55.000; 4.0909</output></td><td><output id="esa-chi-cell-b" dir="ltr">60 → 45.000; 5.0000</output></td></tr>
<tr><th scope="row">إناث</th><td><output id="esa-chi-cell-c" dir="ltr">70 → 55.000; 4.0909</output></td><td><output id="esa-chi-cell-d" dir="ltr">30 → 45.000; 5.0000</output></td></tr>
</tbody></table></div>
<div class="esa-chi-results" role="status" aria-live="polite" aria-atomic="true">
<p>إحصائية بيرسون χ² = <output id="esa-chi-stat" dir="ltr">18.181818</output>؛ درجات الحرية = <output id="esa-chi-df" dir="ltr">1</output>.</p>
<p>القيمة الاحتمالية للطرف الأيمن (تقريبية، دون تصحيح الاستمرارية) = <output id="esa-chi-p" dir="ltr">2.008e-5</output>.</p>
<p>معامل كرامر V = <output id="esa-chi-v" dir="ltr">0.301511</output>. في جدول 2 × 2 يكون V = √(χ²/N).</p>
</div>
<p id="esa-chi-warning" role="status" aria-live="polite">جميع التكرارات المتوقعة الأربعة لا تقل عن 5 في المثال الابتدائي.</p>
<p class="muted-mini">تستخدم القيمة الاحتمالية توزيع كاي تربيع بدرجة حرية واحدة، وليست اختبار فيشر الدقيق. يجب أن تكون المشاهدات مستقلة، وقد تُفسد التكرارات المتوقعة الصغيرة تقريب العينة الكبيرة. الارتباط ليس دليلًا على السببية.</p>
<button type="button" class="btn btn-outline" id="esa-chi-reset">إعادة المثال المحلول</button>
</section>
<h2>8. الافتراضات والقيود</h2>
<ul class="bullets"><li>كل مشاهدة مستقلة عن غيرها، وتُعدّ مرة واحدة فقط في خلية واحدة.</li><li>البيانات تكرارات (أعداد) لا نسبًا مئوية أو متوسطات.</li><li>الفئات متنافية وشاملة لكل متغير.</li><li>ينبغي أن تكون التكرارات <strong>المتوقعة</strong> كافية؛ والقاعدة الشائعة \(E_{ij}\ge5\) إرشادية وليست شرطًا رياضيًا مطلقًا.</li></ul>
<p>إذا كانت التكرارات المتوقعة صغيرة في جدول 2 × 2 فقد يكون اختبار فيشر الدقيق أنسب. ولا يُستخدم الاختبار للعينات المزدوجة (القياس القبلي والبعدي للأفراد أنفسهم)؛ فتلك حالة اختبار ماكنمار. كما أن رفض \(H_0\) لا يحدد أي الخلايا تقود الارتباط، ولا يثبت علاقة سببية، وقد يكون الارتباط ناتجًا عن متغير ثالث مُربك.</p>
<h2>9. الاستقلال والتجانس وحسن المطابقة</h2>
<p>تُحسب إحصائية بيرسون بالصيغة نفسها في اختباري الاستقلال والتجانس، لكن تصميم الدراسة مختلف: في <strong>الاستقلال</strong> نأخذ عينة واحدة ونصنف كل فرد وفق متغيرين؛ وفي <strong>التجانس</strong> نأخذ عينات مستقلة من عدة مجموعات محددة مسبقًا ونقارن توزيع متغير واحد بينها. أما <strong>حسن المطابقة</strong> فيقارن متغيرًا واحدًا بتوزيع نظري محدد.</p>
<p><a href="/inference/classical-tests/chi-square-homogeneity-test/">الدرس التالي: اختبار كاي تربيع للتجانس (بالإنجليزية)</a> · <a href="/ar/inference/classical-tests/chi-square-goodness-of-fit/">اختبار كاي تربيع لحسن المطابقة</a></p>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets"><li>يختبر الاستقلال وجود ارتباط بين متغيرين فئويين في عينة واحدة.</li><li>\(E_{ij}=R_iC_j/N\)، و\(\chi^2=\sum(O_{ij}-E_{ij})^2/E_{ij}\) بدرجات حرية \((r-1)(c-1)\).</li><li>القيمة الاحتمالية تقاربية وتتطلب مشاهدات مستقلة وتكرارات متوقعة كافية.</li><li>يقيس معامل كرامر V قوة الارتباط، بينما تتأثر القيمة الاحتمالية بحجم العينة.</li><li>الارتباط الدال إحصائيًا لا يثبت السببية.</li></ul></div>
</div></section>
<style>
#esa-chi-independence-lab{box-sizing:border-box;max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-chi-independence-lab .esa-chi-input-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,180px),1fr));gap:12px;margin:14px 0}
#esa-chi-independence-lab label{display:flex;flex-direction:column;gap:6px;min-width:0;font-weight:600}
#esa-chi-independence-lab input{box-sizing:border-box;max-width:100%;width:100%;font:inherit;padding:8px}
#esa-chi-independence-lab td{min-width:0;overflow-wrap:anywhere}
#esa-chi-independence-lab .table-wrap{display:block;max-width:100%;overflow-x:auto}
#esa-chi-independence-lab output{unicode-bidi:isolate}
#esa-chi-independence-lab :is(input,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
#esa-chi-independence-lab [role="alert"]{font-weight:700;color:#b42318}
#esa-chi-independence-lab [hidden]{display:none!important}
.esa-long-math{max-width:100%;overflow-x:auto;direction:ltr}
@media print{#esa-chi-independence-lab button,#esa-chi-independence-lab .esa-chi-input-grid{display:none}}
</style>
<script defer src="/js/chi-square-independence-2x2.js"></script>
