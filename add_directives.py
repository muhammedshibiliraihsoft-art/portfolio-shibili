import os

files = [
    "src/components/3d/Experience.jsx",
    "src/components/3d/ShowcaseSection.jsx",
    "src/components/3d/About.jsx",
    "src/components/3d/TechStack.jsx",
]

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if '"use client"' not in content:
        content = '/* eslint-disable */\n"use client";\n' + content
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Directives added!")
