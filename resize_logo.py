import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Replace height: '15px' with height: '28px' for better visibility
old_img = "style={{ height: '15px' }}"
new_img = "style={{ height: '28px' }}"

code = code.replace(old_img, new_img)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Resized logo successfully.")
