/* Batch #62: explain how one unusual observation changes Pearson correlation. */
(function () {
  "use strict";
  const root = document.getElementById("esa-scatter-correlation-lab");
  if (!root) return;
  const NS = "http://www.w3.org/2000/svg";
  const original = [[1,2],[2,3],[3,4],[4,6],[5,7],[6,8]];
  const fieldX = document.getElementById("esa-scatter-outlier-x");
  const fieldY = document.getElementById("esa-scatter-outlier-y");
  const include = document.getElementById("esa-scatter-include");
  const error = document.getElementById("esa-scatter-error");
  const status = document.getElementById("esa-scatter-status");
  const baseline = document.getElementById("esa-scatter-base-r");
  const changed = document.getElementById("esa-scatter-new-r");
  const difference = document.getElementById("esa-scatter-change-r");
  const chartBase = document.getElementById("esa-scatter-base-svg");
  const chartNew = document.getElementById("esa-scatter-new-svg");

  function pearson(pairs) {
    if (!Array.isArray(pairs) || pairs.length < 2 ||
        pairs.some(p => !Array.isArray(p) || p.length !== 2 ||
          !Number.isFinite(p[0]) || !Number.isFinite(p[1]))) return null;
    const n = pairs.length;
    const avgX = pairs.reduce((a,p)=>a+p[0],0)/n;
    const avgY = pairs.reduce((a,p)=>a+p[1],0)/n;
    let xx=0, yy=0, xy=0;
    pairs.forEach(p => {
      const dx=p[0]-avgX, dy=p[1]-avgY;
      xx+=dx*dx; yy+=dy*dy; xy+=dx*dy;
    });
    if (!(xx>0) || !(yy>0)) return null;
    return Math.max(-1,Math.min(1,xy/Math.sqrt(xx*yy)));
  }
  // Pure function also permits independent browser tests of degenerate cases.
  window.esaScatterPearson = pearson;
  const r0=pearson(original);
  const format = x => x===null ? "Undefined" : x.toFixed(4);
  baseline.textContent=format(r0);

  function svgNode(name,attrs,text) {
    const node=document.createElementNS(NS,name);
    Object.keys(attrs||{}).forEach(k=>node.setAttribute(k,String(attrs[k])));
    if (text!==undefined) node.textContent=text;
    return node;
  }
  function chart(svg,points,highlight,description) {
    const xs=points.map(p=>p[0]), ys=points.map(p=>p[1]);
    let xmin=Math.min(...xs),xmax=Math.max(...xs),ymin=Math.min(...ys),ymax=Math.max(...ys);
    const xp=Math.max(0.5,(xmax-xmin)*0.12),yp=Math.max(0.5,(ymax-ymin)*0.12);
    xmin-=xp; xmax+=xp;ymin-=yp;ymax+=yp;
    const X=x=>44+(x-xmin)/(xmax-xmin)*321;
    const Y=y=>202-(y-ymin)/(ymax-ymin)*165;
    svg.setAttribute("viewBox","0 0 400 240");
    svg.setAttribute("role","img");
    svg.setAttribute("aria-label",description);
    svg.replaceChildren(
      svgNode("title",{},description),
      svgNode("desc",{},"Horizontal axis: x; vertical axis: y. Exact correlations are shown in the text."),
      svgNode("line",{x1:44,y1:202,x2:365,y2:202,stroke:"currentColor","stroke-width":1.5}),
      svgNode("line",{x1:44,y1:202,x2:44,y2:25,stroke:"currentColor","stroke-width":1.5}),
      svgNode("text",{x:377,y:206,"font-size":13,fill:"currentColor"},"x"),
      svgNode("text",{x:29,y:20,"font-size":13,fill:"currentColor"},"y"),
      svgNode("text",{x:44,y:225,"font-size":11,fill:"currentColor"},xmin.toFixed(1)),
      svgNode("text",{x:339,y:225,"font-size":11,fill:"currentColor"},xmax.toFixed(1))
    );
    points.forEach((p,i)=>{
      svg.appendChild(svgNode("circle",{
        cx:X(p[0]),cy:Y(p[1]),r:highlight&&i===points.length-1?6.5:5,
        fill:highlight&&i===points.length-1?"#b45309":"#215fc7",
        stroke:highlight&&i===points.length-1?"#7c2d12":"#173b7a",
        "stroke-width":1
      }));
    });
  }
  function render() {
    const x=Number(fieldX.value),y=Number(fieldY.value);
    const validX=fieldX.value.trim()!==""&&Number.isFinite(x)&&x>=-20&&x<=20;
    const validY=fieldY.value.trim()!==""&&Number.isFinite(y)&&y>=-20&&y<=20;
    const valid=validX&&validY;
    chart(chartBase,original,false,"Original scatterplot of six observations");
    const withPoint=include.checked;
    fieldX.disabled=!withPoint;fieldY.disabled=!withPoint;
    if (withPoint&&!valid) {
      error.textContent="Enter finite x and y values between −20 and 20.";
      error.hidden=false;status.hidden=true;
      changed.textContent="—";difference.textContent="—";
      chart(chartNew,original,false,"Original points; invalid added observation not plotted");
      return;
    }
    error.hidden=true;status.hidden=false;
    const points=withPoint?original.concat([[x,y]]):original;
    const r=pearson(points);
    chart(chartNew,points,withPoint,
      withPoint?"Scatterplot with an additional point at x="+x+", y="+y:"Scatterplot without an additional point");
    changed.textContent=format(r);
    difference.textContent=r===null?"Undefined":(r-r0).toFixed(4);
    status.textContent=withPoint
      ?"The highlighted point ("+x+", "+y+") changes Pearson r from "+
       format(r0)+" to "+format(r)+". Correlation describes linear association, not causation."
      :"The extra point is removed; the two datasets and correlations now match.";
  }
  [fieldX,fieldY].forEach(node=>node.addEventListener("input",render));
  include.addEventListener("change",render);
  document.getElementById("esa-scatter-reset").addEventListener("click",()=>{
    fieldX.value="7";fieldY.value="0";include.checked=true;render();
  });
  render();
})();