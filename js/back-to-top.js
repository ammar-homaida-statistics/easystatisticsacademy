(function () {
  const button = document.getElementById("back-to-top");
  if (!button) return;

  const updateVisibility = () => {
    const canScroll = document.documentElement.scrollHeight - window.innerHeight > 650;
    button.hidden = !(canScroll && window.scrollY > 550);
  };

  button.addEventListener("click", () => {
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    // Move keyboard focus off the control before it disappears at the top.
    const homeLink = document.querySelector(".site-header .brand");
    if (homeLink) homeLink.focus({ preventScroll: true });
    window.scrollTo({ top: 0, behavior: reduceMotion ? "instant" : "smooth" });
  });
  window.addEventListener("scroll", updateVisibility, { passive: true });
  window.addEventListener("resize", updateVisibility);
  updateVisibility();
})();
