import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Add isMenuOpen state
code = code.replace("const [activeSection, setActiveSection] = useState('');", "const [activeSection, setActiveSection] = useState('');\n  const [isMenuOpen, setIsMenuOpen] = useState(false);")

# Navbar structural changes
# Add menu button for mobile
old_nav_links = '''<div className="hidden md:flex items-center gap-8">'''
new_nav_links = '''<div className="flex md:hidden items-center">
            <button onClick={() => setIsMenuOpen(!isMenuOpen)} className="text-white hover:text-primary transition-colors">
              <span className="material-symbols-outlined text-3xl">{isMenuOpen ? 'close' : 'menu'}</span>
            </button>
          </div>
          <div className="hidden md:flex items-center gap-8">'''
code = code.replace(old_nav_links, new_nav_links)

# Mobile Menu Overlay
mobile_menu = '''
      {isMenuOpen && (
        <div className="fixed inset-0 top-20 bg-background/98 z-40 md:hidden flex flex-col items-center justify-center gap-8 backdrop-blur-md">
          {['experience', 'projects', 'about'].map((id) => (
            <a
              key={id}
              href={#\}
              onClick={() => setIsMenuOpen(false)}
              className="text-2xl font-poppins font-medium text-white capitalize hover:text-primary"
            >
              {id}
            </a>
          ))}
          <a
            href="#contact"
            onClick={() => setIsMenuOpen(false)}
            className="mt-4 bg-primary text-white text-lg font-poppins font-bold px-10 py-4 rounded-full hover:brightness-110"
          >
            Get in Touch
          </a>
        </div>
      )}
'''

# Insert Mobile Menu after </nav>
code = code.replace('</nav>', '</nav>\n' + mobile_menu)

# Remove zoom: 0.75 from <main> and <footer>
code = code.replace('<main className="flex-grow" style={{ zoom: 0.75 }}>', '<main className="flex-grow">')
code = code.replace('<footer style={{ zoom: 0.75 }} className="bg-background', '<footer className="bg-background')

# Fix Hero Section
# 1. Wrapper (remove pt-56 md:pt-64 because no zoom means it will be huge)
# Instead of pt-56, let's use pt-32 md:pt-40
code = code.replace('pt-56 md:pt-64', 'pt-32 md:pt-40')

# 2. Hero Text alignment & scaling
old_h1 = '''<h1 className="text-5xl md:text-[6rem] font-bold text-white mb-2 md:mb-6 tracking-tight leading-none 
whitespace-nowrap font-serif">Muhammed Shibili N</h1>'''
new_h1 = '''<h1 className="text-4xl sm:text-5xl md:text-[5rem] font-bold text-white mb-4 md:mb-6 tracking-tight leading-tight md:leading-none font-serif text-center md:text-left">Muhammed Shibili N</h1>'''
# Handle possible newlines in the original
code = re.sub(r'<h1 className="text-5xl md:text-\[6rem\].*?Muhammed Shibili N</h1>', new_h1, code, flags=re.DOTALL)

old_h2 = '''<h2 className="text-3xl md:text-[3.2rem] font-bold text-primary mb-8 leading-tight font-serif 
whitespace-nowrap" style={{marginTop: '-24px'}}>AI Architect &amp; Full Stack Developer</h2>'''
new_h2 = '''<h2 className="text-2xl sm:text-3xl md:text-[2.5rem] font-bold text-primary mb-6 md:mb-8 leading-tight font-serif text-center md:text-left md:-mt-6">AI Architect &amp; Full Stack Developer</h2>'''
code = re.sub(r'<h2 className="text-3xl md:text-\[3\.2rem\].*?AI Architect &amp; Full Stack Developer</h2>', new_h2, code, flags=re.DOTALL)

old_p = '''<p className="mb-16 text-lg md:text-xl font-poppins font-medium text-neutral opacity-80 max-w-xl 
leading-relaxed">'''
new_p = '''<p className="mb-10 md:mb-16 text-base sm:text-lg md:text-xl font-poppins font-medium text-neutral opacity-80 max-w-xl leading-relaxed text-center md:text-left mx-auto md:mx-0">'''
code = re.sub(r'<p className="mb-16 text-lg md:text-xl font-poppins font-medium text-neutral opacity-80 max-w-xl \s*leading-relaxed">', new_p, code)

old_btn = '''<a className="inline-block bg-[#2563eb] text-[#fff] px-10 py-5 text-lg rounded-full font-bold 
hover:scale-105 hover:brightness-110 transition-all duration-300" href="#contact">Get in Touch</a>'''
new_btn = '''<div className="flex justify-center md:justify-start w-full"><a className="inline-block bg-[#2563eb] text-[#fff] px-8 md:px-10 py-4 md:py-5 text-base md:text-lg rounded-full font-bold hover:scale-105 hover:brightness-110 transition-all duration-300" href="#contact">Get in Touch</a></div>'''
code = re.sub(r'<a className="inline-block bg-\[#2563eb\].*?Get in Touch</a>', new_btn, code, flags=re.DOTALL)

# Fix Projects Section (Sticky -> relative on mobile)
code = code.replace('sticky top-[15vh] h-[70vh]', 'relative md:sticky md:top-[15vh] h-auto md:h-[70vh] py-4 md:py-0 mb-8 md:mb-0')

# About Section image
code = code.replace('w-[300px] h-[300px] shrink-0 border-[16px]', 'w-[200px] h-[200px] md:w-[300px] md:h-[300px] shrink-0 border-[10px] md:border-[16px] mx-auto md:mx-0')

# About section text alignment on mobile
old_about = '''<h2 className="text-4xl md:text-5xl font-extrabold text-white mb-12 text-left">About Me</h2>'''
new_about = '''<h2 className="text-3xl md:text-5xl font-extrabold text-white mb-8 md:mb-12 text-center md:text-left">About Me</h2>'''
code = code.replace(old_about, new_about)

code = code.replace('<div className="flex flex-col md:flex-row gap-12 md:gap-24 items-start w-full">', '<div className="flex flex-col md:flex-row gap-10 md:gap-24 items-center md:items-start w-full">')
code = code.replace('<div className="flex-1 text-left w-full">', '<div className="flex-1 text-center md:text-left w-full">')

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Applied Mobile-First refactor")
