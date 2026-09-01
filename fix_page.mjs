import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

code = code.replace(/I'm/g, "I&apos;m");
code = code.replace(/Spotify's/g, "Spotify&apos;s");
code = code.replace(/what's/g, "what&apos;s");
code = code.replace(/I've/g, "I&apos;ve");

code = code.replace(/href="#"/g, 'href="/"');

code = code.replace(/<img(?![^>]*alt=)/g, '<img alt="" ');

fs.writeFileSync('src/app/page.tsx', code);
