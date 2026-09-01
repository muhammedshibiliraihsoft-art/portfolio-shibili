import fs from 'fs';
let code = fs.readFileSync('src/app/layout.tsx', 'utf8');

code = code.replace(
  /family=Plus\+Jakarta\+Sans:wght@400;700;800&family=JetBrains\+Mono/,
  'family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=JetBrains+Mono'
);

fs.writeFileSync('src/app/layout.tsx', code);
