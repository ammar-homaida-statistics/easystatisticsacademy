/* Easy Statistics Academy Batch #99 — Mann–Whitney U and Wilcoxon signed-rank laboratory.
 *
 * Mann–Whitney (independent samples x, y; SciPy mannwhitneyu conventions):
 *   U1 = R1 - n1 (n1 + 1) / 2, U2 = n1 n2 - U1 (R1 = rank sum of x, average ranks).
 *   Exact (no ties): greater P(U >= U1); less P(U >= U2); two-sided 2 P(U >= max(U1, U2)),
 *   capped at 1, where U has the null distribution counted by dynamic programming.
 *   Normal approximation: mu = n1 n2 / 2,
 *   sigma^2 = n1 n2 / 12 * [(N + 1) - sum (t^3 - t) / (N (N - 1))],
 *   z = (U1 - mu - 0.5 sign) / sigma (continuity correction toward the null).
 *   Rank-biserial r = 2 U1 / (n1 n2) - 1; Hodges–Lehmann shift = median of x_i - y_j.
 *
 * Wilcoxon signed-rank (differences d = x - y; zeros dropped, SciPy "wilcox"):
 *   T+ = sum of ranks of |d| with d > 0, T- likewise, n = number of non-zero d.
 *   Exact (no ties, no zeros): greater P(T+ >= t), less P(T+ <= t),
 *   two-sided 2 min of both, capped at 1.
 *   Normal approximation without continuity correction (SciPy default):
 *   z = (T+ - n (n + 1) / 4) / sqrt([n (n + 1)(2n + 1) - sum (t^3 - t) / 2] / 24).
 *   Matched-pairs rank-biserial r = (T+ - T-) / (T+ + T-).
 */
(function () {
  "use strict";
  function erfcPositive(x){
    if(x<2.5){let sum=x,term=x;const x2=x*x;
      for(let n=1;n<200;n++){term*=-x2/n;const add=term/(2*n+1);sum+=add;if(Math.abs(add)<1e-17*Math.abs(sum))break;}
      return 1-2/Math.sqrt(Math.PI)*sum;}
    const TINY=1e-300;let f=x,C=x,D=0;
    for(let n=1;n<500;n++){const a=n/2;D=x+a*D;if(Math.abs(D)<TINY)D=TINY;C=x+a/C;if(Math.abs(C)<TINY)C=TINY;
      D=1/D;const delta=C*D;f*=delta;if(Math.abs(delta-1)<1e-16)break;}
    return Math.exp(-x*x)/Math.sqrt(Math.PI)/f;
  }
  const upper=z=>z>=0?0.5*erfcPositive(z/Math.SQRT2):1-0.5*erfcPositive(-z/Math.SQRT2);
  const lower=z=>upper(-z);
  function sidesP(z,side){return side==="greater"?upper(z):side==="less"?lower(z):Math.min(1,2*Math.min(upper(z),lower(z)));}
  function rank(values){
    const idx=values.map((v,i)=>i).sort((a,b)=>values[a]-values[b]);
    const r=new Array(values.length);let ties=0,tied=false;
    for(let i=0;i<idx.length;){
      let j=i;while(j+1<idx.length&&values[idx[j+1]]===values[idx[i]])j++;
      const t=j-i+1;if(t>1){ties+=t*t*t-t;tied=true;}
      for(let m=i;m<=j;m++)r[idx[m]]=(i+j)/2+1;i=j+1;
    }
    return {r,ties,tied};
  }
  // Null distribution of U for sizes m, n without ties: counts c[u] of the
  // C(m+n, m) arrangements, built by the standard recurrence on (m, n).
  function mwuCounts(m,n){
    let prev=[];for(let j=0;j<=n;j++)prev.push([1]);   // m = 0: one arrangement, U = 0
    for(let i=1;i<=m;i++){
      const cur=[[1]];                                     // n = 0
      for(let j=1;j<=n;j++){
        const a=prev[j],b=cur[j-1],len=i*j+1,out=new Array(len).fill(0);
        // f(i, j, u) = f(i - 1, j, u - j) + f(i, j - 1, u)
        for(let u=0;u<a.length;u++)out[u+j]+=a[u];
        for(let u=0;u<b.length;u++)out[u]+=b[u];
        cur.push(out);
      }
      prev=cur;
    }
    return prev[n];
  }
  const tail=(counts,k)=>{let s=0,tot=0;for(let u=0;u<counts.length;u++){tot+=counts[u];if(u>=k)s+=counts[u];}return s/tot;};
  function valid(a,min){return Array.isArray(a)&&a.length>=min&&a.length<=50&&a.every(x=>Number.isFinite(x)&&Math.abs(x)<=1e6);}
  const SIDES=["two-sided","greater","less"];
  function mannWhitney(x,y,side){
    if(side===undefined)side="two-sided";
    if(!valid(x,1)||!valid(y,1)||!SIDES.includes(side))return null;
    const n1=x.length,n2=y.length,N=n1+n2,{r,ties,tied}=rank(x.concat(y));
    const R1=r.slice(0,n1).reduce((a,b)=>a+b,0),U1=R1-n1*(n1+1)/2,U2=n1*n2-U1;
    const mu=n1*n2/2,s=Math.sqrt(n1*n2/12*((N+1)-ties/(N*(N-1))));
    let z=NaN,pApprox=NaN;
    if(s>0){const num=U1-mu,sign=side==="greater"?1:side==="less"?-1:Math.sign(num);
      z=(num-0.5*sign)/s;pApprox=sidesP(z,side);}
    let pExact=NaN;
    if(!tied){const c=mwuCounts(n1,n2);
      pExact=side==="greater"?tail(c,U1):side==="less"?tail(c,U2):Math.min(1,2*tail(c,Math.max(U1,U2)));}
    const diffs=[];for(const a of x)for(const b of y)diffs.push(a-b);diffs.sort((a,b)=>a-b);
    const m=diffs.length,hl=m%2?diffs[(m-1)/2]:(diffs[m/2-1]+diffs[m/2])/2;
    return {test:"mann-whitney",side,n1,n2,U1,U2,z,pApprox,pExact,tied,exactAvailable:!tied,
      rankBiserial:2*U1/(n1*n2)-1,hodgesLehmann:hl};
  }
  function wilcoxonCounts(n){
    const max=n*(n+1)/2,c=new Array(max+1).fill(0);c[0]=1;
    for(let k=1;k<=n;k++)for(let t=max;t>=k;t--)c[t]+=c[t-k];
    return c;
  }
  function wilcoxon(x,y,side){
    if(side===undefined)side="two-sided";
    if(!valid(x,1)||!SIDES.includes(side))return null;
    let d;
    if(y===null||y===undefined)d=x.slice();
    else{if(!valid(y,1)||y.length!==x.length)return null;d=x.map((v,i)=>v-y[i]);}
    const zeros=d.filter(v=>v===0).length,nz=d.filter(v=>v!==0),n=nz.length;
    if(n<1)return {test:"wilcoxon",side,n:0,zeros,defined:false,tPlus:0,tMinus:0,z:NaN,pApprox:NaN,pExact:NaN,rankBiserial:NaN,exactAvailable:false};
    const {r,ties,tied}=rank(nz.map(Math.abs));
    let tPlus=0,tMinus=0;nz.forEach((v,i)=>{if(v>0)tPlus+=r[i];else tMinus+=r[i];});
    const mn=n*(n+1)/4,se=Math.sqrt((n*(n+1)*(2*n+1)-ties/2)/24);
    const z=se>0?(tPlus-mn)/se:NaN,pApprox=se>0?sidesP(z,side):NaN;
    const exactAvailable=!tied&&zeros===0;let pExact=NaN;
    if(exactAvailable){const c=wilcoxonCounts(n),tot=Math.pow(2,n);
      let ge=0,le=0;for(let t=0;t<c.length;t++){if(t>=tPlus)ge+=c[t];if(t<=tPlus)le+=c[t];}
      ge/=tot;le/=tot;
      pExact=side==="greater"?ge:side==="less"?le:Math.min(1,2*Math.min(ge,le));}
    return {test:"wilcoxon",side,n,zeros,defined:true,tPlus,tMinus,z,pApprox,pExact,tied,exactAvailable,
      rankBiserial:(tPlus-tMinus)/(tPlus+tMinus)};
  }
  window.esaRankTests={mannWhitney,wilcoxon,mwuCounts,wilcoxonCounts};

  const root=typeof document!=="undefined"&&document.getElementById("esa-rt-lab");
  if(!root)return;
  const AR=root.dataset.locale==="ar";
  const T=AR?{
    error:"أدخل من 1 إلى 50 عددًا في كل عيّنة، مفصولة بفواصل إنجليزية؛ وفي اختبار ويلكوكسون للأزواج يجب أن يتساوى طولا العيّنتين. يجب ألا تتجاوز القيم المطلقة 1,000,000.",
    undef:"غير معرّف",noExactTies:"غير متاح مع القيم المتساوية أو الفروق الصفرية",
    allZero:"جميع الفروق تساوي صفرًا، فلا توجد رتب؛ لذا الاختبار غير معرّف.",
    note:"تُفضَّل القيمة الدقيقة عندما تكون متاحة. مع القيم المتساوية يُستخدم التقريب الطبيعي المصحّح للتساوي."
  }:{
    error:"Enter 1 to 50 numbers per sample, separated by commas; for the paired Wilcoxon test both samples must have the same length. Absolute values must be at most 1,000,000.",
    undef:"Undefined",noExactTies:"Not available with ties or zero differences",
    allZero:"All differences are zero, so there are no ranks and the test is undefined.",
    note:"Prefer the exact p-value when it is available. With ties, the tie-corrected normal approximation is used."
  };
  const get=id=>root.querySelector("#esa-rt-"+id);
  const xEl=get("x"),yEl=get("y"),testEl=get("test"),sideEl=get("side"),error=get("error"),results=get("results");
  const f4=v=>Number.isFinite(v)?v.toFixed(4):T.undef;
  const fp=v=>!Number.isFinite(v)?T.undef:v<1e-6?v.toExponential(3):v.toFixed(6);
  function parse(text){
    const parts=text.split(",").map(t=>t.trim()).filter(t=>t!=="");
    if(!parts.length||parts.some(t=>!/^[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?$/.test(t)))return null;
    return parts.map(Number);
  }
  function update(){
    const x=parse(xEl.value),y=parse(yEl.value),paired=testEl.value==="wilcoxon";
    const r=x&&y?(paired?wilcoxon(x,y,sideEl.value):mannWhitney(x,y,sideEl.value)):null;
    [xEl,yEl].forEach(el=>el.setAttribute("aria-invalid",r?"false":"true"));
    if(!r){error.hidden=false;error.textContent=T.error;results.hidden=true;return;}
    error.hidden=true;error.textContent="";results.hidden=false;
    get("row-mw").hidden=paired;get("row-wx").hidden=!paired;
    if(paired){
      get("n").textContent=String(r.n);get("zeros").textContent=String(r.zeros);
      get("tplus").textContent=String(r.tPlus);get("tminus").textContent=String(r.tMinus);
    }else{
      get("u1").textContent=String(r.U1);get("u2").textContent=String(r.U2);get("hl").textContent=f4(r.hodgesLehmann);
    }
    get("z").textContent=f4(r.z);get("papprox").textContent=fp(r.pApprox);
    get("pexact").textContent=r.exactAvailable?fp(r.pExact):T.noExactTies;
    get("r").textContent=f4(r.rankBiserial);
    get("note").textContent=paired&&!r.defined?T.allZero:T.note;
  }
  const presets={
    mw:["mann-whitney","12.1, 14.3, 11.8, 15.2, 13.9, 12.7","15.8, 16.4, 14.9, 17.2, 18.1"],
    wx:["wilcoxon","142, 151, 138, 160, 147, 156, 149, 163","135, 149, 132, 151, 144, 146, 150, 152"],
    ties:["mann-whitney","3, 4, 4, 5, 6, 6, 7, 8, 9, 9","5, 6, 7, 7, 8, 9, 10, 10, 11, 12"]};
  for(const name of Object.keys(presets))get(name).addEventListener("click",()=>{
    const [t,a,b]=presets[name];testEl.value=t;xEl.value=a;yEl.value=b;sideEl.value="two-sided";update();});
  [xEl,yEl].forEach(el=>el.addEventListener("input",update));
  [testEl,sideEl].forEach(el=>el.addEventListener("change",update));
  update();
})();
