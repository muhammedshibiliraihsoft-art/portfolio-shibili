import os
from PIL import Image

public_dir = 'public'

for filename in os.listdir(public_dir):
    if filename.lower().endswith('.png'):
        png_path = os.path.join(public_dir, filename)
        webp_filename = filename[:-4] + '.webp'
        webp_path = os.path.join(public_dir, webp_filename)
        
        try:
            with Image.open(png_path) as img:
                img.save(webp_path, 'WEBP', quality=85)
                print(f"Converted {filename} to {webp_filename}")
            
            # Optionally delete the original PNG
            # os.remove(png_path)
            
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

# Update references in page.tsx
page_path = 'src/app/page.tsx'
with open(page_path, 'r') as f:
    code = f.read()

# Replace png extensions (that we know we used)
code = code.replace('"/profile.png"', '"/profile.webp"')
code = code.replace('"/AccoutSoft-light.png"', '"/AccoutSoft-light.webp"')
code = code.replace('"/charity.png"', '"/charity.webp"')
code = code.replace('"/festival.png"', '"/festival.webp"')

with open(page_path, 'w') as f:
    f.write(code)

print("Updated page.tsx references to .webp")
