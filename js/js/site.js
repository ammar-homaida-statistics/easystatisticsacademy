(function () {
  // Save last visited lesson whenever a lesson page loads
  const lessonMeta = document.querySelector('meta[name="esa-lesson-url"]');
  const lessonTitle = document.querySelector('meta[name="esa-lesson-title"]');
  const sectionMeta = document.querySelector('meta[name="esa-section"]');

  if (lessonMeta && lessonTitle && sectionMeta) {
    const payload = {
      url: lessonMeta.content,
      title: lessonTitle.content,
      section: sectionMeta.content,
      time: Date.now()
    };
    localStorage.setItem('esa_last_lesson', JSON.stringify(payload));
  }

  // On section pages, render "Continue reading" if last lesson belongs to this section
  const container = document.getElementById('continue-reading');
  if (container) {
    try {
      const raw = localStorage.getItem('esa_last_lesson');
      if (!raw) return;

      const last = JSON.parse(raw);
      if (!last || !last.url || !last.title) return;

      // If this page is a foundations page, only show foundations lessons
      // (Change this logic if you reuse for other sections)
      if (last.section !== 'foundations') return;

      container.style.display = 'block';
      container.innerHTML = `
        <section class="section section-soft">
          <div class="content-narrow">
            <h2>Continue reading</h2>
            <p>You last visited: <strong>${last.title}</strong></p>
            <a class="btn btn-primary" href="${last.url}">Continue</a>
          </div>
        </section>
      `;
    } catch (e) {
      // ignore
    }
  }
})();
