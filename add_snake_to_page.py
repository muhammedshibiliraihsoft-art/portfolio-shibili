import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Add import
import_stmt = "import HeroSnakeBackground from '@/components/hero/HeroSnakeBackground';\n"
if "import HeroSnakeBackground" not in code:
    code = code.replace("export default function PortfolioTemplate() {", import_stmt + "export default function PortfolioTemplate() {")

# Modify Hero Section
hero_start = code.find('{/* Hero Section */}')
if hero_start != -1:
    section_start = code.find('<section className="max-w-[1100px]', hero_start)
    
    # We need to wrap it. Let's find the closing tag of this section.
    # It ends right before {/* Experience Section */}
    exp_start = code.find('{/* Experience Section */}')
    
    if section_start != -1 and exp_start != -1:
        hero_block = code[section_start:exp_start]
        
        # Modify the section tag to add relative z-10 so it sits above the canvas
        hero_block = hero_block.replace('<section className="max-w-[1100px]', '<section className="max-w-[1100px] relative z-10')
        
        # Wrap it
        wrapped = '''<div className="relative w-full overflow-hidden">
          <HeroSnakeBackground />
          ''' + hero_block + '''        </div>
        '''
        
        code = code[:section_start] + wrapped + code[exp_start:]

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Snake added to page")
