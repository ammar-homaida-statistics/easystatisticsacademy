(async function () {
  const input = document.getElementById("site-search");
  const box = document.getElementById("search-results");
  const status = document.getElementById("search-status");
  if (!input || !box || !status) return;

  let pages = [];
  let state = "loading";
  let dismissed = false;
  const normalize = (text) => text.normalize("NFKC")
    .replace(/[‘’]/g, "'").replace(/\s+/g, " ").trim().toLowerCase();

  function decodeEntities(text) {
    const decoder = document.createElement("textarea");
    decoder.innerHTML = text;
    return decoder.value;
  }

  function close() {
    dismissed = true;
    box.hidden = true;
    box.replaceChildren();
    status.textContent = "";
  }

  function message(text) {
    const notice = document.createElement("div");
    notice.className = "search-empty";
    notice.textContent = text;
    box.replaceChildren(notice);
    box.hidden = false;
    status.textContent = text;
  }

  function readableSnippet(content, query) {
    // Match against normalized text, while remembering the corresponding
    // display offsets. Original source offsets diverge after whitespace,
    // Unicode compatibility characters and case-fold expansions.
    const display = content.normalize("NFKC").replace(/\s+/g, " ").trim();
    if (!display) return "";

    let folded = "";
    const offsets = [];
    for (let i = 0; i < display.length;) {
      const character = String.fromCodePoint(display.codePointAt(i));
      const lower = character.replace(/[‘’]/g, "'").toLowerCase();
      for (let j = 0; j < lower.length; j++) offsets.push(i);
      folded += lower;
      i += character.length;
    }

    const position = folded.indexOf(query);
    const matchStart = position < 0 ? 0 : offsets[position];
    let start = Math.max(0, matchStart - 50);
    if (start > 0) {
      const nextSpace = display.indexOf(" ", start);
      if (nextSpace > 0 && nextSpace - start < 24) start = nextSpace + 1;
    }
    let end = Math.min(display.length, start + 160);
    if (end < display.length) {
      const wordEnd = display.lastIndexOf(" ", end);
      if (wordEnd > start + 95) end = wordEnd;
    }

    return (start ? "…" : "") + display.slice(start, end) +
      (end < display.length ? "…" : "");
  }

  function search(query) {
    const q = normalize(query);
    if (!q) return close();
    dismissed = false;
    if (state === "loading") return message("Loading search…");
    if (state === "error") return message("Search is temporarily unavailable. Please try again.");

    // Normalized fields are computed once after fetch, not on each keystroke.
    const matches = pages.map((page) => {
      const title = page.normalizedTitle;
      const content = page.normalizedContent;
      const rank = title === q ? 0 : title.startsWith(q) ? 1 : title.includes(q) ? 2 : content.includes(q) ? 3 : 4;
      return { page, rank };
    }).filter((match) => match.rank < 4)
      .sort((a, b) => a.rank - b.rank).slice(0, 8);

    if (!matches.length) return message("No results found.");
    box.replaceChildren();
    for (const { page } of matches) {
      const link = document.createElement("a");
      link.className = "search-item";
      link.href = page.url;
      const title = document.createElement("div");
      title.className = "search-title";
      title.textContent = page.title;
      const snippet = document.createElement("div");
      snippet.className = "search-snippet";
      snippet.textContent = readableSnippet(page.content, q);
      link.append(title, snippet);
      box.append(link);
    }
    box.hidden = false;
    status.textContent = matches.length + (matches.length === 1 ? " result shown." : " results shown.");
  }

  // Search results are ordinary links: retain Tab/Enter semantics while
  // adding arrow-key traversal, including an accessible focus return.
  const visibleLinks = () => box.hidden ? [] : Array.from(box.querySelectorAll("a.search-item"));
  input.addEventListener("input", () => search(input.value));
  input.addEventListener("focus", () => search(input.value));
  input.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      close();
      return;
    }
    if (event.key === "ArrowDown" || event.key === "ArrowUp") {
      const links = visibleLinks();
      if (!links.length) return;
      event.preventDefault();
      (event.key === "ArrowDown" ? links[0] : links[links.length - 1]).focus();
    }
  });
  box.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      input.focus();
      close();
      return;
    }
    if (event.key !== "ArrowUp" && event.key !== "ArrowDown") return;
    const links = visibleLinks();
    const current = links.indexOf(document.activeElement);
    if (current < 0) return;
    event.preventDefault();
    const next = current + (event.key === "ArrowDown" ? 1 : -1);
    // ArrowUp from the first result returns to the query field.
    if (next < 0) {
      input.focus();
    } else {
      links[next % links.length].focus();
    }
  });
  document.addEventListener("click", (event) => {
    if (!box.contains(event.target) && event.target !== input) close();
  });
  document.addEventListener("focusin", (event) => {
    if (!box.contains(event.target) && event.target !== input) close();
  });

  try {
    const response = await fetch("/search.json", { cache: "no-store" });
    if (!response.ok) throw new Error("Search index request failed");
    const index = await response.json();
    if (!Array.isArray(index) || !index.every((page) =>
      typeof page.title === "string" && typeof page.content === "string" &&
      typeof page.url === "string" && page.url.startsWith("/") &&
      !page.url.startsWith("//") && new URL(page.url, location.origin).origin === location.origin)) {
      throw new Error("Invalid search index");
    }
    pages = index.map((page) => {
      const title = decodeEntities(page.title);
      const content = decodeEntities(page.content);
      return {
        title, content, url: page.url,
        normalizedTitle: normalize(title),
        normalizedContent: normalize(content)
      };
    });
    state = "ready";
  } catch (error) {
    state = "error";
  }
  // Re-run the current query, including one entered before the index arrived.
  if (!dismissed) search(input.value);
})();
