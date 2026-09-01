import re

with open('src/app/globals.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the marquee CSS block
content = re.sub(r'\.projects-marquee\s*\{.*?\n\}\n\n', '', content, flags=re.DOTALL)
content = re.sub(r'\.projects-track\s*\{.*?\n\}\n\n', '', content, flags=re.DOTALL)
content = re.sub(r'\.projects-marquee:hover \.projects-track\s*\{.*?\n\}\n\n', '', content, flags=re.DOTALL)
content = re.sub(r'@keyframes scrollUp\s*\{.*?\n\}\n*', '', content, flags=re.DOTALL)

with open('src/app/globals.css', 'w', encoding='utf-8') as f:
    f.write(content.strip() + '\n')
