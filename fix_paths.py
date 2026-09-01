import os

def replace_in_file(filepath, replacements):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    for old, new in replacements.items():
        content = content.replace(old, new)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

replace_in_file("src/components/3d/Experience.jsx", {
    'import { expCards } from "../constants";': 'import { expCards } from "../../constants";',
    'import TitleHeader from "../components/TitleHeader";': 'import TitleHeader from "./TitleHeader";',
    'import GlowCard from "../components/GlowCard";': 'import GlowCard from "./GlowCard";'
})

replace_in_file("src/components/3d/About.jsx", {
    'import TitleHeader from "../components/TitleHeader";': 'import TitleHeader from "./TitleHeader";'
})

print("Paths fixed!")
