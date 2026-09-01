import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

// Replace the <a> tags inside the nav to use font-poppins and text-lg
code = code.replace(
  /<a className="text-neutral hover:text-primary transition-all duration-300" href="#experience">Experience<\/a>/,
  '<a className="text-neutral text-lg font-poppins font-medium hover:text-primary transition-all duration-300" href="#experience">Experience</a>'
);
code = code.replace(
  /<a className="text-neutral hover:text-primary transition-all duration-300" href="#projects">Projects<\/a>/,
  '<a className="text-neutral text-lg font-poppins font-medium hover:text-primary transition-all duration-300" href="#projects">Projects</a>'
);
code = code.replace(
  /<a className="text-primary font-bold relative after:content-\[''\] after:absolute after:-bottom-2 after:left-1\/2 after:-translate-x-1\/2 after:w-1.5 after:h-1.5 after:bg-primary after:rounded-full hover:text-primary transition-all duration-300" href="#about">About<\/a>/,
  '<a className="text-primary text-lg font-poppins font-bold relative after:content-[\'\'] after:absolute after:-bottom-2 after:left-1/2 after:-translate-x-1/2 after:w-1.5 after:h-1.5 after:bg-primary after:rounded-full hover:text-primary transition-all duration-300" href="#about">About</a>'
);

fs.writeFileSync('src/app/page.tsx', code);
