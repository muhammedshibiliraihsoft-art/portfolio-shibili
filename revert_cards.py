import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Revert the offsets back to exact same positions
code = code.replace('sticky top-[10vh] md:top-[12vh]', 'sticky top-[12vh] md:top-[15vh]')
code = code.replace('sticky top-[12vh] md:top-[16vh]', 'sticky top-[12vh] md:top-[15vh]')
code = code.replace('sticky top-[14vh] md:top-[20vh]', 'sticky top-[12vh] md:top-[15vh]')

# 2. Remove shadow-2xl from the cards
code = code.replace('shadow-2xl relative transform transition-transform duration-500', 'relative transform transition-transform duration-500')

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Reverted to identical overlap and removed shadows.")
