import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the <section id="projects"> block
# We will locate the <div className="flex flex-col gap-12"> and replace it with the new structure.

start_marker = '<div className="flex flex-col gap-12">'
end_marker = '</section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    # Extract the cards HTML
    cards_html = content[start_idx + len(start_marker) : end_idx].strip()
    
    # Wait, the cards HTML currently has <FadeUp delay={...}> wrappers. We must remove them!
    cards_html = re.sub(r'<FadeUp delay=\{[0-9]+\}>', '', cards_html)
    cards_html = re.sub(r'</FadeUp>', '', cards_html)
    # Fix the trailing </div> of the gap-12 container
    cards_html = cards_html.rsplit('</div>', 1)[0]
    
    # Trim and prepare the cloned HTML
    original_cards = cards_html
    
    new_html = f'''<div className="projects-marquee">
            <div className="projects-track">
              {{/* Original Set */}}
              {original_cards}
              
              {{/* Duplicated Set for Infinite Scroll */}}
              {original_cards}
            </div>
          </div>'''
    
    final_content = content[:start_idx] + new_html + '\n        ' + content[end_idx:]
    
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Success")
else:
    print("Could not find markers")
