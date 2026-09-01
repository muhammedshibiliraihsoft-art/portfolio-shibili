import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Add import
import_line = "import ContactPageClient from '@/components/contact/ContactPageClient';"
if "AIGlobe" not in code:
    new_import = """import ContactPageClient from '@/components/contact/ContactPageClient';
import AIGlobe from '@/components/hero/AIGlobe';"""
    code = code.replace(import_line, new_import, 1)

# Find and replace hero inner div using regex
pattern = r'(<div className="w-full text-left" style=\{\{position: \'relative\'\}\}>)(.*?)(</div>\s*</section>)'

def replacer(m):
    return '''<div className="w-full flex flex-col md:flex-row items-center gap-8 md:gap-0" style={{position: 'relative'}}>
              {/* Left: text content */}
              <div className="flex-1 text-left md:pr-8 z-10">''' + m.group(2).rstrip() + """
              </div>
              {/* Right: AI Globe */}
              <div className="hidden md:flex flex-shrink-0 items-center justify-center" style={{ width: '480px', height: '480px', marginRight: '-80px' }}>
                <AIGlobe />
              </div>
            </div>
          </section>"""

new_code, n = re.subn(pattern, replacer, code, count=1, flags=re.DOTALL)
if n:
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(new_code)
    print("Patched with regex OK")
else:
    # Fallback: direct string replacement on actual content
    old_tag = """<div className="w-full text-left" style={{position: 'relative'}}>"""
    new_open = """<div className="w-full flex flex-col md:flex-row items-center gap-8 md:gap-0" style={{position: 'relative'}}>
              {/* Left: text content */}
              <div className="flex-1 text-left md:pr-8 z-10">"""
    
    # Find and inject closing wrapper before </section> of hero
    close_hero_marker = """</div>
          </section>

          {/* Experience Section */}"""
    
    new_close = """</div>
              {/* Right: AI Globe */}
              <div className="hidden md:flex flex-shrink-0 items-center justify-center" style={{ width: '480px', height: '480px', marginRight: '-80px' }}>
                <AIGlobe />
              </div>
            </div>
          </section>

          {/* Experience Section */}"""
    
    if old_tag in code:
        code = code.replace(old_tag, new_open, 1)
        code = code.replace(close_hero_marker, new_close, 1)
        with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
            f.write(code)
        print("Fallback string replacement OK")
    else:
        print("FAILED - nothing matched")
