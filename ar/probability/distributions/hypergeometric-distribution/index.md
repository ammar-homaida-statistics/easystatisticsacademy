---
layout: default
title: التوزيع فوق الهندسي
description: شرح عربي للتوزيع فوق الهندسي عند السحب دون إرجاع مع قانون الاحتمال ودعم القيم الممكنة والتباين المصحّح ومختبر تفاعلي.
permalink: /ar/probability/distributions/hypergeometric-distribution/
lang: ar
sidebar: false
translation_pair: hypergeometric-distribution
math: true
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">التوزيعات المتقطعة</span><span class="badge">المعاينة دون إرجاع</span></div>
<h1>التوزيع فوق الهندسي (Hypergeometric Distribution)</h1>
<p><a href="/probability/distributions/hypergeometric-distribution/" lang="en" dir="ltr">English — Hypergeometric Distribution</a></p>
<p class="lead">ماذا يحدث لاحتمال النجاح إذا سحبنا عناصر من مجتمع محدود ولم نُعد العناصر المسحوبة؟ يصف التوزيع فوق الهندسي عدد النجاحات في عينة عشوائية منتظمة تُسحب دون إرجاع.</p>
<div class="hero-actions"><a class="btn btn-outline" href="/ar/probability/distributions/poisson-distribution/">← توزيع بواسون</a>
<a class="btn btn-outline" href="/probability/distributions/hypergeometric-distribution/" lang="en" dir="ltr">English lesson</a></div>
</div></section>
<section class="section"><div class="content-narrow">
<h2>الفكرة الأساسية: السحب دون إرجاع</h2>
<p>افترض مجتمعًا حجمه <span dir="ltr">N</span> يحتوي بالضبط على <span dir="ltr">K</span> من العناصر المصنّفة «نجاحًا»، ونختار منه عينة حجمها <span dir="ltr">n</span> دون إرجاع. المتغير <span dir="ltr">X</span> هو عدد النجاحات داخل العينة. بسبب عدم الإرجاع، تتغير احتمالات السحب المتتابع، ولذلك لا تكون السحوبات مستقلة عمومًا.</p>
<p>يشترط النموذج أن تكون العينات من الحجم n متساوية الاحتمال، وأن تكون حالات النجاح محددة مسبقًا في مجتمع محدود، مع <span dir="ltr">0 ≤ K ≤ N</span> و<span dir="ltr">0 ≤ n ≤ N</span>.</p>
<div class="esa-ar-hg-eq" dir="ltr" tabindex="0" role="region" aria-label="دعم المتغير فوق الهندسي">\[
X\sim\mathrm{Hypergeometric}(N,K,n),\quad
\max(0,n-(N-K))\le x\le\min(n,K).
\]</div>
<p>تأخذ x قيماً صحيحة فقط داخل هذه الحدود؛ واحتمال أي قيمة خارجها يساوي صفرًا.</p>
<h2>دالة الكتلة الاحتمالية</h2>
<div class="esa-ar-hg-eq" dir="ltr" tabindex="0" role="region" aria-label="دالة الكتلة فوق الهندسية">\[
P(X=x)=\frac{\binom{K}{x}\binom{N-K}{n-x}}{\binom{N}{n}},
\qquad \binom ab=\frac{a!}{b!(a-b)!}.
\]</div>
<p>يمثل البسط اختيار x نجاحات من K، واختيار <span dir="ltr">n−x</span> إخفاقات من <span dir="ltr">N−K</span>، بينما يمثل المقام جميع العينات الممكنة ذات الحجم n. يكون مجموع الاحتمالات على مجال الدعم مساويًا للواحد.</p>
<h2>المتوسط والتباين</h2>
<div class="esa-ar-hg-eq" dir="ltr" tabindex="0" role="region" aria-label="عزوم التوزيع فوق الهندسي">\[
\begin{aligned}
E(X)&=n\frac KN,\\
\operatorname{Var}(X)&=n\frac KN\left(1-\frac KN\right)\frac{N-n}{N-1},\quad N>1.
\end{aligned}
\]</div>
<p>العامل <span dir="ltr">(N−n)/(N−1)</span> هو تصحيح المجتمع المحدود، ويعكس انخفاض التباين بسبب عدم الإرجاع. عندما <span dir="ltr">N=1</span> يكون توزيع عدد النجاحات متدهورًا وتباينه صفرًا. وعندما <span dir="ltr">n=N</span> نعرف عدد النجاحات مسبقًا، فيصبح التباين صفرًا أيضًا.</p>
<h2>مثال محسوب خطوة بخطوة</h2>
<p>في صندوق عشرة عناصر، ثلاثة منها ناجحة وسبعة غير ناجحة. نسحب عنصرين دون إرجاع، ونريد احتمال نجاح واحد بالضبط:</p>
<div class="esa-ar-hg-eq" dir="ltr" tabindex="0" role="region" aria-label="مثال التوزيع فوق الهندسي">\[
P(X=1)=\frac{\binom31\binom71}{\binom{10}{2}}
=\frac{21}{45}\approx0.466667.
\]</div>
<p>المتوسط <span dir="ltr">2(3/10)=0.6</span>، والتباين <span dir="ltr">2(0.3)(0.7)(8/9)≈0.373333</span>. وإذا استخدمنا نموذج ثنائي الحدين المستقل على سبيل التقريب فإن احتمال نجاح واحد هو <span dir="ltr">2(0.3)(0.7)=0.42</span>، وهي قيمة مختلفة.</p>
<h2>مقارنة بالتوزيع ثنائي الحدين</h2>
<p>يفترض التوزيع ثنائي الحدين محاولات مستقلة واحتمال نجاح ثابتًا. أما هنا فالسحب دون إرجاع يولّد اعتمادًا بين النتائج. عندما تكون نسبة العينة إلى المجتمع صغيرة، قد يعطي ثنائي الحدين تقريبًا عمليًا، لكن قاعدة 5% إرشاد تقريبي وليست ضمانًا للدقة.</p>
</div></section>

<section class="section"><div class="content-narrow">
<section class="concept-box" id="esa-hypergeom-explorer" role="group" aria-labelledby="esa-hg-title">
<h2 id="esa-hg-title">مختبر تفاعلي للسحب دون إرجاع</h2>
<p>حدّد حجم المجتمع N، وعدد النجاح K، وحجم العينة n، والقيمة المراد اختبارها x. يعرض المختبر الاحتمال فوق الهندسي الدقيق وتقريب ثنائي الحدين على الرسم نفسه، مع المجال المسموح والمتوسط والتباين.</p>
<div class="esa-hg-grid">
<div><label for="esa-hg-N">حجم المجتمع N (من 1 إلى 1000)</label><input id="esa-hg-N" type="number" min="1" max="1000" step="1" value="100" inputmode="numeric" dir="ltr"></div>
<div><label for="esa-hg-K">عدد النجاحات K (بين 0 وN)</label><input id="esa-hg-K" type="number" min="0" max="1000" step="1" value="10" inputmode="numeric" dir="ltr"></div>
<div><label for="esa-hg-n">حجم العينة n (حتى 100)</label><input id="esa-hg-n" type="number" min="0" max="100" step="1" value="5" inputmode="numeric" dir="ltr"></div>
<div><label for="esa-hg-x">عدد النجاحات المرصودة x (بين 0 وn)</label><input id="esa-hg-x" type="number" min="0" max="100" step="1" value="1" inputmode="numeric" dir="ltr"></div>
</div>
<button type="button" class="btn btn-outline" id="esa-hg-reset">استعادة المثال</button>
<p id="esa-hg-status" role="status" aria-live="polite"></p>
<div class="table-wrap"><table><caption>نتائج الاحتمالات والخصائص الإحصائية (ستة منازل عشرية)</caption><tbody>
<tr><th scope="row">العدد الممكن للنجاحات</th><td id="esa-hg-support">—</td></tr>
<tr><th scope="row">احتمال فوق هندسي دقيق P(X=x)</th><td id="esa-hg-exact">—</td></tr>
<tr><th scope="row">تقريب ثنائي الحدين P(Y=x)</th><td id="esa-hg-approx">—</td></tr>
<tr><th scope="row">الفرق المطلق في الاحتمال</th><td id="esa-hg-difference">—</td></tr>
<tr><th scope="row">المتوسط E(X)</th><td id="esa-hg-mean">—</td></tr>
<tr><th scope="row">التباين Var(X)</th><td id="esa-hg-variance">—</td></tr>
<tr><th scope="row">مجموع احتمالات التوزيع الدقيق</th><td id="esa-hg-total">—</td></tr>
<tr><th scope="row">نسبة المعاينة n/N</th><td id="esa-hg-sampling-fraction">—</td></tr>
</tbody></table></div>
<p class="muted-mini">اللون الأخضر: احتمال دقيق دون إرجاع. اللون البرتقالي: تقريب ثنائي الحدين مع افتراض الإرجاع والاستقلال.</p>
<svg id="esa-hg-chart" viewBox="0 0 720 250" role="img" dir="ltr"
aria-label="مقارنة احتمالات التوزيع فوق الهندسي مع ثنائي الحدين" style="display:block;width:100%;height:auto;max-width:100%;overflow:hidden"><g id="esa-hg-bars"></g></svg>
<p class="muted-mini">يحسب المحرك الاحتمالات باستخدام لوغاريتم معاملات الاختيار للحد من تجاوز السعة العددية. النتائج المعروضة تقريب إلى ست منازل؛ لا تُخزّن البيانات المدخلة.</p>
</section>
</div></section>
<style>
#esa-hypergeom-explorer,#esa-hypergeom-explorer *{box-sizing:border-box}
#esa-hypergeom-explorer{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-hypergeom-explorer .esa-hg-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,195px),1fr));gap:12px;margin:14px 0}
#esa-hypergeom-explorer label{display:block;font-weight:650;margin-bottom:5px}
#esa-hypergeom-explorer input{display:block;box-sizing:border-box;width:100%;min-width:0;max-width:100%;padding:10px;font:inherit;border:1px solid var(--border);border-radius:8px}
#esa-hypergeom-explorer .table-wrap{max-width:100%;overflow-x:auto}
#esa-hypergeom-explorer [hidden]{display:none!important}
#esa-hypergeom-explorer :is(input,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-ar-hg-eq{max-width:100%;overflow-x:auto;direction:ltr}
.esa-ar-hg-eq mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}
@media(max-width:650px){#esa-hypergeom-explorer .esa-hg-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/hypergeometric-explorer.js"></script>
<section class="section"><div class="content-narrow">
<h2>متى يُستخدم النموذج؟</h2>
<p>يصلح مثلًا لفحص عينة من شحنة ذات عدد معلوم من القطع المعيبة، أو اختيار أشخاص دون إرجاع من مجتمع محدود ذي صفتين. يتطلب التطبيق تحديد مجتمع الدراسة وطريقة السحب بدقة؛ ولا يكفي مجرد وجود بيانات نجاح/إخفاق.</p>
<div class="summary-box"><h2>الخلاصة</h2><ul class="bullets">
<li>النموذج خاص بالمجتمع المحدود والسحب دون إرجاع.</li>
<li>يُحدَّد بعدد العناصر N والنجاحات K والعينة n.</li>
<li>مجال x الصحيح يعتمد على العناصر المتاحة.</li>
<li>يتضمن التباين تصحيحًا للمجتمع المحدود.</li>
<li>ثنائي الحدين تقريب في بعض الحالات، وليس نفس التوزيع.</li></ul></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/distributions/poisson-distribution/">← توزيع بواسون</a>
<a class="btn" href="/probability/distributions/hypergeometric-distribution/" lang="en" dir="ltr">English lesson →</a></div>
</div></section>