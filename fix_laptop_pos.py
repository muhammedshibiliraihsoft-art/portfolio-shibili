import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

p3_start = code.find('{/* Project 3 */}')

if p3_start != -1:
    p3_block = code[p3_start:]
    
    # Update image styles to move it left
    old_style = "style={{ top: '60px', left: '80px', width: '100%', height: 'calc(100% - 60px)' }}"
    new_style = "style={{ top: '60px', left: '0px', paddingRight: '20px', width: '100%', height: 'calc(100% - 60px)' }}"
    
    p3_block = p3_block.replace(old_style, new_style, 1)
    
    code = code[:p3_start] + p3_block
    
    with open('src/app/page.tsx', 'w') as f:
        f.write(code)
    print("Fixed laptop position")
else:
    print("Could not find Project 3")
