import fs from 'fs';
let code = fs.readFileSync('src/app/page.tsx', 'utf8');

// Update Get in Touch button href
code = code.replace(
  /<a className="(.*?) bg-\[#2563eb\] (.*?) href="\/"(.*?)>Get in Touch<\/a>/,
  '<a className="$1 bg-[#2563eb] $2 href="#contact"$3>Get in Touch</a>'
);

// Define Contact Section JSX
const contactSection = `
        {/* Contact Section Transition Divider */}
        <div className="w-full h-px bg-gradient-to-r from-transparent via-outline-variant to-transparent my-16 opacity-50"></div>

        {/* Contact Section */}
        <section className="max-w-[1100px] mx-auto px-6 py-section-gap w-full text-left" id="contact">
          <div className="flex flex-col lg:flex-row gap-16 lg:gap-24 items-start w-full">
            
            {/* Left Column - Form & Headers */}
            <div className="lg:w-3/5 w-full">
              <div className="flex items-center gap-4 mb-6">
                <span className="text-primary font-bold tracking-widest text-sm uppercase">GET IN TOUCH</span>
                <div className="h-px bg-primary w-12 opacity-50"></div>
              </div>
              <h2 className="text-5xl md:text-7xl font-extrabold text-white mb-6 leading-[1.1] tracking-tight">
                LET'S BUILD <br/>
                <span className="text-primary">SOMETHING</span> <br/>
                TOGETHER<span className="text-primary">.</span>
              </h2>
              <p className="text-neutral text-lg md:text-xl font-poppins opacity-80 max-w-lg mb-12">
                Have a project in mind? Let's talk about it.<br/>
                I'm always open to discussing new ideas, projects or opportunities.
              </p>

              <form className="space-y-6">
                <div className="flex flex-col md:flex-row gap-6">
                  {/* Name Input */}
                  <div className="flex-1 relative group">
                    <div className="absolute inset-0 bg-primary/20 rounded-xl blur-md opacity-0 group-focus-within:opacity-100 transition-opacity duration-500"></div>
                    <div className="relative bg-[#0c1218] border border-outline-variant rounded-xl p-4 transition-colors focus-within:border-primary/50">
                      <label className="flex items-center gap-2 text-sm text-neutral mb-2 font-medium">
                        <span className="material-symbols-outlined text-[18px]">person</span> Your Name
                      </label>
                      <input type="text" placeholder="Enter your name" className="w-full bg-transparent border-none text-white focus:outline-none placeholder-neutral/50 font-poppins" />
                    </div>
                  </div>
                  {/* Email Input */}
                  <div className="flex-1 relative group">
                    <div className="absolute inset-0 bg-primary/20 rounded-xl blur-md opacity-0 group-focus-within:opacity-100 transition-opacity duration-500"></div>
                    <div className="relative bg-[#0c1218] border border-outline-variant rounded-xl p-4 transition-colors focus-within:border-primary/50">
                      <label className="flex items-center gap-2 text-sm text-neutral mb-2 font-medium">
                        <span className="material-symbols-outlined text-[18px]">mail</span> Your Email
                      </label>
                      <input type="email" placeholder="Enter your email" className="w-full bg-transparent border-none text-white focus:outline-none placeholder-neutral/50 font-poppins" />
                    </div>
                  </div>
                </div>

                {/* Message Input */}
                <div className="relative group">
                  <div className="absolute inset-0 bg-primary/20 rounded-xl blur-md opacity-0 group-focus-within:opacity-100 transition-opacity duration-500"></div>
                  <div className="relative bg-[#0c1218] border border-outline-variant rounded-xl p-4 transition-colors focus-within:border-primary/50">
                    <label className="flex items-center gap-2 text-sm text-neutral mb-2 font-medium">
                      <span className="material-symbols-outlined text-[18px]">chat_bubble</span> Your Message
                    </label>
                    <textarea rows={4} placeholder="Tell me about your project..." className="w-full bg-transparent border-none text-white focus:outline-none placeholder-neutral/50 font-poppins resize-none"></textarea>
                  </div>
                </div>

                {/* Submit Row */}
                <div className="flex flex-col sm:flex-row items-start sm:items-center gap-6 pt-4">
                  <button type="button" className="relative group overflow-hidden bg-surface-container-high border border-outline-variant hover:border-primary text-white px-8 py-4 rounded-xl font-bold flex items-center gap-4 transition-all duration-300">
                    <div className="absolute inset-0 bg-primary/10 translate-y-full group-hover:translate-y-0 transition-transform duration-300"></div>
                    <span className="relative z-10 tracking-widest text-sm">SEND MESSAGE</span>
                    <span className="material-symbols-outlined relative z-10 text-[18px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span>
                  </button>
                  <div className="flex items-center gap-3 text-neutral text-sm opacity-80">
                    <span className="material-symbols-outlined text-[20px]">lock</span>
                    <p>Your information is safe<br/>and will never be shared.</p>
                  </div>
                </div>
              </form>
            </div>

            {/* Right Column - Info Blocks */}
            <div className="lg:w-2/5 w-full flex flex-col gap-12 lg:pt-4 lg:pl-12 border-t lg:border-t-0 lg:border-l border-outline-variant/30 pt-12 relative">
              
              {/* Decorative dotted pattern */}
              <div className="absolute top-0 right-0 w-32 h-32 opacity-10 pointer-events-none hidden md:block" style={{ backgroundImage: 'radial-gradient(#0453d8 2px, transparent 2px)', backgroundSize: '16px 16px' }}></div>

              {/* Status Badge */}
              <div className="inline-flex items-center gap-3 px-6 py-3 rounded-full border border-outline-variant/50 bg-[#0c1218] w-max">
                <span className="w-2.5 h-2.5 rounded-full bg-green-500 animate-pulse shadow-[0_0_8px_rgba(34,197,94,0.6)]"></span>
                <span className="text-white text-xs font-bold tracking-widest uppercase">AVAILABLE FOR WORK</span>
              </div>

              {/* Info Items */}
              <div className="space-y-10">
                {/* Email */}
                <div className="flex gap-6 group cursor-pointer">
                  <div className="w-14 h-14 rounded-full border border-outline-variant/50 bg-surface flex items-center justify-center shrink-0 group-hover:border-primary/50 group-hover:bg-primary/5 transition-all duration-300">
                    <span className="material-symbols-outlined text-neutral group-hover:text-primary transition-colors">mail</span>
                  </div>
                  <div>
                    <h4 className="text-primary text-xs font-bold tracking-widest uppercase mb-2">EMAIL ME</h4>
                    <p className="text-white text-xl font-medium mb-1">hello@shibili.dev</p>
                    <p className="text-neutral text-sm opacity-80">I typically reply within 24 hours.</p>
                  </div>
                </div>

                {/* Response Time */}
                <div className="flex gap-6">
                  <div className="w-14 h-14 rounded-full border border-outline-variant/50 bg-surface flex items-center justify-center shrink-0">
                    <span className="material-symbols-outlined text-neutral">schedule</span>
                  </div>
                  <div>
                    <h4 className="text-primary text-xs font-bold tracking-widest uppercase mb-2">RESPONSE TIME</h4>
                    <p className="text-white text-xl font-medium mb-1">Within 24 hours</p>
                    <p className="text-neutral text-sm opacity-80">I usually respond quickly.</p>
                  </div>
                </div>

                {/* Let's Connect */}
                <div className="flex gap-6 group cursor-pointer">
                  <div className="w-14 h-14 rounded-full border border-outline-variant/50 bg-surface flex items-center justify-center shrink-0 group-hover:border-primary/50 group-hover:bg-primary/5 transition-all duration-300">
                    <span className="material-symbols-outlined text-neutral group-hover:text-primary transition-colors">send</span>
                  </div>
                  <div>
                    <h4 className="text-primary text-xs font-bold tracking-widest uppercase mb-2">LET'S CONNECT</h4>
                    <p className="text-white text-xl font-medium mb-1 leading-snug">Let's turn your ideas<br/>into real products.</p>
                  </div>
                </div>
              </div>

              {/* Social Links */}
              <div className="pt-6">
                <h4 className="text-neutral text-xs font-bold tracking-widest uppercase mb-6">FIND ME ELSEWHERE</h4>
                <div className="flex items-center gap-6">
                  <a href="/" className="text-neutral hover:text-white transition-colors hover:scale-110 transform duration-300">
                    <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fillRule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clipRule="evenodd" /></svg>
                  </a>
                  <a href="/" className="text-neutral hover:text-[#0a66c2] transition-colors hover:scale-110 transform duration-300">
                    <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fillRule="evenodd" d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" clipRule="evenodd" /></svg>
                  </a>
                  <a href="/" className="text-neutral hover:text-[#1da1f2] transition-colors hover:scale-110 transform duration-300">
                    <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" /></svg>
                  </a>
                  <a href="/" className="text-neutral hover:text-[#ea4c89] transition-colors hover:scale-110 transform duration-300">
                    <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fillRule="evenodd" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10c5.51 0 10-4.48 10-10S17.51 2 12 2zm6.605 4.61a8.502 8.502 0 011.93 5.314c-.281-.054-3.101-.629-5.943-.271-.065-.156-.12-.322-.19-.481 2.684-1.22 3.864-2.85 3.93-2.946-.66-.885-1.464-1.637-2.37-2.203l-.01.015c-.067.094-1.22 1.705-3.92 2.836a18.31 18.31 0 00-2.316-3.82c3.08-.942 4.708-2.613 4.774-2.685a8.528 8.528 0 014.115 4.24zm-12.72 1.258c.074.075 1.758 1.802 4.962 2.716-1.168 2.92-2.39 5.251-2.478 5.419-2.73-1.017-4.646-3.265-5.114-6.079a8.498 8.498 0 012.63-2.056zm-1.026 8.874c.092-.158 1.4-2.483 2.614-5.467 2.855.845 5.259.626 5.56.595.05.109.1.218.146.33 1.107 2.805 1.298 5.556 1.332 6.136a8.523 8.523 0 01-9.652-1.594zm10.74 1.703c-.032-.505-.205-3.036-1.213-5.69 2.531-.296 5.122.185 5.38.238a8.502 8.502 0 01-4.167 5.452z" clipRule="evenodd" /></svg>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </section>
`;

code = code.replace(
  /<\/main>/,
  contactSection + '\n      </main>'
);

fs.writeFileSync('src/app/page.tsx', code);
