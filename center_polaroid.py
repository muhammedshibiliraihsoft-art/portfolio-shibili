import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Add mx-auto md:mx-0 to the polaroid frame
old_polaroid = 'transition-transform duration-500  md:mx-0 rounded-sm'
new_polaroid = 'transition-transform duration-500 mx-auto md:mx-0 rounded-sm'

if old_polaroid in code:
    code = code.replace(old_polaroid, new_polaroid)
else:
    # Try an alternative search
    code = re.sub(r'transition-transform duration-500\s*md:mx-0', 'transition-transform duration-500 mx-auto md:mx-0', code)
    code = re.sub(r'transition-transform duration-500 rounded-sm', 'transition-transform duration-500 mx-auto md:mx-0 rounded-sm', code)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Centered polaroid on mobile.")
