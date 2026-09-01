import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

code = code.replace(
  /<nav className="bg-transparent backdrop-blur-xl text-primary font-body-md text-body-md fixed top-0 w-full z-50 transition-all duration-300">/,
  '<nav className="bg-background text-primary font-body-md text-body-md fixed top-0 w-full z-50 transition-all duration-300">'
);

code = code.replace(
  /<div className="flex justify-between items-center max-w-max-width mx-auto px-6 md:px-12 h-20 w-full">/,
  '<div className="flex justify-between items-center max-w-max-width mx-auto px-6 md:px-12 h-16 w-full">'
);

fs.writeFileSync('src/app/page.tsx', code);
