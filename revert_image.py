import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

old_img_div = 'className="w-[200px] h-[200px] md:w-[300px] md:h-[300px] shrink-0 border-[10px] md:border-[16px] border-white shadow-2xl rotate-3 hover:rotate-0 transition-transform duration-500 mx-auto md:mx-0"'
new_img_div = 'className="w-[300px] h-[300px] shrink-0 border-[16px] border-white shadow-2xl rotate-3 hover:rotate-0 transition-transform duration-500"'

code = code.replace(old_img_div, new_img_div)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Reverted image classes")
