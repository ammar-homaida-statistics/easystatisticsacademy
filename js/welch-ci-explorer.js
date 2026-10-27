/* Batch #76: Welch two-independent-means confidence interval; Student-t quantile via regularized beta. */
(function(){'use strict';
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

function welch(m1,s1,n1,m2,s2,n2,confidence){
 if (![m1,s1,n1,m2,s2,n2].every(Number.isFinite)||!Number.isSafeInteger(n1)||!Number.isSafeInteger(n2)||n1<2||n2<2||n1>1000000||n2>1000000||s1<0||s2<0||![90,95,99].includes(confidence))return null;
 const a=s1*s1/n1,b=s2*s2/n2,variance=a+b;
 if(!(variance>0)||!Number.isFinite(variance))return null;
 const df=variance*variance/(a*a/(n1-1)+b*b/(n2-1)),critical=tQuantile((1+confidence/100)/2,df),se=Math.sqrt(variance),diff=m1-m2,margin=critical*se;
 if(!Number.isFinite(margin))return null;
 return {diff,se,df,critical,margin,lower:diff-margin,upper:diff+margin};
}
window.esaWelchMath={welch,tQuantile};
const root=document.getElementById('esa-welch-explorer');if(!root)return;
const get=id=>root.querySelector('#'+id),ids=['m1','s1','n1','m2','s2','n2','confidence'];
function render(){let vals=ids.map(id=>Number(get('esa-welch-'+id).value));const out=welch(...vals),error=get('esa-welch-error'),results=get('esa-welch-results'),svg=get('esa-welch-chart');
 error.hidden=Boolean(out);results.hidden=!out;svg.hidden=!out;if(!out)return;
 for(const key of ['diff','se','df','critical','margin','lower','upper'])get('esa-welch-'+key).textContent=out[key].toFixed(4);
 const low=Math.min(out.lower,0),high=Math.max(out.upper,0),padding=Math.max(out.margin*.4,1),min=low-padding,max=high+padding,x=v=>30+(v-min)/(max-min)*560;
 const NS='http://www.w3.org/2000/svg',node=(tag,attrs,txt)=>{const e=document.createElementNS(NS,tag);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,String(v)));if(txt!==undefined)e.textContent=txt;return e;};
 svg.replaceChildren(node('title',{},'Welch confidence interval for group one minus group two'),node('line',{x1:30,y1:60,x2:590,y2:60,stroke:'currentColor'}),node('line',{x1:x(0),y1:15,x2:x(0),y2:105,stroke:'currentColor','stroke-dasharray':'4 4'}),node('line',{x1:x(out.lower),y1:50,x2:x(out.upper),y2:50,stroke:'#2563eb','stroke-width':6}),node('circle',{cx:x(out.diff),cy:50,r:6,fill:'#0f766e'}),node('text',{x:30,y:115,fill:'currentColor','font-size':12},out.lower.toFixed(2)),node('text',{x:590,y:115,'text-anchor':'end',fill:'currentColor','font-size':12},out.upper.toFixed(2)));
 svg.setAttribute('aria-label', 'Estimated difference '+out.diff.toFixed(4)+'; confidence interval '+out.lower.toFixed(4)+' to '+out.upper.toFixed(4)+'; dashed line denotes zero.');
}
ids.forEach(id=>get('esa-welch-'+id).addEventListener('input',render));render();
})();