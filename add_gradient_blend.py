import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# P1
old_p1 = '<div className="flex-1 relative h-64 md:h-auto overflow-hidden bg-[#0a0e14]">'
new_p1 = '<div className="flex-1 relative h-64 md:h-auto overflow-hidden bg-[#0a0e14]">\n                    <div className="absolute top-0 left-0 right-0 h-24 md:h-full md:bottom-0 md:w-48 bg-gradient-to-b md:bg-gradient-to-r from-[#0e141b] to-transparent z-10 pointer-events-none"></div>'
code = code.replace(old_p1, new_p1)

# P2
old_p2 = '<div className="flex-1 relative h-64 md:h-auto overflow-hidden bg-[#040811]">'
new_p2 = '<div className="flex-1 relative h-64 md:h-auto overflow-hidden bg-[#040811]">\n                    <div className="absolute top-0 left-0 right-0 h-24 md:h-full md:bottom-0 md:w-48 bg-gradient-to-b md:bg-gradient-to-r from-[#060c18] to-transparent z-10 pointer-events-none"></div>'
code = code.replace(old_p2, new_p2)

# P3
old_p3 = '<div className="flex-1 relative h-64 md:h-auto overflow-hidden bg-[#0d1219]">'
new_p3 = '<div className="flex-1 relative h-64 md:h-auto overflow-hidden bg-[#0d1219]">\n                    <div className="absolute top-0 left-0 right-0 h-24 md:h-full md:bottom-0 md:w-48 bg-gradient-to-b md:bg-gradient-to-r from-[#131b26] to-transparent z-10 pointer-events-none"></div>'
code = code.replace(old_p3, new_p3)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Added gradient blend to project image boxes.")
