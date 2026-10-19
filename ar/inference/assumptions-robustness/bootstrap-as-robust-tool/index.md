---
layout: default
title: بوتستراب أداة لتقدير عدم اليقين
description: شرح أكاديمي لإعادة المعاينة مع الإرجاع وتقدير الخطأ المعياري وفترات الثقة بالمئينات مع مختبر تفاعلي.
permalink: /ar/inference/assumptions-robustness/bootstrap-as-robust-tool/
lang: ar
translation_pair: bootstrap
sidebar: false
---
<section class="hero hero-section"><div class="hero-card">
<p><a href="/inference/assumptions-robustness/bootstrap-as-robust-tool/" lang="en" dir="ltr">English — Bootstrap as a Robust Tool</a></p>
<h1>بوتستراب: إعادة المعاينة لتقدير عدم اليقين</h1>
<p class="lead">تساعد طريقة بوتستراب (Bootstrap) في تقدير عدم اليقين الإحصائي عن طريق إنشاء عينات جديدة من البيانات المرصودة، بدل الاعتماد دائمًا على صيغة نظرية لتوزيع المقدّر.</p>
<p>تُستخدم الطريقة في تقدير الخطأ المعياري وفترات الثقة، ولكن صلاحيتها تعتمد على تصميم العينة وطبيعة البيانات والإحصاء المدروس.</p>
</div></section>
<section class="section section-slim"><div class="container">
<h2>1. الفكرة الأساسية</h2>
<p>لنفترض أن لدينا عينة أصلية مكوّنة من <span dir="ltr">n</span> مشاهدات مستقلة. ننشئ عينة بوتستراب باختيار <span dir="ltr">n</span> مشاهدات من العينة الأصلية <strong>مع الإرجاع</strong>؛ لذلك قد تتكرر بعض القيم وقد تغيب قيم أخرى في العينة المعاد سحبها.</p>
<p>نحسب الإحصاء المطلوب، مثل المتوسط، لكل عينة بوتستراب، ونكرر الإجراء <span dir="ltr">B</span> مرة. يمثّل توزيع القيم الناتجة تقريبًا لتوزيع المعاينة للإحصاء تحت التوزيع التجريبي للبيانات.</p>
<h2>2. خطوات إجراء بوتستراب</h2>
<ol><li>حدد الإحصاء المراد تقدير عدم يقينه، مثل متوسط المجتمع.</li><li>احتفظ بحجم العينة الأصلي عند إعادة السحب.</li><li>اسحب المشاهدات مع الإرجاع، واحسب الإحصاء للعينة الجديدة.</li><li>كرر الخطوة السابقة مرات عديدة للحصول على توزيع بوتستراب.</li><li>استخدم تشتت هذا التوزيع لتقدير الخطأ المعياري أو مئيناته لتكوين فترة ثقة تقريبية.</li></ol>
<h2>3. مثال عددي</h2>
<p>إذا كانت البيانات <span dir="ltr">3, 5, 6, 8, 10, 12</span> فإن المتوسط الأصلي يساوي <span dir="ltr">44/6 = 7.3333</span>. قد تتضمن إحدى عينات بوتستراب القيم <span dir="ltr">3, 3, 6, 8, 10, 12</span>، ويكون متوسطها <span dir="ltr">42/6 = 7</span>. هذه عينة ممكنة واحدة وليست نتيجة حتمية.</p>
<h2>4. الخطأ المعياري</h2>
<p>إذا رمزنا لمتوسط العينة المعاد سحبها في التكرار <span dir="ltr">b</span> بالرمز <span dir="ltr">θ*b</span>، فإن الخطأ المعياري المقدر هو الانحراف المعياري للعناصر <span dir="ltr">θ*1, …, θ*B</span> باستخدام المقام <span dir="ltr">B−1</span>. يقيس هذا التشتت التقريبي للمقدّر بسبب المعاينة.</p>
<h2>5. فترة الثقة بالمئينات</h2>
<p>يمكن استخدام المئينين <span dir="ltr">2.5%</span> و<span dir="ltr">97.5%</span> لتكوين فترة بوتستراب بالمئينات بمستوى اسمي <span dir="ltr">95%</span>. هذه الفترة تقريبية، وقد يكون أداؤها ضعيفًا مع العينات الصغيرة أو الإحصاءات المنحازة أو التوزيعات غير المنتظمة. توجد بدائل أكثر تقدمًا مثل فترات <span dir="ltr">BCa</span> عندما تستدعي الحاجة.</p>
<h2>6. متى تكون الطريقة مناسبة؟</h2>
<p>تكون إعادة المعاينة العادية مناسبة غالبًا للبيانات المستقلة والممثلة للمجتمع، عندما يكون الإحصاء مستقرًا بما يكفي. أما السلاسل الزمنية والبيانات العنقودية والمشاهدات المترابطة فتحتاج عادةً إلى تصميم إعادة معاينة يحافظ على بنية الاعتماد.</p>
<p>لا يمكن لبوتستراب إصلاح التحيز الناجم عن اختيار عينة غير ممثلة، ولا تصحيح أخطاء القياس أو فقدان المعلومات أو سوء تعريف المجتمع المستهدف.</p>
<h2>7. تفسير النتائج</h2>
<p>تصف فترة الثقة إجراءً إحصائيًا ذا خصائص تغطية متكررة تحت افتراضات معينة؛ ولا تعني أن احتمال وجود المعلمة الثابتة داخل الفترة المحسوبة يساوي بالضرورة 95%. كما ينبغي التمييز بين عدم اليقين في المتوسط وبين تشتت المشاهدات الفردية.</p>
</div></section>

<!-- مختبر إعادة المعاينة التفاعلي -->
<section class="section section-slim" aria-labelledby="esa-bootstrap-title">
  <div class="container">
    <div class="card" id="esa-bootstrap-lab" style="min-width:0;overflow-wrap:anywhere">
      <h2 id="esa-bootstrap-title">مختبر بوتستراب التفاعلي</h2>
      <p>أدخل المشاهدات المستقلة، واختر بذرة عشوائية وعدد مرات إعادة المعاينة. تتكون كل عينة بوتستراب من سحوبات مع الإرجاع من المشاهدات الأصلية. فترة المئينات توضيحية وليست ضمانًا لتغطية مقدارها 95%.</p>
      <div style="display:flex;flex-wrap:wrap;gap:1rem;align-items:end">
        <label style="flex:2 1 220px">القيم المرصودة (افصل بفاصلة أو مسافة)<textarea id="esa-boot-data" rows="2" style="width:100%">3, 5, 6, 8, 10, 12</textarea></label>
        <label>البذرة العشوائية <input id="esa-boot-seed" type="number" value="42" min="0" max="4294967295" step="1" style="max-width:130px"></label>
        <label>عدد العينات <select id="esa-boot-reps"><option>200</option><option selected>1000</option><option>3000</option></select></label>
        <button type="button" class="btn" id="esa-boot-run">إعادة المعاينة</button>
      </div>
      <p id="esa-boot-status" role="status" aria-live="polite"></p>
      <div id="esa-boot-stats" aria-live="polite"></div>
      <svg id="esa-boot-plot" role="img" aria-label="مدرج تكراري لمتوسطات عينات بوتستراب" viewBox="0 0 640 240" style="width:100%;max-width:640px;display:block;overflow:visible"></svg>
      <p><small>الخطأ المعياري لبوتستراب هو الانحراف المعياري لمتوسطات العينات باستخدام المقام B−1. تُحسب نهايتا الفترة بالمئينين 2.5% و97.5% مع استيفاء خطي. تفترض هذه الطريقة استقلال المشاهدات وتمثيلها للمجتمع، ولا تعالج انحياز الاختيار أو الارتباط. إذا تساوت المشاهدات جميعها فالتباين المقدّر يساوي صفرًا.</small></p>
    </div>
  </div>
</section>
<script>
(function(){
"use strict";
const root=document.getElementById("esa-bootstrap-lab");if(!root)return;
const get=id=>document.getElementById(id),data=get("esa-boot-data"),seed=get("esa-boot-seed"),reps=get("esa-boot-reps"),status=get("esa-boot-status"),stats=get("esa-boot-stats"),svg=get("esa-boot-plot");
const ns="http://www.w3.org/2000/svg";
function node(tag,attrs,text){const e=document.createElementNS(ns,tag);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,String(v)));if(text!==undefined)e.textContent=text;svg.appendChild(e);return e;}
function rng(s){let x=s>>>0;return ()=>{x=(x+0x6D2B79F5)>>>0;let t=Math.imul(x^(x>>>15),1|x);t^=t+Math.imul(t^(t>>>7),61|t);return ((t^(t>>>14))>>>0)/4294967296;};}
function percentile(a,p){const i=(a.length-1)*p,l=Math.floor(i),h=Math.ceil(i);return a[l]+(a[h]-a[l])*(i-l);}
function draw(a){while(svg.firstChild)svg.removeChild(svg.firstChild);const lo=a[0],hi=a[a.length-1],width=hi-lo||1,counts=Array(20).fill(0);a.forEach(v=>counts[Math.min(19,Math.floor((v-lo)/width*20))]++);const top=Math.max(...counts,1);node("line",{x1:42,y1:202,x2:622,y2:202,stroke:"currentColor"});counts.forEach((n,i)=>node("rect",{x:45+i*28.5,y:200-175*n/top,width:26,height:175*n/top,fill:"#2563eb"}));node("text",{x:45,y:225,fill:"currentColor","font-size":12},lo.toFixed(2));node("text",{x:570,y:225,fill:"currentColor","font-size":12},hi.toFixed(2));}
function run(){try{const raw=data.value.trim().split(/[\s,;]+/).filter(Boolean);if(raw.length<2||raw.length>200||raw.some(x=>!Number.isFinite(Number(x))))throw Error("أدخل من 2 إلى 200 قيمة عددية منتهية.");const a=raw.map(Number);if(a.some(x=>Math.abs(x)>1e9))throw Error("استخدم قيمًا لا تتجاوز قيمتها المطلقة مليارًا.");const sd=Number(seed.value);if(!Number.isInteger(sd)||sd<0||sd>4294967295)throw Error("يجب أن تكون البذرة عددًا صحيحًا بين 0 و4294967295.");const B=Number(reps.value);if(![200,1000,3000].includes(B))throw Error("اختر عددًا صالحًا من عينات إعادة المعاينة.");const next=rng(sd),n=a.length,mean=a.reduce((s,x)=>s+x,0)/n,out=[];for(let b=0;b<B;b++){let total=0;for(let i=0;i<n;i++)total+=a[Math.floor(next()*n)];out.push(total/n);}const avg=out.reduce((s,x)=>s+x,0)/B;const se=Math.sqrt(out.reduce((s,x)=>s+(x-avg)**2,0)/(B-1));out.sort((x,y)=>x-y);const ci=[percentile(out,.025),percentile(out,.975)];stats.textContent="متوسط العينة: "+mean.toFixed(4)+" · الخطأ المعياري لبوتستراب: "+se.toFixed(4)+" · فترة المئينات 95%: ["+ci[0].toFixed(4)+", "+ci[1].toFixed(4)+"] · B="+B;status.textContent="اكتملت إعادة المعاينة بنتائج قابلة لإعادة الإنتاج.";draw(out);}catch(e){status.textContent=e.message;stats.textContent="";while(svg.firstChild)svg.removeChild(svg.firstChild);}}
get("esa-boot-run").addEventListener("click",run);run();
})();
</script>
<section class="section section-slim"><div class="container">
<h2>خلاصة الدرس</h2>
<ul><li>تعتمد بوتستراب على إعادة السحب مع الإرجاع من العينة الأصلية.</li><li>يُستخدم توزيع الإحصاء عبر العينات المعاد سحبها لتقدير الخطأ المعياري وفترات الثقة.</li><li>تساعد البذرة العشوائية الثابتة على تكرار المحاكاة والتحقق منها.</li><li>الاستقلال والتمثيل الجيد للعينة مهمان، ولا تعالج الطريقة التحيز الناتج عن سوء المعاينة.</li><li>يجب تفسير فترات المئينات بحذر، خاصة في العينات الصغيرة.</li></ul>
<p><a href="/inference/assumptions-robustness/bootstrap-as-robust-tool/" lang="en" dir="ltr">Return to the English lesson</a> · <a href="/ar/">الصفحة العربية</a></p>
</div></section>