import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

// Use regex to match the paragraph contents
code = code.replace(
  /<p className="text-neutral text-center text-sm">\s*Alejandro[^<]+<\/p>/g,
  '<p className="text-neutral text-center text-sm">\n            Alejandro M&uacute;nez Cuntez &copy; 2026. Designed &amp; Developed by Mois&eacute;s Machuca\n          </p>'
);

fs.writeFileSync('src/app/page.tsx', code);
