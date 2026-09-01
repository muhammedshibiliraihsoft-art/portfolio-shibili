import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

// The main paragraphs have these common classes
code = code.replace(/text-base md:text-lg text-neutral/g, 'text-lg md:text-xl text-neutral font-poppins font-medium opacity-80');
code = code.replace(/text-base md:text-lg font-normal text-neutral/g, 'text-lg md:text-xl font-poppins font-medium text-neutral opacity-80');

fs.writeFileSync('src/app/page.tsx', code);
