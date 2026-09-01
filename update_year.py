import re

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Replace '2024 &mdash; 2025' with '2026'
old_year = '2024 &mdash; 2025'
new_year = '2026'

code = code.replace(old_year, new_year)

with open('src/app/page.tsx', 'w') as f:
    f.write(code)

print("Updated year to 2026.")
