/* Cook's Distance and leave-one-out simple-regression explorer.
   Small fixed x,y dataset; one editable observation. No remote dependencies. */
(function () {
  "use strict";
  if (!document.getElementById("esa-cook-lab")) return;
  const fixed = [[1,2.3],[2,3.7],[3,6.0],[4,7.8],[5,10.3],[6,11.9],[7,13.8]];
  const $ = id => document.getElementById(id);
  const xInput = $("esa-cook-x"), yInput = $("esa-cook-y");
  const svg = $("esa-cook-chart"), rows = $("esa-cook-table"), status = $("esa-cook-status");
  const ns = "http://www.w3.org/2000/svg";
  function node(name, attrs, text) {
    const e = document.createElementNS(ns, name);
    Object.entries(attrs).forEach(([k, v]) => e.setAttribute(k, String(v)));
    if (text !== undefined) e.textContent = text;
    svg.appendChild(e);
    return e;
  }
  function fit(data) {
    const n = data.length;
    const mx = data.reduce((s, z) => s + z[0], 0) / n;
    const my = data.reduce((s, z) => s + z[1], 0) / n;
    const sxx = data.reduce((s, z) => s + (z[0] - mx) ** 2, 0);
    const sxy = data.reduce((s, z) => s + (z[0] - mx) * (z[1] - my), 0);
    if (sxx < 1e-12 || n <= 2) throw Error("Insufficient x-variation or observations.");
    const slope = sxy / sxx, intercept = my - slope * mx;
    const residuals = data.map(z => z[1] - intercept - slope * z[0]);
    const sse = residuals.reduce((s, e) => s + e * e, 0);
    const mse = sse / (n - 2);
    const leverage = data.map(z => 1 / n + (z[0] - mx) ** 2 / sxx);
    return {intercept,slope,residuals,sse,mse,leverage};
  }
  function predicted(f, x) { return f.intercept + f.slope * x; }
  function cookValues(data, full) {
    const p = 2, n = data.length;
    return data.map((z, i) => {
      const h = full.leverage[i], e = full.residuals[i];
      // Exact Cook's D for ordinary least squares with intercept;
      // residual mean square is from the FULL model, with n-p degrees of freedom.
      const expression = full.mse > 1e-12 && h < 1 - 1e-12
        ? (e * e / (p * full.mse)) * h / ((1-h)*(1-h)) : 0;
      const loo = fit(data.filter((_, j) => i !== j));
      const change = data.reduce((s, point) => {
        const delta = predicted(full, point[0]) - predicted(loo, point[0]);
        return s + delta * delta;
      }, 0);
      const direct = full.mse > 1e-12 ? change / (p * full.mse) : 0;
      if (Math.abs(expression - direct) > 1e-6 * Math.max(1, expression))
        throw Error("Cook's Distance consistency check failed.");
      return {expression, loo, residual:e, leverage:h};
    });
  }
  function chart(data, full, without) {
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    const xlo = 0.5, xhi = 16;
    const ys = data.map(z=>z[1]);
    for (const fit of [full, without]) {
      ys.push(predicted(fit, xlo), predicted(fit, xhi));
    }
    const ymin = Math.min(...ys) - 3, ymax = Math.max(...ys) + 3;
    const X = x => 40 + (x-xlo)/(xhi-xlo)*605;
    const Y = y => 258 - (y-ymin)/(ymax-ymin)*226;
    node("line",{x1:40,y1:258,x2:650,y2:258,stroke:"currentColor"});
    const line=(fit,color,dashed) => {
      const attrs={x1:X(xlo),y1:Y(predicted(fit,xlo)),x2:X(xhi),y2:Y(predicted(fit,xhi)),
        stroke:color,"stroke-width":2.5, "data-series":dashed?"leave-one-out":"full"};
      if(dashed)attrs["stroke-dasharray"]="8 5";
      node("line",attrs);
    };
    line(full,"#0f766e",false);
    line(without,"#ea580c",true);
    data.forEach(([x,y],i)=>{
      if(i===data.length-1)node("circle",{cx:X(x),cy:Y(y),r:7,fill:"#b91c1c",id:"esa-cook-selected-point"});
      else node("circle",{cx:X(x),cy:Y(y),r:5,fill:"#2563eb",class:"esa-cook-fixed-point"});
    });
    node("text",{x:48,y:279,fill:"currentColor","font-size":12},"0.5");
    node("text",{x:615,y:279,fill:"currentColor","font-size":12},"16");
    node("text",{x:335,y:291,fill:"currentColor","font-size":12},"x");
  }
  function run() {
    try {
      const x=Number(xInput.value),y=Number(yInput.value);
      if(!Number.isFinite(x)||!Number.isFinite(y)||x<7.5||x>15||y<0||y>35)
        throw Error("Use the available x/y ranges.");
      const data=[...fixed,[x,y]];
      const full=fit(data);
      const cooks=cookValues(data,full),selected=cooks[data.length-1];
      const leave=selected.loo;
      const set=(id,value)=>$(id).textContent=value.toFixed(6);
      $("esa-cook-x-value").textContent=x.toFixed(1);
      $("esa-cook-y-value").textContent=y.toFixed(1);
      set("esa-cook-mse",full.mse);
      set("esa-cook-residual",selected.residual);
      set("esa-cook-leverage",selected.leverage);
      set("esa-cook-d",selected.expression);
      set("esa-cook-full-intercept",full.intercept);
      set("esa-cook-full-slope",full.slope);
      set("esa-cook-leave-intercept",leave.intercept);
      set("esa-cook-leave-slope",leave.slope);
      set("esa-cook-delta-slope",full.slope-leave.slope);
      while(rows.firstChild)rows.removeChild(rows.firstChild);
      cooks.forEach((c,i)=>{
        const tr=document.createElement("tr");
        [String(i+1),c.residual.toFixed(4),c.leverage.toFixed(4),c.expression.toFixed(4)]
          .forEach(t=>{const td=document.createElement("td");td.textContent=t;tr.appendChild(td);});
        rows.appendChild(tr);
      });
      chart(data,full,leave);
      status.textContent="Updated the full model, leave-one-out fit and all eight diagnostics.";
    } catch(error) {
      status.textContent=error.message;
      while(svg.firstChild)svg.removeChild(svg.firstChild);
    }
  }
  xInput.addEventListener("input",run);
  yInput.addEventListener("input",run);
  $("esa-cook-reset").addEventListener("click",()=>{
    xInput.value="9";yInput.value="25";run();
  });
  run();
})();