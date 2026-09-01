import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

// 1. Remove hacky scale and translate from main and footer
code = code.replace(
  /<main className="flex-grow pt-16 scale-90 origin-left translate-x-8 md:translate-x-\[54px\] transition-transform">/,
  '<main className="flex-grow pt-8">'
);
code = code.replace(
  /<footer className="scale-90 origin-left translate-x-8 md:translate-x-\[54px\] transition-transform bg-background text-primary/,
  '<footer className="bg-background text-primary'
);

// 2. Scale down font sizes by ~20%
// h1: 7.5rem -> 6rem
code = code.replace(
  /text-6xl md:text-\[7.5rem\] font-bold text-white mb-2 md:mb-6 tracking-tight leading-none whitespace-nowrap font-serif/,
  'text-5xl md:text-[6rem] font-bold text-white mb-2 md:mb-6 tracking-tight leading-none whitespace-nowrap font-serif'
);

// h2: 4rem -> 3.2rem, and adjust margin-top since size is smaller
code = code.replace(
  /text-4xl md:text-\[4rem\] font-bold text-primary mb-8 leading-tight font-serif whitespace-nowrap" style=\{\{marginTop: '-46px'\}\}/,
  'text-3xl md:text-[3.2rem] font-bold text-primary mb-8 leading-tight font-serif whitespace-nowrap" style={{marginTop: \'-24px\'}}'
);

// Descriptions: text-xl md:text-2xl -> text-lg md:text-xl
code = code.replace(/text-xl md:text-2xl/g, 'text-lg md:text-xl');

// Button size: text-2xl -> text-lg, px-14 py-7 -> px-10 py-5
code = code.replace(
  /px-14 py-7 text-2xl rounded-full/,
  'px-10 py-5 text-lg rounded-full'
);

fs.writeFileSync('src/app/page.tsx', code);
