import re

with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# The regex to remove the unused states, useEffect, and navLink function
pattern = re.compile(r'  const \[isScrolled.*?return \(\n', re.DOTALL)

# Let's verify what we match first
match = pattern.search(content)
if match:
    # Just replace it directly with the return (
    content = content[:match.start()] + "  return (\n" + content[match.end():]

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
