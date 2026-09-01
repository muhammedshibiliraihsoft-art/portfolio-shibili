import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

code = code.replace(
  /<section className="max-w-\[1100px\] mx-auto px-6 py-section-gap flex flex-col items-start w-full">/,
  '<section className="max-w-[1100px] mx-auto px-6 pb-section-gap pt-0 md:pt-4 flex flex-col items-start w-full justify-center min-h-[calc(100vh-200px)]">'
);

code = code.replace(/<main className="flex-grow pt-32/, '<main className="flex-grow pt-24');

fs.writeFileSync('src/app/page.tsx', code);
