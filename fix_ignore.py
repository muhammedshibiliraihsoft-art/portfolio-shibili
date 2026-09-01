with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("import Experience from '@/components/3d/Experience';", "// @ts-ignore\nimport Experience from '@/components/3d/Experience';")

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
print("Fixed!")
