# -*- coding: utf-8 -*-
with open("src/components/3d/Hero.jsx", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("<AnimatedCounter />", "")
content = content.replace("import AnimatedCounter from \"./AnimatedCounter\";", "")

with open("src/components/3d/Hero.jsx", "w", encoding="utf-8") as f:
    f.write(content)
print("Removed AnimatedCounter from Hero.jsx")
