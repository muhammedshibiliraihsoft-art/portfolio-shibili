import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

code = code.replace(/<div className="w-full text-left scale-90 origin-left translate-x-8 md:translate-x-16 transition-transform"/, '<div className="w-full text-left"');

code = code.replace(/<main className="flex-grow pt-32">/, '<main className="flex-grow pt-32 scale-90 origin-left translate-x-8 md:translate-x-16 transition-transform">');

code = code.replace(/<footer className="bg-background text-primary/, '<footer className="scale-90 origin-left translate-x-8 md:translate-x-16 transition-transform bg-background text-primary');

fs.writeFileSync('src/app/page.tsx', code);
