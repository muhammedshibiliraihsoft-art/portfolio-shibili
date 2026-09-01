import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

p3_start = code.find('{/* Project 3 */}')

if p3_start != -1:
    p3_block = code[p3_start:]
    
    # Update text
    p3_block = p3_block.replace('Task Manager', 'Festival Manager', 1)
    p3_block = p3_block.replace('A collaborative productivity app to track daily tasks and goals.', 'A comprehensive dashboard for managing festival events, registrations, and schedules.', 1)
    
    # Update image
    old_img_match = re.search(r'<img\s+alt="Project 3 Preview".*?/>', p3_block, flags=re.DOTALL)
    if old_img_match:
        new_img = '''<img 
                    alt="Festival Manager Preview" 
                    className="absolute object-contain object-right drop-shadow-2xl" 
                    style={{ top: '48px', left: '24px', width: '100%', height: 'calc(100% - 48px)' }} 
                    src="/festival.png" 
                  />'''
        p3_block = p3_block.replace(old_img_match.group(0), new_img, 1)
        
    code = code[:p3_start] + p3_block
    
    with open('src/app/page.tsx', 'w') as f:
        f.write(code)
    print("Updated Project 3")
else:
    print("Could not find Project 3 bounds")
