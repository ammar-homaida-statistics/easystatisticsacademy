---
layout: default
title: ما المتغير العشوائي؟
description: شرح عربي للمتغيرات العشوائية وتمييز النتائج عن القيم العددية، مع تجربة تفاعلية لرمي قطعتين من النقود.
permalink: /ar/probability/random-variables/what-is-a-random-variable/
sidebar: false
lang: ar
translation_pair: what-is-a-random-variable
math: true
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">المتغيرات العشوائية</span><span class="badge">درس تفاعلي</span></div>
<h1>ما المتغير العشوائي؟</h1>
<p class="lead">المتغير العشوائي دالة تُسنِد قيمة عددية لكل ناتج ممكن من تجربة عشوائية، وتسمح بوصف عدم اليقين بلغة الاحتمالات.</p>
<p><a href="/probability/random-variables/what-is-a-random-variable/" lang="en" dir="ltr">English — What Is a Random Variable?</a></p>
</div></section>
<section><div class="content-narrow" dir="rtl">
<h2>التجربة والنتيجة والمتغير العشوائي</h2>
<p>التجربة العشوائية هي إجراء لا نعرف نتيجته مسبقًا على وجه اليقين. فضاء العينة يضم جميع النتائج الممكنة، في حين أن <strong>المتغير العشوائي</strong> قاعدة عددية ثابتة تُطبَّق على تلك النتائج. ليس المتغير نفسه نتيجة التجربة؛ إنه دالة تُعرِّف القيمة التي نقيسها من النتيجة.</p>
<p>لنرمِ قطعتين من النقود. نرمز إلى الصورة بالرمز <span dir="ltr">H</span> وإلى الكتابة بالرمز <span dir="ltr">T</span>. فضاء العينة المرتب هو:</p>
<div class="esa-rv-math" dir="ltr">\[\Omega=\{HH,HT,TH,TT\},\qquad X:\Omega\rightarrow\{0,1,2\}.\]</div>
<p>نعرّف <strong>X</strong> بأنه عدد مرات ظهور الصورة. حينها <span dir="ltr">X(TT)=0</span>، و<span dir="ltr">X(HT)=X(TH)=1</span>، و<span dir="ltr">X(HH)=2</span>. انتبه إلى أن نتيجتين مختلفتين يمكن أن تؤديا إلى القيمة العددية نفسها.</p>
<h2>من النتائج إلى التوزيع الاحتمالي</h2>
<p>عند استقلال الرميتين وعدالة كل قطعة نقدية تكون النتائج الأربع متساوية الاحتمال، ولكل منها احتمال <span dir="ltr">1/4</span>. لكن قيم X الثلاث ليست متساوية الاحتمال:</p>
<div class="esa-rv-math" dir="ltr">\[P(X=0)=\tfrac14,\qquad P(X=1)=\tfrac12,\qquad P(X=2)=\tfrac14.\]</div>
<p>لتفسير القيمة الوسطى، يجمع احتمال كل من النتيجتين <span dir="ltr">HT</span> و<span dir="ltr">TH</span>؛ فهما حدثان متنافيان. ويجب أن يساوي مجموع احتمالات جميع القيم الممكنة واحدًا.</p>
<section id="esa-two-coin-rv" class="concept-box" aria-labelledby="esa-rv-heading" style="min-width:0;overflow-wrap:anywhere">
<h2 id="esa-rv-heading">مختبر تفاعلي: عدد الصور في رميتين</h2>
<p>حرّك احتمال الصورة في كل رمية مستقلة، ثم راقب كيف تتحول احتمالات النتائج الأربع إلى توزيع X. القيمة الابتدائية <strong>50%</strong> تصف قطعتين عادلتين.</p>
<label for="esa-rv-prob">احتمال الصورة في كل رمية: <output id="esa-rv-prob-label" for="esa-rv-prob">50%</output></label>
<input id="esa-rv-prob" type="range" min="0" max="1" step="0.05" value="0.5" style="display:block;width:min(100%,480px)">
<p id="esa-rv-error" role="alert" hidden>احتمال الصورة يجب أن يكون بين الصفر والواحد.</p>
<div id="esa-rv-results" aria-live="polite">
<div class="table-wrap"><table><caption>النتائج الأولية والقيم العددية واحتمالاتها</caption>
<thead><tr><th>النتيجة</th><th>قيمة X</th><th>احتمال النتيجة</th></tr></thead><tbody>
<tr><th scope="row" dir="ltr">TT</th><td><output id="esa-rv-tt-x">0</output></td><td><output id="esa-rv-tt-p">0.2500</output></td></tr>
<tr><th scope="row" dir="ltr">TH</th><td><output id="esa-rv-th-x">1</output></td><td><output id="esa-rv-th-p">0.2500</output></td></tr>
<tr><th scope="row" dir="ltr">HT</th><td><output id="esa-rv-ht-x">1</output></td><td><output id="esa-rv-ht-p">0.2500</output></td></tr>
<tr><th scope="row" dir="ltr">HH</th><td><output id="esa-rv-hh-x">2</output></td><td><output id="esa-rv-hh-p">0.2500</output></td></tr>
</tbody></table></div>
<p>التوزيع الاحتمالي: <span dir="ltr">P(X=0) = <output id="esa-rv-x0">0.2500</output>؛ P(X=1) = <output id="esa-rv-x1">0.5000</output>؛ P(X=2) = <output id="esa-rv-x2">0.2500</output></span>.</p>
<svg id="esa-rv-chart" role="img" viewBox="0 0 465 215" style="width:100%;height:auto;display:block" aria-label="مخطط أعمدة توزيع عدد الصور"></svg>
<p>مجموع الاحتمالات: <output id="esa-rv-sum">1.0000</output>؛ التوقع: <output id="esa-rv-mean">1.0000</output>؛ التباين: <output id="esa-rv-variance">0.5000</output>.</p>
</div>
<button id="esa-rv-reset" type="button" class="btn btn-outline">إعادة المثال العادل</button>
<p>إذا رمزنا إلى احتمال الصورة بـ <span dir="ltr">p</span> فإن X يتبع توزيع ذي الحدين بمعلمتين <span dir="ltr">n=2</span> و<span dir="ltr">p</span>، بشرط استقلال الرميتين وتماثل احتمال الصورة فيهما.</p>
<div class="esa-rv-math" dir="ltr">\[P(X=x)={2\choose x}p^x(1-p)^{2-x},\quad x=0,1,2.\]</div>
</section>
<h2>المتغيرات المنفصلة والمتصلة</h2>
<p><strong>المتغير العشوائي المنفصل:</strong> يأخذ مجموعة قيم يمكن عدّها؛ مثل عدد الصور أو عدد الزبائن في ساعة.</p>
<p><strong>المتغير العشوائي المتصل:</strong> يتخذ قيمًا ضمن مجال عددي ويُوصَف عادةً بكثافة احتمالية؛ مثل زمن الانتظار المقاس بدقة مستمرة. في النموذج المتصل ذي الكثافة، احتمال قيمة مفردة يساوي صفرًا، لكن احتمال فترة يمكن أن يكون موجبًا.</p>
<h2>لماذا نستخدم المتغيرات العشوائية؟</h2>
<p>نستخدم التوزيع الاحتمالي لحساب احتمالات القيم أو الفترات، وتلخيص السلوك بالتوقع والتباين، وبناء نماذج للاستدلال الإحصائي. نرمز إلى المتغير غالبًا بحرف كبير مثل X، وإلى قيمة متحققة منه بحرف صغير مثل x.</p>
<div class="summary-box"><h2>الخلاصة</h2><ul class="bullets"><li>المتغير العشوائي دالة عددية على فضاء النتائج.</li><li>نتائج تجريبية متعددة يمكن أن تؤدي إلى القيمة نفسها.</li><li>احتمالات القيم تُحسب بجمع احتمالات النتائج المناسبة المتنافية.</li><li>توزيع المتغير ليس بالضرورة متساوي الاحتمال حتى لو كانت النتائج الأولية كذلك.</li><li>يجب التمييز بين المتغيرات المنفصلة والمتصلة.</li></ul></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/">الصفحة العربية</a><a class="btn" lang="en" dir="ltr" href="/probability/random-variables/discrete-random-variables/">Next: Discrete Random Variables (English)</a></div>
</div></section>
<style>.esa-rv-math{direction:ltr;max-width:100%;overflow-x:auto}.esa-rv-math mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}</style>
<script defer src="/js/two-coin-random-variable.js"></script>
