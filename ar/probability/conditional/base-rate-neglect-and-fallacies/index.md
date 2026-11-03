---
layout: default
title: إهمال المعدل الأساسي والمغالطات الاحتمالية
description: شرح عربي للأخطاء الشائعة في تفسير الاحتمالات مع مثال اختبارات افتراضية ومختبر بايز تفاعلي للتحقق من أثر الانتشار والحساسية والنوعية.
permalink: /ar/probability/conditional/base-rate-neglect-and-fallacies/
sidebar: false
lang: ar
translation_pair: base-rate-neglect-and-fallacies
math: true
---
<section class="hero hero-section"><div class="hero-card"><div class="badge-row"><span class="badge">الاحتمال الشرطي</span><span class="badge">التفكير النقدي</span></div><h1>إهمال المعدل الأساسي والمغالطات الاحتمالية</h1><p class="lead">قد تبدو الأدلة قوية، لكن تفسيرها يصبح مضللاً إذا تجاهلنا احتمال الحالة قبل ظهور الدليل. نتعلم هنا كيف نقرأ الاحتمال الشرطي دون خلط بين الاتجاهين.</p><p><a href="/probability/conditional/base-rate-neglect-and-fallacies/" lang="en" dir="ltr">Read the English lesson</a></p></div></section>
<section><div class="content-narrow">
<h2>ما المقصود بالمعدل الأساسي؟</h2><p>هو نسبة وجود الحالة في المجتمع قبل الاطلاع على دليل جديد، مثل معدل انتشار حالة افتراضية. إهماله يؤدي إلى المبالغة في قوة الاختبارات أو القرائن، حتى لو كانت الحساسية مرتفعة.</p><p>يجب التفريق بين احتمال الحصول على نتيجة موجبة عند وجود الحالة، واحتمال وجود الحالة بعد الحصول على نتيجة موجبة. لا يتساوى هذان الاحتمالان بالضرورة.</p>
<div class="esa-ar-math" dir="ltr">\[
P(D\mid +)=\frac{P(+\mid D)P(D)}{P(+\mid D)P(D)+P(+\mid D^c)P(D^c)},\quad P(+)>0.
\]</div>
<h2>مثال للاختبار الافتراضي</h2><p>لنفترض انتشاراً يساوي 1%، وحساسية 90%، ونوعية 95%. في مجتمع افتراضي مكوّن من 10,000 شخص تكون النتائج المتوقعة: 90 إيجابية حقيقية، و10 سلبية كاذبة، و495 إيجابية كاذبة، و9,405 سلبية حقيقية. إذن بين 585 نتيجة إيجابية متوقعة توجد 90 حالة فعلية، أي أن احتمال وجود الحالة عند إيجابية النتيجة هو نحو 15.38%، وليس 90%.</p>
<div class="esa-ar-math" dir="ltr">\[
P(D\mid +)=\frac{0.01(0.90)}{0.01(0.90)+0.99(0.05)}=\frac{0.009}{0.0585}\approx0.153846.
\]</div>
<p>عند تغيّر معدل الانتشار، يتغير الاحتمال اللاحق حتى لو لم تتغير حساسية الاختبار أو نوعيته.</p>
<h2>مختبر تفاعلي لتأثير المعدل الأساسي</h2><p>غيّر الانتشار والحساسية والنوعية داخل المحاكاة التالية، وقارن الاحتمالات مع التكرارات المتوقعة. هذه محاكاة تعليمية لنتائج افتراضية، وليست أداة تشخيص.</p>
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
<h2>مغالطة التلازم أو الاقتران</h2><p>لا يمكن أن يكون احتمال وقوع حدثين معاً أكبر من احتمال أي منهما منفرداً، لأن تقاطع الحدثين مجموعة جزئية من كل منهما.</p><div class="esa-ar-math" dir="ltr">\[P(A\cap B)\leq \min\{P(A),P(B)\}.\]</div><p>التفاصيل القصصية المقنعة لا تغير هذه القاعدة الرياضية.</p>
<h2>مغالطة المدّعي العام</h2><p>الخلط بين احتمال مشاهدة دليل معين عند براءة شخص واحتمال براءته عند مشاهدة الدليل خطأ في عكس الشرط؛ لا يمكن إهمال المعدلات الأولية أو المعلومات الأخرى.</p>
<h2>مغالطة المقامر</h2><p>في رميات مستقلة لعملة عادلة، لا تتغير فرصة ظهور الصورة في الرمية التالية بسبب نتائج الرميات السابقة؛ فهي تساوي نصفاً في كل رمية. أما في السحب دون إرجاع فنتائج المراحل السابقة تؤثر بالفعل في الاحتمالات اللاحقة.</p>
<h2>مغالطة اليد الساخنة والتمثيل والتوفر</h2><p>قد نبالغ في تفسير سلسلة نجاح قصيرة بوصفها دليلاً على استمرار النجاح، أو نظن أن الحالة الأكثر حيوية في الذاكرة أكثر شيوعاً. يجب التحقق من نموذج الاعتماد وحجم العينة والمعدل الأساسي بدلاً من الاستنتاج من الحدس وحده.</p>
<h2>قواعد للمراجعة</h2><ul class="bullets"><li>حدد أي احتمال شرطي يُطلب حسابه، وما حدث الشرط.</li><li>تأكد من المعدل الأساسي قبل تحديث الاحتمالات.</li><li>احسب المقام وفق قانون الاحتمال الكلي ولا تشترط على حدث احتماله صفر.</li><li>لا تجمع مسارات غير متنافية وكأنها لا تتداخل.</li><li>تحقق من افتراض الاستقلال قبل استخدامه.</li></ul>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/conditional/tree-diagrams/">السابق: مخططات الشجرة</a><a class="btn" href="/ar/probability/conditional/bayes-theorem/">مراجعة نظرية بايز</a></div></div></section>
<style>.esa-ar-math{direction:ltr;overflow-x:auto;max-width:100%}.esa-ar-math mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}</style>
<script defer src="/js/bayes-evidence-lab.js"></script>
