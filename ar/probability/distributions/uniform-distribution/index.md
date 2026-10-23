---
layout: default
title: التوزيع المنتظم
description: درس عربي شامل للتوزيع المنتظم المستمر والكثافة والاحتمالات على الفترات والمتوسط والتباين والانحراف المعياري مع مختبر تفاعلي موحّد مع الدرس الإنجليزي.
permalink: /ar/probability/distributions/uniform-distribution/
lang: ar
sidebar: false
translation_pair: uniform-distribution
math: true
---

<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">التوزيعات المستمرة</span><span class="badge">الاحتمال بوصفه مساحة</span></div>
<h1>التوزيع المنتظم (Uniform Distribution)</h1>
<p><a href="/probability/distributions/uniform-distribution/" lang="en" dir="ltr">English — Uniform Distribution</a></p>
<p class="lead">إذا كان لكل الفترات المتساوية الطول داخل مجال محدد الاحتمال نفسه، فإن التوزيع المنتظم المستمر نموذج طبيعي لبداية فهم دوال الكثافة والمساحات الاحتمالية.</p>
<div class="hero-actions"><a class="btn btn-outline" href="/ar/probability/distributions/beta-distribution/">← توزيع بيتا بالعربية</a>
<a class="btn btn-outline" href="/probability/distributions/uniform-distribution/" lang="en" dir="ltr">English lesson</a></div>
</div></section>

<section class="section"><div class="content-narrow">
<h2>ما التوزيع المنتظم؟</h2>
<p>التوزيع المنتظم نموذج احتمالي تكون فيه جميع الفترات <strong>المتساوية الطول</strong> داخل مجال محدد متساوية الاحتمال. ويُسمّى المتغير <strong>مستمرًا</strong> عندما يمكنه أخذ أي قيمة حقيقية داخل المجال. ينبغي عدم الخلط بين تساوي احتمالات الفترات وبين احتمال الحصول على قيمة دقيقة واحدة.</p>

<h2>مثال بسيط</h2>
<p>افترض أن وقت وصول منتظر يقع بين الدقيقة 0 والدقيقة 10 بصورة منتظمة وفق النموذج المستمر. يكون احتمال الوصول بين الدقيقتين 2 و5 مساويًا لطول تلك الفترة مقسومًا على طول المجال الكلي، أي <strong>3/10 = 0.30</strong>. وفي المقابل، كل دقيقة بعينها لها احتمال صفري لأن المتغير مستمر.</p>

<h2>التوزيع المنتظم المستمر</h2>
<p>يُرمز إلى المجال بالحد الأدنى <span dir="ltr">a</span> والحد الأعلى <span dir="ltr">b</span> مع <span dir="ltr">a&lt;b</span>. لا تشترط الصيغة أن تكون الحدود أعدادًا صحيحة؛ لكن المختبر التفاعلي يستعمل حدودًا عملية مناسبة للتحريك.</p>
<div class="esa-uniform-equation" dir="ltr" tabindex="0" role="region" aria-label="مجال المنتظم">\[
a\le X\le b,\qquad a<b.
\]</div>

<h2>الترميز</h2>
<div class="esa-uniform-equation" dir="ltr" tabindex="0" role="region" aria-label="ترميز التوزيع المنتظم">\[
X\sim\operatorname{Uniform}(a,b).
\]</div>
<p>هذا ترميز <strong>التوزيع المنتظم المستمر</strong> بين الحدين المذكورين، وليس التوزيع المنتظم المنفصل على مجموعة محدودة من النتائج.</p>

<h2>دالة الكثافة الاحتمالية</h2>
<p>تكون الكثافة ثابتة داخل المجال وصفرًا خارجه:</p>
<div class="esa-uniform-equation" dir="ltr" tabindex="0" role="region" aria-label="كثافة المنتظم">\[
f_X(x)=
\begin{cases}
\dfrac{1}{b-a},&a<x<b,\\
0,&x<a\text{ or }x>b.
\end{cases}
\]</div>
<p>يمكن تعريف قيمة الكثافة عند الطرفين بأي شكل ملائم دون تغيير الاحتمالات؛ لأن احتمال أي نقطة مفردة يساوي صفرًا.</p>

<h2>لماذا الكثافة ثابتة؟</h2>
<p>يجب أن يساوي إجمالي المساحة تحت الكثافة واحدًا. عرض المستطيل هو <span dir="ltr">b−a</span>، ولذلك يجب أن يكون ارتفاعه <span dir="ltr">1/(b−a)</span>.</p>
<div class="esa-uniform-equation" dir="ltr" tabindex="0" role="region" aria-label="مساحة الكثافة">\[
\int_a^b\frac{1}{b-a}\,dx=1.
\]</div>

<h2>الشكل البياني</h2>
<p>الكثافة على هيئة مستطيل أفقي، ويظل الارتفاع ثابتًا مهما تحركنا داخل المجال. إذا ازداد طول المجال مع بقائه منتظمًا، يقل ارتفاع المستطيل حتى تبقى المساحة الكلية واحدة.</p>

<h2>الاحتمال بوصفه مساحة</h2>
<p>عند اختيار فترة فرعية <span dir="ltr">[c,d]</span> داخل المجال، يساوي احتمال وقوع المتغير فيها مساحة المستطيل الواقع تحت الكثافة بين الحدين.</p>
<div class="esa-uniform-equation" dir="ltr" tabindex="0" role="region" aria-label="احتمال الفترة في المنتظم">\[
P(c\le X\le d)=\frac{d-c}{b-a},
\qquad a\le c\le d\le b.
\]</div>

<h2>مثال عددي على الاحتمال</h2>
<p>في توزيع منتظم بين الصفر والعشرة، احتمال الوقوع بين 2 و5 هو:</p>
<div class="esa-uniform-equation" dir="ltr" tabindex="0" role="region" aria-label="احتمال بين اثنين وخمسة">\[
P(2\le X\le5)=\frac{5-2}{10-0}=0.30.
\]</div>
<p>لاحظ أن طول الفترة المختارة <strong>3</strong> بينما طول المجال الكلي <strong>10</strong>.</p>

<div class="concept-box esa-uniform-lab" id="esa-uniform-area-explorer" role="group" aria-labelledby="esa-uniform-lab-heading">
<h2 id="esa-uniform-lab-heading">مختبر تفاعلي: مساحة الاحتمال في التوزيع المنتظم</h2>
<p>حرّك حدّي التوزيع <span dir="ltr">a,b</span>، ثم اختر الفترة الفرعية <span dir="ltr">c,d</span>. يمثل المستطيل المظلل <strong>مساحة احتمال</strong>، بعرض <span dir="ltr">d−c</span> وارتفاع الكثافة <span dir="ltr">1/(b−a)</span>. قيمة الكثافة وحدها ليست احتمالًا.</p>
<div class="esa-uniform-fields">
<div><label for="esa-uniform-a"><strong>الحد الأدنى للتوزيع a: <output for="esa-uniform-a" id="esa-uniform-a-value">0</output></strong></label>
<input id="esa-uniform-a" type="range" min="0" max="9" step="1" value="0" dir="ltr"></div>
<div><label for="esa-uniform-b"><strong>الحد الأعلى للتوزيع b: <output for="esa-uniform-b" id="esa-uniform-b-value">10</output></strong></label>
<input id="esa-uniform-b" type="range" min="1" max="20" step="1" value="10" dir="ltr"></div>
<div><label for="esa-uniform-c"><strong>بداية الفترة المختارة c: <output for="esa-uniform-c" id="esa-uniform-c-value">2</output></strong></label>
<input id="esa-uniform-c" type="range" min="0" max="10" step="0.5" value="2" dir="ltr"></div>
<div><label for="esa-uniform-d"><strong>نهاية الفترة المختارة d: <output for="esa-uniform-d" id="esa-uniform-d-value">5</output></strong></label>
<input id="esa-uniform-d" type="range" min="2" max="10" step="0.5" value="5" dir="ltr"></div>
</div>
<svg id="esa-uniform-area-plot" viewBox="0 0 360 180" width="360" height="180" role="img" aria-label="كثافة منتظمة من الصفر إلى عشرة؛ احتمال المنطقة المظللة من اثنين إلى خمسة يساوي 0.30">
<line x1="36" y1="140" x2="341" y2="140" stroke="currentColor" stroke-width="1.5"/>
<line x1="36" y1="140" x2="36" y2="24" stroke="currentColor" stroke-width="1.5"/>
<rect x="50" y="40" width="280" height="100" fill="#94a3b8" fill-opacity=".17" stroke="#64748b" stroke-width="1.6"/>
<rect id="esa-uniform-highlight" x="106" y="40" width="84" height="100" fill="#0d9488" fill-opacity=".65"/>
<text id="esa-uniform-left-label" x="50" y="157" font-size="11" fill="currentColor" text-anchor="middle">0</text>
<text id="esa-uniform-right-label" x="330" y="157" font-size="11" fill="currentColor" text-anchor="middle">10</text>
<text x="37" y="18" font-size="11" fill="currentColor">Density</text><text x="340" y="157" font-size="11" fill="currentColor">X</text>
</svg>
<div class="esa-uniform-results" role="status" aria-live="polite" aria-atomic="true">
<p>الفترة المختارة: <strong id="esa-uniform-interval" dir="ltr">[2, 5]</strong>. العرض: <output id="esa-uniform-width" dir="ltr">3.00</output>.</p>
<p>ارتفاع الكثافة الثابت: <strong><output id="esa-uniform-density" dir="ltr">0.1000</output></strong>.
المساحة المظللة / الاحتمال: <strong><output id="esa-uniform-probability" dir="ltr">0.3000</output></strong>.</p>
<p>المتوسط <span dir="ltr">E(X)</span> = <output id="esa-uniform-mean" dir="ltr">5.00</output>.
التباين <span dir="ltr">Var(X)</span> = <output id="esa-uniform-variance" dir="ltr">8.3333</output>.
الانحراف المعياري = <output id="esa-uniform-sd" dir="ltr">2.8868</output>.</p>
<p><strong>احتمال النقطة المفردة:</strong> لكل قيمة محددة <span dir="ltr">P(X=c)=0</span>، بما في ذلك طرفا المجال. ضم الطرفين أو استبعادهما لا يغير احتمال الفترة.</p>
</div>
<button type="button" class="btn btn-outline" id="esa-uniform-reset">استعادة المثال الافتراضي</button>
<p class="muted-mini">تلتزم المدخلات بالحدود <span dir="ltr">0≤a&lt;b≤20</span> و<span dir="ltr">a≤c≤d≤b</span>. يعيد الرسم ضبط المحور الأفقي وفق المجال المختار. جميع الحسابات تخص التوزيع المنتظم المستمر.</p>
</div>
<style>
      #esa-uniform-area-explorer {box-sizing:border-box;width:100%;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-uniform-area-explorer .esa-uniform-fields {
        display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));
        gap:12px;margin:14px 0
      }
      #esa-uniform-area-explorer .esa-uniform-fields>div {min-width:0}
      #esa-uniform-area-explorer label {display:block;margin-bottom:8px}
      #esa-uniform-area-explorer input[type="range"] {
        display:block;box-sizing:border-box;width:100%;max-width:100%;
        min-width:0;margin:0;padding:0
      }
      #esa-uniform-area-explorer svg {
        display:block;width:100%;max-width:520px;height:auto;margin:12px auto;
        overflow:visible
      }
      #esa-uniform-area-explorer .esa-uniform-results p {margin:10px 0}
    </style>
<script src="{{ '/js/uniform-area-explorer.js' | relative_url }}" defer></script>

<h2>احتمال القيمة المفردة</h2>
<p>مهما كانت قيمة <span dir="ltr">x</span> الواقعة داخل المجال، فإن احتمال أخذ هذه القيمة الدقيقة يساوي صفرًا؛ ولا يتعارض ذلك مع احتمال موجب للفترة التي تحتويها.</p>
<div class="esa-uniform-equation" dir="ltr" tabindex="0" role="region" aria-label="احتمال نقطة">\[
P(X=x)=0\qquad\text{for each fixed }x.
\]</div>

<h2>المتوسط أو القيمة المتوقعة</h2>
<p>المتوسط يقع في منتصف المجال لأن الكثافة متماثلة حول نقطة المنتصف.</p>
<div class="esa-uniform-equation" dir="ltr" tabindex="0" role="region" aria-label="متوسط التوزيع المنتظم">\[
E(X)=\frac{a+b}{2}.
\]</div>

<h2>مثال على المتوسط</h2>
<p>إذا كان <span dir="ltr">X∼Uniform(0,10)</span> فإن:</p>
<div class="esa-uniform-equation" dir="ltr" tabindex="0" role="region" aria-label="متوسط الصفر والعشرة">\[
E(X)=\frac{0+10}{2}=5.
\]</div>

<h2>التباين</h2>
<p>يقيس التباين تشتت القيم عن المتوسط. ينمو مع مربع طول المجال، مما يوضح أثر اتساع الحدود.</p>
<div class="esa-uniform-equation" dir="ltr" tabindex="0" role="region" aria-label="تباين المنتظم">\[
\operatorname{Var}(X)=\frac{(b-a)^2}{12}.
\]</div>
<p>في المثال السابق يكون التباين <span dir="ltr">100/12≈8.3333</span> وحدة مربعة.</p>

<h2>الانحراف المعياري</h2>
<p>يساوي الجذر التربيعي للتباين، ويقاس بوحدة المتغير نفسه بدلًا من مربع الوحدة.</p>
<div class="esa-uniform-equation" dir="ltr" tabindex="0" role="region" aria-label="الانحراف المعياري للمنتظم">\[
\operatorname{SD}(X)=\frac{b-a}{\sqrt{12}}.
\]</div>
<p>عند <span dir="ltr">a=0</span> و<span dir="ltr">b=10</span> يكون الانحراف المعياري قرابة <span dir="ltr">2.8868</span>.</p>

<h2>تطبيقات شائعة</h2>
<ul class="bullets"><li>توليد أرقام شبه عشوائية في المحاكاة الإحصائية.</li>
<li>نمذجة مواقف تكون فيها الفترات المتساوية الطول متساوية الاحتمال وفق افتراض صريح.</li>
<li>توضيح معنى الكثافة والمساحة والفرق بين متوسط المتغير وقيمة مشاهدة بعينها.</li></ul>

<h2>التوزيع المنتظم في المحاكاة</h2>
<p>كثير من مولدات القيم العشوائية تبدأ بقيم تقريبية لتوزيع منتظم على الفترة من الصفر إلى الواحد، ثم تستخدم تحويلات لإنتاج توزيعات أخرى. وعلى الحاسوب تكون العشوائية شبه عشوائية ودقتها محدودة، ولذلك لا يطابق التنفيذ الرقمي المتغير المستمر المثالي حرفيًا.</p>

<h2>الفرق بين المنتظم المنفصل والمستمر</h2>
<div class="table-wrap"><table><thead><tr><th>المقارنة</th><th>المنتظم المستمر</th><th>المنتظم المنفصل</th></tr></thead><tbody>
<tr><td>مجال القيم</td><td>فترة من الأعداد الحقيقية</td><td>مجموعة من النتائج المنفصلة</td></tr>
<tr><td>احتمال نقطة محددة</td><td>صفر</td><td>موجب عندما تكون النتيجة ضمن المجال الممكن</td></tr>
<tr><td>الاحتمالات</td><td>تكامل الكثافة على فترة</td><td>مجموع احتمالات النتائج</td></tr>
</tbody></table></div>
<p>مثلًا، حجر النرد العادل مثال منفصل يحوي ست نتائج ذات احتمالات متساوية؛ وليس متغيرًا مستمرًا ذا كثافة ثابتة.</p>

<h2>لماذا التوزيع المنتظم مهم؟</h2>
<p>هو أبسط نموذج مستمر للتعرف على مفاهيم المجال والكثافة والتكامل والاحتمال والمساحة. ويؤسس للتمييز بين التوزيعات المستمرة والمنفصلة.</p>

<h2>حدود النموذج</h2>
<p>لا تكفي معرفة الحدين الأدنى والأعلى للاستنتاج أن التوزيع منتظم. ينبغي وجود سبب منطقي أو بيانات تدعم فرضية الكثافة الثابتة. إذا كانت الفترات غير متساوية الاحتمال أو كانت هناك تركزات واضحة، فقد تحتاج نموذجًا مختلفًا مثل <a href="/ar/probability/distributions/beta-distribution/">توزيع بيتا</a> عند متغير محصور بين صفر وواحد.</p>

<h2>ماذا بعد؟</h2>
<p>يمكن متابعة دراسة <a href="/ar/probability/distributions/beta-distribution/">توزيع بيتا</a> لمعرفة كيف يمكن أن تتغير هيئة الكثافة داخل مجال محدود، أو الانتقال إلى <a href="/ar/probability/distributions/exponential-distribution/">التوزيع الأسي</a> لفهم أزمنة الانتظار غير السالبة.</p>

<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>الكثافة ثابتة على <span dir="ltr">[a,b]</span> وارتفاعها <span dir="ltr">1/(b−a)</span>.</li>
<li>احتمال الفترة الفرعية يساوي طولها مقسومًا على طول المجال الكلي.</li>
<li>المتوسط <span dir="ltr">(a+b)/2</span>، والتباين <span dir="ltr">(b−a)²/12</span>.</li>
<li>احتمال النقطة المفردة يساوي صفرًا، رغم أن للكثافة ارتفاعًا موجبًا داخل المجال.</li>
<li>لا تخلط بين التوزيع المنتظم المستمر والمنفصل.</li></ul></div>

<div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/distributions/beta-distribution/">← توزيع بيتا</a>
<a class="btn" href="/probability/distributions/uniform-distribution/" lang="en" dir="ltr">English — Uniform Distribution →</a></div>
</div></section>
<style>
.esa-uniform-equation{box-sizing:border-box;max-width:100%;min-width:0;overflow-x:auto;direction:ltr}
.esa-uniform-equation mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}
.esa-uniform-equation:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
#esa-uniform-area-explorer [dir="ltr"]{unicode-bidi:isolate}
</style>
