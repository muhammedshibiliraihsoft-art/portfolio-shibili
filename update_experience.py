import re

new_experience = '''<section className="max-w-[1100px] mx-auto px-6 py-section-gap w-full text-left" id="experience">
          <h2 className="text-4xl md:text-5xl font-extrabold text-white mb-12 text-left">Work Experience</h2>
          <div className="flex flex-col gap-12 text-left w-full">
            {/* Experience 1 */}
            <div>
              <h3 className="text-2xl md:text-3xl font-bold text-primary mb-1">Full Stack Developer</h3>
              <h4 className="text-lg md:text-xl font-bold text-white mb-1">Independent Developer</h4>
              <p className="text-neutral text-base mb-6">2025 &mdash; Present</p>
              <ul className="space-y-4">
                <li className="flex gap-4 items-start">
                  <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                  <p className="text-lg md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Building responsive web applications and business systems with a focus on clean UI, practical workflows, scalability, and maintainable code.</p>
                </li>
                <li className="flex gap-4 items-start">
                  <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                  <p className="text-lg md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Developing real-world projects using modern frontend and backend technologies, database-driven architecture, authentication, APIs, and cloud-based services.</p>
                </li>
                <li className="flex gap-4 items-start">
                  <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                  <p className="text-lg md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Designing applications around actual business requirements, converting workflows into structured digital products rather than building only static interfaces.</p>
                </li>
              </ul>
            </div>

            {/* Experience 2 */}
            <div>
              <h3 className="text-2xl md:text-3xl font-bold text-primary mb-1">AI &amp; Software Developer</h3>
              <h4 className="text-lg md:text-xl font-bold text-white mb-1">Independent Projects</h4>
              <p className="text-neutral text-base mb-6">2026 &mdash; Present</p>
              <ul className="space-y-4">
                <li className="flex gap-4 items-start">
                  <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                  <p className="text-lg md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Exploring AI-assisted software development and building intelligent application workflows with a focus on automation, tool integration, and practical AI-powered features.</p>
                </li>
                <li className="flex gap-4 items-start">
                  <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                  <p className="text-lg md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Developing a strong foundation in Python, APIs, data structures, backend logic, and modern AI development concepts to build reliable software systems.</p>
                </li>
                <li className="flex gap-4 items-start">
                  <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                  <p className="text-lg md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Experimenting with agentic application architecture, where AI can reason through tasks, use tools, interact with data, and automate multi-step workflows.</p>
                </li>
              </ul>
            </div>

            {/* Experience 3 */}
            <div>
              <h3 className="text-2xl md:text-3xl font-bold text-primary mb-1">Web &amp; Application Developer</h3>
              <h4 className="text-lg md:text-xl font-bold text-white mb-1">Self-Learning &amp; Project Development</h4>
              <p className="text-neutral text-base mb-6">2024 &mdash; Present</p>
              <ul className="space-y-4">
                <li className="flex gap-4 items-start">
                  <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                  <p className="text-lg md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Progressively developing skills across frontend development, backend integration, databases, responsive design, and application architecture through hands-on projects.</p>
                </li>
                <li className="flex gap-4 items-start">
                  <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                  <p className="text-lg md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Building reusable and responsive interfaces with attention to component structure, user experience, performance, and clean code principles.</p>
                </li>
                <li className="flex gap-4 items-start">
                  <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                  <p className="text-lg md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Turning independent ideas into working prototypes and production-oriented applications while continuously improving development and system-design skills.</p>
                </li>
              </ul>
            </div>
          </div>
        </section>'''

with open('src/app/page.tsx', 'r') as f:
    code = f.read()

# Replace the old experience section
start_pattern = r'<section className="max-w-\[1100px\] mx-auto px-6 py-section-gap w-full text-left" id="experience">'
# Find the next section (projects)
end_pattern = r'\{/\* Projects Section \*/\}'

match = re.search(f'({start_pattern}.*?){end_pattern}', code, flags=re.DOTALL)
if match:
    code = code.replace(match.group(1), new_experience + '\n\n        ')
    with open('src/app/page.tsx', 'w') as f:
        f.write(code)
    print("Updated Experience Section")
else:
    print("Could not find the experience section block")
