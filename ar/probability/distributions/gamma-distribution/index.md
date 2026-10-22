---
layout: default
title: توزيع غاما
description: درس عربي شامل عن توزيع غاما ومعلمتي الشكل والمعدل ودالة الكثافة والمتوسط والتباين وحالة إرلانغ ومختبر تفاعلي للانتظار حتى عدة أحداث بواسونية.
permalink: /ar/probability/distributions/gamma-distribution/
lang: ar
sidebar: false
translation_pair: gamma-distribution
math: true
---

<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">التوزيعات المستمرة</span><span class="badge">أزمنة الانتظار</span></div>
<h1>توزيع غاما (Gamma Distribution)</h1>
<p><a href="/probability/distributions/gamma-distribution/" lang="en" dir="ltr">English — Gamma Distribution</a></p>
<p class="lead">كيف يتغير توزيع زمن الانتظار إذا كنا ننتظر وقوع عدة أحداث، بدلًا من انتظار الحدث الأول فقط؟</p>
<div class="hero-actions">
<a class="btn btn-outline" href="/ar/probability/distributions/exponential-distribution/">← الدرس السابق: التوزيع الأسي</a>
<a class="btn btn-outline" href="/ar/probability/distributions/poisson-distribution/">توزيع بواسون</a>
</div></div></section>

<section class="section"><div class="content-narrow">
<h2>ما توزيع غاما؟</h2>
<p>توزيع غاما توزيع احتمالي <strong>مستمر</strong> لمتغير موجب غالبًا ما يمثّل زمنًا أو مقدارًا غير سالب، مع إمكانية تغيير شكل الكثافة باستخدام معلمتين. إذا كانت الأحداث تقع وفق <strong>عملية بواسون متجانسة</strong>، فإن زمن الانتظار حتى الحدث رقم <span dir="ltr">r</span> يتبع توزيع غاما بمعلمة شكل صحيحة موجبة <span dir="ltr">r</span>. يُطلق على هذه الحالة اسم <strong>توزيع إرلانغ (Erlang)</strong>.</p>
<div class="concept-box"><strong>تمييز مهم:</strong><p>يسمح توزيع غاما العام بأن تكون معلمة الشكل <strong>أي عدد حقيقي موجب</strong>، لكن تفسيرها بوصفها «عدد الأحداث المنتظرة» يصح مباشرة فقط عندما تكون عددًا صحيحًا موجبًا في نموذج بواسون المتجانس.</p></div>

<h2>الفكرة الأساسية</h2>
<p>يجيب التوزيع الأسي عن سؤال: «كم ننتظر حتى <strong>أول</strong> حدث؟». أما نموذج إرلانغ فيجيب عن سؤال: «كم ننتظر حتى الحدث <strong>الثالث أو الخامس</strong> مثلًا؟». يتألف الزمن حتى الحدث رقم <span dir="ltr">r</span> من مجموع <span dir="ltr">r</span> فترات انتظار أسية مستقلة لها المعدل نفسه.</p>
<div class="example-box"><p>إذا وصلت المكالمات بمعدل ثابت وفق نموذج بواسون، فزمن الانتظار حتى المكالمة الرابعة يمثّل حالة إرلانغ ذات الشكل <span dir="ltr">r=4</span>.</p></div>

<h2>العلاقة بالتوزيع الأسي</h2>
<p>التوزيع <a href="/ar/probability/distributions/exponential-distribution/">الأسي</a> حالة خاصة من غاما عند الشكل <span dir="ltr">α=1</span>. وفي هذه الحالة تكافئ الكثافة <span dir="ltr">λe<sup>−λt</sup></span>، كما أن زمن الانتظار حتى أول حدث في عملية بواسون هو زمن أسي.</p>
<p>في حال <span dir="ltr">r=2</span> أو أكبر، لا تكون الكثافة أسية عمومًا، ولا يتمتع توزيع إرلانغ بخاصية انعدام الذاكرة الخاصة بالتوزيع الأسي.</p>

<h2>معلمتا الشكل والمعدل</h2>
<p>يعتمد توزيع غاما على معلمتين موجبتين: <strong>الشكل</strong> <span dir="ltr">α</span> الذي يغيّر هيئة المنحنى، و<strong>المعدل</strong> <span dir="ltr">λ</span> الذي يضبط المقياس الزمني. عند قياس الزمن بالدقائق تكون وحدة <span dir="ltr">λ</span> هي دقيقة⁻¹.</p>
<div class="esa-gamma-equation" dir="ltr" tabindex="0" role="region" aria-label="شرط المعلمتين">\[
\alpha>0,\qquad\lambda>0.
\]</div>
<p>يجب عدم الخلط بين معلمة <strong>المعدل</strong> <span dir="ltr">λ</span> ومعلمة <strong>المقياس</strong> <span dir="ltr">θ=1/λ</span> المستخدمة في بعض البرامج والمراجع؛ فاختلاف اصطلاح المعلمات يؤدي إلى نتائج خاطئة.</p>

<h2>الترميز</h2>
<div class="esa-gamma-equation" dir="ltr" tabindex="0" role="region" aria-label="ترميز غاما">\[
T\sim\operatorname{Gamma}(\alpha,\lambda)\quad
\text{(shape–rate parameterization)}.
\]</div>
<p>نستخدم في الدرس ترتيب <span dir="ltr">(الشكل، المعدل)</span> صراحةً، وليس <span dir="ltr">(الشكل، المقياس)</span>.</p>

<h2>دالة الكثافة الاحتمالية</h2>
<p>تُعطى كثافة غاما ذي معلمة المعدل بالعلاقة الآتية:</p>
<div class="esa-gamma-equation" dir="ltr" tabindex="0" role="region" aria-label="دالة كثافة غاما">\[
f_T(t)=
\begin{cases}
\dfrac{\lambda^{\alpha}}{\Gamma(\alpha)}
t^{\alpha-1}e^{-\lambda t},&t>0,\\
0,&t<0.
\end{cases}
\]</div>
<p>تُفسّر قيمة الكثافة عند الصفر وفق قيمة الشكل: تكون صفرًا عند <span dir="ltr">α&gt;1</span>، وتساوي <span dir="ltr">λ</span> عند <span dir="ltr">α=1</span>، وتتباعد باتجاه المالانهاية عندما <span dir="ltr">0&lt;α&lt;1</span>. قيمة الكثافة عند نقطة واحدة لا تغيّر أي احتمال، لأن <span dir="ltr">P(T=t)=0</span>.</p>

<h2>دالة غاما الرياضية</h2>
<p>الرمز <span dir="ltr">Γ(α)</span> يشير إلى دالة غاما، وهي تعميم مناسب لدالة المضروب للقيم غير الصحيحة الموجبة:</p>
<div class="esa-gamma-equation" dir="ltr" tabindex="0" role="region" aria-label="تعريف دالة غاما">\[
\Gamma(\alpha)=\int_0^\infty u^{\alpha-1}e^{-u}\,du,\quad\alpha>0,
\qquad\Gamma(n)=(n-1)!\ (n=1,2,\ldots).
\]</div>
<p>تجعل الدالة التكامل الكلي لكثافة غاما مساويًا للواحد.</p>

<h2>الحالة الخاصة: الشكل يساوي واحدًا</h2>
<p>عند <span dir="ltr">α=1</span> يكون <span dir="ltr">Γ(1)=1</span>، وبالتعويض في الكثافة نحصل على:</p>
<div class="esa-gamma-equation" dir="ltr" tabindex="0" role="region" aria-label="غاما عند الشكل واحد">\[
f_T(t)=\lambda e^{-\lambda t},\quad t\ge0.
\]</div>
<p>وهذه بالضبط كثافة التوزيع الأسي ذي معدل الأحداث <span dir="ltr">λ</span>.</p>

<h2>تفسير معلمة الشكل</h2>
<p>إذا كان <span dir="ltr">α=r</span> عددًا صحيحًا موجبًا، يمثل <span dir="ltr">r</span> ترتيب الحدث المنتظَر في عملية بواسون المتجانسة. عند <span dir="ltr">r=2</span> ننتظر الحدث الثاني، وعند <span dir="ltr">r=5</span> ننتظر الخامس.</p>
<div class="table-wrap"><table><thead><tr><th>الشكل</th><th>تفسيره في إرلانغ</th></tr></thead><tbody>
<tr><td dir="ltr">r=1</td><td>انتظار الحدث الأول: توزيع أسي</td></tr>
<tr><td dir="ltr">r=3</td><td>انتظار الحدث الثالث</td></tr>
<tr><td dir="ltr">r=5</td><td>انتظار الحدث الخامس</td></tr>
</tbody></table></div>
<p>عندما تكون <span dir="ltr">α=2.5</span> مثلًا، يكون توزيع غاما صالحًا رياضيًا، لكن لا يصح تفسيره بأنه «انتظار الحدث رقم 2.5».</p>

<h2>المتوسط أو القيمة المتوقعة</h2>
<div class="esa-gamma-equation" dir="ltr" tabindex="0" role="region" aria-label="متوسط غاما">\[
E(T)=\frac{\alpha}{\lambda}.
\]</div>
<p>يزداد زمن الانتظار المتوقع بزيادة الشكل عندما يبقى المعدل ثابتًا، ويتناقص كلما ازداد معدل الأحداث مع ثبات الشكل. وعند الشكل الصحيح، يساوي هذا مجموع متوسطات <span dir="ltr">r</span> فترات انتظار أسية.</p>

<h2>مثال على المتوسط</h2>
<p>إذا كان <span dir="ltr">r=4</span>، ومعدل الوصول <span dir="ltr">λ=2</span> لكل دقيقة، فإن متوسط انتظار الحدث الرابع يساوي:</p>
<div class="esa-gamma-equation" dir="ltr" tabindex="0" role="region" aria-label="متوسط انتظار الحدث الرابع">\[
E(T)=\frac{4}{2}=2\ \text{minutes}.
\]</div>
<p>النتيجة <strong>متوسط</strong> وليست زمنًا محددًا يلزم أن يتحقق في كل تجربة.</p>

<h2>التباين والانحراف المعياري</h2>
<div class="esa-gamma-equation" dir="ltr" tabindex="0" role="region" aria-label="التباين والانحراف المعياري">\[
\operatorname{Var}(T)=\frac{\alpha}{\lambda^2},\qquad
\operatorname{SD}(T)=\frac{\sqrt{\alpha}}{\lambda}.
\]</div>
<p>يقاس التباين بالزمن المربع، بينما يقاس الانحراف المعياري بالزمن. عند <span dir="ltr">r=4</span> و<span dir="ltr">λ=2/minute</span> يكون التباين <strong>1 دقيقة²</strong> والانحراف المعياري <strong>1 دقيقة</strong>.</p>

<h2>شكل توزيع غاما</h2>
<p>عندما يكون الشكل أقل من الواحد تنخفض الكثافة من قيمة مرتفعة جدًا قرب الصفر. وعند الشكل الذي يساوي واحدًا نحصل على الكثافة الأسية المتناقصة. وعند الشكل الأكبر من الواحد يبدأ المنحنى من الصفر ثم يصل إلى قمة ويهبط تدريجيًا، ويصبح أكثر تماثلًا نسبيًا بزيادة الشكل.</p>
<p>يبقى المتغير غير سالب، والكثافة ليست احتمالًا عند نقطة مفردة.</p>

<!-- Bilingual explorer shares its exact numerical engine with the English lesson. -->
<div class="concept-box esa-erlang-lab" id="esa-erlang-wait-explorer" role="group" aria-labelledby="esa-erlang-lab-heading">
<h2 id="esa-erlang-lab-heading">مختبر تفاعلي: زمن الانتظار في غاما/إرلانغ</h2>
<p>غيّر عدد الأحداث المطلوب <span dir="ltr">r</span>، ومعدل الوصول <span dir="ltr">λ</span>، والزمن المنقضي <span dir="ltr">t</span>. يقتصر هذا المختبر على <strong>الشكل الصحيح الموجب</strong> في عملية بواسون المتجانسة. يدعم توزيع غاما العام أشكالًا حقيقية موجبة أيضًا، لكنها لا تعبّر هنا عن ترتيب حدث.</p>
<div class="esa-erlang-fields">
<div><label for="esa-erlang-r">عدد الأحداث / الشكل r: <output id="esa-erlang-r-value" for="esa-erlang-r">4</output></label>
<input type="range" min="1" max="7" step="1" value="4" id="esa-erlang-r"/></div>
<div><label for="esa-erlang-rate">معدل الأحداث λ: <output id="esa-erlang-rate-value" for="esa-erlang-rate">2.00</output></label>
<input type="range" min="0.5" max="4" step="0.5" value="2" id="esa-erlang-rate"/></div>
<div><label for="esa-erlang-time">زمن الانتظار t: <output id="esa-erlang-time-value" for="esa-erlang-time">2.00</output></label>
<input type="range" min="0" max="12" step="0.25" value="2" id="esa-erlang-time"/></div>
</div>
<h3>كثافة إرلانغ والمساحة المظللة لاحتمال P(T ≤ t)</h3>
<svg id="esa-erlang-chart" viewBox="0 0 360 174" width="360" height="174" role="img"
aria-label="كثافة غاما إرلانغ مع احتمال تراكمي مظلل">
<line x1="34" y1="137" x2="339" y2="137" stroke="currentColor" stroke-width="1.4"/>
<line x1="34" y1="137" x2="34" y2="15" stroke="currentColor" stroke-width="1.4"/>
<path id="esa-erlang-shade" fill="#0d9488" fill-opacity=".45" d="M34 137 L34 137 Z"/>
<path id="esa-erlang-density-path" fill="none" stroke="#64748b" stroke-width="2" d="M34 137"/>
<line id="esa-erlang-time-marker" x1="83.3" y1="16" x2="83.3" y2="137" stroke="#0d9488" stroke-dasharray="4 3" stroke-width="1.2"/>
<text x="34" y="153" font-size="10" fill="currentColor" text-anchor="middle">0</text>
<text x="331" y="153" font-size="10" fill="currentColor" text-anchor="middle">12</text>
<text x="337" y="164" font-size="10" fill="currentColor">t</text>
<text x="8" y="14" font-size="10" fill="currentColor">PDF</text>
</svg>
<div class="esa-erlang-results" role="status" aria-live="polite" aria-atomic="true">
<p><strong>الكثافة عند t:</strong> <span dir="ltr">f(t) = <output id="esa-erlang-pdf">0.39073</output></span> لكل وحدة زمن؛ الكثافة ليست احتمالًا.</p>
<p><strong>احتمال وقوع الحدث رقم r قبل الزمن t:</strong> <span dir="ltr">P(T ≤ t) = <output id="esa-erlang-cdf">0.566530</output></span>.</p>
<p><strong>احتمال الانتظار لأطول من t:</strong> <span dir="ltr">P(T &gt; t) = <output id="esa-erlang-survival">0.433470</output></span>.</p>
<p><strong>المتوسط:</strong> <span dir="ltr">E(T) = r/λ = <output id="esa-erlang-mean">2.0000</output></span> وحدة زمن.
<strong>التباين:</strong> <span dir="ltr">r/λ² = <output id="esa-erlang-variance">1.0000</output></span> زمن².</p>
<p><strong>المقياس:</strong> <span dir="ltr">θ = 1/λ = <output id="esa-erlang-scale">0.5000</output></span> وحدة زمن.</p>
<p id="esa-erlang-special">عندما يساوي الشكل واحدًا نحصل على التوزيع الأسي ذي المعدل λ.</p>
</div>
<div class="esa-erlang-presets">
<button type="button" class="btn btn-outline" id="esa-erlang-reset">استعادة مثال إرلانغ</button>
<button type="button" class="btn btn-outline" id="esa-erlang-exponential">الحالة الأسية: الشكل 1</button>
</div>
<p class="muted-mini">عند الشكل الصحيح الموجب <span dir="ltr">r</span>، نحسب البقاء بالصيغة الدقيقة <span dir="ltr">e<sup>−λt</sup>Σ<sub>j=0</sub><sup>r−1</sup>(λt)<sup>j</sup>/j!</span>، ثم نحصل على التراكمية بطرح البقاء من الواحد. لا تمثل مساحة الرسم الجزء المظلل كل الاحتمال في الذيل غير المرئي. احتمالات الزمن المفرد تساوي صفرًا.</p>
</div>
    <style>
      #esa-erlang-wait-explorer {box-sizing:border-box;width:100%;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-erlang-wait-explorer .esa-erlang-fields {
        display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,185px),1fr));
        gap:14px;margin:16px 0
      }
      #esa-erlang-wait-explorer .esa-erlang-fields>div {min-width:0}
      #esa-erlang-wait-explorer label {display:block;margin-bottom:8px}
      #esa-erlang-wait-explorer input[type="range"] {
        display:block;box-sizing:border-box;width:100%;max-width:100%;
        min-width:0;margin:0;padding:0
      }
      #esa-erlang-wait-explorer h3 {font-size:1.05em;margin:15px 0 10px}
      #esa-erlang-wait-explorer svg {display:block;width:100%;height:auto;max-width:520px;margin:0 auto;overflow:visible}
      #esa-erlang-wait-explorer .esa-erlang-results p {margin:11px 0}
      #esa-erlang-wait-explorer .esa-erlang-presets {display:flex;flex-wrap:wrap;gap:8px}
    </style>
<script src="{{ '/js/gamma-erlang-explorer.js' | relative_url }}" defer></script>

<h2>ما توزيع إرلانغ؟</h2>
<p>إرلانغ اسم لحالة توزيع غاما عندما يكون الشكل <span dir="ltr">r</span> عددًا صحيحًا موجبًا. في عملية بواسون المتجانسة، يتبع مجموع فترات الانتظار المستقلة حتى <span dir="ltr">r</span> أحداث توزيع إرلانغ. تُستخدم هذه النماذج في الطوابير والاتصالات وتوقيت وصول المكالمات، عندما تتحقق افتراضات العملية.</p>

<h2>احتمالات إرلانغ التراكمية</h2>
<p>في المختبر التفاعلي، تؤخذ <span dir="ltr">r</span> صحيحة من 1 إلى 7، ويمكن حساب دالة البقاء بدقة بمجموع منتهٍ:</p>
<div class="esa-gamma-equation" dir="ltr" tabindex="0" role="region" aria-label="دالة البقاء لإرلانغ">\[
P(T>t)=e^{-\lambda t}\sum_{j=0}^{r-1}\frac{(\lambda t)^j}{j!},
\quad r\in\{1,2,\ldots\},\quad t\ge0.
\]</div>
<p>وبالتالي <span dir="ltr">P(T≤t)=1−P(T&gt;t)</span>. أما الشكل غير الصحيح فيتطلب استعمال دالة غاما غير المكتملة أو طرق عددية ملائمة، لا مجموع إرلانغ المنتهي.</p>

<h2>تطبيقات توزيع غاما</h2>
<ul class="bullets">
<li>نمذجة زمن الانتظار حتى وصول عدة أحداث في العمليات البواسونية المتجانسة.</li>
<li>نماذج المدة والاعتمادية عندما تسمح بنية البيانات بشكل ومعدل مناسبين.</li>
<li>أوقات الخدمة والاستجابة في بحوث العمليات ونظرية الطوابير.</li>
<li>بعض المتغيرات الموجبة الملتوية التي يكون نموذج غاما مناسبًا لها بعد التحقق.</li>
</ul>

<h2>علاقة غاما بتوزيعات أخرى</h2>
<p>عند <span dir="ltr">α=1</span> يتحول غاما إلى توزيع <a href="/ar/probability/distributions/exponential-distribution/">أسي</a>. عند الشكل الصحيح الموجب نحصل على إرلانغ. ويتصل أيضًا بنماذج <a href="/ar/probability/distributions/poisson-distribution/">بواسون</a> للعدّ، وبعائلة توزيع مربع كاي تحت اختيار مخصوص لمعلمتي الشكل والمعدل.</p>

<h2>لماذا نحتاج توزيع غاما؟</h2>
<p>يوفر مرونة أكبر من الأسي، لأن المعلمة الإضافية تغيّر شكل المنحنى. وهو يربط بين أزمنة الانتظار وعمليات العدّ، ويقدّم مثالًا مهمًا على الفرق بين مدلول رياضي عام وتفسير خاص بمسألة عملية.</p>

<h2>حدود نموذج غاما</h2>
<p>لا يصح تطبيق تفسير إرلانغ مباشرة عندما يكون الشكل غير صحيح، أو عندما تتغير معدلات الأحداث مع الزمن. كما أن رصد بيانات انتظار موجبة وحده لا يثبت استقلال الوصول أو ثبات معدل الخطر. افحص الافتراضات وملاءمة التوزيع والبدائل قبل التنبؤ.</p>

<h2>الدرس التالي</h2>
<p>تابع تعلّم أزمنة الانتظار في <a href="/ar/probability/distributions/exponential-distribution/">التوزيع الأسي</a>، وراجع <a href="/ar/probability/distributions/poisson-distribution/">توزيع بواسون</a> لمعرفة العلاقة بين عدد الأحداث وزمن وقوعها.</p>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>توزيع غاما عام وله معلمتا الشكل <span dir="ltr">α&gt;0</span> والمعدل <span dir="ltr">λ&gt;0</span>.</li>
<li>المتوسط <span dir="ltr">α/λ</span> والتباين <span dir="ltr">α/λ²</span>.</li>
<li>عند الشكل 1 نحصل على التوزيع الأسي.</li>
<li>عندما يكون الشكل صحيحًا موجبًا، يكون إرلانغ نموذجًا للانتظار حتى الحدث رقم <span dir="ltr">r</span> في عملية بواسون متجانسة.</li>
<li>للمعلمات غير الصحيحة تفسير توزيعي صحيح، ولكن ليس «حدثًا كسريًا» في عملية العدّ.</li>
</ul></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/distributions/exponential-distribution/">← التوزيع الأسي</a>
<a class="btn" href="/probability/distributions/gamma-distribution/" lang="en" dir="ltr">English — Gamma Distribution →</a></div>
</div></section>
<style>
.esa-gamma-equation{box-sizing:border-box;max-width:100%;min-width:0;overflow-x:auto;direction:ltr}
.esa-gamma-equation mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}
.esa-gamma-equation:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
#esa-erlang-wait-explorer [dir="ltr"]{unicode-bidi:isolate}
</style>