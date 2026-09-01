import fs from 'fs';
let code = fs.readFileSync('tailwind.config.ts', 'utf8');

code = code.replace(/Plus Jakarta Sans/g, 'Be Vietnam Pro');
code = code.replace(/"colors": \{/, '"colors": {\n    "neutral": "#94a3b8",');

fs.writeFileSync('tailwind.config.ts', code);
