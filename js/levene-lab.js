/* Easy Statistics Academy Batch #100 — Levene and Brown–Forsythe laboratory.
 *
 * For group i with centre c_i (mean for Levene, median for Brown–Forsythe),
 *   z_ij = |x_ij - c_i|,
 *   W = (N - k) / (k - 1) * sum_i n_i (zbar_i - zbar)^2 / sum_i sum_j (z_ij - zbar_i)^2,
 *   p = P(F_{k-1, N-k} >= W)  (SciPy scipy.stats.levene conventions).
 * W is undefined when every z_ij equals its group mean (zero denominator).
 */
(function () {
  "use strict";
  function logGamma(z){
    const c=[0.99999999999980993,676.5203681218851,-1259.1392167224028,771.32342877765313,
      -176.61502916214059,12.507343278686905,-0.13857109526572012,9.984369578019572e-6,1.5056327351493116e-7];
    if(z<.5)return Math.log(Math.PI/Math.abs(Math.sin(Math.PI*z)))-logGamma(1-z);
    z-=1;let a=c[0];for(let i=1;i<9;i++)a+=c[i]/(z+i);const t=z+7.5;
    return .5*Math.log(2*Math.PI)+(z+.5)*Math.log(t)-t+Math.log(a);
  }
  // Regularized incomplete beta I_x(a, b) by Lentz's continued fraction.
  function betacf(a,b,x){
    const TINY=1e-300;let c=1,d=1-(a+b)*x/(a+1);if(Math.abs(d)<TINY)d=TINY;d=1/d;let h=d;
    for(let m=1;m<=3000;m++){
      const m2=2*m;let aa=m*(b-m)*x/((a+m2-1)*(a+m2));
      d=1+aa*d;if(Math.abs(d)<TINY)d=TINY;c=1+aa/c;if(Math.abs(c)<TINY)c=TINY;d=1/d;h*=d*c;
      aa=-(a+m)*(a+b+m)*x/((a+m2)*(a+m2+1));
      d=1+aa*d;if(Math.abs(d)<TINY)d=TINY;c=1+aa/c;if(Math.abs(c)<TINY)c=TINY;d=1/d;const del=d*c;h*=del;
      if(Math.abs(del-1)<1e-15)break;
    }
    return h;
  }
  function ibeta(x,a,b){
    if(x<=0)return 0;if(x>=1)return 1;
    const lb=logGamma(a+b)-logGamma(a)-logGamma(b)+a*Math.log(x)+b*Math.log(1-x);
    return x<(a+1)/(a+b+2)?Math.exp(lb)*betacf(a,b,x)/a:1-Math.exp(lb)*betacf(b,a,1-x)/b;
  }
  // Upper tail of F(d1, d2): P(F >= f) = I_{d2/(d2 + d1 f)}(d2/2, d1/2).
  function fSurvival(f,d1,d2){
    if(!(f>=0))return NaN;if(f===0)return 1;if(f===Infinity)return 0;
    return ibeta(d2/(d2+d1*f),d2/2,d1/2);
  }
  const median=a=>{const s=a.slice().sort((x,y)=>x-y),n=s.length;return n%2?s[(n-1)/2]:(s[n/2-1]+s[n/2])/2;};
  const mean=a=>a.reduce((s,v)=>s+v,0)/a.length;
  function compute(groups,center){
    if(center===undefined)center="median";
    if(center!=="mean"&&center!=="median")return null;
    if(!Array.isArray(groups)||groups.length<2||groups.length>6||groups.some(
      g=>!Array.isArray(g)||g.length<2||g.length>100||g.some(x=>!Number.isFinite(x)||Math.abs(x)>1e6)))return null;
    const k=groups.length,n=groups.map(g=>g.length),N=n.reduce((a,b)=>a+b,0);
    const z=groups.map(g=>{const c=center==="mean"?mean(g):median(g);return g.map(x=>Math.abs(x-c));});
    const zbar=z.map(mean),zall=z.flat().reduce((a,b)=>a+b,0)/N;
    const between=zbar.reduce((s,m,i)=>s+n[i]*(m-zall)**2,0);
    const within=z.reduce((s,g,i)=>s+g.reduce((t,v)=>t+(v-zbar[i])**2,0),0);
    const sds=groups.map(g=>{const m=mean(g);return Math.sqrt(g.reduce((s,v)=>s+(v-m)**2,0)/(g.length-1));});
    const pos=sds.filter(s=>s>0),ratio=pos.length===sds.length?Math.max(...sds)**2/Math.min(...sds)**2:Infinity;
    const df1=k-1,df2=N-k;
    // Relative tolerance: a within-group sum that is only rounding noise counts as zero.
    const scale=Math.max(1,...z.flat().map(v=>v*v));
    if(!(within>1e-12*scale*N))return {k,N,n,df1,df2,center,sds,varianceRatio:ratio,W:NaN,p:NaN,defined:false};
    const W=(df2/df1)*between/within;
    return {k,N,n,df1,df2,center,sds,varianceRatio:ratio,W,p:fSurvival(W,df1,df2),defined:true};
  }
  window.esaLevene={compute,fSurvival};

  const root=typeof document!=="undefined"&&document.getElementById("esa-lv-lab");
  if(!root)return;
  const AR=root.dataset.locale==="ar";
  const T=AR?{
    error:"أدخل من 2 إلى 6 مجموعات، كل مجموعة في سطر، ومن 2 إلى 100 عدد في كل سطر مفصولة بفواصل إنجليزية. يجب ألا تتجاوز القيم المطلقة 1,000,000.",
    undef:"غير معرّف",inf:"∞ (تباين صفري في مجموعة)",
    undefined:"الانحرافات المطلقة متساوية داخل كل مجموعة، فمقام W يساوي صفرًا؛ لذا الاختبار غير معرّف.",
    reject:"عند α = 0.05 توجد أدلة على اختلاف التباينات. فكّر في طرق لا تفترض تساويها، مثل اختبار ويلش.",
    keep:"عند α = 0.05 لا توجد أدلة كافية على اختلاف التباينات. وهذا لا يثبت تساويها، خاصة مع العينات الصغيرة."
  }:{
    error:"Enter 2 to 6 groups, one per line, each with 2 to 100 numbers separated by commas. Absolute values must be at most 1,000,000.",
    undef:"Undefined",inf:"∞ (a group has zero variance)",
    undefined:"The absolute deviations are constant within every group, so the denominator of W is zero and the test is undefined.",
    reject:"At α = 0.05 there is evidence that the variances differ. Consider methods that do not assume equal variances, such as Welch's test.",
    keep:"At α = 0.05 there is not enough evidence that the variances differ. This does not show they are equal, especially in small samples."
  };
  const get=id=>root.querySelector("#esa-lv-"+id);
  const input=get("input"),centerEl=get("center"),error=get("error"),results=get("results");
  const f4=v=>Number.isFinite(v)?v.toFixed(4):v===Infinity?T.inf:T.undef;
  const fp=v=>!Number.isFinite(v)?T.undef:v<1e-6?v.toExponential(3):v.toFixed(6);
  function parse(text){
    const lines=text.split(/\n/).map(l=>l.trim()).filter(Boolean),out=[];
    for(const line of lines){const parts=line.split(",").map(t=>t.trim());
      if(parts.some(t=>!/^[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?$/.test(t)))return null;out.push(parts.map(Number));}
    return out;
  }
  function update(){
    const g=parse(input.value),r=g&&compute(g,centerEl.value);
    if(!r){input.setAttribute("aria-invalid","true");error.hidden=false;error.textContent=T.error;results.hidden=true;return;}
    input.setAttribute("aria-invalid","false");error.hidden=true;error.textContent="";results.hidden=false;
    get("w").textContent=f4(r.W);get("df").textContent=r.df1+", "+r.df2;get("p").textContent=fp(r.p);
    get("ratio").textContent=f4(r.varianceRatio);
    get("sds").textContent=r.sds.map((s,i)=>String.fromCharCode(65+i)+" "+s.toFixed(4)).join(" · ");
    get("decision").textContent=!r.defined?T.undefined:r.p<=0.05?T.reject:T.keep;
  }
  const presets={example:"12.1, 13.4, 11.8, 12.9, 13.1, 12.4\n10.2, 14.8, 9.5, 15.6, 11.9, 13.7\n12.5, 12.8, 13.0, 12.2, 12.6, 12.9",
    equal:"4.1, 5.3, 3.8, 6.0, 4.9, 5.5\n5.2, 4.4, 6.1, 3.9, 5.0, 4.6\n4.8, 5.9, 4.0, 5.4, 4.3, 5.7",
    outlier:"10, 11, 12, 13, 40\n10, 11, 12, 13, 14\n9, 11, 12, 14, 15"};
  for(const name of Object.keys(presets))get(name).addEventListener("click",()=>{input.value=presets[name];update();});
  input.addEventListener("input",update);centerEl.addEventListener("change",update);
  update();
})();
