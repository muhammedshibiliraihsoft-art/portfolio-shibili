def replace_in_file(filepath, replacements):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    for old, new in replacements.items():
        content = content.replace(old, new)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

replace_in_file("src/components/3d/TechStack.jsx", {
    'import TitleHeader from "../components/TitleHeader";': 'import TitleHeader from "./TitleHeader";',
    'import TechIconCardExperience from "../components/models/tech_logos/TechIconCardExperience";': 'import dynamic from "next/dynamic";\nconst TechIconCardExperience = dynamic(() => import("./models/tech_logos/TechIconCardExperience"), { ssr: false });',
    'import { techStackIcons } from "../constants";': 'import { techStackIcons } from "../../constants";'
})
print("TechStack fixed!")
