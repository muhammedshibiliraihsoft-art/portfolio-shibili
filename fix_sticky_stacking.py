import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Remove gap-8 on mobile to ensure continuous stack
code = code.replace('<div className="flex flex-col gap-8 md:gap-0 w-full relative">', '<div className="flex flex-col gap-0 w-full relative">')

# 2. Offset the sticky tops to create a 'deck of cards' visual effect
# Currently they are all 'sticky top-[12vh] md:top-[15vh]'
old_sticky = 'sticky top-[12vh] md:top-[15vh] h-[85vh] md:h-[70vh] flex items-center justify-center w-full'

# We'll split the file to replace them one by one
parts = code.split(old_sticky)
if len(parts) == 4:
    # Meaning there are 3 occurrences
    new_code = parts[0] + 'sticky top-[10vh] md:top-[12vh] h-[85vh] md:h-[70vh] flex items-center justify-center w-full' + \
               parts[1] + 'sticky top-[12vh] md:top-[16vh] h-[85vh] md:h-[70vh] flex items-center justify-center w-full' + \
               parts[2] + 'sticky top-[14vh] md:top-[20vh] h-[85vh] md:h-[70vh] flex items-center justify-center w-full' + \
               parts[3]
    code = new_code
else:
    print(f"Warning: Expected 3 occurrences of sticky wrapper, found {len(parts)-1}")

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed card stacking logic.")
