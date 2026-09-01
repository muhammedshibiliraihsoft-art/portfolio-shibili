import re

with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(
    r'(<div\s+className="sticky top-\[12vh\] md:top-\[15vh\].*?zIndex:\s*10\s*\}\}>)',
    r'<div ref={project1Ref} className="sticky top-[12vh] md:top-[15vh] h-[85vh] md:h-[70vh] flex items-center justify-center w-full" style={{ zIndex: 10 }}>',
    content,
    flags=re.DOTALL
)
content = re.sub(
    r'(<div\s+className="sticky top-\[12vh\] md:top-\[15vh\].*?zIndex:\s*11\s*\}\}>)',
    r'<div ref={project2Ref} className="sticky top-[12vh] md:top-[15vh] h-[85vh] md:h-[70vh] flex items-center justify-center w-full" style={{ zIndex: 11 }}>',
    content,
    flags=re.DOTALL
)
content = re.sub(
    r'(<div\s+className="sticky top-\[12vh\] md:top-\[15vh\].*?zIndex:\s*12\s*\}\}>)',
    r'<div ref={project3Ref} className="sticky top-[12vh] md:top-[15vh] h-[85vh] md:h-[70vh] flex items-center justify-center w-full" style={{ zIndex: 12 }}>',
    content,
    flags=re.DOTALL
)

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
