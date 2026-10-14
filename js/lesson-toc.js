/* Progressive enhancement: navigation for long existing lessons only. */
(function () {
  const main = document.getElementById("main-content");
  if (!main || main.querySelector(".esa-lesson-toc")) return;
  // Section overviews and marketing pages are not lessons.
  if (main.querySelector(".esa-home, .esa-paths, .esa-about, .esa-error")) return;

  const headings = Array.from(main.querySelectorAll("h2"))
    .filter(heading => heading.textContent.trim() &&
      !heading.closest("nav, aside, footer, .sidebar"));
  if (headings.length < 7 || !main.querySelector(".formula-box, .example-box, .concept-box")) return;

  const toc = document.createElement("nav");
  toc.className = "esa-lesson-toc";
  toc.setAttribute("aria-label", "On this page");
  const details = document.createElement("details");
  const summary = document.createElement("summary");
  summary.textContent = "On this page";
  const list = document.createElement("ol");
  const claimed = new Set(Array.from(document.querySelectorAll("[id]"), element => element.id));

  headings.forEach((heading, index) => {
    // All generated and existing IDs need space below the sticky site header.
    heading.classList.add("esa-lesson-anchor");
    if (!heading.id) {
      const slug = heading.textContent.trim().normalize("NFKD")
        .toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0,65);
      const base = "esa-lesson-" + (slug || "section-" + (index + 1));
      let candidate = base;
      let number = 2;
      while (claimed.has(candidate)) candidate = base + "-" + number++;
      heading.id = candidate;
      claimed.add(candidate);
    }
    const item = document.createElement("li");
    const link = document.createElement("a");
    link.href = "#" + encodeURIComponent(heading.id);
    link.textContent = heading.textContent.trim();
    item.appendChild(link);
    list.appendChild(item);
  });

  details.append(summary, list);
  toc.appendChild(details);
  // Keep the hero heading first and offer the TOC immediately before lesson content.
  const section = Array.from(main.children).find(node =>
    node.matches && node.matches("section.section"));
  if (section) main.insertBefore(toc, section);
  else {
    const hero = Array.from(main.children).find(node =>
      node.querySelector && node.querySelector("h1"));
    if (hero) hero.after(toc);
    else main.prepend(toc);
  }

  // The browser may attempt to resolve an incoming #fragment before this
  // script has assigned IDs to headings. Re-align after generation, and again
  // when page resources finish loading (which can change heading positions).
  const knownHeadings = new Map(headings.map(heading => [heading.id, heading]));
  function alignCurrentSection() {
    let id;
    try {
      id = decodeURIComponent(window.location.hash.slice(1));
    } catch (_) {
      return;
    }
    const heading = knownHeadings.get(id);
    if (heading) heading.scrollIntoView({ block: "start", behavior: "instant" });
  }
  const scheduleSectionAlignment = () => requestAnimationFrame(alignCurrentSection);
  window.addEventListener("hashchange", scheduleSectionAlignment);
  window.addEventListener("popstate", scheduleSectionAlignment);
  if (window.location.hash) {
    scheduleSectionAlignment();
    if (document.readyState !== "complete") {
      window.addEventListener("load", scheduleSectionAlignment, { once: true });
    }
  }
})();
