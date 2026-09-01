import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Replace the broken polaroid div
# The current broken code from Get-Content:
old_broken = '''<div className="w-[260px] md:w-[320px] shrink-0 bg-[#f0f4f8] p-4 pb-16 md:p-5 md:pb-24 shadow-2xl -rotate-3 hover:rotate-0 transition-transform duration-500  rounded-sm">
                <img alt="Profile picture" className="w-full aspect-square object-cover rounded-sm filter contrast-105" src="/profile.png" />
              </div>'''

new_fixed = '''<div className="w-[260px] md:w-[320px] shrink-0 bg-[#f0f4f8] p-4 pb-16 md:p-5 md:pb-24 shadow-2xl -rotate-3 hover:rotate-0 transition-transform duration-500 mx-auto md:mx-0 self-center md:self-start rounded-sm flex flex-col">
                <img alt="Profile picture" className="w-full h-[228px] md:h-[280px] object-cover rounded-sm filter contrast-105" src="/profile.png" />
              </div>'''

# Account for flexible spacing in old_broken
old_regex = r'<div className="w-\[260px\].*?src="/profile\.png" />\s*</div>'

code = re.sub(old_regex, new_fixed, code, flags=re.DOTALL)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Fixed polaroid completely.")
