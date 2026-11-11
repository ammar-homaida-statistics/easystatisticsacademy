---
layout: default
title: اختبار t للعينات المزدوجة
description: شرح عربي لاختبار ستودنت للعينات المزدوجة مع الفرق بين قبل وبعد، الافتراضات والقيمة الاحتمالية وفترة الثقة ومختبر تفاعلي.
permalink: /ar/inference/classical-tests/paired-t-test/
lang: ar
math: true
sidebar: false
translation_pair: paired-student-t
learning_resource: true
---
<section class="hero hero-section"><div class="hero-card">
<h1>اختبار t للعينات المزدوجة</h1>
<p class="lead">نقارن قياسين مترابطين للشخص نفسه أو لوحدتين متطابقتين، وذلك باختبار متوسط <strong>الفروق داخل الأزواج</strong>؛ لا نعامل القياسات وكأنها عينتان مستقلتان.</p>
<p><a lang="en" dir="ltr" href="/inference/classical-tests/paired-t-test/">Read in English: Paired t Test</a></p>
</div></section>
<section class="section"><div class="content-narrow" dir="rtl">
<h2>1. لماذا نستخدم اختبار t للعينات المزدوجة؟</h2>
<p>في دراسة قبل التدخل وبعده، لكل شخص قياسان مترابطان. نعرّف الفرق على أنه \(D_i=X_{i,\text{بعد}}-X_{i,\text{قبل}}\). يتعامل اختبار t المزدوج مع الفروق \(D_i\)، ويُجرى اختبار لعينة واحدة على متوسطها السكاني \(\mu_D\).</p>
<h2>2. الفرضيات والإحصائية</h2>
<p>نفترض \(H_0:\mu_D=\mu_{D,0}\)، وغالباً \(\mu_{D,0}=0\). وتكون البديلة ثنائية الطرف أو باتجاه زيادة أو نقصان محدد مسبقاً.</p>
<div class="esa-pt-math" dir="ltr" role="region" tabindex="0" aria-label="صيغ اختبار ستودنت المزدوج">\[
\overline D=\frac1n\sum_{i=1}^{n}D_i,\qquad
s_D^2=\frac{\sum_{i=1}^{n}(D_i-\overline D)^2}{n-1},\qquad
T=\frac{\overline D-\mu_{D,0}}{s_D/\sqrt{n}},\quad df=n-1.
\]</div>
<p>في ظل افتراض استقلال الأزواج وطبيعية الفروق في المجتمع، تتبع الإحصائية توزيع ستودنت بدرجات حرية \(n-1\) تحت الفرضية الصفرية. داخل كل زوج يوجد ارتباط مسموح به، أما الأزواج المختلفة فيُفترض استقلالها. وقد يكون التقريب مناسباً في عينات كبيرة إذا استوفت البيانات الشروط اللازمة.</p>
<h2>3. مثال محلول بخمسة أزواج</h2>
<p>لدينا قياسات قبل وبعد: \( (70,75),(68,72),(75,79),(71,74),(69,74)\). الفروق «بعد ناقص قبل» هي \(5,4,4,3,5\)، ومن ثم \(\overline d=4.2\)، و\(s_D\approx0.83666\)، و\(\widehat{\mathrm{SE}}\approx0.37417\).</p>
<div class="esa-pt-math" dir="ltr" role="region" tabindex="0" aria-label="حساب إحصائية المثال">\[
T=\frac{4.2-0}{0.836660/\sqrt5}\approx11.224972,\qquad df=4.
\]</div>
<p>القيمة الاحتمالية للاختبار ثنائي الطرف تقارب \(0.000359\)، فنرفض فرضية انعدام متوسط التغير عند \(\alpha=0.05\) إذا تحققت الافتراضات. لا تثبت هذه النتيجة السببية؛ فقد تكون هناك عوامل زمنية أو مؤثرات أخرى.</p>
<h2>4. فترة الثقة لمتوسط الفرق</h2>
<div class="esa-pt-math" dir="ltr" role="region" tabindex="0" aria-label="فترة الثقة">\[
\overline d\pm t_{0.975,n-1}\frac{s_D}{\sqrt n}
=4.2\pm2.776445(0.374166)\approx[3.161,\ 5.239].
\]</div>
<p>الفترة ثنائية الطرف عند مستوى ثقة 95%، حتى لو اخترنا فرضية أحادية الطرف للمختبر. إذا عكسنا تعريف الفرق من «بعد − قبل» إلى «قبل − بعد» انعكست إشارة المتوسط وإحصائية t وحدود فترة الثقة، مع ثبات القيمة الاحتمالية للاختبار ثنائي الطرف.</p>
<h2>5. مختبر تفاعلي عربي</h2>
<section class="concept-box" id="esa-paired-t-lab" data-locale="ar" aria-labelledby="esa-pt-heading">
<h3 id="esa-pt-heading">تجربة اختبار t للأزواج</h3>
<p>أدخل قياسي «قبل، بعد» في كل سطر، من زوجين إلى 40 زوجاً. الاتجاه المعتمد للفرق هو «بعد − قبل».</p>
<label for="esa-pt-input">أزواج القياسات: قبل، بعد</label>
<textarea id="esa-pt-input" rows="6" spellcheck="false" aria-describedby="esa-pt-error">70,75
68,72
75,79
71,74
69,74</textarea>
<div class="esa-pt-fields">
<div><label for="esa-pt-alternative">الفرضية البديلة</label><select id="esa-pt-alternative"><option value="two-sided">ثنائي الطرف</option><option value="greater">متوسط الفرق أكبر من المفترض</option><option value="less">متوسط الفرق أصغر من المفترض</option></select></div>
<div><label for="esa-pt-null">متوسط الفرق المفترض \(\mu_{D,0}\)</label><input id="esa-pt-null" type="number" step="any" value="0" aria-describedby="esa-pt-error"></div>
</div>
<div class="esa-pt-controls"><button type="button" class="btn btn-outline" id="esa-pt-reset">استعادة المثال</button><button type="button" class="btn btn-outline" id="esa-pt-negative">عكس اتجاه قياسات قبل وبعد</button></div>
<p id="esa-pt-error" role="alert" hidden></p>
<section id="esa-pt-results" role="status" aria-live="polite" aria-atomic="true" aria-label="نتائج اختبار ستودنت المزدوج">
<h3>مقارنة القياسات المزدوجة</h3>
<svg id="esa-pt-plot" viewBox="0 0 620 175" role="img" aria-label="مخطط القياسات قبل وبعد لكل زوج" style="display:block;width:100%;height:auto;max-width:100%"></svg>
<p class="muted-mini">الدوائر الرمادية: قبل؛ والدوائر الخضراء: بعد. يصل الخط قياسي كل زوج.</p>
<p id="esa-pt-plot-limit" class="muted-mini"></p>
<div class="table-wrap"><table><caption>الأزواج وفروقها</caption><thead><tr><th>الزوج</th><th>قبل</th><th>بعد</th><th>بعد − قبل</th></tr></thead><tbody id="esa-pt-table"></tbody></table></div>
<p>عدد الأزواج: <output id="esa-pt-n">—</output>؛ متوسط الفرق: <output id="esa-pt-mean">—</output>؛ الانحراف المعياري للفروق: <output id="esa-pt-sd">—</output>.</p>
<p>الخطأ المعياري: <output id="esa-pt-se">—</output>؛ إحصائية t: <output id="esa-pt-t">—</output>؛ درجات الحرية: <output id="esa-pt-df">—</output>؛ القيمة الاحتمالية: <output id="esa-pt-p">—</output>.</p>
<p>قيمة t الحرجة عند 95%: <output id="esa-pt-critical">—</output>؛ فترة الثقة ثنائية الطرف: [<output id="esa-pt-lower">—</output>, <output id="esa-pt-upper">—</output>].</p>
<p id="esa-pt-conclusion"></p><p id="esa-pt-interpret"></p>
</section>
</section>
<h2>6. الحدود والأخطاء الشائعة</h2>
<ul class="bullets">
<li>لا تخلط الاختبار المزدوج باختبار عينتين مستقلتين؛ يجب الحفاظ على المطابقة الصحيحة لكل زوج.</li>
<li>يحتاج التقدير المعتاد إلى تباين موجب للفروق؛ إذا كانت كل الفروق متطابقة فإن الإحصائية وفترة الثقة التقليديتين لا تُعرَّفان.</li>
<li>التوزيع الطبيعي المطلوب عند صغر العينة يتعلق <strong>بالفروق</strong>، لا بالضرورة بكل متغير على حدة.</li>
<li>لا يعني عدم رفض الفرضية إثبات عدم وجود تغير، ولا يعني رفضها أن التغير ذو أهمية عملية أو سببية.</li>
</ul>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/inference/classical-tests/one-sample-t-test-for-mean/">السابق: اختبار t لعينة واحدة</a><a class="btn" href="/ar/inference/classical-tests/two-sample-t-test-independent/">التالي: اختبار t لعينتين مستقلتين</a></div>
</div></section>
<style>
#esa-paired-t-lab{box-sizing:border-box;max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-paired-t-lab textarea{display:block;box-sizing:border-box;max-width:100%;width:100%;padding:10px;min-height:100px}
#esa-paired-t-lab .esa-pt-fields{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,210px),1fr));gap:12px;margin:12px 0}
#esa-paired-t-lab .esa-pt-fields :is(input,select){box-sizing:border-box;width:100%;max-width:100%;padding:10px;font:inherit}
#esa-paired-t-lab .esa-pt-controls{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0}
#esa-paired-t-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-paired-t-lab :is(textarea,input,select,button):focus-visible{outline:2px solid #0f766e;outline-offset:3px}
#esa-paired-t-lab [hidden]{display:none!important}
.esa-pt-math{max-width:100%;overflow-x:auto;direction:ltr;padding:7px 0}
</style>
<script defer src="/js/paired-t-explorer.js"></script>