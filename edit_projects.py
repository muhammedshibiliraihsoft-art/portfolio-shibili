import re

with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the stack container
content = content.replace(
    '<div className="flex flex-col gap-8 md:gap-0 w-full relative">',
    '<div className="relative w-full">'
)

# Replace Project 1 wrapper
p1_wrapper_old = '<div className="relative md:sticky md:top-[15vh] h-auto md:h-[60vh] max-w-4xl mx-auto flex items-center justify-center w-full" style={{ zIndex: 10 }}>'
p1_wrapper_new = '<div className="sticky top-0 h-[100vh] w-full flex items-center justify-center" style={{ zIndex: 10 }}>'
content = content.replace(p1_wrapper_old, p1_wrapper_new)

# Replace Project 2 wrapper
p2_wrapper_old = '<div className="relative md:sticky md:top-[15vh] h-auto md:h-[60vh] max-w-4xl mx-auto flex items-center justify-center w-full" style={{ zIndex: 11 }}>'
p2_wrapper_new = '<div className="sticky top-0 h-[100vh] w-full flex items-center justify-center" style={{ zIndex: 11 }}>'
content = content.replace(p2_wrapper_old, p2_wrapper_new)

# Replace Project 3 wrapper
p3_wrapper_old = '<div className="relative md:sticky md:top-[15vh] h-auto md:h-[60vh] max-w-4xl mx-auto flex items-center justify-center w-full" style={{ zIndex: 12 }}>'
p3_wrapper_new = '<div className="sticky top-0 h-[100vh] w-full flex items-center justify-center" style={{ zIndex: 12 }}>'
content = content.replace(p3_wrapper_old, p3_wrapper_new)

# Now fix the inner cards to not rely on wrapper h-full
# For Project 1
p1_inner_old = '<div className="w-full h-full md:h-[55vh] bg-[#0e141b] rounded-2xl border border-[#94a3b833] flex flex-col md:flex-row overflow-hidden shadow-2xl relative transform transition-transform duration-500 hover:scale-[1.02]">'
p1_inner_new = '<div className="w-full max-w-[900px] h-[75vh] md:h-[60vh] bg-[#0e141b] rounded-2xl border border-[#94a3b833] flex flex-col md:flex-row overflow-hidden shadow-2xl relative transform transition-transform duration-500 hover:scale-[1.02] mx-4">'
content = content.replace(p1_inner_old, p1_inner_new)

# For Project 2
p2_inner_old = '<div className="w-full h-full md:h-[55vh] bg-[#060c18] rounded-2xl border border-[#94a3b833] flex flex-col md:flex-row overflow-hidden shadow-2xl relative transform transition-transform duration-500 hover:scale-[1.02]">'
p2_inner_new = '<div className="w-full max-w-[900px] h-[75vh] md:h-[60vh] bg-[#060c18] rounded-2xl border border-[#94a3b833] flex flex-col md:flex-row overflow-hidden shadow-2xl relative transform transition-transform duration-500 hover:scale-[1.02] mx-4">'
content = content.replace(p2_inner_old, p2_inner_new)

# For Project 3
p3_inner_old = '<div className="w-full h-full md:h-[55vh] bg-[#131b26] rounded-2xl border border-[#94a3b833] flex flex-col md:flex-row overflow-hidden shadow-2xl relative transform transition-transform duration-500 hover:scale-[1.02]">'
p3_inner_new = '<div className="w-full max-w-[900px] h-[75vh] md:h-[60vh] bg-[#131b26] rounded-2xl border border-[#94a3b833] flex flex-col md:flex-row overflow-hidden shadow-2xl relative transform transition-transform duration-500 hover:scale-[1.02] mx-4">'
content = content.replace(p3_inner_old, p3_inner_new)

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated stacking logic in page.tsx")
