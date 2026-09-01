import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Replace height: '28px' with height: '19px' and add object-left and block just in case
old_img = '''<img src="https://media.raihsuite.com/RS0013/raihsoft-logo-light.PNG" alt="RaihSoft" style={{ height: '28px' }} className="opacity-80 object-contain" />'''
new_img = '''<img src="https://media.raihsuite.com/RS0013/raihsoft-logo-light.PNG" alt="RaihSoft" style={{ height: '19px' }} className="opacity-80 object-contain object-left block" />'''

if old_img in code:
    code = code.replace(old_img, new_img)
else:
    code = re.sub(r'<img src="https://media.raihsuite.com/RS0013/raihsoft-logo-light.PNG".*?/>', new_img, code)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Logo resized and aligned.")
