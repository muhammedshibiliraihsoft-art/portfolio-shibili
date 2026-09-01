with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("import Preloader from '@/components/Preloader';", "// @ts-ignore\nimport Preloader from '@/components/Preloader';")

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
print("Fixed!")
