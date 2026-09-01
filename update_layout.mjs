import fs from 'fs';
const layoutPath = 'src/app/layout.tsx';
let code = fs.readFileSync(layoutPath, 'utf8');

code = code.replace(/<html lang="en">/, '<html lang="en" className="dark">');

const fonts = `
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
      </head>
      <body>`;
code = code.replace(/<body>/, fonts);

code = code.replace(/<header[\s\S]*?<\/header>/, '');
code = code.replace(/<main className="container-base">(\{children\})<\/main>/, '<main>$1</main>');
code = code.replace(/<footer[\s\S]*?<\/footer>/, '');

fs.writeFileSync(layoutPath, code);
