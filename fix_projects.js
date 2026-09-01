const fs = require('fs');
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

const project1 = code.match(/\{\/\* Project 1 \*\/\}.*?\{\/\* Project 2 \*\/\}/s)[0].replace(/\{\/\* Project 2 \*\/\}/, '').trim();
const project2 = code.match(/\{\/\* Project 2 \*\/\}.*?\{\/\* Project 3 \*\/\}/s)[0].replace(/\{\/\* Project 3 \*\/\}/, '').trim();

const p3Match = code.match(/(\{\/\* Project 3 \*\/\}.*?)\n\s*\{\/\* Duplicated Set/s);
let p3Content = p3Match ? p3Match[1] : code.match(/\{\/\* Project 3 \*\/\}.*?<\/div>\s*<\/div>\s*<\/section>/s)[0].replace(/<\/div>\s*<\/div>\s*<\/section>/, '');
p3Content = p3Content.trim();

// Strip any <FadeUp delay={...}> and </FadeUp> that might still be in the p1, p2, p3 blocks
const cleanFadeUp = (html) => {
  return html.replace(/<FadeUp[^>]*>\s*/g, '').replace(/\s*<\/FadeUp>/g, '');
};

const wrapSticky = (content, zIndex) => {
  return \
            <div className="sticky top-0 h-[100vh] flex items-center justify-center w-full" style={{ zIndex: \ }}>
              \
            </div>\;
};

const newProjectsHTML = \
        <section className="max-w-[1100px] mx-auto px-6 py-section-gap w-full text-left" id="projects">
          <h2 className="text-4xl md:text-5xl font-extrabold text-white mb-12 text-left">Projects</h2>
          <div className="relative w-full">
\
\
\
          </div>
        </section>\;

const sectionMatch = code.match(/<section className="max-w-\[1100px\] mx-auto px-6 py-section-gap w-full text-left" id="projects">.*?<\/section>/s);
if (sectionMatch) {
  code = code.replace(sectionMatch[0], newProjectsHTML);
  code = code.replace(/function FadeUp.*?return \(\n.*?<\/div>\n  \);\n}\n/s, '');
  code = code.replace(/import React, \{ useState, useEffect, useRef, ReactNode \} from 'react';/, "import React, { useState, useEffect } from 'react';");
  fs.writeFileSync('src/app/page.tsx', code);
  console.log('Successfully replaced projects section');
} else {
  console.log('Could not find projects section');
}
