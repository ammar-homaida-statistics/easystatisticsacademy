/* Easy Statistics Academy Batch #98 — Kruskal–Wallis laboratory.
 *
 * Ranks use average ranks for ties. With N observations in k groups,
 *   H = 12 / (N (N + 1)) * sum_i R_i^2 / n_i - 3 (N + 1),
 *   C = 1 - sum_t (t^3 - t) / (N^3 - N)        (tie correction),
 *   H_c = H / C,  p_chi2 = P(chi2_{k-1} >= H_c)  (SciPy kruskal convention),
 *   epsilon^2 = H_c / (N - 1)                   (Tomczak & Tomczak, 2014).
 * Monte Carlo permutation p-value with B random relabelings of the pooled
 * ranks (C is invariant under relabeling, so sum R_i^2 / n_i is permuted):
 *   p_perm = (1 + #{H* >= H_obs}) / (B + 1),  SE = sqrt(p (1 - p) / B).
 * A fixed seed makes the displayed permutation p-value reproducible.
 */
(function () {
  "use strict";
  const LG=[0.99999999999980993,676.5203681218851,-1259.1392167224028,771.32342877765313,
    -176.61502916214059,12.507343278686905,-0.13857109526572012,9.984369578019572e-6,1.5056327351493116e-7];
  function logGamma(z){
    if(z<.5)return Math.log(Math.PI/Math.abs(Math.sin(Math.PI*z)))-logGamma(1-z);
    z-=1;let a=LG[0];for(let i=1;i<9;i++)a+=LG[i]/(z+i);const t=z+7.5;
    return .5*Math.log(2*Math.PI)+(z+.5)*Math.log(t)-t+Math.log(a);
  }
  // Regularized upper incomplete gamma Q(a, x): series for x < a + 1,
  // Lentz continued fraction otherwise.
  function gammaQ(a,x){
    if(!(a>0)||!(x>=0))return NaN;
    if(x===0)return 1;
    const lf=a*Math.log(x)-x-logGamma(a);
    if(x<a+1){let term=1/a,sum=term;
      for(let n=1;n<2000;n++){term*=x/(a+n);sum+=term;if(Math.abs(term)<Math.abs(sum)*1e-16)break;}
      return Math.min(1,Math.max(0,1-sum*Math.exp(lf)));}
    let b=x+1-a,c=1e300,d=1/b,h=d;
    for(let n=1;n<2000;n++){const an=-n*(n-a);b+=2;d=an*d+b;if(Math.abs(d)<1e-300)d=1e-300;
      c=b+an/c;if(Math.abs(c)<1e-300)c=1e-300;d=1/d;const del=d*c;h*=del;if(Math.abs(del-1)<1e-16)break;}
    return Math.min(1,Math.max(0,Math.exp(lf)*h));
  }
  const chi2Upper=(x,df)=>gammaQ(df/2,x/2);
  function rankAll(groups){
    const all=[];groups.forEach((g,gi)=>g.forEach(v=>all.push({v,gi})));
    all.sort((a,b)=>a.v-b.v);
    const ranks=new Float64Array(all.length);let ties=0;
    for(let i=0;i<all.length;){
      let j=i;while(j+1<all.length&&all[j+1].v===all[i].v)j++;
      const r=(i+j)/2+1,t=j-i+1;if(t>1)ties+=t*t*t-t;
      for(let m=i;m<=j;m++)ranks[m]=r;
      i=j+1;
    }
    return {all,ranks,ties};
  }
  function mulberry32(seed){return function(){seed|=0;seed=seed+0x6D2B79F5|0;let t=Math.imul(seed^seed>>>15,1|seed);
    t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
  function compute(groups,options){
    const opt=Object.assign({permutations:10000,seed:98},options||{});
    if(!Array.isArray(groups)||groups.length<2||groups.length>6||groups.some(
      g=>!Array.isArray(g)||g.length<1||g.length>100||g.some(x=>!Number.isFinite(x)||Math.abs(x)>1e6)))return null;
    if(!Number.isSafeInteger(opt.permutations)||opt.permutations<0||opt.permutations>100000)return null;
    const k=groups.length,n=groups.map(g=>g.length),N=n.reduce((a,b)=>a+b,0);
    if(N<3)return null;
    const {all,ranks,ties}=rankAll(groups);
    const R=new Float64Array(k);all.forEach((o,i)=>{R[o.gi]+=ranks[i];});
    const S=Array.from(R).reduce((a,r,i)=>a+r*r/n[i],0);
    const H=12/(N*(N+1))*S-3*(N+1),C=1-ties/(N*N*N-N),df=k-1;
    const out={k,N,n,df,rankSums:Array.from(R),meanRanks:Array.from(R).map((r,i)=>r/n[i]),H,C,
      small:n.some(v=>v<5),permutations:opt.permutations};
    if(!(C>1e-12))return Object.assign(out,{defined:false,Hc:NaN,p:NaN,epsilon2:NaN,pPerm:NaN,sePerm:NaN});
    const Hc=Math.max(0,H/C);
    out.defined=true;out.Hc=Hc;out.p=chi2Upper(Hc,df);out.epsilon2=Hc/(N-1);
    if(opt.permutations>0){
      const rnd=mulberry32(opt.seed),pool=Float64Array.from(ranks),B=opt.permutations;
      const tol=1e-9*Math.max(1,S);let hits=0;
      for(let b=0;b<B;b++){
        for(let i=pool.length-1;i>0;i--){const j=Math.floor(rnd()*(i+1));const t=pool[i];pool[i]=pool[j];pool[j]=t;}
        let s=0,pos=0;
        for(let g=0;g<k;g++){let r=0;for(let m=0;m<n[g];m++)r+=pool[pos++];s+=r*r/n[g];}
        if(s>=S-tol)hits++;
      }
      out.pPerm=(1+hits)/(B+1);out.sePerm=Math.sqrt(out.pPerm*(1-out.pPerm)/B);
    }else{out.pPerm=NaN;out.sePerm=NaN;}
    return out;
  }
  window.esaKruskal={compute,chi2Upper,gammaQ};

  const root=typeof document!=="undefined"&&document.getElementById("esa-kw-lab");
  if(!root)return;
  const AR=root.dataset.locale==="ar";
  const T=AR?{
    error:"أدخل من 2 إلى 6 مجموعات، كل مجموعة في سطر، ومن 1 إلى 100 عدد في كل سطر مفصولة بفواصل إنجليزية، بإجمالي 3 مشاهدات على الأقل. يجب ألا تتجاوز القيم المطلقة 1,000,000.",
    undef:"غير معرّف",
    allTied:"جميع المشاهدات متساوية، فلا توجد رتب مختلفة؛ لذا H غير معرّفة.",
    small:"مجموعة واحدة على الأقل فيها أقل من 5 مشاهدات؛ قد يكون تقريب كاي تربيع غير دقيق، فاعتمد على القيمة الاحتمالية بالتبديل.",
    ok:"جميع المجموعات فيها 5 مشاهدات أو أكثر؛ تقريب كاي تربيع مقبول عادة قرب مستويات α المعتادة، لكنه قد يكون غير دقيق للقيم الاحتمالية الصغيرة جدًا؛ والقيمة بالتبديل للمقارنة.",
    decision:p=>p<=0.05?"عند α = 0.05 نرفض فرضية أن جميع المجموعات من التوزيع نفسه.":"عند α = 0.05 لا نرفض فرضية أن جميع المجموعات من التوزيع نفسه."
  }:{
    error:"Enter 2 to 6 groups, one per line, each with 1 to 100 numbers separated by commas, and at least 3 observations in total. Absolute values must be at most 1,000,000.",
    undef:"Undefined",
    allTied:"All observations are tied, so there are no distinct ranks and H is undefined.",
    small:"At least one group has fewer than 5 observations; the chi-square approximation can be inaccurate, so rely on the permutation p-value.",
    ok:"Every group has at least 5 observations; the chi-square approximation is usually adequate near conventional α levels but can be inaccurate for very small p-values; the permutation p-value is shown for comparison.",
    decision:p=>p<=0.05?"At α = 0.05, reject the hypothesis that all groups come from the same distribution.":"At α = 0.05, do not reject the hypothesis that all groups come from the same distribution."
  };
  const get=id=>root.querySelector("#esa-kw-"+id);
  const input=get("input"),error=get("error"),results=get("results");
  const f4=x=>Number.isFinite(x)?x.toFixed(4):T.undef;
  const fp=x=>!Number.isFinite(x)?T.undef:x<1e-6?x.toExponential(3):x.toFixed(6);
  function parse(text){
    const lines=text.split(/\n/).map(l=>l.trim()).filter(Boolean),out=[];
    for(const line of lines){
      const parts=line.split(",").map(t=>t.trim());
      if(parts.some(t=>!/^[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?$/.test(t)))return null;
      out.push(parts.map(Number));
    }
    return out;
  }
  function update(){
    const groups=parse(input.value),r=groups&&compute(groups);
    if(!r){input.setAttribute("aria-invalid","true");error.hidden=false;error.textContent=T.error;results.hidden=true;return;}
    input.setAttribute("aria-invalid","false");error.hidden=true;error.textContent="";results.hidden=false;
    get("k").textContent=String(r.k);get("N").textContent=String(r.N);get("df").textContent=String(r.df);
    get("h").textContent=f4(r.H);get("c").textContent=r.C.toFixed(6);get("hc").textContent=f4(r.Hc);
    get("p").textContent=fp(r.p);get("eps").textContent=f4(r.epsilon2);
    get("pperm").textContent=Number.isFinite(r.pPerm)?fp(r.pPerm)+" ± "+r.sePerm.toFixed(4):T.undef;
    const L=i=>String.fromCharCode(65+i);
    get("rows").replaceChildren(...r.n.map((ni,i)=>{
      const tr=document.createElement("tr"),th=document.createElement("th");th.scope="row";th.textContent=L(i);tr.appendChild(th);
      for(const v of [String(ni),r.rankSums[i].toFixed(1),r.meanRanks[i].toFixed(3)]){const td=document.createElement("td");td.textContent=v;tr.appendChild(td);}
      return tr;
    }));
    get("note").textContent=!r.defined?T.allTied:r.small?T.small:T.ok;
    get("decision").textContent=r.defined?T.decision(r.small?r.pPerm:r.p):"";
  }
  const presets={example:"2.1, 3.4, 1.9, 5.6, 2.8\n4.2, 6.1, 5.5, 7.3, 4.9\n8.8, 6.7, 9.4, 7.9, 12.5",
    ties:"1, 2, 2, 3, 3, 3\n2, 3, 3, 4, 4, 5\n3, 4, 5, 5, 5, 6",
    small:"1.2, 3.1, 2.2\n2.8, 4.0, 3.6\n5.1, 4.4"};
  for(const name of Object.keys(presets))get(name).addEventListener("click",()=>{input.value=presets[name];update();});
  let timer=0;
  input.addEventListener("input",()=>{clearTimeout(timer);timer=setTimeout(update,200);});
  update();
})();
