import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

code = code.replace(
  /Muhammed Shibili N &copy; 2026\. Designed &amp; Developed by MoisAcs Machuca/,
  'Alejandro Múnez Cuntez &copy; 2026. Designed &amp; Developed by Moisés Machuca'
);
code = code.replace(
  /Muhammed Shibili N &copy; 2026\. Designed &amp; Developed by Moisés Machuca/,
  'Alejandro Múnez Cuntez &copy; 2026. Designed &amp; Developed by Moisés Machuca'
);

fs.writeFileSync('src/app/page.tsx', code);
