import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

code = code.replace(/LET'S BUILD/g, 'LET&apos;S BUILD');
code = code.replace(/Let's talk about it/g, 'Let&apos;s talk about it');
code = code.replace(/I'm always open/g, 'I&apos;m always open');
code = code.replace(/LET'S CONNECT/g, 'LET&apos;S CONNECT');
code = code.replace(/Let's turn your ideas/g, 'Let&apos;s turn your ideas');

fs.writeFileSync('src/app/page.tsx', code);
