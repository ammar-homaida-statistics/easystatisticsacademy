---
layout: default
title: التوزيع الهندسي
description: درس عربي عن التوزيع الهندسي للانتظار حتى أول نجاح، مع دالة الكتلة الاحتمالية، الاحتمالات التراكمية، المتوسط، التباين، خاصية انعدام الذاكرة ومختبر تفاعلي.
permalink: /ar/probability/distributions/geometric-distribution/
lang: ar
sidebar: false
translation_pair: geometric-distribution
math: true
---

<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">التوزيعات المنفصلة</span><span class="badge">الانتظار حتى أول نجاح</span></div>
<h1>التوزيع الهندسي (Geometric Distribution)</h1>
<p><a href="/probability/distributions/geometric-distribution/" lang="en" dir="ltr">English — Geometric Distribution</a></p>
<p class="lead">كيف نحسب عدد المحاولات المطلوبة للحصول على أول نجاح، عندما تكون التجارب مستقلة ويتكرر احتمال النجاح نفسه في كل تجربة؟</p>
</div></section>

<section class="section"><div class="content-narrow">
<h2>ما التوزيع الهندسي؟</h2>
<p>يصف التوزيع الهندسي عدد المحاولات اللازمة للحصول على <strong>أول نجاح</strong> في سلسلة من تجارب برنولي المستقلة التي يكون احتمال النجاح فيها ثابتًا.</p>
<div class="concept-box"><strong>التعريف:</strong><p>يُحسب عدد المحاولات <strong>مع تضمين المحاولة الناجحة نفسها</strong>. أي أن المتغير لا يقتصر على عدد الإخفاقات السابقة للنجاح. يوجد تعريف اصطلاحي بديل يبدأ من الصفر ويحصي الإخفاقات السابقة فقط؛ نستخدم هنا اصطلاح عدد المحاولات حتى أول نجاح.</p></div>

<h2>السؤال الأساسي</h2>
<p>بخلاف التوزيع ذي الحدين الذي يحصي عدد النجاحات ضمن عدد ثابت من التجارب، يدرس التوزيع الهندسي <strong>مدة الانتظار المقاسة بعدد المحاولات</strong> حتى أول نجاح.</p>
<div class="example-box"><ul class="bullets">
<li>كم رمية لقطعة نقدية نحتاج حتى ظهور أول وجه؟</li>
<li>كم عميلًا نحتاج حتى حدوث أول عملية شراء؟</li>
<li>كم مكالمة حتى إتمام أول عملية بيع؟</li>
<li>كم فحصًا حتى اكتشاف أول عيب؟</li>
</ul></div>

<h2>شروط استخدام التوزيع الهندسي</h2>
<p>يلائم النموذج الهندسي الموقف عندما:</p>
<ul class="bullets">
<li>تكون المحاولات <strong>مستقلة</strong>.</li>
<li>تكون لكل محاولة نتيجتان: نجاح وإخفاق.</li>
<li>يظل احتمال النجاح <strong>ثابتًا</strong> من محاولة إلى أخرى.</li>
<li>نرغب في تحديد المحاولة التي يقع عندها <strong>أول نجاح</strong>.</li>
</ul>
<p>تشبه هذه الشروط شروط التوزيع ذي الحدين، لكن السؤال الاحتمالي مختلف.</p>

<h2>الترميز</h2>
<p>نرمز للمتغير العشوائي الذي يمثل عدد المحاولات حتى أول نجاح بالرمز <span dir="ltr">X</span>:</p>
<div class="esa-geom-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="ترميز التوزيع الهندسي">\[
X\sim\operatorname{Geom}(p),\qquad 0<p\le 1.
\]</div>
<p>يمثل <span dir="ltr">p</span> احتمال النجاح الثابت في كل تجربة مستقلة، ونتطلب أن يكون أكبر من الصفر حتى يتحقق النجاح في عدد منتهٍ من المحاولات باحتمال يساوي واحدًا.</p>

<h2>القيم الممكنة</h2>
<p>يمكن أن يحدث النجاح الأول في المحاولة الأولى، أو الثانية، أو الثالثة، وهكذا:</p>
<div class="esa-geom-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="القيم الممكنة للمتغير الهندسي">\[
X\in\{1,2,3,\ldots\}.
\]</div>
<p>لا تبدأ قيم هذا الاصطلاح من الصفر؛ إذ يجب إجراء محاولة واحدة على الأقل للحصول على نجاح.</p>

<h2>دالة الكتلة الاحتمالية</h2>
<p>احتمال وقوع أول نجاح في المحاولة رقم <span dir="ltr">k</span> يساوي:</p>
<div class="esa-geom-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="دالة الكتلة الاحتمالية للتوزيع الهندسي">\[
P(X=k)=(1-p)^{k-1}p,\qquad k=1,2,\ldots.
\]</div>
<p>تعني الصيغة حدوث <span dir="ltr">k−1</span> إخفاقًا متتابعًا، ثم نجاح واحد في المحاولة رقم <span dir="ltr">k</span>. وبسبب الاستقلال نضرب احتمالات هذه النتائج.</p>

<h2>فهم الصيغة</h2>
<div class="example-box"><ol>
<li>المحاولة الأولى: إخفاق باحتمال <span dir="ltr">1−p</span>.</li>
<li>المحاولة الثانية: إخفاق باحتمال <span dir="ltr">1−p</span>.</li>
<li>وهكذا حتى المحاولة <span dir="ltr">k−1</span>: إخفاق.</li>
<li>المحاولة رقم <span dir="ltr">k</span>: نجاح باحتمال <span dir="ltr">p</span>.</li>
</ol></div>
<p>ضرب هذه الاحتمالات يعطي الصيغة الهندسية. عند <span dir="ltr">p=1</span> يحدث النجاح الأول في المحاولة الأولى يقينًا، ولا يمكن أن يبدأ الانتظار بمحاولة فاشلة.</p>

<h2>مثال: رمي قطعة نقدية</h2>
<p>إذا رمينا قطعة نقدية عادلة مرارًا، فإن احتمال ظهور الوجه في كل رمية هو <span dir="ltr">p=0.5</span>. ما احتمال ظهور أول وجه في الرمية الثالثة؟</p>
<div class="esa-geom-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="احتمال أول وجه في الرمية الثالثة">\[
P(X=3)=\left(1-\frac12\right)^2\frac12=\frac18=0.125.
\]</div>
<p>هذا يعني إخفاقين (ظهور الكتابة مثلًا)، ثم ظهور الوجه في الرمية الثالثة. الاحتمال يساوي <strong>12.5%</strong>.</p>

<section class="concept-box esa-geometric-lab" id="esa-geometric-wait-explorer" role="group" aria-labelledby="esa-geometric-lab-heading">
<h2 id="esa-geometric-lab-heading">مختبر تفاعلي: وقت الانتظار الهندسي</h2>
<p>عدّل احتمال النجاح <span dir="ltr">p</span> ورقم المحاولة <span dir="ltr">k</span>. يحصي المتغير جميع المحاولات حتى <strong>أول نجاح مع تضمين المحاولة الناجحة</strong>، ولذلك تبدأ قيمة <span dir="ltr">k</span> من 1. تفترض النتائج استقلال تجارب برنولي وثبات احتمال نجاحها.</p>
<div class="esa-geometric-fields">
<div><label for="esa-geom-p"><strong>احتمال النجاح p: <output id="esa-geom-p-value" for="esa-geom-p" dir="ltr">0.25</output></strong></label><input id="esa-geom-p" type="range" min="0.05" max="1" step="0.05" value="0.25"></div>
<div><label for="esa-geom-k"><strong>رقم المحاولة k: <output id="esa-geom-k-value" for="esa-geom-k" dir="ltr">3</output></strong></label><input id="esa-geom-k" type="range" min="1" max="20" step="1" value="3"></div>
</div>
<h3>احتمالات أول نجاح في المحاولات الاثنتي عشرة الأولى</h3>
      <svg id="esa-geom-pmf-plot" viewBox="0 0 360 175" width="360" height="175"
           role="img" aria-label="الاحتمالات الهندسية للمحاولات الاثنتي عشرة الأولى">
        <line x1="31" y1="136" x2="343" y2="136" stroke="currentColor" stroke-width="1.4"/>
        <line x1="31" y1="136" x2="31" y2="17" stroke="currentColor" stroke-width="1.4"/>
        <text x="8" y="15" font-size="10" fill="currentColor">P(X=j)</text>
        <text x="343" y="158" font-size="10" fill="currentColor">المحاولة</text>
        <g id="esa-geom-bars">
          <rect data-trial="1" x="40" width="17" y="108.5" height="27.5" fill="#64748b"/>
          <rect data-trial="2" x="64" width="17" y="115.375" height="20.625" fill="#64748b"/>
          <rect data-trial="3" x="88" width="17" y="120.53125" height="15.46875" fill="#0d9488"/>
          <rect data-trial="4" x="112" width="17" y="124.3984375" height="11.6015625" fill="#64748b"/>
          <rect data-trial="5" x="136" width="17" y="127.298828125" height="8.701171875" fill="#64748b"/>
          <rect data-trial="6" x="160" width="17" y="129.474121094" height="6.525878906" fill="#64748b"/>
          <rect data-trial="7" x="184" width="17" y="131.10559082" height="4.89440918" fill="#64748b"/>
          <rect data-trial="8" x="208" width="17" y="132.32919312" height="3.67080688" fill="#64748b"/>
          <rect data-trial="9" x="232" width="17" y="133.24689484" height="2.75310516" fill="#64748b"/>
          <rect data-trial="10" x="256" width="17" y="133.93517113" height="2.06482887" fill="#64748b"/>
          <rect data-trial="11" x="280" width="17" y="134.45137835" height="1.54862165" fill="#64748b"/>
          <rect data-trial="12" x="304" width="17" y="134.83853376" height="1.16146624" fill="#64748b"/>
        </g>
        <text x="48" y="151" text-anchor="middle" font-size="10" fill="currentColor">1</text>
        <text x="95" y="151" text-anchor="middle" font-size="10" fill="currentColor">3</text>
        <text x="191" y="151" text-anchor="middle" font-size="10" fill="currentColor">7</text>
        <text x="311" y="151" text-anchor="middle" font-size="10" fill="currentColor">12</text>
      </svg>
<p class="muted-mini">ارتفاع كل عمود يساوي الاحتمال الحقيقي على محور رأسي من الصفر إلى الواحد. تظهر المحاولة المحددة بلون مميز إذا كان رقمها لا يزيد على 12. لا تُعرَض احتمالات المحاولات اللاحقة كأعمدة، لكنها تدخل في الحسابات الاحتمالية كاملة.</p>
<div class="esa-geometric-results" role="status" aria-live="polite" aria-atomic="true">
<p><strong>النجاح لأول مرة في المحاولة k:</strong> <span dir="ltr">P(X=k)=(1−p)<sup>k−1</sup>p = <output id="esa-geom-pmf">0.140625</output></span>.</p>
<p><strong>النجاح في المحاولة k أو قبلها:</strong> <span dir="ltr">P(X≤k)=1−(1−p)<sup>k</sup> = <output id="esa-geom-cdf">0.578125</output></span>.</p>
<p><strong>النجاح بعد المحاولة k:</strong> <span dir="ltr">P(X&gt;k)=(1−p)<sup>k</sup> = <output id="esa-geom-tail">0.421875</output></span>.</p>
<p>العدد المتوقع للمحاولات <span dir="ltr">E[X]=1/p = <output id="esa-geom-mean">4.0000</output></span>؛ والتباين <span dir="ltr">Var(X)=(1−p)/p² = <output id="esa-geom-variance">12.0000</output></span>.</p>
<p><strong>خاصية انعدام الذاكرة:</strong> بعد عشرة إخفاقات، احتمال النجاح في المحاولة التالية <output id="esa-geom-memoryless-next" dir="ltr">0.2500</output>، واحتمال انتظار أكثر من ثلاث محاولات أخرى <output id="esa-geom-memoryless-tail" dir="ltr">0.421875</output>، بشرط أن تكون سلسلة الإخفاقات السابقة ممكنة.</p>
<p id="esa-geom-memoryless-note" hidden>عندما <span dir="ltr">p=1</span> يكون وقوع عشرة إخفاقات سابقة حدثًا مستحيلًا (احتماله صفر). لذلك لا يُعرّف الاحتمال الشرطي لتجربة تالية <em>بشرط هذا التاريخ المستحيل</em>؛ لكن احتمال النجاح غير المشروط في المحاولة الأولى يساوي واحدًا.</p>
</div>
<button type="button" id="esa-geom-reset" class="btn btn-outline">استعادة المثال الافتراضي</button>
<p class="muted-mini">تُحسب الاحتمالات باستخدام التوزيع الهندسي كاملًا، دون قطع التوزيع أو إعادة تطبيع الاحتمالات بسبب عرض اثني عشر عمودًا فقط.</p>
</section>
    <style>
      #esa-geometric-wait-explorer {box-sizing:border-box;width:100%;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-geometric-wait-explorer .esa-geometric-fields {
        display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));
        gap:12px;margin:15px 0
      }
      #esa-geometric-wait-explorer .esa-geometric-fields>div {min-width:0}
      #esa-geometric-wait-explorer label {display:block;margin-bottom:8px}
      #esa-geometric-wait-explorer input[type="range"] {
        display:block;box-sizing:border-box;width:100%;max-width:100%;min-width:0;
        margin:0;padding:0
      }
      #esa-geometric-wait-explorer svg {
        display:block;width:100%;max-width:520px;height:auto;margin:10px auto;
        overflow:visible
      }
      #esa-geometric-wait-explorer h3 {font-size:1.05em;margin:13px 0 9px}
      #esa-geometric-wait-explorer .esa-geometric-results p {margin:11px 0}
      #esa-geometric-wait-explorer [hidden] {display:none!important}
    </style>
<style>
.esa-geom-equation{max-width:100%;min-width:0;overflow-x:auto}
.esa-geom-equation mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}
.esa-geom-equation:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
#esa-geometric-wait-explorer output{font-variant-numeric:tabular-nums}
</style>
<script src="{{ '/js/geometric-waiting-time-explorer.js' | relative_url }}" defer></script>

<h2>المتوسط أو القيمة المتوقعة</h2>
<p>إذا كان احتمال النجاح في كل محاولة هو <span dir="ltr">p</span>، فإن العدد المتوقع للمحاولات اللازمة حتى أول نجاح يساوي:</p>
<div class="esa-geom-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="متوسط التوزيع الهندسي">\[
E[X]=\frac{1}{p}.
\]</div>
<p>كلما قل احتمال النجاح، زاد العدد المتوقع للمحاولات.</p>

<h2>مثال على المتوسط</h2>
<p>عندما يكون <span dir="ltr">p=0.25</span> فإن:</p>
<div class="esa-geom-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="مثال المتوسط">\[
E[X]=\frac{1}{0.25}=4.
\]</div>
<p>أي أن متوسط الانتظار النظري حتى أول نجاح يساوي أربع محاولات؛ وقد يحدث النجاح في المحاولة الأولى أو بعد أكثر من أربع محاولات في تجربة بعينها.</p>

<h2>التباين</h2>
<p>تباين العدد العشوائي للمحاولات حتى أول نجاح يساوي:</p>
<div class="esa-geom-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="تباين التوزيع الهندسي">\[
\operatorname{Var}(X)=\frac{1-p}{p^2}.
\]</div>
<p>يزداد التباين عندما تقل فرصة النجاح ضمن مجال القيم المسموح به.</p>

<h2>النجاحات النادرة تعني انتظارًا أطول</h2>
<ul class="bullets">
<li>عندما يتناقص <span dir="ltr">p</span> يزداد المتوسط <span dir="ltr">1/p</span>.</li>
<li>يزداد التباين أيضًا، ويصبح عدد المحاولات أكثر تشتتًا.</li>
<li>تقل احتمالات وقوع النجاح سريعًا وتزداد احتمالات فترات انتظار طويلة نسبيًا.</li>
</ul>

<h2>خاصية انعدام الذاكرة</h2>
<div class="concept-box"><strong>انعدام الذاكرة:</strong><p>إذا كانت التجارب مستقلة واحتمال النجاح فيها ثابتًا، فلا يغيّر عدد الإخفاقات السابقة احتمال النجاح في المحاولة التالية، ما دام حدث الإخفاقات السابقة ذا احتمال موجب.</p></div>
<div class="esa-geom-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="صيغة خاصية انعدام الذاكرة">\[
P(X>m+n\mid X>m)=P(X>n)=(1-p)^n,
\qquad 0<p<1.
\]</div>
<p>تُفهم الصيغة على أن الانتظار الإضافي بعد <span dir="ltr">m</span> إخفاقات له التوزيع نفسه، ولا يعتمد على عدد الإخفاقات السابقة. قُيّد احتمال النجاح بـ <span dir="ltr">p&lt;1</span> لأن الشرط <span dir="ltr">X&gt;m</span> قد يصبح مستحيلًا عند <span dir="ltr">p=1</span> و<span dir="ltr">m≥1</span>.</p>

<h2>ما معنى انعدام الذاكرة عمليًا؟</h2>
<p>بعد عشر رميات متتالية لقطعة نقدية عادلة دون ظهور الوجه، يظل احتمال ظهور الوجه في الرمية التالية <strong>0.5</strong>، وهو الاحتمال نفسه منذ البداية، بشرط استقلال الرميات.</p>
<div class="esa-geom-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="احتمال الوجه في الرمية التالية">\[
P(\text{وجه في الرمية التالية}\mid\text{10 إخفاقات})=\frac12.
\]</div>
<p>الإخفاقات السابقة لا تمنحنا دليلًا على أن النجاح «أصبح مستحقًا» في التجربة التالية.</p>

<h2>خطأ شائع: مغالطة المقامر</h2>
<div class="example-box"><p>«ظهرت الكتابة عشر مرات متتالية؛ إذن لا بد أن يظهر الوجه قريبًا».</p></div>
<p>هذه هي <strong>مغالطة المقامر</strong>. في التجارب المستقلة لا يتغير احتمال النجاح بسبب ما وقع في الماضي.</p>

<h2>التوزيع الهندسي مقابل التوزيع ذي الحدين</h2>
<div class="table-wrap"><table><thead><tr><th>التوزيع</th><th>السؤال</th></tr></thead><tbody>
<tr><td>ذو الحدين</td><td>كم نجاحًا يحدث ضمن عدد <strong>ثابت</strong> من المحاولات؟</td></tr>
<tr><td>الهندسي</td><td>كم محاولة نحتاج حتى وقوع <strong>أول نجاح</strong>؟</td></tr>
</tbody></table></div>
<p>يُشتق التوزيعان من تجارب برنولي المتكررة، لكن المتغير العشوائي والسؤال المقصود مختلفان.</p>

<h2>تطبيقات التوزيع الهندسي</h2>
<ul class="bullets">
<li>عدد العملاء حتى أول عملية شراء.</li>
<li>عدد فحوص المعدات حتى اكتشاف أول عطل.</li>
<li>عدد محاولات إرسال البيانات حتى أول إرسال ناجح.</li>
<li>عدد عمليات الفحص حتى اكتشاف الحالة المطلوبة لأول مرة.</li>
<li>عدد محاولات التواصل حتى أول استجابة.</li>
</ul>
<p>تتطلب ملاءمة النموذج التأكد من استقلال التجارب وثبات فرصة النجاح، وإلا فقد نحتاج إلى نموذج آخر.</p>

<h2>شكل التوزيع</h2>
<p>عندما <span dir="ltr">0&lt;p&lt;1</span> تتناقص كتلة الاحتمال هندسيًا بزيادة رقم المحاولة؛ لذا يظهر ذيل أيمن. أما عند <span dir="ltr">p=1</span> فيحدث النجاح في المحاولة الأولى يقينًا، ويكون التوزيع منحلاً في نقطة واحدة.</p>

<h2>حدود النموذج</h2>
<p>يركز التوزيع الهندسي على الانتظار حتى النجاح <strong>الأول فقط</strong>. إذا كان السؤال عن عدد المحاولات حتى النجاح الخامس أو عدد العملاء حتى ثالث عملية شراء، فنحتاج إلى تعميم.</p>

<h2>الدرس التالي</h2>
<p>يُعمِّم <strong>التوزيع السالب ذي الحدين</strong> هذا المنظور إلى الانتظار حتى تحقق عدد محدد من النجاحات. وهو الدرس التالي باللغة الإنجليزية.</p>

<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>يصف التوزيع الهندسي عدد المحاولات حتى أول نجاح، مع تضمين المحاولة الناجحة.</li>
<li>تحتاج التجارب إلى الاستقلال وثبات احتمال النجاح.</li>
<li>دالة الكتلة الاحتمالية هي <span dir="ltr">(1−p)<sup>k−1</sup>p</span>.</li>
<li>المتوسط <span dir="ltr">1/p</span>، والتباين <span dir="ltr">(1−p)/p²</span>.</li>
<li>التوزيع الهندسي يمتلك خاصية انعدام الذاكرة عندما يكون شرط الاحتمال موجبًا.</li>
<li>يمكن فهم الاحتمالات الدقيقة والتراكمية والذيول ومقارنة النتائج بواسطة المستكشف التفاعلي.</li>
</ul></div>
<div class="lesson-nav">
<a class="btn btn-outline" href="/probability/distributions/bernoulli-distribution/" lang="en" dir="ltr">← Bernoulli (English)</a>
<a class="btn" href="/probability/distributions/negative-binomial-distribution/" lang="en" dir="ltr">Negative Binomial (English) →</a>
</div>
</div></section>
