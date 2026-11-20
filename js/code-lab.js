/* Code Lab: R/Python tabs and copy buttons.
   Progressive enhancement: without JavaScript all panels and code stay visible. */
(function () {
  "use strict";
  var STORE_KEY = "esa-codelab-lang";

  function readPref() {
    try { return window.localStorage.getItem(STORE_KEY); } catch (e) { return null; }
  }
  function writePref(lang) {
    try { window.localStorage.setItem(STORE_KEY, lang); } catch (e) { /* storage blocked */ }
  }

  function selectTab(group, lang) {
    var tabs = group.querySelectorAll(".clab-tab");
    var panels = group.querySelectorAll(".clab-panel");
    var found = false;
    tabs.forEach(function (t) {
      var on = t.getAttribute("data-lang") === lang;
      if (on) found = true;
      t.setAttribute("aria-selected", on ? "true" : "false");
      t.tabIndex = on ? 0 : -1;
    });
    if (!found) return false;
    panels.forEach(function (p) { p.hidden = p.getAttribute("data-lang") !== lang; });
    return true;
  }

  function selectEverywhere(lang) {
    document.querySelectorAll(".clab-tabs.is-enhanced").forEach(function (g) { selectTab(g, lang); });
  }

  document.querySelectorAll(".clab-tabs").forEach(function (group, gi) {
    var panels = group.querySelectorAll(".clab-panel");
    if (panels.length < 2) return;

    var list = document.createElement("div");
    list.className = "clab-tablist";
    list.setAttribute("role", "tablist");
    list.setAttribute("aria-label", group.getAttribute("data-label") || "Language");

    panels.forEach(function (panel, pi) {
      var lang = panel.getAttribute("data-lang");
      var label = panel.getAttribute("data-title") || lang;
      var id = "clab-" + gi + "-" + pi;
      panel.id = id + "-panel";
      panel.setAttribute("role", "tabpanel");

      var tab = document.createElement("button");
      tab.type = "button";
      tab.className = "clab-tab";
      tab.id = id + "-tab";
      tab.setAttribute("role", "tab");
      tab.setAttribute("data-lang", lang);
      tab.setAttribute("aria-controls", panel.id);
      tab.textContent = label;
      panel.setAttribute("aria-labelledby", tab.id);

      tab.addEventListener("click", function () { writePref(lang); selectEverywhere(lang); });
      tab.addEventListener("keydown", function (ev) {
        if (ev.key !== "ArrowRight" && ev.key !== "ArrowLeft") return;
        var all = Array.prototype.slice.call(list.querySelectorAll(".clab-tab"));
        var i = all.indexOf(tab) + (ev.key === "ArrowRight" ? 1 : -1);
        var next = all[(i + all.length) % all.length];
        next.focus(); next.click();
      });
      list.appendChild(tab);
    });

    group.insertBefore(list, group.firstChild);
    group.classList.add("is-enhanced");
    var first = panels[0].getAttribute("data-lang");
    if (!selectTab(group, readPref() || first)) selectTab(group, first);
  });

  // Copy buttons on code blocks (not on output blocks).
  if (navigator.clipboard) {
    document.querySelectorAll(".clab pre:not(.clab-output)").forEach(function (pre) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "clab-copy";
      btn.textContent = document.documentElement.lang === "ar" ? "نسخ" : "Copy";
      btn.addEventListener("click", function () {
        var code = pre.querySelector("code");
        navigator.clipboard.writeText((code || pre).innerText).then(function () {
          var old = btn.textContent;
          btn.textContent = document.documentElement.lang === "ar" ? "تم النسخ" : "Copied";
          setTimeout(function () { btn.textContent = old; }, 1500);
        });
      });
      pre.appendChild(btn);
    });
  }
})();
