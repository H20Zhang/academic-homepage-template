(() => {
  const root = document.documentElement;
  const key = 'academic-homepage-theme';
  let saved;
  try { saved = localStorage.getItem(key); } catch (_) {}
  if (saved === 'light' || saved === 'dark') root.dataset.theme = saved;
  document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('theme');
    const system = matchMedia('(prefers-color-scheme: dark)');
    const theme = () => root.dataset.theme || (system.matches ? 'dark' : 'light');
    const label = () => { button.textContent = theme() === 'dark' ? 'Light theme' : 'Dark theme'; };
    label();
    button.hidden = false;
    system.addEventListener('change', label);
    button.addEventListener('click', () => {
      root.dataset.theme = theme() === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem(key, root.dataset.theme); } catch (_) {}
      label();
    });
  });
})();
