import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

// Remove glow divs
code = code.replace(/<div className="absolute inset-0 bg-primary\/20 rounded-xl blur-md opacity-0 group-focus-within:opacity-100 transition-opacity duration-500"><\/div>\s*/g, '');

// Change rounded-xl to rounded-md and remove focus-within border color for inputs
code = code.replace(/className="relative bg-\[#0c1218\] border border-outline-variant rounded-xl p-4 transition-colors focus-within:border-primary\/50"/g, 'className="relative bg-[#0c1218] border border-outline-variant rounded-md p-4 transition-colors"');

// Send Message Button - change rounded-xl to rounded-md
code = code.replace(/rounded-xl font-bold flex items-center/g, 'rounded-md font-bold flex items-center');

fs.writeFileSync('src/app/page.tsx', code);
