import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Replace background color only for Project 2
# It's currently <div className="w-full bg-[#0e141b] rounded-2xl
# Find Project 2 block
p2_start = code.find('{/* Project 2 */}')
p3_start = code.find('{/* Project 3 */}')

if p2_start != -1 and p3_start != -1:
    p2_block = code[p2_start:p3_start]
    
    # Update background
    p2_block = p2_block.replace('bg-[#0e141b]', 'bg-[#060c18]', 1) # A deep navy blue that matches the phone border
    
    # Update text
    p2_block = p2_block.replace('E-Commerce App', 'Contribution Portal')
    p2_block = p2_block.replace('A modern online store with a fully functional cart and checkout system.', 'A mobile application for supporting causes, tracking pledges, and making seamless contributions.')
    
    # Update image
    old_img_match = re.search(r'<img\s+alt="Project 2 Preview".*?/>', p2_block, flags=re.DOTALL)
    if old_img_match:
        new_img = '''<img 
                    alt="Contribution Portal App Preview" 
                    className="absolute object-contain object-bottom drop-shadow-2xl" 
                    style={{ top: '48px', left: '0', right: '0', margin: '0 auto', width: '80%', height: 'calc(100% - 48px)' }} 
                    src="/charity.png" 
                  />'''
        p2_block = p2_block.replace(old_img_match.group(0), new_img)
        
    code = code[:p2_start] + p2_block + code[p3_start:]
    
    with open('src/app/page.tsx', 'w') as f:
        f.write(code)
    print("Updated Project 2")
else:
    print("Could not find Project 2 bounds")
