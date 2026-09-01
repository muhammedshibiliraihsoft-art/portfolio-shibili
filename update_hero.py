# -*- coding: utf-8 -*-
with open("src/components/3d/Hero.jsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the heading text parts
content = content.replace("<h1>web and mobile app</h1>", "<h1>web and mobile application</h1>")
content = content.replace("I specialize in", "I specialize in UI design,")

with open("src/components/3d/Hero.jsx", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated Hero.jsx")
