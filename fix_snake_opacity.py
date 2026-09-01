import re

with open('src/components/hero/HeroSnakeBackground.tsx', 'r') as f:
    code = f.read()

# Change snake body and head colors to have 0.4 opacity (reducing it)
code = code.replace("const COLOR_BODY = '#4d8bff';", "const COLOR_BODY = 'rgba(77, 139, 255, 0.4)';")
code = code.replace("const COLOR_HEAD = '#bfe0ff';", "const COLOR_HEAD = 'rgba(191, 224, 255, 0.4)';")

with open('src/components/hero/HeroSnakeBackground.tsx', 'w') as f:
    f.write(code)

print("Snake opacity reduced")
