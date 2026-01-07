(async function () {
  const input = document.getElementById("site-search");
  const box = document.getElementById("search-results");
  if (!input || !box) return;

  let pages = [];
  let ready = false;

  async function loadIndex() {
    try {
      const res = await fetch("/search.json", { cache: "no-store" });
      if (!res.ok) throw new Error("search.json not found");
      pages = await res.json();
      ready = true;
    } catch (e) {
      // If this happens, your /search.json is missing or invalid.
      box.hidden = false;
      box.innerHTML = `<div class="search-empty">Search index not available. Check /search.json.</div>`;
    }
  }

  function escapeHtml(s) {
    return s.replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    }[c]));
  }

  function render(results) {
    if (!results.length) {
      box.innerHTML = `<div class="search-empty">No results</div>`;
      return;
    }
    box.innerHTML = results.map(r => `
      <a class="search-item" href="${r.url}">
        <div class="search-title">${escapeHtml(r.title)}</div>
        <div class="search-snippet">${escapeHtml(r.snippet)}</div>
      </a>
    `).join("");
  }

  function search(q) {
    q = q.trim().toLowerCase();
    if (!q) {
      box.hidden = true;
      box.innerHTML = "";
      return;
    }
    if (!ready) {
      box.hidden = false;
      box.innerHTML = `<div class="search-empty">Loading…</div>`;
      return;
    }

    const out = [];
    for (const p of pages) {
      const title = (p.title || "").toLowerCase();
      const content = (p.content || "").toLowerCase();
      if (title.includes(q) || content.includes(q)) {
        const raw = p.content || "";
        const pos = content.indexOf(q);
        const start = Math.max(0, pos - 50);
        const snippet = raw.substring(start, start + 140).replace(/\s+/g, " ").trim();
        out.push({ title: p.title || p.url, url: p.url, snippet: snippet || "" });
      }
      if (out.length >= 8) break;
    }

    box.hidden = false;
    render(out);
  }

  // Close results when clicking outside
  document.addEventListener("click", (e) => {
    if (!box.contains(e.target) && e.target !== input) {
      box.hidden = true;
    }
  });

  input.addEventListener("input", (e) => search(e.target.value));
  input.addEventListener("focus", () => {
    if (input.value.trim()) search(input.value);
  });

  await loadIndex();
})();
