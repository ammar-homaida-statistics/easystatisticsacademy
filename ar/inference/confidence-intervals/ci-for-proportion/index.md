---
layout: default
title: فترة الثقة للنسبة
description: "شرح عربي لفترة الثقة لنسبة المجتمع: النسبة في العيّنة، والخطأ المعياري، وفترة والد ومثال محسوب، وشرط النجاح والإخفاق، وفترة ويلسون، مع مختبرين تفاعليين أحدهما يحسب التغطية الدقيقة لفترات والد وويلسون وكلوبر–بيرسون."
permalink: /ar/inference/confidence-intervals/ci-for-proportion/
lang: ar
sidebar: false
math: true
learning_resource: true
translation_pair: ci-for-proportion
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاستدلال</span><span class="badge">فترات الثقة</span><span class="badge">النسب</span></div>
<h1>فترة الثقة للنسبة</h1>
{% include lab-noscript.html %}
<p class="lead">تتعلق أسئلة واقعية كثيرة بالنسب لا بالمتوسطات.</p>
<p class="lead">فنتائج الاستطلاعات، ومعدلات التأييد، ونسب المعيب، ومعدلات التحويل، وانتشار الأمراض كلها أمثلة تكون فيها المعلمة المطلوبة نسبةً في المجتمع.</p>
<p><a href="/inference/confidence-intervals/ci-for-proportion/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/confidence-intervals/width-and-precision-what-controls/">درس ذو صلة: عرض الفترة ودقتها</a></p>
</div></section>
<section><div class="content-narrow">

<h2>1. المعلمة المطلوبة</h2>
<p>عند دراسة النسب تكون معلمة المجتمع \(p\in[0,1]\)، أي نسبة أفراد المجتمع الذين يحملون خاصية معيّنة، مثل: نسبة مؤيدي مرشح، أو نسبة مشتري منتج، أو نسبة القطع المعيبة، أو نسبة من يجيبون «نعم» عن سؤال استطلاع.</p>

<h2>2. النسبة في العيّنة</h2>
<p>لأن النسبة الحقيقية في المجتمع مجهولة، نقدّرها بالنسبة في العيّنة:</p>
<div dir="ltr">\[\hat p=\frac{x}{n},\]</div>
<p>حيث \(x\) عدد النجاحات و\(n\) حجم العيّنة.</p>

<h2>3. مثال على النسبة في العيّنة</h2>
<p>لنفترض أن استطلاعًا سأل 500 شخص عن تأييدهم لسياسة ما، فأيّدها 310:</p>
<div dir="ltr">\[\hat p=\frac{310}{500}=0.62.\]</div>

<section class="concept-box" id="esa-single-proportion-lab" data-locale="ar" aria-labelledby="esa-sp-heading">
<h2 id="esa-sp-heading">مختبر تفاعلي: فترة والد مقابل فترة ويلسون</h2>
<p>أدخل أعداد محاولات ثنائية مستقلة لمقارنة فترة والد المعتادة المبنية على التقريب الطبيعي بفترة ويلسون (Wilson score). فترة ويلسون أكثر موثوقية عمومًا قرب الحدود وفي أحجام العيّنات المتوسطة، ولا توجد طريقة تضمن تغطيتها المعلنة في كل حالة منتهية.</p>
<div class="esa-sp-fields">
  <div><label for="esa-sp-x">عدد النجاحات x</label><input id="esa-sp-x" type="number" min="0" max="10000000" step="1" value="310" inputmode="numeric" dir="ltr" aria-describedby="esa-sp-error esa-sp-warning"></div>
  <div><label for="esa-sp-n">حجم العيّنة n</label><input id="esa-sp-n" type="number" min="1" max="10000000" step="1" value="500" inputmode="numeric" dir="ltr" aria-describedby="esa-sp-error esa-sp-warning"></div>
  <div><label for="esa-sp-level">مستوى الثقة</label><select id="esa-sp-level"><option value="90">90%</option><option value="95" selected>95%</option><option value="99">99%</option></select></div>
</div>
<button type="button" class="btn btn-outline" id="esa-sp-reset">استعادة مثال الاستطلاع</button>
<p id="esa-sp-error" role="alert" hidden></p>
<section id="esa-sp-results" role="status" aria-live="polite" aria-atomic="true">
  <p>النسبة في العيّنة: <span dir="ltr"><output id="esa-sp-estimate">—</output>%</span>.</p>
  <p>فترة والد عند <span dir="ltr"><output id="esa-sp-confidence">95</output>%</span>: <span dir="ltr">[<output id="esa-sp-waldlo">—</output>, <output id="esa-sp-waldhi">—</output>]</span> نقطة مئوية.</p>
  <p>فترة ويلسون: <span dir="ltr">[<output id="esa-sp-wilsonlo">—</output>, <output id="esa-sp-wilsonhi">—</output>]</span> نقطة مئوية.</p>
  <svg id="esa-sp-chart" viewBox="0 0 470 116" role="img" aria-label="فترتا والد وويلسون" style="display:block;width:100%;height:auto;max-width:570px;direction:ltr"></svg>
  <p id="esa-sp-warning" role="status" aria-live="polite"></p>
</section>
<p class="muted-mini">تستخدم فترة والد \(\hat p\pm z\sqrt{\hat p(1-\hat p)/n}\)، وتستخدم فترة ويلسون فترة الدرجة بمقام \(1+z^2/n\). وعندما تكون النجاحات صفرًا أو كلها نجاحات، يصبح الخطأ المعياري في فترة والد صفرًا فتنهار إلى نقطة، بينما تبقى فترة ويلسون مفيدة. وقد تتجاوز فترة والد المجال [0,1]، وتُعرض حدودها المحسوبة دون قص.</p>
</section>
<style>
#esa-single-proportion-lab{max-width:100%;min-width:0;box-sizing:border-box;overflow-wrap:anywhere}
#esa-single-proportion-lab .esa-sp-fields{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,190px),1fr));gap:12px;margin:12px 0}
#esa-single-proportion-lab label{display:block;font-weight:650;margin-bottom:6px}
#esa-single-proportion-lab :is(input,select){box-sizing:border-box;width:100%;max-width:100%;padding:9px;font:inherit}
#esa-single-proportion-lab :is(input,button,select):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
#esa-single-proportion-lab [hidden]{display:none!important}
#esa-single-proportion-lab #esa-sp-error{font-weight:700;color:#b42318}
</style>
<script defer src="/js/newcombe-two-proportion.js"></script>
<script defer src="/js/wald-wilson-one-proportion.js"></script>

<h2>4. مخطط فترة الثقة ما يزال صالحًا</h2>
<p>كما في كل مرة: التقدير ± هامش الخطأ؛ ففي النسب يكون التقدير \(\hat p\)، وهامش الخطأ = القيمة الحرجة × الخطأ المعياري.</p>

<h2>5. الخطأ المعياري للنسبة</h2>
<div dir="ltr">\[\widehat{\operatorname{SE}}(\hat p)=\sqrt{\frac{\hat p(1-\hat p)}{n}}.\]</div>
<p>يقدّر هذا مقدار تغيّر نسبة العيّنة عبر العيّنات المستقلة المتكررة؛ أما الخطأ المعياري الحقيقي فيستخدم النسبة المجهولة \(p\) بدل \(\hat p\).</p>

<h2>6. صيغة فترة الثقة (فترة والد)</h2>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="صيغة فترة والد">\[\hat p\ \pm\ z_{1-\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}{n}}\]</div>
<p>هذه فترة والد المعروفة للعيّنات الكبيرة. وقد تكون تغطيتها الفعلية ضعيفة، خصوصًا مع العيّنات الصغيرة أو النسب القريبة من 0 أو 1، وكثيرًا ما تُفضَّل فترات ويلسون؛ والمختبر الثاني أدناه يبيّن ذلك بالحساب الدقيق.</p>

<h2>7. لماذا نستخدم قيم z الحرجة؟</h2>
<p>بخلاف فترات المتوسط، لا تستخدم فترات النسبة توزيع t؛ ففي ظل شروط مناسبة يكون توزيع المعاينة لنسبة العيّنة طبيعيًا تقريبًا، فنستخدم قيم z الحرجة.</p>

<h2>8. مثال محسوب</h2>
<p>لنفترض: <span dir="ltr">n = 500</span>، و<span dir="ltr">x = 310</span>، و<span dir="ltr">p̂ = 0.62</span>، ومستوى الثقة 95%.</p>
<h3>الخطوة 1: الخطأ المعياري</h3>
<div dir="ltr">\[\sqrt{\frac{0.62(0.38)}{500}}\approx0.0217071.\]</div>
<h3>الخطوة 2: القيمة الحرجة</h3>
<p>لفترة ثقة 95%: <span dir="ltr">z* = 1.96</span>.</p>
<h3>الخطوة 3: هامش الخطأ</h3>
<div dir="ltr">\[\operatorname{ME}=1.96(0.0217071)\approx0.04255.\]</div>
<h3>الخطوة 4: بناء الفترة</h3>
<div dir="ltr">\[0.62\pm0.04255\approx(0.57745,\ 0.66255).\]</div>
<p>أي <span dir="ltr">(0.5775, 0.6625)</span>، أو تقريبًا من 57.8% إلى 66.3%. وللمقارنة، تكون فترة ويلسون للبيانات نفسها <span dir="ltr">(0.5767, 0.6615)</span>، وهي قريبة جدًا هنا لأن العيّنة كبيرة والنسبة بعيدة عن الحدود.</p>

<h2>9. تفسير الفترة</h2>
<p>التفسير الصحيح: استخدمنا طريقة تلتقط نسبة المجتمع الحقيقية في نحو 95% من المرات عبر المعاينة المتكررة؛ وتشير الفترة إلى أن القيم المعقولة لنسبة المجتمع تقع بين نحو 57.8% و66.3%.</p>

<h2>10. شروط فترات النسبة</h2>
<h3>1. المعاينة العشوائية</h3>
<p>ينبغي أن تمثّل العيّنة المجتمع تمثيلًا معقولًا.</p>
<h3>2. الاستقلال</h3>
<p>ينبغي أن تكون المشاهدات مستقلة تقريبًا، ويُستخدم غالبًا شرط 10%: أن يكون حجم العيّنة أقل من نحو 10% من المجتمع عند المعاينة دون إرجاع.</p>
<h3>3. شرط النجاح والإخفاق</h3>
<div class="concept-box"><strong>شرط النجاح والإخفاق:</strong><p dir="ltr">n·p̂ ≥ 10 and n·(1 − p̂) ≥ 10</p></div>
<p>هذه قاعدة تقريبية مفيدة تدعم التقريب الطبيعي، لكنها لا تضمن تغطية دقيقة لفترة والد؛ ويبقى تصميم الدراسة الأصلي وافتراضات الاستقلال مهمين.</p>

<h2>11. فحص الشرط في مثالنا</h2>
<div dir="ltr">\[n\hat p=500(0.62)=310\ge10,\qquad n(1-\hat p)=500(0.38)=190\ge10.\]</div>
<p>القيمتان تتجاوزان 10، فالشرط متحقق بسهولة.</p>

    <!-- مختبر التغطية الدقيقة (Batch #104، النسخة العربية) -->
    <section class="concept-box" id="esa-pcov-lab" data-locale="ar" aria-labelledby="esa-pcov-heading">
    <h2 id="esa-pcov-heading">مختبر تفاعلي: التغطية الدقيقة لفترات النسبة</h2>
    <p>تصف عبارة «ثقة 95%» نسبة المرات التي <em>تلتقط</em> فيها طريقةُ البناء قيمةَ p الحقيقية. ولعدد ذي حدين يمكن حساب هذه النسبة تمامًا، بلا محاكاة، بجمع احتمالات كل النتائج التي تحتوي فتراتها على p:</p>
    <div class="esa-pcov-math" dir="ltr" tabindex="0" role="region" aria-label="صيغة التغطية الدقيقة">
    \[
    C(p)=\sum_{x=0}^{n}\binom{n}{x}p^{x}(1-p)^{n-x}\,\mathbf 1\{L(x)\le p\le U(x)\}.
    \]
    </div>
    <p>يقارن المختبر فترة والد، وفترة ويلسون، وفترة كلوبر–بيرسون «الدقيقة» التي حدودها مئينات من توزيع بيتا: \(L(x)=B_{\alpha/2}(x,\,n-x+1)\) و\(U(x)=B_{1-\alpha/2}(x+1,\,n-x)\).</p>
    <div class="esa-pcov-grid">
      <label for="esa-pcov-n">حجم العيّنة n<input id="esa-pcov-n" dir="ltr" type="number" min="1" max="1000" step="1" inputmode="numeric" value="30" aria-describedby="esa-pcov-error"></label>
      <label for="esa-pcov-p">النسبة الحقيقية p<input id="esa-pcov-p" dir="ltr" type="number" min="0.001" max="0.999" step="0.01" inputmode="decimal" value="0.1" aria-describedby="esa-pcov-error"></label>
      <label for="esa-pcov-level">مستوى الثقة الاسمي<select id="esa-pcov-level"><option value="90">90%</option><option value="95" selected>95%</option><option value="99">99%</option></select></label>
    </div>
    <div class="esa-pcov-controls"><button class="btn btn-outline" type="button" id="esa-pcov-small">n = 30, p = 0.1</button><button class="btn btn-outline" type="button" id="esa-pcov-half">n = 100, p = 0.5</button><button class="btn btn-outline" type="button" id="esa-pcov-rare">n = 20, p = 0.05</button></div>
    <p id="esa-pcov-error" role="alert" hidden></p>
    <section id="esa-pcov-results" aria-label="نتائج التغطية الدقيقة" role="status" aria-live="polite" aria-atomic="true">
      <div class="table-wrap"><table><caption>التغطية الدقيقة عند n وp المختارتين</caption>
        <thead><tr><th scope="col">الفترة</th><th scope="col">التغطية</th><th scope="col">مقارنةً بالمستوى الاسمي</th></tr></thead><tbody>
        <tr><th scope="row">والد</th><td><output id="esa-pcov-wald" dir="ltr">0.8085</output></td><td><output id="esa-pcov-wald-flag">أقل من المستوى الاسمي</output></td></tr>
        <tr><th scope="row">ويلسون</th><td><output id="esa-pcov-wilson" dir="ltr">0.9742</output></td><td><output id="esa-pcov-wilson-flag">عند المستوى الاسمي أو أعلى</output></td></tr>
        <tr><th scope="row">كلوبر–بيرسون</th><td><output id="esa-pcov-cp" dir="ltr">0.9922</output></td><td><output id="esa-pcov-cp-flag">عند المستوى الاسمي أو أعلى</output></td></tr>
      </tbody></table></div>
      <svg id="esa-pcov-chart" viewBox="0 0 460 200" role="img" aria-label="منحنيات التغطية الدقيقة" style="display:block;width:100%;height:auto;max-width:560px;direction:ltr"></svg>
      <p class="muted-mini">الأحمر = والد، والأخضر = ويلسون، والأزرق = كلوبر–بيرسون؛ والخط المتقطع هو المستوى الاسمي، والخط العمودي الباهت يحدد p المختارة.</p>
    </section>
    <p class="muted-mini">المنحنيات مسنّنة لأن n منفصلة: تقفز التغطية كلما عبرت p أحد أطراف الفترات. ومع <span dir="ltr">n = 30</span> و<span dir="ltr">p = 0.1</span> لا تغطي فترة والد «الاسمية 95%» إلا نحو 81% من المرات. وتبقى فترة ويلسون قريبة من 95% في المتوسط لكنها قد تنخفض تحته عند قيم معيّنة لـ p، أما كلوبر–بيرسون فلا تنخفض أبدًا تحت المستوى الاسمي، على حساب فترات أعرض. وتطابق القيم <code>scipy.stats.binom</code> و<code>scipy.stats.beta</code> حتى 10⁻¹². وعند n قريبة من 1,000 قد يستغرق التحديث الأول نحو ثانية.</p>
    </section>
    <style>
    #esa-pcov-lab,#esa-pcov-lab *{box-sizing:border-box}
    #esa-pcov-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
    #esa-pcov-lab label{display:block;font-weight:650;margin:6px 0}
    #esa-pcov-lab :is(input,select){display:block;width:100%;min-width:0;font:inherit;padding:8px;margin-top:4px;border:1px solid #777;border-radius:6px}
    #esa-pcov-lab .esa-pcov-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,160px),1fr));gap:4px 10px}
    #esa-pcov-lab .esa-pcov-controls{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
    #esa-pcov-lab .table-wrap,.esa-pcov-math{max-width:100%;overflow-x:auto}
    .esa-pcov-math{direction:ltr}
    #esa-pcov-lab [hidden]{display:none!important}
    #esa-pcov-lab :is(input,select,button):focus-visible,.esa-pcov-math:focus-visible{outline:2px solid #0f766e;outline-offset:3px}
    </style>
    <script defer src="/js/proportion-coverage-lab.js"></script>

<h2>12. ما الذي يؤثر في عرض الفترة؟</h2>
<p>تتكرر العوامل نفسها: مستوى الثقة، وحجم العيّنة، وتباين النسبة. فالعيّنات الأكبر تقلّل الخطأ المعياري، فتصبح الفترات أضيق (انظر <a href="/ar/inference/confidence-intervals/width-and-precision-what-controls/">عرض الفترة ودقتها</a>).</p>

<h2>13. متى يكون التباين أكبر؟</h2>
<p>تبلغ الكمية \(\hat p(1-\hat p)\) أقصى قيمة لها، وهي 0.25، عند \(\hat p=0.5\). فعند حجم عيّنة ثابت تعطي النسب القريبة من 50% أكبر الأخطاء المعيارية وأعرض فترات والد. أما قرب 0 أو 1 فقد تكون فترة والد ضيقة على نحو مضلل أو تتجاوز [0,1]، وفترة ويلسون أفضل غالبًا.</p>

<h2>14. لماذا تهم فترات النسبة؟</h2>
<p>تظهر فترات الثقة للنسب في كل مكان: الاستطلاعات السياسية، وأبحاث السوق، والدراسات الطبية، وضبط الجودة، واختبارات A/B؛ فهي من أكثر أدوات الاستدلال استخدامًا.</p>
<div class="concept-box"><strong>الرسالة الأساسية:</strong><p>تقدّر فترات الثقة للنسب نسبَ المجتمع بالجمع بين نسبة العيّنة وهامش خطأ مبني على خطئها المعياري. وفترة والد بسيطة لكن تغطيتها قد تكون ضعيفة، وفترات ويلسون وكلوبر–بيرسون بدائل أكثر موثوقية.</p></div>

<h2>15. ماذا بعد؟</h2>
<p>قدّرنا حتى الآن متوسطًا واحدًا ونسبة واحدة، لكن أسئلة بحثية كثيرة تقارن بين مجموعات. ويطوّر الدرس التالي فترات الثقة للفرق بين متوسطي مجتمعين مستقلين.</p>

<div class="summary-box">
<h2>خلاصة الدرس</h2>
<ul class="bullets">
<li>المعلمة المطلوبة هي نسبة المجتمع \(p\).</li>
<li>المقدِّر هو نسبة العيّنة \(\hat p\).</li>
<li>الخطأ المعياري المقدَّر \(\sqrt{\hat p(1-\hat p)/n}\).</li>
<li>تستخدم فترات النسبة قيم z الحرجة.</li>
<li>صيغة فترة والد: <span dir="ltr">p̂ ± z*·SE</span>.</li>
<li>يدعم شرط النجاح والإخفاق التقريب الطبيعي ولا يضمن التغطية.</li>
<li>العيّنات الأكبر تعطي فترات أضيق.</li>
<li>تغطية فترة والد قد تقل كثيرًا عن المستوى الاسمي؛ وويلسون أو كلوبر–بيرسون أفضل في العيّنات الصغيرة أو قرب الحدود.</li>
</ul>
</div>

<div class="lesson-nav">
<a class="btn btn-outline" href="/ar/inference/confidence-intervals/conditions-normality-clt-independence/">→ السابق: الشروط</a>
<a class="btn" href="/ar/inference/confidence-intervals/ci-for-difference-of-means-independent/">التالي: الفرق بين متوسطين ←</a>
</div>
</div></section>
