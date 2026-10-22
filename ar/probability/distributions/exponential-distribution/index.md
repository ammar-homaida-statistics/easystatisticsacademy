---
layout: default
title: التوزيع الأسي
description: درس عربي متكامل عن التوزيع الأسي وأزمنة الانتظار مع شرح معدل الأحداث والكثافة والتوزيع التراكمي والمتوسط والتباين وانعدام الذاكرة وتطبيقات بواسون.
permalink: /ar/probability/distributions/exponential-distribution/
lang: ar
sidebar: false
translation_pair: exponential-distribution
math: true
---

<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">التوزيعات المستمرة</span><span class="badge">أزمنة الانتظار</span></div>
<h1>التوزيع الأسي (Exponential Distribution)</h1>
<p><a href="/probability/distributions/exponential-distribution/" lang="en" dir="ltr">English — Exponential Distribution</a></p>
<p class="lead">كيف نحسب زمن الانتظار حتى الحدث التالي عندما تقع الأحداث وفق عملية بواسون متجانسة؟</p>
<div class="hero-actions"><a class="btn btn-outline" href="/ar/probability/distributions/poisson-distribution/">توزيع بواسون بالعربية</a>
<a class="btn btn-outline" href="/ar/probability/distributions/geometric-distribution/">التوزيع الهندسي بالعربية</a></div>
</div></section>
<section class="section"><div class="content-narrow">

<h2>ما التوزيع الأسي؟</h2>
<p>التوزيع الأسي هو توزيع احتمالي <strong>مستمر</strong> يصف الزمن غير السالب اللازم حتى وقوع الحدث التالي. في <strong>عملية بواسون المتجانسة</strong>، تتبع أزمنة الانتظار بين الأحداث المتتالية هذا التوزيع وتكون مستقلة. لا يلزم ذلك لأي آلية أخرى لوصول الأحداث.</p>
<div class="concept-box"><strong>التعريف:</strong><p>نرمز بزمن الانتظار <span dir="ltr">T</span> ونقيسه بوحدة ثابتة، مثل الدقيقة أو الساعة، خلافًا لنموذج عدّ المحاولات.</p></div>

<h2>السؤال الأساسي</h2>
<p>بدلًا من حساب عدد الأحداث، نسأل <strong>كم ننتظر حتى الحدث التالي؟</strong></p>
<div class="example-box"><ul class="bullets">
<li>كم دقيقة حتى وصول العميل التالي؟</li>
<li>كم ثانية حتى المكالمة القادمة؟</li>
<li>كم ساعة حتى الزيارة التالية للموقع الإلكتروني؟</li>
<li>متى يحدث العطل القادم لمكون يملك معدل فشل ثابتًا؟</li>
</ul></div>

<h2>العلاقة بتوزيع بواسون</h2>
<p>يصف <a href="/ar/probability/distributions/poisson-distribution/">توزيع بواسون</a> <strong>عدد الأحداث</strong> في فترة زمنية، بينما يصف الأسي <strong>الانتظار بين الأحداث</strong> ضمن عملية بواسون المتجانسة بمعدل <span dir="ltr">λ</span>.</p>
<div class="table-wrap"><table><thead><tr><th>التوزيع</th><th>السؤال</th></tr></thead><tbody>
<tr><td>بواسون</td><td>كم حدثًا في مدة معينة؟</td></tr>
<tr><td>الأسي</td><td>كم الوقت حتى الحدث القادم؟</td></tr>
</tbody></table></div>
<p>تنبع هذه العلاقة من افتراضات عملية الوصول، ولا تنطبق تلقائيًا على كل مجموعة بيانات تمثل أحداثًا عبر الزمن.</p>

<h2>معلمة المعدل</h2>
<p>يستخدم التوزيع الأسي <strong>معدل أحداث موجبًا</strong>، يرمز إليه بـ <span dir="ltr">λ</span>:</p>
<div class="esa-exp-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="معلمة المعدل موجبة">\[\lambda>0.\]</div>
<p>إذا كان <span dir="ltr">λ=4/hour</span> فهذا يعني متوسط أربعة أحداث في الساعة. تُقاس <span dir="ltr">λ</span> بوحدة <strong>زمن⁻¹</strong>، أما الانتظار <span dir="ltr">T</span> فبوحدة الزمن. يلزم توحيد الوحدات قبل إجراء الحسابات.</p>

<h2>الترميز واصطلاح المعلمات</h2>
<div class="esa-exp-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="ترميز التوزيع الأسي">\[T\sim\operatorname{Exponential}(\lambda),\quad\lambda>0.\]</div>
<p>نتبع اصطلاح <strong>المعدل</strong>، لا المقياس. في بعض البرامج يُستخدم <span dir="ltr">θ=1/λ</span> بوصفه معلمة المقياس؛ لذلك يجب التحقق من اصطلاح البرنامج.</p>

<h2>دالة الكثافة الاحتمالية</h2>
<div class="esa-exp-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="دالة الكثافة للأسّي">\[
f_T(t)=\begin{cases}\lambda e^{-\lambda t},& t\ge0,\\0,&t<0.\end{cases}
\]</div>
<p>دالة الكثافة <strong>ليست</strong> احتمال وقوع زمن بعينه: لأي عدد مفرد <span dir="ltr">t</span>، يكون <span dir="ltr">P(T=t)=0</span>. تمثل المساحة تحت منحنى الكثافة على فترة زمنية الاحتمال المقابل.</p>

<h2>شكل الكثافة</h2>
<p>يبدأ منحنى الكثافة عند <span dir="ltr">f(0)=λ</span> ويتناقص أسيًا نحو الصفر. لذا تكون فترات الانتظار القصيرة أكثر احتمالًا من الفترات الطويلة المساوية لها في الطول عند أزمنة أبعد، ويكون التوزيع ملتويًا نحو اليمين.</p>

<h2>دالة التوزيع التراكمي</h2>
<p>احتمال وصول الحدث خلال زمن لا يتجاوز <span dir="ltr">t</span> هو:</p>
<div class="esa-exp-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="دالة التوزيع التراكمي">\[
F_T(t)=P(T\le t)=
\begin{cases}0,&t<0,\\1-e^{-\lambda t},&t\ge0.\end{cases}
\]</div>
<p>تساوي الدالة صفرًا عند الصفر، وتقترب من الواحد بزيادة الزمن.</p>

<h2>احتمال الانتظار مدة أطول</h2>
<p>دالة البقاء أو احتمال عدم وصول الحدث حتى الزمن <span dir="ltr">t</span> تساوي:</p>
<div class="esa-exp-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="دالة البقاء">\[P(T>t)=e^{-\lambda t},\qquad t\ge0.\]</div>
<p>بالتالي يكون مجموع احتمال الوصول حتى الزمن المحدد واحتمال الانتظار بعده واحدًا.</p>

<h2>مثال: وصول العملاء</h2>
<p>افترض أن العملاء يصلون وفق عملية بواسون متجانسة بمعدل <strong>عميلين في الدقيقة</strong>. احتمال وصول العميل القادم خلال دقيقة هو:</p>
<div class="esa-exp-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="مثال احتمال الدقيقة">\[
P(T\le1)=1-e^{-2}\approx0.864665.
\]</div>
<p>أي نحو <strong>86.47%</strong>. واحتمال أن يزيد الانتظار على دقيقة يساوي <span dir="ltr">e⁻² ≈ 0.135335</span>.</p>

<h2>المتوسط أو القيمة المتوقعة</h2>
<p>يتناسب متوسط زمن الانتظار عكسيًا مع معدل الأحداث:</p>
<div class="esa-exp-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="متوسط التوزيع الأسي">\[E(T)=\frac{1}{\lambda}.\]</div>
<p>ارتفاع المعدل يعني انتظارًا أقصر في المتوسط، مع استمرار احتمال انتظار فترة أطول في ملاحظة بعينها.</p>

<h2>مثال على المتوسط</h2>
<p>عند <span dir="ltr">λ=4/hour</span> يكون متوسط زمن الانتظار:</p>
<div class="esa-exp-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="متوسط الانتظار ربع ساعة">\[
E(T)=\frac14\,\text{hour}=15\,\text{minutes}.
\]</div>
<p>هذا <strong>متوسط نظري</strong> لفترات انتظار كثيرة، ولا يعني وصول الحدث بعد 15 دقيقة بالتحديد.</p>

<h2>التباين والانحراف المعياري</h2>
<div class="esa-exp-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="التباين والانحراف المعياري">\[
\operatorname{Var}(T)=\frac1{\lambda^2},
\qquad \operatorname{SD}(T)=\frac1\lambda.
\]</div>
<p>تقاس القيمة المتوقعة والانحراف المعياري بوحدة <strong>الزمن</strong>، بينما يقاس التباين بوحدة <strong>الزمن المربع</strong>. ويتساوى المتوسط والانحراف المعياري في هذا التوزيع.</p>

<h2>خاصية انعدام الذاكرة</h2>
<div class="concept-box"><strong>المعنى:</strong><p>لا يتغير توزيع <strong>الوقت الإضافي المتبقي</strong> بعد مضي فترة انتظار سابقة دون وصول حدث في النموذج الأسي. تعتمد الخاصية على المعدل الثابت، وليست صحيحة لأي نظام وصول عشوائي.</p></div>

<h2>صيغة انعدام الذاكرة</h2>
<div class="esa-exp-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="خاصية انعدام الذاكرة">\[
P(T>s+t\mid T>s)=P(T>t)=e^{-\lambda t},\quad s,t\ge0.
\]</div>
<p>ويمكن إثباتها باستعمال احتمال البقاء:</p>
<div class="esa-exp-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="برهان انعدام الذاكرة">\[
\frac{P(T>s+t)}{P(T>s)}
=\frac{e^{-\lambda(s+t)}}{e^{-\lambda s}}
=e^{-\lambda t}.
\]</div>

<h2>كيف نفسر انعدام الذاكرة؟</h2>
<p>إذا لم يصل أي عميل منذ 20 دقيقة، فإن توزيع زمن الانتظار من اللحظة الحالية يظل كما كان عند البداية في نموذج وصول بواسون المتجانس. ولا يعني ذلك أن الحدث أصبح «مستحقًا» أو أن التأخر يزيد احتمال وقوعه فورًا.</p>

<h2>العلاقة بالتوزيع الهندسي</h2>
<p><a href="/ar/probability/distributions/geometric-distribution/">التوزيع الهندسي</a> يعدّ <strong>المحاولات المنفصلة</strong> حتى أول نجاح، بينما يمثل الأسي <strong>الزمن المستمر</strong> حتى الحدث القادم. كلا النموذجين يمتلك خاصية انعدام الذاكرة ضمن افتراضاته.</p>
<div class="table-wrap"><table><thead><tr><th>الصفة</th><th>الهندسي</th><th>الأسي</th></tr></thead><tbody>
<tr><td>المتغير</td><td>عدد المحاولات حتى أول نجاح</td><td>الوقت حتى الحدث التالي</td></tr>
<tr><td>القيم</td><td>أعداد صحيحة موجبة</td><td>أزمنة غير سالبة</td></tr>
<tr><td>المعلمة</td><td>احتمال النجاح p</td><td>المعدل λ</td></tr>
</tbody></table></div>

<h2>تطبيقات التوزيع الأسي</h2>
<ul class="bullets">
<li>أوقات وصول العملاء في الطوابير البواسونية.</li>
<li>الفاصل بين المكالمات عند معدل وصول ثابت.</li>
<li>أعمار المكونات ذات معدل الفشل الثابت.</li>
<li>الفواصل بين وصول الحزم على الشبكات وفق افتراضات مناسبة.</li>
<li>تحليل الاعتمادية وبحوث العمليات ونمذجة أزمنة الانتظار.</li>
</ul>
<p>يجب فحص ثبات المعدل والاستقلال وملاءمة نموذج الوصول للبيانات قبل استخدام النتائج.</p>

<h2>أهمية التوزيع الأسي</h2>
<p>يوفر نموذجًا بسيطًا ودقيقًا لبعض فترات الانتظار، ويربط بين توزيع بواسون ونظرية الطوابير وتحليل الاعتمادية. ويساعد فهمه على الانتقال إلى توزيع غاما لأزمنة الانتظار حتى وقوع عدة أحداث.</p>

<h2>حدود النموذج</h2>
<p>يعتمد التوزيع الأسي على <strong>معدل خطر ثابت</strong>. عند وجود موسمية أو معدل وصول متغير أو اعتماد بين الأحداث، فقد تكون هناك حاجة إلى نموذج بديل.</p>
<p>في عملية بواسون متجانسة يتبع <strong>الانتظار حتى الحدث الثالث</strong> توزيع غاما بمعلمة شكل تساوي 3، وليس توزيعًا أسيًا.</p>

<h2>الدرس التالي</h2>
<p>راجع <a href="/ar/probability/distributions/poisson-distribution/">توزيع بواسون بالعربية</a> لمتابعة العلاقة بين أعداد الأحداث وأزمنة الانتظار. ولمعرفة توزيع زمن الانتظار حتى عدة أحداث، اقرأ <a href="/probability/distributions/gamma-distribution/" lang="en" dir="ltr">Gamma Distribution (English)</a>.</p>

<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>التوزيع الأسي مستمر ويصف أزمنة الانتظار في نموذج معدل أحداث ثابت.</li>
<li>معدل الأحداث λ موجب، ووحدته مقلوب الزمن.</li>
<li>دالة الكثافة للزمن غير السالب <span dir="ltr">λe<sup>−λt</sup></span>، ودالة التوزيع <span dir="ltr">1−e<sup>−λt</sup></span>.</li>
<li>المتوسط والانحراف المعياري كلاهما <span dir="ltr">1/λ</span>؛ والتباين <span dir="ltr">1/λ²</span>.</li>
<li>خاصية انعدام الذاكرة والعلاقة ببواسون والهندسي ترتبطان بافتراضات النموذج.</li>
</ul></div>
<div class="lesson-nav">
<a class="btn btn-outline" href="/ar/probability/distributions/poisson-distribution/">← بواسون بالعربية</a>
<a class="btn" href="/probability/distributions/gamma-distribution/" lang="en" dir="ltr">Gamma Distribution (English) →</a>
</div>
</div></section>
<style>
.esa-exp-equation{box-sizing:border-box;min-width:0;max-width:100%;overflow-x:auto;direction:ltr}
.esa-exp-equation mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}
.esa-exp-equation:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
</style>
