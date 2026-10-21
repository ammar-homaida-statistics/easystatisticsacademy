/* Easy Statistics Academy — identical-data axis-baseline comparison. */
(() => {
  "use strict";
  const root = document.getElementById("esa-truncated-axis-lab");
  if (!root) return;
  const $ = id => document.getElementById("esa-axis-" + id);
  const aInput = $("a"), bInput = $("b"), baselineInput = $("baseline");
  const error = $("error"), results = $("result");
  const diff = $("difference"), percent = $("relative"), apparent = $("apparent");
  const zeroSvg = $("zero-chart"), truncatedSvg = $("truncated-chart");
  const namespace = "http://www.w3.org/2000/svg";
  function element(type,attrs,text) {
    const node = document.createElementNS(namespace,type);
    for (const [key,value] of Object.entries(attrs)) node.setAttribute(key,String(value));
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function chart(svg, a, b, baseline, title) {
    svg.replaceChildren();
    svg.setAttribute("viewBox","0 0 300 208");
    svg.setAttribute("role","img");
    svg.setAttribute("aria-label",title+"; A = "+a+", B = "+b+", baseline = "+baseline);
    const upper=Math.max(a,b);
    const extent=upper-baseline || 1;
    const plotTop=30, plotBottom=168, h=plotBottom-plotTop;
    svg.append(element("line",{x1:35,y1:plotBottom,x2:284,y2:plotBottom,stroke:"currentColor","stroke-width":1.5}));
    svg.append(element("line",{x1:35,y1:plotTop,x2:35,y2:plotBottom,stroke:"currentColor","stroke-width":1.5}));
    svg.append(element("text",{x:30,y:plotTop+5,"text-anchor":"end","font-size":12,fill:"currentColor"},String(upper)));
    svg.append(element("text",{x:30,y:plotBottom+4,"text-anchor":"end","font-size":12,fill:"currentColor"},String(baseline)));
    [[a,90,"#3174ad","A"],[b,202,"#dd8a2c","B"]].forEach(([v,x,color,label]) => {
      const height=Math.max(0,((v-baseline)/extent)*h);
      svg.append(element("rect",{x,y:plotBottom-height,width:58,height,fill:color}));
      svg.append(element("text",{x:x+29,y:plotBottom+22,"text-anchor":"middle","font-size":13,fill:"currentColor"},label));
      svg.append(element("text",{x:x+29,y:Math.max(15,plotBottom-height-8),"text-anchor":"middle","font-size":12,fill:"currentColor"},String(v)));
    });
  }
  function clear() {
    [diff,percent,apparent].forEach(e=>e.textContent="—");
    [zeroSvg,truncatedSvg].forEach(s=>s.replaceChildren());
    results.hidden=true;
  }
  function update() {
    const a=Number(aInput.value), b=Number(bInput.value), lower=Number(baselineInput.value);
    const finite=[a,b,lower].every(Number.isFinite);
    if (!finite || [aInput,bInput,baselineInput].some(e=>!e.value.trim()) ||
        a<0 || b<0 || a>1000 || b>1000 || lower<0 || lower>=Math.min(a,b) && lower!==0 ||
        (lower===0 && Math.min(a,b)===0 && Math.max(a,b)===0 && a!==b) ||
        (lower>0 && (a<=lower || b<=lower))) {
      error.textContent="Enter values A and B between 0 and 1,000 and an axis start of 0 or a nonnegative number strictly smaller than both values.";
      error.hidden=false;
      clear();
      return;
    }
    error.hidden=true;
    error.textContent="";
    const absolute=Math.abs(a-b);
    const relative=Math.min(a,b)>0 ? absolute/Math.min(a,b)*100 : null;
    const ratio = Math.min(a,b)-lower > 0 ? (Math.max(a,b)-lower)/(Math.min(a,b)-lower) : null;
    diff.textContent=absolute.toLocaleString("en-US",{maximumFractionDigits:6});
    percent.textContent=relative === null ? "Undefined (the smaller value is zero)" : relative.toFixed(2)+"%";
    apparent.textContent=ratio===null ? "Undefined" : ratio.toFixed(2)+"×";
    chart(zeroSvg,a,b,0,"Zero-baseline bar chart");
    chart(truncatedSvg,a,b,lower,"Truncated-axis bar chart");
    results.hidden=false;
  }
  root.addEventListener("input",update);
  $("reset").addEventListener("click",() => {
    aInput.value="95";bInput.value="100";baselineInput.value="90";update();
  });
  update();
})();