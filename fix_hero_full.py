import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Remove padding from <main>
code = code.replace('<main className="flex-grow pt-56 md:pt-64"', '<main className="flex-grow"')

# Add padding to the relative wrapper for Hero
code = code.replace('<div className="relative w-full overflow-hidden">', '<div className="relative w-full overflow-hidden pt-56 md:pt-64 min-h-screen">')

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Fixed layout for full screen snake")
