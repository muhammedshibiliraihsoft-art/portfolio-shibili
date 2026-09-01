import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Replace py-section-gap with py-16 md:py-section-gap
code = code.replace('py-section-gap', 'py-16 md:py-section-gap')

# Replace large bottom margins that might not be responsive yet
# Projects section title
code = code.replace('mb-8 md:mb-24', 'mb-10 md:mb-24')

# Experience items gap
code = code.replace('gap-12 text-left w-full', 'gap-10 md:gap-12 text-left w-full')
code = code.replace('gap-4 md:gap-12 group', 'gap-2 md:gap-12 group')

# About section gap
code = code.replace('gap-10 md:gap-24 items-center', 'gap-12 md:gap-24 items-center')

# Contact section gap
code = code.replace('gap-12 md:gap-24', 'gap-12 md:gap-24')

# Any other pb-section-gap?
code = code.replace('pb-section-gap', 'pb-16 md:pb-section-gap')

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Fixed spacing globally across the page")
