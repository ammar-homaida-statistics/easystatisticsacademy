---
layout: default
title: فترات الثقة واختبارات الفرضيات
description: "شرح عربي للعلاقة بين فترات الثقة واختبارات الفرضيات: قاعدة القرار، وتطابق مستوى الثقة مع α، والفرق بين المعالم والصفر، مع مختبر تفاعلي يبيّن أن الفترة والاختبار يعطيان القرار نفسه."
permalink: /ar/inference/hypothesis-testing/ci-and-test-connection/
lang: ar
sidebar: false
math: true
learning_resource: true
translation_pair: ci-and-test-connection
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاستدلال</span><span class="badge">اختبار الفرضيات</span><span class="badge">الصورة الكبرى</span></div>
<h1>فترات الثقة واختبارات الفرضيات</h1>
{% include lab-noscript.html %}
<p class="lead">تُدرَّس فترات الثقة واختبارات الفرضيات غالبًا أداتين إحصائيتين منفصلتين.</p>
<p class="lead">لكنهما في الواقع مترابطتان بشدة، وتقدّمان كثيرًا الاستنتاج الاستدلالي نفسه من زاويتين مختلفتين.</p>
<p><a href="/inference/hypothesis-testing/ci-and-test-connection/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/hypothesis-testing/one-sided-vs-two-sided/">الدرس السابق: الاختبارات أحادية الطرف وثنائية الطرف</a></p>
</div></section>
<section><div class="content-narrow">

<h2>1. أداتان وهدف واحد</h2>
<p>تستخدم فترات الثقة واختبارات الفرضيات بيانات العيّنة لإصدار عبارات حول معالم المجتمع، وتعتمدان معًا على توزيعات المعاينة والأخطاء المعيارية والنماذج الاحتمالية وافتراضات المعاينة العشوائية. لكن هدفيهما مختلفان قليلًا:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">الطريقة</th><th scope="col">السؤال الرئيس</th></tr></thead>
<tbody>
<tr><td>فترة الثقة</td><td>ما قيم المعلمة المعقولة؟</td></tr>
<tr><td>اختبار الفرضية</td><td>هل ادعاء محدد معقول؟</td></tr>
</tbody></table></div>

<h2>2. الفكرة المحورية</h2>
<div class="concept-box"><strong>العلاقة الأساسية:</strong><p>تضم فترة الثقة جميع قيم المعلمة التي لا يرفضها الاختبار المقابل لها.</p></div>
<p>وهذه من أهم الصلات في الاستدلال الإحصائي.</p>

<h2>3. فكرة قيمة العدم</h2>
<p>لنفترض أننا نختبر:</p>
<div dir="ltr">\[H_0:\theta=\theta_0\qquad\text{vs}\qquad H_a:\theta\neq\theta_0.\]</div>
<p>تُسمّى \(\theta_0\) قيمة العدم، وتساعد فترة الثقة على تحديد ما إذا كانت هذه القيمة ما تزال معقولة.</p>

<h2>4. قاعدة القرار</h2>
<div class="concept-box"><strong>قاعدة مكافئة:</strong><p>إذا وقعت قيمة العدم خارج فترة الثقة نرفض <span dir="ltr">H₀</span>؛ وإذا وقعت داخلها لا نرفض <span dir="ltr">H₀</span>.</p></div>
<p>وتصح هذه القاعدة تمامًا عندما تُبنى الفترة بقلب الاختبار نفسه، كما في فترتي z وt للمتوسط. أما إذا استُخدم خطأ معياري مختلف في الفترة وفي الاختبار (مثل فترة والد لنسبة مع اختبار يستخدم \(p_0\) في الخطأ المعياري)، فقد يختلف القراران قرب الحدود.</p>

<h2>5. مثال 1: رفض الفرضية الصفرية</h2>
<p>لنفترض أن فترة ثقة 95% لمتوسط مجتمع هي <span dir="ltr">(102, 108)</span>، وأننا نختبر \(H_0:\mu=100\). بما أن 100 تقع خارج الفترة، نرفض الفرضية الصفرية عند \(\alpha=0.05\).</p>

<h2>6. مثال 2: عدم الرفض</h2>
<p>لو كانت الفترة <span dir="ltr">(96, 108)</span> فإن 100 تقع داخلها، فلا نرفض \(H_0:\mu=100\).</p>

<h2>7. لماذا يحدث ذلك؟</h2>
<p>تُبنى فترات الثقة من المكوّنات نفسها التي تُبنى منها الاختبارات: التقدير، والخطأ المعياري، والقيم الحرجة، وتوزيعات المعاينة. فالرياضيات وراء الإجراءين متطابقة تقريبًا.</p>

<h2>8. الصلة بين مستوى الثقة ومستوى الدلالة</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">فترة الثقة (ثنائية الطرف)</th><th scope="col">مستوى الاختبار ثنائي الطرف المكافئ</th></tr></thead>
<tbody dir="ltr">
<tr><td>90%</td><td>α = 0.10</td></tr>
<tr><td>95%</td><td>α = 0.05</td></tr>
<tr><td>99%</td><td>α = 0.01</td></tr>
</tbody></table></div>
<p>أما الاختبار أحادي الطرف عند مستوى \(\alpha\) فيقابله حدّ ثقة أحادي بمستوى \(1-\alpha\)، كما يوضح المختبر أدناه.</p>

<h2>9. فترات الثقة تقدّم معلومات أكثر</h2>
<p>ينتهي الاختبار عادةً إلى قرار واحد: رفض <span dir="ltr">H₀</span> أو عدم رفضها. أما فترة الثقة فتعرض حجم الأثر المقدَّر، والدقة، وعدم اليقين، والقيم المعقولة للمعلمة؛ ولهذا يفضّل كثير من الباحثين عرض فترات الثقة إلى جانب الاختبارات.</p>

<h2>10. معالم الفرق والصفر</h2>
<p>في تطبيقات كثيرة تكون الفرضية الصفرية \(H_0:\Delta=0\)، لأن الصفر يمثّل غياب أثر المعالجة، أو غياب الفرق بين المتوسطات، أو غياب التغيّر أو الارتباط.</p>
<ul class="bullets"><li>إذا كانت فترة أثر المعالجة <span dir="ltr">(2.1, 7.5)</span> فإن الصفر خارجها، فيرفض الاختبار المقابل \(H_0:\Delta=0\).</li><li>إذا كانت الفترة <span dir="ltr">(−1.2, 5.4)</span> فإن الصفر داخلها، فلا يرفض الاختبار الفرضية الصفرية.</li></ul>

<!-- مختبر العلاقة بين فترة الثقة والاختبار (Batch #102، النسخة العربية) -->
<section class="concept-box" id="esa-cid-lab" data-locale="ar" aria-labelledby="esa-cid-heading">
  <h3 id="esa-cid-heading">مختبر تفاعلي: الفترة والاختبار يعطيان القرار نفسه</h3>
  <p>لمتوسط واحد بخطأ معياري \(\mathrm{SE}=s/\sqrt n\) (أو \(\sigma/\sqrt n\) في نسخة z)، يرفض اختبار \(H_0:\mu=\mu_0\) تمامًا عندما تقع \(\mu_0\) خارج الفترة المقابلة:</p>
  <div class="esa-cid-math" dir="ltr" tabindex="0" role="region" aria-label="التكافؤ بين الفترة ثنائية الطرف والاختبار ثنائي الطرف">
  \[
  \left|\frac{\bar x-\mu_0}{\mathrm{SE}}\right|>c_{1-\alpha/2}
  \iff
  \mu_0\notin\left[\bar x-c_{1-\alpha/2}\,\mathrm{SE},\ \bar x+c_{1-\alpha/2}\,\mathrm{SE}\right].
  \]
  </div>
  <p>ويقابل الاختبار أحادي الطرف حدًّا أحاديًا: اختبار الطرف الأيمن (\(H_a:\mu&gt;\mu_0\)) يقابله الحد الأدنى \(\bar x-c_{1-\alpha}\,\mathrm{SE}\)، واختبار الطرف الأيسر يقابله الحد الأعلى \(\bar x+c_{1-\alpha}\,\mathrm{SE}\).</p>
  <div class="esa-cid-grid">
    <label for="esa-cid-method">التوزيع المرجعي<select id="esa-cid-method"><option value="t" selected>t (σ مجهول، نستخدم s)</option><option value="z">z (σ معلوم)</option></select></label>
    <label for="esa-cid-side">الفرضية البديلة<select id="esa-cid-side"><option value="two-sided" selected>ثنائية الطرف (μ ≠ μ₀) ↔ فترة ثنائية</option><option value="greater">طرف أيمن (μ &gt; μ₀) ↔ حد أدنى</option><option value="less">طرف أيسر (μ &lt; μ₀) ↔ حد أعلى</option></select></label>
    <label for="esa-cid-mean">متوسط العيّنة x̄<input id="esa-cid-mean" type="number" step="any" inputmode="decimal" value="104.2" dir="ltr" aria-describedby="esa-cid-error"></label>
    <label for="esa-cid-sd">الانحراف المعياري (s، أو σ في z)<input id="esa-cid-sd" type="number" step="any" min="0" inputmode="decimal" value="8.5" dir="ltr" aria-describedby="esa-cid-error"></label>
    <label for="esa-cid-n">حجم العيّنة n<input id="esa-cid-n" type="number" step="1" min="2" inputmode="numeric" value="25" dir="ltr" aria-describedby="esa-cid-error"></label>
    <label for="esa-cid-mu0">قيمة العدم μ₀<input id="esa-cid-mu0" type="number" step="any" inputmode="decimal" value="100" dir="ltr" aria-describedby="esa-cid-error"></label>
    <label for="esa-cid-alpha">مستوى الدلالة α<input id="esa-cid-alpha" type="number" step="any" min="0.001" max="0.5" inputmode="decimal" value="0.05" dir="ltr" aria-describedby="esa-cid-error"></label>
  </div>
  <div class="esa-cid-controls"><button class="btn btn-outline" type="button" id="esa-cid-example">μ₀ خارج الفترة</button><button class="btn btn-outline" type="button" id="esa-cid-inside-ex">μ₀ داخل الفترة</button><button class="btn btn-outline" type="button" id="esa-cid-boundary">ضع μ₀ على حدّ الفترة</button></div>
  <p id="esa-cid-error" role="alert" hidden></p>
  <section id="esa-cid-results" aria-label="نتائج الفترة والاختبار" role="status" aria-live="polite" aria-atomic="true">
    <div class="table-wrap"><table><caption>الفترة والاختبار للبيانات نفسها</caption><tbody>
      <tr><th scope="row">القيمة الحرجة</th><td><output id="esa-cid-crit" dir="ltr">t(24) = 2.0639</output></td></tr>
      <tr><th scope="row">فترة الثقة أو الحد</th><td><output id="esa-cid-ci" dir="ltr">95%: [100.6914, 107.7086]</output></td></tr>
      <tr><th scope="row">هل μ₀ داخل الفترة؟</th><td><output id="esa-cid-inside">لا — μ₀ خارج الفترة</output></td></tr>
      <tr><th scope="row">إحصائية الاختبار</th><td><output id="esa-cid-stat" dir="ltr">t = 2.4706</output></td></tr>
      <tr><th scope="row">القيمة الاحتمالية</th><td><output id="esa-cid-p" dir="ltr">0.020981</output></td></tr>
      <tr><th scope="row">القرار</th><td><output id="esa-cid-decision">نرفض H₀ عند α = 0.05 (p &lt; α)</output></td></tr>
    </tbody></table></div>
    <p id="esa-cid-agree">الفترة والاختبار متفقان.</p>
  </section>
  <p class="muted-mini">بزر «ضع μ₀ على حدّ الفترة» تقع μ₀ تمامًا على طرف الفترة، فتساوي إحصائية الاختبار القيمة الحرجة وتكون <span dir="ltr">p = α</span>. يعامل المختبر الفترة على أنها مغلقة، ولا يرفض إلا إذا كانت <span dir="ltr">p &lt; α</span>، بما يطابق الجدول أدناه؛ وتستخدم بعض المراجع <span dir="ltr">p ≤ α</span> مع فترة مفتوحة. ولا يختلف الاصطلاحان إلا على هذا الحد، واحتماله صفر في البيانات المتصلة. تفترض نسخة z أن σ معلوم، وتفترض نسخة t بيانات طبيعية تقريبًا أو عيّنة كبيرة بما يكفي.</p>
</section>
<style>
#esa-cid-lab,#esa-cid-lab *{box-sizing:border-box}
#esa-cid-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-cid-lab label{display:block;font-weight:650;margin:6px 0}
#esa-cid-lab :is(input,select){display:block;width:100%;min-width:0;font:inherit;padding:8px;margin-top:4px;border:1px solid #777;border-radius:6px}
#esa-cid-lab .esa-cid-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));gap:4px 10px}
#esa-cid-lab .esa-cid-controls{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
#esa-cid-lab .table-wrap,.esa-cid-math{max-width:100%;overflow-x:auto}
.esa-cid-math{direction:ltr}
#esa-cid-lab [hidden]{display:none!important}
#esa-cid-lab :is(input,select,button):focus-visible,.esa-cid-math:focus-visible{outline:2px solid #0f766e;outline-offset:3px}
</style>
<script defer src="/js/ci-test-duality-lab.js"></script>

<h2>11. العلاقة بالقيم الاحتمالية</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">نتيجة فترة الثقة</th><th scope="col">نتيجة القيمة الاحتمالية</th></tr></thead>
<tbody>
<tr><td>قيمة العدم خارج الفترة</td><td dir="ltr">p &lt; α</td></tr>
<tr><td>قيمة العدم داخل الفترة</td><td dir="ltr">p ≥ α</td></tr>
</tbody></table></div>

<h2>12. لماذا يعرض الباحثون الاثنين؟</h2>
<p>يتكامل الأسلوبان: يجيب الاختبار عن سؤال «هل يوجد دليل؟»، وتجيب الفترة عن سؤال «ما حجم الأثر؟». ومعًا يقدّمان فهمًا أغنى للنتائج.</p>

<h2>13. حدود التركيز على الدلالة وحدها</h2>
<p>قد تقابل النتيجة الدالة إحصائيًا أثرًا صغيرًا جدًا، وتساعد فترات الثقة على كشف ما إذا كان الأثر مهمًا علميًا أو عمليًا. وهذا يقودنا طبيعيًا إلى فكرة الأهمية العملية.</p>

<h2>14. الصورة الأشمل</h2>
<p>ليست فترات الثقة واختبارات الفرضيات طريقتين متنافستين، بل منظوران لإطار استدلالي واحد، وفهم الصلة بينهما يوحّد كثيرًا من أفكار الاستدلال الإحصائي.</p>
<div class="concept-box"><strong>الرسالة الأساسية:</strong><p>تضم فترة الثقة قيم المعلمة التي تبقى معقولة في ضوء البيانات. فإذا وقعت قيمة الفرضية الصفرية خارج الفترة، فإن الاختبار المقابل يرفضها عند مستوى الدلالة المطابق.</p></div>

<h2>15. ماذا بعد؟</h2>
<p>تخبرنا الدلالة الإحصائية بما إذا كان الأثر قابلًا للكشف، لكنها لا تخبرنا بأهميته. ويقدّم الدرس التالي مفهوم الأهمية العملية ويشرح لماذا لا تكون النتائج الدالة إحصائيًا ذات معنى دائمًا في التطبيقات الواقعية.</p>

<div class="summary-box">
<h2>خلاصة الدرس</h2>
<ul class="bullets">
<li>فترات الثقة واختبارات الفرضيات مترابطة بشدة.</li>
<li>تضم فترة الثقة القيم التي لا يرفضها الاختبار المقابل.</li>
<li>وقوع قيمة العدم خارج الفترة يعني رفض <span dir="ltr">H₀</span>.</li>
<li>وقوعها داخل الفترة يعني عدم رفض <span dir="ltr">H₀</span>.</li>
<li>فترة ثقة 95% تقابل اختبارًا ثنائي الطرف عند <span dir="ltr">α = 0.05</span>.</li>
<li>تقدّم فترات الثقة معلومات أكثر من مجرد قرار الرفض أو عدمه.</li>
<li>تتسق القيم الاحتمالية وفترات الثقة عمومًا عندما تُبنى بالطريقة نفسها.</li>
<li>تساعد فترات الثقة على تقييم الأهمية الإحصائية والعملية معًا.</li>
</ul>
</div>

<div class="lesson-nav">
<a class="btn btn-outline" href="/ar/inference/hypothesis-testing/one-sided-vs-two-sided/">→ السابق: الاختبارات أحادية الطرف وثنائية الطرف</a>
<a class="btn" href="/ar/inference/hypothesis-testing/practical-significance/">التالي: الأهمية العملية ←</a>
</div>
</div></section>
