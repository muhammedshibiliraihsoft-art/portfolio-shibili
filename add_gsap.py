import re

with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Add imports
imports = """
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { useGSAP } from '@gsap/react';
"""
content = content.replace("import React, { useState, useEffect } from 'react';", "import React, { useState, useEffect, useRef } from 'react';" + imports)

# Register GSAP
content = content.replace("export default function PortfolioTemplate() {", "gsap.registerPlugin(ScrollTrigger);\n\nexport default function PortfolioTemplate() {")

# Add refs and useGSAP inside component
hooks = """
  const project1Ref = useRef(null);
  const project2Ref = useRef(null);
  const project3Ref = useRef(null);

  useGSAP(() => {
    const cards = [project1Ref.current, project2Ref.current, project3Ref.current];
    cards.forEach((card, index) => {
      if (!card) return;
      gsap.fromTo(
        card,
        {
          y: 100,
          opacity: 0,
        },
        {
          y: 0,
          opacity: 1,
          duration: 1.2,
          ease: "power3.out",
          scrollTrigger: {
            trigger: card,
            start: "top bottom-=100",
          },
        }
      );
    });
  }, []);
"""
content = content.replace("const [isScrolled, setIsScrolled] = useState(false);", hooks + "\n  const [isScrolled, setIsScrolled] = useState(false);")

# Attach refs to the sticky wrappers
content = content.replace(
    '<div className="sticky top-[12vh] md:top-[15vh] h-[85vh] md:h-[70vh] flex items-center justify-center \nw-full" style={{ zIndex: 10 }}>',
    '<div ref={project1Ref} className="sticky top-[12vh] md:top-[15vh] h-[85vh] md:h-[70vh] flex items-center justify-center \nw-full" style={{ zIndex: 10 }}>'
)
content = content.replace(
    '<div className="sticky top-[12vh] md:top-[15vh] h-[85vh] md:h-[70vh] flex items-center justify-center \nw-full" style={{ zIndex: 11 }}>',
    '<div ref={project2Ref} className="sticky top-[12vh] md:top-[15vh] h-[85vh] md:h-[70vh] flex items-center justify-center \nw-full" style={{ zIndex: 11 }}>'
)
content = content.replace(
    '<div className="sticky top-[12vh] md:top-[15vh] h-[85vh] md:h-[70vh] flex items-center justify-center \nw-full" style={{ zIndex: 12 }}>',
    '<div ref={project3Ref} className="sticky top-[12vh] md:top-[15vh] h-[85vh] md:h-[70vh] flex items-center justify-center \nw-full" style={{ zIndex: 12 }}>'
)

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
