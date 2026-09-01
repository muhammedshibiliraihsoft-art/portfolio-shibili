import re

# Read original globals.css
with open("src/app/globals.css", "r", encoding="utf-8") as f:
    globals_content = f.read()

# Remove the manually injected flat CSS I added earlier
# It started with "/* 3D PORTFOLIO STYLES MIGRATED */"
if "/* 3D PORTFOLIO STYLES MIGRATED */" in globals_content:
    globals_content = globals_content.split("/* 3D PORTFOLIO STYLES MIGRATED */")[0]

# Read Vite index.css
with open("D:/3d-portfolio-main/3d-portfolio-main/src/index.css", "r", encoding="utf-8") as f:
    vite_content = f.read()

# Strip @import tailwindcss and @theme block
vite_content = re.sub(r'@import "tailwindcss";', '', vite_content)
vite_content = re.sub(r'@theme\s*\{[^}]*\}', '', vite_content, flags=re.DOTALL)

# Append to globals
with open("src/app/globals.css", "w", encoding="utf-8") as f:
    f.write(globals_content + "\n" + vite_content)

# Fix page.tsx by removing desktop-zoom
with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    page_content = f.read()

page_content = page_content.replace("desktop-zoom", "")

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(page_content)
