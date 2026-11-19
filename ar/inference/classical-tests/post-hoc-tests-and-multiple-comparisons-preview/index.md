---
layout: default
title: الاختبارات اللاحقة والمقارنات المتعددة
description: "شرح عربي للاختبارات اللاحقة بعد تحليل التباين: معدل الخطأ العائلي، وتوكي–كريمر، وبونفيروني، وهولم، مع مختبرين تفاعليين."
permalink: /ar/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/
lang: ar
sidebar: false
learning_resource: true
translation_pair: post-hoc-tests
---
<section class="hero hero-section"><div class="hero-card">
<h1>الاختبارات اللاحقة والمقارنات المتعددة</h1>
{% include lab-noscript.html %}
<p class="lead">تخبرنا نتيجة تحليل التباين الدالة أن متوسط مجموعة واحدة على الأقل يختلف، لكنها لا تحدد أيّ المجموعات تختلف. تقدّم الإجراءات اللاحقة (Post-hoc) طريقة منهجية لفحص الفروق بين مجموعات بعينها مع ضبط خطر الاكتشافات الكاذبة.</p>
<p><a href="/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/classical-tests/one-way-anova-f-test/">الدرس السابق: تحليل التباين الأحادي</a></p>
</div></section>
<section><div class="content-narrow">
<h2>1. ما الذي لا يخبرنا به تحليل التباين؟</h2>
<p>إذا قارنّا أربع طرق تدريس A وB وC وD، فإن تحليل التباين الدال يقودنا إلى رفض الفرضية الصفرية المشتركة \(H_0:\mu_A=\mu_B=\mu_C=\mu_D\). لكنه لا يكشف:</p>
<ul class="bullets"><li>أيّ المجموعات تختلف؛</li><li>كم مجموعة تختلف؛</li><li>حجم تلك الفروق.</li></ul>
<p>لذلك نحتاج إلى تحليل إضافي.</p>
<h2>2. الإغراء: اختبارات t زوجية كثيرة</h2>
<p>الفكرة البسيطة هي إجراء اختبار t لكل زوج. ومع أربع مجموعات توجد ست مقارنات: A–B وA–C وA–D وB–C وB–D وC–D. لكن هذا يخلق مشكلة جديدة.</p>
<h2>3. مشكلة المقارنات المتعددة</h2>
<p>يحمل كل اختبار فرضية احتمال ارتكاب خطأ من النوع الأول. فإذا أُجري كل اختبار عند \(\alpha=0.05\)، فإن اختبار فرضيات صفرية صحيحة كثيرة قد يرفع احتمال نتيجة إيجابية كاذبة واحدة على الأقل. ويعتمد الاحتمال الدقيق على الاعتماد بين أحداث الرفض وعلى الأحجام الفعلية للاختبارات المفردة.</p>
<div class="concept-box"><strong>المسألة الأساسية:</strong><p>عند اختبار فرضيات صحيحة كثيرة قد يتجاوز احتمال نتيجة كاذبة واحدة أو أكثر مستوى الخطأ لكل اختبار. وإضافة اختبار لا يمكن أن تُنقص هذا الاحتمال، وإن كان الاعتماد بين الاختبارات قد يمنع زيادته زيادة فعلية.</p></div>
<h2>4. معدل الخطأ العائلي</h2>
<p>احتمال ارتكاب خطأ واحد أو أكثر من النوع الأول عبر عائلة من الاختبارات يسمى <strong>معدل الخطأ العائلي</strong> (Family-Wise Error Rate, FWER). وضبطه أحد الأهداف الرئيسة للإجراءات اللاحقة.</p>
<p>مثال توضيحي: لعشرين اختبارًا أحداثُ رفضها مستقلة تحت فرضياتها الصفرية الصحيحة، وحجم كل منها 0.05 تمامًا:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="معدل الخطأ العائلي لعشرين اختبارًا">
\[
P(\text{at least one false positive})=1-(1-0.05)^{20}=1-0.95^{20}\approx0.642 .
\]</div>
<p>أي نحو 64.2%. وتتطلب الصيغة \(1-(1-\alpha)^m\) استقلال أحداث الرفض وأحجامًا دقيقة كما ذُكر؛ فمستوى الاختبار الاسمي وحده لا يضمن هذه القيمة.</p>
<h2>5. ما الاختبارات اللاحقة؟</h2>
<div class="concept-box"><strong>تعريف:</strong><p>الاختبارات اللاحقة إجراءات متابعة تُجرى بعد اختبار شامل دال مثل تحليل التباين، وتحدد أيّ المقارنات بعينها دالة مع ضبط معدلات الخطأ الكلية.</p></div>
<div class="table-wrap"><table><caption>إجراءات لاحقة شائعة</caption><thead><tr><th scope="col">الإجراء</th><th scope="col">الغرض الرئيس</th></tr></thead><tbody>
<tr><td>توكي HSD</td><td>جميع المقارنات الزوجية</td></tr>
<tr><td>تصحيح بونفيروني</td><td>ضبط عام للخطأ</td></tr>
<tr><td>إجراء هولم</td><td>تحسين متدرّج لبونفيروني</td></tr>
<tr><td>طريقة شيفيه</td><td>تباينات (contrasts) مرنة</td></tr>
</tbody></table></div>
<h2>6. طريقة توكي للفروق الدالة حقًا (HSD)</h2>
<p>إجراء توكي من أكثر الطرق اللاحقة استخدامًا، وقد صُمّم خصيصًا لمقارنة <strong>جميع أزواج المتوسطات</strong> مع ضبط معدل الخطأ الكلي من النوع الأول.</p>

<!-- Batch #97: Tukey–Kramer HSD laboratory -->
<section class="concept-box" id="esa-tukey-lab" data-locale="ar" aria-labelledby="esa-tukey-heading">
<h2 id="esa-tukey-heading">مختبر توكي–كريمر التفاعلي (HSD)</h2>
<p>يقارن إجراء توكي كل زوج من متوسطات \(k\) مجموعات باستخدام إحصائية <strong>المدى المعياري</strong> (Studentized range). وللمجموعتين \(i\) و\(j\) (صيغة توكي–كريمر للأحجام غير المتساوية):</p>
<div class="esa-tukey-math" dir="ltr" tabindex="0" role="region" aria-label="صيغ توكي–كريمر">
\[
q_{ij}=\frac{|\bar x_i-\bar x_j|}{\sqrt{\dfrac{MS_W}{2}\left(\dfrac1{n_i}+\dfrac1{n_j}\right)}},\qquad
p_{ij}=P\!\left(Q_{k,\,N-k}\ge q_{ij}\right),\qquad
(\bar x_i-\bar x_j)\pm q_{1-\alpha;\,k,\,N-k}\sqrt{\dfrac{MS_W}{2}\left(\dfrac1{n_i}+\dfrac1{n_j}\right)} .
\]</div>
<p>أدخل كل مجموعة في سطر، وافصل القيم بفواصل إنجليزية. البيانات الافتراضية هي مثال درس تحليل التباين (F = 13 وp = 0.006592).</p>
<label for="esa-tukey-input">المجموعات (مجموعة في كل سطر، من 2 إلى 6 مجموعات)</label>
<textarea id="esa-tukey-input" dir="ltr" rows="4" spellcheck="false" aria-invalid="false" aria-describedby="esa-tukey-error">4, 5, 6
5, 6, 7
8, 9, 10</textarea>
<div class="esa-tukey-controls"><button class="btn btn-outline" type="button" id="esa-tukey-example">مثال تحليل التباين</button><button class="btn btn-outline" type="button" id="esa-tukey-unequal">أحجام مجموعات غير متساوية</button><button class="btn btn-outline" type="button" id="esa-tukey-four">أربع مجموعات</button></div>
<p id="esa-tukey-error" role="alert" hidden></p>
<section id="esa-tukey-results" aria-label="نتائج توكي–كريمر" role="status" aria-live="polite" aria-atomic="true">
<p>عدد المجموعات k = <output id="esa-tukey-k" dir="ltr">3</output> · درجات حرية الخطأ = <output id="esa-tukey-nu" dir="ltr">6</output> · MSW = <output id="esa-tukey-msw" dir="ltr">1.000000</output> · القيمة الحرجة q₀.₉₅ = <output id="esa-tukey-qcrit" dir="ltr">4.3392</output></p>
<div class="table-wrap"><table><caption>جميع المقارنات الزوجية مع فترات ثقة متزامنة 95%</caption>
<thead><tr><th scope="col">الزوج</th><th scope="col">الفرق</th><th scope="col">q</th><th scope="col">p المعدّلة</th><th scope="col">فترة ثقة متزامنة 95%</th><th scope="col">عند α = 0.05</th></tr></thead>
<tbody id="esa-tukey-rows" dir="ltr"></tbody></table></div>
<p id="esa-tukey-summary"></p>
</section>
<p class="muted-mini">يساوي معدل الخطأ العائلي α تمامًا عند تساوي أحجام المجموعات، ولا يتجاوز α عند عدم تساويها (Hayter, 1984)، بافتراض أخطاء مستقلة طبيعية متساوية التباين. ومع مجموعتين تساوي قيمة توكي الاحتمالية قيمةَ اختبار t لعينتين بالتباين المشترك. تُحسب احتمالات المدى المعياري في متصفحك بالتكامل العددي.</p>
</section>
<style>
#esa-tukey-lab,#esa-tukey-lab *{box-sizing:border-box}
#esa-tukey-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-tukey-lab label{display:block;font-weight:650;margin:10px 0 5px}
#esa-tukey-lab textarea{display:block;width:100%;min-width:0;font:inherit;padding:10px;border:1px solid #777;border-radius:6px}
#esa-tukey-lab .esa-tukey-controls{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
#esa-tukey-lab .table-wrap,.esa-tukey-math{max-width:100%;overflow-x:auto}
.esa-tukey-math{direction:ltr}
#esa-tukey-lab [hidden]{display:none!important}
#esa-tukey-lab :is(textarea,button):focus-visible,.esa-tukey-math:focus-visible{outline:2px solid #0f766e;outline-offset:3px}
</style>
<script defer src="/js/tukey-hsd-lab.js"></script>

<h2>7. فكرة بونفيروني</h2>
<p>يوزّع تصحيح بونفيروني المستوى العائلي المطلوب \(\alpha\) على \(m\) اختبارًا محددة مسبقًا. فإجراء كل اختبار عند المستوى \(\alpha/m\) يضبط الخطأ العائلي عند \(\alpha\) أو دونه ما دام كل اختبار صحيحًا. ويأتي ذلك من متباينة الاتحاد (Union bound)، ولا يتطلب استقلال الاختبارات:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="عتبة بونفيروني">
\[
\alpha_{\mathrm{Bonferroni}}=\frac{\alpha}{m},
\]</div>
<p>حيث \(\alpha\) معدل الخطأ العائلي المطلوب، و\(m\) عدد المقارنات.</p>
<section class="concept-box" id="esa-multiple-comparisons-lab" data-locale="ar" aria-labelledby="esa-mc-heading">
<h2 id="esa-mc-heading">مختبر المقارنات المتعددة: بونفيروني وهولم</h2>
<p>أدخل <strong>عائلة محددة مسبقًا من 2 إلى 12 قيمة احتمالية صحيحة</strong>، وقارن القرارات غير المعدّلة بقيم بونفيروني وقيم هولم المتدرّجة. تبقى الفرضيات بترتيب إدخالها؛ يرتّب إجراء هولم القيم داخليًا ثم يعيد الترتيب الأصلي.</p>
<div class="esa-mc-grid">
<div><label for="esa-mc-values">القيم الاحتمالية (مفصولة بفواصل أو مسافات أو أسطر)</label>
<textarea id="esa-mc-values" dir="ltr" rows="3" spellcheck="false">0.003, 0.018, 0.041, 0.22</textarea></div>
<div><label for="esa-mc-alpha">مستوى الدلالة العائلي α (بين 0 و1)</label>
<input id="esa-mc-alpha" dir="ltr" type="number" min="0" max="1" step="any" value="0.05"></div>
</div>
<button class="btn btn-outline" type="button" id="esa-mc-reset">إعادة المثال</button>
<p id="esa-mc-error" role="alert" hidden></p>
<section id="esa-mc-results" aria-live="polite" aria-label="القيم الاحتمالية المعدّلة للمقارنات المتعددة">
<p>عدد الاختبارات: <strong id="esa-mc-count" dir="ltr">4</strong>.</p>
<div class="table-wrap"><table><caption>التعديلات لكل مقارنة وللعائلة (ست منازل عشرية)</caption>
<thead><tr><th scope="col">الاختبار</th><th scope="col">p الأصلية</th><th scope="col">p بونفيروني</th><th scope="col">p هولم</th><th scope="col">القرار دون تعديل</th><th scope="col">بونفيروني</th><th scope="col">هولم</th></tr></thead>
<tbody id="esa-mc-rows"></tbody>
</table></div>
<svg id="esa-mc-chart" role="img" viewBox="0 0 610 265" dir="ltr" style="display:block;width:100%;height:auto" aria-label="القيم الاحتمالية غير المعدّلة وقيم بونفيروني وهولم"></svg>
<p><strong>مفتاح الألوان:</strong> <span style="color:#a16207">دون تعديل</span> · <span style="color:#2563eb">بونفيروني</span> · <span style="color:#0f766e">هولم</span>. الخط الأحمر المتقطع يمثل α.</p>
<p><strong>رفض خاطئ واحد على الأقل عبر m اختبارًا:</strong> إذا كانت جميع الفرضيات الصفرية صحيحة والاختبارات مستقلة، فالاحتمال النظري دون تعديل هو <strong id="esa-mc-fwer" dir="ltr">—</strong> (= 1−(1−α)ᵐ). وهذا <em>ليس</em> تقديرًا من القيم المُدخلة.</p>
<p>ومتباينة الاتحاد، الصحيحة دون افتراض الاستقلال، تجعله لا يتجاوز <strong id="esa-mc-bound" dir="ltr">—</strong> (= min(1,mα)) عندما لا يتجاوز حجم كل اختبار صفري صحيح α.</p>
<p id="esa-mc-summary"></p>
</section>
<p class="muted-mini">قيم هولم المعدّلة هي القيم العظمى التراكمية لـ (m−j+1)p₍ⱼ₎ بعد الترتيب، بحد أقصى 1. ويستخدم بونفيروني min(1,mp). يضبط الإجراءان معدل الخطأ العائلي لعائلة محددة مسبقًا من القيم الاحتمالية الصحيحة مهما كان الاعتماد بينها. ويُفترض الاستقلال <em>فقط</em> في الصيغة التوضيحية 1−(1−α)ᵐ. القيم الاحتمالية لا تقيس حجم الأثر.</p>
</section>
<style>
#esa-multiple-comparisons-lab,#esa-multiple-comparisons-lab *{box-sizing:border-box}
#esa-multiple-comparisons-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-multiple-comparisons-lab .esa-mc-grid{display:grid;grid-template-columns:minmax(0,2fr) minmax(180px,1fr);gap:12px;margin:14px 0}
#esa-multiple-comparisons-lab label{display:block;font-weight:650;margin-bottom:5px}
#esa-multiple-comparisons-lab :is(textarea,input){font:inherit;width:100%;min-width:0;padding:10px;border:1px solid #777;border-radius:6px}
#esa-multiple-comparisons-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-multiple-comparisons-lab [hidden]{display:none!important}
#esa-multiple-comparisons-lab :is(textarea,input,button):focus-visible{outline:2px solid #0f766e;outline-offset:3px}
@media(max-width:600px){#esa-multiple-comparisons-lab .esa-mc-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/multiple-comparisons-explorer.js"></script>
<h2>8. المفاضلة بين الخطأ والقوة</h2>
<p>مع تصميم ثابت واختبارات متماثلة، كثيرًا ما يُنقص الضبطُ الأشد للخطأ العائلي فرصةَ اكتشاف فرق حقيقي. وقد تغيّر التصاميم أو أحجام العينات الأخرى هذه المفاضلة.</p>
<div class="table-wrap"><table><caption>الضبط المتساهل مقابل الضبط الصارم</caption><thead><tr><th scope="col">النهج</th><th scope="col">الخطأ من النوع الأول</th><th scope="col">القوة</th></tr></thead><tbody>
<tr><td>ضبط متساهل</td><td>أعلى</td><td>أعلى</td></tr><tr><td>ضبط صارم</td><td>أقل</td><td>أقل</td></tr></tbody></table></div>
<p>ولهذا يتضمن اختيار الإجراء موازنة بين هذين الهدفين. ويُعدّ هولم أقوى من بونفيروني دائمًا أو مساويًا له مع ضبط الخطأ العائلي نفسه، أما توكي فهو الأقوى عادة لمقارنة جميع الأزواج تحت افتراضات تحليل التباين.</p>
<h2>9. المقارنات المخططة مقابل اللاحقة</h2>
<p>بعض المقارنات تُحدَّد قبل جمع البيانات، وتسمى <strong>مقارنات مخططة</strong> (Planned). وبعضها يُختار بعد فحص النتائج، وهي <strong>المقارنات اللاحقة</strong>. وتحتاج التحليلات اللاحقة عادة إلى ضبط أشد للخطأ لأنها موجّهة بالبيانات.</p>
<h2>10. حجم الأثر ما زال مهمًا</h2>
<p>الدلالة الإحصائية لا تعني تلقائيًا أهمية عملية. فبعد تحديد الفروق الدالة يقيّم الباحثون عادة فروق المتوسطات وفترات الثقة ومقاييس حجم الأثر، وهي التي تساعد في الحكم على الأهمية العملية. وتقدّم فترات توكي المتزامنة في المختبر أعلاه حجم كل فرق ودقته معًا.</p>
<h2>11. الصورة الأشمل</h2>
<p>تمتد أفكار المقارنات المتعددة إلى ما هو أبعد من تحليل التباين: التجارب السريرية، وعلم الجينوم، واختبارات A/B، والتجارب واسعة النطاق، وتقييم نماذج تعلم الآلة. فكلما اختُبرت فرضيات كثيرة في آن واحد صار التعدد مسألة مهمة.</p>
<div class="concept-box"><strong>الرسالة الأساسية:</strong><p>الاختبارات اللاحقة إجراءات متابعة بعد اختبارات شاملة دالة مثل تحليل التباين، تحدد فروقًا بعينها بين المجموعات مع ضبط الخطر المتزايد لأخطاء النوع الأول الناتج عن المقارنات المتعددة.</p></div>
<h2>12. إكمال وحدة الاختبارات الكلاسيكية</h2>
<p>أكملت الآن إجراءات اختبار الفرضيات الكلاسيكية الرئيسة في الاستدلال الإحصائي التمهيدي. وتتناول الوحدة التالية تحليل القوة وتحديد حجم العينة، وهي أدوات تساعد في تصميم الدراسات قبل جمع البيانات.</p>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>يكشف تحليل التباين وجود فروق، لكنه لا يحدد أيّ المجموعات تختلف.</li>
<li>تزيد المقارنات المتعددة خطر أخطاء النوع الأول.</li>
<li>يقيس معدل الخطأ العائلي خطر النتائج الإيجابية الكاذبة الكلي.</li>
<li>تضبط الإجراءات اللاحقة معدلات الخطأ أثناء تحديد الفروق بعينها.</li>
<li>توكي وبونفيروني وهولم وشيفيه مقاربات شائعة.</li>
<li>الضبط الأشد للخطأ يُنقص القوة الإحصائية غالبًا.</li>
<li>المقارنات المخططة تختلف عن المقارنات اللاحقة.</li>
<li>ينبغي أن يشمل التفسير العملي أحجام الأثر وفترات الثقة.</li>
</ul></div>
<div class="lesson-nav">
<a class="btn btn-outline" href="/ar/inference/classical-tests/one-way-anova-f-test/">→ السابق: تحليل التباين الأحادي</a>
<a class="btn" href="/ar/inference/classical-tests/">العودة إلى الاختبارات الكلاسيكية ←</a>
</div>
</div></section>
