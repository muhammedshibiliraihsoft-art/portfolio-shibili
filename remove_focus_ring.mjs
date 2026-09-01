import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

code = code.replace(
  /focus:outline-none/g,
  'focus:outline-none focus:ring-0'
);

fs.writeFileSync('src/app/page.tsx', code);
