import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Replace mx-auto with self-center md:self-start
# Current div: className="w-[260px] md:w-[320px] shrink-0 bg-[#f0f4f8] p-4 pb-16 md:p-5 md:pb-24 shadow-2xl -rotate-3 hover:rotate-0 transition-transform duration-500 mx-auto md:mx-0 rounded-sm"
code = re.sub(
    r'transition-transform duration-500 mx-auto md:mx-0 rounded-sm',
    'transition-transform duration-500 mx-auto md:mx-0 self-center md:self-start rounded-sm',
    code
)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Added self-center to polaroid image.")
