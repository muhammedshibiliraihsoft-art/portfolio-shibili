import re

with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# The original Next.js nav is:
# {/* TopNavBar */}
# <nav ...
# ...
# </nav>

nav_pattern = re.compile(r'\{/\* TopNavBar \*/\}.*?</nav>', re.DOTALL)
content = nav_pattern.sub('<NavBar />', content)

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
