import re

# 1. Update page.tsx to import Hero normally
with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    page_content = f.read()

page_content = page_content.replace(
    "const Hero = dynamic(() => import('@/components/3d/Hero') /* @ts-ignore */, { ssr: false });",
    "import Hero from '@/components/3d/Hero';"
)
with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(page_content)

# 2. Update Hero.jsx to dynamically import HeroExperience
with open("src/components/3d/Hero.jsx", "r", encoding="utf-8") as f:
    hero_content = f.read()

hero_content = hero_content.replace(
    'import HeroExperience from "./models/hero_models/HeroExperience";',
    'import dynamic from "next/dynamic";\nconst HeroExperience = dynamic(() => import("./models/hero_models/HeroExperience"), { ssr: false });'
)

with open("src/components/3d/Hero.jsx", "w", encoding="utf-8") as f:
    f.write(hero_content)

print("Fixed SSR for Hero section!")
