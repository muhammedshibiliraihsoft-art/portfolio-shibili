import fs from 'fs';
let code = fs.readFileSync('tailwind.config.ts', 'utf8');

code = code.replace(
  /"fontFamily": \{/,
  '"fontFamily": {\n    "poppins": ["Poppins", "sans-serif"],'
);

fs.writeFileSync('tailwind.config.ts', code);
