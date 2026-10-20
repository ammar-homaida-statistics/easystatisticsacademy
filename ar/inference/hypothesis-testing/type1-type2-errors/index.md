---
layout: default
title: أخطاء النوع الأول والنوع الثاني في اختبار الفرضيات
description: درس عربي متكامل في خطأ النوع الأول وخطأ النوع الثاني ومستوى المعنوية والقوة الإحصائية مع محاكاة تفاعلية قابلة لإعادة الإنتاج.
permalink: /ar/inference/hypothesis-testing/type1-type2-errors/
lang: ar
sidebar: false
translation_pair: type1-type2-errors
math: true
---
<!-- Restrict all wide mathematical material and tables to their own scrollable sections. -->
<style>
@media(max-width:760px){
 #main-content .content-narrow{width:100%;max-width:100%;min-width:0;overflow-x:clip}
 #main-content .content-narrow .table-wrap{display:block;width:100%;max-width:100%;min-width:0;overflow-x:auto;overscroll-behavior-x:contain}
 #main-content .content-narrow .table-wrap table{display:table;width:max-content;min-width:640px;max-width:none;overflow:visible;white-space:normal}
}
</style>
<section class="hero hero-section"><div class="hero-card">
 <div class="badge-row"><span class="badge">الاستدلال الإحصائي</span><span class="badge">اختبار الفرضيات</span><span class="badge">مخاطر القرار</span></div>
 <h1>أخطاء النوع الأول والنوع الثاني</h1>
 <p><a href="/inference/hypothesis-testing/type1-type2-errors/" lang="en" dir="ltr">English — Type I and Type II Errors</a></p>
 <p class="lead">يُبنى القرار الإحصائي على عينة محدودة، ولذلك قد نرفض فرضية عدم صحيحة أو نفشل في رفض فرضية عدم خاطئة. يساعد فهم هذين الخطأين على تصميم الدراسات وتفسير الأدلة بدقة.</p>
 <div class="hero-actions"><a class="btn btn-outline" href="/ar/">الدروس العربية</a><a class="btn" href="/inference/hypothesis-testing/significance-level-alpha/" lang="en" dir="ltr">Previous (English)</a><a class="btn btn-outline" href="/inference/hypothesis-testing/power-and-effect-size/" lang="en" dir="ltr">Next: Power and Effect Size (English)</a></div>
</div></section>
<section><div class="content-narrow">
<h2>لماذا لا يمكن تفادي الأخطاء بالكامل؟</h2>
<p>لا نلاحظ المجتمع الإحصائي كله عادةً، بل نسحب عينة تخضع للتقلب العشوائي. حتى عندما تكون طريقة الاختبار صحيحة وافتراضاتها مستوفاة، فقد تؤدي المعاينة إلى قرار غير مطابق للحقيقة.</p>
<div class="concept-box"><strong>الفكرة الأساسية:</strong><p>الاختبار الإحصائي أداة لاتخاذ قرار في ظل عدم اليقين، وليس ضماناً للوصول إلى الحقيقة في كل تجربة.</p></div>
<h2>الحالتان الممكنتان في الواقع</h2>
<p>إما أن تكون فرضية العدم <span dir="ltr">H₀</span> صحيحة، وإما أن تكون خاطئة. وفي التطبيق لا نعرف مسبقاً أي الحالتين هي الصحيحة.</p>
<h2>القراران الممكنان</h2>
<p>يؤدي الاختبار إلى أحد قرارين: <strong>رفض فرضية العدم</strong> أو <strong>عدم رفضها</strong>. وعدم الرفض لا يساوي إثبات صحتها.</p>
<h2>جدول القرارات والأخطاء</h2>
<div class="table-wrap"><table><thead><tr><th>الحقيقة</th><th>رفض فرضية العدم</th><th>عدم رفض فرضية العدم</th></tr></thead>
<tbody><tr><th scope="row">فرضية العدم صحيحة</th><td>خطأ من النوع الأول</td><td>قرار صحيح</td></tr><tr><th scope="row">فرضية العدم خاطئة</th><td>كشف صحيح للأثر</td><td>خطأ من النوع الثاني</td></tr></tbody></table></div>
<p>من أصل أربع حالات محتملة للواقع والقرار، حالتان صحيحتان وحالتان تمثلان أخطاء إحصائية.</p>
<h2>الخطأ من النوع الأول</h2>
<div class="concept-box"><strong>التعريف:</strong> رفض فرضية عدم صحيحة، أي اكتشاف أثر لا وجود له وفق النموذج المفترض.</div>
<h2>أمثلة على الخطأ من النوع الأول</h2>
<p>قد نستنتج أن دواءً فعال رغم عدم وجود أثر حقيقي، أو أن عملية صناعية تغيرت رغم ثباتها، أو أن تعديلاً على موقع إلكتروني حسّن الأداء مع أن التحسن المرصود ناجم عن الصدفة.</p>
<h2>احتمال الخطأ من النوع الأول</h2>
<p>إذا صُمّم الاختبار بحيث يكون مستوى المعنوية <span dir="ltr">α</span>، فإن احتمال رفض فرضية العدم الصحيحة لا يزيد على <span dir="ltr">α</span> عند جميع قيم المعلمة المسموح بها في فرضية العدم:</p>
<div class="esa-math-ltr" dir="ltr">\[
\sup_{\theta\in\Theta_0}P_{\theta}(\text{reject }H_0)\le\alpha.
\]</div>
<p>إذا كان مستوى المعنوية <span dir="ltr">α = 0.05</span>، فإن معدل الخطأ من النوع الأول لا يتجاوز <span dir="ltr">5%</span> بشرط معايرة الاختبار بصورة صحيحة. وقد يتحقق التساوي في الاختبارات ذات الحجم الدقيق، بينما يكون الاحتمال أصغر في الاختبارات المتحفظة أو المنفصلة.</p>
<h2>الخطأ من النوع الثاني</h2>
<div class="concept-box"><strong>التعريف:</strong> عدم رفض فرضية عدم خاطئة، أي عدم الكشف عن أثر موجود بالفعل.</div>
<h2>أمثلة على الخطأ من النوع الثاني</h2>
<p>مثل عدم اكتشاف أثر علاجي حقيقي، أو إغفال مشكلة فعلية في السلامة الصناعية، أو عدم رصد فرق موجود بين طريقتين للتعليم.</p>
<h2>احتمال الخطأ من النوع الثاني</h2>
<p>يرمز له بـ <span dir="ltr">β(θ)</span>، وهو يعتمد على قيمة المعلمة المحددة ضمن البديل:</p>
<div class="esa-math-ltr" dir="ltr">\[
\beta(\theta)=P_{\theta}(\text{fail to reject }H_0),\qquad\theta\in\Theta_1.
\]</div>
<p>ويتأثر احتمال الخطأ من النوع الثاني بحجم العينة، وتباين القياسات، وحجم الأثر، ومستوى المعنوية، وطبيعة الاختبار وافتراضاته.</p>
<h2>لماذا يكون الخطأ من النوع الثاني أعقد؟</h2>
<p>يمكن تحديد مستوى الخطأ من النوع الأول في ظل فرضية العدم، أما <span dir="ltr">β(θ)</span> فيختلف باختلاف مقدار ابتعاد المعلمة الفعلية عن القيم الواردة في فرضية العدم؛ لذلك لا يوجد عادةً رقم ثابت واحد يعبّر عن هذا الاحتمال لجميع البدائل.</p>
<h2>تشبيه باستخدام الاختبارات الطبية</h2>
<div class="table-wrap"><table><thead><tr><th>المفهوم الإحصائي</th><th>التشبيه الطبي</th></tr></thead>
<tbody><tr><td>خطأ النوع الأول</td><td>الحكم خطأً بوجود مرض لدى شخص سليم</td></tr><tr><td>خطأ النوع الثاني</td><td>عدم الكشف عن المرض لدى شخص مصاب</td></tr></tbody></table></div>
<p>هذا تشبيه تعليمي للقرار الخاطئ، ولا يعني أن اختبار الفرضيات واختبار التشخيص الطبي لهما النموذج الاحتمالي نفسه.</p>
<h2>المفاضلة بين الخطأين</h2>
<p>إذا خفضنا مستوى المعنوية من <span dir="ltr">0.05</span> إلى <span dir="ltr">0.01</span>، تصبح قاعدة الرفض أكثر صرامة:</p>
<div class="esa-math-ltr" dir="ltr">\[\alpha:\ 0.05\longrightarrow0.01.\]</div>
<p>مع حجم عينة ثابت ومناطق رفض متداخلة، لا يزيد هذا الإجراء الخطأ من النوع الأول، لكنه قد يزيد احتمال الخطأ من النوع الثاني عند بديل معين. أما زيادة حجم العينة أو تحسين تصميم الدراسة فقد يخفف الخطأين دون الالتزام بمفاضلة جامدة.</p>
<section class="concept-box" id="esa-errors-lab" aria-labelledby="esa-errors-title" style="min-width:0;max-width:100%;overflow-x:hidden;overflow-wrap:anywhere">
<h2 id="esa-errors-title">مختبر تفاعلي لمحاكاة أخطاء النوع الأول والثاني</h2>
<p>يقارن المختبر بين <strong>1000 تجربة مستقلة تكون فيها فرضية العدم صحيحة</strong> و<strong>1000 تجربة مستقلة يكون فيها بديل محدد صحيحاً</strong>. نفترض مشاهدات مستقلة من توزيع طبيعي <span dir="ltr">N(μ,1)</span> وانحرافاً معيارياً مجتمعياً معروفاً يساوي 1، ونختبر <span dir="ltr">H₀: μ = 0</span> باستخدام <strong>اختبار Z ثنائي الطرف</strong>. في حالة البديل <span dir="ltr">μ = Δ &gt; 0</span>.</p>
<p>تُولَّد إحصائية متوسط العينة المعياري من توزيعها الطبيعي الدقيق، وهو مكافئ لتوليد <span dir="ltr">n</span> قيماً طبيعية مستقلة وحساب متوسطها. نرفض فرضية العدم عندما تتجاوز القيمة المطلقة لإحصائية الاختبار القيمة الحرجة الثنائية.</p>
<div style="display:flex;flex-wrap:wrap;gap:1rem;align-items:end">
<label for="esa-errors-n">حجم العينة
<select id="esa-errors-n"><option value="10">10</option><option value="30" selected>30</option><option value="100">100</option></select></label>
<label for="esa-errors-effect">الفرق الحقيقي في المتوسطات (σ = 1)
<select id="esa-errors-effect"><option value="0.2">0.2</option><option value="0.5" selected>0.5</option><option value="1">1.0</option></select></label>
<label for="esa-errors-alpha">مستوى المعنوية ثنائي الطرف
<select id="esa-errors-alpha"><option value="0.01">0.01</option><option value="0.05" selected>0.05</option><option value="0.10">0.10</option></select></label>
<label for="esa-errors-seed">بذرة المحاكاة القابلة لإعادة الإنتاج
<input id="esa-errors-seed" type="number" min="1" max="2147483647" step="1" value="2026" inputmode="numeric" dir="ltr" style="max-width:11rem"></label>
<button id="esa-errors-run" class="btn" type="button">نفّذ 2000 اختبار</button>
<button id="esa-errors-reset" class="btn btn-outline" type="button">إعادة القيم الأصلية</button>
</div>
<p id="esa-errors-status" role="status" aria-live="polite"></p>
<div class="table-wrap" style="width:100%;max-width:100%;min-width:0;overflow-x:auto"><table>
<caption>نتائج <span id="esa-errors-n-rep">1000</span> اختبار عند كل حالة</caption>
<thead><tr><th>الحقيقة</th><th>رفض فرضية العدم</th><th>عدم رفضها</th></tr></thead>
<tbody><tr><th scope="row">العدم صحيح (μ = 0)</th><td>خطأ نوع أول: <output id="esa-errors-fp">—</output></td><td>قرار صحيح: <output id="esa-errors-tn">—</output></td></tr>
<tr><th scope="row">البديل صحيح (μ = Δ)</th><td>كشف صحيح: <output id="esa-errors-tp">—</output></td><td>خطأ نوع ثانٍ: <output id="esa-errors-fn">—</output></td></tr></tbody></table></div>
<div class="table-wrap" style="width:100%;max-width:100%;min-width:0;overflow-x:auto"><table>
<caption>الاحتمالات النظرية ومعدلات المحاكاة</caption>
<thead><tr><th>المقياس</th><th>القيمة النظرية الدقيقة</th><th>معدل المحاكاة</th></tr></thead>
<tbody><tr><td>خطأ النوع الأول</td><td><output id="esa-errors-alpha-theory">—</output></td><td><output id="esa-errors-alpha-empirical">—</output></td></tr>
<tr><td>القوة الإحصائية عند البديل المحدد</td><td><output id="esa-errors-power-theory">—</output></td><td><output id="esa-errors-power-empirical">—</output></td></tr>
<tr><td>خطأ النوع الثاني عند البديل المحدد</td><td><output id="esa-errors-beta-theory">—</output></td><td><output id="esa-errors-beta-empirical">—</output></td></tr></tbody></table></div>
<p>في حالة البديل المحدد، يكون متوسط إحصائية الاختبار المعيارية مساوياً <span dir="ltr">Δ√n</span> وتباينها يساوي 1؛ وبالتالي فإن القوة النظرية:</p>
<div class="esa-math-ltr" dir="ltr" role="region" aria-label="معادلة القوة النظرية قابلة للتمرير أفقياً" tabindex="0" style="display:block;max-width:100%;min-width:0;overflow-x:auto">
\[
1-\Phi(z_{1-\alpha/2}-\Delta\sqrt{n})+
\Phi(-z_{1-\alpha/2}-\Delta\sqrt{n}).
\]
</div>
<p>يساوي احتمال خطأ النوع الثاني واحداً ناقص القوة الإحصائية. وتتذبذب المعدلات المحاكية حول القيم النظرية بسبب العشوائية. لا يعني عدم الرفض إثبات فرضية العدم. لا يغطي النموذج العينات التابعة أو الانحراف المعياري المجهول أو التوقف الاختياري أو الاختبارات المتعددة أو سوء تحديد النموذج.</p>
</section>
<h2>كيف يساعد حجم العينة؟</h2>
<p>يساعد ازدياد حجم العينة غالباً على تقليل عدم اليقين وتسهيل اكتشاف الأثر الحقيقي، وبالتالي قد يخفض خطأ النوع الثاني ويزيد القوة الإحصائية، بشرط ثبات افتراضات النموذج.</p>
<h2>تشبيه المحكمة</h2>
<div class="table-wrap"><table><thead><tr><th>المفهوم الإحصائي</th><th>مثال المحكمة</th></tr></thead>
<tbody><tr><td>خطأ النوع الأول</td><td>إدانة شخص بريء</td></tr><tr><td>خطأ النوع الثاني</td><td>تبرئة شخص مذنب</td></tr></tbody></table></div>
<p>يعكس التشبيه المفاضلة الأخلاقية والعملية بين نوعين مختلفين من الأخطاء، لكنه ليس مساواة بين الإجراءات القضائية والنماذج الإحصائية.</p>
<h2>أي الخطأين أشد ضرراً؟</h2>
<p>تعتمد الإجابة على المجال. فقد تُعطى أولوية لتجنب الادعاء بفاعلية علاج غير فعال، بينما قد تكون حساسية الكشف عن الأخطار أهم في بعض تطبيقات السلامة والفحص الأولي. ولا توجد أولوية عامة تصلح لجميع المواقف.</p>
<h2>العلاقة بالقوة الإحصائية</h2>
<p>القوة الإحصائية هي احتمال رفض فرضية عدم خاطئة عند بديل معين، وترتبط مباشرةً باحتمال خطأ النوع الثاني:</p>
<div class="esa-math-ltr" dir="ltr">\[
\operatorname{Power}(\theta)=P_{\theta}(\text{reject }H_0)
=1-\beta(\theta),\qquad\theta\in\Theta_1.
\]</div>
<p>يجب تقييم القوة واحتمال خطأ النوع الثاني عند قيمة البديل نفسها. كما أن عدم رفض فرضية العدم لا يثبت تساوي المعالجات؛ إذ يتطلب إثبات التكافؤ تصميماً مستقلاً وحدود تكافؤ محددة مسبقاً.</p>
<h2>الصورة العامة</h2>
<p>يقودنا فهم أخطاء النوع الأول والثاني إلى تقييم جودة القرارات بدلاً من النظر إلى النتيجة الإحصائية بوصفها حقيقة يقينية، كما يساعد على اختيار حجم العينة ومستوى المعنوية بما يلائم أهمية الأخطاء في الدراسة.</p>
<h2>الدرس التالي</h2>
<p>لفهم كيفية التخطيط لاحتمال اكتشاف أثر حقيقي، تابع درس <a href="/inference/hypothesis-testing/power-and-effect-size/" lang="en" dir="ltr">Power and Effect Size</a> بالإنجليزية.</p>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>خطأ النوع الأول: رفض فرضية عدم صحيحة.</li>
<li>خطأ النوع الثاني: عدم رفض فرضية عدم خاطئة.</li>
<li>مستوى المعنوية يضبط احتمالات الخطأ من النوع الأول وفق معايرة الاختبار.</li>
<li>تعتمد احتمالات الخطأ من النوع الثاني على البديل وحجم الأثر وتصميم الدراسة.</li>
<li>القوة الإحصائية عند بديل محدد تساوي واحداً ناقص احتمال الخطأ من النوع الثاني.</li>
<li>عدم رفض فرضية العدم لا يعني إثبات صحتها أو إثبات التكافؤ.</li>
</ul></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/">الدروس العربية</a><a class="btn" href="/inference/hypothesis-testing/type1-type2-errors/" lang="en" dir="ltr">English version</a></div>
</div></section>
<script src="/js/type1-type2-errors-lab.js" defer></script>
