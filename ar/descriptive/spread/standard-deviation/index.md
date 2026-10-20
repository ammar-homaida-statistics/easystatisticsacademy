---
layout: default
title: الانحراف المعياري
description: درس شامل في الانحراف المعياري وتباين المجتمع والعينة وحساسيته للقيم المتطرفة مع مختبر حسابي تفاعلي.
permalink: /ar/descriptive/spread/standard-deviation/
lang: ar
sidebar: false
translation_pair: standard-deviation
math: true
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الإحصاء الوصفي</span><span class="badge">مقاييس التشتت</span><span class="badge">الانحراف المعياري</span></div>
<h1>الانحراف المعياري</h1>
<p><a lang="en" dir="ltr" href="/descriptive/spread/standard-deviation/">English — Standard Deviation</a></p>
<p class="lead">التباين مقياس أساسي للتشتت، لكن وحدته مربعة؛ لذا نأخذ جذره التربيعي للحصول على
الانحراف المعياري الذي يُعبَّر عنه بوحدة القياس الأصلية، ويشيع استعماله لوصف تشتت البيانات.</p>
<div class="hero-actions">
<a class="btn" lang="en" dir="ltr" href="/descriptive/spread/variance/">Previous: Variance (English)</a>
<a class="btn btn-outline" href="/ar/descriptive/spread/coefficient-of-variation/">التالي: معامل الاختلاف</a>
</div></div></section>
<section class="section"><div class="content-narrow">
<h2>ما الانحراف المعياري؟</h2>
<p><strong>الانحراف المعياري</strong> مقياس لتشتت المشاهدات حول متوسطها الحسابي.
ويمكن فهمه بوصفه جذر متوسط مربعات الفروق عن المتوسط وفق المقام الملائم.
لا يساوي بالضرورة متوسط المسافات المطلقة؛ إذ تُربَّع الفروق أولًا.</p>
<div class="concept-box"><strong>الفكرة الأساسية:</strong><p>كلما ازداد تشتت القيم حول المتوسط ازداد الانحراف المعياري عادةً،
أما إذا تساوت جميع القيم فيكون صفراً.</p></div>
<h2>لماذا نستخدم الانحراف المعياري؟</h2>
<p>يقيس التباين متوسط مربعات الانحرافات عن المتوسط، ويُعد مفيداً رياضياً، لكنه يقاس بوحدة مربعة.
وبأخذ الجذر التربيعي للتباين نعود إلى وحدة المتغير الأصلية، فيصبح الوصف أسهل تفسيراً.</p>
<h2>الصيغة الرياضية</h2>
<p>للعينة، عندما يكون عدد المشاهدات مشاهدتين على الأقل:</p>
<div class="esa-math-ltr">\[
s=\sqrt{\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}},\qquad n\ge 2
\]</div>
<p>وللمجتمع الإحصائي الكامل:</p>
<div class="esa-math-ltr">\[
\sigma=\sqrt{\frac{\sum_{i=1}^{N}(x_i-\mu)^2}{N}},\qquad N\ge 1
\]</div>
<p>الرمز <span dir="ltr">s</span> لانحراف العينة المعياري ومقام التباين هو <span dir="ltr">n − 1</span>،
بينما يعبّر <span dir="ltr">σ</span> عن انحراف المجتمع ومقام تباينه عدد أفراده <span dir="ltr">N</span>.
الانحراف المعياري هو الجذر التربيعي غير السالب للتباين.</p>

<section class="concept-box" id="esa-sd-lab" aria-labelledby="esa-sd-title" style="min-width:0;overflow-wrap:anywhere">
<h2 id="esa-sd-title">مختبر تفاعلي للانحراف المعياري</h2>
<p>غيّر قيم المشاهدات لتشاهد المتوسط، والفروق عنه، ومربعات تلك الفروق، والتباين والانحراف المعياري.
استخدم مقام <span dir="ltr">n</span> لوصف المجتمع الكامل الذي تُمثل هذه القيم كل أفراده؛
واستخدم مقام <span dir="ltr">n − 1</span> لتقدير تباين المجتمع من عينة مستقلة متجانسة التوزيع في الإعداد المعتاد.
جذر تباين العينة هو الانحراف المعياري للعينة، لكنه ليس عمومًا مقدّرًا غير متحيز للانحراف المعياري للمجتمع.</p>
<label for="esa-sd-values">المشاهدات (من 1 إلى 20 قيمة تفصلها فواصل أو مسافات؛ القيمة الواحدة لتوضيح الحالة الحدية)</label>
<textarea id="esa-sd-values" rows="2" dir="ltr" style="display:block;width:100%;max-width:100%;box-sizing:border-box">2, 4, 4, 4, 5, 5, 7, 9</textarea>
<div style="display:flex;flex-wrap:wrap;gap:.5rem;margin:1rem 0">
<button id="esa-sd-run" type="button" class="btn">احسب</button>
<button id="esa-sd-outlier" type="button" class="btn btn-outline">أضف مشاهدة متطرفة</button>
<button id="esa-sd-identical" type="button" class="btn btn-outline">قيم متطابقة</button>
<button id="esa-sd-single" type="button" class="btn btn-outline">مشاهدة واحدة</button>
<button id="esa-sd-reset" type="button" class="btn btn-outline">إعادة الضبط</button>
</div>
<p id="esa-sd-status" role="status" aria-live="polite"></p>
<dl style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,155px),1fr));gap:.8rem">
<div><dt>عدد المشاهدات (n)</dt><dd id="esa-sd-count">—</dd></div>
<div><dt>المتوسط الحسابي</dt><dd id="esa-sd-mean">—</dd></div>
<div><dt>مجموع مربعات الانحرافات</dt><dd id="esa-sd-ss">—</dd></div>
<div><dt>تباين المجتمع (القسمة على n)</dt><dd id="esa-sd-pop-var">—</dd></div>
<div><dt>انحراف المجتمع المعياري (σ)</dt><dd id="esa-sd-pop-sd">—</dd></div>
<div><dt>تباين العينة (القسمة على n − 1)</dt><dd id="esa-sd-samp-var">—</dd></div>
<div><dt>انحراف العينة المعياري (s)</dt><dd id="esa-sd-samp-sd">—</dd></div>
</dl>
<div role="region" tabindex="0" aria-label="جدول الانحرافات القابل للتمرير" style="max-width:100%;overflow-x:auto;overscroll-behavior-x:contain">
<table style="width:100%;min-width:480px">
<caption>إسهام كل مشاهدة في مجموع مربعات الانحرافات</caption>
<thead><tr><th>الترتيب</th><th>القيمة</th><th>الانحراف عن المتوسط</th><th>مربع الانحراف</th></tr></thead><tbody id="esa-sd-table"></tbody>
</table></div>
<p><strong>وحدات القياس:</strong> إذا قسنا الأطوال بالسنتيمتر كان الانحراف المعياري بالسنتيمتر،
في حين يُقاس التباين بالسنتيمتر المربع. تكون القيمتان صفراً إذا تساوت المشاهدات.
عند وجود مشاهدة واحدة، يكون انحراف المجتمع المعياري صفراً، بينما لا يُعرّف تباين العينة وانحرافها المعياري.</p>
<p id="esa-sd-note"></p>
</section><script src="/js/standard-deviation-lab.js" defer></script>

<h2>الصلة بين التباين والانحراف المعياري</h2>
<div class="table-wrap"><table><thead><tr><th>المقياس</th><th>الرمز</th></tr></thead><tbody>
<tr><td>تباين العينة</td><td dir="ltr">s²</td></tr>
<tr><td>الانحراف المعياري للعينة</td><td dir="ltr">s</td></tr>
<tr><td>تباين المجتمع</td><td dir="ltr">σ²</td></tr>
<tr><td>الانحراف المعياري للمجتمع</td><td dir="ltr">σ</td></tr>
</tbody></table></div>
<h2>مثال بسيط</h2>
<p>إذا كان التباين يساوي <span dir="ltr">25</span>، فإن:</p>
<div class="esa-math-ltr">\[
\mathrm{SD}=\sqrt{25}=5
\]</div>
<p>إذن الانحراف المعياري يساوي 5، ويُعبَّر عنه بوحدة القياس الأصلية.</p>
<h2>ما الذي يخبرنا به الانحراف المعياري؟</h2>
<p>يوضح مدى انتشار المشاهدات حول متوسطها. القيم الصغيرة تدل على تركز أشد قرب المتوسط،
والقيم الكبيرة تدل على انتشار أوسع، عند المقارنة بين متغيرات ذات وحدة ومقياس مناسبين.</p>
<h2>انحراف معياري صغير</h2>
<p>انظر إلى القيم <span dir="ltr">98, 99, 100, 101, 102</span>. إنها متقاربة حول 100؛
ومن ثم يكون الانحراف المعياري صغيراً وتبدو المشاهدات متسقة نسبياً.</p>
<h2>انحراف معياري كبير</h2>
<p>انظر إلى القيم <span dir="ltr">20, 40, 60, 80, 100</span>. انتشارها حول المتوسط
أوسع، ولذلك يكون الانحراف المعياري أكبر ويقل تشابه المشاهدات.</p>
<h2>متى يساوي الانحراف المعياري صفراً؟</h2>
<p>عندما تتطابق القيم جميعها، مثل <span dir="ltr">10, 10, 10, 10, 10</span>،
يكون كل فرق عن المتوسط صفراً. بالتالي:</p>
<div class="esa-math-ltr">\[
\text{Variance}=0,\qquad \text{Standard deviation}=0
\]</div>
<p>هذه النتيجة تنطبق على تباين المجتمع والعينة إذا كان مقامهما معرَّفاً.</p>
<h2>تفسير وحدات القياس</h2>
<ul class="bullets"><li>إذا قيس الطول بالسنتيمتر كان الانحراف المعياري بالسنتيمتر.</li>
<li>إذا قيس الوزن بالكيلوغرام كان الانحراف المعياري بالكيلوغرام.</li>
<li>إذا قيس الدخل بالدولار كان الانحراف المعياري بالدولار.</li></ul>
<p>وهذا ما يسهّل تفسيره مقارنة بالتباين ذي الوحدة المربعة.</p>
<h2>الانحراف المعياري والمتوسط الحسابي</h2>
<p>يُحسب الانحراف المعياري بالنسبة إلى المتوسط الحسابي؛ لذا تُعرض القيمتان معاً كثيراً
لأن المتوسط يلخص المركز، والانحراف المعياري يلخص التشتت حوله.</p>
<div class="example-box"><p>المتوسط الحسابي ± الانحراف المعياري</p></div>
<h2>عرض المتوسط والانحراف المعياري معاً</h2>
<p>بالنسبة إلى توزيع عددي متماثل تقريباً، قد نعرض مثلاً:
المتوسط الحسابي = <span dir="ltr">72.4</span>؛ والانحراف المعياري = <span dir="ltr">8.1</span>.
بهذا نوجز موضع المركز ومقدار التشتت معاً.</p>
<h2>تأثير القيم المتطرفة</h2>
<p>يقوم التباين على تربيع الانحرافات؛ لذلك تحظى الفروق الكبيرة بوزن أكبر،
ويكون الانحراف المعياري <strong>حساساً للقيم المتطرفة</strong> وغير مقاوم لها.
جرّب زر المشاهدة المتطرفة في المختبر أعلاه لملاحظة التأثير.</p>
<h2>الانحراف المعياري وشكل التوزيع</h2>
<p>يلخص الانحراف المعياري مقدار التشتت، لكنه لا يبيّن وحده الالتواء
أو عدد القمم أو بقية خصائص الشكل. لهذا من المهم النظر إلى الرسوم البيانية
ومقاييس أخرى عند وصف مجموعة بيانات.</p>
<h2>القاعدة التجريبية 68–95–99.7</h2>
<p>في <strong>التوزيع الطبيعي</strong> المتماثل ذي الشكل الجرسي، تقع تقريباً النسب التالية
من المشاهدات حول متوسط المجتمع:</p>
<div class="table-wrap"><table><thead><tr><th>المجال حول المتوسط</th><th>النسبة التقريبية</th></tr></thead><tbody>
<tr><td>المتوسط ± انحراف معياري واحد</td><td>68%</td></tr>
<tr><td>المتوسط ± انحرافين معياريين</td><td>95%</td></tr>
<tr><td>المتوسط ± ثلاثة انحرافات معيارية</td><td>99.7%</td></tr>
</tbody></table></div>
<p>هذه قاعدة تقريبية للتوزيع الطبيعي وليست قانوناً صالحاً لكل التوزيعات؛
فقد تختلف النسب كثيراً مع الالتواء أو الذيول الثقيلة.</p>
<h2>تطبيقات الانحراف المعياري</h2>
<ul class="bullets"><li>البحوث العلمية</li><li>تحليلات الأعمال</li><li>الاقتصاد</li><li>التمويل</li>
<li>الهندسة</li><li>تعلم الآلة</li><li>مراقبة الجودة</li></ul>
<p>لذلك يعد من المقاييس الأكثر استعمالاً في التقارير العلمية.</p>
<h2>لماذا يهم الانحراف المعياري؟</h2>
<p>يجمع الانحراف المعياري بين أساس رياضي واضح وتفسير عملي مباشر.
وهو يستخدم جميع القيم ولا يكتفي بالقيمتين القصويين، ويمكن التعبير عنه
بوحدات المتغير المقاس، ولذلك يستخدم كثيراً في وصف البيانات.</p>
<h2>ماذا يأتي بعد ذلك؟</h2>
<p>يقيس الانحراف المعياري التشتت المطلق، بينما قد نحتاج عند المقارنة بين مقاييس مختلفة
إلى مقياس نسبي مثل <strong>معامل الاختلاف</strong>، الذي يقارن التشتت بحجم المتوسط
مع الانتباه لشروط ملاءمة هذا الاستخدام.</p>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>الانحراف المعياري هو الجذر التربيعي للتباين.</li>
<li>يلخص مقدار تشتت القيم حول المتوسط الحسابي.</li>
<li>وحدته هي وحدة المتغير، على خلاف التباين.</li>
<li>يدل صغر الانحراف المعياري على تقارب القيم نسبياً.</li>
<li>ويدل كبره على انتشار أكبر.</li>
<li>يتأثر بالقيم المتطرفة.</li>
<li>يُعد من أهم مقاييس التشتت في الإحصاء الوصفي.</li>
</ul></div>
<div class="lesson-nav">
<a class="btn btn-outline" href="/descriptive/spread/variance/" lang="en" dir="ltr">Previous: Variance (English)</a>
<a class="btn" href="/descriptive/spread/coefficient-of-variation/" lang="en" dir="ltr">Next: Coefficient of Variation (English)</a>
</div></div></section>