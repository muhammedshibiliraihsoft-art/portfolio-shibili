import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# 1. Update the RaihSoft image link
code = code.replace('src="/RaihSoft.png"', 'src="https://media.raihsuite.com/RS0013/raihsoft-logo-light.PNG"')

# 2. Update the subtitle for the 3rd experience
code = code.replace('<h4 className="text-lg md:text-xl font-medium text-neutral mb-6">Frontend Engineering</h4>', 
                    '<h4 className="text-lg md:text-xl font-medium text-neutral mb-6">Full-Stack Development &middot; Internship</h4>')

# 3. Update the description for the 3rd experience
old_desc = '<p className="text-base md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Designed and developed scalable React architectures focusing on performance, reusability, and clean code.</p>'
new_desc = '<p className="text-base md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Developing scalable web applications across frontend and backend systems, with a focus on performance, maintainable architecture, seamless user experiences, and clean code.</p>'
code = code.replace(old_desc, new_desc)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Updated last experience successfully.")
