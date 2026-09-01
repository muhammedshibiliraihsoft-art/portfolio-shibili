import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Remove import
code = re.sub(r"import AIGlobe from '@/components/hero/AIGlobe';\n", "", code)

# Remove the right div with the AI Globe
# Find the start and end of the AI Globe div
globe_start = code.find('{/* Right: AI Globe */}')
if globe_start != -1:
    # Find the closing tag of this div
    # It starts with <div className="flex flex-shrink-0
    globe_div_start = code.find('<div', globe_start)
    
    # We know the content ends with </AIGlobe>\n              </div> or similar
    # Let's just use regex to match the whole block since it's simple
    pattern = r'\{\/\* Right: AI Globe \*\/\}.*?<\/div>'
    code = re.sub(pattern, '', code, flags=re.DOTALL)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Globe removed")
