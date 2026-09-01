import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# The specific gradient div for Project 1
gradient_p1 = '<div className="absolute top-0 left-0 right-0 h-24 md:h-full md:bottom-0 md:w-48 bg-gradient-to-b md:bg-gradient-to-r from-[#0e141b] to-transparent z-10 pointer-events-none"></div>'

code = code.replace(gradient_p1, '')

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Removed gradient from Project 1.")
