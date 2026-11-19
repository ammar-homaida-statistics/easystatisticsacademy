/* Easy Statistics Academy Batch #97 — Tukey–Kramer HSD laboratory.
 *
 * Studentized range distribution for k means and nu error degrees of freedom:
 *   P(Q <= q) = int_0^inf f_S(s) P_inf(q s) ds,  S = sqrt(chi2_nu / nu),
 *   P_inf(w)  = k int phi(z) [Phi(z) - Phi(z - w)]^(k - 1) dz.
 * Both integrals use composite 10-point Gauss–Legendre quadrature. The upper
 * tail is computed directly as int f_S(s) [1 - P_inf(q s)] ds, where
 *   1 - P_inf(w) = k int phi(z) {Phi(z)^(k-1) - [Phi(z) - Phi(z - w)]^(k-1)} dz,
 * so small p-values do not suffer from cancellation.
 *
 * Tukey–Kramer for groups i < j:  SE_ij = sqrt(MSW / 2 * (1/n_i + 1/n_j)),
 *   q_ij = |xbar_i - xbar_j| / SE_ij,  p_ij = P(Q_{k,nu} >= q_ij),
 *   simultaneous CI: (xbar_i - xbar_j) +/- q_{1-alpha;k,nu} SE_ij.
 * Exact family-wise level 1 - alpha for equal n under normality and equal
 * variances; conservative for unequal n (Hayter, 1984).
 */
(function () {
  "use strict";
  const GX=[-0.9739065285171717,-0.8650633666889845,-0.6794095682990244,-0.4333953941292472,-0.1488743389816312,
    0.1488743389816312,0.4333953941292472,0.6794095682990244,0.8650633666889845,0.9739065285171717];
  const GW=[0.0666713443086881,0.1494513491505806,0.2190863625159820,0.2692667193099963,0.2955242247147529,
    0.2955242247147529,0.2692667193099963,0.2190863625159820,0.1494513491505806,0.0666713443086881];
  function nodes(a,b,panels){
    const x=[],w=[],h=(b-a)/panels;
    for(let p=0;p<panels;p++){const mid=a+(p+.5)*h;
      for(let i=0;i<10;i++){x.push(mid+GX[i]*h/2);w.push(GW[i]*h/2);}}
    return {x,w};
  }
  // erfc with relative accuracy near 1e-15: Taylor series for |x| < 2.5,
  // Lentz continued fraction otherwise.
  function erfc(x){
    if(x<0)return 2-erfc(-x);
    if(x<2.5){
      let sum=x,term=x,x2=x*x;
      for(let n=1;n<200;n++){term*=-x2/n;const add=term/(2*n+1);sum+=add;if(Math.abs(add)<1e-17*Math.abs(sum))break;}
      return 1-2/Math.sqrt(Math.PI)*sum;
    }
    // erfc(x) = exp(-x^2)/sqrt(pi) * 1/(x + 1/2/(x + 1/(x + 3/2/(x + ...))))
    const TINY=1e-300;let f=x,C=x,D=0;
    for(let n=1;n<500;n++){const a=n/2;D=x+a*D;if(Math.abs(D)<TINY)D=TINY;C=x+a/C;if(Math.abs(C)<TINY)C=TINY;
      D=1/D;const delta=C*D;f*=delta;if(Math.abs(delta-1)<1e-16)break;}
    return Math.exp(-x*x)/Math.sqrt(Math.PI)/f;
  }
  const Phi=z=>0.5*erfc(-z/Math.SQRT2);
  const phi=z=>Math.exp(-z*z/2)/Math.sqrt(2*Math.PI);
  const Z=nodes(-8.5,8.5,16);
  const PHIZ=Z.x.map(Phi),DENZ=Z.x.map(phi);
  function upperInf(w,k){
    if(w<=0)return 1;
    let s=0;
    for(let i=0;i<Z.x.length;i++){
      const a=PHIZ[i],d=a-Phi(Z.x[i]-w);
      s+=Z.w[i]*DENZ[i]*(Math.pow(a,k-1)-Math.pow(Math.max(0,d),k-1));
    }
    return Math.min(1,Math.max(0,k*s));
  }
  function logGamma(z){
    const c=[0.99999999999980993,676.5203681218851,-1259.1392167224028,771.32342877765313,
      -176.61502916214059,12.507343278686905,-0.13857109526572012,9.984369578019572e-6,1.5056327351493116e-7];
    if(z<0.5)return Math.log(Math.PI/Math.abs(Math.sin(Math.PI*z)))-logGamma(1-z);
    z-=1;let x=c[0];for(let i=1;i<9;i++)x+=c[i]/(z+i);const t=z+7.5;
    return .5*Math.log(2*Math.PI)+(z+.5)*Math.log(t)-t+Math.log(x);
  }
  // Outer integral over S. Only s < 13/q matters, because 1 - P_inf(w) is
  // below 1e-30 for w >= 13 and k <= 6, so the range shrinks with q.
  function ptukeyUpper(q,k,nu){
    if(!(k>=2)||!(nu>=1)||!Number.isFinite(k)||Number.isNaN(nu)||Number.isNaN(q))return NaN;
    if(q<=0)return 1;
    if(q===Infinity)return 0;
    if(nu===Infinity)return upperInf(q,k);
    const lc=(nu/2)*Math.log(nu)-logGamma(nu/2)-(nu/2-1)*Math.LN2,sd=1/Math.sqrt(2*nu);
    const lo=nu<=4?0:Math.max(0,1-14*sd),hi=Math.min(nu<=4?1+30/Math.sqrt(nu):1+14*sd+2/nu,13/q);
    if(hi<=lo)return 0;
    const g=nodes(lo,hi,nu<=4?40:16);let s=0;
    for(let i=0;i<g.x.length;i++){
      const x=g.x[i],dens=Math.exp(lc+(nu-1)*Math.log(x)-nu*x*x/2);
      s+=g.w[i]*dens*upperInf(q*x,k);
    }
    return Math.min(1,Math.max(0,s));
  }
  // Quantile: q with P(Q >= q) = alpha. Illinois (modified regula falsi) on
  // log P(Q >= q) - log alpha, keeping a bracket so it always converges.
  function qtukey(alpha,k,nu){
    if(!(alpha>0&&alpha<1)||!(k>=2)||!(nu>=1))return NaN;
    const g=q=>Math.log(ptukeyUpper(q,k,nu))-Math.log(alpha);
    let a=0.5,fa=g(a),b=4,fb=g(b);
    while(fa<0&&a>1e-6){b=a;fb=fa;a/=4;fa=g(a);}
    while(fb>0&&b<1e4){a=b;fa=fb;b*=2;fb=g(b);}
    let side=0;
    for(let it=0;it<100;it++){
      const c=(a*fb-b*fa)/(fb-fa),fc=g(c);
      if(Math.abs(fc)<1e-12||Math.abs(b-a)<1e-11*c)return c;
      if(fc*fb<0){a=b;fa=fb;b=c;fb=fc;side=0;}
      else{b=c;fb=fc;if(side===-1)fa/=2;side=-1;}
    }
    return (a+b)/2;
  }
  function compute(groups,alpha){
    if(alpha===undefined)alpha=0.05;
    if(!Array.isArray(groups)||groups.length<2||groups.length>6||!(alpha>0&&alpha<1)||groups.some(
      g=>!Array.isArray(g)||g.length<2||g.length>100||g.some(x=>!Number.isFinite(x)||Math.abs(x)>1e6)))return null;
    const k=groups.length,n=groups.map(g=>g.length),N=n.reduce((a,b)=>a+b,0),nu=N-k;
    const means=groups.map(g=>g.reduce((a,b)=>a+b,0)/g.length);
    const ssw=groups.reduce((a,g,i)=>a+g.reduce((b,x)=>b+(x-means[i])**2,0),0),msw=ssw/nu;
    const qcrit=qtukey(alpha,k,nu),pairs=[];
    for(let i=0;i<k;i++)for(let j=i+1;j<k;j++){
      const diff=means[i]-means[j],se=Math.sqrt(msw/2*(1/n[i]+1/n[j]));
      const q=se>0?Math.abs(diff)/se:(diff===0?NaN:Infinity);
      const p=Number.isNaN(q)?NaN:ptukeyUpper(q,k,nu);
      pairs.push({i,j,diff,se,q,p,lower:diff-qcrit*se,upper:diff+qcrit*se,reject:p<=alpha});
    }
    return {k,n,N,nu,means,msw,alpha,qcrit,pairs,degenerate:!(msw>0)};
  }
  window.esaTukey={compute,ptukeyUpper,qtukey,erfc};

  const root=typeof document!=="undefined"&&document.getElementById("esa-tukey-lab");
  if(!root)return;
  const AR=root.dataset.locale==="ar";
  const T=AR?{
    error:"أدخل من 2 إلى 6 مجموعات، كل مجموعة في سطر، ومن 2 إلى 100 عدد في كل سطر مفصولة بفواصل إنجليزية. يجب ألا تتجاوز القيم المطلقة 1,000,000.",
    yes:"دال",no:"غير دال",undef:"غير معرّف",
    degenerate:"لا يوجد تباين داخل المجموعات (MSW = 0)، لذا لا تُعرَّف إحصائية q ولا فترات الثقة بمعناها المعتاد.",
    summary:(r,c)=>"عند α = 0.05 تكون "+r+" من أصل "+c+" مقارنة زوجية دالة، ويُضبط معدل الخطأ العائلي لجميع المقارنات معًا."
  }:{
    error:"Enter 2 to 6 groups, one per line, each with 2 to 100 numbers separated by commas. Absolute values must be at most 1,000,000.",
    yes:"Significant",no:"Not significant",undef:"Undefined",
    degenerate:"There is no within-group variation (MSW = 0), so q and the intervals are not defined in the usual sense.",
    summary:(r,c)=>r+" of "+c+" pairwise comparisons are significant at α = 0.05, with the family-wise error rate controlled across all of them."
  };
  const get=id=>root.querySelector("#esa-tukey-"+id);
  const input=get("input"),error=get("error"),results=get("results");
  const fmt=x=>Number.isNaN(x)?T.undef:x===Infinity?"∞":x.toFixed(4);
  const fmtp=x=>Number.isNaN(x)?T.undef:x<1e-6?"< 0.000001":x.toFixed(6);
  function parse(text){
    const lines=text.split(/\n/).map(l=>l.trim()).filter(Boolean);
    const out=[];
    for(const line of lines){
      const parts=line.split(",").map(t=>t.trim());
      if(parts.some(t=>!/^[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?$/.test(t)))return null;
      out.push(parts.map(Number));
    }
    return out;
  }
  function update(){
    const groups=parse(input.value),r=groups&&compute(groups,0.05);
    if(!r){input.setAttribute("aria-invalid","true");error.hidden=false;error.textContent=T.error;results.hidden=true;return;}
    input.setAttribute("aria-invalid","false");error.hidden=true;error.textContent="";results.hidden=false;
    get("k").textContent=String(r.k);get("nu").textContent=String(r.nu);
    get("msw").textContent=r.msw.toFixed(6);get("qcrit").textContent=fmt(r.qcrit);
    const L=i=>String.fromCharCode(65+i);
    get("rows").replaceChildren(...r.pairs.map(pr=>{
      const tr=document.createElement("tr"),th=document.createElement("th");
      th.scope="row";th.textContent=L(pr.i)+" − "+L(pr.j);th.setAttribute("dir","ltr");tr.appendChild(th);
      for(const v of [fmt(pr.diff),fmt(pr.q),fmtp(pr.p),"["+fmt(pr.lower)+", "+fmt(pr.upper)+"]",
        Number.isNaN(pr.p)?T.undef:pr.reject?T.yes:T.no]){
        const td=document.createElement("td");td.textContent=v;tr.appendChild(td);
      }
      return tr;
    }));
    get("summary").textContent=r.degenerate?T.degenerate:T.summary(r.pairs.filter(p=>p.reject).length,r.pairs.length);
  }
  const presets={example:"4, 5, 6\n5, 6, 7\n8, 9, 10",unequal:"2, 3, 6, 7\n3, 4\n8, 8, 9, 10, 11",
    four:"1.2, 3.4, 2.2, 5.1\n2.0, 2.5, 2.9\n3.3, 4.1, 6.0, 5.5, 4.4\n0.4, 1.1, 2.6"};
  for(const name of Object.keys(presets))get(name).addEventListener("click",()=>{input.value=presets[name];update();});
  let timer=0;
  input.addEventListener("input",()=>{clearTimeout(timer);timer=setTimeout(update,200);});
  update();
})();
