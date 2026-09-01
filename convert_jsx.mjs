import fs from 'fs';

let html = fs.readFileSync('templates/source-reference/alejandro-portfolio/index.html', 'utf8');

// Extract body inner content
const bodyMatch = html.match(/<body[^>]*>([\s\S]*?)<\/body>/);
let bodyContent = bodyMatch ? bodyMatch[1] : '';

// Remove any lingering script tags
bodyContent = bodyContent.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');

// class -> className
bodyContent = bodyContent.replace(/class=/g, 'className=');

// Self close img, hr, br, input
bodyContent = bodyContent.replace(/<(img|hr|br|input)([^>]*?)(?<!\/)>/g, '<$1$2 />');

// Handle style="opacity: 1;"
bodyContent = bodyContent.replace(/style="([^"]*)"/g, (match, p1) => {
  const styles = p1.split(';').filter(s => s.trim());
  let obj = '{';
  styles.forEach(s => {
    let [key, val] = s.split(':');
    if (!key || !val) return;
    key = key.trim().replace(/-([a-z])/g, (g) => g[1].toUpperCase());
    val = val.trim();
    // if val contains single quotes, use double quotes, else single quotes
    obj += `${key}: '${val}', `;
  });
  obj += '}';
  return `style={{${obj.slice(1, -1)}}}`;
});

// HTML comments to JSX comments
bodyContent = bodyContent.replace(/<!--([\s\S]*?)-->/g, '{/* $1 */}');

// The layout already adds the html/body tags, so we just return the fragments.
// Wait, the body has these classes: "antialiased selection:bg-primary selection:text-white flex flex-col min-h-screen bg-background"
// Let's wrap it in a div with those classes.

const pageTsx = `
export default function PortfolioTemplate() {
  return (
    <div className="antialiased selection:bg-primary selection:text-white flex flex-col min-h-screen bg-background">
      ${bodyContent}
    </div>
  );
}
`;

fs.writeFileSync('src/app/page.tsx', pageTsx);
console.log('Updated page.tsx');
