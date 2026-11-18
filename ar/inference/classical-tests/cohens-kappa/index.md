---
layout: default
title: معامل كوهين كابا لاتفاق المقيّمين
description: "شرح عربي لمعامل كوهين كابا لقياس الاتفاق بين مقيّمَين بعد استبعاد الاتفاق العشوائي، مع مفارقة كابا وكابا الموزونة للفئات المرتبة ومختبر تفاعلي."
permalink: /ar/inference/classical-tests/cohens-kappa/
lang: ar
sidebar: false
math: true
learning_resource: true
translation_pair: cohens-kappa
---
<section class="hero hero-section"><div class="hero-card">
<h1>معامل كوهين كابا لاتفاق المقيّمين</h1>
<p class="lead">طبيبان يصنّفان المرضى أنفسهم، أو مُرمِّزان يصنّفان المقابلات نفسها. ما مدى اتفاقهما بعد استبعاد الاتفاق الذي نتوقعه بالصدفة وحدها؟</p>
<p><a href="/inference/classical-tests/cohens-kappa/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/classical-tests/mcnemar-test/">اختبار ماكنمار: هل تغيّرت النسبة؟</a> · <a href="/ar/inference/classical-tests/chi-square-independence-test/">اختبار كاي تربيع للاستقلال</a></p>
</div></section>
<section><div class="content-narrow">
<h2>1. الاتفاق سؤال مختلف عن التغيّر</h2>
<p>يسأل <a href="/ar/inference/classical-tests/mcnemar-test/">اختبار ماكنمار</a> عمّا إذا كان لتصنيفين مزدوجين النسب <em>الهامشية</em> نفسها. وقد تتطابق النسب الهامشية لمقيّمَين ومع ذلك يختلفان في حالات فردية كثيرة. أما <strong>معامل كوهين كابا</strong> فيقيس مدى وضع المقيّمَين <em>الحالة نفسها</em> في <em>الفئة نفسها</em>، بعد تصحيح أثر الصدفة.</p>
<h2>2. جدول الاتفاق</h2>
<p>يقرأ أخصائيا أشعة خمسين صورة ويصنّفان كلًّا منها «غير طبيعية» أو «طبيعية»:</p>
<div class="table-wrap"><table><caption>الاتفاق بين أخصائيَّي أشعة (N = 50)</caption><thead><tr><th scope="col">المقيّم A \ المقيّم B</th><th scope="col">غير طبيعية</th><th scope="col">طبيعية</th><th scope="col">المجموع</th></tr></thead><tbody><tr><th scope="row">غير طبيعية</th><td>20</td><td>5</td><td>25</td></tr><tr><th scope="row">طبيعية</th><td>10</td><td>15</td><td>25</td></tr><tr><th scope="row">المجموع</th><td>30</td><td>20</td><td>50</td></tr></tbody></table></div>
<h2>3. الاتفاق المشاهد والاتفاق بالصدفة</h2>
<p><strong>الاتفاق المشاهد</strong> نسبة الحالات على القطر. و<strong>الاتفاق بالصدفة</strong> هو الاتفاق المتوقع لو صنّف المقيّمان باستقلال، كلٌّ بنسبه الهامشية \(r_i\) و\(c_i\):</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="الاتفاق المشاهد والمتوقع">
\[
p_o=\sum_{i=1}^{k}p_{ii}=\frac{20+15}{50}=0.70,\qquad
p_e=\sum_{i=1}^{k}r_i\,c_i=0.5\times0.6+0.5\times0.4=0.50 .
\]</div>
<h2>4. معامل كوهين كابا</h2>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="معامل كابا">
\[
\kappa=\frac{p_o-p_e}{1-p_e}=\frac{0.70-0.50}{1-0.50}=0.40 .
\]</div>
<p>كابا هي الحصة التي حققها المقيّمان فعلًا من التحسّن <em>الممكن</em> فوق الصدفة: \(\kappa=1\) اتفاق تام، و\(\kappa=0\) اتفاق لا يزيد على الصدفة، و\(\kappa&lt;0\) اختلاف منهجي. وتكون كابا غير معرّفة عندما \(p_e=1\)، ولا يحدث ذلك إلا إذا استخدم المقيّمان دائمًا الفئة الوحيدة نفسها.</p>
<h2>5. أقصى قيمة ممكنة لكابا</h2>
<p>إذا اختلفت النسب الهامشية للمقيّمَين، فلا يمكن حتى لأفضل ترتيب للحالات أن يبلغ \(\kappa=1\):</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="أقصى كابا">
\[
\kappa_{\max}=\frac{\sum_i\min(r_i,c_i)-p_e}{1-p_e}=\frac{0.5+0.4-0.5}{0.5}=0.80 .
\]</div>
<p>هنا يصنّف المقيّم B صورًا «غير طبيعية» أكثر (60%) من المقيّم A (50%)، لذا فالسقف 0.80. وذكر \(\kappa\) بجانب \(\kappa_{\max}\) يفصل الاختلاف الناتج عن اختلاف الميول العامة عن الاختلاف حالةً بحالة.</p>
<h2>6. مفارقة كابا</h2>
<p>لنفترض أن 85 حالة من 100 صنّفها المقيّمان «طبيعية»، و5 «غير طبيعية»، وانقسمت 10 حالات بالتساوي. الاتفاق المشاهد 0.90، ومع ذلك:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="مثال مفارقة كابا">
\[
p_e=0.9^2+0.1^2=0.82,\qquad \kappa=\frac{0.90-0.82}{1-0.82}\approx0.444 .
\]</div>
<p>عندما تهيمن فئة واحدة يكون الاتفاق بالصدفة مرتفعًا أصلًا، فتكلّف الاختلافات نفسها قدرًا أكبر من كابا. لذلك يجب دائمًا ذكر كابا مع الجدول، أو مع \(p_o\) ونسب انتشار الفئات.</p>
<h2>7. الخطأ المعياري وفترة الثقة</h2>
<p>للعينات الكبيرة يعطي فليس وكوهين وإيفريت (Fleiss, Cohen &amp; Everitt, 1969) تباين \(\hat\kappa\):</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="تباين كابا">
\[
\widehat{\operatorname{Var}}(\hat\kappa)=\frac{A+B-C}{N(1-p_e)^2},\quad
A=\sum_i p_{ii}\bigl[1-(r_i+c_i)(1-\hat\kappa)\bigr]^2,\quad
B=(1-\hat\kappa)^2\sum_{i\ne j}p_{ij}(c_i+r_j)^2,\quad
C=\bigl[\hat\kappa-p_e(1-\hat\kappa)\bigr]^2 .
\]</div>
<p>في مثال الأشعة \(SE\approx0.127\)، وفترة الثقة التقريبية 95% هي:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="فترة الثقة التقريبية لكابا">
\[
0.40\pm1.96\times0.127=[0.151,\,0.649].
\]</div>
<p>فترة والد (Wald) هذه تقريب للعينات الكبيرة: قد تكون ضعيفة عندما يكون \(N\) صغيرًا أو \(\kappa\) قريبة من \(\pm1\)، وتنكمش إلى نقطة واحدة عند الاتفاق التام.</p>
<h2>8. كابا الموزونة للفئات المرتبة</h2>
<p>تعامل كابا غير الموزونة اختلاف «خفيف مقابل شديد» تمامًا كاختلاف «خفيف مقابل متوسط». فإذا كانت الفئات <strong>مرتبة</strong>، تمنح كابا الموزونة اتفاقًا جزئيًا للاختلافات القريبة. وعند ترقيم الفئات \(1,\dots,k\) تكون أوزان الاتفاق المعتادة:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="كابا الموزونة">
\[
w_{ij}^{\text{lin}}=1-\frac{|i-j|}{k-1},\qquad
w_{ij}^{\text{quad}}=1-\frac{(i-j)^2}{(k-1)^2},\qquad
\kappa_w=\frac{\sum_{ij}w_{ij}p_{ij}-\sum_{ij}w_{ij}r_ic_j}{1-\sum_{ij}w_{ij}r_ic_j}.
\]</div>
<p>في مثال الفئات الثلاث في المختبر أدناه (خفيف، متوسط، شديد): \(\hat\kappa=0.720\) دون أوزان، و\(\hat\kappa_w=0.771\) بالأوزان الخطية، و\(\hat\kappa_w=0.824\) بالأوزان التربيعية. معظم الاختلافات بين فئات متجاورة، لذا يرفع الترجيح قيمة المعامل. وترتبط كابا ذات الأوزان التربيعية ارتباطًا وثيقًا بمعامل الارتباط داخل الفئات (ICC). ومع فئتين فقط يتساوى الترجيحان مع كابا غير الموزونة. اختر الأوزان <em>قبل</em> النظر في البيانات، واذكر أيّها استخدمت، ولا تستخدم الأوزان للفئات الاسمية غير المرتبة. يستخدم المختبر للخطأ المعياري لـ\(\hat\kappa_w\) تباين العينات الكبيرة لفليس وكوهين وإيفريت (1969)، مع التحفظات نفسها بشأن العينات الصغيرة.</p>
<h2>9. مختبر كابا التفاعلي</h2>
<section id="esa-kappa-lab" class="concept-box" data-locale="ar" aria-labelledby="esa-kappa-heading">
<h3 id="esa-kappa-heading">أدخل جدول الاتفاق</h3>
<noscript><p class="esa-noscript" role="note">يتطلب هذا المختبر التفاعلي تفعيل JavaScript. من دونه تبقى الأرقام المعروضة هي المثال المحلول الثابت، وتظل الصيغ والتفسير في الدرس متاحة.</p></noscript>
<p>كل سطر فئة للمقيّم A، وكل عمود الفئة نفسها للمقيّم B. افصل الأعداد الصحيحة بفواصل إنجليزية (من 2 إلى 5 فئات).</p>
<label for="esa-kappa-input">أعداد الاتفاق (صفوف المقيّم A × أعمدة المقيّم B)</label>
<textarea id="esa-kappa-input" dir="ltr" rows="5" spellcheck="false" aria-describedby="esa-kappa-error" aria-invalid="false">20, 5
10, 15</textarea>
<label for="esa-kappa-weights">الترجيح</label>
<select id="esa-kappa-weights"><option value="none" selected>دون أوزان (فئات اسمية)</option><option value="linear">أوزان خطية (فئات مرتبة)</option><option value="quadratic">أوزان تربيعية (فئات مرتبة)</option></select>
<div class="esa-kappa-controls"><button type="button" class="btn btn-outline" id="esa-kappa-example">مثال الأشعة</button><button type="button" class="btn btn-outline" id="esa-kappa-paradox">مفارقة كابا</button><button type="button" class="btn btn-outline" id="esa-kappa-three">ثلاث فئات</button></div>
<p id="esa-kappa-error" role="alert" hidden></p>
<div class="table-wrap" role="status" aria-live="polite" aria-atomic="true"><table><caption>ملخص الاتفاق</caption><tbody>
<tr><th scope="row">عدد الحالات N</th><td><output id="esa-kappa-n" dir="ltr">50</output></td></tr>
<tr><th scope="row">الاتفاق المشاهد pₒ</th><td><output id="esa-kappa-po" dir="ltr">0.7000</output></td></tr>
<tr><th scope="row">الاتفاق بالصدفة pₑ</th><td><output id="esa-kappa-pe" dir="ltr">0.5000</output></td></tr>
<tr><th scope="row">كابا κ (بالترجيح المختار)</th><td><output id="esa-kappa-kappa" dir="ltr">0.4000</output></td></tr>
<tr><th scope="row">أقصى κ ممكنة</th><td><output id="esa-kappa-kmax" dir="ltr">0.8000</output></td></tr>
<tr><th scope="row">الخطأ المعياري للعينات الكبيرة</th><td><output id="esa-kappa-se" dir="ltr">0.1270</output></td></tr>
<tr><th scope="row">فترة ثقة تقريبية 95%</th><td><output id="esa-kappa-ci" dir="ltr">[0.1511, 0.6489]</output></td></tr>
</tbody></table></div>
<p id="esa-kappa-note" role="status" aria-live="polite"></p>
</section>
<h2>10. تفسير كابا</h2>
<p>تنتشر تصنيفات لفظية مثل «0.41–0.60 = متوسط» (لانديس وكوخ، 1977)، لكنها اعتباطية: لم تُشتق من بيانات، وتتجاهل الانتشار وعدد الفئات وعواقب الاختلاف. اذكر \(\hat\kappa\) وفترة ثقتها و\(p_o\) وجدول الاتفاق، واحكم على الكفاية في سياق التطبيق.</p>
<h2>11. الافتراضات والقيود</h2>
<ul class="bullets"><li>يقيّم مقيّمان اثنان فقط الحالات نفسها (N) باستقلال، باستخدام الفئات نفسها المتنافية.</li><li>تعامل كابا غير الموزونة كل اختلاف على أنه بالخطورة نفسها؛ وللفئات المرتبة تمنح كابا الموزونة اتفاقًا جزئيًا للاختلافات القريبة، وتعتمد النتيجة على الأوزان المختارة.</li><li>تعتمد كابا على الانتشار وعلى الميول الهامشية لكل مقيّم، فلا تُقارن مباشرة قيم من مجتمعات مختلفة الانتشار.</li><li>لأكثر من مقيّمَين استخدم معاملًا متعدد المقيّمين مثل كابا فليس.</li></ul>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets"><li>\(\kappa=(p_o-p_e)/(1-p_e)\) تقيس الاتفاق فوق الصدفة.</li><li>اختلاف الميول الهامشية يحدّ أقصى \(\kappa\) ممكنة دون 1.</li><li>الفئات المهيمنة قد تجعل الاتفاق المرتفع يعطي \(\kappa\) منخفضة (مفارقة كابا).</li><li>للفئات المرتبة استخدم كابا الموزونة، واذكر نوع الأوزان.</li><li>اذكر الجدول و\(p_o\) و\(\hat\kappa\) وفترتها بدل التصنيف اللفظي وحده.</li></ul></div>
</div></section>
<style>
#esa-kappa-lab{box-sizing:border-box;max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-kappa-lab label{display:block;font-weight:650;margin-bottom:8px}
#esa-kappa-lab select{display:block;box-sizing:border-box;width:100%;max-width:100%;padding:8px;margin-bottom:8px;font:inherit}
#esa-kappa-lab textarea{display:block;box-sizing:border-box;width:100%;max-width:100%;padding:10px;font:inherit;border:1px solid var(--border);border-radius:8px;resize:vertical}
#esa-kappa-lab .esa-kappa-controls{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
#esa-kappa-lab .esa-kappa-controls button{max-width:100%;white-space:normal}
#esa-kappa-lab .table-wrap{display:block;max-width:100%;overflow-x:auto}
#esa-kappa-lab [hidden]{display:none!important}
#esa-kappa-lab [role="alert"]{color:#b42318;font-weight:700}
#esa-kappa-lab :is(textarea,button,select):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-long-math{max-width:100%;overflow-x:auto;direction:ltr}
</style>
<script defer src="/js/cohens-kappa-lab.js"></script>
