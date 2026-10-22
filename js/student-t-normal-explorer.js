/* Batch #64: independent Student-t and normal curves and confidence critical values.
   No dependencies or network calls. For a one-sample t interval df=n-1. */
(function(){
  "use strict";
  const root=document.getElementById("esa-t-normal-explorer");
  if(!root)return;
  const id=s=>document.getElementById(s);
  const nControl=id("esa-t-normal-n");
  const confidenceControl=id("esa-t-normal-confidence");
  const svg=id("esa-t-normal-plot");
  const NS="http://www.w3.org/2000/svg";
  const zCritical={90:1.6448536269514722,95:1.959963984540054,99:2.5758293035489004};
  const sqrt2pi=Math.sqrt(2*Math.PI);
  // Lanczos formula, valid for positive arguments used in Student-t densities.
  const c=[0.99999999999980993,676.5203681218851,-1259.1392167224028,
    771.32342877765313,-176.61502916214059,12.507343278686905,
    -0.13857109526572012,9.984369578019572e-6,1.5056327351493116e-7];
  function logGamma(z){
    if(!(z>0)||!Number.isFinite(z))return NaN;
    if(z<.5)return Math.log(Math.PI)-Math.log(Math.sin(Math.PI*z))-logGamma(1-z);
    z-=1;
    let a=c[0];
    for(let i=1;i<c.length;i++)a+=c[i]/(z+i);
    const t=z+7.5;
    return .5*Math.log(2*Math.PI)+(z+.5)*Math.log(t)-t+Math.log(a);
  }
  function betaFraction(a,b,x){
    const TINY=1e-300, EPS=4e-14;
    let qab=a+b,qap=a+1,qam=a-1,cz=1,d=1-qab*x/qap;
    if(Math.abs(d)<TINY)d=TINY;
    d=1/d;let h=d;
    for(let m=1;m<=320;m++){
      const m2=2*m;
      let aa=m*(b-m)*x/((qam+m2)*(a+m2));
      d=1+aa*d;if(Math.abs(d)<TINY)d=TINY;
      cz=1+aa/cz;if(Math.abs(cz)<TINY)cz=TINY;
      d=1/d;h*=d*cz;
      aa=-(a+m)*(qab+m)*x/((a+m2)*(qap+m2));
      d=1+aa*d;if(Math.abs(d)<TINY)d=TINY;
      cz=1+aa/cz;if(Math.abs(cz)<TINY)cz=TINY;
      d=1/d;
      const delta=d*cz;h*=delta;
      if(Math.abs(delta-1)<EPS)break;
    }
    return h;
  }
  function regularizedBeta(x,a,b){
    if(!(a>0)||!(b>0)||!Number.isFinite(x)||x<0||x>1)return NaN;
    if(x===0)return 0;
    if(x===1)return 1;
    const bt=Math.exp(logGamma(a+b)-logGamma(a)-logGamma(b)+
      a*Math.log(x)+b*Math.log1p(-x));
    return x<(a+1)/(a+b+2)
      ?bt*betaFraction(a,b,x)/a
      :1-bt*betaFraction(b,a,1-x)/b;
  }
  function tDensity(x,df){
    if(!Number.isFinite(x)||!Number.isFinite(df)||df<=0)return null;
    return Math.exp(logGamma((df+1)/2)-logGamma(df/2)-
      .5*Math.log(df*Math.PI)-(df+1)/2*Math.log1p(x*x/df));
  }
  function normalDensity(x){
    return Number.isFinite(x)?Math.exp(-x*x/2)/sqrt2pi:null;
  }
  function tCdf(x,df){
    if(!Number.isFinite(x)||!Number.isFinite(df)||df<=0)return null;
    if(x===0)return .5;
    const z=df/(df+x*x);
    const half=.5*regularizedBeta(z,df/2,.5);
    return x>0?1-half:half;
  }
  function tQuantile(prob,df){
    if(!Number.isFinite(prob)||prob<=0||prob>=1||
       !Number.isFinite(df)||df<=0)return null;
    if(prob===.5)return 0;
    if(prob<.5)return -tQuantile(1-prob,df);
    let low=0,high=2;
    while(tCdf(high,df)<prob&&high<1e7)high*=2;
    if(high>=1e7)return null;
    for(let i=0;i<75;i++){
      const mid=(low+high)/2;
      if(tCdf(mid,df)<prob)low=mid;else high=mid;
    }
    return (low+high)/2;
  }
  // Public pure functions for reproducible independent mathematical checks.
  window.esaStudentTMath={logGamma,tDensity,normalDensity,tCdf,tQuantile};
  const fmt=x=>Number.isFinite(x)?x.toFixed(4):"—";
  const el=(tag,attrs,text)=>{
    const e=document.createElementNS(NS,tag);
    for(const [k,v] of Object.entries(attrs||{}))e.setAttribute(k,String(v));
    if(text!==undefined)e.textContent=text;
    return e;
  };
  const xPixel=x=>45+(x+6)/12*585;
  const yPixel=y=>237-y/0.44*198;
  function draw(df,tStar,zStar,confidence){
    const plot=svg;
    plot.replaceChildren(
      el("title",{},"Student t and standard normal probability densities"),
      el("desc",{},"Blue solid curve: Student-t with degrees of freedom equal to n minus one. Green dashed curve: standard normal. The two-sided critical values are shown where they fit on the plot."),
      el("line",{x1:45,y1:237,x2:630,y2:237,stroke:"currentColor","stroke-width":1.3}),
      el("line",{x1:45,y1:237,x2:45,y2:22,stroke:"currentColor","stroke-width":1.3}),
      el("text",{x:11,y:30,"font-size":12,fill:"currentColor"},"Density"),
      el("text",{x:622,y:260,"font-size":12,fill:"currentColor"},"x")
    );
    for(let x=-6;x<=6;x+=2){
      plot.appendChild(el("text",{x:xPixel(x),y:255,"text-anchor":"middle","font-size":11,fill:"currentColor"},String(x)));
    }
    for(const [dfn,color,dash] of [[x=>tDensity(x,df),"#245fd4",null],[normalDensity,"#0f766e","8 5"]]){
      let d="";
      for(let i=0;i<=240;i++){
        const x=-6+12*i/240,y=dfn(x);
        d+=(i?"L":"M")+xPixel(x).toFixed(2)+","+yPixel(y).toFixed(2)+" ";
      }
      const props={d,fill:"none",stroke:color,"stroke-width":2.8};
      if(dash)props["stroke-dasharray"]=dash;
      plot.appendChild(el("path",props));
    }
    const limits=[[zStar,"#0f766e","5 5"],[tStar,"#245fd4","3 3"]];
    for(const [q,color,dash] of limits){
      if(!(q<=6))continue;
      for(const sign of [-1,1]){
        const x=xPixel(sign*q);
        plot.appendChild(el("line",{x1:x,y1:237,x2:x,y2:38,
          stroke:color,"stroke-dasharray":dash,"stroke-width":1.5,opacity:.75}));
      }
    }
    svg.setAttribute("aria-label",
      "Student-t distribution with "+df+" degrees of freedom and standard normal. "+
      confidence+" percent confidence: t critical ±"+fmt(tStar)+
      ", z critical ±"+fmt(zStar)+". Some critical lines may be outside plotted x range.");
  }
  function render(){
    const n=Number(nControl.value),confidence=Number(confidenceControl.value);
    if(!Number.isSafeInteger(n)||n<2||n>121||!Object.hasOwn(zCritical,confidence))return;
    const df=n-1;
    const probability=(1+confidence/100)/2;
    const tStar=tQuantile(probability,df);
    const zStar=zCritical[confidence];
    if(tStar===null)return;
    const se=1/Math.sqrt(n);
    id("esa-t-normal-n-value").textContent=String(n);
    id("esa-t-normal-df").textContent=String(df);
    id("esa-t-normal-tcrit").textContent=fmt(tStar);
    id("esa-t-normal-zcrit").textContent=fmt(zStar);
    id("esa-t-normal-tmargin").textContent=fmt(tStar*se);
    id("esa-t-normal-zmargin").textContent=fmt(zStar*se);
    id("esa-t-normal-ratio").textContent=fmt(tStar/zStar);
    id("esa-t-normal-tail").textContent=(100-confidence)/2+"%";
    id("esa-t-normal-note").textContent=
      "Illustration assumes numerical values s = σ = 1, with one-sample df = n − 1. "+
      "The t margin uses the estimated sample SD s; the z comparison assumes known population σ. "+
      (tStar>6?"The t critical value lies outside the plotted ±6 range. ":"")+
      "The t reference law is exact for an iid normal population with unknown σ; "+
      "large-sample approximation requires additional conditions.";
    draw(df,tStar,zStar,confidence);
  }
  nControl.addEventListener("input",render);
  confidenceControl.addEventListener("change",render);
  id("esa-t-normal-reset").addEventListener("click",()=>{
    nControl.value="10";confidenceControl.value="95";render();
  });
  render();
})();