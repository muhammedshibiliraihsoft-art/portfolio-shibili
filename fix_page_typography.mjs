import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

// Hero section text size and color
code = code.replace(
  /text-lg font-normal text-on-surface-variant opacity-70 md:text-2xl max-w-3xl leading-relaxed/g,
  'text-base md:text-lg font-normal text-neutral max-w-3xl leading-relaxed'
);

// Other sections description color
code = code.replace(/text-on-surface-variant/g, 'text-neutral');

// Remove opacity-70 from any other places if it exists
code = code.replace(/opacity-70/g, '');

fs.writeFileSync('src/app/page.tsx', code);
