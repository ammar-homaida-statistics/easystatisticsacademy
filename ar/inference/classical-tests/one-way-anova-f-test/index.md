---
layout: default
title: تحليل التباين الأحادي واختبار F
description: "شرح عربي لتحليل التباين الأحادي (ANOVA): مقارنة متوسطات ثلاث مجموعات أو أكثر بإحصائية F، مع جدول ANOVA ودرجات الحرية وحجم الأثر η² ومختبر تفاعلي."
permalink: /ar/inference/classical-tests/one-way-anova-f-test/
lang: ar
sidebar: false
learning_resource: true
translation_pair: one-way-anova
---
<section class="hero hero-section"><div class="hero-card">
<h1>تحليل التباين الأحادي واختبار F</h1>
<p class="lead">كثيرًا ما يحتاج الباحث إلى مقارنة متوسطات ثلاث مجموعات أو أكثر في آن واحد. يقدّم تحليل التباين الأحادي (One-Way ANOVA) طريقة منهجية لتقرير ما إذا كان متوسط مجتمع واحد على الأقل يختلف عن البقية.</p>
<p><a href="/inference/classical-tests/one-way-anova-f-test/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/classical-tests/chi-square-homogeneity-test/">الدرس السابق: اختبار كاي تربيع للتجانس</a> · <a href="/ar/inference/classical-tests/two-sample-t-test-independent/">مجموعتان فقط: اختبار t لعينتين مستقلتين</a></p>
</div></section>
<section><div class="content-narrow">
<h2>1. مشكلة اختبارات t المتعددة</h2>
<p>لنفترض أن باحثين يقارنون متوسط درجات الاختبار لأربع طرق تدريس: A وB وC وD. يمكن إجراء اختبار t لكل زوج من الطرق، أي ستة اختبارات. لكن تكرار الاختبار يرفع احتمال ارتكاب خطأ من النوع الأول مرة واحدة على الأقل.</p>
<p>إذا كانت الاختبارات مستقلة وأُجري كل منها عند \(\alpha=0.05\)، فإن احتمال رفض صفري صحيح مرة واحدة على الأقل في ستة اختبارات هو \(1-0.95^6\approx0.265\). الاختبارات الزوجية ليست مستقلة تمامًا، لكن المشكلة تبقى قائمة.</p>
<div class="concept-box"><strong>الدافع الأساسي:</strong><p>يسمح تحليل التباين باختبار تساوي عدة متوسطات باختبار واحد شامل، فيضبط معدل الخطأ من النوع الأول لهذا السؤال الشامل عند \(\alpha\).</p></div>
<h2>2. ماذا يعني تحليل التباين؟</h2>
<p>ANOVA اختصار لـ <span lang="en" dir="ltr">Analysis of Variance</span>. ومع أن الهدف مقارنة المتوسطات، فإن الطريقة تعمل بتحليل مصادر التباين في البيانات.</p>
<h2>3. سؤال البحث والفرضيتان</h2>
<p>لدينا \(k\ge2\) من المجتمعات المستقلة متوسطاتها \(\mu_1,\mu_2,\ldots,\mu_k\)، ونريد معرفة ما إذا كانت جميعها متساوية:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="فرضيتا تحليل التباين">
\[
H_0:\ \mu_1=\mu_2=\cdots=\mu_k,\qquad H_a:\ \text{at least one } \mu_j \text{ differs.}
\]</div>
<p>الفرضية البديلة تعني أن متوسطًا واحدًا على الأقل يختلف. لاحظ أن تحليل التباين لا يحدد <em>أيّ</em> المتوسطات يختلف؛ إنما يختبر وجود دليل على أي اختلاف. ومع \(k=2\) يكافئ اختبار F اختبار t الثنائي ذا التباين المشترك، إذ \(F=t^2\).</p>
<h2>4. الفكرة الجوهرية: مصدران للتباين</h2>
<ul class="bullets">
<li><strong>التباين بين المجموعات:</strong> مدى ابتعاد متوسطات المجموعات عن المتوسط العام. كلما كبر، زاد احتمال أن تكون متوسطات المجتمعات مختلفة.</li>
<li><strong>التباين داخل المجموعات:</strong> التشتت الطبيعي للمشاهدات داخل كل مجموعة. وهو متوقع حتى عندما تتساوى متوسطات المجتمعات جميعها.</li>
</ul>
<div class="concept-box"><strong>منطق تحليل التباين:</strong><p>إذا كان التباين بين المجموعات أكبر بكثير من التباين داخلها، فمن غير المرجح أن تفسّر عشوائية المعاينة وحدها الفروق المشاهدة بين متوسطات المجموعات.</p></div>
<h2>5. مجاميع المربعات وإحصائية F</h2>
<p>إذا كان \(n_j\) حجم المجموعة \(j\) و\(\bar x_j\) متوسطها و\(\bar x\) المتوسط العام و\(N=\sum n_j\):</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="مجاميع المربعات وإحصائية F">
\[
SS_B=\sum_{j=1}^{k}n_j(\bar x_j-\bar x)^2,\qquad
SS_W=\sum_{j=1}^{k}\sum_{i=1}^{n_j}(x_{ij}-\bar x_j)^2,\qquad
SS_T=SS_B+SS_W,
\]
\[
F=\frac{MS_B}{MS_W}=\frac{SS_B/(k-1)}{SS_W/(N-k)}.
\]</div>
<p>إحصائية F نسبة بين متوسطَي مربعات، أي تقديرين للتباين: \(MS_W\) يقدّر تباين الخطأ \(\sigma^2\) دائمًا، و\(MS_B\) يقدّره أيضًا عندما تكون \(H_0\) صحيحة، ويميل إلى قيم أكبر عندما تختلف المتوسطات.</p>
<h2>6. جدول تحليل التباين ودرجات الحرية</h2>
<div class="table-wrap"><table><caption>بنية جدول تحليل التباين الأحادي</caption><thead><tr><th scope="col">المصدر</th><th scope="col">مجموع المربعات</th><th scope="col">درجات الحرية</th><th scope="col">متوسط المربعات</th></tr></thead><tbody>
<tr><th scope="row">بين المجموعات</th><td dir="ltr">SSB</td><td dir="ltr">k − 1</td><td dir="ltr">MSB</td></tr>
<tr><th scope="row">داخل المجموعات</th><td dir="ltr">SSW</td><td dir="ltr">N − k</td><td dir="ltr">MSW</td></tr>
<tr><th scope="row">الكلي</th><td dir="ltr">SST</td><td dir="ltr">N − 1</td><td>—</td></tr>
</tbody></table></div>
<p>درجتا الحرية هما \(k-1\) للبسط و\(N-k\) للمقام، حيث \(k\) عدد المجموعات و\(N\) الحجم الكلي للعينة.</p>
<h2>7. توزيع F والقيمة الاحتمالية</h2>
<p>تحت \(H_0\) ومع تحقق الافتراضات، تتبع الإحصائية توزيع \(F_{k-1,\,N-k}\). هذا التوزيع موجب دائمًا، وملتوٍ نحو اليمين، ويعتمد على درجتي الحرية. لذلك تُحسب القيمة الاحتمالية من <strong>الذيل الأعلى</strong> وحده: \(p=P(F_{k-1,N-k}\ge F_{\text{obs}})\). قيم F القريبة من 1 متسقة مع تساوي المتوسطات، وكلما كبرت F صغرت القيمة الاحتمالية. ولا يوجد حدّ ثابت لـ«F كبيرة»؛ فالحكم دائمًا بالمقارنة مع توزيع F بدرجتي الحرية المناسبتين.</p>
<div class="concept-box"><strong>قاعدة القرار:</strong><p>نرفض \(H_0\) إذا كانت \(p\le\alpha\)، ولا نرفضها إذا كانت \(p&gt;\alpha\). وعدم الرفض ليس دليلًا على تساوي المتوسطات.</p></div>
<h2>8. مثال محلول</h2>
<p>ثلاث مجموعات صغيرة: A = {4, 5, 6} وB = {5, 6, 7} وC = {8, 9, 10}. المتوسطات 5 و6 و9، والمتوسط العام \(\bar x=60/9\approx6.667\).</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="حسابات المثال المحلول">
\[
SS_B=3\left[(5-\tfrac{20}{3})^2+(6-\tfrac{20}{3})^2+(9-\tfrac{20}{3})^2\right]=26,\qquad SS_W=2+2+2=6,
\]
\[
MS_B=\frac{26}{2}=13,\quad MS_W=\frac{6}{6}=1,\quad F=13,\quad p=P(F_{2,6}\ge13)\approx0.006592 .
\]</div>
<p>عند \(\alpha=0.05\) نرفض تساوي متوسطات المجتمعات الثلاثة، بشرط تحقق الافتراضات. ويقيس <strong>حجم الأثر</strong> \(\eta^2=SS_B/SS_T\)، وهو هنا 26/32 = 0.8125، نسبة التباين الكلي في العينة المرتبطة بالانتماء إلى المجموعة. وهو مقياس وصفي متحيّز نحو الأعلى في العينات الصغيرة، فلا يُفسَّر بمعزل عن حجم العينة.</p>
<h2>9. مختبر تحليل التباين التفاعلي</h2>
<section id="esa-anova-lab" class="concept-box" data-locale="ar" aria-labelledby="esa-anova-title">
<h3 id="esa-anova-title">مستكشف تحليل التباين الأحادي</h3>
{% include lab-noscript.html %}
<p>أدخل <strong>المشاهدات الفردية</strong> لثلاث مجموعات مستقلة، وقارن التباين بين المجموعات بالتباين داخلها، بما في ذلك أحجام المجموعات غير المتساوية، باستخدام تحليل التباين الكلاسيكي بالتباين المشترك.</p>
<div class="esa-anova-fields">
<div><label for="esa-anova-a">مشاهدات المجموعة A</label><textarea id="esa-anova-a" dir="ltr" rows="2" spellcheck="false" aria-invalid="false" aria-describedby="esa-anova-error">4, 5, 6</textarea></div>
<div><label for="esa-anova-b">مشاهدات المجموعة B</label><textarea id="esa-anova-b" dir="ltr" rows="2" spellcheck="false" aria-invalid="false" aria-describedby="esa-anova-error">5, 6, 7</textarea></div>
<div><label for="esa-anova-c">مشاهدات المجموعة C</label><textarea id="esa-anova-c" dir="ltr" rows="2" spellcheck="false" aria-invalid="false" aria-describedby="esa-anova-error">8, 9, 10</textarea></div>
</div>
<div class="esa-anova-controls">
<button class="btn btn-outline" type="button" id="esa-anova-reset">إعادة المثال</button>
<button class="btn btn-outline" type="button" id="esa-anova-equal">متوسطات متساوية</button>
<button class="btn btn-outline" type="button" id="esa-anova-unequal">أحجام مجموعات غير متساوية</button>
<button class="btn btn-outline" type="button" id="esa-anova-constant">لا تباين داخل المجموعات</button>
</div>
<p id="esa-anova-error" role="alert" hidden></p>
<section id="esa-anova-results" aria-label="نتائج تحليل التباين" role="status" aria-live="polite" aria-atomic="true">
<h4>البيانات المشاهدة والمتوسطات</h4>
<svg id="esa-anova-chart" viewBox="0 0 410 220" role="img" aria-label="المشاهدات ومتوسطات المجموعات" dir="ltr"></svg>
<div class="table-wrap"><table><caption>ملخصات وصفية لكل مجموعة (الانحراف المعياري بقسمة n−1)</caption>
<thead><tr><th scope="col">المجموعة</th><th scope="col">n</th><th scope="col">المتوسط</th><th scope="col">الانحراف المعياري للعينة</th></tr></thead>
<tbody id="esa-anova-groups" dir="ltr"></tbody></table></div>
<div class="table-wrap"><table><caption>تجزئة تحليل التباين الأحادي</caption>
<thead><tr><th scope="col">المصدر</th><th scope="col">مجموع المربعات</th><th scope="col">درجات الحرية</th><th scope="col">متوسط المربعات</th></tr></thead>
<tbody>
<tr><th scope="row">بين المجموعات</th><td><output id="esa-anova-ssb" dir="ltr">26.000000</output></td><td><output id="esa-anova-dfb" dir="ltr">2</output></td><td><output id="esa-anova-msb" dir="ltr">13.000000</output></td></tr>
<tr><th scope="row">داخل المجموعات</th><td><output id="esa-anova-ssw" dir="ltr">6.000000</output></td><td><output id="esa-anova-dfw" dir="ltr">6</output></td><td><output id="esa-anova-msw" dir="ltr">1.000000</output></td></tr>
</tbody></table></div>
<p><strong>إحصائية F:</strong> <output id="esa-anova-f" dir="ltr">13.000000</output> · <strong>القيمة الاحتمالية للذيل الأعلى:</strong> <output id="esa-anova-p" dir="ltr">0.006592</output></p>
<p><strong>تحليل التباين لويلش (تباينات غير متساوية):</strong> F = <output id="esa-anova-welch-f" dir="ltr">11.142857</output>، ودرجتا الحرية = <output id="esa-anova-welch-df" dir="ltr">2, 4.0000</output>، وp = <output id="esa-anova-welch-p" dir="ltr">0.023157</output></p>
<p id="esa-anova-decision">عند α=0.05 نرفض تساوي متوسطات المجتمعات إذا تحققت افتراضات ANOVA. ولا يحدد ذلك أي المجموعات تختلف.</p>
</section>
<p class="muted-mini">يعرض الرسم المشاهدات (النقاط) ومتوسطات العينات (الخطوط الأفقية القصيرة)، لا فترات عدم اليقين. القيمة الاحتمالية هي <strong>الذيل الأعلى لتوزيع F</strong> بدرجتي حرية \((k-1,\,N-k)\). يفترض استدلال F الكلاسيكي استقلال المشاهدات، وأخطاء طبيعية في كل مجموعة، وتساوي تباينات المجتمعات؛ ولا يمكن التحقق من ذلك في هذا المثال التعليمي. والرفض لا يثبت السببية ولا يحدد أي مجموعة تختلف.</p>
</section>
<h2>10. ماذا يعني الرفض؟</h2>
<p>رفض \(H_0:\mu_1=\cdots=\mu_k\) يعني أن البيانات تقدّم دليلًا على أن متوسط مجتمع واحد على الأقل يختلف. لكن تحليل التباين وحده لا يكشف أيّ المجموعات تختلف؛ لذلك تُستخدم بعده المقارنات اللاحقة (Post-hoc) التي تضبط معدلات الخطأ.</p>
<h2>11. الافتراضات</h2>
<ul class="bullets">
<li>استقلال المشاهدات داخل المجموعات وبينها، وهو ما يضمنه عادة التصميم (معاينة عشوائية أو توزيع عشوائي).</li>
<li>توزيع طبيعي تقريبًا للأخطاء في كل مجموعة؛ ومع المجموعات الكبيرة والمتوازنة يكون الاختبار متينًا نسبيًا تجاه الانحراف المعتدل عن الطبيعية.</li>
<li>تساوي تباينات المجتمعات بين المجموعات.</li>
</ul>
<h2>12. لماذا يهمّ تساوي التباينات؟</h2>
<p>يجمع \(MS_W\) تباينات المجموعات في تقدير مشترك واحد. فإذا اختلفت تباينات المجتمعات كثيرًا، خاصة مع أحجام مجموعات غير متساوية، قد يصبح معدل الخطأ الفعلي لاختبار F بعيدًا عن \(\alpha\). عندئذ توجد بدائل مثل تحليل التباين لويلش (Welch's ANOVA)، أو اختبار كروسكال–واليس عندما يكون السؤال عن اختلاف التوزيعات.</p>
<p>يرجّح <strong>تحليل التباين لويلش</strong> (Welch, 1951) متوسط كل مجموعة بالوزن \(w_i=n_i/s_i^2\) بدل تجميع التباينات:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="تحليل التباين لويلش">
\[
F_W=\frac{\sum_i w_i(\bar x_i-\tilde x)^2/(k-1)}{1+\frac{2(k-2)}{k^2-1}\Lambda},\quad
\tilde x=\frac{\sum_i w_i\bar x_i}{\sum_i w_i},\quad
\Lambda=\sum_i\frac{(1-w_i/\sum_j w_j)^2}{n_i-1},\quad
\nu_2=\frac{k^2-1}{3\Lambda}.
\]</div>
<p>تُقارن \(F_W\) بتوزيع F بدرجتي حرية \(k-1\) و\(\nu_2\)، و\(\nu_2\) غالبًا ليست عددًا صحيحًا. ومع مجموعتين تساوي \(F_W\) مربع إحصائية t لويلش. تُظهر دراسات المحاكاة أن اختبار ويلش يحافظ على معدل الخطأ من النوع الأول قريبًا من \(\alpha\) عند اختلاف التباينات، خاصة مع أحجام مجموعات غير متساوية، ولا يخسر إلا قليلًا من القوة عند تساويها؛ لذلك يستخدمه كثير من الإحصائيين افتراضيًا. لكنه ما زال يفترض استقلال المشاهدات وطبيعيتها التقريبية، ويكون غير معرّف إذا كان تباين إحدى المجموعات صفرًا. يعرض المختبر الاختبارين معًا؛ فاختر أحدهما قبل رؤية البيانات، لا الاختبار الذي يعطي قيمة احتمالية أصغر.</p>
<h2>13. تحليل التباين مقابل اختبارات t المتعددة</h2>
<div class="table-wrap"><table><caption>مقارنة بين النهجين</caption><thead><tr><th scope="col">الخاصية</th><th scope="col">اختبارات t متعددة</th><th scope="col">تحليل التباين</th></tr></thead><tbody>
<tr><th scope="row">مقارنة مجموعات كثيرة</th><td>غير فعّال</td><td>نعم</td></tr>
<tr><th scope="row">ضبط الخطأ الكلي من النوع الأول</th><td>ضعيف</td><td>نعم، للاختبار الشامل</td></tr>
<tr><th scope="row">اختبار شامل واحد</th><td>لا</td><td>نعم</td></tr>
</tbody></table></div>
<h2>14. تطبيقات شائعة</h2>
<p>مقارنة طرق التدريس، والعلاجات الطبية، وعمليات التصنيع، واستراتيجيات التسويق، والنتائج بين المناطق.</p>
<h2>15. الصورة الأشمل</h2>
<p>يعمّم تحليل التباين الأحادي اختبار t لعينتين على ثلاث مجموعات أو أكثر. فبدلًا من مقارنة المجموعات زوجًا زوجًا، يقيّم جميع المجموعات معًا عبر نسبة التباين بين المجموعات إلى التباين داخلها. والخطوة التالية بعد نتيجة دالة هي المقارنات اللاحقة لتحديد مواضع الاختلاف (<a href="/ar/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/">الدرس التالي</a>).</p>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>يقارن تحليل التباين الأحادي متوسطات ثلاثة مجتمعات أو أكثر باختبار شامل واحد.</li>
<li>الفرضية الصفرية: جميع متوسطات المجتمعات متساوية.</li>
<li>\(F=MS_B/MS_W\) بدرجتي حرية \((k-1,\,N-k)\)، والقيمة الاحتمالية من الذيل الأعلى.</li>
<li>النتيجة الدالة تعني أن متوسطًا واحدًا على الأقل يختلف، دون تحديده.</li>
<li>\(\eta^2=SS_B/SS_T\) يصف حجم الأثر في العينة.</li>
<li>يفترض الاختبار الاستقلال وطبيعية الأخطاء وتساوي التباينات.</li>
</ul></div>
<div class="lesson-nav">
<a class="btn btn-outline" href="/ar/inference/classical-tests/chi-square-homogeneity-test/">→ السابق: اختبار كاي تربيع للتجانس</a>
<a class="btn" href="/ar/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/">التالي: الاختبارات اللاحقة والمقارنات المتعددة ←</a>
</div>
</div></section>
<style>
      #esa-anova-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-anova-lab .esa-anova-fields{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
      #esa-anova-lab label{display:block;font-weight:650;margin-bottom:6px}
      #esa-anova-lab textarea{box-sizing:border-box;display:block;max-width:100%;width:100%;min-width:0;resize:vertical;
        background:var(--surface);color:var(--text);border:1px solid var(--border);border-radius:8px;padding:9px;font:inherit}
      #esa-anova-lab .esa-anova-controls{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0}
      #esa-anova-lab .esa-anova-controls button{max-width:100%;white-space:normal}
      #esa-anova-lab [hidden]{display:none!important}
      #esa-anova-lab #esa-anova-error{font-weight:650;color:#b42318}
      #esa-anova-lab #esa-anova-chart{display:block;width:100%;max-width:560px;height:auto;margin:8px auto}
      #esa-anova-lab :is(textarea,button):focus-visible,.esa-anova-equation:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
      #esa-anova-lab .esa-anova-equation{max-width:100%;overflow-x:auto;direction:ltr}
      #esa-anova-lab .esa-anova-equation mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}
      #esa-anova-lab output{font-variant-numeric:tabular-nums}
      @media(max-width:650px){#esa-anova-lab .esa-anova-fields{grid-template-columns:minmax(0,1fr)}}
#esa-anova-lab{box-sizing:border-box}
.esa-long-math{max-width:100%;overflow-x:auto;direction:ltr}
</style>
<script defer src="/js/one-way-anova-explorer.js"></script>
