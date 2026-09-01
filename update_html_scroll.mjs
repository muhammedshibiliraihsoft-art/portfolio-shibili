import fs from 'fs';
let code = fs.readFileSync('src/app/layout.tsx', 'utf8');

code = code.replace(
  /<html lang="en" className="dark">/,
  '<html lang="en" className="dark scroll-smooth scroll-pt-32">'
);

fs.writeFileSync('src/app/layout.tsx', code);
