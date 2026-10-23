---
layout: default
title: التوزيع الطبيعي
description: درس عربي متكامل عن التوزيع الطبيعي والكثافة والمتوسط والانحراف المعياري والتحويل إلى Z وحساب الاحتمالات بمختبر تفاعلي.
permalink: /ar/probability/distributions/normal-distribution/
lang: ar
sidebar: false
translation_pair: normal-distribution
math: true
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">التوزيعات المستمرة</span><span class="badge">التوزيع الطبيعي</span></div>
<h1>التوزيع الطبيعي (Normal Distribution)</h1>
<p><a href="/probability/distributions/normal-distribution/" lang="en" dir="ltr">English — Normal Distribution</a></p>
<p class="lead">يُعد التوزيع الطبيعي أحد أكثر النماذج الاحتمالية استخدامًا في الإحصاء. يساعدنا هذا الدرس على فهم منحنى الجرس، والكثافة، والتحويل المعياري، وكيفية حساب احتمالات الفترات والذيلين بدقة.</p>
<div class="hero-actions"><a class="btn btn-outline" href="/ar/probability/distributions/uniform-distribution/">← التوزيع المنتظم بالعربية</a>
<a class="btn btn-outline" href="/probability/distributions/normal-distribution/" lang="en" dir="ltr">English lesson</a></div>
</div></section>
<section class="section"><div class="content-narrow">
<h2>ما التوزيع الطبيعي؟</h2>
<p>هو توزيع احتمالي <strong>مستمر</strong> ذو كثافة متناظرة حول المتوسط، وللكثافة شكل يشبه الجرس. يحدد المتوسط <span dir="ltr">μ</span> موقع المنحنى، ويحدد الانحراف المعياري الموجب <span dir="ltr">σ</span> مدى انتشاره. لا يعني الشكل الجَرَسي أن البيانات الحقيقية تتبع توزيعًا طبيعيًا بالضرورة.</p>
<div class="esa-ar-normal-eq" dir="ltr" tabindex="0" role="region" aria-label="تعريف النموذج الطبيعي">\[
X\sim N(\mu,\sigma^2),\quad -\infty<\mu<\infty,\quad \sigma>0.
\]</div>
<h2>دالة الكثافة الاحتمالية</h2>
<div class="esa-ar-normal-eq" dir="ltr" tabindex="0" role="region" aria-label="كثافة التوزيع الطبيعي">\[
f_X(x)=\frac{1}{\sigma\sqrt{2\pi}}
\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right),\quad x\in\mathbb R.
\]</div>
<p>لا تمثل قيمة الكثافة عند نقطة معينة احتمال وقوع تلك النقطة؛ فالاحتمال يساوي <strong>المساحة تحت الكثافة</strong> على فترة محددة. المساحة الكلية تحت المنحنى تساوي واحدًا، واحتمال أي نقطة منفردة يساوي صفرًا.</p>
<h2>المتوسط والتباين والانحراف المعياري</h2>
<div class="esa-ar-normal-eq" dir="ltr" tabindex="0" role="region" aria-label="عزوم الطبيعي">\[
E(X)=\mu,\qquad \operatorname{Var}(X)=\sigma^2,\qquad \operatorname{SD}(X)=\sigma.
\]</div>
<p>في التوزيع الطبيعي، يتطابق المتوسط والوسيط والمنوال. عند ثبات الانحراف المعياري تؤدي زيادة المتوسط إلى تحريك المنحنى أفقيًا فقط. وعند ثبات المتوسط، تؤدي زيادة الانحراف المعياري إلى توسيع المنحنى وخفض قمته مع بقاء المساحة الكلية واحدًا.</p>
<h2>التوزيع الطبيعي المعياري ودرجات Z</h2>
<p>لتوحيد المقاييس، نطرح المتوسط ونقسم على الانحراف المعياري. إذا كان <span dir="ltr">X</span> يتبع توزيعًا طبيعيًا بالفعل، فإن المتغير الناتج يتبع التوزيع الطبيعي المعياري:</p>
<div class="esa-ar-normal-eq" dir="ltr" tabindex="0" role="region" aria-label="التحويل إلى الطبيعي المعياري">\[
Z=\frac{X-\mu}{\sigma}\sim N(0,1)\quad\text{إذا كان }X\sim N(\mu,\sigma^2).
\]</div>
<p>تشير <span dir="ltr">Z=+2</span> إلى قيمة تقع بمقدار انحرافين معياريين فوق المتوسط، وتشير <span dir="ltr">Z=-1</span> إلى قيمة تقع بمقدار انحراف معياري واحد دونه. يمكن حساب درجة Z لبيانات غير طبيعية، لكن درجتها لا تتبع بالضرورة التوزيع الطبيعي المعياري.</p>
<h2>كيف نحسب الاحتمالات؟</h2>
<p>باستخدام دالة التوزيع التراكمي <span dir="ltr">Φ</span> للتوزيع الطبيعي المعياري:</p>
<div class="esa-ar-normal-eq" dir="ltr" tabindex="0" role="region" aria-label="احتمالات الطبيعي">\[
P(a\le X\le b)=\Phi\!\left(\frac{b-\mu}{\sigma}\right)-
\Phi\!\left(\frac{a-\mu}{\sigma}\right),\quad a<b.
\]</div>
<p>كذلك <span dir="ltr">P(X≤a)=Φ((a−μ)/σ)</span>، و<span dir="ltr">P(X≥b)=1−Φ((b−μ)/σ)</span>. بالنسبة للمتغير المستمر لا يؤثر استخدام المتراجحة الصارمة أو غير الصارمة عند الحد.</p>
<h2>مثال عددي مُتحقَّق منه</h2>
<p>افترض أن <span dir="ltr">X∼N(100,15²)</span>. الاحتمال بين 85 و115 هو احتمال أن يقع متغير طبيعي معياري بين −1 و+1:</p>
<div class="esa-ar-normal-eq" dir="ltr" tabindex="0" role="region" aria-label="مثال 68 بالمئة">\[
P(85\le X\le115)=\Phi(1)-\Phi(-1)\approx0.682689.
\]</div>
<p>أما احتمال تجاوز 130 فيساوي تقريبًا <strong>0.022750</strong> لأن <span dir="ltr">Z=(130−100)/15=2</span>. هذه احتمالات وفق <strong>النموذج المفترض</strong> وليست نسبًا مضمونة في أي عينة فعلية.</p>
<div class="example-box" id="esa-normal-probability-explorer" aria-labelledby="esa-normal-title">
<h2 id="esa-normal-title">مختبر تفاعلي لحساب احتمالات التوزيع الطبيعي</h2>
<p>غيّر المتوسط والانحراف المعياري وحدّي الفترة، ثم اختر الاحتمال على يسار <span dir="ltr">a</span>، أو يمين <span dir="ltr">b</span>، أو بينهما. يمثّل الجزء المظلّل المساحة الاحتمالية، وتُحسب الاحتمالات باستخدام كامل التوزيع حتى خارج الجزء الظاهر من الرسم.</p>
<div class="esa-normal-controls">
<label>المتوسط μ <input id="esa-normal-mu" type="number" step="any" value="0" dir="ltr"></label>
<label>الانحراف المعياري σ (موجب) <input id="esa-normal-sigma" type="number" step="any" min="0.000001" value="1" dir="ltr"></label>
<label>الحد الأدنى a <input id="esa-normal-a" type="number" step="any" value="-1" dir="ltr"></label>
<label>الحد الأعلى b <input id="esa-normal-b" type="number" step="any" value="1" dir="ltr"></label>
<label>منطقة الاحتمال <select id="esa-normal-mode"><option value="between" selected>بين a و b</option><option value="left">يسار a</option><option value="right">يمين b</option></select></label>
</div>
<p role="alert" id="esa-normal-error" hidden></p>
<svg width="440" height="245" viewBox="0 0 440 245" id="esa-normal-chart" role="img" aria-label="منحنى طبيعي مع تظليل منطقة الاحتمال" dir="ltr">
<line x1="34" x2="404" y1="200" y2="200" stroke="currentColor"></line>
<path id="esa-normal-shade" fill="#0d9488" fill-opacity="0.35"></path>
<path id="esa-normal-density" fill="none" stroke="#0d9488" stroke-width="2.5"></path>
<line id="esa-normal-bound-a" stroke="#64748b" stroke-dasharray="4 3" y1="40" y2="200"></line>
<line id="esa-normal-bound-b" stroke="#64748b" stroke-dasharray="4 3" y1="40" y2="200"></line>
<text x="34" y="226" fill="currentColor" font-size="12">μ − 4σ</text>
<text x="219" y="226" fill="currentColor" font-size="12" text-anchor="middle">μ</text>
<text x="404" y="226" fill="currentColor" font-size="12" text-anchor="end">μ + 4σ</text>
</svg>
<div role="status" aria-live="polite" aria-atomic="true" dir="ltr">
<p>z(a) = <output id="esa-normal-za">−1.0000</output>; z(b) = <output id="esa-normal-zb">1.0000</output>.</p>
<p><span id="esa-normal-prob-label">P(a ≤ X ≤ b)</span> = <output id="esa-normal-probability">0.682689</output> (<output id="esa-normal-percent">68.2689</output>%).</p>
</div>
<p id="esa-normal-warning" class="muted-mini">يُعرض المنحنى حتى أربعة انحرافات معيارية حول المتوسط، لكن الحساب يتضمن الذيول غير المحدودة.</p>
<button type="button" class="btn btn-outline" id="esa-normal-reset">إعادة المثال المعياري</button>
<p class="muted-mini">تُستخدم طريقة تقريب عددي لدالة التوزيع التراكمي بدقة مطلقة تقارب 2×10⁻⁷؛ هذا المختبر ليس محاكاة. لا تُخزّن المدخلات.</p>
</div>
<h2>القاعدة التقريبية 68–95–99.7</h2>
<div class="table-wrap"><table><thead><tr><th>المجال حول المتوسط</th><th>الاحتمال التقريبي في التوزيع الطبيعي</th></tr></thead>
<tbody><tr><td dir="ltr">μ ± 1σ</td><td>68.27%</td></tr><tr><td dir="ltr">μ ± 2σ</td><td>95.45%</td></tr><tr><td dir="ltr">μ ± 3σ</td><td>99.73%</td></tr></tbody></table></div>
<p>هذه النسب تخص النموذج الطبيعي؛ لا تُستخدم قاعدة ثابتة لجميع أشكال البيانات أو لضمان نتائج عينات صغيرة.</p>
<h2>الارتباط بنظرية الحد المركزي</h2>
<p>تحت شروط مناسبة تتقارب توزيعات متوسطات العينات نحو التوزيع الطبيعي عندما يزداد حجم العينة. لا يعني ذلك أن البيانات الأصلية تصبح طبيعية، كما أن الاعتماد الشديد أو الذيول الثقيلة جدًا قد يتطلب عناية أو شروطًا إضافية.</p>
<h2>متى يكون التوزيع الطبيعي غير ملائم؟</h2>
<p>قد تكون المتغيرات محدودة أو موجبة فقط أو شديدة الالتواء، وقد تكون البيانات متعددة المنوال أو مليئة بقيم متطرفة؛ لذلك ينبغي مراجعة شكل البيانات وسياق القياس والافتراضات قبل اختيار النموذج.</p>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>يعتمد النموذج على المتوسط μ والانحراف المعياري الموجب σ، وتباينه σ².</li>
<li>احتمال الفترة مساحة تحت منحنى الكثافة؛ واحتمال النقطة المنفردة صفر.</li>
<li>التحويل المعياري ينتج N(0,1) إذا كان المتغير الأصلي طبيعيًا.</li>
<li>قاعدة 68–95–99.7 تقريبية وتصح تحت افتراض التوزيع الطبيعي.</li>
<li>يجب التحقق من ملاءمة النموذج عند التطبيق.</li></ul></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/distributions/uniform-distribution/">← التوزيع المنتظم</a>
<a class="btn" href="/probability/distributions/normal-distribution/" lang="en" dir="ltr">English lesson →</a></div>
</div></section>
<style>
#esa-normal-probability-explorer{box-sizing:border-box;max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-normal-probability-explorer .esa-normal-controls{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,170px),1fr));gap:12px;margin:14px 0}
#esa-normal-probability-explorer label{display:flex;flex-direction:column;gap:6px;font-weight:600;min-width:0}
#esa-normal-probability-explorer input,#esa-normal-probability-explorer select{box-sizing:border-box;font:inherit;padding:8px;width:100%;max-width:100%;min-width:0}
#esa-normal-probability-explorer svg{display:block;width:100%;height:auto;max-width:550px;margin:10px auto}
#esa-normal-probability-explorer [hidden]{display:none!important}
.esa-ar-normal-eq{max-width:100%;overflow-x:auto;direction:ltr}.esa-ar-normal-eq mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}
.esa-ar-normal-eq:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
@media print{#esa-normal-probability-explorer .esa-normal-controls,#esa-normal-probability-explorer button{display:none}}
</style>
<script defer src="/js/normal-probability-explorer.js"></script>
