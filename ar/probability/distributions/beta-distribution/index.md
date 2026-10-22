---
layout: default
title: توزيع بيتا
description: درس عربي موثق عن توزيع بيتا ومعلمتي الشكل ودالة الكثافة ودالة بيتا والمتوسط والتباين وأمثلة بايزية للاحتمالات والنسب، مع الصيغ الرياضية الصحيحة.
permalink: /ar/probability/distributions/beta-distribution/
lang: ar
sidebar: false
translation_pair: beta-distribution
math: true
---

<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">التوزيعات المستمرة</span><span class="badge">النسب والاحتمالات</span></div>
<h1>توزيع بيتا (Beta Distribution)</h1>
<p><a href="/probability/distributions/beta-distribution/" lang="en" dir="ltr">English — Beta Distribution</a></p>
<p class="lead">كيف نصف عدم اليقين حول كمية لا تقع إلا بين الصفر والواحد، مثل نسبة في مجتمع أو احتمال نجاح مجهول؟</p>
<div class="hero-actions">
<a class="btn btn-outline" href="/ar/probability/distributions/gamma-distribution/">← توزيع غاما بالعربية</a>
<a class="btn btn-outline" href="/ar/probability/distributions/binomial-distribution/">التوزيع ذو الحدين بالعربية</a>
</div></div></section>

<section class="section"><div class="content-narrow">
<h2>ما توزيع بيتا؟</h2>
<p>توزيع بيتا توزيع احتمالي <strong>مستمر</strong> مناسب لنمذجة متغير عشوائي تقع قيمه بين الصفر والواحد. يمكن استخدامه لوصف عدم اليقين حول نسبة أو حول <strong>احتمال نجاح مجهول</strong> في نموذج ثنائي النتائج، عندما تكون افتراضات النموذج مناسبة.</p>
<div class="concept-box"><strong>تمييز أساسي:</strong><p>عندما نمثل احتمال النجاح نفسه بتوزيع بيتا فإن الاحتمال <span dir="ltr">p</span> يُعامل بوصفه كمية مجهولة لها توزيع احتمالي في المنهج البايزي. هذا لا يعني أن نتيجة المحاولة الثنائية نفسها تتبع توزيع بيتا؛ فالنتيجة الثنائية تتبع برنولي، وعدد النجاحات في عدد ثابت من المحاولات يمكن نمذجته بذي الحدين.</p></div>

<h2>لماذا نحتاج توزيع بيتا؟</h2>
<p>التوزيع الطبيعي يسمح بقيم أقل من الصفر أو أكبر من الواحد، بينما يظل توزيع بيتا داخل المجال المناسب للعديد من الاحتمالات والنسب. ويمكن تغيير شكله بسهولة بفضل معلمتين، لتمثيل اعتقادات متفاوتة حول القيم الأقرب إلى الصفر أو النصف أو الواحد.</p>

<h2>مجال المتغير</h2>
<div class="esa-beta-equation" dir="ltr" role="region" tabindex="0" aria-label="مجال متغير بيتا">\[
0<X<1,\qquad \alpha>0,\quad \beta>0.
\]</div>
<p>تُعرّف الكثافة على المجال المفتوح، وقد تزداد دون حد بالقرب من طرفيه عندما تقل بعض معلمات الشكل عن الواحد. مع ذلك، يبقى احتمال أي قيمة مفردة (بما فيها الطرفان) صفرًا في توزيع بيتا المستمر المعتاد.</p>

<h2>معلمتا الشكل</h2>
<p>تعتمد عائلة بيتا على <strong>معلمتي شكل موجبتين</strong> هما <span dir="ltr">α</span> و<span dir="ltr">β</span>. تتحكم نسبتهما ومجموعهما في مكان تركز الكثافة وفي مقدار تشتتها؛ وليستا معدل وصول أو معلمة مقياس كما في توزيع غاما.</p>
<div class="esa-beta-equation" dir="ltr" role="region" tabindex="0" aria-label="ترميز توزيع بيتا">\[
X\sim\operatorname{Beta}(\alpha,\beta).
\]</div>

<h2>دالة الكثافة الاحتمالية</h2>
<p>لكل <span dir="ltr">0&lt;x&lt;1</span>، تُعطى الكثافة بالشكل:</p>
<div class="esa-beta-equation" dir="ltr" role="region" tabindex="0" aria-label="دالة كثافة بيتا">\[
f_X(x)=\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)},
\qquad 0<x<1.
\]</div>
<p>تساوي الكثافة صفرًا خارج المجال <span dir="ltr">[0,1]</span>، وقيمتها عند نقطة مفردة ليست احتمالًا. الاحتمالات على الفترات تساوي المساحة تحت منحنى الكثافة بين حدّي الفترة.</p>

<h2>دالة بيتا وعلاقتها بدالة غاما</h2>
<p>تُستخدم دالة بيتا لتطبيع الكثافة بحيث يكون تكاملها الكلي واحدًا:</p>
<div class="esa-beta-equation" dir="ltr" role="region" tabindex="0" aria-label="دالة بيتا والتكامل">\[
B(\alpha,\beta)=\int_0^1 x^{\alpha-1}(1-x)^{\beta-1}\,dx
=\frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}.
\]</div>
<p>تشير <span dir="ltr">Γ</span> إلى <a href="/ar/probability/distributions/gamma-distribution/">دالة غاما</a> الرياضية التي تعمم المضروب. تشابه الاسم لا يعني تطابق توزيع بيتا وتوزيع غاما؛ لكل منهما مجال ونمط استخدام مختلف.</p>

<h2>لماذا يتغير شكل المنحنى؟</h2>
<p>تسمح المعلمتان بظهور منحنى منتظم أو متماثل أو ملتوي أو على شكل حرف <span dir="ltr">U</span>. يجب قراءة هذه الأشكال مع نطاق المتغير؛ فالكثافة الكبيرة قرب الصفر لا تعني أن النقطة صفر وحدها تمتلك احتمالًا موجبًا.</p>

<h2>الحالة الأولى: التوزيع المنتظم</h2>
<p>عندما تكون <span dir="ltr">α=β=1</span> يختفي تأثير الأسّين، فتصبح الكثافة ثابتة:</p>
<div class="esa-beta-equation" dir="ltr" role="region" tabindex="0" aria-label="بيتا واحد واحد منتظم">\[
\operatorname{Beta}(1,1)=\operatorname{Uniform}(0,1),\qquad f_X(x)=1.
\]</div>
<p>جميع الفترات المتساوية طولًا داخل المجال تمتلك الاحتمال نفسه، لكن لا يوجد احتمال موجب لأي نقطة محددة.</p>

<h2>الحالة الثانية: التماثل حول النصف</h2>
<p>عندما تكون <span dir="ltr">α=β</span> يكون التوزيع متماثلًا حول <span dir="ltr">0.5</span>. عند <span dir="ltr">α=β=2</span> يتخذ شكلًا بقمة قرب النصف، بينما عند <span dir="ltr">α=β=0.5</span> تكون الكثافة على هيئة <span dir="ltr">U</span> وتتزايد قرب الطرفين.</p>

<h2>الحالة الثالثة: الميل نحو القيم الصغيرة</h2>
<p>عند <span dir="ltr">α=2, β=5</span> يكون التوزيع ملتويًا لليمين، ويتركز معظم حجمه الاحتمالي عند القيم الأصغر نسبيًا. يشير ذلك إلى تفضيل احتمالات النجاح المنخفضة إذا كان المتغير يمثل احتمال نجاح مجهولًا.</p>

<h2>الحالة الرابعة: الميل نحو القيم الكبيرة</h2>
<p>عند <span dir="ltr">α=5, β=2</span> تصبح الكثافة صورة معكوسة للحالة السابقة، ويميل المتغير إلى القيم الأكبر. لا ينبغي الخلط بين شكل كثافة المعلمة وبين توزيع البيانات الثنائية الناتجة عنها.</p>

<h2>القيمة المتوقعة</h2>
<div class="esa-beta-equation" dir="ltr" role="region" tabindex="0" aria-label="متوسط توزيع بيتا">\[
E(X)=\frac{\alpha}{\alpha+\beta}.
\]</div>
<p>تحدد نسبة معلمة الشكل الأولى إلى مجموع المعلمتين موقع المتوسط. هذه قيمة متوقعة للمتغير الذي يتبع بيتا، ولا تساوي بالضرورة نسبة النجاح الفعلية المجهولة.</p>

<h2>مثال على المتوسط</h2>
<p>إذا كان المتغير يتبع <span dir="ltr">Beta(8,2)</span> فإن المتوسط يساوي:</p>
<div class="esa-beta-equation" dir="ltr" role="region" tabindex="0" aria-label="متوسط بيتا ثمانية اثنان">\[
E(X)=\frac{8}{8+2}=0.8.
\]</div>
<p>تفسير <span dir="ltr">0.8</span> يعتمد على التطبيق؛ ففي نموذج بايزي للاحتمال المجهول يمثل <strong>متوسط توزيع الاحتمال</strong> المعتمد في التحليل.</p>

<h2>التباين</h2>
<div class="esa-beta-equation" dir="ltr" role="region" tabindex="0" aria-label="تباين توزيع بيتا">\[
\operatorname{Var}(X)=
\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}.
\]</div>
<p>عند ثبات المتوسط وزيادة مجموع معلمتي الشكل، يقل التباين ويصبح التوزيع أكثر تركزًا. لا يجوز تفسير زيادة التركيز دائمًا بوصفها «معلومات فعلية أكثر» دون تحديد المصدر الذي جاءت منه المعلمتان.</p>

<h2>مثال للتحقق من التباين</h2>
<p>للتوزيع <span dir="ltr">Beta(8,2)</span> نحصل على:</p>
<div class="esa-beta-equation" dir="ltr" role="region" tabindex="0" aria-label="تباين بيتا ثمانية اثنان">\[
\operatorname{Var}(X)=
\frac{8\times2}{(8+2)^2(8+2+1)}
=\frac{16}{1100}\approx0.01454545.
\]</div>
<p>الانحراف المعياري يساوي الجذر التربيعي للتباين، أي نحو <span dir="ltr">0.1206059</span> في المثال.</p>

<h2>ما المقصود بتركيز التوزيع؟</h2>
<p>إذا ثبتت النسبة <span dir="ltr">α/(α+β)</span> وظل المتوسط نفسه، فإن زيادة المجموع <span dir="ltr">α+β</span> تؤدي إلى تباين أصغر. على سبيل المثال، يتساوى متوسط <span dir="ltr">Beta(2,2)</span> و<span dir="ltr">Beta(20,20)</span> عند <span dir="ltr">0.5</span>، لكن الثاني أكثر تركزًا حول النصف.</p>

<h2>تفسير بايزي: الاحتمال نفسه مجهول</h2>
<p>في الاستدلال البايزي يمكن افتراض <span dir="ltr">p∼Beta(α,β)</span> قبل رؤية البيانات، حيث <span dir="ltr">p</span> احتمال النجاح الثابت خلال تجارب برنولي مستقلة مشروطة بقيمته. إذا رصدنا <span dir="ltr">s</span> نجاحات و<span dir="ltr">f</span> إخفاقات، يتحدث التوزيع وفق القاعدة:</p>
<div class="esa-beta-equation" dir="ltr" role="region" tabindex="0" aria-label="اقتران بيتا وبرنولي">\[
p\sim\operatorname{Beta}(\alpha,\beta),\quad
p\mid \text{data}\sim\operatorname{Beta}(\alpha+s,\beta+f).
\]</div>
<p>هذا اقتران توزيعي <strong>مشروط بافتراض</strong> استقلال المحاولات وثبات <span dir="ltr">p</span> وصحة نموذج البيانات؛ ليس قاعدة لكل أشكال البيانات التي تحتوي نسبًا.</p>

<h2>مثال بايزي محلول</h2>
<p>نبدأ بتوزيع سابق <span dir="ltr">Beta(2,2)</span>، ثم نرصد <strong>8 نجاحات وإخفاقين</strong> خلال 10 محاولات مستقلة. يصبح التوزيع اللاحق:</p>
<div class="esa-beta-equation" dir="ltr" role="region" tabindex="0" aria-label="التوزيع اللاحق ومعدل النجاح">\[
p\mid\text{data}\sim\operatorname{Beta}(10,4),\qquad
E(p\mid\text{data})=\frac{10}{14}\approx0.714286.
\]</div>
<p>النسبة المشاهدة هي <span dir="ltr">8/10=0.8</span>، لكنها لا تساوي بالضرورة المتوسط اللاحق الذي يتأثر بالتوزيع السابق. ويوضح ذلك الفرق بين <strong>النسبة المشاهدة</strong> و<strong>توزيع عدم اليقين حول احتمال النجاح</strong>.</p>

<h2>العلاقة بتوزيعات أخرى</h2>
<div class="table-wrap"><table><thead><tr><th>التوزيع</th><th>دوره المعتاد</th></tr></thead><tbody>
<tr><td><a href="/ar/probability/distributions/binomial-distribution/">ذو الحدين</a></td><td>عدد النجاحات خلال عدد محدد من المحاولات المستقلة، عند احتمال نجاح ثابت</td></tr>
<tr><td>برنولي</td><td>نتيجة محاولة ثنائية واحدة عند احتمال نجاح محدد</td></tr>
<tr><td><a href="/ar/probability/distributions/gamma-distribution/">غاما</a></td><td>متغير موجب، ويتصل بدالة غاما المستخدمة في دالة بيتا</td></tr>
<tr><td>بيتا</td><td>متغير بين الصفر والواحد أو توزيع عدم يقين بايزي حول احتمال مجهول</td></tr>
</tbody></table></div>

<h2>تطبيقات</h2>
<ul class="bullets">
<li>نمذجة عدم اليقين حول احتمال نجاح أو فشل ضمن نموذج بايزي.</li>
<li>تحليل نسب وكسور مستمرة ضمن المجال المناسب، مع الانتباه إلى الصفر والواحد المقاسين فعليًا.</li>
<li>نماذج الاحتمالات السابقة واللاحقة في التجارب ذات نتيجتين.</li>
<li>تفسير أثر المعلومات السابقة والمشاهدات في الاستدلال البايزي.</li>
</ul>

<h2>متى لا يصلح توزيع بيتا؟</h2>
<p>إذا كانت البيانات تحتوي عدد نجاحات صحيحًا، لا يجوز اعتبار ذلك العدد نفسه متغيرًا يتبع بيتا. كذلك، يعطى توزيع بيتا القياسي كثافة داخل المجال المفتوح وليس كتلًا احتمالية مستقلة عند الصفر أو الواحد؛ البيانات التي تتضمن كتلة حقيقية في الطرفين قد تحتاج نموذجًا موسعًا. ويجب تقييم الاستقلال وبنية البيانات قبل تفسير أي توزيع سابق أو لاحق.</p>

<h2>الدرس التالي</h2>
<p>لتطبيقات العدّ يمكن مراجعة <a href="/ar/probability/distributions/binomial-distribution/">التوزيع ذي الحدين</a>. ولمعرفة العلاقة بين بيتا وغاما راجع <a href="/ar/probability/distributions/gamma-distribution/">توزيع غاما</a>.</p>

<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>توزيع بيتا مستمر، وتتركز كتلته الاحتمالية بين الصفر والواحد.</li>
<li>معلمتا الشكل <span dir="ltr">α</span> و<span dir="ltr">β</span> موجبتان، وتتحكمان في موقع التوزيع وشكله وتشتته.</li>
<li>متوسطه <span dir="ltr">α/(α+β)</span>، وتباينه <span dir="ltr">αβ/[(α+β)²(α+β+1)]</span>.</li>
<li>عند <span dir="ltr">Beta(1,1)</span> نحصل على التوزيع المنتظم داخل المجال.</li>
<li>يمكن استعماله توزيعًا سابقًا مقترنًا بايزيًا مع نموذج برنولي/ذي الحدين ضمن افتراضات محددة.</li>
</ul></div>
<div class="lesson-nav">
<a class="btn btn-outline" href="/ar/probability/distributions/gamma-distribution/">← توزيع غاما</a>
<a class="btn" href="/probability/distributions/beta-distribution/" lang="en" dir="ltr">English — Beta Distribution →</a>
</div>
</div></section>
<style>
.esa-beta-equation{box-sizing:border-box;max-width:100%;min-width:0;overflow-x:auto;direction:ltr}
.esa-beta-equation mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}
.esa-beta-equation:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
</style>
