---
layout: default
title: ما فترة الثقة؟
description: شرح عربي متكامل لفترات الثقة وتفسير تغطيتها على المدى الطويل، مع تجربة تفاعلية لمحاكاة فترات الثقة للمتوسط.
permalink: /ar/inference/confidence-intervals/what-is-a-confidence-interval/
lang: ar
sidebar: false
translation_pair: confidence-interval-introduction
math: true
---
<style>
@media(max-width:760px){
 #main-content .content-narrow{max-width:100%;width:100%;min-width:0;overflow-x:clip}
 #main-content .content-narrow .table-wrap{display:block;width:100%;max-width:100%;overflow-x:auto}
}
#esa-ci-coverage-lab .esa-ci-chart-wrap, #esa-ci-coverage-lab .esa-ci-equation {direction:ltr}
#esa-ci-coverage-lab .esa-ci-recent {padding-right:1.4rem;padding-left:0;direction:ltr;text-align:left}
</style>
<section class="hero hero-section"><div class="hero-card">
  <div class="badge-row"><span class="badge">الاستدلال الإحصائي</span><span class="badge">فترات الثقة</span><span class="badge">المفاهيم الأساسية</span></div>
  <h1>ما فترة الثقة؟</h1>
  <p><a href="/inference/confidence-intervals/what-is-a-confidence-interval/" lang="en" dir="ltr">English — What Is a Confidence Interval?</a></p>
  <p class="lead">يقدّم التقدير النقطي قيمة واحدة لتقدير معلمة مجهولة، أما فترة الثقة فتقدّم مجالاً من القيم المتوافقة بدرجات متفاوتة مع البيانات، مع إظهار عدم اليقين الناتج عن المعاينة.</p>
  <div class="hero-actions"><a class="btn btn-outline" href="/ar/">الدروس العربية</a><a class="btn" href="/inference/confidence-intervals/" lang="en" dir="ltr">Confidence Intervals block (English)</a><a class="btn btn-outline" href="/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/" lang="en" dir="ltr">Next lesson (English)</a></div>
</div></section>
<section class="section"><div class="content-narrow">
  <h2>لماذا لا يكفي التقدير النقطي؟</h2>
  <p>افترض أن استطلاعاً لعينة من الناخبين أعطى تقديراً بأن <strong>62%</strong> يؤيدون سياسة معينة. هذه النسبة تلخّص بيانات العينة، لكنها لا تُبيّن وحدها مدى دقة التقدير.</p>
  <div class="example-box"><p>التقدير النقطي = <span dir="ltr">62%</span></p></div>
  <p>لو سحبنا عينات أخرى من المجتمع نفسه، لتغيّر التقدير من عينة إلى أخرى. لهذا ينشأ عدم يقين بسبب تقلب المعاينة، حتى لو كانت عملية جمع البيانات سليمة.</p>

  <h2>لماذا نحتاج إلى مجال من القيم؟</h2>
  <p>بدلاً من الإبلاغ عن قيمة واحدة، يمكن عرض فترة من القيم المعقولة للمعلمة المجهولة في ضوء البيانات وافتراضات طريقة الاستدلال.</p>
  <div class="example-box"><p dir="ltr">62% (95% CI: 58%–66%)</p></div>
  <p>يسمى هذا المجال <strong>فترة ثقة</strong>. المثال توضيحي؛ ولا يمكن استنتاج حدود الفترة من التقدير النقطي وحده دون معلومات عن حجم العينة وتصميمها وطريقة الحساب.</p>

  <h2>التعريف</h2>
  <div class="concept-box"><strong>تعريف:</strong><p>فترة الثقة هي فترة تُبنى من بيانات العينة وفق إجراء إحصائي صُمّم بحيث يحتوي المعلمة الحقيقية للمجتمع بنسبة تغطية محددة عند تكرار المعاينة في ظل افتراضات النموذج.</p></div>

  <h2>الفكرة الأساسية</h2>
  <p>لا نقول إن معلمة المجتمع تساوي <span dir="ltr">62%</span> على وجه اليقين؛ بل نبيّن أن مجالاً مثل <span dir="ltr">58%–66%</span> يتضمن قيماً متوافقة بصورة معقولة مع البيانات، وفق الطريقة والافتراضات المستخدمة.</p>
  <p>هذه الصياغة تُظهر عدم اليقين بدلاً من إخفائه خلف رقم وحيد.</p>

  <h2>مم تتكوّن فترة الثقة؟</h2>
  <p>تستند فترات الثقة عادةً إلى عناصر مترابطة:</p>
  <ul class="bullets">
    <li><strong>تقدير نقطي:</strong> قيمة محسوبة من العينة لتقدير المعلمة.</li>
    <li><strong>توزيع المعاينة:</strong> وصف تغير المقدّر عبر العينات المتكررة.</li>
    <li><strong>خطأ معياري:</strong> مقياس لتقلب المقدّر تحت نموذج المعاينة.</li>
    <li><strong>مستوى ثقة:</strong> معدل تغطية مستهدف، مثل <span dir="ltr">95%</span>.</li>
  </ul>
  <p>تختلف الصيغ الدقيقة وشروط صلاحيتها بحسب نوع المعلمة والنموذج والتصميم وطريقة إنشاء الفترة.</p>

  <h2>صورة ذهنية: نكرر سحب العينات</h2>
  <p>تخيّل أننا نسحب عينات عشوائية مستقلة مراراً من المجتمع نفسه، وننشئ فترة ثقة من كل عينة باستخدام الإجراء ذاته. ستشمل بعض الفترات المعلمة الحقيقية، بينما لن تشملها فترات أخرى. وإذا كان إجراء فترة الثقة ذا تغطية صحيحة مقدارها <span dir="ltr">95%</span>، فإنه سيشمل المعلمة في نحو 95% من العينات على المدى الطويل.</p>
  <div class="concept-box"><strong>الفكرة الجوهرية:</strong><p>خاصية الثقة تصف أداء <em>طريقة إنشاء الفترات عبر العينات المتكررة</em>، لا حركة المعلمة الحقيقية داخل فترة معينة بعد حسابها.</p></div>

  <!-- Shared statistical engine with the English lesson; Arabic text is localized. -->
  <section id="esa-ci-coverage-lab" class="concept-box esa-ci-lab" role="group" aria-labelledby="esa-ci-lab-heading" style="max-width:100%;min-width:0;overflow-wrap:anywhere">
    <h2 id="esa-ci-lab-heading">مختبر تفاعلي: تغطية فترات الثقة</h2>
    <p>نفترض سحب عينات مستقلة، حجم كل منها <span dir="ltr">n</span>، من مجتمع طبيعي بمتوسط حقيقي ثابت <span dir="ltr">μ = 0</span> وانحراف معياري مجتمعي <strong>معلوم</strong> <span dir="ltr">σ = 1</span>. نبني لكل عينة فترة ثقة ثنائية الطرف من نوع <span dir="ltr">z</span>.</p>
    <p>لزيادة سرعة المحاكاة، يُولَّد متوسط كل عينة مباشرةً من توزيعه الطبيعي الدقيق، وهو مكافئ إحصائياً لحساب متوسط <span dir="ltr">n</span> قيم مستقلة من التوزيع <span dir="ltr">N(0,1)</span> في هذا النموذج.</p>
    <p>صيغة الفترة هي <span class="esa-ci-equation esa-math-ltr" dir="ltr">\( \bar X \pm z_{1-\alpha/2}/\sqrt{n} \)</span>. تحت الافتراضات المذكورة، تساوي التغطية النظرية طويلة الأمد مستوى الثقة المختار.</p>
    <div class="esa-ci-controls">
      <div><label for="esa-ci-confidence">مستوى الثقة</label><select id="esa-ci-confidence"><option value="90">90%</option><option value="95" selected>95%</option><option value="99">99%</option></select></div>
      <div><label for="esa-ci-n">حجم كل عينة (n)</label><select id="esa-ci-n"><option value="10">10</option><option value="30" selected>30</option><option value="100">100</option><option value="300">300</option></select></div>
    </div>
    <div class="esa-ci-buttons">
      <button class="btn" type="button" id="esa-ci-run-100">إنشاء 100 فترة إضافية</button>
      <button class="btn btn-outline" type="button" id="esa-ci-run-500">إنشاء 500 فترة إضافية</button>
      <button class="btn btn-outline" type="button" id="esa-ci-reset">إعادة ضبط المحاكاة</button>
    </div>
    <div class="esa-ci-summary" role="status" aria-live="polite" aria-atomic="true">
      <p><strong>إجمالي الفترات:</strong> <span id="esa-ci-total">0</span> · <strong>تشمل المتوسط الحقيقي:</strong> <span id="esa-ci-hit">0</span> · <strong>لا تشمله:</strong> <span id="esa-ci-miss">0</span></p>
      <p><strong>التغطية المشاهدة:</strong> <span id="esa-ci-observed">—</span> · <strong>التغطية الاسمية:</strong> <span id="esa-ci-nominal">95%</span></p>
      <p><strong>نصف عرض الفترة:</strong> <span id="esa-ci-halfwidth">—</span> (مع <span dir="ltr">σ = 1</span> المعلوم، وهو ثابت عند تثبيت الإعدادات)</p>
    </div>
    <div class="esa-ci-chart-wrap" dir="ltr">
      <svg id="esa-ci-chart" viewBox="0 0 640 344" role="img" aria-label="أحدث فترات الثقة؛ الخط الرأسي يمثل المتوسط الحقيقي الثابت عند الصفر">
        <rect x="52" y="17" width="536" height="302" fill="none" stroke="currentColor" opacity=".2"/>
        <line x1="320" y1="18" x2="320" y2="320" stroke="currentColor" stroke-width="2" stroke-dasharray="3 4"/>
        <text x="320" y="337" fill="currentColor" font-size="14" text-anchor="middle">μ = 0</text>
        <g id="esa-ci-intervals"></g>
      </svg>
    </div>
    <p class="muted-mini">يعرض المخطط <strong>آخر 20 فترة</strong> فقط، بينما تعتمد نسبة التغطية المحسوبة على <strong>جميع</strong> الفترات المولدة. الخط الأخضر المتصل يدل على فترة تشمل المتوسط الحقيقي، والخط البرتقالي المتقطع يدل على فترة لا تشمله.</p>
    <p class="muted-mini"><strong>أحدث خمس فترات:</strong></p>
    <ol id="esa-ci-recent" class="esa-ci-recent" aria-label="أحدث خمس نتائج لفترات الثقة" dir="ltr"></ol>
    <p class="muted-mini">تتقلب التغطية المشاهدة عشوائياً حول المستوى الاسمي، ولا يلزم أن تطابقه في محاكاة صغيرة. عند ثبات مستوى الثقة، يؤدي ازدياد حجم العينة إلى تضييق الفترة، لكنه لا يغير تغطيتها النظرية في هذا النموذج الطبيعي بانحراف معياري معلوم. هذا المثال لا يضمن التغطية نفسها مع بيانات غير طبيعية أو عينات تابعة أو انحراف معياري مجهول أو انحياز في الاختيار.</p>
  </section>
    <style>
      #esa-ci-coverage-lab {max-width:100%;box-sizing:border-box;min-width:0}
      #esa-ci-coverage-lab * {box-sizing:border-box}
      #esa-ci-coverage-lab .esa-ci-equation {display:inline-block;max-width:100%;overflow-x:auto;vertical-align:middle}
      #esa-ci-coverage-lab .esa-ci-controls {
        display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,190px),1fr));
        gap:.9rem;margin:1rem 0
      }
      #esa-ci-coverage-lab .esa-ci-controls > div {min-width:0}
      #esa-ci-coverage-lab label {display:block;font-weight:650;margin-bottom:.35rem}
      #esa-ci-coverage-lab select {
        width:100%;max-width:100%;padding:.65rem;border:1px solid #888;
        border-radius:.4rem;background:var(--surface,#fff);color:inherit;font:inherit
      }
      #esa-ci-coverage-lab .esa-ci-buttons {display:flex;flex-wrap:wrap;gap:.6rem;margin:1rem 0}
      #esa-ci-coverage-lab button {max-width:100%;white-space:normal;text-align:center}
      #esa-ci-coverage-lab .esa-ci-summary {
        padding:.75rem 1rem;border:1px solid #888;border-radius:.5rem;margin:1rem 0;
        overflow-wrap:anywhere
      }
      #esa-ci-coverage-lab .esa-ci-summary p {margin:.4rem 0}
      #esa-ci-coverage-lab .esa-ci-chart-wrap {width:100%;max-width:100%;min-width:0;overflow:hidden}
      #esa-ci-coverage-lab #esa-ci-chart {display:block;width:100%;height:auto;max-width:100%}
      #esa-ci-coverage-lab .esa-ci-recent {padding-left:1.4rem;margin-top:.4rem;overflow-wrap:anywhere}
      #esa-ci-coverage-lab .esa-ci-recent li {margin:.25rem 0}
      @media print {
        #esa-ci-coverage-lab .esa-ci-buttons,#esa-ci-coverage-lab .esa-ci-controls {display:none}
        #esa-ci-coverage-lab .esa-ci-chart-wrap {max-width:500px}
      }
    </style>
  <script src="/js/confidence-interval-coverage.js" defer></script>

  <h2>ماذا تعني ثقة 95%؟</h2>
  <p>إن مستوى <span dir="ltr">95%</span> شائع الاستخدام، لكن يجب تفسيره بدقة. في التفسير التكراري الكلاسيكي، لا يجوز بعد ملاحظة فترة ثقة معينة القول إن احتمال وقوع المعلمة الثابتة داخل هذه الفترة يساوي <span dir="ltr">95%</span>.</p>
  <div class="example-box"><p><strong>التفسير غير الصحيح:</strong> هناك احتمال 95% أن المعلمة داخل الفترة المحسوبة بالفعل.</p></div>
  <div class="example-box"><p><strong>التفسير الصحيح:</strong> لو كررنا المعاينة وبناء الفترة بالإجراء نفسه في الظروف المفترضة، لاحتوت نحو 95% من الفترات المعلمة الحقيقية على المدى الطويل.</p></div>
  <p>تختلف فترات المصداقية في الاستدلال البايزي عن فترات الثقة التكرارية؛ ولا ينبغي الخلط بين تفسيري النسبتين.</p>

  <h2>المعلمة ثابتة والفترة تتغير</h2>
  <ul class="bullets">
    <li>تُعامل معلمة المجتمع بوصفها <strong>ثابتة ولكن مجهولة</strong> في الاستدلال التكراري.</li>
    <li>تتغير حدود فترة الثقة قبل سحب العينة لأنها تعتمد على إحصاءات عشوائية.</li>
    <li>بعد مشاهدة البيانات، تكون الفترة المحسوبة محددة؛ إما أنها تشمل المعلمة الحقيقية وإما لا تشملها.</li>
  </ul>
  <p>إذن مصدر العشوائية هنا هو آلية المعاينة، لا تغير المعلمة بين عينات المجتمع نفسه.</p>

  <h2>مثال استطلاع رأي</h2>
  <p>لنفترض أن نسبة التأييد المقدّرة من العينة هي <span dir="ltr">p̂ = 0.62</span>، وأن إجراءً ملائماً أنتج فترة <span dir="ltr">(0.58, 0.66)</span>. يشير ذلك إلى أن القيم بين <span dir="ltr">58%</span> و<span dir="ltr">66%</span> معقولة وفق البيانات والنموذج. هذا مثال إيضاحي، وليس نتيجة استطلاع فعلي أو ضماناً بتغطية 95% لأي تصميم معاينة.</p>

  <h2>لماذا تكون بعض الفترات واسعة؟</h2>
  <p>تظهر فترات واسعة غالباً مع صغر العينات أو ازدياد التشتت أو زيادة الخطأ المعياري، كما أن طلب مستوى ثقة أعلى يؤدي عادةً إلى اتساع الفترة عند ثبات بقية العوامل. عرض الفترة الأكبر يعني دقة أقل من حيث تحديد نطاق المعلمة.</p>

  <h2>لماذا تكون فترات أخرى ضيقة؟</h2>
  <p>تضيق الفترات عادةً مع زيادة حجم عينة فعالة أو انخفاض التشتت أو انخفاض الخطأ المعياري، عند ثبات بقية العوامل والطريقة المستخدمة. الفترة الأضيق تعني دقة أعلى، لكنها ليست دليلاً تلقائياً على غياب الانحياز أو صحة افتراضات النموذج.</p>

  <h2>فترة الثقة مقارنة بالتقدير النقطي</h2>
  <div class="table-wrap"><table><thead><tr><th>التقدير النقطي</th><th>فترة الثقة</th></tr></thead>
  <tbody><tr><td>قيمة واحدة</td><td>مجال من القيم</td></tr>
  <tr><td>ملخص مركزي للتقدير</td><td>التقدير مع إظهار عدم يقينه</td></tr>
  <tr><td>لا يوضح دقة التقدير وحده</td><td>تبيّن حدود الفترة درجة الدقة تحت الافتراضات</td></tr></tbody></table></div>

  <h2>لماذا يفضّل الباحثون الإبلاغ عن فترات الثقة؟</h2>
  <p>تساعد فترات الثقة على عرض <strong>حجم الأثر المقدَّر</strong>، ودقة التقدير، وعدم اليقين الناشئ عن المعاينة، ومجال القيم المعقول للمعلمة. لذلك تكون غالباً أكثر إفادة من تقديم التقدير النقطي وحده.</p>

  <h2>فترات الثقة واتخاذ القرار</h2>
  <p>عند تقييم سياسة أو تدخل أو نتيجة علمية، لا يكفي أحياناً النظر إلى القيمة المقدرة وحدها. يساعد مجال عدم اليقين على تقييم النتائج المحتملة وأهمية الفروق عملياً، مع مراعاة تصميم الدراسة ومخاطر الانحياز.</p>

  <h2>طريقة التفكير بفترات الثقة</h2>
  <p>يتحوّل السؤال من «ما القيمة الدقيقة للمعلمة؟» إلى «ما القيم المتوافقة بصورة معقولة مع بياناتنا وطريقة التحليل؟». هذا المنظور أقرب إلى واقع الاستدلال من عينات محدودة.</p>

  <h2>الصورة العامة</h2>
  <p>تجمع فترات الثقة بين التقدير وعدم اليقين في نتيجة واحدة قابلة للتفسير. وفي الدروس التالية سنتعلم طرق إنشائها للمتوسطات والنسب والفروق، والشروط التي تحدد صلاحية كل طريقة.</p>
  <div class="concept-box"><strong>الرسالة الأساسية:</strong><p>فترة الثقة مجال يُستخلص من بيانات العينة لتقدير معلمة مجهولة، وله خاصية تغطية على المدى الطويل في ظل شروط الإجراء المستخدم.</p></div>

  <h2>ماذا بعد؟</h2>
  <p>تتبع كثير من فترات الثقة النموذج التعليمي <span dir="ltr">point estimate ± margin of error</span>، مع وجود أساليب أكثر تعقيداً قد تكون غير متناظرة. يشرح الدرس التالي البنية العامة للفترات وكيفية تفسير الخطأ المعياري والقيم الحرجة.</p>

  <div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
    <li>فترة الثقة تعبّر عن عدم اليقين حول التقدير.</li>
    <li>تقدّم مجالاً من القيم المتوافقة مع بيانات العينة.</li>
    <li>تعتمد الصيغ الشائعة على المقدّر وتوزيع المعاينة والخطأ المعياري.</li>
    <li>يشير مستوى ثقة 95% إلى أداء طريقة بناء الفترة عبر العينات المتكررة.</li>
    <li>المعلمة ثابتة في التفسير التكراري، بينما تتغير الفترة قبل المعاينة.</li>
    <li>الفترات الواسعة أقل دقة من الضيقة عند تساوي الظروف الأخرى.</li>
    <li>فترة الثقة أكثر إفادة عادةً من التقدير النقطي وحده.</li>
  </ul></div>
  <div class="lesson-nav"><a class="btn btn-outline" href="/ar/">← قائمة الدروس العربية</a><a class="btn" href="/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/" lang="en" dir="ltr">Next: Interval Blueprint (English) →</a></div>
</div></section>
