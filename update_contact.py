# -*- coding: utf-8 -*-
with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("hello@shibili.dev", "shibili.n@zohomail.in")

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated contact email")
