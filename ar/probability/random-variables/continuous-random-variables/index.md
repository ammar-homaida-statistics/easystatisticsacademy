---
layout: default
title: المتغيرات العشوائية المتصلة ودالة الكثافة الاحتمالية
description: درس عربي في المتغيرات العشوائية المتصلة ودالة الكثافة وتكامل الاحتمالات مع مختبر تفاعلي للتوزيع المنتظم.
permalink: /ar/probability/random-variables/continuous-random-variables/
lang: ar
sidebar: false
translation_pair: continuous-random-variables
math: true
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">المتغيرات العشوائية</span><span class="badge">مختبر تفاعلي</span></div>
<h1>المتغيرات العشوائية المتصلة ودالة الكثافة الاحتمالية</h1>
<p class="lead">يمثّل المتغير العشوائي المتصل مقادير يمكن قياسها على مجال عددي. في النماذج ذات الكثافة، تُحسب احتمالات الفترات بمساحات تحت منحنى دالة الكثافة، لا بقيم الدالة وحدها.</p>
<p><a href="/probability/random-variables/continuous-random-variables/" lang="en" dir="ltr">Read in English: Continuous Random Variables</a></p>
</div></section>
<section><div class="content-narrow" dir="rtl">
<h2>من المتغير المنفصل إلى المتغير المتصل</h2>
<p>في الدرس السابق، استخدمنا <strong>دالة الكتلة الاحتمالية (PMF)</strong> لإسناد احتمال إلى كل قيمة ممكنة لمتغير منفصل. أما عند دراسة زمن الانتظار أو الطول أو قياس مستمر مثالي، فنستخدم عادةً <strong>دالة كثافة احتمالية (PDF)</strong>. لا ينبغي الخلط بين ارتفاع الكثافة واحتمال نقطة مفردة.</p>
<p>تتحقق شروط دالة الكثافة \(f(x)\) عندما تكون غير سالبة وتساوي المساحة الكلية تحتها واحداً:</p>
<div class="esa-updf-ar-math" dir="ltr">\[f(x)\geq 0,\qquad\int_{-\infty}^{+\infty}f(x)\,dx=1.\]</div>
<p>احتمال أن يقع X في الفترة من c إلى d يساوي المساحة تحت الكثافة فوق هذه الفترة:</p>
<div class="esa-updf-ar-math" dir="ltr">\[P(c\leq X\leq d)=\int_c^d f(x)\,dx,\qquad c\leq d.\]</div>
<p>في أي نموذج متصل ذي دالة كثافة، يكون <span dir="ltr">P(X=c)=0</span>. هذا لا يعني أن القيمة مستحيلة عملياً، بل أن النقطة وحدها لا تملك مساحة.</p>
<h2>مثال: التوزيع المنتظم المتصل</h2>
<p>إذا كان X يتبع التوزيع المنتظم على الفترة من a إلى b، حيث <span dir="ltr">a&lt;b</span>، فإن ارتفاع الكثافة ثابت داخل الفترة، ويساوي مقلوب طولها:</p>
<div class="esa-updf-ar-math" dir="ltr">\[f(x)=\begin{cases}\frac{1}{b-a},&a\leq x\leq b,\\0,&\text{otherwise.}\end{cases}\]</div>
<p>مثلاً إذا كانت الفترة <span dir="ltr">[0,4]</span> فإن الكثافة تساوي <span dir="ltr">0.25</span>، واحتمال الوقوع بين 1 و3 يساوي <span dir="ltr">(3-1)/(4-0)=0.5</span>.</p>
<div class="esa-updf-ar-math" dir="ltr">\[E(X)=\frac{a+b}{2},\qquad\operatorname{Var}(X)=\frac{(b-a)^2}{12}.\]</div>
<section class="concept-box" id="esa-uniform-pdf-lab" lang="ar" aria-labelledby="esa-updf-heading" style="min-width:0;overflow-wrap:anywhere">
<h2 id="esa-updf-heading">مختبر تفاعلي: الاحتمالات تحت الكثافة المنتظمة</h2>
<p>عدّل الحدين a وb لتحديد مجال التوزيع، والحدين c وd للفترة المطلوبة. قد تمتد الفترة المطلوبة إلى خارج مجال التوزيع؛ لا تُحسب إلا مساحة التقاطع.</p>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,150px),1fr));gap:12px">
<label for="esa-updf-a">الحد الأدنى للتوزيع a<input id="esa-updf-a" type="number" step="any" value="0" dir="ltr" style="width:100%"></label>
<label for="esa-updf-b">الحد الأعلى للتوزيع b<input id="esa-updf-b" type="number" step="any" value="4" dir="ltr" style="width:100%"></label>
<label for="esa-updf-c">بداية الفترة المطلوبة c<input id="esa-updf-c" type="number" step="any" value="1" dir="ltr" style="width:100%"></label>
<label for="esa-updf-d">نهاية الفترة المطلوبة d<input id="esa-updf-d" type="number" step="any" value="3" dir="ltr" style="width:100%"></label>
</div>
<p role="alert" id="esa-updf-error" hidden></p>
<div id="esa-updf-results" aria-live="polite">
<p>ارتفاع الكثافة: <output id="esa-updf-density" dir="ltr">0.250000</output>؛ احتمال الفترة: <strong><output id="esa-updf-probability" dir="ltr">0.500000</output></strong>.</p>
<p>المساحة الكلية: <output id="esa-updf-integral" dir="ltr">1.000000</output>؛ احتمال نقطة مفردة: <output id="esa-updf-pointProbability" dir="ltr">0.000000</output>.</p>
<p>المتوسط: <output id="esa-updf-mean" dir="ltr">2.000000</output>؛ التباين: <output id="esa-updf-variance" dir="ltr">1.333333</output>.</p>
<p id="esa-updf-interpretation"></p></div>
<svg id="esa-updf-chart" viewBox="0 0 610 235" role="img" style="width:100%;height:auto;display:block" aria-label="منحنى الكثافة المنتظمة وتظليل المساحة الاحتمالية"></svg>
<button id="esa-updf-reset" class="btn btn-outline" type="button">استعادة المثال</button>
<p>عندما يكون طول المجال أقل من واحد، قد يزيد ارتفاع دالة الكثافة عن واحد، وهذا صحيح لأن الاحتمال يُقاس بالمساحة وليس بالارتفاع. وتُفترض هنا كثافة ثابتة على المجال، وليس أن جميع المتغيرات المتصلة لها توزيع منتظم.</p>
</section>
<h2>الفرق بين PMF وPDF</h2>
<p>في المتغير المنفصل يمكن أن تكون كتلة احتمال قيمة بعينها موجبة. أما المتغير المتصل الموصوف بكثافة فتكون احتمالات القيم المفردة صفراً، وتنتج احتمالات الفترات من التكامل. ولا يجوز استخدام قيمة الكثافة مباشرة كما لو كانت احتمالاً.</p>
<h2>أخطاء شائعة</h2>
<ul class="bullets"><li>اعتبار الكثافة عند نقطة ما مساوية لاحتمال هذه النقطة.</li><li>افتراض أن قيمة دالة الكثافة يجب ألا تتجاوز الواحد.</li><li>حساب احتمال الجزء الواقع خارج مجال التوزيع.</li><li>استخدام حدين معكوسين عند إدخال الفترة المطلوبة.</li><li>تعميم خصائص التوزيع المنتظم على جميع التوزيعات المتصلة.</li></ul>
<div class="summary-box"><h2>الخلاصة</h2><p>تعطي الكثافة احتمال الفترة من خلال مساحتها. شرطا صحة الكثافة هما عدم السلبية ووحدة المساحة الكلية، بينما تختلف قيمة الكثافة عن الاحتمال.</p></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/random-variables/discrete-random-variables/">السابق: المتغيرات العشوائية المنفصلة</a><a class="btn" lang="en" dir="ltr" href="/probability/random-variables/cumulative-distribution-function/">Next: Cumulative Distribution Function (English)</a></div>
</div></section>
<style>.esa-updf-ar-math{direction:ltr;max-width:100%;overflow-x:auto}.esa-updf-ar-math mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}</style>
<script defer src="/js/uniform-pdf-interval-explorer.js"></script>
