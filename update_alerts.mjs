import fs from 'fs';
let code = fs.readFileSync('src/components/contact/ContactPageClient.tsx', 'utf8');

const oldSuccess = /{status === 'success' && \(\s*<div className="bg-green-500\/10 border border-green-500 text-green-500 p-4 rounded-md mb-6 font-medium">\s*Thank you! Your message has been sent successfully\. I will get back to you soon\.\s*<\/div>\s*\)}/;

const newSuccess = `{status === 'success' && (
        <div className="relative bg-[#0c1218] border border-primary/30 p-6 rounded-md mb-6 flex items-start gap-4 shadow-[0_0_20px_rgba(4,83,216,0.15)]">
          <span className="material-symbols-outlined text-primary text-[24px]">check_circle</span>
          <div>
            <h3 className="text-white font-bold mb-1">Message Sent</h3>
            <p className="text-neutral text-sm opacity-80">Thank you! Your message has been sent successfully. I will get back to you soon.</p>
          </div>
        </div>
      )}`;

const oldError = /{status === 'error' && \(\s*<div className="bg-red-500\/10 border border-red-500 text-red-500 p-4 rounded-md mb-6 font-medium">\s*\{errorMessage\}\s*<\/div>\s*\)}/;

const newError = `{status === 'error' && (
        <div className="relative bg-[#0c1218] border border-red-500/30 p-6 rounded-md mb-6 flex items-start gap-4">
          <span className="material-symbols-outlined text-red-400 text-[24px]">error</span>
          <div>
            <h3 className="text-white font-bold mb-1">Something went wrong</h3>
            <p className="text-neutral text-sm opacity-80">{errorMessage}</p>
          </div>
        </div>
      )}`;

code = code.replace(oldSuccess, newSuccess);
code = code.replace(oldError, newError);

fs.writeFileSync('src/components/contact/ContactPageClient.tsx', code);
