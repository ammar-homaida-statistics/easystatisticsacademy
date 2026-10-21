---
layout: default
title: المتوسط الحسابي والوسيط — مقارنة عملية
description: شرح عربي شامل للفروق بين المتوسط الحسابي والوسيط، والقيم المتطرفة والالتواء، مع مختبر تفاعلي للمقارنة الدقيقة.
permalink: /ar/descriptive/center/mean-vs-median/
lang: ar
sidebar: false
translation_pair: mean-median
math: true
---
<style>
#esa-mean-median-explorer {box-sizing:border-box;width:100%;max-width:100%;min-width:0;overflow-x:clip;overflow-wrap:anywhere}
#esa-mean-median-explorer * {box-sizing:border-box}
#esa-mean-median-explorer .esa-mm-controls {display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:1rem;margin:1rem 0}
#esa-mean-median-explorer label {display:block;font-weight:650;margin-bottom:.35rem}
#esa-mean-median-explorer textarea,#esa-mean-median-explorer input {display:block;width:100%;min-width:0;max-width:100%;padding:.65rem;border:1px solid #888;border-radius:.35rem;color:inherit;background:var(--surface,#fff);font:inherit;direction:ltr;text-align:left}
#esa-mean-median-explorer .table-wrap,.content-narrow .table-wrap {max-width:100%;overflow-x:auto}
#esa-mean-median-explorer #esa-mm-error {color:#b91c1c;font-weight:650;overflow-wrap:anywhere}
#esa-mean-median-explorer #esa-mm-chart {overflow:hidden!important;direction:ltr}
#esa-mean-median-explorer #esa-mm-chart[hidden]{display:none!important}
@media(max-width:760px){#main-content .content-narrow{width:100%;max-width:100%;min-width:0;overflow-x:clip}}
</style>

<section class="hero hero-section"><div class="hero-card">
  <div class="badge-row"><span class="badge">الإحصاء الوصفي</span><span class="badge">مقاييس النزعة المركزية</span><span class="badge">المقارنة والتفسير</span></div>
  <h1>المتوسط الحسابي والوسيط: متى نستخدم كلاً منهما؟</h1>
  <p><a href="/descriptive/center/mean-vs-median/" lang="en" dir="ltr">English — Mean vs Median</a></p>
  <p class="lead">يُعدّ المتوسط الحسابي والوسيط من أشهر مقاييس النزعة المركزية. يهدف كلاهما إلى وصف مركز البيانات أو قيمتها النموذجية، لكن طريقة الحساب والاستجابة للقيم المتطرفة تختلف بينهما. ويتوقف اختيار المقياس المناسب على طبيعة البيانات والغرض من التحليل.</p>
  <div class="hero-actions"><a class="btn btn-outline" href="/ar/">فهرس الدروس العربية</a><a class="btn" href="/descriptive/center/mode/" lang="en" dir="ltr">Previous: Mode (English)</a><a class="btn btn-outline" href="/descriptive/center/weighted-mean/" lang="en" dir="ltr">Next: Weighted Mean (English)</a></div>
</div></section>

<section class="section"><div class="content-narrow">
  <h2>الأهداف التعليمية</h2>
  <p>بعد هذا الدرس ستتمكن من مقارنة المتوسط الحسابي بالوسيط، وشرح سبب اختلافهما، وفهم أثر القيم المتطرفة في كل منهما، واختيار مقياس مناسب لمركز التوزيع، واستخدام المقارنة لفهم الالتواء بحذر.</p>

  <h2>لماذا نقارن بين المتوسط والوسيط؟</h2>
  <p>قد يُعطي المقياسان قيمتين متقاربتين في بعض مجموعات البيانات، وقد تختلفان اختلافاً كبيراً في مجموعات أخرى. وإذا اكتفينا بمقياس غير ملائم فقد ننقل صورة مضللة عن المستوى النموذجي للبيانات.</p>
  <div class="concept-box"><strong>الفكرة الأساسية:</strong><p>يستخدم المتوسط الحسابي مقادير <strong>جميع المشاهدات</strong>، بينما يعتمد الوسيط على <strong>موقع القيمة الوسطى بعد ترتيب البيانات</strong>.</p></div>

  <h2>مراجعة سريعة: تعريف المقياسين</h2>
  <div class="table-wrap"><table>
    <thead><tr><th scope="col">المقياس</th><th scope="col">التعريف</th><th scope="col">الصيغة أو القاعدة</th></tr></thead>
    <tbody><tr><th scope="row">المتوسط الحسابي</th><td>مجموع القيم مقسوماً على عددها</td><td dir="ltr">\( \bar{x}=\frac{1}{n}\sum_{i=1}^n x_i \)</td></tr>
    <tr><th scope="row">الوسيط</th><td>قيمة المنتصف في البيانات المرتبة تصاعدياً</td><td>إذا كان العدد فردياً: القيمة الوسطى. وإذا كان زوجياً: متوسط القيمتين الوسطيتين.</td></tr></tbody>
  </table></div>
  <p>ترمز <span dir="ltr">n</span> إلى عدد المشاهدات. يمكن أن يُحسب المتوسط والوسيط من عينة أو من بيانات مجتمع كامل، لكن التفسير يعتمد على السياق.</p>

  <h2>مجموعة بيانات من دون قيم متطرفة</h2>
  <p>انظر إلى القيم المرتبة الآتية:</p>
  <div class="example-box" dir="ltr">10, 12, 14, 16, 18</div>
  <p>المتوسط الحسابي:</p>
  <div dir="ltr">\[ \bar{x}=\frac{10+12+14+16+18}{5}=14 \]</div>
  <p>والوسيط هو القيمة الثالثة بعد الترتيب، أي <strong>14</strong>. في هذه المجموعة المتناظرة يتساوى المقياسان.</p>
  <img src="{{ 'descriptive/images/mean-equals-median.png' | relative_url }}" alt="رسم يوضح تساوي المتوسط والوسيط في مثال لتوزيع متناظر" style="margin-top:15px;max-width:100%;height:auto">

  <h2>لماذا يتفقان كثيراً؟</h2>
  <p>في التوزيعات المتناظرة حول مركز، قد تتوازن القيم على جانبي المركز، فيتساوى المتوسط والوسيط أو يتقاربان. لكن التناظر لا يضمن أن يتساويا تماماً في كل عينة محدودة.</p>

  <h2>مجموعة بيانات تتضمن قيمة متطرفة</h2>
  <p>استبدل الآن القيمة الأخيرة من المثال السابق بالقيمة <strong>100</strong>:</p>
  <div class="example-box" dir="ltr">10, 12, 14, 16, 100</div>
  <p>المتوسط الحسابي الجديد:</p>
  <div dir="ltr">\[ \bar{x}=\frac{10+12+14+16+100}{5}=30.4 \]</div>
  <p>أما الوسيط فما يزال <strong>14</strong>. جذبت القيمة الكبيرة المتوسط نحو الأعلى، بينما بقي موقع القيمة الوسطى ثابتاً في هذا المثال.</p>
  <img src="{{ 'descriptive/images/outlier-pulls-mean.png' | relative_url }}" alt="رسم يبيّن تأثير القيمة المتطرفة في المتوسط أكثر من الوسيط" style="margin-top:15px;max-width:100%;height:auto">

  <section id="esa-mean-median-explorer" class="concept-box" role="group" aria-labelledby="esa-mm-title" style="max-width:100%;min-width:0;overflow-wrap:anywhere">
    <h2 id="esa-mm-title">مختبر تفاعلي: المقارنة بين المتوسط والوسيط</h2>
    <p>أدخل ثلاث مشاهدات على الأقل، ثم استبدل <strong>واحدة من أكبر القيم الأصلية</strong> بقيمة جديدة. قارن المقياسين قبل التغيير وبعده. هذا مثال تعليمي على الحساسية للقيم الكبيرة، وليس توصية بحذف البيانات أو تعديلها في التحليل الحقيقي.</p>
    <div class="esa-mm-controls">
      <div><label for="esa-mm-sample">القيم الأصلية (من 3 إلى 40 عدداً)</label><textarea id="esa-mm-sample" rows="2" spellcheck="false" aria-describedby="esa-mm-guidance" dir="ltr">2, 4, 6, 8, 10</textarea></div>
      <div><label for="esa-mm-extreme">استبدل إحدى أكبر القيم بـ</label><input id="esa-mm-extreme" type="text" value="100" inputmode="decimal" autocomplete="off" aria-describedby="esa-mm-guidance" dir="ltr"></div>
    </div>
    <p id="esa-mm-guidance" class="muted-mini">استخدم النقطة للفصل العشري، وافصل المشاهدات بفاصلة إنجليزية أو مسافة أو فاصلة منقوطة. يجب أن تكون القيم منتهية وألا تتجاوز قيمتها المطلقة ملياراً. اكتب الأرقام بصيغة <span dir="ltr">0–9</span>.</p>
    <button class="btn btn-outline" type="button" id="esa-mm-reset">إعادة المثال الافتراضي</button>
    <p id="esa-mm-error" role="alert" aria-live="polite" hidden></p>
    <div id="esa-mm-results">
      <div class="table-wrap"><table>
        <caption>المتوسط والوسيط قبل الاستبدال وبعده</caption>
        <thead><tr><th scope="col">المقياس</th><th scope="col">الأصل</th><th scope="col">بعد التغيير</th><th scope="col">مقدار التغير</th></tr></thead>
        <tbody>
          <tr><th scope="row">المتوسط الحسابي</th><td id="esa-mm-mean-before">—</td><td id="esa-mm-mean-after">—</td><td id="esa-mm-mean-change">—</td></tr>
          <tr><th scope="row">الوسيط</th><td id="esa-mm-median-before">—</td><td id="esa-mm-median-after">—</td><td id="esa-mm-median-change">—</td></tr>
        </tbody>
      </table></div>
      <p id="esa-mm-explainer" aria-live="polite"></p>
    </div>
    <svg id="esa-mm-chart" viewBox="0 0 680 215" role="img" aria-label="مخطط نقطي يقارن البيانات الأصلية والمعدّلة" style="display:block;width:100%;max-width:100%;height:auto;overflow:visible" dir="ltr"><g id="esa-mm-points"></g></svg>
    <p class="muted-mini">تمثل كل نقطة مشاهدة واحدة، ويُظهر الإزاحة الرأسية الصغيرة القيم المتكررة. ويُستخدم المقياس الأفقي نفسه للمجموعتين؛ وقد تضغط القيمة المتطرفة باقي النقاط بصرياً.</p>
    <p class="muted-mini"><strong>تنبيه تفسيري:</strong> قد يتغير الوسيط أيضاً، خصوصاً مع العينات الصغيرة أو الاستبدالات التي تغير ترتيب القيم الوسطى. ولا يكفي الفرق بين المتوسط والوسيط وحده للحكم على شكل التوزيع.</p>
  </section>
  <script src="/js/mean-median-explorer.js" defer></script>

  <h2>الفرق الجوهري</h2>
  <div class="table-wrap"><table><thead><tr><th>المتوسط الحسابي</th><th>الوسيط</th></tr></thead><tbody>
  <tr><td>يعتمد على جميع القيم ومقاديرها</td><td>يعتمد على الترتيب والقيم الوسطى</td></tr>
  <tr><td>حساس للقيم المتطرفة</td><td>أكثر مقاومة للقيم المتطرفة</td></tr>
  <tr><td>يمثل نقطة التوازن الحسابية</td><td>يمثل موقع المنتصف في الترتيب</td></tr>
  <tr><td>قد يتأثر بشدة بالالتواء</td><td>غالباً أقل تأثراً بالالتواء</td></tr>
  </tbody></table></div>

  <h2>المقاومة للقيم المتطرفة</h2>
  <p>نسمّي المقياس <strong>مقاوماً</strong> عندما لا يتأثر بشدة بتغيير عدد صغير من المشاهدات إلى قيم متطرفة جداً. الوسيط مقياس مقاوم نسبياً، أما المتوسط الحسابي فغير مقاوم بهذه الصورة؛ لذلك يشيع استخدام الوسيط في البيانات الملتوية.</p>

  <h2>التوزيعات المتناظرة</h2>
  <p>عندما يكون التوزيع متناظراً تقريباً ولا تهيمن قيم شاذة، يمكن أن يلخّص المتوسط والوسيط مركز البيانات بصورة جيدة، وغالباً ما يكونان متقاربين.</p>

  <h2>التوزيع الملتوي إلى اليمين</h2>
  <p>قد تولّد قلة من القيم الكبيرة ذيلاً طويلاً نحو اليمين. ومن الأمثلة الشائعة على ذلك الدخول والثروات وأسعار العقارات وبعض النفقات الطبية. يكون المتوسط <strong>غالباً</strong> أكبر من الوسيط، وقد يكون الوسيط أنسب لوصف قيمة نموذجية، لكن هذه علاقة إرشادية وليست قاعدة مطلقة.</p>

  <h2>التوزيع الملتوي إلى اليسار</h2>
  <p>عندما توجد قلة من القيم الصغيرة جداً، يمتد الذيل نحو اليسار. وفي كثير من الحالات يكون المتوسط أقل من الوسيط، بينما يبقى الوسيط أكثر مقاومة للقيم المتطرفة.</p>

  <h2>المتوسط والوسيط بوصفهما مؤشرين لشكل التوزيع</h2>
  <img src="{{ 'descriptive/images/mean-median-skewness.png' | relative_url }}" alt="مقارنة مواضع المتوسط والوسيط في توزيعات متناظرة وملتوية" style="margin-top:15px;max-width:100%;height:auto">
  <div class="table-wrap"><table><thead><tr><th>العلاقة التقريبية</th><th>ما قد تشير إليه</th></tr></thead><tbody>
  <tr><td dir="ltr">Mean ≈ Median</td><td>تناظر تقريبي محتمل</td></tr>
  <tr><td dir="ltr">Mean &gt; Median</td><td>التواء موجب أو قيم كبيرة مؤثرة</td></tr>
  <tr><td dir="ltr">Mean &lt; Median</td><td>التواء سالب أو قيم صغيرة مؤثرة</td></tr>
  </tbody></table></div>
  <p>هذه المؤشرات ليست اختباراً لشكل التوزيع. فهناك توزيعات غير متناظرة يتساوى فيها المتوسط والوسيط، لذا ينبغي الرجوع أيضاً إلى المدرج التكراري أو المخطط الصندوقي والسياق.</p>

  <h2>الدخل: مثال معروف</h2>
  <p>افترض أن الدخل السنوي لخمسة أشخاص، بالدولار، هو:</p>
  <div class="example-box" dir="ltr">30,000; 35,000; 40,000; 45,000; 500,000</div>
  <p>المجموع <span dir="ltr">650,000</span>، لذا المتوسط <span dir="ltr">130,000</span> دولار، بينما الوسيط <span dir="ltr">40,000</span> دولار. ترفع القيمة الأخيرة المتوسط كثيراً، مع أن أربعة أشخاص من الخمسة يقل دخل كل منهم عن المتوسط. ولهذا يُستخدم الدخل الوسيط كثيراً لتمثيل دخل الفرد النموذجي.</p>
  <img src="{{ 'descriptive/images/income-mean-vs-median.png' | relative_url }}" alt="رسم لتوزيع دخل يتضمن قيمة مرتفعة جداً تدفع المتوسط إلى الأعلى" style="margin-top:15px;max-width:100%;height:auto">

  <h2>متى نفضّل المتوسط الحسابي؟</h2>
  <ul class="bullets"><li>عندما تكون البيانات عددية ويكون المتوسط متسقاً مع سؤال البحث.</li><li>عندما يكون التوزيع قريباً من التناظر، ولا تهيمن القيم المتطرفة.</li><li>عندما نحتاج إلى استخدام مجاميع القيم أو خصائص المتوسط في تحليل لاحق.</li></ul>

  <h2>متى نفضّل الوسيط؟</h2>
  <ul class="bullets"><li>عندما يكون التوزيع ملتويًا بشدة أو توجد قيم متطرفة مؤثرة.</li><li>عندما نحتاج إلى وصف مشاهدة نموذجية بمقياس مقاوم.</li><li>عندما يكون ترتيب القيم أهم من الفروق في مقاديرها، مع مراعاة مستوى قياس المتغير.</li></ul>

  <h2>هل أحدهما أفضل دائماً؟</h2>
  <img src="{{ 'descriptive/images/mean-vs-median-decision-guide.png' | relative_url }}" alt="مخطط لاتخاذ قرار بشأن اختيار المتوسط أو الوسيط وفق شكل البيانات وهدف التحليل" style="margin-top:15px;max-width:100%;height:auto">
  <p>لا يوجد مقياس أفضل في جميع الظروف؛ فالقرار يعتمد على السؤال، وشكل التوزيع، ومستوى القياس، وطبيعة القيم المتطرفة. قد يكون من المفيد الإبلاغ عن كلا المقياسين مع وصف شكل البيانات.</p>

  <h2>أخطاء شائعة</h2>
  <ul class="bullets"><li>اعتبار المتوسط الحسابي الخيار الأفضل دائماً.</li><li>تجاهل القيم المتطرفة قبل اختيار مقياس المركز.</li><li>عرض مقياس واحد من دون فحص توزيع البيانات.</li><li>الاعتقاد بأن المتوسط والوسيط يجب أن يتساويا.</li><li>الجزم بوجود التواء اعتماداً على الفرق بينهما وحده.</li></ul>

  <h2>لماذا تهم هذه المقارنة؟</h2>
  <p>يمكن أن يؤدي تلخيص مجموعات البيانات بمقياس واحد غير مناسب إلى استنتاجات مضللة في الاقتصاد والصحة والتعليم وغيرها. الإحصاء الجيد لا يكتفي بحساب الصيغة، بل يختار الملخص الذي يجيب بدقة عن سؤال التحليل.</p>

  <h2>المقارنة باستخدام SPSS</h2>
  <p>يمكن حساب المتوسط والوسيط في تحليل واحد داخل <span dir="ltr">SPSS</span>:</p>
  <ol><li>اختر <span dir="ltr"><strong>Analyze → Descriptive Statistics → Frequencies</strong></span>.</li>
  <li>انقل المتغير العددي إلى خانة <span dir="ltr"><strong>Variable(s)</strong></span>.</li>
  <li>اضغط <span dir="ltr"><strong>Statistics…</strong></span>.</li>
  <li>اختر <span dir="ltr"><strong>Mean</strong></span> و<span dir="ltr"><strong>Median</strong></span> معاً.</li>
  <li>اضغط <span dir="ltr"><strong>Continue</strong></span> ثم <span dir="ltr"><strong>OK</strong></span>.</li></ol>
  <p>قارن النتائج، ثم ارجع إلى الرسم البياني لتجنب تفسير الالتواء بناءً على هذه المقارنة وحدها.</p>

  <h3>مثال بلغة Python</h3>
  <p>تحسب الشيفرة التالية المتوسط والوسيط لمثال الدخل السابق باستخدام مكتبة <span dir="ltr">statistics</span>:</p>
  <pre dir="ltr"><code>import statistics

income = [30000, 35000, 40000, 45000, 500000]
print("Mean =", statistics.mean(income))
print("Median =", statistics.median(income))</code></pre>

  <h3>مثال بلغة R</h3>
  <p>يمكن حساب القيمتين نفسيهما باستخدام الدالتين <span dir="ltr">mean</span> و<span dir="ltr">median</span>:</p>
  <pre dir="ltr"><code>income &lt;- c(30000, 35000, 40000, 45000, 500000)
mean(income)
median(income)</code></pre>

  <div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
    <li>يصف المتوسط والوسيط مركز البيانات بطريقتين مختلفتين.</li>
    <li>يستخدم المتوسط مقادير جميع المشاهدات، بينما يعتمد الوسيط على ترتيبها.</li>
    <li>يتأثر المتوسط بشدة بالقيم المتطرفة، والوسيط أكثر مقاومة لها.</li>
    <li>قد يختلف المقياسان في التوزيعات الملتوية؛ ويظل فحص الشكل ضرورياً.</li>
    <li>يعتمد اختيار المقياس على البيانات والهدف التحليلي، وليس على قاعدة واحدة مطلقة.</li>
    <li>يسمح المختبر التفاعلي بملاحظة الفروق عددياً وبصرياً دون تعديل البيانات الأصلية للمستخدم.</li>
  </ul></div>
  <div class="lesson-nav"><a class="btn btn-outline" href="/ar/">← الدروس العربية</a><a class="btn" href="/descriptive/center/mean-vs-median/" lang="en" dir="ltr">English version →</a></div>
</div></section>
