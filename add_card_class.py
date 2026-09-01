import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add project-card to the card containers
old_class = 'className="bg-[#0e141b] rounded-2xl overflow-hidden flex flex-col md:flex-row items-stretch border border-[#94a3b833] relative shadow-lg text-left"'
new_class = 'className="project-card bg-[#0e141b] rounded-2xl overflow-hidden flex flex-col md:flex-row items-stretch border border-[#94a3b833] relative shadow-lg text-left"'

content = content.replace(old_class, new_class)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
