import re

with open('src/components/hero/HeroSnakeBackground.tsx', 'r') as f:
    code = f.read()

code = code.replace("const COLOR_BODY = 'rgba(77, 139, 255, 0.25)';", "const COLOR_BODY = '#4d8bff';")
code = code.replace("const COLOR_HEAD = 'rgba(191, 224, 255, 0.25)';", "const COLOR_HEAD = '#bfe0ff';")

with open('src/components/hero/HeroSnakeBackground.tsx', 'w') as f:
    f.write(code)

print("Reverted snake colors to solid")
