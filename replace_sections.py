import re

with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Experience Section
exp_pattern = re.compile(r'\{/\* Experience Section \*/\}.*?\{/\* Projects Section \*/\}', re.DOTALL)
content = exp_pattern.sub('<!-- EXPERIENCE SPACE -->\n\n      {/* Projects Section */}', content)

# Replace Projects Section
proj_pattern = re.compile(r'\{/\* Projects Section \*/\}.*?\{/\* About Section \*/\}', re.DOTALL)
content = proj_pattern.sub('<!-- PROJECTS SPACE -->\n\n      {/* About Section */}', content)

# Replace About Section
about_pattern = re.compile(r'\{/\* About Section \*/\}.*?\{/\* Contact Section \*/\}', re.DOTALL)
content = about_pattern.sub('<!-- ABOUT SPACE -->\n\n      {/* Contact Section */}', content)

# Import them
imports = """// @ts-ignore
import Experience from '@/components/3d/Experience';
// @ts-ignore
import ShowcaseSection from '@/components/3d/ShowcaseSection';
// @ts-ignore
import About from '@/components/3d/About';
"""

content = content.replace("export default function PortfolioTemplate() {", imports + "\nexport default function PortfolioTemplate() {")

content = content.replace("<!-- EXPERIENCE SPACE -->", "<Experience />")
content = content.replace("<!-- PROJECTS SPACE -->", "<ShowcaseSection />")
content = content.replace("<!-- ABOUT SPACE -->", "<About />")

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
print("Sections replaced!")
