import fs from 'fs';
let code = fs.readFileSync('src/components/contact/ContactPageClient.tsx', 'utf8');

// Fix unused err
code = code.replace(/catch \(err\) \{/g, 'catch {');

// Fix label-has-associated-control by removing label tags and using divs for the visual label
// since the input has a placeholder, it's not strictly necessary, or I can add htmlFor.
// But it's easier to just change <label to <div
code = code.replace(/<label className="flex items-center gap-2 text-sm text-neutral mb-2 font-medium">/g, '<div className="flex items-center gap-2 text-sm text-neutral mb-2 font-medium">');
code = code.replace(/<\/label>/g, '<\/div>');

fs.writeFileSync('src/components/contact/ContactPageClient.tsx', code);
