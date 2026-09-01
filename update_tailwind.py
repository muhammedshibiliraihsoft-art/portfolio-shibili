with open('tailwind.config.ts', 'r', encoding='utf-8') as f:
    content = f.read()

new_colors = """
    "black-50": "#1c1c21",
    "black-100": "#0e0e10",
    "black-200": "#282732",
    "white-50": "#d9ecff",
    "blue-50": "#839cb5",
    "blue-100": "#2d2d38",
"""

content = content.replace('"colors": {', '"colors": {' + new_colors)

with open('tailwind.config.ts', 'w', encoding='utf-8') as f:
    f.write(content)
