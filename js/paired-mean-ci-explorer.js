/* Batch #78: matched-pair confidence interval; audited Student-t quantile code reused from Batch #76. */
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

function paired(mean,sd,n,level){
 if(!Number.isFinite(mean)||!Number.isFinite(sd)||Math.abs(mean)>1e9||!(sd>0)||sd>1e9||
    !Number.isSafeInteger(n)||n<2||n>1000000||![90,95,99].includes(level))return null;
 const df=n-1,critical=tQuantile((1+level/100)/2,df),se=sd/Math.sqrt(n),margin=critical*se;
 if(!Number.isFinite(margin)||!Number.isFinite(mean-margin)||!Number.isFinite(mean+margin))return null;
 return {mean,sd,n,df,se,critical,margin,lower:mean-margin,upper:mean+margin,includesZero:mean-margin<=0&&mean+margin>=0};
}
window.esaPairedCIMath={paired,tQuantile};
const root=document.getElementById('esa-paired-ci-lab');if(!root)return;
const get=id=>root.querySelector('#esa-pci-'+id),ids=['mean','sd','n','level'];
const el=(tag,attrs={},content)=>{const n=document.createElementNS('http://www.w3.org/2000/svg',tag);for(const [k,v] of Object.entries(attrs))n.setAttribute(k,String(v));if(content!==undefined)n.textContent=String(content);return n;};
function render(){
 const data=ids.map(id=>get(id).value.trim());
 const mean=data[0]===''?NaN:Number(data[0]),sd=data[1]===''?NaN:Number(data[1]),n=data[2]===''?NaN:Number(data[2]),level=Number(data[3]);
 const stats=paired(mean,sd,n,level),error=get('error'),results=get('results'),chart=get('chart');
 error.hidden=Boolean(stats);results.hidden=!stats;chart.hidden=!stats;
 if(!stats){get('error').textContent='Enter finite mean difference, positive sample SD, integer number of pairs 2–1,000,000, and a supported confidence level.';return;}
 for(const name of ['df','se','critical','margin','lower','upper'])get(name).textContent=stats[name].toFixed(5);
 get('zero').textContent=stats.includesZero?'Zero lies within this interval; the corresponding two-sided t test does not reject a zero mean difference at the matching significance level.':'Zero lies outside this interval; the corresponding two-sided t test rejects a zero mean difference at the matching significance level.';
 const scale=Math.max(stats.margin*.3,1e-6),min=Math.min(stats.lower,0)-scale,max=Math.max(stats.upper,0)+scale;
 const x=v=>35+(v-min)/(max-min)*560;
 const nodes=[el('title',{},'Confidence interval for mean paired difference'),el('desc',{},'Horizontal interval, point estimate and vertical dashed null line at zero.'),el('line',{x1:35,x2:595,y1:90,y2:90,stroke:'currentColor'}),el('line',{x1:x(0),x2:x(0),y1:22,y2:112,stroke:'#64748b','stroke-dasharray':'5 5'}),el('line',{x1:x(stats.lower),x2:x(stats.upper),y1:55,y2:55,stroke:'#0f766e','stroke-width':7}),el('circle',{cx:x(stats.lower),cy:55,r:5,fill:'#0f766e'}),el('circle',{cx:x(stats.upper),cy:55,r:5,fill:'#0f766e'}),el('circle',{cx:x(stats.mean),cy:55,r:7,fill:'#b45309'}),el('text',{x:35,y:115,fill:'currentColor','font-size':12},min.toFixed(2)),el('text',{x:595,y:115,fill:'currentColor','font-size':12,'text-anchor':'end'},max.toFixed(2))];
 chart.replaceChildren(...nodes);
 chart.setAttribute('aria-label',level+' percent confidence interval from '+stats.lower.toFixed(4)+' to '+stats.upper.toFixed(4)+'; estimated mean paired difference '+stats.mean.toFixed(4)+'; dashed line at zero.');
}
ids.forEach(id=>get(id).addEventListener('input',render));
get('reset').addEventListener('click',()=>{get('mean').value='4.2';get('sd').value='3';get('n').value='10';get('level').value='95';render();});
render();
})();
