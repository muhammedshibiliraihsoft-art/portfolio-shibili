import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Define the old skills block
old_skills_pattern = r'<div className="flex flex-wrap gap-4 mt-12 justify-start">.*?</div>'

# Define the new skills block
new_skills = '''<div className="flex flex-wrap gap-4 mt-12 justify-start">
                  <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">React / Next.js</span>
                  <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">TypeScript</span>
                  <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Python</span>
                  <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Node.js</span>
                  <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Antigravity</span>
                  <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Codex</span>
                </div>'''

# Replace using regex dotall
code = re.sub(old_skills_pattern, new_skills, code, flags=re.DOTALL)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Updated skills list successfully.")
