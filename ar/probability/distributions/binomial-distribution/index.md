---
layout: default
title: التوزيع ذي الحدين
description: درس متكامل عن التوزيع ذي الحدين وشروطه واحتمالاته الدقيقة والتراكمية والمتوسط والتباين، مع حاسبة تفاعلية باللغة العربية.
permalink: /ar/probability/distributions/binomial-distribution/
lang: ar
sidebar: false
translation_pair: binomial-distribution
math: true
---

<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">التوزيعات الاحتمالية</span><span class="badge">المتغيرات المتقطعة</span></div>
<h1>التوزيع ذو الحدين (Binomial Distribution)</h1>
<p><a href="/probability/distributions/binomial-distribution/" lang="en" dir="ltr">English — Binomial Distribution</a></p>
<p class="lead">يصف توزيع برنولي تجربة واحدة لها نتيجتان: نجاح أو إخفاق. أما التوزيع ذو الحدين فيصف <strong>عدد النجاحات</strong> خلال عدد ثابت من تجارب برنولي المستقلة التي تشترك في احتمال النجاح نفسه.</p>
<div class="hero-actions"><a class="btn" href="/probability/distributions/bernoulli-distribution/" lang="en" dir="ltr">Previous (English): Bernoulli Distribution</a><a class="btn btn-outline" href="/probability/distributions/geometric-distribution/" lang="en" dir="ltr">Next (English): Geometric Distribution</a></div>
</div></section>

<section class="section"><div class="content-narrow">
<h2>ما التوزيع ذو الحدين؟</h2>
<p>التوزيع ذو الحدين نموذج احتمالي لعدد النجاحات في <strong>n</strong> تجربة مستقلة ومتماثلة التوزيع، لكل منها نتيجتان واحتمال ثابت للنجاح <strong>p</strong>. وإذا اختلف احتمال النجاح بين التجارب المستقلة، يصبح النموذج المناسب عادةً <span dir="ltr">Poisson-binomial</span>، أما الاعتماد بين التجارب فقد يستلزم نموذجاً آخر.</p>
<div class="concept-box"><strong>التعريف:</strong><p>المتغير العشوائي ذو الحدين هو مجموع مؤشرات برنولي المستقلة، حيث يأخذ كل مؤشر القيمة 1 عند النجاح و0 عند الإخفاق، ويكون احتمال النجاح مشتركاً ويساوي <span dir="ltr">0 ≤ p ≤ 1</span>.</p></div>

<h2>الشروط الأربعة</h2>
<p>يصح استخدام هذا النموذج عند تحقق الشروط التالية جميعاً، وليس لمجرد تكرار تجربة ما:</p>
<div class="table-wrap"><table><thead><tr><th>الشرط</th><th>المعنى</th></tr></thead><tbody>
<tr><td>عدد التجارب ثابت</td><td>يُحدد عدد التجارب مسبقاً.</td></tr>
<tr><td>التجارب مستقلة</td><td>لا يغيّر ناتج تجربة احتمال نتيجة تجربة أخرى.</td></tr>
<tr><td>نتيجتان لكل تجربة</td><td>نجاح أو إخفاق بحسب التعريف المعتمد.</td></tr>
<tr><td>احتمال نجاح ثابت</td><td>قيمة <span dir="ltr">p</span> لا تتبدل بين التجارب.</td></tr>
</tbody></table></div>

<h2>مثال: رمي قطعة نقدية</h2>
<p>نرمي قطعة نقدية عادلة عشر مرات، ونعرف <span dir="ltr">X</span> بأنه عدد مرات ظهور الوجه. عند افتراض استقلال الرميات، لدينا عشر تجارب ثنائية، واحتمال ظهور الوجه في كل رمية هو 0.5؛ لذلك يُنمذج <span dir="ltr">X</span> بتوزيع ذي حدين ذي المعلمتين <span dir="ltr">n = 10, p = 0.5</span>.</p>
<h2>الترميز والقيم الممكنة</h2>
<div dir="ltr" class="esa-math-ltr">\[
X\sim\operatorname{Binomial}(n,p),\qquad
X\in\{0,1,\ldots,n\}.
\]</div>
<p>ترمز <span dir="ltr">n</span> إلى عدد التجارب و<span dir="ltr">p</span> إلى احتمال النجاح. وتشمل القيم الحسابية الممكنة جميع الأعداد الصحيحة من صفر إلى <span dir="ltr">n</span>، لكن عند <span dir="ltr">p = 0</span> أو <span dir="ltr">p = 1</span> لا يحمل احتمالاً موجباً سوى العدد عند أحد الطرفين.</p>

<h2>دالة الكتلة الاحتمالية</h2>
<p>احتمال الحصول على <span dir="ltr">k</span> نجاحات <strong>بالضبط</strong> يُعطى بالصيغة:</p>
<div class="esa-math-ltr" dir="ltr">\[
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k},\quad k=0,\ldots,n.
\]</div>
<p>هذه دالة الكتلة الاحتمالية للتوزيع ذي الحدين. للمعلمة <span dir="ltr">0 &lt; p &lt; 1</span> تتألف الصيغة من عدد الترتيبات الممكنة للنجاحات، واحتمال سلسلة النجاحات، واحتمال سلسلة الإخفاقات. تُحسب حالتا الطرف <span dir="ltr">p=0,1</span> مباشرةً بوصفهما توزيعَين حتميَّين.</p>
<h2>فهم حدود الصيغة</h2>
<div class="table-wrap"><table><thead><tr><th>العامل</th><th>تفسيره</th></tr></thead><tbody>
<tr><td><span dir="ltr">C(n,k)</span></td><td>عدد طرق وضع <span dir="ltr">k</span> نجاحات بين <span dir="ltr">n</span> تجارب.</td></tr>
<tr><td><span dir="ltr">p^k</span></td><td>احتمال النجاح في التجارب المحددة البالغ عددها <span dir="ltr">k</span>.</td></tr>
<tr><td><span dir="ltr">(1-p)^(n-k)</span></td><td>احتمال الإخفاق في التجارب المتبقية.</td></tr>
</tbody></table></div>
<h2>معامل التوافيق</h2>
<div class="esa-math-ltr" dir="ltr">\[
\binom{n}{k}=\frac{n!}{k!(n-k)!}.
\]</div>
<p>نقرأ الرمز «اختيار <span dir="ltr">k</span> من <span dir="ltr">n</span>»، وهو يحصي المواضع المختلفة التي يمكن أن تشغلها النجاحات، دون اعتبار ترتيب النجاحات والإخفاقات داخل كل مجموعة.</p>
<h2>مثال محسوب: نجاحان من ثلاث رميات</h2>
<p>عند رمي قطعة نقدية عادلة ثلاث مرات، يكون احتمال الحصول على وجهين بالضبط:</p>
<div class="esa-math-ltr" dir="ltr">\[
P(X=2)=\binom{3}{2}(0.5)^2(0.5)^{3-2}
=3(0.5)^3=0.375.
\]</div>
<p>إذن الاحتمال هو <strong>37.5%</strong>، ولا يعني ذلك أن نجاحين سيحدثان حتماً في كل ثلاث رميات.</p>

<h2>المتوسط أو القيمة المتوقعة</h2>
<div class="esa-math-ltr" dir="ltr">\[
\operatorname{E}(X)=np.
\]</div>
<p>القيمة المتوقعة تساوي عدد التجارب مضروباً في احتمال النجاح. مثلاً عند <span dir="ltr">n=100</span> و<span dir="ltr">p=0.2</span> تكون القيمة المتوقعة <span dir="ltr">100(0.2)=20</span> نجاحاً، وهي متوسط نظري وليست نتيجة مضمونة لتجربة بعينها.</p>
<h2>التباين والانحراف المعياري</h2>
<div class="esa-math-ltr" dir="ltr">\[
\operatorname{Var}(X)=np(1-p),\qquad
\operatorname{SD}(X)=\sqrt{np(1-p)}.
\]</div>
<p>لفهم سبب هذه الصيغة، نكتب عدد النجاحات بوصفه مجموع مؤشرات برنولي مستقلة <span dir="ltr">I₁,…,Iₙ</span>. تباين كل مؤشر يساوي <span dir="ltr">p(1−p)</span>؛ وبالاستقلال تتجمع التباينات:</p>
<div class="esa-math-ltr" dir="ltr">\[
\operatorname{Var}\left(\sum_{i=1}^{n}I_i\right)
=\sum_{i=1}^{n}\operatorname{Var}(I_i)=np(1-p).
\]</div>

<section class="concept-box" id="esa-binomial-calculator" aria-labelledby="esa-binomial-calculator-heading" style="max-width:100%;min-width:0;overflow-wrap:anywhere">
<h2 id="esa-binomial-calculator-heading">حاسبة تفاعلية لاحتمالات التوزيع ذي الحدين</h2>
<p>أدخل عدد التجارب المستقلة <span dir="ltr">n</span> واحتمال النجاح المشترك <span dir="ltr">p</span> وعدد النجاحات <span dir="ltr">k</span> لحساب الاحتمال الدقيق والاحتمالين التراكميين <strong>مع شمول k</strong>. تدعم الحاسبة من 1 إلى 1000 تجربة.</p>
<form id="esa-binomial-calculator-form" novalidate>
<div class="esa-binomial-input-grid">
<div><label for="esa-binomial-n">عدد التجارب (n)</label><input id="esa-binomial-n" type="number" inputmode="numeric" min="1" max="1000" step="1" value="3" dir="ltr" required></div>
<div><label for="esa-binomial-p">احتمال النجاح (p)</label><input id="esa-binomial-p" type="number" inputmode="decimal" min="0" max="1" step="any" value="0.5" dir="ltr" required></div>
<div><label for="esa-binomial-k">عدد النجاحات (k)</label><input id="esa-binomial-k" type="number" inputmode="numeric" min="0" max="1000" step="1" value="2" dir="ltr" required></div>
</div>
<p class="esa-binomial-math-note"><strong>القانون:</strong> <span dir="ltr">P(X=k)=C(n,k) × p<sup>k</sup> × (1−p)<sup>n−k</sup></span>. يشمل الاحتمالان التراكميان العدد <span dir="ltr">k</span> نفسه.</p>
<div class="example-box" id="esa-binomial-result-region" role="status" aria-live="polite">
<div class="esa-binomial-result-grid">
<p>احتمال العدد بالضبط <span dir="ltr">P(X=k)</span>: <strong><output id="esa-binomial-exact" dir="ltr">0.375</output></strong></p>
<p>الاحتمال التراكمي <span dir="ltr">P(X≤k)</span>: <strong><output id="esa-binomial-cdf" dir="ltr">0.875</output></strong></p>
<p>الذيل الأعلى <span dir="ltr">P(X≥k)</span>: <strong><output id="esa-binomial-upper" dir="ltr">0.5</output></strong></p>
<p>المتوسط <span dir="ltr">(np)</span>: <strong><output id="esa-binomial-mean" dir="ltr">1.5</output></strong></p>
<p>التباين <span dir="ltr">(np(1−p))</span>: <strong><output id="esa-binomial-variance" dir="ltr">0.75</output></strong></p>
</div>
<p id="esa-binomial-explanation">احتمال الحصول على نجاحين بالضبط هو 0.375.</p></div>
<p id="esa-binomial-error" role="alert" hidden></p>
</form>
<p class="muted-mini"><strong>الافتراضات والقيود:</strong> يجب أن يكون عدد التجارب صحيحاً وموجباً، وأن تكون التجارب ثنائية ومستقلة ولها احتمال نجاح ثابت. عند <span dir="ltr">n=1</span> نحصل على توزيع برنولي. عند <span dir="ltr">p=0</span> يكون عدد النجاحات صفراً حتماً، وعند <span dir="ltr">p=1</span> يساوي <span dir="ltr">n</span> حتماً. تستخدم الحاسبة الجمع في المجال اللوغاريتمي لتقليل فقدان الدقة؛ وقد تُعرض الاحتمالات الأصغر من حدود تمثيل الفاصلة العائمة على أنها صفر. استقلال التجارب مع اختلاف احتمالات نجاحها أو اعتماد بعضها على بعض يحتاج إلى نموذج مختلف.</p>
</section>
<style>
      #esa-binomial-calculator{max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-binomial-calculator .esa-binomial-input-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:16px 0}
      #esa-binomial-calculator .esa-binomial-input-grid>div{min-width:0}
      #esa-binomial-calculator label{display:block;font-weight:650;margin:0 0 6px}
      #esa-binomial-calculator input[type="number"]{display:block;width:100%;max-width:100%;min-width:0;box-sizing:border-box;background:var(--surface);color:var(--text);border:1px solid var(--border-strong);border-radius:8px;padding:10px;font:inherit}
      #esa-binomial-calculator input:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
      #esa-binomial-calculator .esa-binomial-result-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 16px}
      #esa-binomial-calculator .esa-binomial-result-grid>*{min-width:0;margin:4px 0}
      #esa-binomial-calculator .esa-binomial-math-note{overflow-wrap:anywhere}
      #esa-binomial-calculator #esa-binomial-error{color:#b42318;font-weight:650}
      @media(max-width:620px){
        #esa-binomial-calculator .esa-binomial-input-grid{grid-template-columns:minmax(0,1fr)}
        #esa-binomial-calculator .esa-binomial-result-grid{grid-template-columns:minmax(0,1fr)}
      }
    </style>
<script src="{{ '/js/binomial-probability-calculator.js' | relative_url }}" defer></script>

<h2>شكل التوزيع</h2>
<p>يتحدد شكل التوزيع بدرجة كبيرة بواسطة <span dir="ltr">p</span>. عند <span dir="ltr">p=0.5</span> يكون متماثلاً حول <span dir="ltr">n/2</span>. عند <span dir="ltr">0&lt;p&lt;0.5</span> يميل إلى الالتواء الموجب (ذيل نحو اليمين)، وعند <span dir="ltr">0.5&lt;p&lt;1</span> يميل إلى الالتواء السالب (ذيل نحو اليسار). وقد يصبح التقريب الطبيعي مناسباً إذا كان كل من <span dir="ltr">np</span> و<span dir="ltr">n(1−p)</span> كبيراً بما يكفي؛ زيادة عدد التجارب وحدها لا تضمن تقريباً جيداً عندما يكون الاحتمال قريباً جداً من صفر أو واحد.</p>

<h2>تطبيقات واقعية</h2>
<ul class="bullets"><li>عدد العملاء الذين يشترون منتجاً.</li><li>عدد القطع المعيبة في مجموعة.</li><li>عدد المكالمات البيعية الناجحة.</li><li>عدد المرضى المستجيبين للعلاج.</li><li>عدد الناخبين المؤيدين لمرشح.</li></ul>
<p>هذه الأمثلة لا تكون ذات حدين تلقائياً؛ يجب أولاً التأكد من ثبات عدد التجارب وثنائية النتيجة والاستقلال واحتمال النجاح المشترك. مثلاً، سحب وحدات من مجموعة محدودة دون إرجاع قد ينتهك الاستقلال.</p>
<h2>مقارنة برنولي بالتوزيع ذي الحدين</h2>
<div class="table-wrap"><table><thead><tr><th>التوزيع</th><th>ما الذي يمثله؟</th></tr></thead><tbody>
<tr><td>برنولي</td><td>نتيجة تجربة ثنائية واحدة.</td></tr>
<tr><td>ذو الحدين</td><td>عدد النجاحات في عدة تجارب برنولي مستقلة ومتماثلة الاحتمال.</td></tr>
</tbody></table></div>
<p>عند <span dir="ltr">n=1</span> يصبح التوزيع ذو الحدين مطابقاً لبرنولي. أما مجموع تجارب برنولي المستقلة ذات الاحتمالات المختلفة فلا يتبع عادةً توزيعاً ذا حدين بمعلمة مشتركة.</p>
<h2>ما الذي لا يصفه النموذج؟</h2>
<p>يجيب التوزيع ذو الحدين عن السؤال «كم نجاحاً يحدث في <span dir="ltr">n</span> تجربة؟»، لكنه لا يصف مباشرةً عدد التجارب اللازمة حتى <strong>النجاح الأول</strong>. هذا الأخير موضوع التوزيع الهندسي.</p>
<h2>الدرس التالي</h2>
<p>سندرس في التوزيع الهندسي نماذج زمن الانتظار حتى أول نجاح، وهي فئة مهمة من التوزيعات الاحتمالية.</p>

<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>يحصي التوزيع ذو الحدين عدد النجاحات في تجارب برنولي مستقلة واحتمالها مشترك.</li>
<li>نرمز له بـ <span dir="ltr">Bin(n,p)</span>، وتستخدم احتمالاته الدقيقة معامل التوافيق.</li>
<li>المتوسط هو <span dir="ltr">np</span> والتباين <span dir="ltr">np(1−p)</span>.</li>
<li>توفر الحاسبة احتمال العدد المحدد والتراكمين الشاملين له؛ الاحتمال لا يعني اليقين.</li>
<li>لا يصح اختيار النموذج دون فحص شروطه الأربعة.</li>
</ul></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/probability/distributions/bernoulli-distribution/" lang="en" dir="ltr">← Bernoulli (English)</a><a class="btn" href="/probability/distributions/geometric-distribution/" lang="en" dir="ltr">Geometric (English) →</a></div>
</div></section>
