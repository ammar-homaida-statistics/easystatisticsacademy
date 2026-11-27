---
layout: default
title: الاستقلال والاعتماد
description: "شرح عربي لافتراض استقلال المشاهدات: أمثلة الاعتماد الزمني والعنقودي والقياسات المتكررة، وحجم العيّنة الفعّال، وأثر تجاهل الاعتماد في الأخطاء المعيارية، مع مختبر تفاعلي لنموذج AR(1)."
permalink: /ar/inference/assumptions-robustness/independence-and-dependence/
lang: ar
sidebar: false
math: true
learning_resource: true
translation_pair: independence-and-dependence
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاستدلال</span><span class="badge">الافتراضات والحصانة</span><span class="badge">الاستقلال</span></div>
<h1>الاستقلال والاعتماد</h1>
{% include lab-noscript.html %}
<p class="lead">الاستقلال من أهم الافتراضات في الاستدلال الإحصائي.</p>
<p class="lead">وبخلاف كثير من الانحرافات الطفيفة عن الطبيعية، قد يشوّه انتهاك الاستقلال الأخطاءَ المعيارية وفترات الثقة واختبارات الفرضيات والاستنتاجات تشويهًا كبيرًا.</p>
<p><a href="/inference/assumptions-robustness/independence-and-dependence/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/assumptions-robustness/heteroscedasticity-variance-issues/">الدرس التالي: عدم تجانس التباين</a></p>
</div></section>
<section><div class="content-narrow">

<h2>1. لماذا يهم الاستقلال؟</h2>
<p>تفترض معظم الطرق الإحصائية أن كل مشاهدة تقدّم معلومة منفصلة. فإذا كانت المشاهدات مرتبطة بعضها ببعض ارتباطًا قويًا، فقد تكون كمية المعلومات في البيانات أقل بكثير مما يوحي به حجم العيّنة.</p>
<div class="concept-box"><strong>الفكرة الرئيسة:</strong><p>الاستقلال يعني أن المعلومة التي تقدّمها مشاهدة لا تحدد مباشرة المعلومة التي تقدّمها مشاهدة أخرى.</p></div>

<h2>2. ما الاستقلال؟</h2>
<p>بصورة غير رسمية، تكون مشاهدتان مستقلتين إذا كانت معرفة إحداهما لا تغيّر توقعنا للأخرى. وفي نظرية الاحتمال يعني الاستقلال:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="تعريف الاستقلال">\[P(A\cap B)=P(A)P(B)\quad\text{for all relevant events }A,B.\]</div>
<p>فمعرفة وقوع حدث لا تقدّم أي معلومة عن وقوع الآخر.</p>

<h2>3. أمثلة على مشاهدات مستقلة</h2>
<ul class="bullets"><li>أفراد مختارون عشوائيًا من مجتمع كبير</li><li>وحدات تجريبية مستقلة</li><li>رميات متكررة لعملة متوازنة</li><li>قياسات من أشخاص لا صلة بينهم</li></ul>

<h2>4. ما الاعتماد؟</h2>
<div class="concept-box"><strong>تعريف:</strong><p>يوجد الاعتماد عندما تؤثر المشاهدات بعضها في بعض أو تشترك في مصادر تباين واحدة؛ فتساعد معلومة من مشاهدة على التنبؤ بأخرى أو تفسيرها.</p></div>

<h2>5. أمثلة على الاعتماد</h2>
<ul class="bullets"><li>قياسات متكررة من الشخص نفسه</li><li>طلاب في الصف نفسه</li><li>مرضى في المستشفى نفسه</li><li>أسعار الأسهم اليومية عبر الزمن</li><li>أفراد الأسرة الواحدة</li></ul>

<h2>6. مثال من الصف الدراسي</h2>
<p>لنفترض أننا جمعنا درجات اختبار لطلاب صف واحد. يشترك هؤلاء الطلاب في المعلّم نفسه والمنهج نفسه والبيئة نفسها؛ لذا قد تكون درجاتهم أكثر تشابهًا من درجات طلاب مختارين عشوائيًا من مدارس كثيرة.</p>

<h2>7. لماذا يسبب الاعتماد مشكلات؟</h2>
<p>تفترض معظم الصيغ المعتادة أن كل مشاهدة تضيف معلومة جديدة كاملة. وعندما تكون المشاهدات معتمدة:</p>
<ul class="bullets"><li>ينخفض حجم العيّنة الفعّال</li><li>قد تُقدَّر الأخطاء المعيارية بأقل من حقيقتها</li><li>قد تصبح فترات الثقة أضيق مما ينبغي</li><li>قد تصبح القيم الاحتمالية صغيرة على نحو مصطنع</li></ul>
<p>وقد تولّد هذه المشكلات ثقة زائفة بالنتائج.</p>

<h2>8. فكرة حجم العيّنة الفعّال</h2>
<p>تخيّل جمع 100 مشاهدة متطابقة تقريبًا؛ فمع أن البيانات تضم 100 سجل، فإنها لا تقدّم كمية المعلومات التي تقدّمها 100 مشاهدة مستقلة حقًا. فالاعتماد يقلّل تنوّع المعلومات.</p>

<h2>9. الاعتماد الزمني والارتباط الذاتي</h2>
<p>يظهر الاعتماد كثيرًا في البيانات المجموعة عبر الزمن، مثل أسعار الأسهم، وقياسات الطقس، وحركة زيارات المواقع، والمؤشرات الاقتصادية؛ فقيمة اليوم تشبه غالبًا قيمة الأمس. ويُسمّى الاعتماد عبر الزمن <strong>الارتباط الذاتي</strong> (Autocorrelation): الارتباط الذاتي الموجب يعني أن المشاهدات المتجاورة متشابهة، والسالب يعني أنها تتحرك في اتجاهين متعاكسين.</p>

<!-- مختبر AR(1) (Batch #103، النسخة العربية) -->
<section class="concept-box" id="esa-ar1-lab" data-locale="ar" aria-labelledby="esa-ar1-heading">
  <h3 id="esa-ar1-heading">مختبر تفاعلي: كيف يُفسد الاعتمادُ الخطأَ المعياري</h3>
  <p>لنفترض أن المشاهدات تتبع عملية AR(1) مستقرة، يكون فيها الارتباط بين مشاهدتين تفصل بينهما \(k\) خطوة مساويًا \(\rho^k\). عندئذ يكون تباين متوسط العيّنة:</p>
  <div class="esa-ar1-math" dir="ltr" tabindex="0" role="region" aria-label="تباين متوسط العيّنة في ظل اعتماد AR(1)">
  \[
  \operatorname{Var}(\bar X)=\frac{\sigma^2}{n}\Bigl[1+2\sum_{k=1}^{n-1}\Bigl(1-\frac kn\Bigr)\rho^k\Bigr]=\frac{\sigma^2}{n}\,\mathrm{VIF},
  \qquad n_{\mathrm{eff}}=\frac{n}{\mathrm{VIF}}.
  \]
  </div>
  <p>واختبار z الذي يستخدم خطأً \(\sigma/\sqrt n\) يكون معدل خطئه الحقيقي من النوع الأول، للبيانات الطبيعية، مساويًا \(2\,\Phi\bigl(-z_{1-\alpha/2}/\sqrt{\mathrm{VIF}}\bigr)\).</p>
  <div class="esa-ar1-grid">
    <label for="esa-ar1-n">حجم العيّنة n<input id="esa-ar1-n" type="number" min="2" max="100000" step="1" inputmode="numeric" value="100" dir="ltr" aria-describedby="esa-ar1-error"></label>
    <label for="esa-ar1-rho">معامل الارتباط عند الفجوة 1 (ρ)<input id="esa-ar1-rho" type="number" min="-0.95" max="0.95" step="0.05" inputmode="decimal" value="0.5" dir="ltr" aria-describedby="esa-ar1-error"></label>
    <label for="esa-ar1-alpha">مستوى α الاسمي<input id="esa-ar1-alpha" type="number" min="0.001" max="0.5" step="any" inputmode="decimal" value="0.05" dir="ltr" aria-describedby="esa-ar1-error"></label>
  </div>
  <div class="esa-ar1-controls"><button class="btn btn-outline" type="button" id="esa-ar1-pos">ارتباط موجب (ρ = 0.5)</button><button class="btn btn-outline" type="button" id="esa-ar1-neg">ارتباط سالب (ρ = −0.5)</button><button class="btn btn-outline" type="button" id="esa-ar1-ind">مستقلة (ρ = 0)</button></div>
  <p id="esa-ar1-error" role="alert" hidden></p>
  <section id="esa-ar1-results" aria-label="أثر الاعتماد" role="status" aria-live="polite" aria-atomic="true">
    <div class="table-wrap"><table><caption>ماذا يحدث عند تجاهل الاعتماد</caption><tbody>
      <tr><th scope="row">عامل تضخم التباين (VIF)</th><td><output id="esa-ar1-vif" dir="ltr">2.9600</output></td></tr>
      <tr><th scope="row">حجم العيّنة الفعّال n/VIF</th><td><output id="esa-ar1-neff" dir="ltr">33.8</output></td></tr>
      <tr><th scope="row">الخطأ المعياري الحقيقي ÷ الساذج</th><td><output id="esa-ar1-ratio" dir="ltr">1.7205</output></td></tr>
      <tr><th scope="row">معدل الخطأ الحقيقي من النوع الأول لاختبار z الساذج</th><td><output id="esa-ar1-typeI" dir="ltr">0.254617</output></td></tr>
      <tr><th scope="row">التغطية الحقيقية للفترة الساذجة</th><td><output id="esa-ar1-coverage" dir="ltr">0.745383</output></td></tr>
    </tbody></table></div>
    <p id="esa-ar1-note"></p>
  </section>
  <p class="muted-mini">مع <span dir="ltr">n = 100</span> و<span dir="ltr">ρ = 0.5</span> تحمل المشاهدات المئة معلومات عن المتوسط تعادل نحو 34 مشاهدة مستقلة فقط، ويرفض اختبار اسمي عند 5% فرضية صفرية صحيحة في نحو 25% من المرات. وقد أعطت محاكاة ببذرة ثابتة لـ 20,000 سلسلة AR(1) النسبة 25.7%، بما يتفق مع الصيغة. يفترض المختبر أخطاء AR(1) طبيعية مستقرة و\(\sigma\) معلومًا؛ وقد يكون للبيانات الحقيقية بنى اعتماد أخرى، مثل العناقيد أو الذاكرة الطويلة.</p>
</section>
<style>
#esa-ar1-lab,#esa-ar1-lab *{box-sizing:border-box}
#esa-ar1-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-ar1-lab label{display:block;font-weight:650;margin:6px 0}
#esa-ar1-lab input{display:block;width:100%;min-width:0;font:inherit;padding:8px;margin-top:4px;border:1px solid #777;border-radius:6px}
#esa-ar1-lab .esa-ar1-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,160px),1fr));gap:4px 10px}
#esa-ar1-lab .esa-ar1-controls{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
#esa-ar1-lab .table-wrap,.esa-ar1-math{max-width:100%;overflow-x:auto}
.esa-ar1-math{direction:ltr}
#esa-ar1-lab [hidden]{display:none!important}
#esa-ar1-lab :is(input,button):focus-visible,.esa-ar1-math:focus-visible{outline:2px solid #0f766e;outline-offset:3px}
</style>
<script defer src="/js/ar1-dependence-lab.js"></script>

<h2>10. البيانات العنقودية</h2>
<p>يظهر الاعتماد أيضًا عندما تنتمي المشاهدات إلى مجموعات، مثل المدارس والمستشفيات والأسر والمناطق الجغرافية؛ فالمشاهدات داخل العنقود الواحد أكثر تشابهًا غالبًا من المشاهدات في عناقيد مختلفة.</p>

<h2>11. بيانات القياسات المتكررة</h2>
<p>ومن مصادر الاعتماد الشائعة قياس الشخص نفسه مرات عدة، كما في دراسات «قبل وبعد»، والدراسات الطولية، وتتبع النمو، والمتابعة الطبية؛ فقياسات الشخص نفسه نادرًا ما تكون مستقلة.</p>

<h2>12. هل يمكن التحقق من الاستقلال؟</h2>
<p>بخلاف الطبيعية، يصعب غالبًا التحقق من الاستقلال من البيانات وحدها. ويعتمد المحللون كثيرًا على معلومات تصميم الدراسة، وإجراءات المعاينة، ومعرفة عملية توليد البيانات، والرسوم التشخيصية. وفهم كيفية جمع البيانات حاسم في الغالب.</p>

<h2>13. التصميم مهم</h2>
<p>الاستقلال كثيرًا ما يكون افتراضًا تصميميًا لا افتراضًا نموذجيًا، وأسئلة مثل: هل اختيرت الوحدات عشوائيًا؟ هل المشاهدات عنقودية؟ هل توجد قياسات متكررة؟ غالبًا أهم من التشخيصات الإحصائية الرسمية.</p>

<h2>14. التعامل مع الاعتماد</h2>
<p>عند وجود اعتماد قد نحتاج إلى طرق متخصصة، مثل: التحليلات الزوجية، ونماذج التأثيرات المختلطة، ونماذج السلاسل الزمنية، والأخطاء المعيارية الحصينة للعناقيد. وهذه الطرق تأخذ بنية الاعتماد في الحسبان صراحةً.</p>

<h2>15. الاستقلال مقابل الطبيعية</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">الانتهاك</th><th scope="col">العاقبة المعتادة</th></tr></thead>
<tbody>
<tr><td>انحراف طفيف عن الطبيعية</td><td>طفيفة غالبًا</td></tr>
<tr><td>اعتماد قوي</td><td>قد تكون شديدة</td></tr>
</tbody></table></div>
<p>ولهذا يُعدّ الاستقلال من أهم افتراضات الاستدلال؛ فكثير من الطرق حصين نسبيًا للانحرافات المعتدلة عن الطبيعية، وقليل منها حصين لاعتماد شديد مُهمَل في التحليل.</p>

<h2>16. قائمة تحقق عملية</h2>
<p>قبل إجراء الاستدلال اسأل:</p>
<ol><li>هل يمكن أن تؤثر المشاهدات بعضها في بعض؟</li><li>هل جُمعت قياسات متكررة؟</li><li>هل المشاهدات عنقودية؟</li><li>هل يوجد مكوّن زمني؟</li><li>هل يأخذ التحليل هذه العلاقات في الحسبان؟</li></ol>

<h2>17. الصورة الأشمل</h2>
<p>الاستقلال افتراض أساسي لأنه يحدد كمية المعلومات الموجودة فعلًا في البيانات، وتجاهل الاعتماد قد يعطي فترات ثقة واختبارات دلالة واستنتاجات مضللة.</p>
<div class="concept-box"><strong>الرسالة الأساسية:</strong><p>الاستقلال يعني أن المشاهدات تقدّم معلومات منفصلة، والاعتماد يعني أنها مترابطة. وقد يشوّه انتهاك الاستقلال الاستدلالَ الإحصائي تشويهًا كبيرًا، ويتطلب غالبًا طرقًا متخصصة.</p></div>

<h2>18. ماذا بعد؟</h2>
<p>ثمة افتراض مهم آخر يتعلق بالتباين؛ إذ تفترض طرق كثيرة أن التباين ثابت تقريبًا عبر المشاهدات أو المجموعات. ويتناول الدرس التالي عدم تجانس التباين وأثره في الاستنتاجات.</p>

<div class="summary-box">
<h2>خلاصة الدرس</h2>
<ul class="bullets">
<li>الاستقلال من أهم افتراضات الاستدلال.</li>
<li>المشاهدات المعتمدة تتقاسم المعلومات.</li>
<li>الاعتماد يقلّل حجم العيّنة الفعّال.</li>
<li>تجاهل الاعتماد الموجب يقلّل تقدير الأخطاء المعيارية ويضخّم معدل الخطأ من النوع الأول.</li>
<li>بيانات السلاسل الزمنية والعنقودية والقياسات المتكررة معتمدة غالبًا.</li>
<li>الاستقلال كثيرًا ما يكون افتراضًا تصميميًا.</li>
<li>توجد طرق متخصصة للبيانات المعتمدة.</li>
<li>انتهاك الاستقلال غالبًا أخطر من الانحراف الطفيف عن الطبيعية.</li>
</ul>
</div>

<div class="lesson-nav">
<a class="btn btn-outline" href="/inference/assumptions-robustness/checking-normality-what-and-why/" hreflang="en" lang="en" dir="ltr">← Previous: Checking Normality (English)</a>
<a class="btn" href="/ar/inference/assumptions-robustness/heteroscedasticity-variance-issues/">التالي: عدم تجانس التباين ←</a>
</div>
</div></section>
