with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

imports = "// @ts-ignore\nimport TechStack from '@/components/3d/TechStack';\n"
content = content.replace("import Experience", imports + "import Experience")

content = content.replace("<Experience />", "<Experience />\n        <TechStack />")

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
print("TechStack injected!")
