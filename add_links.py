import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# 1. Wrap RaihSoft logo with <a> tag
old_img = '<img src="https://media.raihsuite.com/RS0013/raihsoft-logo-light.PNG" alt="RaihSoft" style={{ height: \'19px\' }} className="opacity-80 object-contain object-left block -ml-[5px]" />'
new_img = '<a href="https://www.raihsoft.com" target="_blank" rel="noopener noreferrer" className="block w-fit"><img src="https://media.raihsuite.com/RS0013/raihsoft-logo-light.PNG" alt="RaihSoft" style={{ height: \'19px\' }} className="opacity-80 object-contain object-left block -ml-[5px]" /></a>'

if old_img in code:
    code = code.replace(old_img, new_img)
else:
    print("Warning: RaihSoft image tag not exactly matched. Will try regex.")
    code = re.sub(
        r'(<img src="https://media\.raihsuite\.com.*?/>)', 
        r'<a href="https://www.raihsoft.com" target="_blank" rel="noopener noreferrer" className="block w-fit">\1</a>', 
        code
    )

# 2. Add RaihSoft to footer with violet color
old_fb = '<a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="https://www.facebook.com/profile.php?id=100082191128704" target="_blank" rel="noopener noreferrer">Facebook <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>'
new_raihsoft = '<a className="text-[#a78bfa] hover:brightness-110 transition-all flex items-center gap-1 group font-bold" href="https://www.raihsoft.com" target="_blank" rel="noopener noreferrer">RaihSoft <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>'

if old_fb in code:
    code = code.replace(old_fb, old_fb + '\n            ' + new_raihsoft)
else:
    print("Warning: Facebook link not exactly matched.")

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Links added successfully.")
