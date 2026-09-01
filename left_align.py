import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Replace mobile center alignments with left alignments
code = code.replace('text-center md:text-left', 'text-left')
code = code.replace('justify-center md:justify-start', 'justify-start')
code = code.replace('items-center md:items-start', 'items-start')
code = code.replace('mx-auto md:mx-0', '') # Removing it defaults to left, or just replace with empty string if it's not needed.

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Changed mobile alignments to left.")
