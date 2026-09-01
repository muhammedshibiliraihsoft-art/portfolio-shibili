import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

// Add import at the top
if (!code.includes('ContactPageClient')) {
  code = code.replace(
    /import \{ useState, useEffect \} from 'react';/,
    "import { useState, useEffect } from 'react';\nimport ContactPageClient from '@/components/contact/ContactPageClient';"
  );
}

// Replace static form with ContactPageClient
// Note: Regex spans multiple lines. Using a trick to match everything between <form ...> and </form>
code = code.replace(/<form className="space-y-6">[\s\S]*?<\/form>/, '<ContactPageClient />');

fs.writeFileSync('src/app/page.tsx', code);
