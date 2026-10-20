---
layout: default
title: معامل الاختلاف ومقارنة التشتت النسبي
description: درس عربي متكامل يشرح معامل الاختلاف وصيغته وتطبيقاته وحدوده مع مختبر تفاعلي لمقارنة مجموعتين من البيانات.
permalink: /ar/descriptive/spread/coefficient-of-variation/
lang: ar
sidebar: false
translation_pair: coefficient-of-variation
math: true
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الإحصاء الوصفي</span><span class="badge">مقاييس التشتت</span><span class="badge">التشتت النسبي</span></div>
<h1>معامل الاختلاف (Coefficient of Variation)</h1>
<p><a href="/descriptive/spread/coefficient-of-variation/" lang="en" dir="ltr">English — Coefficient of Variation</a></p>
<p class="lead">يصف الانحراف المعياري مقدار تشتت البيانات بوحدتها الأصلية، لكن المقارنة بين مجموعتين مختلفتين في متوسطاتهما قد تتطلب مقياساً نسبياً. ولهذا نستخدم <strong>معامل الاختلاف (CV)</strong> مع الانتباه إلى نوع مقياس القياس وإلى المتوسط الحسابي.</p>
<div class="hero-actions"><a class="btn" href="/ar/descriptive/spread/standard-deviation/">الدرس السابق: الانحراف المعياري</a><a class="btn btn-outline" href="/descriptive/spread/reporting-spread-properly/" lang="en" dir="ltr">Next (English): Reporting Spread</a></div>
</div></section>
<section class="section"><div class="content-narrow">
<h2>لماذا نحتاج إلى معامل الاختلاف؟</h2>
<p>يمثل الانحراف المعياري مقياساً مطلقاً للتشتت. فقد يكون انحراف أحد المتغيرين المعياري أكبر، ومع ذلك يكون تشتته <strong>النسبي</strong> أقل لأن متوسطه أكبر بكثير.</p>
<p>مثلاً، إذا كان متوسط العائد لاستثمار «أ» 10% وانحرافه المعياري نقطتين مئويتين، بينما كان متوسط عائد استثمار «ب» 100% وانحرافه خمس نقاط مئوية، فالتشتت المطلق للاستثمار «ب» أكبر، لكن معامل الاختلاف فيه أصغر. هذا مثال حسابي توضيحي، ولا يكفي معامل الاختلاف وحده لاتخاذ قرار استثماري.</p>
<div class="concept-box"><strong>الفكرة الأساسية:</strong><p>معامل الاختلاف يقيس الانحراف المعياري <strong>نسبةً إلى المتوسط</strong>، ولا يكتفي بوصف التشتت بوحدة القياس الأصلية.</p></div>
<h2>ما معامل الاختلاف؟</h2>
<p>معامل الاختلاف هو نسبة الانحراف المعياري إلى المتوسط الحسابي. عند وجود <strong>مقياس نسبي بصفر حقيقي ذي معنى ومتوسط موجب</strong>، يمكن استعمال هذه النسبة لوصف التشتت النسبي. يُلغى البعد الفيزيائي عندما تكون وحدتا البسط والمقام متماثلتين، ولذلك يكون المقياس بلا وحدة.</p>
<h2>الصيغة الرياضية</h2>
<p>لعينة تضم مشاهدتين على الأقل، ومع متوسط عينة موجب <span dir="ltr">x̄ &gt; 0</span>، نرمز للانحراف المعياري للعينة بالرمز <span dir="ltr">s</span>:</p>
<div class="esa-math-ltr" dir="ltr">\[
\mathrm{CV}=\frac{s}{\bar{x}},\qquad \bar{x}>0,\quad n\ge 2.
\]</div>
<p>وبالصيغة المئوية:</p>
<div class="esa-math-ltr" dir="ltr">\[
\mathrm{CV}_{\%}=\frac{s}{\bar{x}}\times100\%.
\]</div>
<p>للمجتمع الكامل نستخدم الانحراف المعياري للمجتمع <span dir="ltr">σ</span> والمتوسط <span dir="ltr">μ</span> في النسبة المقابلة. يتضمن مقام تباين العينة <span dir="ltr">n − 1</span>، بينما يستخدم تباين المجتمع <span dir="ltr">N</span>. يعرض المختبر الحسابين بوضوح.</p>
<h2>كيف نفسّر النسبة؟</h2>
<p>إذا كان معامل الاختلاف 20%، فهذا يعني أن الانحراف المعياري يساوي 20% من المتوسط الحسابي. ومع استيفاء الافتراضات، يشير معامل الاختلاف الأصغر إلى <strong>تشتت نسبي أقل</strong>، لا بالضرورة إلى جودة أعلى في جميع السياقات.</p>
<h2>مثال حسابي بسيط</h2>
<div class="example-box"><p>المتوسط الحسابي = 50، والانحراف المعياري = 10.</p></div>
<div class="esa-math-ltr" dir="ltr">\[
\mathrm{CV}=\frac{10}{50}=0.20,\qquad
\mathrm{CV}_{\%}=0.20\times100\%=20\%.
\]</div>
<p>إذن يمثل الانحراف المعياري خُمس المتوسط الحسابي في هذا المثال.</p>

<section class="concept-box" id="esa-cv-lab" aria-labelledby="esa-cv-title" style="max-width:100%;min-width:0;overflow-wrap:anywhere;overflow-x:clip">
<h2 id="esa-cv-title">مختبر تفاعلي لمعامل الاختلاف</h2>
<p>أدخل مجموعتين من المشاهدات لمقارنة المتوسط والانحراف المعياري ومعامل الاختلاف. يمكن اختيار حساب العينة باستخدام المقام <span dir="ltr">n − 1</span>، أو وصف مجتمع كامل باستخدام المقام <span dir="ltr">n</span>. يجب أن يكون الصفر ذا معنى ومتوسط كل مجموعة موجباً لكي تكون المقارنة النسبية ملائمة.</p>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:1rem">
<label for="esa-cv-a"><strong>المجموعة أ</strong> — قيم تفصل بينها فواصل أو مسافات
<textarea id="esa-cv-a" rows="3" dir="ltr" style="display:block;width:100%;max-width:100%;min-width:0" spellcheck="false">8, 10, 12</textarea></label>
<label for="esa-cv-b"><strong>المجموعة ب</strong> — قيم تفصل بينها فواصل أو مسافات
<textarea id="esa-cv-b" rows="3" dir="ltr" style="display:block;width:100%;max-width:100%;min-width:0" spellcheck="false">45, 50, 55</textarea></label>
</div>
<div style="display:flex;flex-wrap:wrap;gap:1rem;align-items:end;margin-top:1rem">
<label for="esa-cv-mode">طريقة حساب الانحراف المعياري
<select id="esa-cv-mode"><option value="sample" selected>العينة (n − 1)</option><option value="population">المجتمع (n)</option></select></label>
<label for="esa-cv-scale">مقياس القياس
<select id="esa-cv-scale"><option value="ratio" selected>مقياس نسبي بصفر حقيقي</option><option value="interval">مقياس فترة بصفر اعتباطي</option></select></label>
<button id="esa-cv-run" type="button" class="btn">قارن المجموعتين</button>
<button id="esa-cv-reset" type="button" class="btn btn-outline">إعادة المثال</button>
</div>
<p id="esa-cv-status" role="status" aria-live="polite"></p>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:1rem">
<div class="example-box" style="min-width:0;overflow-wrap:anywhere">
<h3>المجموعة أ</h3>
<p>عدد المشاهدات: <output id="esa-cv-a-n">—</output></p>
<p>المتوسط: <output id="esa-cv-a-mean">—</output></p>
<p>الانحراف المعياري: <output id="esa-cv-a-sd">—</output></p>
<p><strong>معامل الاختلاف: <output id="esa-cv-a-cv">—</output></strong></p></div>
<div class="example-box" style="min-width:0;overflow-wrap:anywhere">
<h3>المجموعة ب</h3>
<p>عدد المشاهدات: <output id="esa-cv-b-n">—</output></p>
<p>المتوسط: <output id="esa-cv-b-mean">—</output></p>
<p>الانحراف المعياري: <output id="esa-cv-b-sd">—</output></p>
<p><strong>معامل الاختلاف: <output id="esa-cv-b-cv">—</output></strong></p></div>
</div>
<p><strong>نتيجة المقارنة:</strong> <output id="esa-cv-comparison">—</output></p>
<p><strong>تحقق مستقل:</strong> للمجموعة أ = {8، 10، 12} والمجموعة ب = {45، 50، 55}، يكون متوسطا العينتين 10 و50، وانحرافاهما المعياريان 2 و5، ومعاملا الاختلاف 20% و10%. عند اعتبار القيم مجتمعيْن كاملين، يكون الانحرافان المعياريان تقريباً 1.633 و4.082، ومعاملا الاختلاف 16.33% و8.16%.</p>
<p><strong>حدود الاستخدام:</strong> لا يُفسَّر معامل الاختلاف لمتوسط صفري أو سالب في الصيغة الموجبة المستعملة هنا، ويصبح غير مستقر إذا كان المتوسط قريباً من الصفر. ويظهر التحذير التوضيحي إذا كان المتوسط أصغر من أو يساوي 10% من الانحراف المعياري؛ هذه ليست عتبة إحصائية عامة. لا يناسب معامل الاختلاف قياسات الحرارة بالدرجة المئوية لأن الصفر فيها ليس صفراً مطلقاً. تُحسب القيم داخل المتصفح، ويُقبل بين مشاهدتين و200 مشاهدة منتهية لكل مجموعة.</p>
</section>

<h2>مقارنة مجموعتين من البيانات</h2>
<div class="table-wrap"><table><thead><tr><th>المجموعة</th><th>المتوسط</th><th>الانحراف المعياري</th><th>معامل الاختلاف</th></tr></thead>
<tbody><tr><td>أ</td><td>20</td><td>4</td><td>20%</td></tr><tr><td>ب</td><td>100</td><td>10</td><td>10%</td></tr></tbody></table></div>
<p>رغم أن الانحراف المعياري للمجموعة «ب» أكبر، فإن التشتت النسبي للمجموعة «أ» أكبر في المثال.</p>
<div class="esa-math-ltr" dir="ltr">\[
\mathrm{CV}_{A,\%}=\frac{4}{20}\times100\%=20\%,
\qquad
\mathrm{CV}_{B,\%}=\frac{10}{100}\times100\%=10\%.
\]</div>
<h2>مقياس بلا وحدة</h2>
<p>عند قياس متغير بوحدة جديدة تنتج عن ضرب كل القيم بثابت موجب، يُضرب كل من المتوسط والانحراف المعياري بالثابت نفسه، ويبقى معامل الاختلاف دون تغيير. أما إضافة ثابت للبيانات أو نقل نقطة الصفر فيغيّر المتوسط دون الانحراف المعياري، فتتغير النسبة. لهذا يُشترط وجود صفر حقيقي ذي معنى عند المقارنة عبر الوحدات.</p>
<h2>معامل الاختلاف والاتساق</h2>
<p>إذا كانت البيانات ذات مقياس نسبي ومتوسط موجب، دل معامل الاختلاف الأصغر على تشتت أقل نسبةً إلى المتوسط، وهو ما قد يعكس تجانساً أكبر في بعض عمليات التصنيع أو القياس. لكنه لا يثبت صحة العمليات أو جودة الأداء وحده.</p>
<h2>تطبيقات في التمويل</h2>
<p>قد تُقارن بعض التطبيقات المالية تقلب العوائد بوصفه نسبةً إلى متوسط العائد الموجب، لكن قياسات العائد قد تكون سالبة أو قريبة من الصفر، فلا تصلح نسبة التشتت إلى المتوسط معياراً عاماً للمخاطرة. لا ينبغي اتخاذ قرار استثماري اعتماداً على معامل الاختلاف وحده.</p>
<h2>تطبيقات في العلوم والقياس</h2>
<p>يستخدم معامل الاختلاف لمقارنة دقة القياسات أو اختلافها النسبي عندما تكون المقاييس متناسبة، وتكون مقارنات المعايرة وظروف التجربة واضحة. ويُفيد في وصف تكرار القياسات بمقياس ذي صفر حقيقي.</p>
<h2>حدود معامل الاختلاف</h2>
<ul class="bullets">
<li>يعتمد على المتوسط، ويصبح غير معرّف عندما يكون المتوسط صفراً في النسبة المئوية المعتادة.</li>
<li>لا يكون تفسيره المعتاد مناسباً إذا كان المتوسط سالباً، وقد يؤدي المتوسط الصغير إلى قيمة ضخمة مضللة.</li>
<li>لا يصلح للمقاييس ذات الصفر الاعتباطي مثل درجات الحرارة المئوية.</li>
<li>يجب أن تكون المقارنة منطقية بحسب طبيعة المتغير ومقياسه، ولا يمثل مقياساً وحيداً لجودة البيانات.</li>
</ul>
<h2>المشكلة قرب المتوسط الصفري</h2>
<p>إذا كان المتوسط 0.5 والانحراف المعياري 5، فإن النسبة الحسابية 5 / 0.5 = 10، أي 1000%. هذه القيمة الكبيرة ناتجة عن صغر المتوسط وليس بالضرورة عن تشتت مطلق غير مألوف. لذلك يجب توخي الحذر.</p>
<h2>معامل الاختلاف مقارنةً بالانحراف المعياري</h2>
<div class="table-wrap"><table><thead><tr><th>الانحراف المعياري</th><th>معامل الاختلاف</th></tr></thead>
<tbody><tr><td>مقياس مطلق للتشتت</td><td>مقياس نسبي للتشتت</td></tr>
<tr><td>يحمل وحدة المتغير</td><td>بلا وحدة إذا توافقت وحدتا البسط والمقام</td></tr>
<tr><td>مناسب لوصف الانتشار داخل مقياس معين</td><td>مفيد لمقارنات التشتت النسبي عند استيفاء الشروط</td></tr></tbody></table></div>
<h2>متى نستخدم معامل الاختلاف؟</h2>
<p>يكون مفيداً عند مقارنة مجموعات ذات متوسطات موجبة، وصفر حقيقي ذي معنى، ومقاييس متناسبة، مثل قياسات الإنتاج أو بعض القياسات المخبرية أو متغيرات الحجم والكتلة، شريطة توافق التفسير العلمي. ولا يُستنتج من تفوق CV وحده تفوق أسلوب أو علاج في الدراسة.</p>
<h2>أهمية معامل الاختلاف</h2>
<p>يوفر معامل الاختلاف منظوراً نسبياً يكمل الانحراف المعياري والتباين. وتكمن قيمته في توفير مقارنة أوضح للتشتت عندما لا تكون المقاييس المطلقة قابلة للمقارنة مباشرةً.</p>
<h2>ماذا بعد؟</h2>
<p>بعد دراسة المدى والربيعات والتباين والانحراف المعياري ومعامل الاختلاف، ننتقل إلى كيفية عرض مقاييس التشتت والتواصل بشأنها بوضوح. <a href="/descriptive/spread/reporting-spread-properly/" lang="en" dir="ltr">Reporting Spread Properly (English)</a>.</p>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>معامل الاختلاف هو نسبة الانحراف المعياري إلى المتوسط الحسابي.</li>
<li>يمكن التعبير عنه كنسبة مئوية، ويكون بلا وحدة عندما تلغى وحدات البسط والمقام.</li>
<li>في المقاييس النسبية ذات المتوسط الموجب، يدل المعامل الأصغر على تشتت نسبي أقل.</li>
<li>يجب الحذر عند المتوسط الصفري أو السالب أو القريب من الصفر، وعند المقاييس ذات الصفر الاعتباطي.</li>
<li>توفر الأداة التفاعلية مقارنة بين حسابات العينة والمجتمع مع تحذيرات تفسيرية.</li>
</ul></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/descriptive/spread/standard-deviation/">السابق: الانحراف المعياري</a><a class="btn" href="/descriptive/spread/coefficient-of-variation/" lang="en" dir="ltr">English version</a></div>
</div></section>
<script src="/js/coefficient-of-variation-explorer.js" defer></script>
