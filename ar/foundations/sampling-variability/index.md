---
layout: default
title: تباين المعاينة
description: لماذا تختلف نتائج العينات العشوائية وكيف يتغير الخطأ المعياري مع حجم العينة وطريقة السحب، مع مختبر تفاعلي دقيق.
permalink: /ar/foundations/sampling-variability/
sidebar: false
lang: ar
math: true
translation_pair: sampling-variability
---
<!-- ترجمة تعليمية متكاملة للدرس الإنجليزي، مع حسابات تفاعلية مشتركة. -->
<section class="hero hero-section">
<div class="hero-card">
  <div class="badge-row"><span class="badge">أساسيات الإحصاء</span><span class="badge">فكرة جوهرية</span><span class="badge">عدم اليقين</span></div>
  <h1>تباين المعاينة</h1>
  <p><a href="/foundations/sampling-variability/" lang="en" dir="ltr">English — Sampling Variability</a></p>
  <p class="lead">لماذا نحصل على متوسطات ونِسب مختلفة عند سحب عينات عشوائية جديدة من المجتمع نفسه؟
  فهم هذا الاختلاف هو الأساس الذي تقوم عليه الاستدلالات الإحصائية.</p>
  <div class="hero-actions"><a class="btn" href="#content">ابدأ الدرس</a><a class="btn btn-outline" href="/ar/">الدروس العربية</a></div>
</div>
</section>
<section class="section" id="content">
<div class="section-block">
  <h2>الفكرة الأساسية</h2>
  <p>إذا سحبنا عينات مختلفة من المجتمع الإحصائي نفسه، فقد نلاحظ نتائج مختلفة، حتى مع استعمال طريقة معاينة عشوائية صحيحة. يسمى هذا الاختلاف الطبيعي <strong>تباين المعاينة</strong>.</p>
  <p>ليس اختلاف النتائج بين العينات خطأً في ذاته، وإنما خاصية احتمالية لعملية المعاينة. لا نعرف قيمة معلمة المجتمع بالضرورة من عينة واحدة معرفة تامة، لذلك نستخدم الاحتمالات والخطأ المعياري لوصف مقدار عدم اليقين في التقدير.</p>
</div>
<div class="section-block">
  <h2>مثال بسيط</h2>
  <p>افترض أن متوسط طول الأفراد في مجتمع معين غير معروف. سحبنا ثلاث عينات عشوائية، فكانت متوسطاتها كما يلي:</p>
  <ul class="bullets"><li>العينة الأولى: <span dir="ltr">170</span></li><li>العينة الثانية: <span dir="ltr">168</span></li><li>العينة الثالثة: <span dir="ltr">172</span></li></ul>
  <p>هذه تقديرات مختلفة للمعلمة السكانية ذاتها، ولا يلزم أن يكون اختلافها ناجمًا عن خطأ قياس أو تحيز.</p>
</div>
<div class="section-block">
  <h2>لماذا يحدث تباين المعاينة؟</h2>
  <p>تضم كل عينة مجموعة مختلفة من الوحدات؛ فقد تحتوي عينة على قيم كبيرة نسبيًا، بينما تضم أخرى قيمًا أصغر. تؤثر هوية العناصر المختارة في الإحصاء المحسوب، مثل المتوسط أو النسبة.</p>
</div>
<div class="section-block">
  <h2>الاختلاف العشوائي لا يعني وقوع خطأ</h2>
  <p>قد يظهر تباين المعاينة حتى مع اختيار الوحدات عشوائيًا بصورة مثالية ومن دون تحيز منهجي. وهو أمر متوقع ما دامت العينات الجزئية الممكنة لا تعطي جميعها النتيجة نفسها.</p>
</div>
<div class="section-block">
  <h2>التباين العشوائي مقابل التحيز</h2>
  <ul class="bullets"><li><strong>تباين المعاينة:</strong> اختلاف الإحصاءات بين العينات بسبب الاختيار العشوائي.</li><li><strong>تحيز المعاينة:</strong> انحراف منهجي عن المجتمع المستهدف، قد ينتج عن طريقة اختيار لا تمثل المجتمع تمثيلًا مناسبًا.</li></ul>
  <p>غالبًا ما يقل التشتت العشوائي عند زيادة حجم العينة؛ لكن زيادة الحجم وحدها لا تعالج اختيار عينة غير ممثلة.</p>
</div>
<div class="section-block">
  <h2>التصور البياني</h2>
  <p>يمكن تصور المجتمع بوصفه توزيعًا كاملًا للقيم. تسجّل كل عينة جزءًا من هذا التوزيع، فتختلف ملخصاتها باختلاف الوحدات المختارة.</p>
  <img src="{{ '/foundations/images/sampling-variability.png' | relative_url }}" alt="رسم توضيحي لاختلاف العينات المسحوبة من المجتمع نفسه" style="margin-top:15px;">
</div>
<div class="section-block">
  <h2>أثر حجم العينة</h2>
  <p>في كثير من التصاميم الاحتمالية، تكون متوسطات العينات الصغيرة أكثر تشتتًا، في حين تتركز متوسطات العينات الأكبر بدرجة أكبر حول متوسط المجتمع.</p>
  <ul class="bullets"><li><strong>عينة صغيرة:</strong> عدم يقين أكبر عادةً وتقدير أقل استقرارًا.</li><li><strong>عينة كبيرة:</strong> خطأ معياري أصغر عادةً عند ثبات التصميم والظروف.</li></ul>
  <p>قد يختفي تباين المعاينة تمامًا عند إجراء <strong>حصر شامل</strong> من مجتمع محدود دون إرجاع؛ أما السحب مع الإرجاع فلا يساوي الحصر الشامل تلقائيًا.</p>
</div>
<div class="section-block">
  <h2>مثال عددي</h2>
  <p>يتكون مجتمع محدود من القيم <span dir="ltr">160, 165, 170, 175, 180</span>، ومتوسطه <span dir="ltr">170</span>.</p>
  <ul class="bullets"><li>العينة (أ): <span dir="ltr">160, 165</span> ومتوسطها <span dir="ltr">162.5</span>.</li><li>العينة (ب): <span dir="ltr">175, 180</span> ومتوسطها <span dir="ltr">177.5</span>.</li></ul>
  <p>العينتان من المجتمع نفسه، لكن المتوسطين يختلفان. سنستخدم هذه القيم نفسها في المختبر أدناه، حيث يبلغ تباين المجتمع (بالمقام <span dir="ltr">N</span>) <span dir="ltr">50</span>.</p>
</div>

<!-- نموذج محاكاة مشترك يضمن تطابق الحسابات مع النسخة الإنجليزية. -->
<div class="section-block" id="esa-sv-lab" style="min-width:0;overflow-wrap:anywhere">
<h2>مختبر تفاعلي لتباين المعاينة</h2>
<p>اسحب عينات متكررة من <strong>مجتمع محدود معروف وثابت</strong> قيمه
<span dir="ltr">160, 165, 170, 175, 180</span> وعدد أفراده <span dir="ltr">N = 5</span>.
ليست هذه إعادة معاينة بوتستراب من عينة سابقة؛ بل سحب عينات جديدة مباشرة من المجتمع.
السحوبات مستقلة بين التكرارات، ويمكنك تحديد السماح بتكرار العنصر داخل العينة الواحدة.</p>
<div style="display:flex;flex-wrap:wrap;align-items:end;gap:1rem">
  <label>حجم العينة (<span dir="ltr">n</span>)
    <select id="esa-sv-size"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option></select>
  </label>
  <label>طريقة المعاينة
    <select id="esa-sv-method"><option value="without" selected>دون إرجاع</option><option value="with">مع الإرجاع</option></select>
  </label>
  <label>عدد العينات المحاكاة
    <select id="esa-sv-reps"><option>100</option><option selected>500</option><option>2000</option></select>
  </label>
  <label>البذرة العشوائية
    <input id="esa-sv-seed" type="number" min="0" max="4294967295" step="1" value="2026" style="max-width:135px" dir="ltr">
  </label>
  <button class="btn" type="button" id="esa-sv-run">شغّل المحاكاة</button>
  <button class="btn btn-outline" type="button" id="esa-sv-reset">إعادة الضبط</button>
</div>
<p id="esa-sv-status" role="status" aria-live="polite"></p>
<dl style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,180px),1fr));gap:.45rem">
  <div><dt>متوسط المجتمع</dt><dd id="esa-sv-mu">—</dd></div>
  <div><dt>تباين المجتمع (المقام N)</dt><dd id="esa-sv-sigma2">—</dd></div>
  <div><dt>الخطأ المعياري النظري الدقيق لمتوسط العينة</dt><dd id="esa-sv-theory">—</dd></div>
  <div><dt>الخطأ المعياري المحاكى (المقام B−1)</dt><dd id="esa-sv-simulated">—</dd></div>
  <div><dt>متوسط المتوسطات المحاكاة</dt><dd id="esa-sv-average">—</dd></div>
  <div><dt>الفرق الناجم عن المحاكاة (المتوسط المحاكى − μ)</dt><dd id="esa-sv-bias">—</dd></div>
</dl>
<p>قيم العينة الأولى: <span id="esa-sv-preview" dir="ltr"></span></p>
<svg id="esa-sv-plot" role="img" aria-label="مدرج تكراري لمتوسطات العينات المسحوبة" viewBox="0 0 680 276" style="display:block;width:100%;max-width:680px"></svg>
<div class="concept-box">
<p><strong>المرجع النظري:</strong> يُعرَّف تباين المجتمع المحدود بالصيغة
\(\sigma_N^2=\sum_{i=1}^N(x_i-\mu)^2/N\).
عند السحب المستقل <strong>مع الإرجاع</strong>، يكون
\(\operatorname{SE}(\bar X)=\sqrt{\sigma_N^2/n}\).
أما عند المعاينة العشوائية البسيطة <strong>دون إرجاع</strong> فيكون
\(\operatorname{SE}(\bar X)=\sqrt{(\sigma_N^2/n)\,(N-n)/(N-1)}\).
يُطبّق تصحيح المجتمع المحدود على الحالة الثانية فقط.</p>
<p>يحدّد تصميم المعاينة الخطأ المعياري النظري الدقيق، بينما يقترب منه الانحراف المعياري المحاكى،
وقد يختلف بسبب محدودية عدد التكرارات. إذا كان <span dir="ltr">n=N</span> دون إرجاع
فإن كل عينة تتضمن المجتمع بالكامل ويكون الخطأ المعياري صفرًا.
أما السحب مع الإرجاع فلا يضمن ظهور جميع الأفراد حتى إن ساوى حجم العينة حجم المجتمع.</p>
<p>يقيس تباين المعاينة اختلاف النتائج عند سحب عينات جديدة من المجتمع؛
بينما تعيد بوتستراب سحب مشاهدات من عينة مرصودة لتقدير توزيع معاينة غير معلوم.
ولا تعالج أيٌّ من الطريقتين انحياز اختيار العينة.</p>
</div>
</div>
<script src="/js/sampling-variability-lab.js" defer></script>

<div class="section-block">
  <h2>جرّب بنفسك ببرامج التحليل</h2>
  <p>يمكن ملاحظة اختلاف النتائج عند تكرار السحب أو تحليل مجموعات فرعية مختارة بصورة احتمالية صحيحة.</p>
  <p><strong>SPSS:</strong> استخدم قائمة <span dir="ltr">Analyze → Descriptive Statistics → Explore</span> لتحليل عينات مختلفة ومقارنة المتوسطات، مع مراعاة كيفية اختيار العينات.</p>
  <p><strong>Excel:</strong> يمكنك استعمال الدالة <code dir="ltr">RANDBETWEEN(1,100)</code> لتوليد أعداد عشوائية توضيحية، ثم حساب متوسط عشر قيم في كل مرة وإعادة التجربة.</p>
  <p><strong>Python (اختياري):</strong></p>
  <pre dir="ltr"><code>import numpy as np

for _ in range(5):
    sample = np.random.randint(1, 101, 10)
    print(sample.mean())</code></pre>
  <p>هذه المحاكاة البرمجية مثال على سحب مستقل مع الإرجاع من القيم الصحيحة من 1 إلى 100، وليست محاكاة سحب دون إرجاع من مجتمع محدود.</p>
</div>
<div class="section-block">
  <h2>تجربة فكرية</h2>
  <p>تخيل سحب عينات مستقلة ومتكررة، حجم كل منها <span dir="ltr">50</span> فردًا، من المجتمع نفسه. إذا حسبنا متوسط كل عينة، فسنحصل على <strong>توزيع لمتوسطات العينات</strong>، لا على رقم واحد دائمًا. هذا هو مفهوم توزيع المعاينة.</p>
</div>
<div class="section-block">
  <h2>لماذا يهم هذا الموضوع؟</h2>
  <ul class="bullets"><li>يبين سبب عدم يقين النتائج المستخلصة من العينات.</li><li>يوضح لماذا تكون التقديرات تقريبية عادةً.</li><li>يدفعنا إلى استعمال نظرية الاحتمالات.</li><li>يفسر الحاجة إلى الخطأ المعياري وفترات الثقة وغيرها من أدوات الاستدلال.</li></ul>
</div>
<div class="section-block">
  <h2>خطأ شائع</h2>
  <p>من الخطأ اعتبار إحصاء عينة واحدة مساويًا تمامًا لمعلمة المجتمع دون افتراضات أو تحليل لعدم اليقين. العينة مصدر مفيد للمعلومات، لكنها لا تلغي خطأ المعاينة.</p>
</div>
<div class="section-block">
  <h2>الفكرة الرئيسية</h2>
  <p>لا نسعى إلى إنكار وجود التباين العشوائي، بل إلى <strong>فهمه وقياسه</strong> وتحسين تصميم جمع البيانات وتفسير النتائج.</p>
</div>
<div class="section-block">
  <h2>ماذا بعد؟</h2>
  <p>تصلنا فكرة تباين المعاينة بالفرق بين <strong>معلمات المجتمع</strong> و<strong>إحصاءات العينة</strong>، وهو فرق أساسي في الإحصاء الاستدلالي.</p>
</div>
</section>
<section class="section section-slim"><div class="callout"><div class="callout-copy">
<h2>التنقل</h2>
<div class="hero-actions">
  <a class="btn btn-outline" href="/ar/">الصفحة العربية</a>
  <a class="btn" href="/foundations/sampling-variability/" lang="en" dir="ltr">English lesson</a>
</div>
</div></div></section>
