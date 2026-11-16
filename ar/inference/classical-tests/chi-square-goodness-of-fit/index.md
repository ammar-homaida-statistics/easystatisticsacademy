---
layout: default
title: اختبار كاي تربيع لحسن المطابقة
description: شرح عربي شامل لاختبار كاي تربيع لحسن المطابقة مع أمثلة ومختبر تفاعلي للتحقق من تكرارات الفئات.
permalink: /ar/inference/classical-tests/chi-square-goodness-of-fit/
lang: ar
sidebar: false
learning_resource: true
translation_pair: chi-square-gof
---
<section class="hero hero-section"><div class="hero-card">
<h1>اختبار كاي تربيع لحسن المطابقة</h1>
<p class="lead">هل توافق التكرارات المشاهدة التوزيع الاحتمالي المفترض لفئات البيانات؟ يوضح هذا الدرس كيفية إجراء اختبار بيرسون لحسن المطابقة (Pearson chi-square goodness-of-fit) وتفسير نتائجه.</p>
<p><a href="/inference/classical-tests/chi-square-goodness-of-fit/">English version</a> · <a href="/ar/inference/classical-tests/two-proportion-z-test/">اختبار Z لنسبتين مستقلتين</a></p>
</div></section>
<section><div class="content-narrow">
<h2>1. سؤال البحث ومعنى حسن المطابقة</h2>
<p>إذا رمينا حجر نرد سداسيًا عدة مرات، فهل تتفق الأعداد المشاهدة مع احتمال \(1/6\) لكل وجه؟ وبصورة أعم، قد يكون لدينا توزيع مفترض لنسب تفضيلات المستهلكين أو تصنيفات جودة المنتجات. يختبر حسن المطابقة مدى ابتعاد تكرارات الفئات عن التكرارات المتوقعة في ظل هذا النموذج.</p>
<p>الاختبار مخصص لبيانات <strong>فئوية</strong> تُصنف إلى فئات متنافية وشاملة. إنه لا يختبر العلاقة بين متغيرين فئويين؛ تلك مسألة اختبار الاستقلال.</p>
<h2>2. الفرضيتان الإحصائيتان</h2>
<p>الفرضية الصفرية \(H_0\): احتمالات جميع الفئات تساوي القيم المحددة في النموذج \(p_i=p_i^{(0)}\). الفرضية البديلة \(H_a\): يختلف احتمال فئة واحدة على الأقل عن قيمتها المفترضة. يجب أن تُحدَّد الاحتمالات الصفرية قبل الاطلاع على النتائج التي ستُختبر.</p>
<h2>3. التكرارات المشاهدة والمتوقعة</h2>
<p>لنرمز إلى عدد المشاهدات في الفئة \(i\) بـ \(O_i\)، وإجمالي حجم العينة بـ \(n\)، واحتمال الفئة المفترض بـ \(p_i\). يصبح التكرار المتوقع \(E_i=np_i\)، مع شرط \(p_i>0\) وأن يكون مجموع الاحتمالات واحدًا.</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="تعريف التكرار المتوقع">
\[
E_i=n p_i,\quad \sum_{i=1}^{k}p_i=1.
\]</div>
<p>في مثال حجر النرد العادل، إذا كان \(n=120\)، فإن التكرار المتوقع لكل وجه هو \(120/6=20\).</p>
<h2>4. إحصائية بيرسون ودرجات الحرية</h2>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="إحصائية اختبار حسن المطابقة">
\[
\chi^2=\sum_{i=1}^{k}\frac{(O_i-E_i)^2}{E_i},\qquad df=k-1.
\]</div>
<p>تُحسب مساهمة كل فئة بطرح المتوقع من المشاهد، وتربيع الفرق، ثم قسمته على التكرار المتوقع. وتُجمع المساهمات، لذلك تكون الإحصائية غير سالبة. كلما زاد الفرق الكلي، زادت الإحصائية في العادة.</p>
<p>تساوي درجات الحرية \(k-1\) <strong>عندما تكون احتمالات جميع الفئات محددة مسبقًا</strong>. إذا قُدِّرت معلمات التوزيع من البيانات نفسها فقد تتغير درجات الحرية بحسب النموذج وطريقة التقدير؛ ولا يعالج المختبر أدناه هذه الحالة.</p>
<h2>5. مثال حسابي: ستون رمية</h2>
<p>لنفترض أن الأعداد المشاهدة للأوجه الستة هي \(8،11،9،13،10،9\)، ومجموعها 60. لكل وجه تكرار متوقع يساوي 10. مساهمات بيرسون هي \(0.4،0.1،0.1،0.9،0،0.1\)، وبالتالي:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="حساب اختبار النرد">
\[\chi^2=1.6,\qquad df=5,\qquad P(\chi^2_5\ge1.6)\approx0.901249.\]</div>
<p>عند مستوى دلالة \(\alpha=0.05\)، لا نرفض الفرضية الصفرية. <strong>عدم الرفض لا يثبت عدالة حجر النرد</strong>؛ بل يعني أن هذه البيانات لم تقدم دليلًا كافيًا ضد النموذج المفترض بهذا الاختبار.</p>
<h2>6. مختبر كاي تربيع التفاعلي</h2>
<section id="esa-gof-explorer" class="concept-box" data-locale="ar" aria-labelledby="esa-gof-heading">
<h3 id="esa-gof-heading">قارن التكرارات المشاهدة والمتوقعة</h3>
<p>أدخل أعدادًا صحيحة غير سالبة للفئات، واحتمالات صفرية موجبة ومحددة مسبقًا مجموعها يساوي 1. يسمح المختبر بفئتين إلى 12 فئة، ويحسب إحصائية بيرسون والقيمة الاحتمالية التقريبية للطرف الأيمن.</p>
<div class="esa-gof-fields">
<div><label for="esa-gof-counts">التكرارات المشاهدة (افصل بينها بفاصلة إنجليزية)</label><textarea id="esa-gof-counts" dir="ltr" rows="3" spellcheck="false" aria-invalid="false" aria-describedby="esa-gof-error esa-gof-warning">8, 11, 9, 13, 10, 9</textarea></div>
<div><label for="esa-gof-probs">احتمالات الفئات تحت الفرضية الصفرية (مجموعها 1)</label><textarea id="esa-gof-probs" dir="ltr" rows="3" spellcheck="false" aria-invalid="false" aria-describedby="esa-gof-error esa-gof-warning">0.1666666667, 0.1666666667, 0.1666666667, 0.1666666667, 0.1666666667, 0.1666666665</textarea></div>
</div>
<div class="esa-gof-controls"><button type="button" class="btn btn-outline" id="esa-gof-die">مثال النرد العادل</button><button type="button" class="btn btn-outline" id="esa-gof-uneven">احتمالات غير متساوية</button><button type="button" class="btn btn-outline" id="esa-gof-reset">إعادة الضبط</button></div>
<p id="esa-gof-error" role="alert" hidden></p>
<div id="esa-gof-results" role="status" aria-live="polite" aria-atomic="true">
<h3>المشاهَد والمتوقَّع حسب الفئة</h3>
<svg id="esa-gof-chart" viewBox="0 0 540 205" role="img" aria-label="الأعمدة المشاهدة والمتوقعة بحسب الفئة"></svg>
<p class="muted-mini">اللون الأخضر المزرق: المشاهَد؛ الرمادي: المتوقَّع.</p>
<div class="table-wrap"><table><caption>مساهمة كل فئة في إحصائية بيرسون</caption><thead><tr><th>الفئة</th><th>المشاهَد</th><th>احتمال العدم</th><th>المتوقَّع</th><th>(O−E)²/E</th></tr></thead><tbody id="esa-gof-table"></tbody></table></div>
<p>إجمالي المشاهدات: <output id="esa-gof-n">60</output>؛ إحصائية χ²: <output id="esa-gof-chi">1.600000</output>؛ درجات الحرية: <output id="esa-gof-df">5</output>؛ القيمة الاحتمالية: <output id="esa-gof-p">0.901249</output>.</p>
<p id="esa-gof-warning" role="status" aria-live="polite">جميع التكرارات المتوقعة لا تقل عن 5.</p>
<p id="esa-gof-decision">عند α=0.05 لا نرفض الفرضية الصفرية المحددة مسبقًا.</p>
</div>
<p class="muted-mini">تعرض الآلة تقريب كاي تربيع التقاربي فقط؛ وهي لا تحسب قيمة احتمالية متعددة الحدود دقيقة، ولا تُقدِّر معلمات فرضية العدم من البيانات.</p>
</section>
<h2>7. افتراضات الاختبار والقيود</h2>
<ul class="bullets"><li>تأتي البيانات من مشاهدات مستقلة وفق تصميم سحب ملائم.</li><li>كل مشاهدة تنتمي إلى فئة واحدة من فئات متنافية وشاملة.</li><li>احتمالات العدم موجبة وثابتة ومحددة قبل تحليل البيانات.</li><li>ينبغي أن تكون التكرارات المتوقعة كافية ليكون تقريب كاي تربيع موثوقًا.</li></ul>
<p>القاعدة الشائعة \(E_i\ge5\) لكل فئة إرشادية وليست شرطًا رياضيًا مطلقًا. إذا كانت التكرارات صغيرة، فقد نحتاج إلى اختبار متعدد الحدود دقيق أو أسلوب محاكاة ملائم. كما أن قيمة احتمالية كبيرة لا تعني احتمالًا كبيرًا لصحة \(H_0\)، ولا يثبت رفض الفرضية وجود علاقة سببية.</p>
<h2>8. الفرق بين اختبارات النسب وحسن المطابقة والاستقلال</h2>
<p>تختبر اختبارات النسب نسبة واحدة أو فرقًا بين نسبتين. أما حسن المطابقة فيقارن <strong>توزيع متغير فئوي واحد</strong> مع توزيع مفترض سلفًا. بينما يفحص اختبار استقلال كاي تربيع ارتباط <strong>متغيرين فئويين</strong> في جدول توافق؛ ويمكن مقارنة اختبار فيشر الدقيق مع بيرسون في جداول 2×2.</p>
<p><a href="/inference/classical-tests/chi-square-independence-test/">اختبار الاستقلال (بالإنجليزية)</a> · <a href="/inference/classical-tests/fisher-exact-vs-chi-square/">مختبر فيشر مقابل كاي تربيع (بالإنجليزية)</a></p>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets"><li>حسن المطابقة يقارن التكرارات المشاهدة والمتوقعة.</li><li>\(E_i=np_i\)، و\(\chi^2=\sum(O_i-E_i)^2/E_i\).</li><li>درجات الحرية \(k-1\) عندما تكون احتمالات الفئات محددة مسبقًا.</li><li>القيمة الاحتمالية تقاربية وتحتاج افتراضات سليمة وتكرارات متوقعة كافية.</li><li>عدم رفض \(H_0\) لا يثبت صحتها.</li></ul></div>
</div></section>
<style>
#esa-gof-explorer{box-sizing:border-box;min-width:0;max-width:100%;overflow-wrap:anywhere}
#esa-gof-explorer .esa-gof-fields{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
#esa-gof-explorer label{display:block;font-weight:650;margin-bottom:8px}
#esa-gof-explorer textarea{box-sizing:border-box;display:block;min-width:0;width:100%;padding:10px;resize:vertical;font:inherit;color:var(--text);background:var(--surface);border:1px solid var(--border);border-radius:8px}
#esa-gof-explorer .esa-gof-controls{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0}
#esa-gof-explorer [hidden]{display:none!important}
#esa-gof-explorer #esa-gof-error{color:#b42318;font-weight:650}
#esa-gof-explorer svg{display:block;width:100%;height:auto;max-width:560px}
#esa-gof-explorer :is(textarea,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-long-math{max-width:100%;overflow-x:auto;direction:ltr}
@media(max-width:650px){#esa-gof-explorer .esa-gof-fields{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/chi-square-gof-explorer.js"></script>
