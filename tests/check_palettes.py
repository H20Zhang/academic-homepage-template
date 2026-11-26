"""Check palette definitions and CSS text contrast (WCAG AA, 4.5:1)."""
import re
from pathlib import Path


def luminance(color):
    channels = [int(color[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(value * weight for value, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def ratio(a, b):
    dark, light = sorted((luminance(a), luminance(b)))
    return (light + 0.05) / (dark + 0.05)


css = Path("assets/css/site.css").read_text()
layout = Path("_layouts/default.html").read_text()
options = re.findall(r'<option value="([^"]+)">', layout)
blocks = {"warm": css.split(":root {", 1)[1].split("}", 1)[0]}
blocks.update(re.findall(r':root\[data-palette="([^"]+)"\]\s*\{([^}]+)\}', css))
assert sorted(options) == sorted(blocks), "Palette menu and color definitions differ"
lowest = 21.0
for name, source in blocks.items():
    colors = dict(re.findall(r"--([a-z]+-[ld]):\s*#([0-9a-f]{6});", source, flags=re.I))
    for mode in ("l", "d"):
        for foreground in ("ink", "muted", "accent"):
            for background in ("paper", "card", "rail", "tint"):
                cr = ratio(colors[f"{foreground}-{mode}"], colors[f"{background}-{mode}"])
                assert cr >= 4.5, (name, mode, foreground, background, round(cr, 2))
                lowest = min(lowest, cr)
print(f"Verified {len(blocks)} palettes in light and dark mode, minimum text contrast {lowest:.2f}:1")
