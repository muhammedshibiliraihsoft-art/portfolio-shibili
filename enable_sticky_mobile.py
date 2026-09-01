import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Re-enable sticky stacking on mobile
old_classes = 'relative md:sticky md:top-[15vh] h-auto md:h-[70vh]'
new_classes = 'sticky top-[12vh] md:top-[15vh] h-[85vh] md:h-[70vh]'

code = code.replace(old_classes, new_classes)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Re-enabled sticky stacking for mobile.")
