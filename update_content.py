import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# 1. Hero text (Remove 'Developer based in San Francisco, USA. ')
code = code.replace('Developer based in San Francisco, USA. I specialize', 'I specialize')

# 2. Tech Corp to RaihSoft PNG
# The text is: <p className="text-neutral text-sm uppercase tracking-widest font-bold opacity-50">Tech Corp</p>
# "text-sm" is 14px. User asked for 1 pixel larger, so 15px height.
# I will replace it with: <img src="/RaihSoft.png" alt="RaihSoft" style={{ height: '15px' }} className="opacity-80" />
old_tech_corp = '<p className="text-neutral text-sm uppercase tracking-widest font-bold opacity-50">Tech Corp</p>'
new_tech_corp = '<img src="/RaihSoft.png" alt="RaihSoft" style={{ height: \'15px\' }} className="opacity-80 object-contain" />'
code = code.replace(old_tech_corp, new_tech_corp)

# 3. Email
code = code.replace('hello@shibili.dev', 'shibili.n@zohomail.in')

# 4. Social Links
# Existing:
# <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">Twitter <span ...>north_east</span></a>
# <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">LinkedIn <span ...>north_east</span></a>
# <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">Github <span ...>north_east</span></a>
# <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">Youtube <span ...>north_east</span></a>
# <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">Dribbble <span ...>north_east</span></a>

old_social = '''<div className="flex flex-wrap justify-center gap-8 mb-4">
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">Twitter <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">LinkedIn <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">Github <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">Youtube <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">Dribbble <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
          </div>'''

new_social = '''<div className="flex flex-wrap justify-center gap-8 mb-4">
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="https://github.com/shibilikds" target="_blank" rel="noopener noreferrer">Github <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="https://www.instagram.com/shib_ili_y/" target="_blank" rel="noopener noreferrer">Instagram <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="https://www.facebook.com/profile.php?id=100082191128704" target="_blank" rel="noopener noreferrer">Facebook <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
          </div>'''

if old_social in code:
    code = code.replace(old_social, new_social)
else:
    # Use regex if exact match fails
    code = re.sub(r'<div className="flex flex-wrap justify-center gap-8 mb-4">.*?</div>', new_social, code, flags=re.DOTALL)


# 5. About Me Content
old_about = '''<p className="text-lg md:text-2xl text-neutral font-poppins font-medium leading-relaxed opacity-90 mb-8">
                I am a dedicated software engineer with a strong passion for building beautiful, responsive, and highly functional digital experiences. My journey in tech started out of curiosity and quickly became a lifelong pursuit of mastering both the frontend aesthetics and backend logic.
              </p>
              <p className="text-lg md:text-2xl text-neutral font-poppins font-medium leading-relaxed opacity-90 mb-8">
                When I'm not coding, you can find me exploring new technologies, experimenting with design systems, or contributing to open-source projects. I believe in writing code that is not only effective but also maintainable and clean.
              </p>'''

new_about = '''<p className="text-lg md:text-2xl text-neutral font-poppins font-medium leading-relaxed opacity-90 mb-8">
                I am an aspiring software engineer passionate about building modern, intelligent, and user-focused digital experiences. My journey in technology began with curiosity and has grown into a continuous pursuit of learning software development, AI, and agentic systems while strengthening my foundation in both frontend and backend engineering.
              </p>
              <p className="text-lg md:text-2xl text-neutral font-poppins font-medium leading-relaxed opacity-90 mb-8">
                When I'm not coding, I enjoy exploring emerging technologies, experimenting with AI-powered solutions, and turning ideas into practical projects. I believe in writing clean, maintainable code and continuously improving my skills by learning, building, and solving real-world problems.
              </p>'''
              
code = code.replace(old_about, new_about)
if new_about not in code:
    # Regex fallback for About
    code = re.sub(
        r'<p className="text-lg md:text-2xl text-neutral font-poppins font-medium leading-relaxed opacity-90 mb-8">\s*I am a dedicated software engineer.*?</p>\s*<p className="text-lg md:text-2xl text-neutral font-poppins font-medium leading-relaxed opacity-90 mb-8">\s*When I\'m not coding,.*?</p>',
        new_about,
        code,
        flags=re.DOTALL
    )

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Content updated.")
