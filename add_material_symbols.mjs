import fs from 'fs';
let code = fs.readFileSync('src/app/layout.tsx', 'utf8');

// Add Material Symbols link into <head>
if (!code.includes('Material+Symbols+Outlined')) {
  code = code.replace(
    /<head>/,
    `<head>\n        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />`
  );
  fs.writeFileSync('src/app/layout.tsx', code);
}
