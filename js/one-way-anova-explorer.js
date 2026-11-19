/* Easy Statistics Academy Batch #65 — interactive one-way ANOVA.
 * Dependency-free numerical methods; independent benchmark tests live in CI. */
(function () {
  "use strict";
  const root=document.getElementById("esa-anova-lab");
  // Lanczos logGamma, with the positive arguments used in F-tail calculations.
  const c=[0.99999999999980993,676.5203681218851,-1259.1392167224028,
    771.32342877765313,-176.61502916214059,12.507343278686905,
    -0.13857109526572012,9.984369578019572e-6,1.5056327351493116e-7];
  function logGamma(z) {
    if(!(z>0)||!Number.isFinite(z))return NaN;
    if(z<0.5)return Math.log(Math.PI)-Math.log(Math.sin(Math.PI*z))-logGamma(1-z);
    z-=1;let x=c[0];
    for(let i=1;i<c.length;i++)x+=c[i]/(z+i);
    const t=z+7.5;
    return .5*Math.log(2*Math.PI)+(z+.5)*Math.log(t)-t+Math.log(x);
  }
  function betaCF(a,b,x) {
    const MAX=400,EPS=2e-14,TINY=1e-300;
    let qab=a+b,qap=a+1,qam=a-1,c=1,d=1-qab*x/qap;
    if(Math.abs(d)<TINY)d=TINY;
    d=1/d;let h=d;
    for(let m=1;m<=MAX;m++) {
      const m2=2*m;
      let aa=m*(b-m)*x/((qam+m2)*(a+m2));
      d=1+aa*d;if(Math.abs(d)<TINY)d=TINY;
      c=1+aa/c;if(Math.abs(c)<TINY)c=TINY;
      d=1/d;h*=d*c;
      aa=-(a+m)*(qab+m)*x/((a+m2)*(qap+m2));
      d=1+aa*d;if(Math.abs(d)<TINY)d=TINY;
      c=1+aa/c;if(Math.abs(c)<TINY)c=TINY;
      d=1/d;const delta=d*c;h*=delta;
      if(Math.abs(delta-1)<EPS)break;
    }
    return h;
  }
  function ibeta(x,a,b) {
    if(!Number.isFinite(x)||!Number.isFinite(a)||!Number.isFinite(b)||!(a>0&&b>0)||x<0||x>1)return NaN;
    if(x===0)return 0;
    if(x===1)return 1;
    const bt=Math.exp(logGamma(a+b)-logGamma(a)-logGamma(b)+
      a*Math.log(x)+b*Math.log1p(-x));
    const val=x<(a+1)/(a+b+2)?bt*betaCF(a,b,x)/a:
      1-bt*betaCF(b,a,1-x)/b;
    return Math.max(0,Math.min(1,val));
  }
  function fSurvival(f,d1,d2) {
    if(!(d1>0&&d2>0)||Number.isNaN(f)||f<0)return NaN;
    if(f===Infinity)return 0;
    // The F right tail is I_{d2/(d2+d1*f)}(d2/2,d1/2).
    const x=d2/(d2+d1*f);
    return ibeta(x,d2/2,d1/2);
  }
  function compute(groups) {
    if(!Array.isArray(groups)||groups.length<2||groups.some(
      g=>!Array.isArray(g)||g.length<2||g.length>100||
      g.some(x=>!Number.isFinite(x)||Math.abs(x)>1e6)))return null;
    const count=groups.reduce((n,g)=>n+g.length,0),k=groups.length;
    const sum=groups.reduce((a,g)=>a+g.reduce((b,x)=>b+x,0),0);
    const grand=sum/count;
    const means=groups.map(g=>g.reduce((a,b)=>a+b,0)/g.length);
    let between=0,within=0;
    for(let i=0;i<k;i++){
      between+=groups[i].length*(means[i]-grand)**2;
      for(const x of groups[i])within+=(x-means[i])**2;
    }
    // Sum of squares is nonnegative. Do not impose an absolute tolerance:
    // a legitimate tiny-variance dataset must not be marked deterministic.
    const df1=k-1,df2=count-k,msb=between/df1,msw=within/df2;
    const f=within===0?(between>0?Infinity:NaN):msb/msw;
    const p=Number.isNaN(f)?NaN:fSurvival(f,df1,df2);
    return {count,means,grand,between,within,df1,df2,msb,msw,f,p,
      sizes:groups.map(g=>g.length),groups};
  }
  // Batch #97: Welch's (1951) heteroscedastic one-way ANOVA.
  //   w_i = n_i / s_i^2, W = sum w_i, m = sum w_i xbar_i / W,
  //   A = sum w_i (xbar_i - m)^2 / (k - 1),
  //   L = sum (1 - w_i / W)^2 / (n_i - 1),
  //   F = A / (1 + 2 (k - 2) L / (k^2 - 1)),  df1 = k - 1,  df2 = (k^2 - 1) / (3 L).
  // Undefined when any group has zero sample variance (w_i would be infinite).
  function welch(groups) {
    const base=compute(groups);
    if(!base)return null;
    const k=groups.length,n=base.sizes,means=base.means;
    const vars=groups.map((g,i)=>g.reduce((a,x)=>a+(x-means[i])**2,0)/(n[i]-1));
    if(vars.some(v=>!(v>0)))return {k,df1:k-1,df2:NaN,f:NaN,p:NaN,defined:false};
    const w=vars.map((v,i)=>n[i]/v),W=w.reduce((a,b)=>a+b,0);
    const m=w.reduce((a,wi,i)=>a+wi*means[i],0)/W;
    const A=w.reduce((a,wi,i)=>a+wi*(means[i]-m)**2,0)/(k-1);
    const L=w.reduce((a,wi,i)=>a+(1-wi/W)**2/(n[i]-1),0);
    const f=A/(1+2*(k-2)*L/(k*k-1)),df2=(k*k-1)/(3*L);
    return {k,df1:k-1,df2,f,p:fSurvival(f,k-1,df2),defined:true};
  }
  // Pure calculations are exposed only for independent numerical regression tests.
  window.esaAnovaMath={compute,welch,fSurvival,ibeta};
  if(!root)return;
  // One numerical engine for both languages: only the strings below change.
  const AR=root.dataset.locale==="ar";
  const T=AR?{
    undef:"غير معرّف",chartTitle:"القيم المشاهدة ومتوسطات المجموعات",
    chartDesc:"تمثل الدوائر المشاهدات الفردية، والخطوط الأفقية متوسطات المجموعات. لا تُرسم فترات عدم يقين.",
    group:"المجموعة ",value:"القيمة",aria:"القيم المشاهدة ومتوسطات المجموعات: ",mean:" المتوسط ",
    input:"أدخل من 2 إلى 100 عدد منتهٍ لكل مجموعة، مفصولة بفواصل. يجب ألا تتجاوز القيم المطلقة 1,000,000.",
    invalid:"مجموعات غير صالحة.",
    nan:"جميع المشاهدات متطابقة: كلا متوسطي المربعات يساوي صفرًا؛ لذا F وقيمة p غير معرّفتين.",
    inf:"كل مجموعة ثابتة ومتوسطات المجموعات مختلفة: متوسط المربعات داخل المجموعات يساوي صفرًا؛ F=∞ والاحتمال الحدّي للذيل الأعلى يساوي صفرًا.",
    reject:"عند α=0.05 نرفض تساوي متوسطات المجتمعات إذا تحققت افتراضات ANOVA. ولا يحدد ذلك أي المجموعات تختلف.",
    keep:"عند α=0.05 لا نرفض تساوي متوسطات المجتمعات. وهذا ليس دليلًا على أن جميع المتوسطات متساوية.",
    welchUndef:"غير معرّف: تحتاج كل مجموعة إلى تباين عينة موجب."
  }:{
    undef:"Undefined",chartTitle:"Observed sample values and group means",
    chartDesc:"Circles display individual observations; horizontal bars show group means. No uncertainty interval is drawn.",
    group:"Group ",value:"Value",aria:"Observed values and group means: ",mean:" mean ",
    input:"Enter 2 to 100 finite numbers per group, separated by commas. Absolute values must be at most 1,000,000.",
    invalid:"Invalid groups.",
    nan:"All observations are identical: both mean squares are zero; F and p are undefined.",
    inf:"All groups are constant with different means: within-group mean square is zero; F=∞ and the limiting upper-tail probability is zero.",
    reject:"At α=0.05, reject equality of population means if the ANOVA assumptions hold. This does not identify which groups differ.",
    keep:"At α=0.05, do not reject equality of population means. This is not evidence that all means are identical.",
    welchUndef:"Undefined: every group needs a positive sample variance."
  };
  const get=id=>root.querySelector("#esa-anova-"+id);
  const source=[get("a"),get("b"),get("c")],error=get("error"),results=get("results");
  function parse(text) {
    const parts=text.split(/[,\n;]+/).map(s=>s.trim());
    if(parts.length<2||parts.length>100||parts.some(s=>!s||
      !/^[+-]?(?:\d+\.?\d*|\.\d+)(?:e[+-]?\d+)?$/i.test(s)))return null;
    const numbers=parts.map(Number);
    return numbers.every(x=>Number.isFinite(x)&&Math.abs(x)<=1e6)?numbers:null;
  }
  const svgNS="http://www.w3.org/2000/svg";
  const svg=(name,attrs,text)=>{
    const n=document.createElementNS(svgNS,name);
    for(const [key,value] of Object.entries(attrs||{}))n.setAttribute(key,String(value));
    if(text!==undefined)n.textContent=String(text);
    return n;
  };
  const fmt=n=>Number.isNaN(n)?T.undef:n===Infinity?"∞":n.toFixed(6);
  function draw(groups,stats) {
    const chart=get("chart"),vals=groups.flat();
    let low=Math.min(...vals),high=Math.max(...vals);
    if(low===high){low-=1;high+=1;}
    const pad=(high-low)*.08;low-=pad;high+=pad;
    const Y=x=>180-(x-low)/(high-low)*145;
    chart.replaceChildren(
      svg("title",{},T.chartTitle),
      svg("desc",{},T.chartDesc),
      svg("line",{x1:36,y1:15,x2:36,y2:180,stroke:"currentColor"}),
      svg("line",{x1:36,y1:180,x2:380,y2:180,stroke:"currentColor"})
    );
    groups.forEach((g,i)=>{
      const cx=92+i*115;
      for(let j=0;j<g.length;j++)chart.appendChild(
        svg("circle",{cx:cx+((j%5)-2)*6,cy:Y(g[j]),r:3,fill:"#64748b"}));
      chart.appendChild(svg("line",{x1:cx-22,y1:Y(stats.means[i]),x2:cx+22,y2:Y(stats.means[i]),
        stroke:"#0f766e","stroke-width":3}));
      chart.appendChild(svg("text",{x:cx,y:205,fill:"currentColor","font-size":12,"text-anchor":"middle"},
        T.group+String.fromCharCode(65+i)));
    });
    chart.appendChild(svg("text",{x:38,y:12,fill:"currentColor","font-size":11},T.value));
    chart.setAttribute("aria-label",T.aria+
      stats.means.map((x,i)=>String.fromCharCode(65+i)+T.mean+x.toFixed(4)).join("; "));
  }
  function update(){
    const groups=source.map(x=>parse(x.value));
    if(groups.some(g=>g===null)){
      source.forEach((field,i)=>field.setAttribute("aria-invalid",groups[i]===null?"true":"false"));
      error.hidden=false;error.textContent=T.input;
      results.hidden=true;get("chart").replaceChildren();return;
    }
    const s=compute(groups);
    if(!s){source.forEach(field=>field.setAttribute("aria-invalid","true"));error.hidden=false;error.textContent=T.invalid;results.hidden=true;get("chart").replaceChildren();return;}
    source.forEach(field=>field.setAttribute("aria-invalid","false"));
    error.hidden=true;error.textContent="";results.hidden=false;
    get("groups").replaceChildren(...s.means.map((mean,i)=>{
      const tr=document.createElement("tr");
      for(const v of [String.fromCharCode(65+i),String(s.sizes[i]),fmt(mean),
        fmt(Math.sqrt(s.groups[i].reduce((sum,x)=>sum+(x-mean)**2,0)/(s.sizes[i]-1)))]){
        const td=document.createElement("td");td.textContent=v;tr.appendChild(td);
      }
      return tr;
    }));
    for(const [id,val] of Object.entries({ssb:s.between,ssw:s.within,
      dfb:s.df1,dfw:s.df2,msb:s.msb,msw:s.msw,f:s.f,p:s.p}))get(id).textContent=
      id==="dfb"||id==="dfw"?String(val):fmt(val);
    const wf=get("welch-f");
    if(wf){
      const w=welch(groups);
      if(w.defined){
        wf.textContent=fmt(w.f);get("welch-df").textContent=w.df1+", "+w.df2.toFixed(4);
        get("welch-p").textContent=fmt(w.p);
      }else{
        wf.textContent=T.welchUndef;get("welch-df").textContent="—";get("welch-p").textContent="—";
      }
    }
    get("decision").textContent=Number.isNaN(s.f)?
      T.nan:
      s.f===Infinity?
      T.inf:
      s.p<.05?
      T.reject:
      T.keep;
    draw(groups,s);
  }
  source.forEach(x=>x.addEventListener("input",update));
  const presets={
    reset:["4, 5, 6","5, 6, 7","8, 9, 10"],
    equal:["3, 5, 7","3, 5, 7","3, 5, 7"],
    unequal:["2, 3, 6, 7","3, 4","8, 8, 9, 10, 11"],
    constant:["1, 1, 1","2, 2, 2","3, 3, 3"]
  };
  for(const name of Object.keys(presets))get(name).addEventListener("click",()=>{
    source.forEach((input,i)=>{input.value=presets[name][i]});update();
  });
  update();
})();