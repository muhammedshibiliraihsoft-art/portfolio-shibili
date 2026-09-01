import fs from 'fs';
const tailwindPath = 'tailwind.config.ts';
let code = fs.readFileSync(tailwindPath, 'utf8');

if (!code.includes('darkMode')) {
  code = code.replace(/theme: \{/, "darkMode: 'class',\n  theme: {");
  fs.writeFileSync(tailwindPath, code);
}
