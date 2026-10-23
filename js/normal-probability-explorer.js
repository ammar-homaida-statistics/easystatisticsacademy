/* Shared English/Arabic normal probability explorer; preserves established numeric method. */

    (function () {
      "use strict";
      const root=document.getElementById("esa-normal-probability-explorer");if(!root)return;
      const arabic=document.documentElement.lang==="ar";
      const el=id=>root.querySelector("#esa-normal-"+id);
      const inputs=["mu","sigma","a","b"].map(el),mode=el("mode");
      const erfcPos=x=>{
        const t=1/(1+0.3275911*x);
        return t*(0.254829592+t*(-0.284496736+
          t*(1.421413741+t*(-1.453152027+t*1.061405429))))*Math.exp(-x*x);
      };
      const cdf=z=>z<0?0.5*erfcPos(-z/Math.SQRT2):1-0.5*erfcPos(z/Math.SQRT2);
      const survival=z=>z>=0?0.5*erfcPos(z/Math.SQRT2):1-0.5*erfcPos(-z/Math.SQRT2);
      window.esaNormalMath={cdf,survival};
      const sx=z=>34+(z+4)*370/8;
      const sy=z=>200-145*Math.exp(-z*z/2);
      const path=(lo,hi)=> {
        if(hi<=lo)return "";
        const count=Math.max(1,Math.ceil((hi-lo)/0.05));
        let d="M "+sx(lo).toFixed(2)+" 200";
        for(let i=0;i<=count;i++) {
          const z=lo+(hi-lo)*i/count;
          d+=" L "+sx(z).toFixed(2)+" "+sy(z).toFixed(2);
        }
        return d+" L "+sx(hi).toFixed(2)+" 200 Z";
      };
      const density=()=>{
        let d="";
        for(let i=0;i<=160;i++){
          const z=-4+8*i/160;
          d+=(i?" L ":"M ")+sx(z).toFixed(2)+" "+sy(z).toFixed(2);
        }
        return d;
      };
      el("density").setAttribute("d",density());
      function invalid(message){
        el("error").textContent=message;el("error").hidden=false;
        el("chart").setAttribute("hidden","");
        ["za","zb","probability","percent"].forEach(id=>el(id).textContent="—");
      }
      function update(){
        const [mu,sigma,a,b]=inputs.map(i=>i.value.trim()===""?NaN:Number(i.value));
        if([mu,sigma,a,b].some(v=>!Number.isFinite(v)||Math.abs(v)>100000)||sigma<=0||sigma<0.000001||sigma>10000||
           (mode.value==="between"&&a>=b)){
          invalid(arabic?"أدخل قيماً محدودة، وانحرافاً معيارياً بين 0.000001 و10000، ويجب أن يكون a أصغر من b عند حساب احتمال الفترة.":"Enter finite values, σ between 0.000001 and 10,000, and a below b for the between-bounds region.");
          return;
        }
        const za=(a-mu)/sigma,zb=(b-mu)/sigma;
        if(!Number.isFinite(za)||!Number.isFinite(zb)){invalid(arabic?"تجاوزت الحدود المعيارية المجال العددي المدعوم.":"The standardized limits exceed the supported numeric range.");return;}
        let p,label,from,to;
        if(mode.value==="left"){p=cdf(za);label="P(X ≤ a)";from=-4;to=za;}
        else if(mode.value==="right"){p=survival(zb);label="P(X ≥ b)";from=zb;to=4;}
        else {
          p=za>=0?survival(za)-survival(zb):zb<=0?cdf(zb)-cdf(za):cdf(zb)-cdf(za);
          label="P(a ≤ X ≤ b)";from=za;to=zb;
        }
        p=Math.max(0,Math.min(1,p));
        el("error").hidden=true;el("error").textContent="";el("chart").removeAttribute("hidden");
        el("za").textContent=za.toFixed(4);el("zb").textContent=zb.toFixed(4);
        el("prob-label").textContent=label;
        el("probability").textContent=p<0.0000005?"< 0.000001":p.toFixed(6);
        el("percent").textContent=p<0.0000005?"< 0.0001":(100*p).toFixed(4);
        const l=Math.max(-4,from),h=Math.min(4,to);
        el("shade").setAttribute("d",path(l,h));
        const aLine=el("bound-a"),bLine=el("bound-b");
        if(za>=-4&&za<=4)aLine.removeAttribute("hidden");else aLine.setAttribute("hidden","");
        if(zb>=-4&&zb<=4)bLine.removeAttribute("hidden");else bLine.setAttribute("hidden","");
        aLine.setAttribute("x1",sx(za));aLine.setAttribute("x2",sx(za));
        bLine.setAttribute("x1",sx(zb));bLine.setAttribute("x2",sx(zb));
        el("warning").textContent=(arabic?"يعرض الرسم المجال μ ± 4σ فقط، بينما يدخل ذيلا التوزيع الكامل في الحساب.":"The graph shows μ ± 4σ only. The probability includes all unbounded normal tails")+
          (from < -4 || to>4?(arabic?" الحدود المختارة تتجاوز المجال المرئي.":"; selected bounds extend beyond the visible graph."):(arabic?"":"."));
        el("chart").setAttribute("aria-label",(arabic?"توزيع طبيعي بمتوسط ":"Normal model with mean ")+mu+
          (arabic?" وانحراف معياري ":" and standard deviation ")+sigma+". "+label+" = "+p.toFixed(6)+
          (arabic?". المساحة المظللة مقصوصة عند μ ± 4σ.":". Shaded area is clipped to μ ± 4σ."));
      }
      [...inputs,mode].forEach(i=>{i.addEventListener("input",update);i.addEventListener("change",update)});
      el("reset").addEventListener("click",()=>{
        [0,1,-1,1].forEach((v,i)=>inputs[i].value=String(v));
        mode.value="between";update();
      });
      update();
    })();
    