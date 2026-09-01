import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

if (!code.includes('"use client"')) {
  code = '"use client";\n' + code;
}

if (!code.includes('import { useState, useEffect }')) {
  code = code.replace(/import React from 'react';/, "import React, { useState, useEffect } from 'react';");
}

const componentRegex = /export default function PortfolioTemplate\(\) \{/;
if (!code.includes('const [isScrolled, setIsScrolled]')) {
  code = code.replace(
    componentRegex,
    `export default function PortfolioTemplate() {
  const [isScrolled, setIsScrolled] = useState(false);
  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);`
  );
}

code = code.replace(
  /<div className="flex justify-between items-center max-w-max-width mx-auto px-6 md:px-12 h-16 w-full">/,
  '<div className={`flex justify-between items-center max-w-max-width mx-auto px-6 md:px-12 w-full transition-all duration-300 ${isScrolled ? "h-16" : "h-20"}`}>'
);

code = code.replace(
  /<nav className="bg-background text-primary font-body-md text-body-md fixed top-0 w-full z-50 transition-all duration-300">/,
  '<nav className={`bg-background text-primary font-body-md text-body-md fixed top-0 w-full z-50 transition-all duration-300 ${isScrolled ? "shadow-md shadow-black/50" : ""}`}>'
);

fs.writeFileSync('src/app/page.tsx', code);
