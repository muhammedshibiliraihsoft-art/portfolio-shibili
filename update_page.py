# -*- coding: utf-8 -*-
import re

with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Update Projects Images
content = content.replace("/AccoutSoft-light.png", "/AccoutSoft-light.webp")
content = content.replace("/charity.png", "/charity.webp")
content = content.replace("/festival.png", "/festival.webp")

# Update Profile image
content = content.replace("/profile.png", "/profile.webp")

# About Section Update
old_about1 = "I am a dedicated software engineer with a strong passion for building beautiful, responsive, and highly functional digital experiences. My journey in tech started out of curiosity and quickly became a lifelong pursuit of mastering both the frontend aesthetics and backend logic."
new_about1 = "I am an aspiring software engineer passionate about building modern, intelligent, and user-focused digital experiences. My journey in technology began with curiosity and has grown into a continuous pursuit of learning software development, AI, and agentic systems while strengthening my foundation in both frontend and backend engineering."

old_about2 = "When I'm not coding, you can find me exploring new technologies, experimenting with design systems, or contributing to open-source projects. I believe in writing code that is not only effective but also maintainable and clean."
new_about2 = "When I'm not coding, I enjoy exploring emerging technologies, experimenting with AI-powered solutions, and turning ideas into practical projects. I believe in writing clean, maintainable code and continuously improving my skills by learning, building, and solving real-world problems."

content = content.replace(old_about1, new_about1)
content = content.replace(old_about2, new_about2)

# Skills Tags
old_skills = """<span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">React / Next.js</span>
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">TypeScript</span>
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Tailwind CSS</span>
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Node.js</span>
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Figma</span>"""

new_skills = """<span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">React / Next.js</span>
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">TypeScript</span>
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Node.js</span>
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Python</span>
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Antigravity</span>
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Codex</span>"""

content = content.replace(old_skills, new_skills)

# Job 3 Logo block
# Wait, I didn't verify if I actually replaced the Job 1/3 text in the FIRST script.
# Let's just do it here too just in case.
content = content.replace("2024 &mdash; 2025", "2026")
content = content.replace("Tech Corp", "RaihSoft")
content = content.replace("Frontend Engineering", "Full-Stack Development &middot; Internship")
content = content.replace("Designed and developed scalable React architectures focusing on performance, reusability, and clean code.", "Developing scalable web applications across frontend and backend systems, with a focus on performance, maintainable architecture, seamless user experiences, and clean code.")


old_job3_date = '<p className="text-primary font-bold text-lg font-poppins tracking-wider uppercase mb-2">2026</p>\n                <p className="text-neutral text-sm uppercase tracking-widest font-bold opacity-50">RaihSoft</p>'
new_job3_date = """<p className="text-primary font-bold text-lg font-poppins tracking-wider uppercase mb-2">2026</p>
                <a href="https://www.raihsoft.com" target="_blank" rel="noopener noreferrer" className="block mb-2">
                  <img 
                    src="https://media.raihsuite.com/RS0013/raihsoft-logo-light.PNG"
                    alt="RaihSoft"
                    style={{ height: '19px', marginLeft: '-5px', opacity: 0.8, objectFit: 'contain' }}
                  />
                </a>
                <p className="text-neutral text-sm uppercase tracking-widest font-bold opacity-50">RaihSoft</p>"""

if '<a href="https://www.raihsoft.com"' not in content:
    content = content.replace(old_job3_date, new_job3_date)

# Footer Social Links
old_socials = """<a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">Twitter <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">LinkedIn <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">Github <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">Youtube <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="/">Dribbble <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>"""

new_socials = """<a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="https://github.com/shibilikds">Github <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="https://www.instagram.com/shib_ili_y/">Instagram <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="https://www.facebook.com/profile.php?id=100082191128704">Facebook <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-[#a78bfa] hover:text-primary transition-colors flex items-center gap-1 group" href="https://www.raihsoft.com">RaihSoft <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>"""

content = content.replace(old_socials, new_socials)

# Profile Polaroid Frame Class adjustments
old_profile_frame = "w-[200px] h-[200px] md:w-[300px] md:h-[300px] shrink-0 border-[10px] md:border-[16px] border-white shadow-2xl rotate-3 hover:rotate-0 transition-transform duration-500 mx-auto md:mx-0"
new_profile_frame = "w-[200px] h-[200px] md:w-[300px] md:h-[300px] shrink-0 bg-white p-3 md:p-4 pb-12 md:pb-16 shadow-2xl -rotate-3 hover:rotate-0 transition-transform duration-500 mx-auto md:mx-0"

content = content.replace(old_profile_frame, new_profile_frame)

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated page.tsx!")
