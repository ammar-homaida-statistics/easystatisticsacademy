---
layout: default
title: نظرية بايز
description: درس عربي شامل في نظرية بايز والاحتمال الشرطي والاحتمالات الأولية واللاحقة، مع مختبر تفاعلي للحساسية والنوعية وأثر معدل الانتشار.
permalink: /ar/probability/conditional/bayes-theorem/
lang: ar
sidebar: false
translation_pair: bayes-theorem
math: true
---
<section class="hero hero-section"><div class="hero-card">
  <div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">الاحتمال الشرطي</span><span class="badge">التفكير البايزي</span></div>
  <h1>نظرية بايز</h1>
  <p><a href="/probability/conditional/bayes-theorem/" lang="en" dir="ltr">English — Bayes' Theorem</a></p>
  <p class="lead">تتيح نظرية بايز تحديث احتمال حدث معين عند ظهور دليل جديد، وتوضح الفرق بين احتمال الدليل في ظل سبب معين واحتمال ذلك السبب بعد مشاهدة الدليل.</p>
  <div class="hero-actions">
    <a class="btn btn-outline" href="/ar/">الدروس العربية</a>
    <a class="btn" href="/probability/conditional/law-of-total-probability/" lang="en" dir="ltr">Previous (English)</a>
    <a class="btn btn-outline" href="/probability/conditional/tree-diagrams/" lang="en" dir="ltr">Next: Tree Diagrams (English)</a>
  </div>
</div></section>
<section><div class="content-narrow">
<h2>السؤال الأساسي</h2>
<p>قد نعرف احتمال الحصول على نتيجة إيجابية إذا كان الشخص مصاباً بحالة معينة، لكننا نرغب في معرفة احتمال وجود الحالة إذا ظهرت نتيجة إيجابية. السؤالان مختلفان: الأول يشترط وجود الحالة، والثاني يشترط ظهور النتيجة.</p>
<div class="concept-box"><strong>الفكرة الأساسية:</strong><p>تربط نظرية بايز بين الاتجاهين باستخدام الاحتمال الأولي واحتمال الدليل.</p></div>
<h2>لماذا نحتاج إلى نظرية بايز؟</h2>
<p>الاحتمالات الشرطية ليست قابلة للعكس مباشرةً. عموماً يختلف احتمال وقوع الدليل عند تحقق السبب عن احتمال تحقق السبب عند ملاحظة الدليل. ولا يمكن استنتاج أحدهما من الآخر دون معلومات إضافية عن معدلات الحدوث.</p>
<h2>تذكير بالاحتمال الشرطي</h2>
<p>للحدثين <span dir="ltr">A</span> و<span dir="ltr">B</span>، وعندما يكون احتمال الحدث المشروط عليه موجباً:</p>
<div class="esa-math-ltr" dir="ltr">
\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)},\quad P(B)>0,
\qquad
P(B\mid A)=\frac{P(A\cap B)}{P(A)},\quad P(A)>0.
\]
</div>
<p>يمثل البسط في العبارتين احتمال تقاطع الحدثين نفسه، بينما يختلف المقام باختلاف الحدث المشروط عليه.</p>
<h2>اشتقاق نظرية بايز</h2>
<p>نستخدم قاعدة الضرب لاحتمال التقاطع ثم نعوضها في تعريف الاحتمال الشرطي:</p>
<div class="esa-math-ltr" dir="ltr">
\[
P(A\cap B)=P(B\mid A)P(A),\qquad
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)},\quad P(B)>0.
\]
</div>
<h2>صيغة بايز وتفسير عناصرها</h2>
<div class="esa-math-ltr" dir="ltr">
\[
\underbrace{P(A\mid B)}_{\text{posterior}}
=\frac{\overbrace{P(B\mid A)}^{\text{likelihood}}\,
\overbrace{P(A)}^{\text{prior}}}
{\underbrace{P(B)}_{\text{evidence}}}.
\]
</div>
<div class="table-wrap"><table>
<thead><tr><th>الرمز</th><th>المعنى</th></tr></thead>
<tbody>
<tr><td dir="ltr">P(A)</td><td>الاحتمال الأولي للحدث قبل مشاهدة الدليل</td></tr>
<tr><td dir="ltr">P(B | A)</td><td>احتمال مشاهدة الدليل إذا تحقق الحدث</td></tr>
<tr><td dir="ltr">P(B)</td><td>الاحتمال الكلي لظهور الدليل</td></tr>
<tr><td dir="ltr">P(A | B)</td><td>الاحتمال اللاحق للحدث بعد مشاهدة الدليل</td></tr>
</tbody></table></div>
<h2>كيف يجري التحديث البايزي؟</h2>
<p>نبدأ باحتمال أولي مستند إلى المعرفة السابقة أو الإحصاءات المتاحة، ثم نراعي قوة ارتباط الدليل بالحدث، ونقسم على الاحتمال الكلي للدليل لنحصل على الاحتمال اللاحق. لا تعني عملية التحديث أن الاحتمال اللاحق أكبر دائماً؛ فقد يزيد أو ينقص وفق الدليل.</p>
<h2>مثال توضيحي على الاختبارات</h2>
<p>لنفترض أن معدل انتشار حالة افتراضية يساوي <span dir="ltr">1%</span>، وحساسية الاختبار <span dir="ltr">95%</span>، وأن <strong>الاحتمال الكلي للنتائج الإيجابية في المجتمع</strong> يساوي <span dir="ltr">5%</span>. الرقم الأخير ليس معدل النتائج الإيجابية الكاذبة.</p>
<p>إذا رمزنا للحالة بالرمز <span dir="ltr">D</span> وللنتيجة الإيجابية بالرمز <span dir="ltr">+</span>، فإن:</p>
<div class="esa-math-ltr" dir="ltr">
\[
P(D\mid +)=\frac{P(+\mid D)P(D)}{P(+)}
=\frac{0.95\times0.01}{0.05}=0.19=19\%.
\]
</div>
<p>إذن الاحتمال اللاحق عند ظهور نتيجة إيجابية هو <span dir="ltr">19%</span> في هذا المثال، ولا يساوي حساسية الاختبار البالغة <span dir="ltr">95%</span>. ولكي تتسق هذه المعطيات، فإن احتمال النتيجة الإيجابية لدى غير المصابين يساوي:</p>
<div class="esa-math-ltr" dir="ltr">
\[
P(+\mid D^c)=\frac{0.05-0.95(0.01)}{0.99}
\approx0.0409=4.09\%.
\]
</div>
<p>لاحظ الفرق بين الاحتمال الكلي للإيجابية <span dir="ltr">5%</span> ومعدل الإيجابيات الكاذبة المشروط بعدم وجود الحالة <span dir="ltr">4.09%</span>.</p>
<section class="concept-box" id="esa-bayes-lab" aria-labelledby="esa-bayes-title" style="min-width:0;overflow-wrap:anywhere">
  <h2 id="esa-bayes-title">مختبر تفاعلي لنظرية بايز وأثر معدل الانتشار</h2>
  <p>غيّر معدل الانتشار والحساسية والنوعية في <strong>اختبار ثنائي افتراضي</strong>. يحسب المختبر احتمال وجود الحالة بعد النتيجة الإيجابية أو السلبية، إضافةً إلى التكرارات المتوقعة من بين عشرة آلاف فرد افتراضي. هذه أداة تعليمية وليست نصيحة طبية أو اختباراً سريرياً معتمداً.</p>
  <div style="display:flex;flex-wrap:wrap;gap:1rem;align-items:end">
    <label for="esa-bayes-prev">معدل الانتشار (%)
      <input id="esa-bayes-prev" type="number" min="0" max="100" step="any" value="1" inputmode="decimal" dir="ltr" style="max-width:9rem">
    </label>
    <label for="esa-bayes-sens">الحساسية (%)
      <input id="esa-bayes-sens" type="number" min="0" max="100" step="any" value="90" inputmode="decimal" dir="ltr" style="max-width:9rem">
    </label>
    <label for="esa-bayes-spec">النوعية (%)
      <input id="esa-bayes-spec" type="number" min="0" max="100" step="any" value="95" inputmode="decimal" dir="ltr" style="max-width:9rem">
    </label>
    <button id="esa-bayes-run" class="btn" type="button">احسب</button>
    <button id="esa-bayes-reset" class="btn btn-outline" type="button">إعادة المثال</button>
  </div>
  <p id="esa-bayes-status" role="status" aria-live="polite"></p>
  <p><strong>احتمال وجود الحالة بعد نتيجة إيجابية:</strong> <output id="esa-bayes-pos" dir="ltr">—</output></p>
  <p><strong>احتمال وجود الحالة بعد نتيجة سلبية:</strong> <output id="esa-bayes-neg" dir="ltr">—</output></p>
  <p><strong>الاحتمال الكلي للنتيجة الإيجابية:</strong> <output id="esa-bayes-plus-prob" dir="ltr">—</output>؛ <strong>وللنتيجة السلبية:</strong> <output id="esa-bayes-minus-prob" dir="ltr">—</output>.</p>
  <div class="table-wrap"><table>
    <caption>التكرارات المتوقعة من بين 10,000 فرد افتراضي (قد تكون كسوراً)</caption>
    <thead><tr><th>الحالة الفعلية</th><th>نتيجة إيجابية</th><th>نتيجة سلبية</th></tr></thead>
    <tbody>
      <tr><th scope="row">الحالة موجودة</th><td><output id="esa-bayes-tp" dir="ltr">—</output></td><td><output id="esa-bayes-fn" dir="ltr">—</output></td></tr>
      <tr><th scope="row">الحالة غير موجودة</th><td><output id="esa-bayes-fp" dir="ltr">—</output></td><td><output id="esa-bayes-tn" dir="ltr">—</output></td></tr>
    </tbody>
  </table></div>
  <p><strong>مثال التحقق:</strong> عندما يكون الانتشار <span dir="ltr">1%</span>، والحساسية <span dir="ltr">90%</span>، والنوعية <span dir="ltr">95%</span>، يكون:</p>
  <div class="esa-math-ltr" dir="ltr">\[P(D\mid+)=\frac{0.009}{0.009+0.0495}\approx15.38\%.\]</div>
  <p>لا تعني حساسية تبلغ <span dir="ltr">90%</span> أن <span dir="ltr">90%</span> من النتائج الإيجابية تدل على وجود الحالة.</p>
  <p><strong>حالة خاصة:</strong> إذا كان احتمال نتيجة ما صفراً، فإن الاحتمال الشرطي عليها <strong>غير معرّف</strong> وليس صفراً. يرفض المختبر النسب المدخلة خارج المجال من صفر إلى مئة. تنفذ الحسابات داخل المتصفح، ولا تُحفظ البيانات ولا تُرسل.</p>
</section>
<h2>الاحتمال الأولي</h2>
<p>يمثل الاحتمال الأولي المعلومات المتاحة قبل ظهور الدليل. وقد يستند إلى بيانات تاريخية أو دراسات سابقة أو إحصاءات المجتمع أو معرفة خبراء، وفق سياق المشكلة.</p>
<h2>دور احتمال الدليل</h2>
<p>يحدد احتمال ظهور دليل معين في ظل فرضية محددة مدى توافق الدليل مع هذه الفرضية. ويجب التمييز بين الاحتمال الشرطي للدليل واحتمال الفرضية بعد مشاهدة ذلك الدليل.</p>
<h2>الاحتمال اللاحق</h2>
<p>هو الاحتمال بعد استخدام البيانات الجديدة. لذلك يمكن تلخيص العملية: <strong>معلومات أولية + دليل جديد → احتمال مُحدَّث</strong>. لا يساوي هذا الاحتمال الأولي بالضرورة.</p>
<h2>أهمية معدلات الانتشار الأساسية</h2>
<p>إذا كانت الحالة نادرة، فقد يكون عدد النتائج الإيجابية الكاذبة كبيراً مقارنةً بعدد الإيجابيات الحقيقية، حتى مع حساسية ونوعية مرتفعتين نسبياً. ويُسمى تجاهل معدل الانتشار الأساسي عند التفسير «إهمال المعدل الأساسي».</p>
<h2>العلاقة بقانون الاحتمال الكلي</h2>
<p>عندما يقسم الحدث <span dir="ltr">D</span> المجتمع إلى حالتين متنافيتين وشاملتين، فإن:</p>
<div class="esa-math-ltr" dir="ltr">\[
P(+)=P(+\mid D)P(D)+P(+\mid D^c)P(D^c).
\]</div>
<p>توضح هذه الصيغة كيف يجمع احتمال النتيجة الإيجابية بين مساهمة من لديهم الحالة ومساهمة من ليست لديهم.</p>
<h2>تطبيقات نظرية بايز</h2>
<p>تستخدم النظرية في تحديث تقديرات المخاطر، والتشخيص الاحتمالي، وتصنيف البيانات، وتقييم الفرضيات، ودمج المعلومات في التعلم الآلي وعلوم القرار، مع مراعاة صلاحية النموذج والبيانات.</p>
<h2>خطأ شائع في التفسير</h2>
<p>لا يجوز استبدال <span dir="ltr">P(D | +)</span> بـ <span dir="ltr">P(+ | D)</span>. فالأول احتمال الحالة بعد إيجابية الاختبار، والثاني حساسية الاختبار عند وجود الحالة؛ وهما احتمالان مشروطان على حدثين مختلفين.</p>
<h2>الصورة العامة</h2>
<p>تجعل نظرية بايز الاحتمال إطاراً متجدداً للتعلم من المعلومات: نبدأ بتقدير أولي، ونراعي الدليل وكيف يمكن ظهوره، ثم نحسب احتمالاً لاحقاً متسقاً مع المعطيات.</p>
<h2>من بايز إلى المخططات الشجرية</h2>
<p>يمكن تمثيل المسارات التي تقود إلى الأدلة المختلفة باستخدام شجرة احتمالات، ما يساعد على تنظيم المسائل المتعددة المراحل. الدرس التالي بالإنجليزية: <a lang="en" dir="ltr" href="/probability/conditional/tree-diagrams/">Tree Diagrams</a>.</p>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>الاحتمالات الشرطية تختلف بحسب اتجاه الشرط.</li>
<li>تجمع نظرية بايز بين الاحتمال الأولي واحتمال الدليل لتحديث الاحتمال اللاحق.</li>
<li>يجب أن يكون احتمال الدليل الذي نقسم عليه أكبر من الصفر.</li>
<li>معدل الانتشار أساسي لتفسير النتائج الإيجابية والسلبية.</li>
<li>الاحتمال اللاحق لا يساوي حساسية الاختبار بالضرورة.</li>
</ul></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/">الرئيسية العربية</a><a class="btn" lang="en" dir="ltr" href="/probability/conditional/bayes-theorem/">English lesson</a></div>
</div></section>
<script src="/js/bayes-evidence-lab.js" defer></script>
