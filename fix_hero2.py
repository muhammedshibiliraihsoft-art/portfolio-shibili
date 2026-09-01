with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

old = '''          <div className="w-full flex flex-col md:flex-row items-center gap-8 md:gap-0" style={{position: 'relative'}}>
              {/* Left: text content */}
              <div className="flex-1 text-left md:pr-8 z-10">
            <h1 className="text-5xl md:text-[6rem] font-bold text-white mb-2 md:mb-6 tracking-tight leading-none whitespace-nowrap font-serif">Muhammed Shibili N</h1>
            <h2 className="text-3xl md:text-[3.2rem] font-bold text-primary mb-8 leading-tight font-serif whitespace-nowrap" style={{marginTop: '-24px'}}>AI Architect &amp; Full Stack Developer</h2>
            <p className="mb-16 text-lg md:text-xl font-poppins font-medium text-neutral opacity-80 max-w-3xl leading-relaxed">
              Developer based in San Francisco, USA. I specialize in UI design, web and mobile application development and maintenance.
            </p>
            <a className="inline-block bg-[#2563eb] text-[#fff] px-10 py-5 text-lg rounded-full font-bold hover:scale-105 hover:brightness-110 transition-all duration-300" href="#contact">Get in Touch</a>
              </div>
              {/* Right: AI Globe */}
              <div className="hidden md:flex flex-shrink-0 items-center justify-center" style={{ width: '480px', height: '480px', marginRight: '-80px' }}>
                <AIGlobe />
              </div>
            </div>
          </section>'''

new = '''          <div className="w-full flex flex-col md:flex-row items-center gap-8 md:gap-0" style={{position: 'relative'}}>
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
          </div>
        </section>'''

if old in code:
    code = code.replace(old, new, 1)
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Fixed indentation/structure")
else:
    print("String not found exactly")
