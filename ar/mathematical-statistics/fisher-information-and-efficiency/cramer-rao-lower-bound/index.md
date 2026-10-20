---
layout: default
title: حد كرامر–راو الأدنى ومعلومات فيشر
description: شرح عربي لحد كرامر–راو الأدنى للمقدّرات غير المتحيزة مع برهان قائم على التغاير ومختبر تفاعلي لنموذج برنولي.
permalink: /ar/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/
lang: ar
sidebar: false
translation_pair: cramer-rao-lower-bound
math: true
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الإحصاء الرياضي</span><span class="badge">معلومات فيشر</span><span class="badge">كفاءة التقدير</span></div>
<h1>حد كرامر–راو الأدنى للتباين</h1>
<p><a href="/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/" lang="en" dir="ltr">English — Cramér–Rao Lower Bound</a></p>
<p class="lead">هل يمكن الحصول على مقدّر غير متحيّز بتباين صغير كيفما شئنا؟ يقدّم حد كرامر–راو الأدنى (<span dir="ltr">Cramér–Rao Lower Bound, CRLB</span>) حدّاً نظرياً لدقّة التقدير عندما تتحقق شروط الانتظام المناسبة. يرتبط هذا الحد بمعلومات فيشر المستخلصة من العينة.</p>
<div class="hero-actions"><a class="btn btn-outline" href="/mathematical-statistics/fisher-information-and-efficiency/" lang="en" dir="ltr">Fisher Information block (English)</a><a class="btn" href="/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/" lang="en" dir="ltr">English version</a></div>
</div></section>
<section class="section"><div class="content-narrow">
<h2>الأهداف التعليمية</h2>
<ul class="bullets"><li>تفسير معلومات فيشر وعلاقتها بدقّة التقدير.</li><li>فهم الحد الأدنى لتباين المقدّرات غير المتحيّزة.</li><li>تتبّع فكرة البرهان باستخدام التغاير ومتباينة كوشي–شفارتس.</li><li>التمييز بين المقدّر الذي يحقق الحد وغيره من المقدّرات غير المتحيّزة.</li><li>فحص تأثير حجم العينة واحتمال النجاح باستخدام نموذج برنولي.</li></ul>
<h2>1. معلومات فيشر: ما المقصود بها؟</h2>
<p>لنفترض وجود نموذج إحصائي ذي معلمة عددية <span dir="ltr">θ</span>، ولدينا دالة الإمكان <span dir="ltr">L(θ)</span> ودالة لوغاريتم الإمكان <span dir="ltr">ℓ(θ)</span>. تُعرف <strong>دالة الدرجة</strong> (<span dir="ltr">score</span>) بأنها مشتقة لوغاريتم الإمكان بالنسبة إلى المعلمة:</p>
<div class="esa-math-ltr" dir="ltr">\[
U(\theta)=\frac{\partial}{\partial\theta}\ell(\theta).
\]</div>
<p>في النماذج المنتظمة، يكون متوسط الدرجة صفراً، وتُعرَّف معلومات فيشر — في الصيغة القائمة على تباين الدرجة — كما يأتي:</p>
<div class="esa-math-ltr" dir="ltr">\[
\mathbb{E}_{\theta}[U(\theta)]=0,\qquad I(\theta)=\mathbb{E}_{\theta}[U(\theta)^2].
\]</div>
<p>عند تحقق الشروط الإضافية الملائمة، تتساوى هذه الصيغة مع سالب متوسط المشتقة الثانية للوْغاريتم الإمكان. وتعبّر معلومات فيشر الأكبر عن قدرة العينة على التمييز بين قيم متقاربة من المعلمة في الإطار النموذجي المعتمد.</p>
<h2>2. صيغة حد كرامر–راو الأدنى</h2>
<p>إذا كان المقدّر <span dir="ltr">T</span> غير متحيّز للمعلمة <span dir="ltr">θ</span> في جوار القيمة قيد الدراسة، وكانت معلومات فيشر موجبة ومنتهية، وتحققت شروط الانتظام اللازمة، فإن:</p>
<div class="esa-math-ltr" dir="ltr">\[
\operatorname{Var}_{\theta}(T)\ \geq\ \frac{1}{I(\theta)}.
\]</div>
<p>بعبارة أخرى، لا يمكن لمقدّر منتظم وغير متحيّز لهذه المعلمة أن يملك تبايناً أقل من مقلوب معلومات فيشر. **هذا ليس حكماً عاماً على المقدّرات المتحيّزة**؛ فقد يقل التباين عند السماح بالتحيّز، لكن عندها يجب فحص متوسط مربعات الخطأ، لا التباين وحده.</p>
<p>إذا كان المقدّر غير متحيّز لدالة قابلة للاشتقاق من المعلمة <span dir="ltr">g(θ)</span>، فإن الصيغة العددية العامة للحد، وفق الشروط المناسبة، هي:</p>
<div class="esa-math-ltr" dir="ltr">\[
\operatorname{Var}_{\theta}(T)\ \geq\ \frac{[g'(\theta)]^2}{I(\theta)}.
\]</div>
<h2>3. فكرة البرهان: التغاير وليس التعامد</h2>
<p>لتكن <span dir="ltr">m(θ)=Eθ[T]</span>. عند السماح بتبادل الاشتقاق والتكامل، تُعطي هوية الدرجة:</p>
<div class="esa-math-ltr" dir="ltr">\[
\operatorname{Cov}_{\theta}(T,U(\theta))=m'(\theta).
\]</div>
<p>في حالة عدم التحيّز للمعلمة <span dir="ltr">θ</span>، تكون <span dir="ltr">m(θ)=θ</span>، ولذلك:</p>
<div class="esa-math-ltr" dir="ltr">\[
\operatorname{Cov}_{\theta}(T,U(\theta))=1.
\]</div>
<p>إذن ليس خطأ التقدير متعامداً مع دالة الدرجة؛ <strong>التغاير يساوي واحداً</strong> في هذه الحالة المنتظمة. وتُعطي متباينة كوشي–شفارتس:</p>
<div class="esa-math-ltr" dir="ltr">\[
\{\operatorname{Cov}_{\theta}(T,U)\}^{2}
\leq \operatorname{Var}_{\theta}(T)\operatorname{Var}_{\theta}(U)
=\operatorname{Var}_{\theta}(T)\,I(\theta).
\]</div>
<p>بالتعويض عن التغاير بالقيمة واحد نحصل مباشرة على حد كرامر–راو. ويتطلب هذا الاستدلال اشتقاقاً صحيحاً، وتوقعات وتباينات موجودة، وانتظاماً مناسباً لدعم التبادل بين الاشتقاق والتوقع.</p>
<h2>4. كيف نُفسِّر الحد؟</h2>
<div class="grid grid-2">
<div class="card"><h3>حدّ للدقة</h3><p>تباين المقدّر غير المتحيّز لا يقل عن الحد، في ظل الافتراضات اللازمة.</p></div>
<div class="card"><h3>يعتمد على النموذج</h3><p>تختلف معلومات فيشر باختلاف توزيع البيانات وبنيته الاحتمالية.</p></div>
<div class="card"><h3>حجم العينة</h3><p>تُجمع معلومات المشاهدات المستقلة والمتماثلة التوزيع؛ لذلك يتقلص الحد عادةً مع زيادة حجم العينة.</p></div>
<div class="card"><h3>الكفاءة</h3><p>يُسمى المقدّر غير المتحيّز كفؤاً من حيث هذا الحد عندما يحقق الحد الأدنى المسموح للتباين.</p></div>
</div>
<h2>5. مثال برنولي</h2>
<p>لنفرض أن المشاهدات <span dir="ltr">X₁,…,Xₙ</span> مستقلة ومتماثلة التوزيع وتتبع توزيع برنولي بمعلمة احتمالية <span dir="ltr">p</span>، حيث <span dir="ltr">0&lt;p&lt;1</span>. في هذه الحالة:</p>
<div class="esa-math-ltr" dir="ltr">\[
X_i\sim\operatorname{Bernoulli}(p),\qquad
I_n(p)=\frac{n}{p(1-p)},\qquad
\operatorname{CRLB}=\frac{p(1-p)}{n}.
\]</div>
<p>متوسط العينة <span dir="ltr">X̄</span> مقدّر غير متحيّز لاحتمال النجاح، وله التباين:</p>
<div class="esa-math-ltr" dir="ltr">\[
\mathbb E[\bar X]=p,\qquad
\operatorname{Var}(\bar X)=\frac{p(1-p)}{n}.
\]</div>
<p>وبذلك يحقق متوسط العينة الحد تماماً في هذا النموذج. أما المقدّر <span dir="ltr">X₁</span> الذي يعتمد على المشاهدة الأولى فقط، فهو أيضاً غير متحيّز، لكن تباينه أكبر عندما يزيد حجم العينة على مشاهدة واحدة:</p>
<div class="esa-math-ltr" dir="ltr">\[
\mathbb E[X_1]=p,\qquad
\operatorname{Var}(X_1)=p(1-p).
\]</div>
<h2>6. مختبر تفاعلي: معلومات فيشر وحد كرامر–راو</h2>
<section class="concept-box" id="esa-crlb-lab" aria-labelledby="esa-crlb-title" style="max-width:100%;min-width:0;overflow-x:clip;overflow-wrap:anywhere">
<h3 id="esa-crlb-title">استكشاف دقّة التقدير في نموذج برنولي</h3>
<p>غيّر احتمال النجاح وحجم العينة. تُحسب المعلومات والحد والتباينان مباشرة وفق الصيغ الدقيقة، دون محاكاة عشوائية، حتى تكون المقارنة قابلة للتكرار.</p>
<div style="display:flex;gap:1rem;flex-wrap:wrap;align-items:end">
<label for="esa-crlb-p">احتمال النجاح p (بين 0 و1 حصراً)
<input id="esa-crlb-p" type="number" min="0.001" max="0.999" step="0.01" value="0.30" inputmode="decimal" dir="ltr" style="display:block;width:100%;max-width:12rem"></label>
<label for="esa-crlb-n">عدد المشاهدات n (من 1 إلى 500)
<input id="esa-crlb-n" type="number" min="1" max="500" step="1" value="20" inputmode="numeric" dir="ltr" style="display:block;width:100%;max-width:12rem"></label>
<button class="btn" id="esa-crlb-run" type="button">احسب الحد الأدنى</button>
<button class="btn btn-outline" id="esa-crlb-reset" type="button">إعادة الضبط</button>
</div>
<p id="esa-crlb-status" role="status" aria-live="polite"></p>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,190px),1fr));gap:1rem">
<div class="example-box" style="min-width:0;overflow-wrap:anywhere"><h3>المعلومات والحد</h3><p>معلومات فيشر: <output id="esa-crlb-information" dir="ltr">—</output></p><p>حد كرامر–راو: <output id="esa-crlb-crlb" dir="ltr">—</output></p></div>
<div class="example-box" style="min-width:0;overflow-wrap:anywhere"><h3>متوسط العينة (مقدّر كفؤ)</h3><p>التباين: <output id="esa-crlb-variance-mean" dir="ltr">—</output></p><p>الكفاءة: <output id="esa-crlb-efficiency-mean" dir="ltr">—</output></p></div>
<div class="example-box" style="min-width:0;overflow-wrap:anywhere"><h3>المشاهدة الأولى X₁ (غير متحيّز)</h3><p>التباين: <output id="esa-crlb-variance-first" dir="ltr">—</output></p><p>الكفاءة: <output id="esa-crlb-efficiency-first" dir="ltr">—</output></p><p>التباين نسبةً إلى الحد: <output id="esa-crlb-ratio" dir="ltr">—</output></p></div>
</div>
<div class="esa-math-ltr" dir="ltr">\[
\operatorname{Efficiency}(\bar X)=100\%,\qquad
\operatorname{Efficiency}(X_1)=\frac{1}{n}\times100\%.
\]</div>
<p>عند <span dir="ltr">p=0.30</span> و<span dir="ltr">n=20</span> تكون معلومات فيشر نحو <span dir="ltr">95.238095</span>، وحد التباين <span dir="ltr">0.010500</span>، وتباين المشاهدة الأولى <span dir="ltr">0.210000</span>، وكفاءتها <span dir="ltr">5%</span>. وعند <span dir="ltr">n=1</span> يتطابق المقدّران ويحقق كلاهما الحد.</p>
<p><strong>تنبيه:</strong> تُستبعد القيمتان <span dir="ltr">p=0</span> و<span dir="ltr">p=1</span> من تطبيق صيغة حد كرامر–راو المنتظمة. جميع النتائج هنا مشروطة بفرض استقلال المشاهدات وتماثل توزيعها. تُعرض نسب الكفاءة للمقدّرات غير المتحيّزة فقط.</p>
</section>
<h2>7. حدود النظرية</h2>
<p>يتطلب الحد المألوف شروط انتظام تضمن صحة هوية الدرجة ووجود معلومات فيشر موجبة ومنتهية. لا تطبّق الصيغة ذاتها دون تحقق عند وجود حدود للمعلمة، أو دعم يعتمد على المعلمة، أو تقدير متحيّز، أو عندما لا تُستوفى شروط تبادل الاشتقاق مع التكامل. الحد خاص بتباين المقدّر غير المتحيّز ولا يساوي بالضرورة أقل متوسط مربعات خطأ بين جميع المقدّرات الممكنة.</p>
<h2>8. ماذا نتعلّم بعد ذلك؟</h2>
<p>يمكن استكمال المفاهيم عبر <a href="/mathematical-statistics/fisher-information-and-efficiency/efficiency-and-achieving-the-bound/" lang="en" dir="ltr">Efficiency and Achieving the Bound (English)</a>. للمزيد من الأسس النظرية، يُنصح بمراجعة مفهوم الإمكان ودالة الدرجة وشروط الانتظام.</p>
<div class="summary-box"><h2>الخلاصة</h2><ul class="bullets">
<li>حد كرامر–راو الأدنى يربط تباين المقدّر المنتظم غير المتحيّز بمعلومات فيشر.</li>
<li>هوية الدرجة تعطي تغايراً مقداره واحد بين المقدّر غير المتحيّز للمعلمة والدرجة، وليس تعامداً.</li>
<li>في نموذج برنولي المستقل يساوي الحد <span dir="ltr">p(1−p)/n</span> ويحققه متوسط العينة تماماً.</li>
<li>قد يكون مقدّران غير متحيّزين لكن بكفاءتين مختلفتين نتيجة استعمال معلومات مختلفة من العينة.</li>
<li>تنطبق النتائج ضمن شروطها، ولا تبرّر تطبيق الحد نفسه على مقدّرات متحيّزة دون تعديل.</li>
</ul></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/">الصفحة العربية الرئيسية</a><a class="btn" href="/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/" lang="en" dir="ltr">English version</a></div>
</div></section>
<script src="/js/bernoulli-crlb-explorer.js" defer></script>
