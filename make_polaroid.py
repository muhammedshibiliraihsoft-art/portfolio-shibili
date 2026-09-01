import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

old_polaroid = '''<div className="w-[300px] h-[300px] shrink-0 border-[16px] border-white shadow-2xl rotate-3 hover:rotate-0 transition-transform duration-500">
              <img alt="Profile picture" className="w-full h-full object-cover" src="/profile.png" />
            </div>'''

new_polaroid = '''<div className="w-[260px] md:w-[320px] shrink-0 bg-[#f0f4f8] p-4 pb-16 md:p-5 md:pb-24 shadow-2xl -rotate-3 hover:rotate-0 transition-transform duration-500 mx-auto md:mx-0 rounded-sm">
              <img alt="Profile picture" className="w-full aspect-square object-cover rounded-sm filter contrast-105" src="/profile.png" />
            </div>'''

if old_polaroid in code:
    code = code.replace(old_polaroid, new_polaroid)
else:
    # Use regex if exact string mismatch
    code = re.sub(r'<div className="w-\[300px\].*?</div>', new_polaroid, code, flags=re.DOTALL)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Updated to real polaroid frame")
