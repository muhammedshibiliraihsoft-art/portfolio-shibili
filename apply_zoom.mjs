import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

// 1. Add zoom to main and fix top padding
code = code.replace(
  /<main className="flex-grow pt-8">/,
  '<main className="flex-grow pt-28 md:pt-32" style={{ zoom: 0.75 }}>'
);

// 2. Add zoom to footer
code = code.replace(
  /<footer className="bg-background text-primary/,
  '<footer style={{ zoom: 0.75 }} className="bg-background text-primary'
);

// 3. Remove negative margin from hero section wrapper to stop it from going under the nav bar
code = code.replace(
  /<div className="w-full text-left" style=\{\{position: 'relative', marginTop: '-12px'\}\}>/,
  '<div className="w-full text-left" style={{position: \'relative\'}}>'
);

fs.writeFileSync('src/app/page.tsx', code);
