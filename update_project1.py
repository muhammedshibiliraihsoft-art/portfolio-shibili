import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Replace text
code = code.replace('Spotifu Music', 'AccuBook')
code = code.replace('A music streaming app that emulates Spotify&apos;s core features.', 'A comprehensive accounting software dashboard for managing business finances.')

# Replace image for project 1
# Find the specific img tag for project 1
old_img = '''<img 
                    alt="Spotifu App Preview" 
                    className="absolute object-cover object-left-top rounded-tl-2xl" 
                    style={{ top: '98px', left: '48px', width: '100%', height: '100%' }} 
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuBjqKLHdVjtpXWZVZs_3AzwzJ8MiK2-Wr3XzbtazwXheb4PH4EdqsxYU0IjJCWOd9IsHeqjyEvgFCxU1cmLhClFJ5kp7-yQ0waUyH3TLkssZdvenrs-APfORnwj0p0t2nJA3aAdVHnaN5T5oX7APHDNFvv-x8usryy7ZzeNVzxsxO-_mIDTtt47ltgzP3COllsW_RFX9BEt_e0Hdwdzm9nFhjfMmOUodapDZPFfmM2mJYUUgotWkNe_VJY0MQCnfJhK2FM" 
                  />'''

new_img = '''<img 
                    alt="AccuBook App Preview" 
                    className="absolute object-cover object-right-top rounded-tl-2xl" 
                    style={{ top: '98px', left: '48px', width: '100%', height: '100%' }} 
                    src="/accubook.png" 
                  />'''

if old_img in code:
    code = code.replace(old_img, new_img)
else:
    print("Could not find exact img string. Using regex...")
    code = re.sub(r'<img\s+alt="Spotifu App Preview".*?/>', new_img, code, flags=re.DOTALL)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Updated Project 1")
