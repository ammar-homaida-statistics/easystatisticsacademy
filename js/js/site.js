(function () {
  // Save lesson progress without assuming browser storage is available.
  const lessonMeta = document.querySelector('meta[name="esa-lesson-url"]');
  const lessonTitle = document.querySelector('meta[name="esa-lesson-title"]');
  const sectionMeta = document.querySelector('meta[name="esa-section"]');

  if (lessonMeta && lessonTitle && sectionMeta) {
    try {
      localStorage.setItem('esa_last_lesson', JSON.stringify({
        url: lessonMeta.content,
        title: lessonTitle.content,
        section: sectionMeta.content,
        time: Date.now()
      }));
    } catch (e) {
      // Storage may be disabled; the lesson still works normally.
    }
  }

  // The Foundations overview is the only page using this resume panel.
  const container = document.getElementById('continue-reading');
  if (!container) return;

  try {
    const raw = localStorage.getItem('esa_last_lesson');
    if (!raw) return;

    const last = JSON.parse(raw);
    if (!last || last.section !== 'foundations' ||
        typeof last.url !== 'string' ||
        typeof last.title !== 'string' || !last.title.trim()) return;

    // Only navigate to a lesson actually listed on the Foundations page.
    // Never build an HTML string from browser-controlled storage.
    const isListedLesson = Array.from(
      document.querySelectorAll('#lessons a[href]')
    ).some(link => link.getAttribute('href') === last.url);
    if (!isListedLesson || !/^\/foundations\/[a-z0-9-]+\/$/.test(last.url)) return;

    const section = document.createElement('section');
    section.className = 'section section-soft';
    const body = document.createElement('div');
    body.className = 'content-narrow';
    const heading = document.createElement('h2');
    heading.textContent = 'Continue reading';
    const summary = document.createElement('p');
    summary.textContent = 'You last visited: ';
    const title = document.createElement('strong');
    title.textContent = last.title;
    summary.appendChild(title);
    const link = document.createElement('a');
    link.className = 'btn btn-primary';
    link.textContent = 'Continue';
    link.href = last.url;
    body.append(heading, summary, link);
    section.appendChild(body);
    container.replaceChildren(section);
    container.style.display = 'block';
  } catch (e) {
    // Invalid or unavailable storage must not break the page.
  }
})();
