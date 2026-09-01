import re

with open('src/components/hero/HeroSnakeBackground.tsx', 'r') as f:
    code = f.read()

code = code.replace("const COLOR_BODY = 'rgba(77, 139, 255, 0.4)';", "const COLOR_BODY = 'rgba(77, 139, 255, 0.5)';")
code = code.replace("const COLOR_HEAD = 'rgba(191, 224, 255, 0.4)';", "const COLOR_HEAD = 'rgba(191, 224, 255, 0.5)';")

with open('src/components/hero/HeroSnakeBackground.tsx', 'w') as f:
    f.write(code)

print("Snake opacity set to 50%")
