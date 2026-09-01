import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Replace the AI Globe div
old_div = '''<div className="hidden md:flex flex-shrink-0 items-center justify-center" style={{ width: '480px', height: '480px', marginRight: '-80px' }}>'''
new_div = '''<div className="flex flex-shrink-0 items-center justify-center absolute md:relative right-[-20%] md:right-0 top-[20%] md:top-auto opacity-30 md:opacity-100 pointer-events-none md:pointer-events-auto w-[300px] h-[300px] md:w-[480px] md:h-[480px] z-0 md:z-10 md:-mr-[80px]">'''

if old_div in code:
    code = code.replace(old_div, new_div)
    with open('src/app/page.tsx', 'w') as f:
        f.write(code)
    print("Fixed AI globe for mobile.")
else:
    print("Could not find the exact div. Trying regex...")
    # Just in case there are spacing differences
    pattern = r'<div className="hidden md:flex[^>]*>\s*<AIGlobe />\s*</div>'
    replacement = '''<div className="flex flex-shrink-0 items-center justify-center absolute md:relative right-[-10%] md:right-0 top-[40%] md:top-auto opacity-25 md:opacity-100 pointer-events-none md:pointer-events-auto w-[350px] h-[350px] md:w-[480px] md:h-[480px] z-0 md:z-10 md:-mr-[80px]">
                <AIGlobe />
              </div>'''
    code = re.sub(pattern, replacement, code)
    with open('src/app/page.tsx', 'w') as f:
        f.write(code)
    print("Regex fix applied.")
