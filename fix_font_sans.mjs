import fs from 'fs';
let code = fs.readFileSync('tailwind.config.ts', 'utf8');

if (!code.includes('"sans":')) {
  code = code.replace(
    /"fontFamily": \{/,
    '"fontFamily": {\n    "sans": ["var(--font-be-vietnam-pro)", "sans-serif"],'
  );
}

fs.writeFileSync('tailwind.config.ts', code);
