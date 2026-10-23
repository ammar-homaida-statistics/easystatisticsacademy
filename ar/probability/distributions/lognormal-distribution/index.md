---
layout: default
title: التوزيع اللوغاريتمي الطبيعي
description: درس عربي شامل للتوزيع اللوغاريتمي الطبيعي ومعلمات مقياس اللوغاريتم والكثافة والتراكم والعزوم مع مختبر احتمالي تفاعلي.
permalink: /ar/probability/distributions/lognormal-distribution/
lang: ar
sidebar: false
translation_pair: lognormal-distribution
math: true
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">التوزيعات المستمرة</span><span class="badge">الالتواء إلى اليمين</span></div>
<h1>التوزيع اللوغاريتمي الطبيعي (Lognormal Distribution)</h1>
<p><a href="/probability/distributions/lognormal-distribution/" lang="en" dir="ltr">English — Lognormal Distribution</a></p>
<p class="lead">يساعد التوزيع اللوغاريتمي الطبيعي في نمذجة المقادير الموجبة التي تتفاوت غالبًا على نحو مضاعف؛ مثل بعض التراكيز والأحجام وأزمنة التشغيل. وهو ليس اختيارًا تلقائيًا لكل بيانات موجبة.</p>
<div class="hero-actions"><a class="btn btn-outline" href="/ar/probability/distributions/normal-distribution/">← التوزيع الطبيعي بالعربية</a>
<a class="btn btn-outline" href="/probability/distributions/lognormal-distribution/" lang="en" dir="ltr">English lesson</a></div>
</div></section>
<section class="section"><div class="content-narrow">
<h2>التعريف والفرق عن التوزيع الطبيعي</h2>
<p>يكون المتغير العشوائي الموجب <strong>X</strong> لوغاريتميًا طبيعيًا إذا كان لوغاريتمه الطبيعي <span dir="ltr">Y=ln(X)</span> يتبع توزيعًا طبيعيًا. وبذلك يكون <span dir="ltr">X=exp(Y)</span>. نطاق X هو الأعداد الموجبة فقط، أما نطاق ln(X) فهو خط الأعداد الحقيقي كله.</p>
<div class="esa-ln-equation" dir="ltr" tabindex="0" role="region" aria-label="تعريف التوزيع اللوغاريتمي الطبيعي">\[
Y=\ln X\sim N(\mu,\sigma^2),\qquad X=e^Y>0,\qquad \sigma>0.
\]</div>
<p><strong>تنبيه مهم:</strong> تمثل μ متوسط <span dir="ltr">ln(X)</span>، وσ انحرافه المعياري؛ ولا يساوي μ متوسط X، ولا يساوي σ انحراف X المعياري. هذا التمييز ضروري لتفسير المعلمات والحسابات بصورة صحيحة.</p>
<h2>دالة الكثافة الاحتمالية</h2>
<p>عند تحويل المتغير الطبيعي بالأسّ، يجب استخدام عامل التحويل <span dir="ltr">1/x</span> في الكثافة:</p>
<div class="esa-ln-equation" dir="ltr" tabindex="0" role="region" aria-label="كثافة اللوغاريتمي الطبيعي">\[
f_X(x)=\begin{cases}\displaystyle
\frac{1}{x\sigma\sqrt{2\pi}}\exp\!\left[-\frac{(\ln x-\mu)^2}{2\sigma^2}\right],&x>0,\\
0,&x\le0.
\end{cases}
\]</div>
<p>المساحة تحت الكثافة على الأعداد الموجبة تساوي واحدًا. ارتفاع الكثافة عند قيمة بعينها ليس احتمالًا؛ واحتمال الحصول على نقطة مفردة في نموذج مستمر يساوي صفرًا.</p>
<h2>دالة التوزيع التراكمي واحتمالات الفترات</h2>
<p>نستعمل دالة التوزيع التراكمي <span dir="ltr">Φ</span> للمتغير الطبيعي المعياري. عندما يكون x موجبًا:</p>
<div class="esa-ln-equation" dir="ltr" tabindex="0" role="region" aria-label="دالة التوزيع اللوغاريتمي الطبيعي">\[
F_X(x)=P(X\le x)=\Phi\!\left(\frac{\ln x-\mu}{\sigma}\right),\quad x>0.
\]</div>
<p>وتكون <span dir="ltr">F_X(x)=0</span> عندما <span dir="ltr">x≤0</span>. وبين حدين <span dir="ltr">0≤a<b</span>:</p>
<div class="esa-ln-equation" dir="ltr" tabindex="0" role="region" aria-label="احتمال فترة لوغاريتمي طبيعي">\[
P(a\le X\le b)=F_X(b)-F_X(a).
\]</div>
<p>لأن التوزيع مستمر، لا يغيّر إدراج طرفي الفترة أو استبعادهما قيمة الاحتمال.</p>
<h2>المتوسط والوسيط والمنوال والتباين</h2>
<p>التوزيع ذو ذيل ممتد نحو اليمين؛ لذلك يكون المنوال أصغر من الوسيط، ويكون الوسيط أصغر من المتوسط عندما تكون <span dir="ltr">σ>0</span>.</p>
<div class="esa-ln-equation" dir="ltr" tabindex="0" role="region" aria-label="عزوم اللوغاريتمي الطبيعي">\[
\begin{aligned}
E(X)&=e^{\mu+\sigma^2/2},\\
\operatorname{Median}(X)&=e^\mu,\\
\operatorname{Mode}(X)&=e^{\mu-\sigma^2},\\
\operatorname{Var}(X)&=(e^{\sigma^2}-1)e^{2\mu+\sigma^2},\\
\operatorname{SD}(X)&=\sqrt{\operatorname{Var}(X)}.
\end{aligned}
\]</div>
<p>تغيّر σ شكل التوزيع ودرجة التشتت. مثلًا، عندما <span dir="ltr">μ=0</span> و<span dir="ltr">σ=0.5</span> يكون الوسيط 1، والمنوال نحو 0.7788، والمتوسط نحو 1.1331، والتباين نحو 0.3647. ليست هذه القيم إحصاءات عينة بل خصائص التوزيع النظري.</p>
<h2>مثال لحساب الاحتمال</h2>
<p>إذا كان <span dir="ltr">ln(X)∼N(0,0.5²)</span> فإن احتمال وجود X بين <span dir="ltr">e^{-0.5}</span> و<span dir="ltr">e^{0.5}</span> يساوي احتمال وجود المتغير الطبيعي المعياري بين −1 و1:</p>
<div class="esa-ln-equation" dir="ltr" tabindex="0" role="region" aria-label="احتمال بين حدين أسّيين">\[
P(e^{-0.5}\le X\le e^{0.5})=\Phi(1)-\Phi(-1)\approx0.682689.
\]</div>
<h2>التفسير العملي وحدود النموذج</h2>
<p>قد يلائم النموذج عمليات النمو بالمضاعفة، والتراكيز البيئية، وبعض بيانات الإيرادات والأحجام. لكن وجود قيم موجبة أو التواء موجب وحده لا يثبت أن البيانات لوغاريتمية طبيعية. يجب فحص لوغاريتم القيم، وإمكان وجود الأصفار، والقيم المتطرفة، والاعتماد بين المشاهدات، واحتمال وجود ذيول أثقل من النموذج المفترض.</p>
<p>حتى عند ملاءمة نموذج لوغاريتمي طبيعي، فإن المتوسط الحسابي على المقياس الأصلي <strong>ليس</strong> مجرد أسّ المتوسط اللوغاريتمي؛ فأسّ μ يعطي الوسيط، بينما يعتمد المتوسط على كل من μ وσ².</p>
</div></section>
<section class="example-box" id="esa-lognormal-lab" aria-labelledby="esa-ln-heading">
<h2 id="esa-ln-heading">مختبر تفاعلي لاحتمالات التوزيع اللوغاريتمي الطبيعي</h2><p>اضبط متوسط وانحراف اللوغاريتم الطبيعي، وحدد مجال الاحتمال. يستخدم الحساب التوزيع الطبيعي المعياري ويحافظ على الاحتمال في الذيول غير الظاهرة.</p>
<div class="esa-ln-fields">
<label>متوسط ln(X) — μ<input id="esa-ln-mu" type="number" value="0" step="any" dir="ltr"></label>
<label>الانحراف المعياري لـ ln(X) — σ<input id="esa-ln-sigma" type="number" value=".5" min=".000001" step="any" dir="ltr"></label>
<label>الحد الأدنى a<input id="esa-ln-a" type="number" value="1" min="0" step="any" dir="ltr"></label>
<label>الحد الأعلى b<input id="esa-ln-b" type="number" value="2" min="0" step="any" dir="ltr"></label>
<label>منطقة الاحتمال<select id="esa-ln-mode"><option value="between">بين a و b</option><option value="left">يسار a</option><option value="right">يمين b</option></select></label>
</div><p id="esa-ln-error" role="alert" hidden></p>
<div id="esa-ln-results" aria-live="polite" aria-atomic="true">
<p><strong><span id="esa-ln-region">P(a ≤ X ≤ b)</span>:</strong> <output id="esa-ln-probability"></output>
(<output id="esa-ln-percent"></output>%).</p>
<svg id="esa-ln-plot" viewBox="0 0 620 225" role="img" aria-label="مختبر تفاعلي لاحتمالات التوزيع اللوغاريتمي الطبيعي" dir="ltr"></svg>
<p id="esa-ln-warning" class="muted-mini"></p>
<p>المتوسط: <output id="esa-ln-mean"></output>; الوسيط: <output id="esa-ln-median"></output>; المنوال: <output id="esa-ln-modeValue"></output>.</p>
<p>التباين: <output id="esa-ln-variance"></output>; الانحراف المعياري: <output id="esa-ln-sd"></output>.</p></div>
<button type="button" class="btn btn-outline" id="esa-ln-reset">استعادة المثال</button>
<p class="muted-mini">تستخدم جميع المعلمات μ وσ مقياس اللوغاريتم الطبيعي. قيم الاحتمال تقريبية عدديًا؛ لا تحفظ الأداة أي مدخلات.</p>
</section><style>
#esa-lognormal-lab{max-width:100%;min-width:0;box-sizing:border-box;overflow-wrap:anywhere}
#esa-lognormal-lab .esa-ln-fields{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,155px),1fr));gap:12px;margin:12px 0}
#esa-lognormal-lab label{display:block;font-weight:600}
#esa-lognormal-lab input,#esa-lognormal-lab select{display:block;box-sizing:border-box;width:100%;max-width:100%;min-width:0;padding:9px;font:inherit;border:1px solid var(--border);border-radius:8px}
#esa-lognormal-lab [hidden]{display:none!important}
#esa-lognormal-lab svg{width:100%;height:auto;max-width:640px;display:block;margin:10px auto}
#esa-lognormal-lab output{font-variant-numeric:tabular-nums}
#esa-lognormal-lab :is(input,select,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-ln-equation{max-width:100%;overflow-x:auto;direction:ltr}.esa-ln-equation mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}
@media print{#esa-lognormal-lab .esa-ln-fields,#esa-lognormal-lab button{display:none}}
</style><script defer src="/js/lognormal-probability-explorer.js"></script>
<section class="section"><div class="content-narrow">
<h2>خلاصة الدرس</h2><div class="summary-box"><ul class="bullets">
<li>يكون X لوغاريتميًا طبيعيًا إذا كان ln(X) طبيعي التوزيع.</li>
<li>μ وσ معلمتان على مقياس اللوغاريتم، لا على مقياس X الأصلي.</li>
<li>التوزيع موجب ومائل إلى اليمين؛ ومنواله أصغر من وسيطه ومتوسطه عند σ>0.</li>
<li>تعتمد احتمالات X على التوزيع الطبيعي المعياري بعد أخذ اللوغاريتم.</li>
<li>صلاحية النموذج تتطلب فحص الافتراضات والبيانات، وليس مجرد ملاحظة أن القيم موجبة.</li>
</ul></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/distributions/normal-distribution/">← التوزيع الطبيعي</a>
<a class="btn" href="/probability/distributions/lognormal-distribution/" lang="en" dir="ltr">English lesson →</a></div>
</div></section>