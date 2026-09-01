import fs from 'fs';
const html = fs.readFileSync('templates/source-reference/alejandro-portfolio/index.html', 'utf8');
const match = html.match(/tailwind\.config = (\{[\s\S]*?\})\s*<\/script>/);
if (match) {
  const configStr = match[1];
  let configObj = eval('(' + configStr + ')');
  const tailwindPath = 'tailwind.config.ts';
  const oldConfig = fs.readFileSync(tailwindPath, 'utf8');
  let newExtendStr = JSON.stringify(configObj.theme.extend, null, 2);
  let newConfig = oldConfig.replace(/extend: \{[\s\S]*?\},?\s*plugins/, `extend: ${newExtendStr},\n  plugins`);
  fs.writeFileSync(tailwindPath, newConfig);
  console.log('Updated tailwind.config.ts');
} else {
  console.log('No tailwind config found');
}
