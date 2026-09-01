import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Add a negative left margin to pull the logo exactly under the text
# Currently: className="opacity-80 object-contain object-left block"
old_class = 'className="opacity-80 object-contain object-left block"'
new_class = 'className="opacity-80 object-contain object-left block -ml-[5px]"'

code = code.replace(old_class, new_class)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Applied negative margin to fix alignment.")
