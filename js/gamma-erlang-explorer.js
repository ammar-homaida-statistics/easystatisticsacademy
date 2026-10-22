/* Gamma/Erlang shared bilingual numerical explorer — Batch #66. */
(function () {
      "use strict";
      const root=document.getElementById("esa-erlang-wait-explorer");
      if (!root) return;
      const isArabic=document.documentElement.lang==="ar";
      const byId=id=>root.querySelector("#"+id);
      const rInput=byId("esa-erlang-r"),rateInput=byId("esa-erlang-rate"),
            timeInput=byId("esa-erlang-time");
      const maxTime=12, xToPx=t=>34+296*t/maxTime;
      function factorial(n){
        let result=1;
        for(let j=2;j<=n;j++)result*=j;
        return result;
      }
      function density(t,r,lambda) {
        if(t<0) return 0;
        if(t===0) return r===1?lambda:0;
        return Math.pow(lambda,r)*Math.pow(t,r-1)*
          Math.exp(-lambda*t)/factorial(r-1);
      }
      function survival(t,r,lambda) {
        if(t<=0)return 1;
        const z=lambda*t;
        let term=1,sum=1;
        for(let j=1;j<r;j++){
          term*=z/j;
          sum+=term;
        }
        return Math.min(1,Math.max(0,Math.exp(-z)*sum));
      }
      function update() {
        const r=Number(rInput.value),lambda=Number(rateInput.value),
              t=Number(timeInput.value);
        const s=survival(t,r,lambda),c=Math.max(0,Math.min(1,1-s)),
              pdf=density(t,r,lambda);
        byId("esa-erlang-r-value").textContent=String(r);
        byId("esa-erlang-rate-value").textContent=lambda.toFixed(2);
        byId("esa-erlang-time-value").textContent=t.toFixed(2);
        byId("esa-erlang-pdf").textContent=pdf.toFixed(5);
        byId("esa-erlang-cdf").textContent=c.toFixed(6);
        byId("esa-erlang-survival").textContent=s.toFixed(6);
        byId("esa-erlang-mean").textContent=(r/lambda).toFixed(4);
        byId("esa-erlang-variance").textContent=(r/(lambda*lambda)).toFixed(4);
        byId("esa-erlang-scale").textContent=(1/lambda).toFixed(4);
        byId("esa-erlang-special").textContent=isArabic?
          (r===1?"الشكل 1 يعيد التوزيع الأسي بمعدل λ.":
            "عند الشكل الصحيح الموجب r = "+r+" ننتظر الحدث رقم r في عملية بواسون المتجانسة."):
          (r===1?"Shape 1 is exactly the Exponential distribution with rate λ.":
            "With positive integer shape r = "+r+
            ", this is waiting for the r-th event in a Poisson process.");
        const samples=480,all=[];
        let maximum=0;
        for(let i=0;i<=samples;i++){
          const time=maxTime*i/samples;
          const value=density(time,r,lambda);
          all.push({time,value});
          maximum=Math.max(maximum,value);
        }
        const yToPx=value=>137-110*value/Math.max(maximum,0.000001);
        const path=all.map((pt,i)=>(i===0?"M":"L")+
          xToPx(pt.time).toFixed(3)+" "+yToPx(pt.value).toFixed(3)).join(" ");
        byId("esa-erlang-density-path").setAttribute("d",path);
        const shaded=all.filter(pt=>pt.time<t);
        shaded.push({time:t,value:pdf});
        const coordinates=shaded.map((pt,i)=>(i===0?"L":"L")+
          xToPx(pt.time).toFixed(3)+" "+yToPx(pt.value).toFixed(3)).join(" ");
        byId("esa-erlang-shade").setAttribute("d",
          "M34 137 "+coordinates+" L"+xToPx(t).toFixed(3)+" 137 Z");
        byId("esa-erlang-time-marker").setAttribute("x1",String(xToPx(t)));
        byId("esa-erlang-time-marker").setAttribute("x2",String(xToPx(t)));
        byId("esa-erlang-chart").setAttribute("aria-label",isArabic?
          "كثافة غاما/إرلانغ: الشكل "+r+"، المعدل "+lambda.toFixed(2)+
          "، احتمال الانتظار حتى الزمن "+t.toFixed(2)+" يساوي "+c.toFixed(6)+
          " واحتمال البقاء "+s.toFixed(6):
          "Gamma/Erlang density, shape "+r+", rate "+lambda.toFixed(2)+
          ", shaded probability from time 0 to "+t.toFixed(2)+
          " equals "+c.toFixed(6)+". Survival probability "+s.toFixed(6));
      }
      window.esaGammaErlangMath={density,survival};
      [rInput,rateInput,timeInput].forEach(input=>input.addEventListener("input",update));
      function preset(r,rate,t) {
        rInput.value=String(r);
        rateInput.value=String(rate);
        timeInput.value=String(t);
        update();
      }
      byId("esa-erlang-reset").addEventListener("click",()=>preset(4,2,2));
      byId("esa-erlang-exponential").addEventListener("click",()=>preset(1,2,2));
      update();
    })();
