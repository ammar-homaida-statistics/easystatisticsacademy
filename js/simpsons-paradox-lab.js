/* Group/stratum rate comparisons: Simpson's paradox with validated count input. */
(function(){
  "use strict";
  if(!document.getElementById("esa-simpson-lab"))return;
  const $=id=>document.getElementById(id);
  const fields=["a1","b1","a2","b2"];
  const initial={a1:[81,87],b1:[234,270],a2:[192,263],b2:[55,80]};
  const balanced={a1:[81,90],b1:[85,100],a2:[70,100],b2:[65,100]};
  const fmt=p=>(100*p).toFixed(2)+"%";
  const winner=(a,b)=>a>b?"A":b>a?"B":"Tie";
  function fill(preset){
    for(const f of fields){$(`esa-sp-${f}-s`).value=String(preset[f][0]);
      $(`esa-sp-${f}-n`).value=String(preset[f][1]);}
    run();
  }
  function parse(id,min){
    const element=$(id),raw=element.value.trim();
    if(!/^\d+$/.test(raw))return null;
    const n=Number(raw);
    return Number.isSafeInteger(n)&&n>=min&&n<=10000?n:null;
  }
  function run(){
    const data={};
    for(const f of fields){
      const success=parse(`esa-sp-${f}-s`,0),total=parse(`esa-sp-${f}-n`,1);
      if(success===null||total===null||success>total){
        $("esa-sp-status").textContent="Invalid counts: each total must be a positive whole number (maximum 10,000); each success count must be a whole number between zero and its total.";
        return;
      }
      data[f]={success,total,rate:success/total};
    }
    for(const f of fields){
      $(`esa-sp-${f}-rate`).textContent=fmt(data[f].rate);
      $(`esa-sp-${f}-out`).textContent=fmt(data[f].rate);
    }
    const a=(data.a1.success+data.a2.success)/(data.a1.total+data.a2.total);
    const b=(data.b1.success+data.b2.success)/(data.b1.total+data.b2.total);
    const aStandard=(data.a1.rate+data.a2.rate)/2;
    const bStandard=(data.b1.rate+data.b2.rate)/2;
    [["esa-sp-a-pooled",fmt(a)],["esa-sp-b-pooled",fmt(b)],
     ["esa-sp-a-standard",fmt(aStandard)],["esa-sp-b-standard",fmt(bStandard)],
     ["esa-sp-winner1",winner(data.a1.rate,data.b1.rate)],
     ["esa-sp-winner2",winner(data.a2.rate,data.b2.rate)],
     ["esa-sp-winner-pooled",winner(a,b)],["esa-sp-winner-standard",winner(aStandard,bStandard)]]
     .forEach(([id,value])=>{$(id).textContent=value;});
    const within1=winner(data.a1.rate,data.b1.rate);
    const within2=winner(data.a2.rate,data.b2.rate);
    const pooled=winner(a,b);
    const reversal=within1===within2&&within1!=="Tie"&&pooled!=="Tie"&&within1!==pooled;
    $("esa-sp-explanation").textContent=reversal?
      "Simpson's paradox: group "+within1+" has the higher rate in each stratum, but group "+pooled+
      " has the higher pooled rate because stratum composition differs. Equal-stratum standardization uses the same mix for each group.":
      "No strict Simpson reversal for these inputs. Compare the stratum allocations and their corresponding rates; pooled and within-stratum rankings need not agree.";
    $("esa-sp-status").textContent="Calculated all rates from the current integer successes and denominators.";
  }
  $("esa-sp-run").addEventListener("click",run);
  $("esa-sp-balanced").addEventListener("click",()=>fill(balanced));
  $("esa-sp-reset").addEventListener("click",()=>fill(initial));
  run();
})();