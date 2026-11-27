---
layout: default
title: فترة الثقة للفرق بين نسبتين
description: "شرح عربي لفترة الثقة للفرق بين نسبتي مجتمعين مستقلين: المقدِّر والخطأ المعياري غير المجمّع، وفترة والد مع مثال اختبار A/B، وفترة نيوكومب المبنية على ويلسون، ومعنى الصفر، مع مختبر تفاعلي."
permalink: /ar/inference/confidence-intervals/ci-for-difference-of-proportions/
lang: ar
sidebar: false
math: true
learning_resource: true
translation_pair: ci-for-difference-of-proportions
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاستدلال</span><span class="badge">فترات الثقة</span><span class="badge">مقارنة مجموعتين</span></div>
<h1>فترة الثقة للفرق بين نسبتين</h1>
{% include lab-noscript.html %}
<p class="lead">تقارن أسئلة إحصائية مهمة كثيرة بين نسب مئوية في مجموعتين.</p>
<p class="lead">وتساعد فترات الثقة للفرق بين نسبتين على تقدير مقدار اختلاف نسبتي المجتمعين مع أخذ عدم يقين المعاينة في الحسبان.</p>
<p><a href="/inference/confidence-intervals/ci-for-difference-of-proportions/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/confidence-intervals/ci-for-proportion/">درس ذو صلة: فترة الثقة للنسبة</a></p>
</div></section>
<section><div class="content-narrow">

<h2>1. السؤال البحثي</h2>
<p>بدل مقارنة المتوسطات نقارن الآن النسب، مثل: معدلات تأييد مرشحين، أو معدلات التحويل لتصميمين لموقع إلكتروني، أو معدلات الشفاء لعلاجين، أو نسب المعيب من عمليتي تصنيع. والهدف تقدير مقدار اختلاف نسبتي المجتمعين.</p>

<h2>2. المعلمة المطلوبة</h2>
<p>لتكن \(p_1\) نسبة المجتمع في المجموعة 1، و\(p_2\) نسبته في المجموعة 2. المعلمة المطلوبة هي \(p_1-p_2\)، أي الفرق الحقيقي بين نسبتي المجتمعين، ونقدّرها بـ \(\hat p_1-\hat p_2\) حيث تُحسب كل نسبة من عيّنتها.</p>

<h2>3. تفسير الفرق</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">الفرق</th><th scope="col">التفسير</th></tr></thead>
<tbody>
<tr><td>موجب</td><td>نسبة المجموعة 1 أكبر</td></tr>
<tr><td>سالب</td><td>نسبة المجموعة 2 أكبر</td></tr>
<tr><td>صفر</td><td>لا فرق بين نسبتي المجتمعين</td></tr>
</tbody></table></div>

<h2>4. المخطط والخطأ المعياري</h2>
<p>من جديد: التقدير ± هامش الخطأ، حيث التقدير \(\hat p_1-\hat p_2\)، والهامش مبني على الخطأ المعياري للفرق. وللعيّنات المستقلة:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="الخطأ المعياري للفرق بين نسبتين">\[\widehat{\operatorname{SE}}(\hat p_1-\hat p_2)=\sqrt{\frac{\hat p_1(1-\hat p_1)}{n_1}+\frac{\hat p_2(1-\hat p_2)}{n_2}}\]</div>
<p>وهو يجمع عدم اليقين من النسبتين؛ لأن تباين الفرق بين مقدِّرين مستقلين يساوي مجموع تبايناتهما.</p>

<h2>5. صيغة الفترة (فترة والد)</h2>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="فترة والد للفرق بين نسبتين">\[(\hat p_1-\hat p_2)\pm z_{1-\alpha/2}\sqrt{\frac{\hat p_1(1-\hat p_1)}{n_1}+\frac{\hat p_2(1-\hat p_2)}{n_2}}\]</div>
<p>هذه فترة والد غير المجمّعة المعتادة للعيّنات الكبيرة. وقد تكون تغطيتها ضعيفة، خصوصًا في العيّنات الصغيرة أو النسب القريبة من 0 أو 1، وتكون الطرق المبنية على الدرجة مثل طريقة نيوكومب أفضل غالبًا. ويكون توزيع المعاينة للفرق طبيعيًا تقريبًا مع مجموعات مستقلة وعدد كافٍ من النجاحات والإخفاقات في كل مجموعة، فنستخدم قيم z الحرجة لا قيم t.</p>

    <section class="example-box" id="esa-two-proportion-ci-calculator" data-locale="ar" aria-labelledby="esa-two-proportion-ci-heading">
      <h2 id="esa-two-proportion-ci-heading">مختبر تفاعلي: فترة الثقة للفرق بين نسبتين</h2>
      <p>أدخل أعداد النجاح في مجموعتين مستقلتين لحساب <strong>فترة والد غير المجمّعة للعيّنات الكبيرة</strong> للفرق «المجموعة 1 − المجموعة 2». والقيم الأولية تطابق مثال اختبار A/B أدناه.</p>
      <div class="esa-proportion-fields">
        <label>نجاحات المجموعة 1 <input id="esa-prop-x1" dir="ltr" type="number" min="0" max="10000000" step="1" inputmode="numeric" value="240"></label>
        <label>حجم عيّنة المجموعة 1 <input id="esa-prop-n1" dir="ltr" type="number" min="1" max="10000000" step="1" inputmode="numeric" value="600"></label>
        <label>نجاحات المجموعة 2 <input id="esa-prop-x2" dir="ltr" type="number" min="0" max="10000000" step="1" inputmode="numeric" value="180"></label>
        <label>حجم عيّنة المجموعة 2 <input id="esa-prop-n2" dir="ltr" type="number" min="1" max="10000000" step="1" inputmode="numeric" value="600"></label>
        <label>مستوى الثقة
          <select id="esa-prop-level">
            <option value="90">90%</option>
            <option value="95" selected>95%</option>
            <option value="99">99%</option>
          </select>
        </label>
      </div>
      <p role="alert" id="esa-prop-error" hidden></p>
      <div role="status" aria-live="polite" aria-atomic="true" class="esa-proportion-results">
        <p>الفرق المقدَّر (المجموعة 1 − المجموعة 2) = <output id="esa-prop-difference" dir="ltr">10.0000</output> نقطة مئوية.</p>
        <p>الخطأ المعياري المقدَّر غير المجمّع = <output id="esa-prop-se" dir="ltr">0.027386</output> (بوحدات النسبة)؛
           وهامش الخطأ = <output id="esa-prop-margin" dir="ltr">5.3676</output> نقطة مئوية.</p>
        <p>فترة والد عند <span dir="ltr"><output id="esa-prop-confidence">95</output>%</span> =
           <span dir="ltr">[<output id="esa-prop-lower">4.6324</output>, <output id="esa-prop-upper">15.3676</output>]</span> نقطة مئوية.</p>
      </div>
      <svg id="esa-prop-interval-chart" viewBox="0 0 360 112" width="360" height="112"
           role="img" style="direction:ltr" aria-label="فترة ثقة 95% للفرق: من 4.63 إلى 15.37 نقطة مئوية؛ الصفر خارج الفترة">
        <line x1="24" y1="62" x2="336" y2="62" stroke="currentColor"/>
        <line x1="24" y1="57" x2="24" y2="67" stroke="currentColor"/>
        <line x1="336" y1="57" x2="336" y2="67" stroke="currentColor"/>
        <line id="esa-prop-zero" x1="100" x2="100" y1="20" y2="77" stroke="#64748b" stroke-dasharray="3 3"/>
        <line id="esa-prop-range" x1="140" x2="270" y1="42" y2="42" stroke="#0d9488" stroke-width="5" stroke-linecap="round"/>
        <circle id="esa-prop-point" cx="205" cy="42" r="6" fill="#0d9488"/>
        <text id="esa-prop-axis-low" x="24" y="89" font-size="11" text-anchor="start" fill="currentColor">−5 pp</text>
        <text id="esa-prop-axis-high" x="336" y="89" font-size="11" text-anchor="end" fill="currentColor">20 pp</text>
        <text id="esa-prop-zero-label" x="100" y="103" font-size="11" text-anchor="middle" fill="currentColor">0 pp</text>
      </svg>
      <p id="esa-prop-zero-interpretation">الصفر خارج هذه الفترة؛ فالفترة تستبعد تساوي نسبتي المجتمعين.</p>
      <p id="esa-prop-warning">في كل مجموعة 10 نجاحات و10 إخفاقات على الأقل.</p>
      <p class="muted-mini">تقدّر هذه الحاسبة فرقًا، وليست اختبار Z بالتقدير المجمّع، ولا تثبت السببية. وهي تفترض مشاهدات مستقلة في مجموعتين مستقلتين. وقد تكون تغطية فترة والد ضعيفة حتى عند تحقق قاعدة العد البسيطة؛ فاستخدم طريقة مبنية على الدرجة أو طريقة أكثر موثوقية عند الحاجة.</p>
      <button type="button" class="btn btn-outline" id="esa-prop-reset">استعادة المثال المحلول</button>

      <div class="concept-box" id="esa-prop-newcombe-panel" aria-labelledby="esa-prop-newcombe-title">
        <h3 id="esa-prop-newcombe-title">مقارنة فترة والد بفترة نيوكومب المبنية على درجة ويلسون</h3>
        <p>تجمع طريقة نيوكومب العاشرة حدود ويلسون لكل نسبة ذات حدين مستقلة. وهي أفضل غالبًا قرب 0 أو 1 وفي العيّنات الأصغر، لكن لا طريقة تضمن التغطية الاسمية في كل حالة. وتبقى فترة والد معروضة أعلاه.</p>
        <p id="esa-prop-newcombe-error" role="alert" hidden></p>
        <div id="esa-prop-newcombe-results" role="status" aria-live="polite" aria-atomic="true">
          <p>فترة نيوكومب عند <span dir="ltr"><output id="esa-prop-newcombe-level">95</output>%</span> =
          <span dir="ltr">[<output id="esa-prop-newcombe-lower">—</output>, <output id="esa-prop-newcombe-upper">—</output>]</span> نقطة مئوية.</p>
          <p id="esa-prop-newcombe-zero">جارٍ حساب الفترة المبنية على الدرجة.</p>
        </div>
        <svg id="esa-prop-compare-chart" viewBox="0 0 480 112" role="img" style="direction:ltr" aria-label="مقارنة فترتي والد ونيوكومب للفرق بين نسبتين مستقلتين"></svg>
        
      </div>
      <script defer src="/js/newcombe-two-proportion.js"></script>

    </section>
    <style>
      #esa-two-proportion-ci-calculator{box-sizing:border-box;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-two-proportion-ci-calculator .esa-proportion-fields{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,185px),1fr));gap:12px;margin:14px 0}
      #esa-two-proportion-ci-calculator label{display:flex;flex-direction:column;gap:6px;font-weight:600;min-width:0}
      #esa-two-proportion-ci-calculator input,#esa-two-proportion-ci-calculator select{box-sizing:border-box;width:100%;max-width:100%;padding:8px;font:inherit}
      #esa-two-proportion-ci-calculator svg{display:block;width:100%;height:auto;max-width:550px;margin:12px auto;overflow:visible}
      #esa-two-proportion-ci-calculator p{margin:10px 0}
      #esa-two-proportion-ci-calculator [role="alert"]{font-weight:700}
      @media print{#esa-two-proportion-ci-calculator button,#esa-two-proportion-ci-calculator .esa-proportion-fields{display:none}}
    </style>
    <script>
    (function () {
      "use strict";
      const root=document.getElementById("esa-two-proportion-ci-calculator");
      if(!root)return;
      const el=id=>root.querySelector("#"+id);
      const inputs=["x1","n1","x2","n2"].map(x=>el("esa-prop-"+x));
      const level=el("esa-prop-level");
      const Z={90:1.6448536269514722,95:1.959963984540054,99:2.5758293035489004};
      const outputs=["difference","se","margin","confidence","lower","upper"];
      function clear(message) {
        el("esa-prop-error").hidden=false;
        el("esa-prop-error").textContent=message;
        outputs.forEach(s=>el("esa-prop-"+s).textContent="—");
        el("esa-prop-interval-chart").hidden=true;
        el("esa-prop-zero-interpretation").textContent="أدخل أعدادًا صحيحة لتفسير الفترة.";
        el("esa-prop-warning").textContent="";
      }
      function update() {
        const nums=inputs.map(input=>input.value.trim()===""?NaN:Number(input.value));
        const [x1,n1,x2,n2]=nums;
        if(nums.some(n=>!Number.isSafeInteger(n)||n<0||n>10000000)||
           n1===0||n2===0||x1>n1||x2>n2) {
          clear("استخدم أحجام عيّنات صحيحة موجبة حتى 10,000,000، وأعداد نجاح بين 0 وحجم العيّنة المقابل.");
          return;
        }
        const p1=x1/n1,p2=x2/n2,d=p1-p2;
        const se=Math.sqrt(p1*(1-p1)/n1+p2*(1-p2)/n2);
        const margin=Z[Number(level.value)]*se;
        const lower=d-margin,upper=d+margin;
        el("esa-prop-error").hidden=true;
        el("esa-prop-error").textContent="";
        el("esa-prop-difference").textContent=(100*d).toFixed(4);
        el("esa-prop-se").textContent=se.toFixed(6);
        el("esa-prop-margin").textContent=(100*margin).toFixed(4);
        el("esa-prop-confidence").textContent=level.value;
        el("esa-prop-lower").textContent=(100*lower).toFixed(4);
        el("esa-prop-upper").textContent=(100*upper).toFixed(4);
        const zeroIncluded=lower<=0&&upper>=0;
        el("esa-prop-zero-interpretation").textContent=zeroIncluded?
          "الصفر داخل هذه الفترة؛ فالفترة لا تستبعد تساوي نسبتي المجتمعين عند مستوى الثقة المختار.":
          "الصفر خارج هذه الفترة؛ فالفترة تستبعد تساوي نسبتي المجتمعين عند مستوى الثقة المختار، بشرط افتراضات الطريقة.";
        const small=[x1,n1-x1,x2,n2-x2].some(n=>n<10);
        el("esa-prop-warning").textContent=small?
          "تنبيه: في مجموعة واحدة على الأقل أقل من 10 نجاحات أو أقل من 10 إخفاقات؛ فقد يكون التقريب الطبيعي وتغطية فترة والد غير موثوقين، ففكّر في فترة مبنية على الدرجة مثل فترة نيوكومب.":
          "في كل مجموعة 10 نجاحات و10 إخفاقات على الأقل؛ وهذه قاعدة فرز وليست ضمانًا لتغطية فترة والد.";
        const chart=el("esa-prop-interval-chart");
        chart.hidden=false;
        const pad=Math.max(0.03,margin*0.2);
        const axisMin=Math.min(-0.03,lower-pad),axisMax=Math.max(0.03,upper+pad);
        const sx=x=>24+(x-axisMin)*312/(axisMax-axisMin);
        el("esa-prop-range").setAttribute("x1",sx(lower).toFixed(2));
        el("esa-prop-range").setAttribute("x2",sx(upper).toFixed(2));
        el("esa-prop-point").setAttribute("cx",sx(d).toFixed(2));
        const zeroX=sx(0).toFixed(2);
        ["x1","x2"].forEach(a=>el("esa-prop-zero").setAttribute(a,zeroX));
        el("esa-prop-zero-label").setAttribute("x",zeroX);
        el("esa-prop-axis-low").textContent=(100*axisMin).toFixed(1)+" pp";
        el("esa-prop-axis-high").textContent=(100*axisMax).toFixed(1)+" pp";
        chart.setAttribute("aria-label","فترة والد عند "+level.value+"% للفرق: "+
          (100*lower).toFixed(2)+" إلى "+(100*upper).toFixed(2)+
          " نقطة مئوية؛ الصفر "+(zeroIncluded?"داخلها.":"خارجها."));
      }
      [...inputs,level].forEach(input=>{
        input.addEventListener("input",update);
        input.addEventListener("change",update);
      });
      el("esa-prop-reset").addEventListener("click",()=>{
        [240,600,180,600].forEach((n,i)=>inputs[i].value=String(n));
        level.value="95";update();
      });
      update();
    })();
    </script>

<h2>6. مثال محسوب: اختبار A/B</h2>
<p>لنفترض أن اختبار A/B قارن نسختين من موقع: النسخة A حققت 240 تحويلًا من 600 زائر، والنسخة B حققت 180 تحويلًا من 600 زائر، ومستوى الثقة 95%.</p>
<h3>الخطوة 1: نسبتا العيّنتين</h3>
<div dir="ltr">\[\hat p_1=\frac{240}{600}=0.40,\qquad \hat p_2=\frac{180}{600}=0.30.\]</div>
<h3>الخطوة 2: الفرق المقدَّر</h3>
<div dir="ltr">\[\hat p_1-\hat p_2=0.40-0.30=0.10,\]</div>
<p>أي إن العيّنة تشير إلى أفضلية قدرها 10 نقاط مئوية للنسخة A.</p>
<h3>الخطوة 3: الخطأ المعياري</h3>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="حساب الخطأ المعياري">\[\widehat{\operatorname{SE}}=\sqrt{\frac{0.40(0.60)}{600}+\frac{0.30(0.70)}{600}}=\sqrt{0.00075}\approx0.0273861\]</div>
<h3>الخطوة 4: هامش الخطأ</h3>
<div dir="ltr">\[\operatorname{ME}=z_{0.975}(0.0273861)\approx1.95996(0.0273861)\approx0.053676.\]</div>
<p>(وبالقيمة المقرّبة 1.96 يكون الهامش 0.053677؛ والفرق في المنزلة السادسة فقط.)</p>
<h3>الخطوة 5: بناء الفترة</h3>
<div dir="ltr">\[0.10\pm0.053676\approx(0.046324,\ 0.153676).\]</div>
<p>أي <span dir="ltr">(0.0463, 0.1537)</span>. وفترة نيوكومب للبيانات نفسها <span dir="ltr">(0.0461, 0.1531)</span>، قريبة جدًا هنا لأن العيّنتين كبيرتان والنسبتين بعيدتان عن الحدود.</p>

<h2>7. تفسير الفترة</h2>
<p>تتراوح القيم المعقولة لـ \(p_1-p_2\) بين نحو 4.6 و15.4 نقطة مئوية. وفي ظل شروط العيّنات المستقلة وإجراء والد للعيّنات الكبيرة، تشير البيانات إلى أن معدل التحويل في مجتمع النسخة A يزيد على معدل النسخة B بنحو 4.6 إلى 15.4 نقطة مئوية.</p>

<h2>8. أهمية الصفر</h2>
<div class="concept-box"><strong>الفرق الصفري:</strong><p>فرق قدره صفر يعني أن نسبتي المجتمعين متساويتان.</p></div>
<ul class="bullets"><li>في الفترة <span dir="ltr">(0.046, 0.154)</span> الصفر مستبعد، فتساوي النسبتين ليس من القيم المعقولة، والدليل يشير إلى فرق حقيقي.</li><li>لو كانت الفترة <span dir="ltr">(−0.04, 0.08)</span> لكان الصفر داخلها، فيبقى تساوي النسبتين معقولًا، ولا يوجد دليل قوي على الفرق.</li></ul>

<h2>9. شروط الفترة</h2>
<ul class="bullets"><li>معاينة عشوائية للاستدلال على المجتمع، أو تعيين عشوائي في التجارب (والتعيين وحده لا يضمن تمثيل المجتمع).</li><li>مشاهدات مستقلة داخل كل مجموعة.</li><li>مجموعات مستقلة.</li><li>أحجام عيّنات كبيرة بما يكفي للتقريب الطبيعي.</li></ul>
<div class="concept-box"><strong>شروط النجاح والإخفاق (لكل عيّنة):</strong><p dir="ltr">n₁p̂₁ ≥ 10, n₁(1 − p̂₁) ≥ 10, n₂p̂₂ ≥ 10, n₂(1 − p̂₂) ≥ 10</p></div>
<p>وهذه الشروط تدعم التقريب الطبيعي ولا تضمن التغطية.</p>

<h2>10. أين تُستخدم هذه الفترات؟</h2>
<p>في استطلاعات الانتخابات، واختبارات A/B، والتجارب السريرية، ودراسات التسويق، ومقارنات ضبط الجودة؛ فمقارنة النسب من أكثر المهام شيوعًا في الإحصاء التطبيقي.</p>

<h2>11. الفرق بين متوسطين مقابل الفرق بين نسبتين</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">الخاصية</th><th scope="col">المتوسطات</th><th scope="col">النسب</th></tr></thead>
<tbody>
<tr><td>المعلمة</td><td dir="ltr">μ₁ − μ₂</td><td dir="ltr">p₁ − p₂</td></tr>
<tr><td>المقدِّر</td><td dir="ltr">x̄₁ − x̄₂</td><td dir="ltr">p̂₁ − p̂₂</td></tr>
<tr><td>القيمة الحرجة</td><td>t عادةً</td><td>z</td></tr>
</tbody></table></div>
<div class="concept-box"><strong>الرسالة الأساسية:</strong><p>تقدّر فترات الثقة للفرق بين نسبتين مقدار اختلاف نسبتي المجتمعين مع أخذ عدم اليقين من العيّنتين في الحسبان.</p></div>

<h2>12. ماذا بعد؟</h2>
<p>لا تتضمن كل المقارنات مجموعات مستقلة؛ فدراسات كثيرة تقيس الأشخاص أنفسهم مرتين، كتجارب «قبل وبعد». ويقدّم الدرس التالي فترات الثقة لمتوسط الفروق الزوجية.</p>

<div class="summary-box">
<h2>خلاصة الدرس</h2>
<ul class="bullets">
<li>المعلمة المطلوبة \(p_1-p_2\).</li>
<li>المقدِّر \(\hat p_1-\hat p_2\).</li>
<li>الخطأ المعياري يجمع عدم اليقين من العيّنتين.</li>
<li>تستخدم الفترة قيم z الحرجة.</li>
<li>الصفر يمثّل تساوي نسبتي المجتمعين.</li>
<li>إذا كان الصفر خارج الفترة فالدليل يشير إلى فرق حقيقي.</li>
<li>يجب فحص شروط النجاح والإخفاق في المجموعتين.</li>
<li>فترة نيوكومب أكثر موثوقية من فترة والد في العيّنات الصغيرة أو قرب الحدود.</li>
</ul>
</div>

<div class="lesson-nav">
<a class="btn btn-outline" href="/ar/inference/confidence-intervals/ci-for-difference-of-means-independent/">→ السابق: فترة الثقة للفرق بين متوسطين</a>
<a class="btn" href="/inference/confidence-intervals/ci-for-paired-mean-difference/" hreflang="en" lang="en" dir="ltr">Next: CI for Paired Mean Difference (English) →</a>
</div>
</div></section>
