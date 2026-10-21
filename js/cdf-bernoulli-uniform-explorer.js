/* Batch #63: exact Bernoulli and uniform CDFs and interval probabilities. */
(function(){
  "use strict";
  const root=document.getElementById("esa-cdf-explorer");
  if(!root)return;
  const byId=id=>document.getElementById(id);
  const distribution=byId("esa-cdf-kind"),pControl=byId("esa-cdf-p"),
    aControl=byId("esa-cdf-a"),bControl=byId("esa-cdf-b"),
    xControl=byId("esa-cdf-x"),left=byId("esa-cdf-left"),right=byId("esa-cdf-right"),
    error=byId("esa-cdf-error"),panel=byId("esa-cdf-results"),plot=byId("esa-cdf-chart");
  const ns="http://www.w3.org/2000/svg";
  function cdf(kind,x,p,a,b){
    if(!Number.isFinite(x))return null;
    if(kind==="bernoulli"){
      if(!Number.isFinite(p)||p<0||p>1)return null;
      return x<0?0:x<1?1-p:1;
    }
    if(kind==="uniform"){
      if(!Number.isFinite(a)||!Number.isFinite(b)||!(a<b))return null;
      return x<=a?0:x>=b?1:(x-a)/(b-a);
    }
    return null;
  }
  function interval(kind,L,R,p,a,b){
    if(!Number.isFinite(L)||!Number.isFinite(R)||!(L<R))return null;
    const low=cdf(kind,L,p,a,b),high=cdf(kind,R,p,a,b);
    return low===null||high===null?null:Math.max(0,Math.min(1,high-low));
  }
  // Exposed pure mathematical kernels allow independent test benchmarks.
  window.esaCdfMath={cdf,interval};
  const node=(tag,attrs,content)=>{
    const item=document.createElementNS(ns,tag);
    Object.entries(attrs||{}).forEach(([k,v])=>item.setAttribute(k,String(v)));
    if(content!==undefined)item.textContent=content;
    return item;
  };
  const X=x=>45+(x+1.5)*68.5;
  const Y=y=>194-y*153;
  function plotLine(pts,color,width=3,style){
    const attrs={points:pts.map(pt=>X(pt[0])+","+Y(pt[1])).join(" "),
      fill:"none",stroke:color,"stroke-width":width,"stroke-linecap":"round","stroke-linejoin":"round"};
    if(style)attrs["stroke-dasharray"]=style;
    plot.appendChild(node("polyline",attrs));
  }
  function point(x,y,filled,color){
    plot.appendChild(node("circle",{cx:X(x),cy:Y(y),r:4.5,
      fill:filled?color:"var(--surface)",stroke:color,"stroke-width":2}));
  }
  function draw(kind,p,a,b,x){
    const color="#2563eb",contrast="#0f766e";
    plot.replaceChildren(
      node("title",{},"Cumulative distribution function graph"),
      node("desc",{},"The CDF is nondecreasing and ranges between zero and one. Bernoulli has jumps at zero and one. Uniform is continuous."),
      node("line",{x1:X(-1.5),y1:Y(0),x2:X(3.5),y2:Y(0),stroke:"currentColor","stroke-width":1.2}),
      node("line",{x1:X(-1.5),y1:Y(0),x2:X(-1.5),y2:Y(1.08),stroke:"currentColor","stroke-width":1.2}),
      node("text",{x:X(-1.5),y:Y(1)+3,"font-size":11,fill:"currentColor"},"1"),
      node("text",{x:X(3.5)-7,y:Y(0)+19,"font-size":11,fill:"currentColor"},"x"),
      node("text",{x:X(-1.5)+3,y:Y(1.08)-5,"font-size":11,fill:"currentColor"},"F(x)")
    );
    for(const tick of [-1,0,1,2,3]){
      plot.appendChild(node("text",{x:X(tick),y:Y(0)+18,"font-size":10,"text-anchor":"middle",fill:"currentColor"},tick));
    }
    if(kind==="bernoulli"){
      plotLine([[-1.5,0],[0,0]],color);
      plotLine([[0,1-p],[1,1-p]],color);
      plotLine([[1,1],[3.5,1]],color);
      plotLine([[0,0],[0,1-p]],color,1.5,"4 3");
      plotLine([[1,1-p],[1,1]],color,1.5,"4 3");
      point(0,0,false,color);point(0,1-p,true,color);
      point(1,1-p,false,color);point(1,1,true,color);
    }else{
      plotLine([[-1.5,0],[a,0],[b,1],[3.5,1]],color);
    }
    const f=cdf(kind,x,p,a,b);
    plot.appendChild(node("line",{x1:X(x),y1:Y(0),x2:X(x),y2:Y(f),stroke:contrast,"stroke-width":2,"stroke-dasharray":"4 3"}));
    point(x,f,true,contrast);
    plot.setAttribute("aria-label",(kind==="bernoulli"?"Bernoulli CDF with p="+p:
      "Uniform CDF from "+a+" to "+b)+", F("+x+") = "+f.toFixed(6));
  }
  const fmt=n=>n.toFixed(6);
  function render(){
    const kind=distribution.value, p=Number(pControl.value),
      a=Number(aControl.value),b=Number(bControl.value),x=Number(xControl.value),
      L=Number(left.value),R=Number(right.value);
    root.querySelector("#esa-cdf-bernoulli-options").hidden=kind!=="bernoulli";
    root.querySelector("#esa-cdf-uniform-options").hidden=kind!=="uniform";
    byId("esa-cdf-p-label").textContent=p.toFixed(2);
    byId("esa-cdf-a-label").textContent=a.toFixed(1);
    byId("esa-cdf-b-label").textContent=b.toFixed(1);
    byId("esa-cdf-x-label").textContent=x.toFixed(2);
    const invalidBounds=kind==="uniform"&&!(a<b);
    const invalidInterval=left.value.trim()===""||right.value.trim()===""||
      !Number.isFinite(L)||!Number.isFinite(R)||L>=R;
    const f=cdf(kind,x,p,a,b),value=interval(kind,L,R,p,a,b);
    if(invalidBounds||invalidInterval||f===null||value===null){
      error.textContent=invalidBounds?"Uniform endpoints must satisfy a < b.":
        "Enter finite interval bounds L < R.";
      error.hidden=false;panel.hidden=true;plot.replaceChildren();
      return;
    }
    error.hidden=true;panel.hidden=false;
    byId("esa-cdf-fx").textContent=fmt(f);
    byId("esa-cdf-interval").textContent=fmt(value);
    byId("esa-cdf-description").textContent=kind==="bernoulli"
      ?"Bernoulli CDF jumps by 1−p at x=0 and by p at x=1. Filled dots include the jump value; hollow dots exclude the left limit."
      :"For Uniform[a,b], the CDF increases linearly from zero at a to one at b. Single points have probability zero.";
    draw(kind,p,a,b,x);
  }
  for(const item of [distribution,pControl,aControl,bControl,xControl,left,right]){
    item.addEventListener(item===distribution?"change":"input",render);
  }
  byId("esa-cdf-reset").addEventListener("click",()=>{
    distribution.value="bernoulli";pControl.value="0.35";aControl.value="0";bControl.value="2";
    xControl.value="0.5";left.value="0";right.value="1";render();
  });
  render();
})();