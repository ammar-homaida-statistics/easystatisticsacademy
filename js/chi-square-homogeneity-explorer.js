/* Easy Statistics Academy Batch #67 — chi-square test of homogeneity.
 * This is the Pearson asymptotic test WITHOUT continuity correction,
 * on independent groups with positive row/column marginal counts.
 */
(function(){
 "use strict";
 const root=document.getElementById("esa-homogeneity-lab");
 if(!root)return;
 const byId=id=>root.querySelector("#esa-hom-"+id);
 const lanczos=[0.99999999999980993,676.5203681218851,-1259.1392167224028,
 771.32342877765313,-176.61502916214059,12.507343278686905,
 -0.13857109526572012,9.984369578019572e-6,1.5056327351493116e-7];
 function logGamma(z){
   if(!(z>0)||!Number.isFinite(z))return NaN;
   if(z<.5)return Math.log(Math.PI)-Math.log(Math.sin(Math.PI*z))-logGamma(1-z);
   z-=1;let a=lanczos[0];
   for(let i=1;i<lanczos.length;i++)a+=lanczos[i]/(z+i);
   const t=z+7.5;
   return .5*Math.log(2*Math.PI)+(z+.5)*Math.log(t)-t+Math.log(a);
 }
 function gammaQ(a,x){
   if(!(a>0)||!Number.isFinite(a)||Number.isNaN(x)||x<0)return NaN;
   if(x===0)return 1;
   if(x===Infinity)return 0;
   const factor=Math.exp(-x+a*Math.log(x)-logGamma(a)),eps=2e-14,
     tiny=1e-300,iterations=700;
   let value;
   if(x<a+1){
     let sum=1/a,del=sum,ap=a;
     for(let j=1;j<=iterations;j++){
       ap+=1;del*=x/ap;sum+=del;
       if(Math.abs(del)<=Math.abs(sum)*eps)break;
     }
     value=1-sum*factor;
   }else{
     let b=x+1-a,c=1/tiny,d=1/b,h=d;
     for(let j=1;j<=iterations;j++){
       const an=-j*(j-a);b+=2;
       d=an*d+b;if(Math.abs(d)<tiny)d=tiny;
       c=b+an/c;if(Math.abs(c)<tiny)c=tiny;
       d=1/d;const mult=d*c;h*=mult;
       if(Math.abs(mult-1)<eps)break;
     }
     value=factor*h;
   }
   return Math.max(0,Math.min(1,value));
 }
 function compute(rows){
   if(!Array.isArray(rows)||rows.length<2||rows.length>5||!Array.isArray(rows[0]))return null;
   const R=rows.length,C=rows[0].length;
   if(C<2||C>5||rows.some(row=>!Array.isArray(row)||row.length!==C||
      row.some(x=>!Number.isSafeInteger(x)||x<0||x>10000000)))return null;
   const rowTotals=rows.map(row=>row.reduce((a,b)=>a+b,0));
   const colTotals=Array.from({length:C},(_,j)=>rows.reduce((s,row)=>s+row[j],0));
   const total=rowTotals.reduce((a,b)=>a+b,0);
   // A zero marginal gives zero expected values and an invalid division.
   if(total===0||rowTotals.some(x=>x===0)||colTotals.some(x=>x===0))return null;
   const expected=rows.map((row,i)=>row.map((_,j)=>rowTotals[i]*colTotals[j]/total));
   const contrib=rows.map((row,i)=>row.map((x,j)=>(x-expected[i][j])**2/expected[i][j]));
   const chi=contrib.reduce((s,row)=>s+row.reduce((a,b)=>a+b,0),0);
   const df=(R-1)*(C-1),p=gammaQ(df/2,chi/2);
   const percentages=rows.map((row,i)=>row.map(x=>100*x/rowTotals[i]));
   const minExpected=Math.min(...expected.flat());
   return {R,C,rows,expected,contrib,rowTotals,colTotals,total,chi,df,p,
     percentages,minExpected,smallExpected:minExpected<5};
 }
 window.esaHomogeneityMath={compute,gammaQ};
 const input=byId("input"),output=byId("results"),error=byId("error");
 const presets={
  cities:"40, 35, 25\n30, 45, 25\n50, 30, 20",
  balanced:"10, 10\n10, 10",
  unequal:"5, 20, 15\n8, 10, 12",
  sparse:"0, 10\n8, 12"
 };
 const SVG="http://www.w3.org/2000/svg";
 const node=(tag,attrs,text)=>{
  const el=document.createElementNS(SVG,tag);
  for(const [name,value] of Object.entries(attrs||{}))el.setAttribute(name,String(value));
  if(text!==undefined)el.textContent=String(text);
  return el;
 };
 const fmt=x=>Number.isFinite(x)?x.toFixed(6):"Undefined";
 function parse(text){
  const lines=text.trim().split(/\n|;/).map(s=>s.trim()).filter(Boolean);
  if(lines.length<2||lines.length>5)return null;
  const rows=lines.map(line=>line.split(",").map(x=>x.trim()));
  if(rows.some(row=>row.length<2||row.length>5||
     row.some(t=>!/^(?:0|[1-9]\d*)$/.test(t))))return null;
  const nums=rows.map(row=>row.map(Number));
  if(nums.some(row=>row.length!==nums[0].length||
       row.some(n=>!Number.isSafeInteger(n)||n>10000000)))return null;
  return nums;
 }
 function chart(stats){
   const graph=byId("chart"),r=stats.R,c=stats.C;
   graph.replaceChildren(
     node("title",{},"Within-group category percentages"),
     node("desc",{},"Bars compare category proportions within each population rather than raw group counts."),
     node("line",{x1:46,y1:172,x2:580,y2:172,stroke:"currentColor"}),
     node("line",{x1:46,y1:20,x2:46,y2:172,stroke:"currentColor"}),
     node("text",{x:8,y:19,fill:"currentColor","font-size":12},"100%"),
     node("text",{x:24,y:175,fill:"currentColor","font-size":12},"0")
   );
   const step=520/c,gap=4,barWidth=Math.max(7,Math.min(24,(step-14)/r));
   const colors=["#0f766e","#64748b","#7c3aed","#d97706","#0284c7"];
   for(let j=0;j<c;j++){
     const center=52+step*(j+.5);
     for(let i=0;i<r;i++){
       const v=stats.percentages[i][j],height=v*1.5;
       const x=center+(i-(r-1)/2)*(barWidth+gap);
       graph.appendChild(node("rect",{x:x-barWidth/2,y:172-height,width:barWidth,
         height,fill:colors[i]}));
     }
     graph.appendChild(node("text",{x:center,y:193,fill:"currentColor",
       "text-anchor":"middle","font-size":11},"Category "+(j+1)));
   }
   graph.setAttribute("aria-label",stats.percentages.map((row,i)=>
     "Population "+(i+1)+": "+row.map((x,j)=>"category "+(j+1)+" "+x.toFixed(1)+" percent").join(", ")
   ).join("; "));
 }
 function render(){
   const matrix=parse(input.value),s=matrix?compute(matrix):null;
   if(!s){
     error.textContent="Enter a rectangular 2–5 by 2–5 table: each row is a population, with nonnegative integer counts (up to 10,000,000), separated by commas. Row and column totals must be positive.";
     error.hidden=false;output.hidden=true;byId("chart").replaceChildren();
     return;
   }
   error.hidden=true;output.hidden=false;
   const grid=byId("table");
   grid.replaceChildren();
   const header=document.createElement("tr");
   for(const val of ["Population",...Array.from({length:s.C},(_,j)=>"Category "+(j+1)),"Row total"]){
     const th=document.createElement("th");th.scope="col";th.textContent=val;header.appendChild(th);
   }
   const thead=document.createElement("thead");thead.appendChild(header);grid.appendChild(thead);
   const tbody=document.createElement("tbody");
   for(let i=0;i<s.R;i++){
     const tr=document.createElement("tr"),th=document.createElement("th");
     th.scope="row";th.textContent="Population "+(i+1);tr.appendChild(th);
     for(let j=0;j<s.C;j++){
       const td=document.createElement("td");
       td.textContent="O "+s.rows[i][j]+"; E "+s.expected[i][j].toFixed(3)+
         "; χ² contribution "+s.contrib[i][j].toFixed(3)+
         "; within-group "+s.percentages[i][j].toFixed(1)+"%";
       tr.appendChild(td);
     }
     const total=document.createElement("td");total.textContent=String(s.rowTotals[i]);tr.appendChild(total);
     tbody.appendChild(tr);
   }
   grid.appendChild(tbody);
   const foot=document.createElement("tr");
   const title=document.createElement("th");title.scope="row";title.textContent="Column totals";foot.appendChild(title);
   for(const x of [...s.colTotals,s.total]){
     const td=document.createElement("td");td.textContent=String(x);foot.appendChild(td);
   }
   const tfoot=document.createElement("tfoot");tfoot.appendChild(foot);grid.appendChild(tfoot);
   for(const [key,value] of Object.entries({chi:fmt(s.chi),df:String(s.df),
      p:fmt(s.p),n:String(s.total)}))byId(key).textContent=value;
   byId("warning").textContent=s.smallExpected?
     "Warning: some expected counts are below 5 (minimum "+s.minExpected.toFixed(3)+
     "). The asymptotic chi-square p-value may be unreliable; consider an appropriate exact/Monte Carlo method or obtain more data.":
     "All expected counts are at least 5. The test still assumes independent observations across independently sampled populations.";
   byId("decision").textContent=s.p<.05?
     "At α = 0.05, reject the hypothesis of equal category distributions if sampling and approximation assumptions hold. This does not establish causality or specify every differing group.":
     "At α = 0.05, do not reject equal category distributions. This is not proof that populations have identical distributions.";
   chart(s);
 }
 input.addEventListener("input",render);
 for(const [name,data] of Object.entries(presets)){
   byId(name).addEventListener("click",()=>{input.value=data;render();});
 }
 render();
})();