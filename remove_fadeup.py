import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove FadeUp definition
content = re.sub(r'function FadeUp.*?return \(\n\s*<div\n\s*ref=\{domRef\}.*?</div>\n\s*\);\n}', '', content, flags=re.DOTALL)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
