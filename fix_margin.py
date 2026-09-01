import re

with open('src/app/globals.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace project-card CSS
old_card_css = '''
.project-card {
  margin-top: -80px; /* Overlap effect */
  position: relative;
}

.project-card:first-child {
  margin-top: 0;
}
'''

new_card_css = '''
.project-card {
  margin-bottom: -80px; /* Overlap effect */
  position: relative;
}
'''

content = content.replace(old_card_css.strip(), new_card_css.strip())

with open('src/app/globals.css', 'w', encoding='utf-8') as f:
    f.write(content)
