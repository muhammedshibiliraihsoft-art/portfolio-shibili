import re

with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Remove the GSAP imports
content = re.sub(r"import \{ gsap \} from 'gsap';\nimport \{ ScrollTrigger \} from 'gsap/ScrollTrigger';\nimport \{ useGSAP \} from '@gsap/react';\n", "", content)

# Remove the GSAP register
content = content.replace("gsap.registerPlugin(ScrollTrigger);\n\n", "")
content = content.replace("import React, { useState, useEffect, useRef } from 'react';", "import React, { useState, useEffect } from 'react';")

# Remove the useGSAP hook and refs
hook_pattern = re.compile(r'\s*const project1Ref = useRef\(null\);.*?const \[isScrolled, setIsScrolled\] = useState\(false\);', re.DOTALL)
content = hook_pattern.sub('\n  const [isScrolled, setIsScrolled] = useState(false);', content)

# Remove the refs from the sticky wrappers
content = content.replace('ref={project1Ref} ', '')
content = content.replace('ref={project2Ref} ', '')
content = content.replace('ref={project3Ref} ', '')

# Reduce project card heights and adjust max width
content = content.replace('md:h-[70vh]', 'md:h-[60vh] max-w-4xl mx-auto')
content = content.replace('md:h-[65vh]', 'md:h-[55vh]')

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
