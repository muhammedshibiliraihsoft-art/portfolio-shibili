with open("src/app/globals.css", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("overflow-x: hidden;", "overflow-x: clip;")

with open("src/app/globals.css", "w", encoding="utf-8") as f:
    f.write(content)
print("Fixed overflow-x!")
