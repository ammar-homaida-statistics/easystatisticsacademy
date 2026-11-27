---
layout: default
title: عرض فترة الثقة ودقتها — ما الذي يتحكم فيهما؟
description: "شرح عربي للعوامل التي تتحكم في عرض فترة الثقة: مستوى الثقة، وحجم العيّنة (قاعدة 1/√n)، والتباين، وتصميم الدراسة، مع مختبر تفاعلي لتخطيط حجم العيّنة والفرق بين الدقة والصحة."
permalink: /ar/inference/confidence-intervals/width-and-precision-what-controls/
lang: ar
sidebar: false
math: true
learning_resource: true
translation_pair: width-and-precision-what-controls
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاستدلال</span><span class="badge">فترات الثقة</span><span class="badge">الدقة</span></div>
<h1>عرض فترة الثقة ودقتها — ما الذي يتحكم فيهما؟</h1>
{% include lab-noscript.html %}
<p class="lead">قد تقدّر دراستان المعلمة نفسها لكنهما تعطيان فترتي ثقة مختلفتين جدًا.</p>
<p class="lead">وفهم ما يتحكم في عرض الفترة ضروري، لأن عرض الفترة يعكس الدقة الإحصائية.</p>
<p><a href="/inference/confidence-intervals/width-and-precision-what-controls/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/">درس ذو صلة: مخطط فترة الثقة</a></p>
</div></section>
<section><div class="content-narrow">

<h2>1. لماذا يهم عرض الفترة؟</h2>
<p>لا تقتصر فترات الثقة على تقدير المعالم؛ فعرضها يخبرنا بمدى دقة تقدير المعلمة.</p>
<div class="concept-box"><strong>الفكرة الرئيسة:</strong><p>الفترات الضيقة تدل على دقة أكبر، والفترات العريضة تدل على عدم يقين أكبر.</p></div>

<h2>2. الدقة مقابل الصحة</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">المفهوم</th><th scope="col">المعنى</th></tr></thead>
<tbody>
<tr><td>الصحة (Accuracy)</td><td>القرب من القيمة الحقيقية</td></tr>
<tr><td>الدقة (Precision)</td><td>مقدار عدم اليقين</td></tr>
</tbody></table></div>
<p>يعكس عرض فترة الثقة الدقة أساسًا، لا الصحة.</p>

<h2>3. تذكير بمخطط الفترة</h2>
<p>معظم فترات الثقة المتماثلة على الصورة:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="مخطط الفترة">\[\text{estimate}\pm(\text{critical value})(\text{standard error})\]</div>
<p>لذلك يتحدد عرض الفترة بالقيمة الحرجة والخطأ المعياري.</p>

<h2>4. صيغة العرض</h2>
<p>لأن الفترة تمتد بالمقدار نفسه في الاتجاهين، فإن عرضها الكلي:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="صيغة عرض الفترة">\[\text{interval width}=2(\text{critical value})(\text{standard error})\]</div>
<p>وأي عامل يغيّر القيمة الحرجة أو الخطأ المعياري يغيّر عرض الفترة.</p>

<h2>5. العامل الأول: مستوى الثقة</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">مستوى الثقة</th><th scope="col">z* التقريبية</th></tr></thead>
<tbody dir="ltr">
<tr><td>90%</td><td>1.645</td></tr>
<tr><td>95%</td><td>1.960</td></tr>
<tr><td>99%</td><td>2.576</td></tr>
</tbody></table></div>
<p>مع ازدياد مستوى الثقة تزداد القيمة الحرجة، فتصبح الفترة أعرض.</p>
<div class="concept-box"><strong>الموازنة:</strong><p>مزيد من الثقة يتطلب التضحية بشيء من الدقة؛ فعند حجم عيّنة ثابت لا يمكن عمومًا الحصول على ثقة أعلى وفترة أضيق معًا.</p></div>

<h2>6. العامل الثاني: حجم العيّنة</h2>
<p>حجم العيّنة هو غالبًا أهم عامل عملي؛ فالعيّنات الأكبر تقلّل الأخطاء المعيارية، والأخطاء المعيارية الأصغر تعطي فترات أضيق. ولمقدِّرات كثيرة:</p>
<div dir="ltr">\[\operatorname{SE}\propto\frac{1}{\sqrt n}.\]</div>

<h2>7. سوء فهم شائع</h2>
<p>مضاعفة حجم العيّنة لا تنصّف عرض الفترة؛ فبسبب الجذر التربيعي يجب زيادة حجم العيّنة نحو <strong>أربعة أضعاف</strong> لتنصيف الخطأ المعياري، أما مضاعفته فتقلّل العرض بنسبة \(1-1/\sqrt2\approx29\%\) فقط.</p>

<section class="concept-box" id="esa-precision-lab" data-locale="ar" aria-labelledby="esa-pr-heading">
<h2 id="esa-pr-heading">مختبر تفاعلي: دقة فترة الثقة وتخطيط حجم العيّنة</h2>
<p>استكشف <strong>فترة الثقة الطبيعية ثنائية الطرف لمتوسط مجتمع مع σ معلوم</strong>. هامش الخطأ يساوي <span dir="ltr">z × σ/√n</span>، والعرض الكلي ضعف الهامش. ولا يستخدم نموذج التخطيط هذا انحرافًا معياريًا مقدَّرًا من العيّنة.</p>
<div class="esa-pr-grid">
<div><label for="esa-pr-n">حجم العيّنة n (عدد صحيح موجب)</label><input type="number" id="esa-pr-n" min="1" max="1000000000" step="1" value="100" dir="ltr"></div>
<div><label for="esa-pr-sigma">الانحراف المعياري المعلوم للمجتمع σ</label><input type="number" id="esa-pr-sigma" min="0" step="any" value="20" dir="ltr"></div>
<div><label for="esa-pr-level">مستوى الثقة ثنائي الطرف</label><select id="esa-pr-level">
<option value="90">90%</option><option value="95" selected>95%</option><option value="99">99%</option>
</select></div>
<div><label for="esa-pr-target">أقصى هامش خطأ مرغوب (بوحدات البيانات نفسها)</label><input type="number" id="esa-pr-target" min="0" step="any" value="3" dir="ltr"></div>
</div>
<button type="button" id="esa-pr-reset" class="btn btn-outline">استعادة المثال المحلول</button>
<p id="esa-pr-error" role="alert" aria-live="assertive" hidden></p>
<section id="esa-pr-results" aria-label="نتائج دقة فترة الثقة" aria-live="polite">
<div class="table-wrap"><table><caption>نتائج تخطيط فترة الثقة (ست منازل عشرية)</caption><tbody>
<tr><th scope="row">القيمة الحرجة الطبيعية z</th><td id="esa-pr-critical" dir="ltr">—</td></tr>
<tr><th scope="row">الخطأ المعياري σ/√n</th><td id="esa-pr-stderr" dir="ltr">—</td></tr>
<tr><th scope="row">هامش الخطأ ±</th><td id="esa-pr-margin" dir="ltr">—</td></tr>
<tr><th scope="row">العرض الكلي للفترة</th><td id="esa-pr-width" dir="ltr">—</td></tr>
<tr><th scope="row">أصغر حجم عيّنة صحيح يحقق الهامش المستهدف</th><td id="esa-pr-needed" dir="ltr">—</td></tr>
<tr><th scope="row">الهامش عند 4n</th><td id="esa-pr-margin4" dir="ltr">—</td></tr>
<tr><th scope="row">العرض عند 4n</th><td id="esa-pr-width4" dir="ltr">—</td></tr>
</tbody></table></div>
<svg id="esa-pr-chart" viewBox="0 0 530 210" role="img" aria-label="عرض الفترة عند حجم العيّنة المختار وعند أربعة أضعافه" style="display:block;width:100%;height:auto;max-width:100%;direction:ltr"></svg>
<p id="esa-pr-explain"></p>
</section>
<p class="muted-mini">صيغة التخطيط: <span dir="ltr">n ≥ (zσ/E)²</span>، ونأخذ أصغر عدد صحيح يحقق الهامش المستهدف E؛ ففي المثال <span dir="ltr">(1.96 × 20 / 3)² ≈ 170.7</span>، فيلزم 171 مشاهدة. الثقة الأعلى وσ الأكبر يوسّعان الفترة، وزيادة n تضيّقها بمعدل الجذر التربيعي. والضيق لا يعني تلقائيًا الصحة أو انعدام التحيز؛ فالارتباط والعنقودية وتحيز الاختيار وجهالة σ تتطلب تصميمًا أو نموذج استدلال مختلفًا. وهذا تمرين لتخطيط الدقة، لا فترة ثقة محسوبة لبيانات مرصودة.</p>
</section>
<style>
#esa-precision-lab,#esa-precision-lab *{box-sizing:border-box}
#esa-precision-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-precision-lab .esa-pr-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:12px 0}
#esa-precision-lab label{display:block;font-weight:650;margin-bottom:5px}
#esa-precision-lab :is(input,select){width:100%;min-width:0;font:inherit;padding:10px;border:1px solid #777;border-radius:6px}
#esa-precision-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-precision-lab [hidden]{display:none!important}
#esa-precision-lab :is(input,select,button):focus-visible{outline:2px solid #0f766e;outline-offset:3px}
@media(max-width:640px){#esa-precision-lab .esa-pr-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/ci-precision-explorer.js"></script>

<h2>8. مثال على أثر حجم العيّنة</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">حجم العيّنة</th><th scope="col">الخطأ المعياري النسبي</th></tr></thead>
<tbody dir="ltr">
<tr><td>100</td><td>1.00</td></tr>
<tr><td>400</td><td>0.50</td></tr>
<tr><td>900</td><td>0.33</td></tr>
</tbody></table></div>
<p>العيّنات الأكبر تحسّن الدقة، لكن بعوائد متناقصة.</p>

<h2>9. العامل الثالث: التباين</h2>
<p>البيانات الأكثر تباينًا تعطي أخطاء معيارية أكبر، فتصبح الفترات أعرض؛ فالتباين الأكبر يعني يقينًا أقل بشأن المعلمة. وفي تقدير المتوسط:</p>
<div dir="ltr">\[\operatorname{SE}(\bar X)=\frac{\sigma}{\sqrt n},\]</div>
<p>فكلما كبر \(\sigma\) زاد عدم اليقين مباشرة.</p>

<h2>10. مثال: تقدير النسبة</h2>
<p>في تقدير النسب:</p>
<div dir="ltr">\[\widehat{\operatorname{SE}}(\hat p)=\sqrt{\frac{\hat p(1-\hat p)}{n}}.\]</div>
<p>ويعتمد التباين هنا على \(\hat p(1-\hat p)\)، وأكبر قيمة لـ \(p(1-p)\) تكون عند \(p=0.5\)؛ لذلك تعطي النسب القريبة من 50% غالبًا أعرض الفترات (انظر <a href="/ar/inference/confidence-intervals/ci-for-proportion/">فترة الثقة للنسبة</a>).</p>

<h2>11. العامل الرابع: تصميم الدراسة</h2>
<p>قد تؤثر التصاميم المختلفة في الدقة تأثيرًا كبيرًا؛ فالتصاميم الزوجية مثلًا تقلّل التباين غالبًا، وقد تعطي دراسات «قبل وبعد» فترات أضيق من دراسات المجموعات المستقلة، لأن كل مشارك يكون ضابطًا لنفسه.</p>

<h2>12. مثلث الدقة</h2>
<p>يتحكم في عرض الفترة أساسًا: مستوى الثقة، وحجم العيّنة، والتباين. وتتكرر هذه العوامل الثلاثة في الاستدلال الإحصائي كله.</p>

<h2>13. ما الذي يتحكم فيه الباحث؟</h2>
<p>قبل جمع البيانات يتحكم الباحث غالبًا مباشرة في حجم العيّنة، وتصميم الدراسة، ومستوى الثقة المرغوب، وهذه الخيارات تؤثر في دقة التقديرات المستقبلية.</p>

<h2>14. هامش الخطأ والعرض</h2>
<p>تذكر التقارير الإخبارية كثيرًا عبارة «هامش الخطأ ±3 نقاط مئوية»، وهو ببساطة نصف عرض الفترة؛ فهوامش الخطأ الأصغر تقابل تقديرات أدق.</p>

<h2>15. لماذا تندر الفترات الضيقة جدًا؟</h2>
<p>الدقة التامة مستحيلة لأن عدم يقين المعاينة لا يزول كليًا، والفترات الضيقة جدًا تتطلب عادةً عيّنات كبيرة جدًا، وتباينًا منخفضًا، ومستويات ثقة معتدلة.</p>

<h2>16. تفسير العرض تفسيرًا صحيحًا</h2>
<p>الفترة الضيقة تدل على أن المعلمة قُدّرت بدقة، لكنها لا تعني بالضرورة أن التقدير صحيح؛ فالتحيز وسوء المعاينة قد يعطيان نتائج مضللة رغم ضيق الفترة.</p>

<h2>17. الصورة الأشمل</h2>
<p>تنقل فترات الثقة التقديرات وعدم اليقين معًا، وعرضها من أهم المعلومات التي تقدّمها. وفهم ما يتحكم فيه يساعد على تصميم الدراسات وتفسير النتائج بفاعلية أكبر.</p>
<div class="concept-box"><strong>الرسالة الأساسية:</strong><p>يتحكم في عرض فترة الثقة أساسًا مستوى الثقة وحجم العيّنة والتباين. الفترات الضيقة تدل على دقة أكبر، والعريضة تدل على عدم يقين أكبر.</p></div>

<h2>18. ماذا بعد؟</h2>
<p>تُفهم فترات الثقة كثيرًا فهمًا خاطئًا، حتى من باحثين متمرسين. ويتناول الدرس التالي أشيع أخطاء تفسير فترات الثقة وكيف نفسّرها تفسيرًا صحيحًا.</p>

<div class="summary-box">
<h2>خلاصة الدرس</h2>
<ul class="bullets">
<li>يقيس عرض الفترة الدقة الإحصائية.</li>
<li>الدقة والصحة مفهومان مختلفان.</li>
<li>مستويات الثقة الأعلى تعطي فترات أعرض.</li>
<li>العيّنات الأكبر تعطي فترات أضيق.</li>
<li>التباين الأكبر يعطي فترات أعرض.</li>
<li>تتناقص الأخطاء المعيارية غالبًا بمعدل \(1/\sqrt n\).</li>
<li>قد يؤثر تصميم الدراسة في دقة الفترة.</li>
<li>الفترة الضيقة تعني تقديرًا أدق، لا بالضرورة أصح.</li>
</ul>
</div>

<div class="lesson-nav">
<a class="btn btn-outline" href="/inference/confidence-intervals/ci-for-paired-mean-difference/" hreflang="en" lang="en" dir="ltr">← Previous: CI for Paired Mean Difference (English)</a>
<a class="btn" href="/inference/confidence-intervals/common-mistakes-and-interpretation/" hreflang="en" lang="en" dir="ltr">Next: Common Mistakes and Interpretation (English) →</a>
</div>
</div></section>
