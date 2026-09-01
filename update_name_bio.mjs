import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

// Update Footer text
code = code.replace(
  /Alejandro M&uacute;nez Cuntez &copy; 2026\. Designed &amp; Developed by Mois&eacute;s Machuca/,
  'Muhammed Shibili N &copy; 2026. Designed &amp; Developed by Muhammed Shibili N'
);

// Update About section text
const oldAboutRegex = /Hi, I&apos;m Alejandro[^<]+/g;
const newAboutText = "Hi, I&apos;m Muhammed Shibili N, an aspiring AI Architect and Full Stack Developer focused on building practical and scalable digital products. I&apos;m passionate about turning real-world ideas into useful software using modern web technologies, backend systems, databases, and AI-powered solutions. My development journey has been driven by self-learning and hands-on project development, where I continuously explore application architecture, clean code, responsive interfaces, APIs, and intelligent automation. I&apos;m especially interested in agentic AI and how intelligent systems can work with tools, data, and software to solve complex problems. My goal is to build reliable products that combine thoughtful design, strong engineering, and practical AI capabilities.";

code = code.replace(oldAboutRegex, newAboutText);

fs.writeFileSync('src/app/page.tsx', code);
