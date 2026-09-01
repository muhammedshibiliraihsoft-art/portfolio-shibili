import re

with open('src/components/hero/HeroSnakeBackground.tsx', 'r') as f:
    code = f.read()

code = code.replace("const COLOR_BODY = 'rgba(77, 139, 255, 0.5)';", "const COLOR_BODY = 'rgba(77, 139, 255, 0.25)';")
code = code.replace("const COLOR_HEAD = 'rgba(191, 224, 255, 0.5)';", "const COLOR_HEAD = 'rgba(191, 224, 255, 0.25)';")

with open('src/components/hero/HeroSnakeBackground.tsx', 'w') as f:
    f.write(code)

print("Snake opacity set to 0.25")
