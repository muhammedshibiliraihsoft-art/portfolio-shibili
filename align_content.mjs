import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

// 1. Shift main and footer 10px left (64px -> 54px)
code = code.replace(
  /translate-x-8 md:translate-x-16/g,
  'translate-x-8 md:translate-x-[54px]'
);

// 2. Remove marginLeft from hero section inner div to align it with other sections
code = code.replace(
  /<div className="w-full text-left" style=\{\{position: 'relative', marginTop: '12px', marginLeft: '59px'\}\}>/,
  '<div className="w-full text-left" style={{position: \'relative\', marginTop: \'12px\'}}>'
);

// 3. Add whitespace-nowrap to h2 so it doesn't wrap
code = code.replace(
  /<h2 className="text-4xl md:text-\[4rem\] font-bold text-primary mb-8 leading-tight font-serif" style=\{\{marginTop: '-46px'\}\}>/,
  '<h2 className="text-4xl md:text-[4rem] font-bold text-primary mb-8 leading-tight font-serif whitespace-nowrap" style={{marginTop: \'-46px\'}}>'
);

fs.writeFileSync('src/app/page.tsx', code);
