with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Add the import after existing imports
import_line = "import ContactPageClient from '@/components/contact/ContactPageClient';"
new_import = """import ContactPageClient from '@/components/contact/ContactPageClient';
import AIGlobe from '@/components/hero/AIGlobe';"""
code = code.replace(import_line, new_import, 1)

# Replace the hero section — wrap text in a flex layout with globe on right
old_hero_inner = """<div className="w-full text-left" style={{position: 'relative'}}>
              <h1 className="text-5xl md:text-[6rem] font-bold text-white mb-2 md:mb-6 tracking-tight leading-none whitespace-nowrap font-serif">Muhammed Shibili N</h1>
              <h2 className="text-3xl md:text-[3.2rem] font-bold text-primary mb-8 leading-tight font-serif whitespace-nowrap" style={{marginTop: '-24px'}}>AI Architect &amp; Full Stack Developer</h2>
              <p className="mb-16 text-lg md:text-xl font-poppins font-medium text-neutral opacity-80 max-w-3xl leading-relaxed">
                Developer based in San Francisco, USA. I specialize in UI design, web and mobile application development and maintenance.
              </p>
              <a className="inline-block bg-[#2563eb] text-[#fff] px-10 py-5 text-lg rounded-full font-bold hover:scale-105 hover:brightness-110 transition-all duration-300" href="#contact">Get in Touch</a>
            </div>"""

new_hero_inner = """<div className="w-full flex flex-col md:flex-row items-center md:items-center gap-8 md:gap-0" style={{position: 'relative'}}>
              {/* Left: text content */}
              <div className="flex-1 text-left md:pr-8 z-10">
                <h1 className="text-5xl md:text-[6rem] font-bold text-white mb-2 md:mb-6 tracking-tight leading-none whitespace-nowrap font-serif">Muhammed Shibili N</h1>
                <h2 className="text-3xl md:text-[3.2rem] font-bold text-primary mb-8 leading-tight font-serif whitespace-nowrap" style={{marginTop: '-24px'}}>AI Architect &amp; Full Stack Developer</h2>
                <p className="mb-16 text-lg md:text-xl font-poppins font-medium text-neutral opacity-80 max-w-xl leading-relaxed">
                  Developer based in San Francisco, USA. I specialize in UI design, web and mobile application development and maintenance.
                </p>
                <a className="inline-block bg-[#2563eb] text-[#fff] px-10 py-5 text-lg rounded-full font-bold hover:scale-105 hover:brightness-110 transition-all duration-300" href="#contact">Get in Touch</a>
              </div>
              {/* Right: AI Globe */}
              <div className="hidden md:flex flex-shrink-0 items-center justify-center" style={{ width: '480px', height: '480px', marginRight: '-80px' }}>
                <AIGlobe />
              </div>
            </div>"""

if old_hero_inner in code:
    code = code.replace(old_hero_inner, new_hero_inner, 1)
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Hero patched successfully")
else:
    print("HERO BLOCK NOT FOUND — trying fallback")
    # Try to find what's actually there
    idx = code.find('text-left" style={{position: \'relative\'}}>')
    print(f"Found at index: {idx}")
    if idx != -1:
        print(code[idx:idx+500])
