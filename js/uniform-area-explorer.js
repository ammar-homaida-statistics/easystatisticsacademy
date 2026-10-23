/* Shared English and Arabic continuous Uniform probability-area explorer. */
(function () {
      "use strict";
      const root=document.getElementById("esa-uniform-area-explorer");
      if (!root) return;
      const arabic=document.documentElement.lang==="ar";
      const el=id=>root.querySelector("#"+id);
      const a=el("esa-uniform-a"),b=el("esa-uniform-b"),
            c=el("esa-uniform-c"),d=el("esa-uniform-d");
      const clamp=(value,low,high)=>Math.max(low,Math.min(high,value));
      function bound(input,low,high,value) {
        input.min=String(low);input.max=String(high);
        input.value=String(clamp(value,low,high));
      }
      function calculate(A,B,C,D) {
        if(![A,B,C,D].every(Number.isFinite) || !(A<B) || C<A || D>B || C>D)return null;
        const span=B-A, interval=D-C, density=1/span;
        return {density,probability:interval/span,mean:(A+B)/2,
          variance:span*span/12,sd:span/Math.sqrt(12)};
      }
      window.esaUniformMath={calculate};
      function update(source) {
        // Change the dependent range bounds before assigning values; native
        // sliders otherwise clamp against stale limits when presets change.
        if (source===b) {
          const upper=Number(b.value);
          bound(a,0,Math.min(9,upper-1),Number(a.value));
        } else {
          const lower=Number(a.value);
          bound(b,lower+1,20,Number(b.value));
        }
        const A=Number(a.value),B=Number(b.value);
        const C=clamp(Number(c.value),A,B);
        bound(c,A,B,C);
        const D=clamp(Number(d.value),Number(c.value),B);
        bound(d,Number(c.value),B,D);
        const from=Number(c.value),to=Number(d.value);
        const span=B-A,interval=to-from;
        const density=1/span,probability=interval/span;
        const mean=(A+B)/2,variance=span*span/12;
        for(const [key,v] of [
          ["esa-uniform-a-value",A],["esa-uniform-b-value",B],
          ["esa-uniform-c-value",from],["esa-uniform-d-value",to]
        ])el(key).textContent=String(v);
        el("esa-uniform-interval").textContent="["+from+", "+to+"]";
        el("esa-uniform-width").textContent=interval.toFixed(2);
        el("esa-uniform-density").textContent=density.toFixed(4);
        el("esa-uniform-probability").textContent=probability.toFixed(4);
        el("esa-uniform-mean").textContent=mean.toFixed(2);
        el("esa-uniform-variance").textContent=variance.toFixed(4);
        el("esa-uniform-sd").textContent=Math.sqrt(variance).toFixed(4);
        const offset=280*(from-A)/span;
        el("esa-uniform-highlight").setAttribute("x",String(50+offset));
        el("esa-uniform-highlight").setAttribute("width",String(280*probability));
        el("esa-uniform-left-label").textContent=String(A);
        el("esa-uniform-right-label").textContent=String(B);
        el("esa-uniform-area-plot").setAttribute("aria-label",
          arabic ? ("كثافة التوزيع المنتظم من "+A+" إلى "+B+
            "؛ احتمال الفترة من "+from+" إلى "+to+" يساوي "+probability.toFixed(4)) :
            ("Uniform density from "+A+" to "+B+"; shaded probability between "+
             from+" and "+to+" equals "+probability.toFixed(4)));
      }
      [a,b,c,d].forEach(input=>input.addEventListener("input",()=>update(input)));
      el("esa-uniform-reset").addEventListener("click",()=>{
        a.value="0";b.value="10";
        // Reset dependent bounds before restoring the original interval.
        update(a);
        c.value="2";update(c);
        d.value="5";update(d);
      });
      update(a);
    })();
