const navLinks = [
  {
    name: "Work",
    link: "#work",
  },
  {
    name: "Experience",
    link: "#experience",
  },
  {
    name: "Skills",
    link: "#skills",
  },
  {
    name: "About",
    link: "#about",
  },
];

const words = [
  { text: "Ideas", imgPath: "/images/ideas.svg" },
  { text: "Concepts", imgPath: "/images/concepts.svg" },
  { text: "Designs", imgPath: "/images/designs.svg" },
  { text: "Code", imgPath: "/images/code.svg" },
  { text: "Ideas", imgPath: "/images/ideas.svg" },
  { text: "Concepts", imgPath: "/images/concepts.svg" },
  { text: "Designs", imgPath: "/images/designs.svg" },
  { text: "Code", imgPath: "/images/code.svg" },
];

const counterItems = [
  { value: 2, suffix: "+", label: "Years of Experience" },
  { value: 10, suffix: "+", label: "Projects Completed" },
  { value: 5, suffix: "+", label: "Tech Stacks" },
  { value: 100, suffix: "%", label: "Commitment" },
];

const logoIconsList = []; // Empty, as there are no collaborator logos

const abilities = [
  {
    imgPath: "/images/seo.png",
    title: "Clean UI & Workflows",
    desc: "Designing applications around actual business requirements, converting workflows into structured digital products.",
  },
  {
    imgPath: "/images/chat.png",
    title: "AI-Powered Automation",
    desc: "Building intelligent application workflows with a focus on automation and tool integration.",
  },
  {
    imgPath: "/images/time.png",
    title: "Scalable Architecture",
    desc: "Developing scalable web applications with a focus on performance and maintainable code.",
  },
];

const techStackImgs = [
  { name: "React / Next.js", imgPath: "/images/logos/react.png" },
  { name: "Python", imgPath: "/images/logos/python.svg" },
  { name: "Node.js", imgPath: "/images/logos/node.png" },
  { name: "TypeScript", imgPath: "/images/logos/three.png" },
  { name: "AI Tools", imgPath: "/images/logos/git.svg" },
];

const techStackIcons = [
  {
    name: "React / Next.js",
    modelPath: "/models/react_logo-transformed.glb",
    scale: 1,
    rotation: [0, 0, 0],
  },
  {
    name: "Python",
    modelPath: "/models/python-transformed.glb",
    scale: 0.8,
    rotation: [0, 0, 0],
  },
  {
    name: "Node.js",
    modelPath: "/models/node-transformed.glb",
    scale: 5,
    rotation: [0, -Math.PI / 2, 0],
  },
  {
    name: "TypeScript",
    modelPath: "/models/three.js-transformed.glb",
    scale: 0.05,
    rotation: [0, 0, 0],
  },
  {
    name: "AI Tools",
    modelPath: "/models/git-svg-transformed.glb",
    scale: 0.05,
    rotation: [0, -Math.PI / 4, 0],
  },
];

const expCards = [
  {
    review: "Building responsive web applications and business systems with a focus on clean UI, practical workflows, scalability, and maintainable code.",
    imgPath: "/images/exp1.png",
    logoPath: null,
    title: "Full Stack Developer",
    date: "2025 - Present",
    company: "Independent Developer",
    responsibilities: [
      "Building responsive web applications and business systems with a focus on clean UI, practical workflows, scalability, and maintainable code.",
      "Developing real-world projects using modern frontend and backend technologies, database-driven architecture, authentication, APIs, and cloud-based services.",
      "Designing applications around actual business requirements, converting workflows into structured digital products rather than building only static interfaces."
    ],
  },
  {
    review: "Exploring AI-assisted software development and building intelligent application workflows with a focus on automation, tool integration, and practical AI-powered features.",
    imgPath: "/images/exp2.png",
    logoPath: null,
    title: "AI & Software Developer",
    date: "2026 - Present",
    company: "Independent Projects",
    responsibilities: [
      "Exploring AI-assisted software development and building intelligent application workflows with a focus on automation, tool integration, and practical AI-powered features.",
      "Developing a strong foundation in Python, APIs, data structures, backend logic, and modern AI development concepts to build reliable software systems.",
      "Experimenting with agentic application architecture, where AI can reason through tasks and interact with tools seamlessly."
    ],
  },
  {
    review: "Developing scalable web applications across frontend and backend systems, with a focus on performance, maintainable architecture, seamless user experiences, and clean code.",
    imgPath: "/images/exp3.png",
    htmlLogo: `<a href="https://www.raihsoft.com" target="_blank" rel="noopener noreferrer"><img src="https://media.raihsuite.com/RS0013/raihsoft-logo-light.PNG" alt="RaihSoft" style="height: 19px; margin-left: -5px; opacity: 0.8; object-fit: contain;" /></a>`,
    title: "Web & Application Developer",
    date: "2026",
    company: "RaihSoft",
    responsibilities: [
      "Developing scalable web applications across frontend and backend systems, with a focus on performance, maintainable architecture, seamless user experiences, and clean code."
    ],
  },
];

const expLogos = [];

const testimonials = [];

const socialImgs = [
  {
    name: "github",
    imgPath: "/images/github.png",
    url: "https://github.com/shibilikds",
  },
  {
    name: "insta",
    imgPath: "/images/insta.png",
    url: "https://www.instagram.com/shib_ili_y/",
  },
  {
    name: "fb",
    imgPath: "/images/fb.png",
    url: "https://www.facebook.com/profile.php?id=100082191128704",
  },
];

export {
  words,
  abilities,
  logoIconsList,
  counterItems,
  expCards,
  expLogos,
  testimonials,
  socialImgs,
  techStackIcons,
  techStackImgs,
  navLinks,
};
