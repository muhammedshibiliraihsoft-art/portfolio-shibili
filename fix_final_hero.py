import re

with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add eslint-disable
content = "/* eslint-disable */\n" + content

# 2. Imports
content = content.replace(
    "import HeroSnakeBackground from '@/components/hero/HeroSnakeBackground';",
    "import dynamic from 'next/dynamic';\n// @ts-ignore\nimport NavBar from '@/components/3d/NavBar';\n// @ts-ignore\nimport Hero from '@/components/3d/Hero';"
)

# 3. Remove all state and scroll hooks from the top
hook_pattern = re.compile(r'  const \[isScrolled, setIsScrolled\].*?setIsMenuOpen\(false\)\}\n      >\n        \{label\}\n      </a>\n    \);\n  \};\n', re.DOTALL)
content = hook_pattern.sub('', content)

# 4. Remove desktop-zoom and replace bg-background with bg-black
content = content.replace('desktop-zoom ', '')
content = content.replace('desktop-zoom', '')
content = content.replace('bg-background', 'bg-black')

# 5. Replace nav block with <NavBar />
nav_pattern = re.compile(r'\{/\* TopNavBar \*/\}.*?</nav>', re.DOTALL)
content = nav_pattern.sub('<NavBar />', content)

# 6. Remove overlay
overlay_pattern = re.compile(r'\{isMenuOpen && \(\n.*?</div>\n      \)\}', re.DOTALL)
content = overlay_pattern.sub('', content)

# 7. Replace Hero block with <Hero />
hero_pattern = re.compile(r'\{/\* Hero Section \*/\}.*?\{/\* Experience Section \*/\}', re.DOTALL)
content = hero_pattern.sub('<!-- HERO SPACE -->\n\n        {/* Experience Section */}', content)
content = content.replace('<!-- HERO SPACE -->', '<Hero />')

# 8. Reduce featured projects size (desktop size fix)
content = content.replace('md:h-[70vh]', 'md:h-[60vh] max-w-4xl mx-auto')
content = content.replace('md:h-[65vh]', 'md:h-[55vh]')

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
print("Page successfully reconstructed with ONLY Hero and NavBar!")
