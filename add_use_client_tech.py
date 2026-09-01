filepath = "src/components/3d/models/tech_logos/TechIconCardExperience.jsx"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

if '"use client"' not in content:
    content = '/* eslint-disable */\n"use client";\n' + content
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
print("Done")
