import re

with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

overlay_pattern = re.compile(r'\{isMenuOpen && \(\n.*?</div>\n      \)\}', re.DOTALL)
content = overlay_pattern.sub('', content)

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
