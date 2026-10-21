---
layout: default
title: التوزيع البواسوني
description: شرح عربي متكامل للتوزيع البواسوني، دالة الكتلة الاحتمالية، الافتراضات، المتوسط والتباين، وتقارب ذي الحدين، مع مستكشف تفاعلي لعملية بواسون وزمن الانتظار الأسي.
permalink: /ar/probability/distributions/poisson-distribution/
lang: ar
sidebar: false
translation_pair: poisson-distribution
math: true
---

<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">التوزيعات</span><span class="badge">بيانات العد</span></div>
<h1>التوزيع البواسوني (Poisson Distribution)</h1>
<p><a href="/probability/distributions/poisson-distribution/" lang="en" dir="ltr">English — Poisson Distribution</a></p>
<p class="lead">يُستخدم التوزيع البواسوني لنمذجة عدد مرات وقوع حدث خلال فترة زمنية أو مساحة أو نطاق محدد، عند تحقق افتراضات ملائمة عن آلية وقوع الأحداث.</p>
<div class="hero-actions"><a class="btn btn-outline" href="/probability/distributions/negative-binomial-distribution/" lang="en" dir="ltr">Previous (English): Negative Binomial</a><a class="btn" href="/probability/distributions/hypergeometric-distribution/" lang="en" dir="ltr">Next (English): Hypergeometric</a></div>
</div></section>

<section class="section"><div class="content-narrow">
<h2>ما التوزيع البواسوني؟</h2>
<p>التوزيع البواسوني توزيع احتمالي <strong>متقطع</strong> يصف عدد الأحداث التي تقع في مجال محدد. وعند نمذجة عملية بواسون المتجانسة، تقع الأحداث بمعدل ثابت، وتكون الزيادات في الفترات المنفصلة مستقلة.</p>
<div class="concept-box"><strong>التعريف:</strong><p>المتغير العشوائي البواسوني يحصي عدد الأحداث في فترة زمنية محددة، أو داخل مسافة أو مساحة أو حجم معين. لا يكفي مجرد عدّ الأحداث لتأكيد أن توزيعها بواسوني؛ يجب التحقق من ملاءمة النموذج.</p></div>

<h2>أمثلة على عمليات بواسون</h2>
<div class="example-box"><ul class="bullets">
<li>عدد العملاء الوافدين خلال ساعة.</li>
<li>عدد رسائل البريد الإلكتروني الواردة خلال يوم.</li>
<li>عدد الحوادث عند تقاطع مروري خلال شهر.</li>
<li>عدد العيوب في مساحة محددة من مادة مصنّعة.</li>
<li>عدد المكالمات الواردة خلال دقيقة.</li>
</ul></div>
<p>هذه سياقات محتملة لنماذج العد، وليست أدلة تلقائية على استقلال الأحداث أو ثبات معدلها.</p>

<h2>الافتراضات الأساسية</h2>
<p>من خصائص <strong>عملية بواسون المتجانسة</strong> ما يأتي:</p>
<ul class="bullets">
<li>شدة وقوع الأحداث ثابتة خلال فترة الرصد.</li>
<li>أعداد الأحداث في الفترات غير المتداخلة مستقلة (زيادات مستقلة).</li>
<li>العدد المتوقع للأحداث يتناسب مع طول الفترة، بمعدل ثابت.</li>
<li>احتمال وقوع حدثين أو أكثر في فترة قصيرة جدًا يكون ضئيلًا بالنسبة إلى طول تلك الفترة؛ ويُهمل في الحد من الرتبة الأولى.</li>
</ul>
<p>قد تتبع أعداد الأحداث توزيع بواسون في فترة معينة من دون أن تكون العملية الزمنية الكاملة عملية بواسون متجانسة. لذلك يجب التمييز بين <strong>توزيع العدد</strong> و<strong>نموذج العملية</strong>.</p>

<h2>معلمة المعدل</h2>
<p>يحدد التوزيع البواسوني معامل واحد هو <span dir="ltr">λ</span> (لامبدا)، وهو العدد المتوقع للأحداث في <strong>الفترة المحددة نفسها</strong>:</p>
<div class="esa-math-ltr" dir="ltr">\[
\lambda\geq 0,\qquad \lambda=rt.
\]</div>
<p>هنا <span dir="ltr">r</span> معدل وقوع الأحداث لكل وحدة زمن، و<span dir="ltr">t</span> مدة الملاحظة بوحدة الزمن ذاتها. فالقيمة <span dir="ltr">λ=5</span> تعني متوسط خمسة أحداث لكل فترة محددة؛ لا تعني احتمالًا قدره خمسة.</p>

<h2>الترميز</h2>
<div class="esa-math-ltr" dir="ltr">\[
X\sim\operatorname{Poisson}(\lambda).
\]</div>
<p>يرمز <span dir="ltr">X</span> إلى عدد الأحداث، ويرمز <span dir="ltr">λ</span> إلى متوسط عددها في الفترة المحددة.</p>

<h2>القيم الممكنة</h2>
<p>العدّ غير سالب، ولا يوجد حد أعلى ثابت لعدد الأحداث في نموذج بواسون:</p>
<div class="esa-math-ltr" dir="ltr">\[
X\in\{0,1,2,\ldots\}.
\]</div>
<p>عندما <span dir="ltr">λ=0</span> يصبح عدد الأحداث صفرًا على نحو حتمي.</p>

<h2>دالة الكتلة الاحتمالية</h2>
<p>احتمال وقوع <span dir="ltr">k</span> أحداث بالضبط هو:</p>
<div class="esa-math-ltr" dir="ltr">\[
P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!},
\qquad k=0,1,2,\ldots.
\]</div>
<p>يمثل <span dir="ltr">e</span> أساس اللوغاريتم الطبيعي، و<span dir="ltr">λ</span> متوسط عدد الأحداث، و<span dir="ltr">k</span> عدد الأحداث المرصودة وهو عدد صحيح غير سالب. عند <span dir="ltr">λ=0</span> نستخدم الحالة الحدية مباشرةً: <span dir="ltr">P(X=0)=1</span>، و<span dir="ltr">P(X&gt;0)=0</span>.</p>

<h2>فهم مكونات الصيغة</h2>
<p>تجمع دالة الاحتمال ثلاثة عوامل تؤدي أدوارًا مختلفة:</p>
<div class="table-wrap"><table><thead><tr><th>الحد</th><th>التفسير</th></tr></thead><tbody>
<tr><td><span dir="ltr">e<sup>−λ</sup></span></td><td>عامل يضمن تطبيع الاحتمالات في مجموعها.</td></tr>
<tr><td><span dir="ltr">λ<sup>k</sup></span></td><td>يعكس دور متوسط عدد الأحداث في احتمال العد المحدد.</td></tr>
<tr><td><span dir="ltr">k!</span></td><td>عامل المضروب المرتبط بعدد الأحداث ويظهر في المقام.</td></tr>
</tbody></table></div>

<h2>مثال محسوب: وصول العملاء</h2>
<p>لنفرض أن متوسط عدد الوافدين ثلاثة عملاء في الساعة، وأن نموذج بواسون ملائم. ما احتمال وصول عميلين بالضبط خلال ساعة؟</p>
<div class="esa-math-ltr" dir="ltr">\[
\lambda=3,\qquad
P(X=2)=\frac{e^{-3}3^2}{2!}\approx0.224042.
\]</div>
<p>إذن احتمال وصول عميلين بالضبط يقارب <strong>22.4042%</strong>، وليس هذا تنبؤًا مؤكدًا بعدد العملاء الفعلي.</p>

<h2>المتوسط أو القيمة المتوقعة</h2>
<div class="esa-math-ltr" dir="ltr">\[
\operatorname{E}(X)=\lambda.
\]</div>
<p>يتساوى متوسط العدد النظري للأحداث مع معلمة التوزيع ضمن الفترة المحددة.</p>

<h2>التباين</h2>
<div class="esa-math-ltr" dir="ltr">\[
\operatorname{Var}(X)=\lambda.
\]</div>
<div class="concept-box"><strong>خاصية مهمة:</strong><p>في توزيع بواسون يكون <strong>المتوسط مساويًا للتباين</strong>. وقد تشير زيادة التباين أو انخفاضه الكبير عن المتوسط في بيانات فعلية إلى عدم ملاءمة نموذج بواسون البسيط، وإن لم يكن ذلك اختبارًا حاسمًا وحده.</p></div>

<h2>الانحراف المعياري</h2>
<div class="esa-math-ltr" dir="ltr">\[
\operatorname{SD}(X)=\sqrt{\lambda}.
\]</div>
<p>كلما زاد متوسط الأحداث زاد الانحراف المعياري بوحدات العد، لكن الزيادة تكون بمعدل الجذر التربيعي.</p>

<h2>شكل التوزيع</h2>
<div class="example-box"><ul class="bullets">
<li>عند <span dir="ltr">λ</span> الصغيرة يكون التوزيع عادةً منحرفًا إلى اليمين.</li>
<li>مع ازدياد <span dir="ltr">λ</span> يقل الالتواء النسبي.</li>
<li>عندما تكبر <span dir="ltr">λ</span> يصبح الشكل أقرب إلى المنحنى الجرسي، وقد يصلح التقريب الطبيعي.</li>
</ul></div>
<p>لا يتطلب نموذج بواسون تناظر التوزيع عند القيم الصغيرة للمعلمة.</p>

<h2>نموذج الأحداث النادرة</h2>
<p>يُستخدم توزيع بواسون كثيرًا عندما تكون الأحداث الفردية قليلة الاحتمال، وتوجد فرص عديدة لحدوثها، ويظل متوسط عدد الأحداث خلال الفترة ثابتًا تقريبًا.</p>
<p>لكن «ندرة الحدث» ليست شرطًا كافيًا لوحدها؛ يجب النظر أيضًا إلى الاستقلال وطريقة تحديد الفترة أو التعرض.</p>

<h2>بواسون بوصفه تقريبًا للتوزيع ذي الحدين</h2>
<p>إذا كان <span dir="ltr">X_n</span> ذا توزيع ذي حدين بعدد تجارب كبير <span dir="ltr">n</span>، واحتمال نجاح صغير <span dir="ltr">p</span>، مع بقاء <span dir="ltr">np</span> قريبًا من قيمة محدودة، يمكن تقريب توزيع العدد بتوزيع بواسون:</p>
<div class="esa-math-ltr" dir="ltr">\[
n\to\infty,\quad p\to0,\quad np\to\lambda.
\]</div>
<p>تتعلق جودة التقريب عند <span dir="ltr">n</span> المنتهية بكلٍّ من <span dir="ltr">n</span> و<span dir="ltr">p</span>؛ وليست كل تجربة نادرة مستقلة قابلة للتقريب تلقائيًا بالطريقة نفسها.</p>

<h2>تطبيقات في علم البيانات</h2>
<ul class="bullets">
<li>تحليل عدد زيارات المواقع خلال فترات ثابتة.</li>
<li>دراسة أعداد وصول العملاء إلى نقاط الخدمة.</li>
<li>نمذجة المكالمات في مراكز الاتصال.</li>
<li>عدّ العيوب في خطوط الإنتاج.</li>
<li>رصد بعض الأحداث الصحية عبر الزمن.</li>
<li>تحليل أعداد الأحداث في شبكات الاتصال.</li>
</ul>
<p>يجب في كل تطبيق مواءمة معدل الأحداث مع طول فترة الرصد أو مقدار التعرض، وفحص التغاير الزمني والتجمع والاعتماد.</p>

<h2>المقارنة بين بواسون وذي الحدين</h2>
<div class="table-wrap"><table><thead><tr><th>التوزيع</th><th>ما الذي يُنمذجه؟</th></tr></thead><tbody>
<tr><td>ذو الحدين</td><td>عدد النجاحات ضمن عدد ثابت من تجارب برنولي المستقلة والمتساوية في احتمال النجاح.</td></tr>
<tr><td>بواسون</td><td>عدد الأحداث خلال مجال محدد، بمتوسط عدد أحداث معين، ويمكن اشتقاقه من عملية بواسون عند تحقق شروطها.</td></tr>
</tbody></table></div>
<p>كلاهما ينمذج أعدادًا، لكن بنيتهما وافتراضاتهما الأساسية ليست متطابقة.</p>

<h2>القيود والحالات غير الملائمة</h2>
<p>لا يكون معدل وقوع الأحداث ثابتًا أو زياداتها مستقلة دائمًا. وقد تُظهر البيانات تجمّع الأحداث أو اختلاف شدة وقوعها بين الأفراد والفترات. في هذه الحالات ينبغي النظر في نماذج بديلة أو توسيعات مناسبة.</p>
<div class="example-box"><p>السحب من أوراق اللعب دون إرجاع، أو اختيار منتجات من شحنة محدودة دون إرجاع، أو أخذ عينة من مجتمع محدود: هذه مواقف قد يناسبها توزيع فوق هندسي بدل نموذج بواسون المستقل.</p></div>

<h2>الدرس التالي</h2>
<p>نتناول لاحقًا <strong>التوزيع فوق الهندسي</strong> الذي يصف أعداد النجاحات عند السحب من مجتمع محدود دون إرجاع.</p>

<section class="concept-box" id="esa-poisson-exponential-explorer" aria-labelledby="esa-poisson-exponential-heading" style="max-width:100%;min-width:0;overflow-wrap:anywhere">
<h2 id="esa-poisson-exponential-heading">مستكشف بواسون وزمن الانتظار الأسي</h2>
<p>في <strong>عملية بواسون متجانسة</strong> بمعدل وقوع <span dir="ltr">r</span> حدث في الدقيقة، يتبع عدد الأحداث <span dir="ltr">N(t)</span> توزيع بواسون بمتوسط <span dir="ltr">rt</span>، ويتبع زمن الانتظار <span dir="ltr">T</span> حتى الحدث التالي توزيعًا أسيًا بالمعدل نفسه. قارِن الاحتمالات خلال المدة <span dir="ltr">t</span>.</p>
<form id="esa-event-explorer-form" novalidate>
<div class="esa-event-input-grid">
<div><label for="esa-event-rate">معدل الأحداث في الدقيقة (r)</label><input id="esa-event-rate" type="number" inputmode="decimal" min="0" max="20" step="any" value="2" dir="ltr" required></div>
<div><label for="esa-event-time">مدة الرصد بالدقائق (t)</label><input id="esa-event-time" type="number" inputmode="decimal" min="0" max="60" step="any" value="1" dir="ltr" required></div>
</div>
<p id="esa-event-error" role="alert" hidden></p>
<div id="esa-event-results" role="status" aria-live="polite" aria-atomic="true">
<div class="esa-event-result-grid">
<p>احتمال عدم وقوع حدث <span dir="ltr">P(N(t)=0)</span>: <strong><output id="esa-event-none" dir="ltr">0.135335</output></strong></p>
<p>احتمال الانتظار أكثر من المدة <span dir="ltr">P(T&gt;t)</span>: <strong><output id="esa-event-survival" dir="ltr">0.135335</output></strong></p>
<p>احتمال وقوع حدث واحد على الأقل <span dir="ltr">P(N(t)≥1)</span>: <strong><output id="esa-event-at-least-one" dir="ltr">0.864665</output></strong></p>
<p>عدد الأحداث المتوقع <span dir="ltr">rt</span>: <strong><output id="esa-event-expected" dir="ltr">2.000000</output></strong></p>
<p>متوسط زمن الانتظار بالدقائق <span dir="ltr">1/r</span>: <strong><output id="esa-event-meanwait" dir="ltr">0.500000</output></strong></p>
</div>
<p id="esa-event-explanation">يتساوى احتمال عدم وقوع أي حدث مع احتمال الانتظار أكثر من المدة، وكلاهما يساوي <span dir="ltr">e<sup>−rt</sup></span>.</p>
</div>
<button type="button" id="esa-event-reset" class="btn btn-outline">إعادة القيم الافتراضية</button>
</form>
<p class="muted-mini"><strong>الافتراضات والقيود:</strong> تتطلب هذه الهوية عملية بواسون متجانسة بمعدل موجب وثابت مع زيادات مستقلة. التجمع، أو الاعتماد بين الأحداث، أو تغير المعدل مع الزمن، قد يجعل نموذج زمن الانتظار الأسي غير مناسب. قد تُقرّب النتائج إلى ست منازل عشرية؛ وهذا لا يعني أن قيمة صغيرة جدًا تساوي صفرًا تمامًا.</p>
</section>
<style>
#esa-poisson-exponential-explorer{min-width:0;max-width:100%;overflow-wrap:anywhere}
#esa-poisson-exponential-explorer .esa-event-input-grid,#esa-poisson-exponential-explorer .esa-event-result-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 16px;margin:12px 0}
#esa-poisson-exponential-explorer .esa-event-input-grid>div,#esa-poisson-exponential-explorer .esa-event-result-grid>p{min-width:0;margin:5px 0}
#esa-poisson-exponential-explorer label{display:block;font-weight:650;margin:0 0 6px}
#esa-poisson-exponential-explorer input[type="number"]{display:block;width:100%;max-width:100%;min-width:0;box-sizing:border-box;padding:10px;font:inherit;background:var(--surface);color:var(--text);border:1px solid var(--border-strong);border-radius:8px}
#esa-poisson-exponential-explorer input:focus-visible,#esa-poisson-exponential-explorer button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
#esa-poisson-exponential-explorer #esa-event-error{color:#b42318;font-weight:650}
#esa-poisson-exponential-explorer [hidden]{display:none!important}
@media(max-width:600px){#esa-poisson-exponential-explorer .esa-event-input-grid,#esa-poisson-exponential-explorer .esa-event-result-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script src="{{ '/js/poisson-exponential-explorer.js' | relative_url }}" defer></script>

<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>يصف توزيع بواسون أعداد الأحداث في مجال محدد عند ملاءمة افتراضاته.</li>
<li>معلمته <span dir="ltr">λ</span> هي متوسط عدد الأحداث في الفترة.</li>
<li>تستخدم دالة الكتلة الاحتمالية <span dir="ltr">λ</span> والثابت <span dir="ltr">e</span> والمضروب.</li>
<li>المتوسط والتباين كلاهما يساوي <span dir="ltr">λ</span>، والانحراف المعياري يساوي جذرها التربيعي.</li>
<li>قد يقرب التوزيع ذا الحدين عند كثرة التجارب وصغر احتمال النجاح.</li>
<li>في عملية بواسون المتجانسة يتطابق احتمال عدم وقوع أحداث خلال <span dir="ltr">t</span> مع احتمال أن يتجاوز زمن الانتظار <span dir="ltr">t</span>.</li>
</ul></div>
<div class="lesson-nav">
<a class="btn btn-outline" href="/probability/distributions/negative-binomial-distribution/" lang="en" dir="ltr">← Negative Binomial (English)</a>
<a class="btn" href="/probability/distributions/hypergeometric-distribution/" lang="en" dir="ltr">Hypergeometric (English) →</a>
</div>
</div></section>
