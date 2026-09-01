import re

# 1. Update HeroSnakeBackground.tsx
with open('src/components/hero/HeroSnakeBackground.tsx', 'r') as f:
    code = f.read()

# Increase canvas opacity
code = code.replace("opacity: 0.06,", "opacity: 0.15,")

# Update score div
old_score_div = '''<div className="absolute bottom-8 right-12 font-mono text-3xl font-bold tracking-widest transition-opacity duration-1000" style={{ color: 'rgba(255, 255, 255, 0.25)' }}>'''
new_score_div = '''<div className="absolute bottom-8 right-12 text-sm tracking-widest transition-opacity duration-1000" style={{ color: 'rgba(255, 255, 255, 0.15)', fontFamily: '"Press Start 2P", monospace' }}>'''
code = code.replace(old_score_div, new_score_div)

with open('src/components/hero/HeroSnakeBackground.tsx', 'w') as f:
    f.write(code)

# 2. Update globals.css to include Press Start 2P
with open('src/app/globals.css', 'r') as f:
    css = f.read()

if "Press+Start+2P" not in css:
    import_stmt = "@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');\n"
    css = import_stmt + css
    with open('src/app/globals.css', 'w') as f:
        f.write(css)

print("Styles updated")
