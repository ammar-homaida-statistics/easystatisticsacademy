---
layout: default
title: قاعدة الضرب في الاحتمالات
description: شرح عربي مفصل لقاعدة الضرب في الاحتمالات والأحداث المستقلة والتابعة وسحب البطاقات دون إرجاع وشجرة احتمالات تفاعلية مشتركة باللغتين.
permalink: /ar/probability/conditional/multiplication-rule/
lang: ar
sidebar: false
translation_pair: multiplication-rule
math: true
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">الاحتمال الشرطي</span><span class="badge">الاستقلال</span></div>
<h1>قاعدة الضرب في الاحتمالات</h1>
<p><a href="/probability/conditional/multiplication-rule/" lang="en" dir="ltr">English — Multiplication Rule</a></p>
<p class="lead">تمكّننا قاعدة الضرب من حساب احتمال وقوع حدثين معًا باستخدام احتمال أحدهما واحتمال الآخر بشرط تحقّق الأول، ومن ثم تحليل التجارب المتتابعة والمخططات الشجرية.</p>
</div></section>
<section class="section"><div class="content-narrow">
<h2>من الاحتمال الشرطي إلى قاعدة الضرب</h2>
<p>ليكن A وB حدثين. إذا كان احتمال A موجبًا، فإن تعريف الاحتمال الشرطي يعطي نسبة التقاطع إلى احتمال A. بضرب الطرفين في P(A) نحصل على قاعدة الضرب:</p>
<div dir="ltr" class="esa-ar-math">\[
P(B\mid A)=\frac{P(A\cap B)}{P(A)}
\quad\Longrightarrow\quad
P(A\cap B)=P(A)P(B\mid A),\quad P(A)>0.
\]</div>
<p>وبتغيير اتجاه الشرط يمكن كتابة الصيغة المكافئة عندما يكون احتمال B موجبًا:</p>
<div dir="ltr" class="esa-ar-math">\[
P(A\cap B)=P(B)P(A\mid B),\quad P(B)>0.
\]</div>
<p>تعبر القاعدتان عن احتمال التقاطع نفسه؛ لكن اختيار الصيغة يعتمد على أي الاحتمالات المشروطة نعرفه في المسألة.</p>
<h2>الأحداث المستقلة والأحداث التابعة</h2>
<p>عندما يكون A وB مستقلين، فإن معرفة وقوع A لا تغيّر احتمال وقوع B، ولذلك تختزل قاعدة الضرب إلى حاصل ضرب الاحتمالين الهامشيين:</p>
<div dir="ltr" class="esa-ar-math">\[
A\perp B \quad\Longrightarrow\quad P(A\cap B)=P(A)P(B).
\]</div>
<p>لا تستخدم هذه الصيغة المختصرة للأحداث التابعة. فالسحب المتتابع دون إرجاع مثال واضح على اعتماد السحبة الثانية على الأولى.</p>
<h2>مثال محلول: ورقتا آص دون إرجاع</h2>
<p>نسحب ورقتين من مجموعة قياسية مكونة من 52 ورقة، تحتوي على أربع أوراق آص، دون إعادة الورقة الأولى. احتمال أن تكون الورقتان آص هو:</p>
<div dir="ltr" class="esa-ar-math">\[
P(\text{آص أولًا وآص ثانيًا})
=\frac{4}{52}\times\frac{3}{51}
=\frac{1}{221}\approx0.00452489.
\]</div>
<p>بعد اختيار آص في السحبة الأولى، لا يبقى إلا ثلاث أوراق آص من أصل 51 ورقة. لذلك لا يجوز استعمال \((4/52)^2\) في حالة السحب دون إرجاع.</p>
<h2>مثال الاستقلال: رمي قطعتين نقديتين</h2>
<p>عند رمي قطعتين عادلتين ومستقلتين، احتمال ظهور الصورة في المرتين يساوي ربعًا:</p>
<div dir="ltr" class="esa-ar-math">\[
P(H_1\cap H_2)=\frac12\times\frac12=\frac14.
\]</div>
<h2>مثال للطلاب: الدراسة والنجاح</h2>
<p>لنفترض أن 60% من الطلاب يدرسون، وأن 90% من الدارسين ينجحون، في حين ينجح 40% من غير الدارسين. احتمال أن يدرس الطالب وينجح يساوي \(0.6\times0.9=0.54\)، بينما احتمال النجاح إجمالًا يساوي \(0.54+0.4\times0.4=0.70\). لا تُفسَّر هذه العلاقة على أنها دليل على السببية.</p>
</div></section>
<section class="section"><div class="content-narrow">
<div class="concept-box esa-conditional-tree" id="esa-conditional-tree-explorer"
         role="group" aria-labelledby="esa-conditional-tree-heading">
      <h2 id="esa-conditional-tree-heading">شجرة الاحتمالات الشرطية التفاعلية</h2>
      <p>افترض مجموعة من الطلاب: الطالب يدرس أو لا يدرس، ثم ينجح أو لا ينجح. نضرب احتمالات كل مسار للحصول على احتمال مشترك، ثم نجمع المسارات المتنافية ونستخدم قاعدة بايز لحساب الاحتمال العكسي.</p>
      <div class="esa-conditional-tree-fields">
        <div>
          <label for="esa-tree-study"><strong>احتمال الدراسة:
            <output id="esa-tree-study-value" for="esa-tree-study">0.60</output></strong></label>
          <input id="esa-tree-study" type="range" min="0.05" max="0.95" step="0.05" value="0.6">
        </div>
        <div>
          <label for="esa-tree-pass-study"><strong>احتمال النجاح بشرط الدراسة:
            <output id="esa-tree-pass-study-value" for="esa-tree-pass-study">0.90</output></strong></label>
          <input id="esa-tree-pass-study" type="range" min="0" max="1" step="0.05" value="0.9">
        </div>
        <div>
          <label for="esa-tree-pass-no-study"><strong>احتمال النجاح بشرط عدم الدراسة:
            <output id="esa-tree-pass-no-study-value" for="esa-tree-pass-no-study">0.40</output></strong></label>
          <input id="esa-tree-pass-no-study" type="range" min="0" max="1" step="0.05" value="0.4">
        </div>
      </div>
      <p class="muted-mini">تصف أشرطة التمرير احتمالات افتراضية لا علاقات سببية. احتمالا النجاح والإخفاق بعد كل فرع مجموعهما واحد، ويكون احتمال كل فرع في المرحلة الأولى موجبًا، لذا فاحتمال النجاح المشروط بكل فرع معرّف.</p>
      <div class="esa-tree-results" role="status" aria-live="polite" aria-atomic="true">
        <h3>شجرة الاحتمالات من مرحلتين</h3>
        <ul class="esa-tree-root">
          <li>
            <strong>يدرس — P(Study) = <output id="esa-tree-p-study">0.6000</output></strong>
            <ul>
              <li>نجاح: P(Pass | Study) = <output id="esa-tree-p-pass-study">0.9000</output>
                <span class="esa-tree-path">الاحتمال المشترك P(Study and Pass) = <output id="esa-tree-joint-study-pass">0.5400</output></span>
              </li>
              <li>إخفاق: P(No Pass | Study) = <output id="esa-tree-p-fail-study">0.1000</output>
                <span class="esa-tree-path">الاحتمال المشترك P(Study and No Pass) = <output id="esa-tree-joint-study-fail">0.0600</output></span>
              </li>
            </ul>
          </li>
          <li>
            <strong>لا يدرس — P(No Study) = <output id="esa-tree-p-no-study">0.4000</output></strong>
            <ul>
              <li>Pass: P(Pass | No Study) = <output id="esa-tree-p-pass-no-study">0.4000</output>
                <span class="esa-tree-path">الاحتمال المشترك P(No Study and Pass) = <output id="esa-tree-joint-no-study-pass">0.1600</output></span>
              </li>
              <li>No pass: P(No Pass | No Study) = <output id="esa-tree-p-fail-no-study">0.6000</output>
                <span class="esa-tree-path">الاحتمال المشترك P(No Study and No Pass) = <output id="esa-tree-joint-no-study-fail">0.2400</output></span>
              </li>
            </ul>
          </li>
        </ul>
        <h3>تتبّع المسارات</h3>
        <p><strong>الضرب:</strong> P(Study and Pass) = P(Study) × P(Pass | Study) =
          <output id="esa-tree-multiply">0.5400</output>.</p>
        <p><strong>الجمع:</strong> P(Pass) = P(Study and Pass) + P(No Study and Pass) =
          <output id="esa-tree-total-pass">0.7000</output>.</p>
        <p><strong>قاعدة بايز:</strong> P(Study | Pass) = P(Study and Pass) / P(Pass) =
          <output id="esa-tree-bayes">0.7714</output>.</p>
        <p id="esa-tree-undefined-note" hidden>
          إذا كان P(Pass)=0 فإن احتمال الدراسة بشرط النجاح غير معرّف؛ لا يجوز الشرط على حدث احتماله صفر.</p>
      </div>
      <svg id="esa-tree-chart" role="img" viewBox="0 0 620 260" dir="ltr" style="display:block;width:100%;height:auto" aria-label="احتمالات المسارات الأربعة"></svg>
      <button id="esa-tree-reset" class="btn btn-outline" type="button">استعادة مثال شجرة الاحتمالات</button>
      <p class="muted-mini">مجموع الاحتمالات المشتركة للمسارات الأربعة يساوي واحدًا قبل التقريب. يتصل المثال بدرس <a href="/ar/probability/conditional/law-of-total-probability/">قانون الاحتمال الكلي</a> ودرس <a href="/ar/probability/conditional/bayes-theorem/">نظرية بايز</a> لفهم الاحتمال العكسي.</p>
    </div>
    <style>
      #esa-conditional-tree-explorer {box-sizing:border-box;width:100%;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-conditional-tree-explorer .esa-conditional-tree-fields {
        display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,225px),1fr));gap:14px;
        margin:16px 0
      }
      #esa-conditional-tree-explorer .esa-conditional-tree-fields>div {min-width:0}
      #esa-conditional-tree-explorer label {display:block;margin-bottom:10px}
      #esa-conditional-tree-explorer input[type="range"] {box-sizing:border-box;display:block;width:100%;max-width:100%;min-width:0;margin:0;padding:0}
      #esa-conditional-tree-explorer .esa-tree-root,
      #esa-conditional-tree-explorer .esa-tree-root ul {list-style:none;padding:0;margin:12px 0}
      #esa-conditional-tree-explorer .esa-tree-root>li {margin:14px 0;padding-left:12px;border-left:3px solid #64748b}
      #esa-conditional-tree-explorer .esa-tree-root>li>ul {padding-left:12px;margin:8px 0;border-left:2px solid #0d9488}
      #esa-conditional-tree-explorer .esa-tree-root>li>ul>li {margin:10px 0;padding-left:8px}
      #esa-conditional-tree-explorer .esa-tree-path {display:block;font-size:.94em}
      #esa-conditional-tree-explorer .esa-tree-results h3 {font-size:1.05em;margin:12px 0 6px}
      #esa-conditional-tree-explorer .esa-tree-results p {margin:10px 0}
      #esa-conditional-tree-explorer [hidden] {display:none!important}
    </style>
    <script defer src="/js/conditional-tree-explorer.js"></script>
<h2>قاعدة الضرب لثلاثة أحداث</h2>
<p>عندما تقع الأحداث على مراحل، نضرب احتمال المرحلة الأولى في احتمال الثانية بشرط الأولى، ثم احتمال الثالثة بشرط تحقق المرحلتين السابقتين:</p>
<div dir="ltr" class="esa-ar-math">\[
P(A\cap B\cap C)=P(A)\,P(B\mid A)\,P(C\mid A\cap B).
\]</div>
<p>تتطلب العوامل الشرطية في هذه الصيغة أن تكون أحداث الشرط ذات احتمال موجب. وإذا كان أحد الأحداث الشرطية مستحيلاً، تُستخدم صيغة مناسبة غير مشروطة بدلًا من القسمة على الصفر.</p>
<h2>تفسير شجرة الاحتمالات</h2>
<p>يمثل كل مسار نهائي تسلسلًا محددًا من النتائج. نضرب الاحتمالات على طول المسار للحصول على احتمال التسلسل، ثم نجمع احتمالات المسارات النهائية المتنافية التي تؤدي إلى الحدث المطلوب. ويجب أن يساوي مجموع احتمالات جميع المسارات النهائية الواحد.</p>
<h2>أخطاء يجب تجنبها</h2>
<ul class="bullets">
<li>افتراض الاستقلال دون دليل أو دون معطيات تدعمه.</li>
<li>نسيان تعديل المقام عند السحب دون إرجاع.</li>
<li>جمع احتمالات مسارات متداخلة على أنها متنافية.</li>
<li>الخلط بين \(P(A\mid B)\) و\(P(B\mid A)\).</li>
<li>الشرط على حدث احتماله صفر في التعريف الابتدائي.</li>
</ul>
<h2>خلاصة الدرس</h2>
<p>تربط قاعدة الضرب بين الاحتمالات الشرطية واحتمالات التقاطع. وتُستخدم في السحب المتتابع، ومخططات الشجرة، والاستدلال البايزي، وتحليل مسارات الأحداث.</p>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/conditional/what-is-conditional-probability/">السابق: الاحتمال الشرطي</a>
<a class="btn" href="/ar/probability/conditional/law-of-total-probability/">التالي: قانون الاحتمال الكلي</a></div>
</div></section>
<style>.esa-ar-math{direction:ltr;max-width:100%;overflow-x:auto}.esa-ar-math mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}
html[dir="rtl"] #esa-conditional-tree-explorer .esa-tree-root>li{border-left:0;border-right:3px solid #64748b;padding-left:0;padding-right:12px}
html[dir="rtl"] #esa-conditional-tree-explorer .esa-tree-root>li>ul{border-left:0;border-right:2px solid #0d9488;padding-left:0;padding-right:12px}
html[dir="rtl"] #esa-conditional-tree-explorer .esa-tree-root>li>ul>li{padding-left:0;padding-right:8px}
</style>