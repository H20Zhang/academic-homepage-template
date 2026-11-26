(() => {
  const root = document.documentElement;
  const scope = root.dataset.siteBase || '/';
  const modeKey = `academic-homepage-theme:${scope}`;
  const paletteKey = `academic-homepage-palette:${scope}`;
  const palettes = ['warm', 'ocean', 'forest', 'lilac', 'ink', 'contrast'];
  const load = (key) => {
    try { return localStorage.getItem(key); } catch (_) { return null; }
  };
  const save = (key, value) => {
    try { localStorage.setItem(key, value); } catch (_) {}
  };
  const savedMode = load(modeKey);
  if (savedMode === 'light' || savedMode === 'dark') root.dataset.theme = savedMode;
  const defaultPalette = palettes.includes(root.dataset.palette) ? root.dataset.palette : 'warm';
  const savedPalette = load(paletteKey);
  root.dataset.palette = palettes.includes(savedPalette) ? savedPalette : defaultPalette;
  document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('theme');
    const select = document.getElementById('palette');
    const system = matchMedia('(prefers-color-scheme: dark)');
    const theme = () => root.dataset.theme || (system.matches ? 'dark' : 'light');
    const label = () => { button.textContent = theme() === 'dark' ? 'Light theme' : 'Dark theme'; };
    label();
    select.value = root.dataset.palette;
    document.getElementById('appearance').hidden = false;
    system.addEventListener('change', label);
    select.addEventListener('change', () => {
      root.dataset.palette = select.value;
      save(paletteKey, select.value);
    });
    button.addEventListener('click', () => {
      root.dataset.theme = theme() === 'dark' ? 'light' : 'dark';
      save(modeKey, root.dataset.theme);
      label();
    });
  });
})();
