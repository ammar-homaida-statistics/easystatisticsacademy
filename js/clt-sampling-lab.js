/* Central Limit Theorem lab: same deterministic mathematical model for English and Arabic. */
(function () {
  "use strict";
  const root=document.getElementById("esa-clt-lab");
  if(!root)return;
  const $=id=>document.getElementById(id);
  const ar=document.documentElement.lang==="ar";
  const T=ar?{
    invalid:"أدخل بذرة صحيحة من 1 إلى 2147483647.",
    done:"اكتملت المحاكاة. تغيير حجم العينة يغير توزيع المتوسطات، لا توزيع المشاهدات.",
    xaxis:"متوسطات العينات",empty:"لا توجد بيانات"
  }:{
    invalid:"Enter an integer seed between 1 and 2147483647.",
    done:"Simulation completed. Changing n changes the distribution of sample means, not the source distribution.",
    xaxis:"Sample means",empty:"No data"
  };
  const N=800, BINS=16, NS="http://www.w3.org/2000/svg";
  function rngFactory(seed){
    let state=seed>>>0;
    return function(){
      state^=state<<13;state^=state>>>17;state^=state<<5;
      return ((state>>>0)+0.5)/4294967296;
    };
  }
  function fmt(x){return x.toFixed(4);}
  function svgEl(tag,attrs,txt){
    const node=document.createElementNS(NS,tag);
    for(const [name,value] of Object.entries(attrs||{}))node.setAttribute(name,String(value));
    if(txt!==undefined)node.textContent=txt;
    return node;
  }
  function run(){
    const raw=$("esa-clt-seed").value.trim();
    if(!/^\d+$/.test(raw)){ $("esa-clt-status").textContent=T.invalid;return;}
    const seed=Number(raw), n=Number($("esa-clt-n").value);
    if(!Number.isSafeInteger(seed)||seed<1||seed>2147483647||
       ![1,5,30,100].includes(n)){$("esa-clt-status").textContent=T.invalid;return;}
    const random=rngFactory(seed);
    const means=[];
    for(let k=0;k<N;k++){
      let sum=0;
      for(let j=0;j<n;j++)sum+=-Math.log(1-random());
      means.push(sum/n);
    }
    const avg=means.reduce((a,b)=>a+b,0)/N;
    const sd=Math.sqrt(means.reduce((a,b)=>a+(b-avg)**2,0)/N);
    const lo=Math.min(...means),hi=Math.max(...means);
    const width=(hi-lo)/BINS||1;
    const bins=Array(BINS).fill(0);
    for(const x of means)bins[Math.min(BINS-1,Math.floor((x-lo)/width))]++;
    const maxCount=Math.max(...bins);
    const chart=$("esa-clt-chart");
    chart.replaceChildren();
    chart.append(svgEl("line",{x1:40,y1:200,x2:620,y2:200,stroke:"currentColor","stroke-width":1.2}));
    for(let i=0;i<BINS;i++){
      const h=168*bins[i]/maxCount;
      chart.append(svgEl("rect",{x:42+i*36,y:200-h,width:33,height:h,fill:"#2e6ba6"}));
    }
    chart.append(svgEl("text",{x:42,y:224,"font-size":13,fill:"currentColor"},lo.toFixed(2)));
    chart.append(svgEl("text",{x:330,y:224,"text-anchor":"middle","font-size":13,fill:"currentColor"},((lo+hi)/2).toFixed(2)));
    chart.append(svgEl("text",{x:618,y:224,"text-anchor":"end","font-size":13,fill:"currentColor"},hi.toFixed(2)));
    chart.append(svgEl("text",{x:330,y:243,"text-anchor":"middle","font-size":13,fill:"currentColor"},T.xaxis));
    $("esa-clt-theory-mean").textContent="1.0000";
    $("esa-clt-theory-se").textContent=fmt(1/Math.sqrt(n));
    $("esa-clt-emp-mean").textContent=fmt(avg);
    $("esa-clt-emp-sd").textContent=fmt(sd);
    $("esa-clt-count").textContent=String(N);
    $("esa-clt-status").textContent=T.done;
  }
  $("esa-clt-run").addEventListener("click",run);
  run();
})();