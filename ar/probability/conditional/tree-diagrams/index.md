---
layout: default
title: مخططات الشجرة الاحتمالية
permalink: /ar/probability/conditional/tree-diagrams/
description: تعلّم بناء شجرة احتمالية وحساب احتمالات المسارات والجمع بين النتائج المتنافية مع مثال تفاعلي.
lang: ar
translation_pair: tree-diagrams
math: true
---
<section class="hero hero-section"><div class="hero-card"><h1>مخططات الشجرة الاحتمالية</h1><p class="lead">تساعدنا الشجرة الاحتمالية على تتبّع الأحداث المتتابعة: نضرب احتمالات الفروع على المسار الواحد ثم نجمع المسارات المتنافية التي تحقق الحدث المطلوب.</p><p><a href="/probability/conditional/tree-diagrams/" lang="en" dir="ltr">Read this lesson in English</a></p></div></section>
<section><div class="content-narrow" dir="rtl"><h2>فروع الشجرة والمسارات النهائية</h2><p>تبدأ الشجرة بالتجربة الأولى، ويخرج من كل عقدة فرع لكل نتيجة ممكنة. يجب أن يكون مجموع احتمالات الفروع الخارجة من العقدة واحدًا. احتمال المسار الكامل هو حاصل ضرب احتمالات الفروع الشرطية على طول المسار.</p><div class="esa-ar-math" dir="ltr">\\[P(A\\cap B)=P(A)P(B\\mid A).\\]</div><p>إذا كان A وB مستقلين، تصبح الصيغة P(A∩B)=P(A)P(B). أمّا مع الاعتماد فلا نستبدل الاحتمال الشرطي بالهامشي دون مبرر.</p><h2>مثال: رمي قطعة نقود مرتين</h2><p>إذا كانت القطعة عادلة والرميتان مستقلتين، فالمسارات HH وHT وTH وTT لكل منها احتمال 0.25، ومجموعها واحد. الحدث «ظهور الصورة مرة واحدة على الأقل» يشمل HH وHT وTH، لذا احتماله 0.75.</p><div class="esa-ar-math" dir="ltr">\\[P(\\text{at least one head})=P(HH)+P(HT)+P(TH)=\\tfrac34.\\]</div><h2>مسارات غير مستقلة: سحب دون إرجاع</h2><p>لدينا رزمة تضم 52 ورقة فيها 4 أوراق آس. احتمال الحصول على ورقتي آس متتاليتين دون إرجاع هو حاصل ضرب 4/52 و3/51، ويساوي 1/221 تقريبًا 0.004525. يتغير احتمال السحب الثاني بعد مشاهدة الأول.</p><div class="esa-ar-math" dir="ltr">\\[P(\\text{two aces})=\\frac4{52}\\frac3{51}=\\frac1{221}.\\]</div><h2>جمع المسارات وقانون الاحتمال الكلي</h2><p>إذا شكلت A₁,…,Aₖ تقسيمًا متنافيًا وشاملًا للفضاء وكان لكل حالة احتمال موجب، نحسب احتمال B بجمع احتمالات المسارات الموصلة إليه:</p><div class="esa-ar-math" dir="ltr">\\[P(B)=\\sum_{i=1}^{k}P(A_i)P(B\\mid A_i).\\]</div><p>عند احتمال صفر لأحد فروع الشرط، يكون الاحتمال الشرطي عليه غير معرّف في التعريف الابتدائي؛ ويمكن حساب احتمال المسار مباشرةً بوصفه صفرًا دون قسمة على الصفر.</p><h2>مختبر شجرة الاحتمالات التفاعلي</h2><p>جرّب احتمالات الدراسة والنجاح باستخدام الحسابات المشتركة نفسها الموجودة في الدرس الإنجليزي عن قاعدة الضرب. تحقق أن مجموع احتمالات المسارات النهائية الأربعة يساوي واحدًا قبل التقريب.</p><div class="concept-box esa-conditional-tree" id="esa-conditional-tree-explorer"
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
<h2>أخطاء شائعة</h2><ul class="bullets"><li>الجمع بين مسارات متداخلة دون استبعاد التكرار.</li><li>افتراض استقلال مراحل السحب دون إرجاع.</li><li>استخدام احتمال شرطي عند شرط احتماله صفر.</li><li>نسيان فحص مجموع الاحتمالات النهائية.</li></ul><div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/conditional/bayes-theorem/">نظرية بايز</a><a class="btn" href="/ar/probability/conditional/multiplication-rule/">قاعدة الضرب</a></div></div></section>