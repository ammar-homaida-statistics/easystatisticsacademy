---
layout: default
title: الشروط — الطبيعية ومبرهنة النهاية المركزية والاستقلال
description: "شرح عربي لشروط فترات الثقة للمتوسط: الاستقلال وشرط 10%، والطبيعية، ومبرهنة النهاية المركزية وحدودها، ولماذا لا يكفي n = 30 دائمًا، مع مختبر محاكاة لتغطية فترة t في مجتمعات ملتوية."
permalink: /ar/inference/confidence-intervals/conditions-normality-clt-independence/
lang: ar
sidebar: false
math: true
learning_resource: true
translation_pair: conditions-normality-clt-independence
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاستدلال</span><span class="badge">فترات الثقة</span><span class="badge">الشروط</span></div>
<h1>الشروط — الطبيعية ومبرهنة النهاية المركزية والاستقلال</h1>
{% include lab-noscript.html %}
<p class="lead">صيغ فترات الثقة جديرة بالثقة بقدر ما تكون افتراضاتها صحيحة.</p>
<p class="lead">لذلك يجب قبل بناء الفترة التحقق من أن الشروط التي تدعم توزيع المعاينة متحققة على نحو معقول.</p>
<p><a href="/inference/confidence-intervals/conditions-normality-clt-independence/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/">الدرس السابق: فترة t للمتوسط</a></p>
</div></section>
<section><div class="content-narrow">

<h2>1. لماذا تهم الشروط؟</h2>
<p>تعتمد فترات الثقة على نماذج احتمالية تصف سلوك التقديرات في المعاينة المتكررة؛ فإذا انتُهكت الافتراضات انتهاكًا شديدًا فقد لا تبلغ الفترة مستوى الثقة المعلن.</p>
<div class="concept-box"><strong>الفكرة الرئيسة:</strong><p>فترة الثقة موثوقة بقدر موثوقية الافتراضات التي تبررها.</p></div>

<h2>2. الشروط الثلاثة الكبرى</h2>
<p>لفترات الثقة الخاصة بالمتوسطات ثلاثة شروط مهمة خصوصًا: <strong>الاستقلال</strong>، و<strong>الطبيعية</strong>، و<strong>مبرهنة النهاية المركزية</strong>. ومعًا تبرر توزيع المعاينة الذي تستخدمه صيغ فترات الثقة.</p>

<h2>3. الشرط الأول: الاستقلال</h2>
<div class="concept-box"><strong>الاستقلال:</strong><p>معرفة مشاهدة ما لا ينبغي أن تحدد مشاهدة أخرى تحديدًا كبيرًا.</p></div>
<p>تفترض صيغ الخطأ المعياري أن المعلومات تتراكم مع ازدياد حجم العيّنة؛ فإذا كانت المشاهدات معتمدة بقوة كانت كمية المعلومات الفعلية أقل مما يوحي به حجم العيّنة، وقد تصبح فترات الثقة ضيقة على نحو مضلل (انظر مختبر <a href="/ar/inference/assumptions-robustness/independence-and-dependence/">الاستقلال والاعتماد</a>).</p>
<p>ويُقرَّب الاستقلال عادةً بالمعاينة العشوائية، أو التعيين العشوائي، أو كون المجتمع كبيرًا مقارنةً بالعيّنة؛ فالتصميم السليم هو خط الدفاع الأول ضد مشكلات الاعتماد.</p>

<h2>4. شرط 10%</h2>
<div class="concept-box"><strong>شرط 10%:</strong><p>عند المعاينة دون إرجاع ينبغي أن يكون حجم العيّنة أقل من نحو 10% من حجم المجتمع.</p></div>
<p>ويساعد ذلك على تبرير معاملة المشاهدات على أنها مستقلة تقريبًا.</p>

<h2>5. الشرط الثاني: الطبيعية</h2>
<p>تُبنى فترات الثقة للمتوسطات بتوزيعات تفترض الطبيعية تقريبًا، فيصبح السؤال: <strong>هل توزيع المعاينة لمتوسط العيّنة طبيعي تقريبًا؟</strong> فإذا كان المجتمع نفسه طبيعيًا كان متوسط العيّنة طبيعيًا عند كل حجم عيّنة (مع مشاهدات مستقلة).</p>

<h2>6. المشكلة الواقعية</h2>
<p>معظم المجتمعات الحقيقية ليست طبيعية تمامًا؛ فقد تكون ملتوية، أو ثقيلة الذيول، أو متعددة القمم، أو فيها قيم متطرفة. ولحسن الحظ توجد نتيجة قوية أخرى تساعدنا غالبًا.</p>

<h2>7. الشرط الثالث: مبرهنة النهاية المركزية</h2>
<div class="concept-box"><strong>مبرهنة النهاية المركزية:</strong><p>للمشاهدات المستقلة متطابقة التوزيع ذات التباين المنتهي، يقترب توزيع المعاينة للمتوسط المعياري من التوزيع الطبيعي مع ازدياد حجم العيّنة، أيًّا كان شكل المجتمع.</p></div>
<p>لاحظ شرط التباين المنتهي: ففي المجتمعات ذات الذيول الثقيلة جدًا (مثل توزيع كوشي) لا تنطبق المبرهنة. ومن دونها كانت فترات الثقة ستتطلب مجتمعات طبيعية في حالات أكثر بكثير.</p>

<h2>8. أثر حجم العيّنة</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">حجم العيّنة</th><th scope="col">التقريب الطبيعي</th></tr></thead>
<tbody>
<tr><td>صغير</td><td>قد يكون ضعيفًا</td></tr>
<tr><td>متوسط</td><td>معقول غالبًا</td></tr>
<tr><td>كبير</td><td>جيد جدًا عادةً</td></tr>
</tbody></table></div>

<!-- مختبر مبرهنة النهاية المركزية وتغطية فترة t (Batch #105، النسخة العربية) -->
<section class="concept-box" id="esa-clt-lab" data-locale="ar" aria-labelledby="esa-clt-heading">
  <h3 id="esa-clt-heading">مختبر تفاعلي: هل تنقذ مبرهنة النهاية المركزية فترة t؟</h3>
  <p>يسحب المختبر 20,000 عيّنة بحجم n من المجتمع المختار، ويبني من كل عيّنة الفترة المعتادة \(\bar x\pm t_{n-1,\,1-\alpha/2}\,s/\sqrt n\)، ثم يعدّ المرات التي تحتوي فيها الفترة على المتوسط الحقيقي μ. كما يبيّن عدد المرات التي تخطئ فيها الفترة كلها من كل جهة، ويعرض مدرجًا تكراريًا لمتوسطات العيّنات العشرين ألفًا.</p>
  <div class="esa-clt-grid">
    <label for="esa-clt-pop">المجتمع<select id="esa-clt-pop"><option value="normal">طبيعي (متماثل)</option><option value="uniform">منتظم (متماثل، ذيول خفيفة)</option><option value="exponential" selected>أسّي (ملتوٍ نحو اليمين)</option><option value="lognormal">لوغاريتمي طبيعي (شديد الالتواء نحو اليمين)</option></select></label>
    <label for="esa-clt-n">حجم العيّنة n<input id="esa-clt-n" dir="ltr" type="number" min="2" max="200" step="1" inputmode="numeric" value="10" aria-describedby="esa-clt-error"></label>
    <label for="esa-clt-level">مستوى الثقة الاسمي<select id="esa-clt-level"><option value="90">90%</option><option value="95" selected>95%</option><option value="99">99%</option></select></label>
  </div>
  <div class="esa-clt-controls"><button class="btn btn-outline" type="button" id="esa-clt-exp10">أسّي، n = 10</button><button class="btn btn-outline" type="button" id="esa-clt-exp100">أسّي، n = 100</button><button class="btn btn-outline" type="button" id="esa-clt-norm10">طبيعي، n = 10</button></div>
  <p id="esa-clt-error" role="alert" hidden></p>
  <section id="esa-clt-results" aria-label="التغطية بالمحاكاة" role="status" aria-live="polite" aria-atomic="true">
    <div class="table-wrap"><table><caption>20,000 عيّنة محاكاة (ببذرة ثابتة)</caption><tbody>
      <tr><th scope="row">التغطية الفعلية</th><td><output id="esa-clt-coverage" dir="ltr">0.8995</output></td></tr>
      <tr><th scope="row">الخطأ المعياري لمونت كارلو</th><td><output id="esa-clt-mcse" dir="ltr">0.0021</output></td></tr>
      <tr><th scope="row">الفترة كلها تحت μ</th><td><output id="esa-clt-below" dir="ltr">0.0959</output></td></tr>
      <tr><th scope="row">الفترة كلها فوق μ</th><td><output id="esa-clt-above" dir="ltr">0.0046</output></td></tr>
      <tr><th scope="row">قيمة t الحرجة</th><td><output id="esa-clt-crit" dir="ltr">2.2622</output></td></tr>
    </tbody></table></div>
    <p id="esa-clt-note"></p>
    <svg id="esa-clt-chart" viewBox="0 0 460 170" role="img" aria-label="مدرج تكراري لمتوسطات العيّنات" style="display:block;width:100%;height:auto;max-width:560px;direction:ltr"></svg>
  </section>
  <p class="muted-mini">للبيانات الطبيعية تكون فترة t تامة، فتساوي التغطية بالمحاكاة 95% ضمن خطأ مونت كارلو. أما للبيانات الأسية مع <span dir="ltr">n = 10</span> فلا تغطي الفترة «95%» إلا نحو 90%، وتقع الأخطاء كلها تقريبًا في جهة واحدة: فحين يصادف أن يكون متوسط عيّنة ملتوية صغيرًا، يكون انحرافها المعياري صغيرًا أيضًا غالبًا، فتقصر الفترة تمامًا حين تكون منخفضة. وعند <span dir="ltr">n = 100</span> تبلغ التغطية نحو 94%، قريبة من 95% لكنها ما تزال تحتها. البذرة الثابتة تجعل كل نتيجة قابلة لإعادة الإنتاج، وتتفق محاكاة مستقلة لـ 200,000 عيّنة معها ضمن خطأ مونت كارلو.</p>
</section>
<style>
#esa-clt-lab,#esa-clt-lab *{box-sizing:border-box}
#esa-clt-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-clt-lab label{display:block;font-weight:650;margin:6px 0}
#esa-clt-lab :is(input,select){display:block;width:100%;min-width:0;font:inherit;padding:8px;margin-top:4px;border:1px solid #777;border-radius:6px}
#esa-clt-lab .esa-clt-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,170px),1fr));gap:4px 10px}
#esa-clt-lab .esa-clt-controls{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
#esa-clt-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-clt-lab [hidden]{display:none!important}
#esa-clt-lab :is(input,select,button):focus-visible{outline:2px solid #0f766e;outline-offset:3px}
</style>
<script defer src="/js/clt-coverage-lab.js"></script>

<h2>9. هل n = 30 رقم سحري؟</h2>
<p>تذكر مقررات تمهيدية كثيرة القاعدة <span dir="ltr">n ≥ 30</span>، لكن لا شيء سحري في الرقم 30؛ فحجم العيّنة اللازم يعتمد على شكل المجتمع. فإذا كان المجتمع طبيعيًا تقريبًا قد تكفي عيّنات من 10 أو 15 مشاهدة، أما المجتمعات شديدة الالتواء أو ثقيلة الذيول أو التي فيها قيم متطرفة شديدة فقد تتطلب عيّنات أكبر بكثير، كما يبيّن المختبر أعلاه.</p>

<h2>10. دور القيم المتطرفة</h2>
<p>قد تؤثر القيم المتطرفة بقوة في متوسط العيّنة وانحرافها المعياري معًا، ولأن فترات المتوسط تعتمد على الكميتين، فإن المشاهدات المتطرفة تستحق فحصًا دقيقًا (انظر <a href="/ar/inference/assumptions-robustness/outliers-and-influence/">القيم المتطرفة والمشاهدات المؤثرة</a>).</p>

<h2>11. قائمة تحقق عملية</h2>
<p>قبل بناء فترة ثقة لمتوسط اسأل:</p>
<ol><li>هل جُمعت العيّنة بطريقة عشوائية معقولة؟</li><li>هل المشاهدات مستقلة تقريبًا؟</li><li>هل العيّنة أقل من 10% من المجتمع؟</li><li>هل المجتمع طبيعي تقريبًا، أو العيّنة كبيرة بما يكفي لمبرهنة النهاية المركزية بالنظر إلى شكله؟</li><li>هل توجد قيم متطرفة خطيرة أو التواء شديد؟</li></ol>

<h2>12. ماذا يحدث إذا لم تتحقق الشروط؟</h2>
<p>لا تُبطل الانتهاكات الفترةَ تلقائيًا؛ فالأثر يعتمد على شدة الانتهاك، وحجم العيّنة، ونوع الفترة. بعض الانتهاكات طفيف، وبعضها قد يشوّه احتمالات التغطية تشويهًا كبيرًا، وعندئذ قد تكون <a href="/ar/inference/assumptions-robustness/bootstrap-as-robust-tool/">طرق بوتستراب</a> أو التحويلات أو <a href="/ar/inference/assumptions-robustness/robust-alternatives-nonparametric/">البدائل الحصينة</a> أنسب.</p>

<h2>13. لماذا يتحقق الإحصائيون من الافتراضات أولًا؟</h2>
<p>حساب الفترة سهل، أما تحديد ما إذا كانت جديرة بالثقة فهو المهمة الأصعب؛ والممارسة الإحصائية الجيدة تضع فحص الافتراضات قبل التفسير.</p>

<h2>14. الصورة الأشمل</h2>
<p>تعتمد فترات الثقة على توزيعات المعاينة: الاستقلال يدعم صحة الأخطاء المعيارية، والطبيعية ومبرهنة النهاية المركزية تدعمان التوزيعات المستخدمة للقيم الحرجة؛ ومعًا تجعل هذه الشروط إجراءات فترات الثقة تعمل كما ينبغي.</p>
<div class="concept-box"><strong>الرسالة الأساسية:</strong><p>تتطلب فترات الثقة الموثوقة مشاهدات مستقلة تقريبًا وتوزيع معاينة طبيعيًا تقريبًا، يتحقق بطبيعية المجتمع أو بمبرهنة النهاية المركزية أو بكليهما؛ وسرعة عمل المبرهنة تعتمد على شكل المجتمع.</p></div>

<h2>15. ماذا بعد؟</h2>
<p>ركّزنا حتى الآن على فترات الثقة للمتوسطات، ومن المهام الاستدلالية الشائعة جدًا أيضًا تقدير نسب المجتمع. ويطوّر الدرس التالي فترات الثقة للنسب ويبيّن كيف ينطبق المخطط نفسه في سياق جديد.</p>

<div class="summary-box">
<h2>خلاصة الدرس</h2>
<ul class="bullets">
<li>تعتمد فترات الثقة على افتراضات.</li>
<li>الاستقلال أساسي لصحة الأخطاء المعيارية.</li>
<li>يساعد شرط 10% على تبرير الاستقلال التقريبي.</li>
<li>المجتمعات الطبيعية تعطي توزيعات معاينة طبيعية للمتوسط.</li>
<li>تبرر مبرهنة النهاية المركزية غالبًا التقريب الطبيعي، بشرط تباين منتهٍ.</li>
<li>العيّنات الأكبر تحسّن التقريب، وسرعته تعتمد على شكل المجتمع.</li>
<li>الالتواء يجعل أخطاء فترة t غير متوازنة بين الطرفين.</li>
<li>فحص الافتراضات جزء حاسم من الاستدلال الإحصائي.</li>
</ul>
</div>

<div class="lesson-nav">
<a class="btn btn-outline" href="/ar/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/">→ السابق: فترة t للمتوسط</a>
<a class="btn" href="/ar/inference/confidence-intervals/ci-for-proportion/">التالي: فترة الثقة للنسبة ←</a>
</div>
</div></section>
