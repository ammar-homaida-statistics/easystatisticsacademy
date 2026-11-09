---
layout: default
title: التباين والانحراف المعياري للمتغير العشوائي
description: درس عربي عن التباين والانحراف المعياري للمتغير العشوائي، والأمثلة المنفصلة والمتصلة وقواعد التحويل الخطي.
permalink: /ar/probability/random-variables/variance-and-standard-deviation/
lang: ar
math: true
sidebar: false
translation_pair: random-variable-variance
learning_resource: true
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">المتغيرات العشوائية</span><span class="badge">التشتت</span></div>
<h1>التباين والانحراف المعياري</h1>
<p class="lead">تصف القيمة المتوقعة مركز التوزيع، بينما يصف التباين مدى تشتت النتائج حول هذا المركز.</p>
<p><a href="/probability/random-variables/variance-and-standard-deviation/" lang="en" dir="ltr">Read in English: Variance and Standard Deviation</a></p>
</div></section>
<section><div class="content-narrow" dir="rtl">
<h2>لماذا نحتاج إلى قياس التشتت؟</h2>
<p>قد يكون لمتغيرين المتوسط نفسه ولكن بتشتت مختلف. إذا كان العائد الأول 100 دائماً، والعائد الثاني صفراً أو 200 باحتمال نصف لكل منهما، فالمتوسط في الحالتين 100، والتباين في الأولى صفر وفي الثانية 10000.</p>
<h2>الانحراف عن المتوسط</h2>
<p>الانحراف هو الفرق بين قيمة المتغير والمتوسط النظري. الانحرافات الموجبة والسالبة تتلاشى عند جمعها موزونةً بالاحتمالات، لذلك نربّعها قبل حساب متوسطها.</p>
<div class="esa-variance-math" dir="ltr">\[\mu=E(X),\qquad \operatorname{Var}(X)=E[(X-\mu)^2]\geq0.\]</div>
<p>عندما يكون العزم الثاني منتهياً، تتوافر الصيغة المكافئة:</p>
<div class="esa-variance-math" dir="ltr">\[\operatorname{Var}(X)=E(X^2)-[E(X)]^2,\qquad \operatorname{SD}(X)=\sqrt{\operatorname{Var}(X)}.\]</div>
<p>وحدة التباين هي مربع وحدة المتغير، أما الانحراف المعياري فوحدته هي وحدة المتغير نفسها. ينبغي التمييز بين تباين التوزيع النظري وتباين عينة من بيانات مشاهدة.</p>
<h2>توزيع منفصل: مثال محلول</h2>
<p>ليكن المتغير يأخذ القيم 0 و1 و2 باحتمالات 0.2 و0.5 و0.3، ومجموع الاحتمالات واحد:</p>
<div class="esa-variance-math" dir="ltr">\[E(X)=0(0.2)+1(0.5)+2(0.3)=1.1,\qquad E(X^2)=0+0.5+4(0.3)=1.7.\]</div>
<div class="esa-variance-math" dir="ltr">\[\operatorname{Var}(X)=1.7-1.1^2=0.49,\qquad \operatorname{SD}(X)=0.7.\]</div>
<p>لا يعني الانحراف المعياري 0.7 أن كل نتيجة تبعد عن المتوسط بالمقدار نفسه.</p>
<h2>توزيع متصل</h2>
<p>إذا كانت للمتغير كثافة \(f(x)\) وكان العزم الثاني منتهياً، نحسب:</p>
<div class="esa-variance-math" dir="ltr">\[\operatorname{Var}(X)=\int_{-\infty}^{\infty}(x-\mu)^2f(x)\,dx.\]</div>
<p>للتوزيع المنتظم على الفترة \([a,b]\) مع \(a&lt;b\)، يكون:</p>
<div class="esa-variance-math" dir="ltr">\[E(X)=\frac{a+b}{2},\qquad \operatorname{Var}(X)=\frac{(b-a)^2}{12},\qquad \operatorname{SD}(X)=\frac{b-a}{\sqrt{12}}.\]</div>
<p>عندما تكون الفترة \([0,2]\)، يكون التباين \(1/3\) والانحراف المعياري \(1/\sqrt3\).</p>
<h2>الإزاحة وتغيير المقياس</h2>
<p>عندما يكون التباين منتهياً وللثابتين الحقيقيين \(a,b\):</p>
<div class="esa-variance-math" dir="ltr">\[E(a+bX)=a+bE(X),\quad \operatorname{Var}(a+bX)=b^2\operatorname{Var}(X),\quad \operatorname{SD}(a+bX)=|b|\operatorname{SD}(X).\]</div>
<p>إضافة ثابت لا تغير التباين. أما ضرب النتائج في عدد سالب فيعكس ترتيبها ولا يجعل التباين سالباً؛ وعند \(b=0\) يصبح المتغير ثابتاً وتباينه صفراً.</p>
<h2>أخطاء شائعة</h2>
<ul class="bullets"><li>حساب متوسط الانحرافات الخام بدلاً من مربعاتها.</li><li>الخلط بين وحدة التباين ووحدة الانحراف المعياري.</li><li>استخدام صيغة العزم الثاني دون تحقق وجوده.</li><li>اعتبار المتوسط نتيجة مضمونة في كل تجربة.</li><li>الخلط بين التباين النظري ومقدّر تباين العينة.</li></ul>
<div class="summary-box"><h2>الخلاصة</h2><p>التباين متوسط مربع الانحراف الموزون بالاحتمالات. تترك الإزاحة التباين دون تغيير، ويغيّره التحويل الضربي بمربع المعامل.</p></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/random-variables/expectation/">السابق: القيمة المتوقعة</a><a class="btn" href="/ar/">الدروس العربية</a></div>
</div></section>
<style>.esa-variance-math{direction:ltr;max-width:100%;overflow-x:auto;padding:4px 0}</style>