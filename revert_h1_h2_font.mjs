import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

code = code.replace(
  /<h1 className="text-6xl md:text-\[7.5rem\] font-bold text-white mb-2 md:mb-6 tracking-tight leading-none whitespace-nowrap font-sans">/,
  '<h1 className="text-6xl md:text-[7.5rem] font-bold text-white mb-2 md:mb-6 tracking-tight leading-none whitespace-nowrap font-serif">'
);

code = code.replace(
  /<h2 className="text-4xl md:text-\[4rem\] font-bold text-primary mb-8 leading-tight font-sans" style=\{\{marginTop: '-46px'\}\}>/,
  '<h2 className="text-4xl md:text-[4rem] font-bold text-primary mb-8 leading-tight font-serif" style={{marginTop: \'-46px\'}}>'
);

fs.writeFileSync('src/app/page.tsx', code);
