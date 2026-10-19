/* Independent labeled p-value demonstrations: unadjusted, Bonferroni and BH. */
(function () {
  "use strict";
  if (!document.getElementById("esa-mt-lab")) return;
  const $ = id => document.getElementById(id);
  const count=$("esa-mt-count"), alpha=$("esa-mt-alpha"), seed=$("esa-mt-seed");
  const status=$("esa-mt-status");
  function random(seedValue) {
    let state=seedValue>>>0;
    return () => {
      state=(state+0x6D2B79F5)>>>0;
      let t=Math.imul(state^(state>>>15),1|state);
      t^=t+Math.imul(t^(t>>>7),61|t);
      return ((t^(t>>>14))>>>0)/4294967296;
    };
  }
  function fixed(x) { return x.toFixed(6); }
  function makeCell(row,value) {
    const td=document.createElement("td");
    td.textContent=String(value);
    row.appendChild(td);
  }
  function run() {
    const m=Number(count.value), a=Number(alpha.value), s=Number(seed.value);
    if (![5,10,20].includes(m) || ![.01,.05,.1].includes(a) ||
        !seed.value.trim() || !Number.isInteger(s) || s<0 || s>4294967295) {
      status.textContent="Use the available counts/levels and an integer seed from 0 to 4294967295.";
      return;
    }
    const rng=random(s);
    const pvalues=Array.from({length:m},(_,i)=>{
      const u=rng();
      return i%4===0 ? Math.pow(u,4) : u;
    });
    const isNull=Array.from({length:m},(_,i)=>i%4!==0);
    const order=Array.from({length:m},(_,i)=>i).sort((i,j)=>pvalues[i]-pvalues[j]||i-j);
    // BH step-up: find the largest rank k satisfying p_(k) <= k*alpha/m.
    let k=0;
    order.forEach((index,j)=>{if(pvalues[index]<=(j+1)*a/m)k=j+1;});
    const cutoff=k?pvalues[order[k-1]]:null;
    const decision=[
      pvalues.map(p=>p<=a),
      pvalues.map(p=>p<=a/m),
      pvalues.map(p=>cutoff!==null && p<=cutoff)
    ];
    $("esa-mt-bonf-cut").textContent=fixed(a/m);
    $("esa-mt-bh-rank").textContent=String(k);
    $("esa-mt-bh-cut").textContent=cutoff===null?"No rejections":fixed(cutoff);
    $("esa-mt-fwer").textContent=fixed(1-Math.pow(1-a,m));
    const rows=$("esa-mt-table"),sum=$("esa-mt-summary");
    rows.replaceChildren();sum.replaceChildren();
    pvalues.forEach((p,i)=>{
      const tr=document.createElement("tr");
      [i+1,isNull[i]?"True null":"Alternative",fixed(p),...decision.map(d=>d[i]?"Reject":"Retain")].forEach(x=>makeCell(tr,x));
      rows.appendChild(tr);
    });
    ["Unadjusted","Bonferroni","Benjamini–Hochberg"].forEach((name,j)=>{
      const d=decision[j];
      const R=d.filter(Boolean).length;
      const V=d.filter((rejected,i)=>rejected && isNull[i]).length;
      const tr=document.createElement("tr");
      [name,R,V,fixed(V/Math.max(R,1))].forEach(x=>makeCell(tr,x));
      sum.appendChild(tr);
    });
    status.textContent="Simulation complete; identical settings and seed reproduce every p-value and decision.";
    $("esa-mt-notes").textContent="BH sorts p-values, finds the largest eligible rank, and rejects all hypotheses through that rank. "+
      "Retain means not rejected, NOT that the null hypothesis is proven true. False-discovery labels exist only in this simulation.";
  }
  $("esa-mt-run").addEventListener("click",run);
  $("esa-mt-reset").addEventListener("click",()=>{
    count.value="10";alpha.value="0.05";seed.value="2026";run();
  });
  run();
})();