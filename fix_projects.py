import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Extract the individual projects
p1_match = re.search(r'(\{\/\* Project 1 \*\/\}.*?)(?=\{\/\* Project 2 \*\/\})', code, re.DOTALL)
p2_match = re.search(r'(\{\/\* Project 2 \*\/\}.*?)(?=\{\/\* Project 3 \*\/\})', code, re.DOTALL)
p3_match = re.search(r'(\{\/\* Project 3 \*\/\}.*?)(?=\{\/\* Duplicated Set|<\/div>\s*<\/section>)', code, re.DOTALL)

if p1_match and p2_match and p3_match:
    def wrap_sticky(html, z_index):
        # Remove any FadeUp tags
        html = re.sub(r'<FadeUp[^>]*>\s*', '', html)
        html = re.sub(r'\s*</FadeUp>', '', html)
        return f'\n            <div className="sticky top-0 h-[100vh] flex items-center justify-center w-full" style={{{{ zIndex: {z_index} }}}}>\n              {html.strip()}\n            </div>'

    new_section = (
        '        <section className="max-w-[1100px] mx-auto px-6 py-section-gap w-full text-left" id="projects">\n'
        '          <h2 className="text-4xl md:text-5xl font-extrabold text-white mb-12 text-left">Featured Projects</h2>\n'
        '          <div className="relative w-full">'
        + wrap_sticky(p1_match.group(1), 1) +
        wrap_sticky(p2_match.group(1), 2) +
        wrap_sticky(p3_match.group(1), 3) +
        '\n          </div>\n'
        '        </section>'
    )
    
    # Replace the section
    code = re.sub(r'<section className="max-w-\[1100px\] mx-auto px-6 py-section-gap w-full text-left" id="projects">.*?</section>', new_section, code, flags=re.DOTALL)
    
    # Remove FadeUp component definition
    code = re.sub(r'function FadeUp.*?return \(\n.*?</div>\n  \);\n}\n', '', code, flags=re.DOTALL)
    code = code.replace("import React, { useState, useEffect, useRef, ReactNode } from 'react';", "import React, { useState, useEffect } from 'react';")
    
    with open('src/app/page.tsx', 'w') as f:
        f.write(code)
    print("Success")
else:
    print("Failed to find projects")
