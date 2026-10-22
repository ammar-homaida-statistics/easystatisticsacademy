---
layout: default
title: التوزيع السالب ذو الحدين
description: شرح عربي شامل للتوزيع السالب ذي الحدين لعدد المحاولات حتى النجاح المحدد، مع الافتراضات ودالة الكتلة الاحتمالية والمتوسط والتباين ومختبر تفاعلي.
permalink: /ar/probability/distributions/negative-binomial-distribution/
lang: ar
sidebar: false
translation_pair: negative-binomial-distribution
math: true
---

<section class="hero hero-section"><div class="hero-card">
  <div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">التوزيعات المنفصلة</span><span class="badge">الانتظار حتى نجاحات متعددة</span></div>
  <h1>التوزيع السالب ذو الحدين (Negative Binomial)</h1>
  <p><a href="/probability/distributions/negative-binomial-distribution/" lang="en" dir="ltr">English — Negative Binomial Distribution</a></p>
  <p class="lead">ينمذج التوزيع الهندسي عدد المحاولات حتى أول نجاح، أما التوزيع السالب ذو الحدين فيعمِّم ذلك إلى عدد المحاولات اللازمة لتحقيق عدد محدد من النجاحات.</p>
  <div class="hero-actions">
    <a class="btn btn-outline" href="/ar/probability/distributions/geometric-distribution/">← الدرس السابق: التوزيع الهندسي</a>
    <a class="btn" href="/ar/probability/distributions/poisson-distribution/">الدرس التالي: توزيع بواسون ←</a>
  </div>
</div></section>

<section class="section"><div class="content-narrow">
<h2>ما التوزيع السالب ذو الحدين؟</h2>
<p>هو توزيع احتمالي <strong>منفصل</strong> يصف عدد تجارب برنولي المستقلة المطلوبة حتى وقوع عدد محدد مسبقًا من النجاحات. يظل احتمال النجاح نفسه في كل تجربة.</p>
<div class="concept-box"><strong>التعريف واصطلاح العد:</strong>
<p>يرمز المتغير العشوائي <span dir="ltr">X</span> إلى <strong>إجمالي عدد المحاولات بما فيها المحاولة الناجحة الأخيرة</strong> حتى تحقيق النجاح رقم <span dir="ltr">r</span>، حيث <span dir="ltr">r</span> عدد صحيح موجب، و<span dir="ltr">0&lt;p≤1</span>. ويوجد اصطلاح آخر يحصي الإخفاقات السابقة للنجاح رقم <span dir="ltr">r</span>؛ وهو متغير مختلف يساوي <span dir="ltr">X−r</span>. لن نخلط بين الاصطلاحين.</p></div>

<h2>السؤال الأساسي</h2>
<p>بدل السؤال: «كم محاولة حتى أول نجاح؟» نسأل:</p>
<div class="example-box"><ul class="bullets">
<li>كم رمية لقطعة نقدية حتى ظهور الوجه للمرة الخامسة؟</li>
<li>كم عميلًا حتى إتمام ثالث عملية شراء؟</li>
<li>كم فحصًا حتى اكتشاف العيب العاشر؟</li>
</ul></div>
<p>تتعلق هذه الأسئلة بعدد المحاولات اللازم لبلوغ عدد <strong>ثابت من النجاحات</strong>، لا بعدد النجاحات ضمن عدد ثابت من التجارب.</p>

<h2>شروط نموذج السالب ذي الحدين</h2>
<ul class="bullets">
<li>المحاولات مستقلة بعضها عن بعض.</li>
<li>لكل محاولة نتيجتان محتملتان: نجاح أو إخفاق.</li>
<li>احتمال النجاح <span dir="ltr">p</span> ثابت في كل محاولة.</li>
<li>يستمر تكرار المحاولات حتى تحقيق <span dir="ltr">r</span> نجاحات.</li>
</ul>
<p>إذا تغيّر احتمال النجاح مع الزمن، أو وُجد اعتماد بين التجارب، فلن تكون هذه الصيغة البسيطة ملائمة بالضرورة.</p>

<h2>الترميز والمعلمتان</h2>
<div class="esa-negbin-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="الترميز والمعلمات">\[
X\sim\operatorname{NegBin}(r,p),\qquad r\in\{1,2,\ldots\},\quad 0<p\le1.
\]</div>
<p><span dir="ltr">r</span> عدد النجاحات المطلوبة، و<span dir="ltr">p</span> احتمال النجاح لكل تجربة مستقلة.</p>

<h2>القيم الممكنة</h2>
<p>نحتاج إلى <span dir="ltr">r</span> محاولات على الأقل لتحقيق <span dir="ltr">r</span> نجاحات:</p>
<div class="esa-negbin-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="مجموعة القيم الممكنة">\[
X\in\{r,r+1,r+2,\ldots\}.
\]</div>
<p>عند <span dir="ltr">p=1</span> تحدث النجاحات جميعًا دون إخفاق، فيصبح <span dir="ltr">X=r</span> باحتمال يساوي واحدًا.</p>

<h2>دالة الكتلة الاحتمالية</h2>
<p>احتمال وقوع النجاح رقم <span dir="ltr">r</span> في المحاولة <span dir="ltr">k</span> بالضبط هو:</p>
<div class="esa-negbin-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="دالة الكتلة الاحتمالية">\[
P(X=k)=\binom{k-1}{r-1}p^r(1-p)^{k-r},
\qquad k=r,r+1,\ldots.
\]</div>
<p>تكون المحاولة الأخيرة ناجحة بالضرورة، وبين المحاولات <span dir="ltr">k−1</span> السابقة يجب أن تقع <span dir="ltr">r−1</span> نجاحات و<span dir="ltr">k−r</span> إخفاقات. يمثّل العامل التوافقي عدد الترتيبات الممكنة لهذه النتائج السابقة.</p>

<h2>فهم الصيغة خطوة بخطوة</h2>
<div class="example-box"><ol>
<li>نجاح في المحاولة رقم <span dir="ltr">k</span> باحتمال <span dir="ltr">p</span>.</li>
<li>بالضبط <span dir="ltr">r−1</span> نجاحات ضمن المحاولات السابقة.</li>
<li>عدد الترتيبات السابقة الممكنة <span dir="ltr">C(k−1,r−1)</span>.</li>
<li>من استقلال التجارب نحصل على حاصل ضرب احتمالات النجاحات والإخفاقات ثم نجمع الترتيبات المتكافئة.</li>
</ol></div>
<p>لا يجوز اعتبار <span dir="ltr">r</span> متغيرًا عشريًا في هذا النموذج؛ إنه عدد صحيح للنجاحات المطلوبة.</p>

<h2>العلاقة مع التوزيع الهندسي</h2>
<p>التوزيع الهندسي هو الحالة الخاصة <span dir="ltr">r=1</span>. بالتعويض تصبح دالة الكتلة الاحتمالية:</p>
<div class="esa-negbin-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="اختزال السالب ذي الحدين إلى الهندسي">\[
P(X=k)=\binom{k-1}{0}p(1-p)^{k-1}
=p(1-p)^{k-1}.
\]</div>
<p>وهذا هو احتمال أن يحدث <strong>أول نجاح</strong> في المحاولة <span dir="ltr">k</span>.</p>

<h2>مثال: انتظار ثلاثة أوجه لقطعة نقدية</h2>
<p>نرمي قطعة نقدية عادلة باستقلال حتى يظهر الوجه للمرة الثالثة. عندئذٍ <span dir="ltr">r=3</span> و<span dir="ltr">p=0.5</span>. احتمال أن يظهر الوجه الثالث في الرمية الخامسة هو:</p>
<div class="esa-negbin-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="مثال محلول لاحتمال النجاح الثالث في الخامسة">\[
P(X=5)=\binom{4}{2}(0.5)^3(0.5)^2
=6(0.5)^5=0.1875.
\]</div>
<p>إذن الاحتمال يساوي <strong>18.75%</strong>. يلزم هنا نجاحان بالضبط في الرميات الأربع الأولى ثم نجاح ثالث في الخامسة.</p>

<h2>المتوسط أو القيمة المتوقعة</h2>
<div class="esa-negbin-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="متوسط عدد المحاولات">\[
E[X]=\frac{r}{p}.
\]</div>
<p>يزداد متوسط عدد المحاولات عندما يزداد عدد النجاحات المطلوبة أو تقل فرصة النجاح الفردية.</p>

<h2>مثال على المتوسط</h2>
<p>إذا كان المطلوب <span dir="ltr">r=5</span> نجاحات، واحتمال النجاح في المحاولة <span dir="ltr">p=0.25</span>، فإن:</p>
<div class="esa-negbin-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="المتوسط عند خمس نجاحات واحتمال ربع">\[
E[X]=\frac{5}{0.25}=20.
\]</div>
<p>هذا متوسط نظري على عدد كبير من عمليات التكرار، ولا يعني أن النجاح الخامس سيحدث حتمًا في المحاولة العشرين.</p>

<h2>التباين</h2>
<div class="esa-negbin-equation esa-math-ltr" dir="ltr" role="region" tabindex="0" aria-label="تباين عدد المحاولات">\[
\operatorname{Var}(X)=\frac{r(1-p)}{p^2}.
\]</div>
<p>يزداد تشتت عدد المحاولات عند انخفاض <span dir="ltr">p</span>، ويتلاشى التباين عند <span dir="ltr">p=1</span> لأن جميع المحاولات تكون ناجحة.</p>

<section class="concept-box esa-negbin-lab" id="esa-negbin-wait-explorer" role="group" aria-labelledby="esa-negbin-lab-heading">
<h2 id="esa-negbin-lab-heading">مختبر تفاعلي: الانتظار حتى النجاح رقم r</h2>
<p>اختر عدد النجاحات المطلوبة <span dir="ltr">r</span>، واحتمال النجاح <span dir="ltr">p</span>، والمحاولة <span dir="ltr">k</span> التي يتحقق عندها النجاح الأخير. يشمل <span dir="ltr">X</span> <strong>المحاولة الناجحة الأخيرة</strong>. يحدّث المختبر دالة الكتلة الاحتمالية والاحتمال التراكمي والذيلي والمتوسط والتباين.</p>
<div class="esa-negbin-fields">
<div><label for="esa-negbin-r">عدد النجاحات المطلوبة r: <output for="esa-negbin-r" id="esa-negbin-r-value" dir="ltr">3</output></label>
<input type="range" dir="ltr" min="1" max="6" step="1" value="3" id="esa-negbin-r"></div>
<div><label for="esa-negbin-p">احتمال النجاح p: <output for="esa-negbin-p" id="esa-negbin-p-value" dir="ltr">0.50</output></label>
<input type="range" dir="ltr" min="0.05" max="1" step="0.05" value="0.5" id="esa-negbin-p"></div>
<div><label for="esa-negbin-k">رقم المحاولة عند النجاح الأخير k: <output for="esa-negbin-k" id="esa-negbin-k-value" dir="ltr">5</output></label>
<input type="range" dir="ltr" min="3" max="30" step="1" value="5" id="esa-negbin-k"></div>
</div>
<h3>احتمالات النجاح الأخير في اثنتي عشرة محاولة ممكنة متتالية</h3>
<div dir="ltr"><svg id="esa-negbin-chart" viewBox="0 0 360 176" role="img"
           aria-label="احتمال وقوع النجاح الثالث في المحاولات المتعاقبة مع احتمال نجاح 0.50؛ المحاولة المختارة 5"
           width="360" height="176">
        <line x1="30" y1="135" x2="347" y2="135" stroke="currentColor" stroke-width="1.4"/>
        <line x1="30" y1="135" x2="30" y2="16" stroke="currentColor" stroke-width="1.4"/>
        <text x="8" y="15" fill="currentColor" font-size="10">PMF</text>
        <g id="esa-negbin-bars"></g>
        <text x="344" y="159" fill="currentColor" font-size="10">k</text>
      </svg></div>
<p class="muted-mini">تعرض الأعمدة أول اثنتي عشرة قيمة ممكنة للمحاولة الأخيرة، ابتداءً من <span dir="ltr">r</span>. الارتفاعات على مقياس احتمالي مطلق من صفر إلى واحد. لا تُحذف احتمالات المحاولات الأبعد من الحسابات التراكمية والذيول.</p>
<div class="esa-negbin-results" role="status" aria-live="polite" aria-atomic="true">
<p><strong>الاحتمال الدقيق:</strong> <span dir="ltr">P(X=k)=<output id="esa-negbin-pmf">0.187500</output></span>.</p>
<p><strong>الاحتمال حتى المحاولة k:</strong> <span dir="ltr">P(X≤k)=<output id="esa-negbin-cdf">0.500000</output></span>.</p>
<p><strong>الاحتمال بعد المحاولة k:</strong> <span dir="ltr">P(X&gt;k)=<output id="esa-negbin-tail">0.500000</output></span>.</p>
<p><strong>المتوسط:</strong> <span dir="ltr">E[X]=r/p=<output id="esa-negbin-mean">6.0000</output></span> محاولة؛
<strong>التباين:</strong> <span dir="ltr">r(1−p)/p²=<output id="esa-negbin-variance">6.0000</output></span> محاولة مربعة.</p>
<p id="esa-negbin-special">عندما r = 1 يصبح التوزيع السالب ذو الحدين هو التوزيع الهندسي لعدد المحاولات حتى أول نجاح.</p>
</div>
<div class="esa-negbin-presets">
<button type="button" class="btn btn-outline" id="esa-negbin-reset">استعادة المثال الافتراضي</button>
<button type="button" class="btn btn-outline" id="esa-negbin-geometric">الحالة الهندسية: r = 1</button>
</div>
<p class="muted-mini">يحسب المختبر الاحتمالات على كامل التوزيع وليس على الأعمدة المعروضة فقط. إذا أصبح <span dir="ltr">r&gt;k</span> يرفع الحد الأدنى للمتغير <span dir="ltr">k</span> تلقائيًا إلى <span dir="ltr">r</span>. وعند <span dir="ltr">p=1</span> يتركز الاحتمال كله عند <span dir="ltr">X=r</span>.</p>
</section>
    <style>
      .esa-negbin-equation{max-width:100%;min-width:0;overflow-x:auto}
      .esa-negbin-equation mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}
      .esa-negbin-equation:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
      #esa-negbin-wait-explorer {box-sizing:border-box;width:100%;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-negbin-wait-explorer .esa-negbin-fields {
        display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,185px),1fr));
        gap:14px;margin:16px 0
      }
      #esa-negbin-wait-explorer .esa-negbin-fields>div {min-width:0}
      #esa-negbin-wait-explorer label {display:block;margin-bottom:8px}
      #esa-negbin-wait-explorer input[type="range"] {
        display:block;box-sizing:border-box;width:100%;max-width:100%;
        min-width:0;margin:0;padding:0
      }
      #esa-negbin-wait-explorer h3 {font-size:1.05em;margin:16px 0 10px}
      #esa-negbin-wait-explorer svg {display:block;width:100%;height:auto;max-width:520px;margin:0 auto;overflow:visible}
      #esa-negbin-wait-explorer .esa-negbin-results p {margin:11px 0}
      #esa-negbin-wait-explorer .esa-negbin-presets {display:flex;flex-wrap:wrap;gap:8px}
    </style>
<script src="{{ '/js/negative-binomial-waiting-explorer.js' | relative_url }}" defer></script>

<h2>مقارنة الهندسي والسالب ذي الحدين</h2>
<div class="table-wrap"><table><thead><tr><th>التوزيع</th><th>ما الذي ينمذجه؟</th></tr></thead><tbody>
<tr><td>الهندسي</td><td>عدد المحاولات حتى أول نجاح فقط.</td></tr>
<tr><td>السالب ذو الحدين</td><td>عدد المحاولات حتى تحقيق <span dir="ltr">r</span> نجاحات.</td></tr>
</tbody></table></div>
<p>الاصطلاح في هذا الدرس يعدّ <strong>كل المحاولات</strong> حتى النجاح الأخير؛ فلا ينبغي خلطه بتوزيع عدد الإخفاقات السابق له.</p>

<h2>لماذا يُسمى «السالب ذو الحدين»؟</h2>
<p>تأتي التسمية من متسلسلة ذات حدين في الجبر تتضمن أسسًا سالبة. لا تعني كلمة «السالب» هنا أن الاحتمالات سالبة، أو أن عدد المحاولات يمكن أن يكون سالبًا.</p>

<h2>تطبيقات عملية</h2>
<ul class="bullets">
<li>عدد المكالمات المطلوبة حتى إتمام عدة عمليات بيع.</li>
<li>عدد المرضى المفحوصين حتى اكتشاف عدد محدد من الحالات الإيجابية، إن كانت افتراضات النموذج ملائمة.</li>
<li>عدد محاولات إرسال حزم البيانات حتى تحقيق عدة عمليات إرسال ناجحة.</li>
<li>عدد الفحوص الصناعية حتى رصد مجموعة من العيوب.</li>
<li>عدد المحاولات الرياضية قبل تحقيق عدد معين من النتائج الناجحة.</li>
</ul>

<h2>العلاقة بنماذج العد</h2>
<p>يحصي التوزيع ذو الحدين عدد النجاحات خلال <strong>عدد ثابت من التجارب</strong>، في حين يثبت نموذج السالب ذي الحدين عدد النجاحات المطلوب ويترك <strong>عدد التجارب</strong> عشوائيًا.</p>
<div class="example-box"><p>ذو الحدين: محاولات ثابتة ← عدّ النجاحات. السالب ذو الحدين: نجاحات مطلوبة وثابتة ← عدّ المحاولات.</p></div>
<p>قد يُستخدم اسم «السالب ذو الحدين» أيضًا لعائلات أخرى من نماذج بيانات العد تختلف في تفسير معلماتها؛ الصيغ هنا تخص اصطلاح عدد التجارب حتى النجاح رقم <span dir="ltr">r</span>.</p>

<h2>شكل التوزيع</h2>
<p>يملك توزيع عدد المحاولات حدًا أدنى يساوي <span dir="ltr">r</span> وذيلًا يمتد يمينًا عند <span dir="ltr">0&lt;p&lt;1</span>. يصبح انتظار محاولات كثيرة أكثر احتمالًا نسبيًا عندما تقل فرصة النجاح في كل تجربة. عند <span dir="ltr">p=1</span> لا يبقى ذيل عشوائي لأن العدد ثابت ويساوي <span dir="ltr">r</span>.</p>

<h2>حدود هذا النموذج</h2>
<p>تنشأ توزيعات برنولي، وذي الحدين، والهندسي، والسالب ذي الحدين من تجارب نجاح/إخفاق متكررة. لا تنطبق هذه البنية تلقائيًا على أعداد الأحداث الواقعة خلال الزمن أو المكان، مثل الرسائل الواردة أو الحوادث أو زيارات المواقع؛ إذ قد تكون نماذج بواسون أو نماذج عد أخرى أكثر ملاءمة بعد فحص افتراضاتها.</p>

<h2>الدرس التالي: توزيع بواسون</h2>
<p>يدرس توزيع بواسون عدد الأحداث خلال مجال زمني أو مكاني محدد ضمن افتراضات معينة. وهو متاح بالعربية في الدرس التالي.</p>

<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>ينمذج السالب ذو الحدين إجمالي عدد المحاولات حتى <span dir="ltr">r</span> نجاحات.</li>
<li>يفترض استقلال المحاولات واحتمال نجاح ثابتًا.</li>
<li>التوزيع الهندسي هو الحالة الخاصة <span dir="ltr">r=1</span>.</li>
<li>المتوسط يساوي <span dir="ltr">r/p</span> والتباين <span dir="ltr">r(1−p)/p²</span>.</li>
<li>القيم الممكنة تبدأ من <span dir="ltr">r</span>، وتصبح النتيجة حتمية عند <span dir="ltr">p=1</span>.</li>
<li>تساعد أداة الانتظار التفاعلية على فهم الاحتمالات الدقيقة والتراكمية والذيول.</li>
</ul></div>
<div class="lesson-nav">
<a class="btn btn-outline" href="/ar/probability/distributions/geometric-distribution/">← التوزيع الهندسي</a>
<a class="btn" href="/ar/probability/distributions/poisson-distribution/">توزيع بواسون ←</a>
</div>
</div></section>