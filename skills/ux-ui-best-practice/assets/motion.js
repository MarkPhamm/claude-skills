/* =========================================================
   motion.js — tiny, dependency-free helpers (~1KB)
   - Scroll reveal with stagger (runs once per element)
   - Accordion toggles with aria-expanded
   - SPA view transitions with graceful fallback
   Usage: <script type="module" src="motion.js"></script>
   ========================================================= */

const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ---------- Scroll reveal ----------
   Mark elements: <section data-reveal> or a group:
   <ul data-reveal-group><li>…</li><li>…</li></ul>  (children stagger) */
export function initReveal(root = document) {
  if (!('IntersectionObserver' in window)) return; // content stays visible
  document.documentElement.classList.add('js-reveal');

  root.querySelectorAll('[data-reveal-group]').forEach((group) => {
    [...group.children].forEach((child, i) => {
      child.setAttribute('data-reveal', '');
      child.style.setProperty('--i', Math.min(i, 8)); // cap stagger so long lists don't lag
    });
  });

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          io.unobserve(e.target); // once only
        }
      });
    },
    { rootMargin: '0px 0px -10% 0px', threshold: 0.1 }
  );

  root.querySelectorAll('[data-reveal]').forEach((el) => {
    // Already in view on load (e.g. hero) → reveal immediately in sequence
    io.observe(el);
  });
}

/* ---------- Accordion ----------
   <button aria-expanded="false" aria-controls="faq-1">Question</button>
   <div id="faq-1" class="collapse" data-open="false"><div>Answer</div></div> */
export function initAccordions(root = document) {
  root.querySelectorAll('button[aria-controls][aria-expanded]').forEach((btn) => {
    const panel = document.getElementById(btn.getAttribute('aria-controls'));
    if (!panel || !panel.classList.contains('collapse')) return;
    btn.addEventListener('click', () => {
      const open = btn.getAttribute('aria-expanded') !== 'true';
      btn.setAttribute('aria-expanded', String(open));
      panel.dataset.open = String(open);
      panel.toggleAttribute('inert', !open);
    });
    panel.toggleAttribute('inert', btn.getAttribute('aria-expanded') !== 'true');
  });
}

/* ---------- View transition wrapper for SPA state changes ----------
   withTransition(() => renderNewView()); */
export function withTransition(update) {
  if (reduceMotion || !document.startViewTransition) return update();
  return document.startViewTransition(update);
}

/* ---------- Exaggerated feedback helper ---------- */
export function shake(el) {
  if (reduceMotion) return;
  el.classList.remove('shake');
  void el.offsetWidth; // restart animation
  el.classList.add('shake');
}

/* ---------- Postel's law: forgiving input normalizers ---------- */
export const normalize = {
  email: (v) => v.trim().toLowerCase(),
  phone: (v) => v.replace(/[^\d+]/g, ''),
  text:  (v) => v.replace(/\s+/g, ' ').trim(),
};

/* Auto-init */
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => { initReveal(); initAccordions(); });
} else {
  initReveal(); initAccordions();
}
