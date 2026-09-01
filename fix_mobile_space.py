import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Fix 1: Wrapper
old_wrapper = 'className="relative w-full overflow-hidden pt-32 md:pt-64 min-h-screen"'
new_wrapper = 'className="relative w-full overflow-hidden pt-28 md:pt-64 min-h-[75vh] md:min-h-screen flex items-center pb-12 md:pb-0"'
code = code.replace(old_wrapper, new_wrapper)

# Fix 2: Section
old_section = 'className="max-w-[1100px] relative z-10 mx-auto px-4 md:px-6 pb-section-gap pt-0 md:pt-4 flex flex-col items-start w-full justify-center min-h-[calc(100vh-200px)]"'
new_section = 'className="max-w-[1100px] relative z-10 mx-auto px-4 md:px-6 pb-8 md:pb-section-gap pt-0 md:pt-4 flex flex-col items-start w-full justify-center h-auto md:min-h-[calc(100vh-200px)]"'
code = code.replace(old_section, new_section)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Fixed mobile spacing in hero section")
