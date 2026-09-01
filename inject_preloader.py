with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

imports = "import Preloader from '@/components/Preloader';\n"
content = content.replace("export default function PortfolioTemplate() {", imports + "export default function PortfolioTemplate() {")

content = content.replace("<NavBar />", "<Preloader />\n      <NavBar />")

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
print("Preloader injected!")
