import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

p3_start = code.find('{/* Project 3 */}')

if p3_start != -1:
    p3_block = code[p3_start:]
    
    # Update background: Change bg-[#0e141b] to bg-[#131b26]
    p3_block = p3_block.replace('bg-[#0e141b]', 'bg-[#131b26]', 1)
    
    # Update image styles
    # We want to add a custom drop shadow and push it to the right
    old_img_match = re.search(r'<img\s+alt="Festival Manager Preview".*?/>', p3_block, flags=re.DOTALL)
    if old_img_match:
        new_img = '''<img 
                    alt="Festival Manager Preview" 
                    className="absolute object-contain object-right drop-shadow-[0_25px_35px_rgba(0,0,0,0.6)]" 
                    style={{ top: '60px', left: '80px', width: '100%', height: 'calc(100% - 60px)' }} 
                    src="/festival.png" 
                  />'''
        p3_block = p3_block.replace(old_img_match.group(0), new_img, 1)
        
    code = code[:p3_start] + p3_block
    
    with open('src/app/page.tsx', 'w') as f:
        f.write(code)
    print("Updated Project 3 styling")
else:
    print("Could not find Project 3 bounds")
