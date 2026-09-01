import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

old_wrapper = 'w-[260px] md:w-[320px] shrink-0 bg-[#f0f4f8] p-4 pb-16 md:p-5 md:pb-24 shadow-2xl'
new_wrapper = 'w-[260px] md:w-[400px] shrink-0 bg-[#f0f4f8] p-4 pb-16 md:p-6 md:pb-32 shadow-2xl'
code = code.replace(old_wrapper, new_wrapper)

old_img = 'w-full h-[228px] md:h-[280px] object-cover'
# if md:p-6 is used, total padding is 48px. 400 - 48 = 352px height for perfect square
new_img = 'w-full h-[228px] md:h-[352px] object-cover'
code = code.replace(old_img, new_img)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Resized desktop polaroid.")
