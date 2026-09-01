import fs from 'fs';
let code = fs.readFileSync('src/app/layout.tsx', 'utf8');

// Add Poppins to the Google Fonts link
code = code.replace(
  /family=Be\+Vietnam\+Pro:wght@400;500;600;700;800&family=JetBrains\+Mono/,
  'family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=Poppins:wght@400;500;600;700&family=JetBrains+Mono'
);

fs.writeFileSync('src/app/layout.tsx', code);
