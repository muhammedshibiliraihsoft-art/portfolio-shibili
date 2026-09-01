import fs from 'fs';
let code = fs.readFileSync('tailwind.config.ts', 'utf8');

const brandColors = `
    "brand": {
      "DEFAULT": "hsl(var(--color-brand) / <alpha-value>)",
      "light": "#5ab0ff",
      "dark": "#004a7f"
    },
    "on-primary":`;

code = code.replace(/"on-primary":/, brandColors);
fs.writeFileSync('tailwind.config.ts', code);
