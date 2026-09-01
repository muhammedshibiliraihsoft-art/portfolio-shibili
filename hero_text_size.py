import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Make h1 larger and tighter on mobile
old_h1 = 'className="text-4xl sm:text-5xl md:text-[6rem] font-bold text-white mb-4 md:mb-6 tracking-tight leading-tight md:leading-none font-serif whitespace-normal md:whitespace-nowrap"'
new_h1 = 'className="text-[4rem] sm:text-[5rem] md:text-[6rem] font-bold text-white mb-2 md:mb-6 tracking-tighter leading-[0.9] md:leading-none font-serif whitespace-normal md:whitespace-nowrap"'
code = code.replace(old_h1, new_h1)

# Make h2 larger and tighter on mobile
old_h2 = 'className="text-2xl sm:text-3xl md:text-[3.2rem] font-bold text-primary mb-6 md:mb-8 leading-tight font-serif md:-mt-6 whitespace-normal md:whitespace-nowrap"'
new_h2 = 'className="text-4xl sm:text-5xl md:text-[3.2rem] font-bold text-primary mb-6 md:mb-8 leading-[1] md:leading-tight font-serif md:-mt-6 whitespace-normal md:whitespace-nowrap tracking-tight"'
code = code.replace(old_h2, new_h2)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Updated hero text size and leading for mobile.")
