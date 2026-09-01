/* eslint-disable */
"use client";
import React, { useState, useEffect } from 'react';
import ContactPageClient from '@/components/contact/ContactPageClient';
import dynamic from 'next/dynamic';
// @ts-ignore
import NavBar from '@/components/3d/NavBar';
// @ts-ignore
import Hero from '@/components/3d/Hero';

import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { useGSAP } from '@gsap/react';

// Register ScrollTrigger
if (typeof window !== 'undefined') {
  gsap.registerPlugin(ScrollTrigger);
}

// @ts-ignore
import Preloader from '@/components/Preloader';
export default function PortfolioTemplate() {
  
  useGSAP(() => {
    const fadeElements = gsap.utils.toArray('.fade-up');
    fadeElements.forEach((el: any) => {
      gsap.from(el, {
        y: 40,
        opacity: 0,
        duration: 0.8,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 85%', // when top of element hits 85% of viewport
          toggleActions: 'play none none none' // play only once
        }
      });
    });
  }, []);

  return (
    <div className="antialiased selection:bg-primary selection:text-white flex flex-col min-h-screen bg-black">
      <Preloader />
      <NavBar />

      

      <main className="flex-grow ">
        <Hero />

        {/* Experience Section */}
        <section className="max-w-[1100px] mx-auto px-4 md:px-6 py-10 md:py-16 w-full text-left" id="experience">
          <h2 className="fade-up text-3xl md:text-5xl font-extrabold text-white mb-8 md:mb-12 text-left">Work Experience</h2>
          <div className="flex flex-col gap-12 text-left w-full">
            {/* Experience 1 */}
            <div className="fade-up flex flex-col md:flex-row gap-4 md:gap-12 group">
              <div className="md:w-1/4 shrink-0">
                <p className="text-primary font-bold text-lg font-poppins tracking-wider uppercase mb-2">2025 &mdash; Present</p>
                <p className="text-neutral text-sm uppercase tracking-widest font-bold opacity-50">Independent</p>
              </div>
              <div className="md:w-3/4">
                <h3 className="text-2xl md:text-3xl font-bold text-white mb-1 group-hover:text-primary transition-colors duration-300">Full Stack Developer</h3>
                <h4 className="text-lg md:text-xl font-medium text-neutral mb-6">Independent Developer</h4>
                <ul className="space-y-4">
                  <li className="flex gap-4 items-start">
                    <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                    <p className="text-base md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Building responsive web applications and business systems with a focus on clean UI, practical workflows, scalability, and maintainable code.</p>
                  </li>
                  <li className="flex gap-4 items-start">
                    <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                    <p className="text-base md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Developing real-world projects using modern frontend and backend technologies, database-driven architecture, authentication, APIs, and cloud-based services.</p>
                  </li>
                  <li className="flex gap-4 items-start">
                    <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                    <p className="text-base md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Designing applications around actual business requirements, converting workflows into structured digital products rather than building only static interfaces.</p>
                  </li>
                </ul>
              </div>
            </div>

            {/* Experience 2 */}
            <div className="fade-up flex flex-col md:flex-row gap-4 md:gap-12 group">
              <div className="md:w-1/4 shrink-0">
                <p className="text-primary font-bold text-lg font-poppins tracking-wider uppercase mb-2">2026 &mdash; Present</p>
                <p className="text-neutral text-sm uppercase tracking-widest font-bold opacity-50">Independent</p>
              </div>
              <div className="md:w-3/4">
                <h3 className="text-2xl md:text-3xl font-bold text-white mb-1 group-hover:text-primary transition-colors duration-300">AI &amp; Software Developer</h3>
                <h4 className="text-lg md:text-xl font-medium text-neutral mb-6">Independent Projects</h4>
                <ul className="space-y-4">
                  <li className="flex gap-4 items-start">
                    <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                    <p className="text-base md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Exploring AI-assisted software development and building intelligent application workflows with a focus on automation, tool integration, and practical AI-powered features.</p>
                  </li>
                  <li className="flex gap-4 items-start">
                    <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                    <p className="text-base md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Developing a strong foundation in Python, APIs, data structures, backend logic, and modern AI development concepts to build reliable software systems.</p>
                  </li>
                  <li className="flex gap-4 items-start">
                    <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                    <p className="text-base md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Experimenting with agentic application architecture, where AI can reason through tasks and interact with tools seamlessly.</p>
                  </li>
                </ul>
              </div>
            </div>

            {/* Experience 3 */}
            <div className="fade-up flex flex-col md:flex-row gap-4 md:gap-12 group">
              <div className="md:w-1/4 shrink-0">
                <p className="text-primary font-bold text-lg font-poppins tracking-wider uppercase mb-2">2026</p>
                <a href="https://www.raihsoft.com" target="_blank" rel="noopener noreferrer" className="block mb-2">
                  <img 
                    src="https://media.raihsuite.com/RS0013/raihsoft-logo-light.PNG"
                    alt="RaihSoft"
                    style={{ height: '19px', marginLeft: '-5px', opacity: 0.8, objectFit: 'contain' }}
                  />
                </a>
              </div>
              <div className="md:w-3/4">
                <h3 className="text-2xl md:text-3xl font-bold text-white mb-1 group-hover:text-primary transition-colors duration-300">Web &amp; Application Developer</h3>
                <h4 className="text-lg md:text-xl font-medium text-neutral mb-6">Full-Stack Development &middot; Internship</h4>
                <ul className="space-y-4">
                  <li className="flex gap-4 items-start">
                    <span className="material-symbols-outlined text-primary text-[20px] mt-1 shrink-0">check_circle</span>
                    <p className="text-base md:text-xl text-neutral font-poppins font-medium opacity-80 leading-relaxed">Developing scalable web applications across frontend and backend systems, with a focus on performance, maintainable architecture, seamless user experiences, and clean code.</p>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        {/* Projects Section */}
        <section className="max-w-[1100px] mx-auto px-4 md:px-6 py-10 md:py-16 w-full text-left" id="projects">
          <h2 className="text-3xl md:text-5xl font-extrabold text-white mb-8 md:mb-24 text-left">Featured Projects</h2>
          <div className="relative w-full">
            
            {/* Project 1 */}
            <div className="sticky top-0 h-[100vh] w-full flex items-center justify-center" style={{ zIndex: 10 }}>
              <div className="w-full max-w-[900px] h-[75vh] md:h-[60vh] bg-[#0e141b] rounded-2xl border border-[#94a3b833] flex flex-col md:flex-row overflow-hidden shadow-2xl relative transform transition-transform duration-500 hover:scale-[1.02] mx-4">
                <div className="absolute inset-0 z-0 pointer-events-none opacity-20" style={{ backgroundImage: 'url("data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noiseFilter%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%221.5%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noiseFilter)%22/%3E%3C/svg%3E")' }}></div>
                <div className="flex-1 p-8 md:p-16 flex flex-col justify-center z-10 relative">
                  <h3 className="text-3xl md:text-5xl font-bold text-white mb-4 md:mb-6">AccoutSoft</h3>
                  <p className="text-base md:text-xl text-neutral opacity-80 mb-8 md:mb-10 font-poppins max-w-lg leading-relaxed">A comprehensive financial tracking application enabling businesses to monitor real-time accounting data, streamline billing, and visualize metrics through dynamic dashboards.</p>
                  <div className="flex gap-4 md:gap-6 mt-auto flex-wrap">
                    <a className="text-white hover:text-primary font-bold text-base md:text-lg flex items-center gap-2 transition-colors group" href="/">
                      Live Preview <span className="material-symbols-outlined text-[20px] group-hover:translate-x-[3px] transition-transform">arrow_forward</span>
                    </a>
                    <a className="text-neutral hover:text-white font-bold text-base md:text-lg flex items-center gap-2 transition-colors group" href="/">
                      Source Code <span className="material-symbols-outlined text-[20px] group-hover:translate-x-[3px] transition-transform">arrow_forward</span>
                    </a>
                  </div>
                </div>
                <div className="flex-1 relative h-64 md:h-auto overflow-hidden bg-[#0a0e14]">
                  <img alt="AccoutSoft" className="absolute top-0 left-0 w-full h-full object-cover object-right-top transition-transform duration-1000 hover:scale-105" src="/AccoutSoft-light.webp" />
                </div>
              </div>
            </div>

            {/* Project 2 */}
            <div className="sticky top-0 h-[100vh] w-full flex items-center justify-center" style={{ zIndex: 11 }}>
              <div className="w-full max-w-[900px] h-[75vh] md:h-[60vh] bg-[#060c18] rounded-2xl border border-[#94a3b833] flex flex-col md:flex-row overflow-hidden shadow-2xl relative transform transition-transform duration-500 hover:scale-[1.02] mx-4">
                <div className="absolute inset-0 z-0 pointer-events-none opacity-20" style={{ backgroundImage: 'url("data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noiseFilter%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%221.5%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noiseFilter)%22/%3E%3C/svg%3E")' }}></div>
                <div className="flex-1 p-8 md:p-16 flex flex-col justify-center z-10 relative">
                  <h3 className="text-3xl md:text-5xl font-bold text-white mb-4 md:mb-6">Contribution Portal</h3>
                  <p className="text-base md:text-xl text-neutral opacity-80 mb-8 md:mb-10 font-poppins max-w-lg leading-relaxed">A secure and transparent platform for managing charity donations and member contributions. Features robust reporting tools and automated receipt generation.</p>
                  <div className="flex gap-4 md:gap-6 mt-auto flex-wrap">
                    <a className="text-white hover:text-primary font-bold text-base md:text-lg flex items-center gap-2 transition-colors group" href="/">
                      Live Preview <span className="material-symbols-outlined text-[20px] group-hover:translate-x-[3px] transition-transform">arrow_forward</span>
                    </a>
                    <a className="text-neutral hover:text-white font-bold text-base md:text-lg flex items-center gap-2 transition-colors group" href="/">
                      Source Code <span className="material-symbols-outlined text-[20px] group-hover:translate-x-[3px] transition-transform">arrow_forward</span>
                    </a>
                  </div>
                </div>
                <div className="flex-1 relative h-64 md:h-auto overflow-hidden bg-[#040811]">
                  <img alt="Contribution Portal" className="absolute top-0 left-0 w-full h-full object-contain object-bottom drop-shadow-2xl transition-transform duration-1000 hover:scale-105" src="/charity.webp" />
                </div>
              </div>
            </div>

            {/* Project 3 */}
            <div className="sticky top-0 h-[100vh] w-full flex items-center justify-center" style={{ zIndex: 12 }}>
              <div className="w-full max-w-[900px] h-[75vh] md:h-[60vh] bg-[#131b26] rounded-2xl border border-[#94a3b833] flex flex-col md:flex-row overflow-hidden shadow-2xl relative transform transition-transform duration-500 hover:scale-[1.02] mx-4">
                <div className="absolute inset-0 z-0 pointer-events-none opacity-20" style={{ backgroundImage: 'url("data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noiseFilter%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%221.5%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noiseFilter)%22/%3E%3C/svg%3E")' }}></div>
                <div className="flex-1 p-8 md:p-16 flex flex-col justify-center z-10 relative">
                  <h3 className="text-3xl md:text-5xl font-bold text-white mb-4 md:mb-6">Festival Manager</h3>
                  <p className="text-base md:text-xl text-neutral opacity-80 mb-8 md:mb-10 font-poppins max-w-lg leading-relaxed">An end-to-end event management suite tailored for large-scale festivals, handling ticketing workflows, artist schedules, and real-time venue coordination seamlessly.</p>
                  <div className="flex gap-4 md:gap-6 mt-auto flex-wrap">
                    <a className="text-white hover:text-primary font-bold text-base md:text-lg flex items-center gap-2 transition-colors group" href="/">
                      Live Preview <span className="material-symbols-outlined text-[20px] group-hover:translate-x-[3px] transition-transform">arrow_forward</span>
                    </a>
                    <a className="text-neutral hover:text-white font-bold text-base md:text-lg flex items-center gap-2 transition-colors group" href="/">
                      Source Code <span className="material-symbols-outlined text-[20px] group-hover:translate-x-[3px] transition-transform">arrow_forward</span>
                    </a>
                  </div>
                </div>
                <div className="flex-1 relative h-64 md:h-auto overflow-hidden bg-[#0d1219]">
                  <img alt="Festival Manager" className="absolute top-0 w-full h-full object-contain object-right drop-shadow-[0_25px_35px_rgba(0,0,0,0.6)] transition-transform duration-1000 hover:scale-105" style={{ left: '0px', paddingRight: '20px' }} src="/festival.webp" />
                </div>
              </div>
            </div>

          </div>
        </section>

        {/* About Section */}
        <section className="max-w-[1100px] mx-auto px-4 md:px-6 py-10 md:py-16 w-full" id="about">
          <h2 className="fade-up text-3xl md:text-5xl font-extrabold text-white mb-8 md:mb-12 text-left">About Me</h2>
          <div className="flex flex-col md:flex-row gap-10 md:gap-24 items-start w-full">
            <div className="fade-up flex-1 text-left w-full">
              <p className="text-lg md:text-2xl text-neutral font-poppins font-medium leading-relaxed opacity-90 mb-8">
                I am an aspiring software engineer passionate about building modern, intelligent, and user-focused digital experiences. My journey in technology began with curiosity and has grown into a continuous pursuit of learning software development, AI, and agentic systems while strengthening my foundation in both frontend and backend engineering.
              </p>
              <p className="text-lg md:text-2xl text-neutral font-poppins font-medium leading-relaxed opacity-90 mb-8">
                When I'm not coding, I enjoy exploring emerging technologies, experimenting with AI-powered solutions, and turning ideas into practical projects. I believe in writing clean, maintainable code and continuously improving my skills by learning, building, and solving real-world problems.
              </p>
              <div className="flex flex-wrap gap-4 mt-12 justify-start">
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">React / Next.js</span>
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">TypeScript</span>
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Node.js</span>
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Python</span>
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Antigravity</span>
                <span className="px-6 py-3 bg-surface border border-outline-variant rounded-full text-white font-bold text-sm tracking-wider shadow-sm">Codex</span>
              </div>
            </div>
            <div className="fade-up w-[240px] h-[300px] md:w-[320px] md:h-[400px] shrink-0 bg-[#f8f9fa] p-4 md:p-5 pb-16 md:pb-20 shadow-2xl rotate-3 hover:rotate-0 transition-transform duration-500 mx-auto md:mx-0 self-center md:self-auto">
              <img alt="Profile picture" className="w-full h-full object-cover object-top" src="/profile.webp" />
            </div>
          </div>
        </section>

        {/* Contact Section */}
        <section className="w-full bg-[#070a0f] border-t border-outline-variant" id="contact">
          <div className="max-w-[1100px] mx-auto px-4 md:px-6 py-10 md:py-16 w-full flex flex-col md:flex-row gap-12 md:gap-24">
            <div className="fade-up flex-1">
              <h2 className="text-3xl md:text-5xl font-extrabold text-white mb-6">Let's talk</h2>
              <p className="text-lg md:text-xl text-neutral font-poppins opacity-80 mb-12 max-w-md leading-relaxed">
                Have a project in mind? Looking to partner or work together? Reach out through the form and I'll get back to you in the next 48 hours.
              </p>
              
              <div className="space-y-10">
                <div className="flex gap-6 group cursor-pointer">
                  <div className="w-14 h-14 rounded-full border border-outline-variant/50 bg-surface flex items-center justify-center shrink-0 group-hover:border-primary/50 group-hover:bg-primary/5 transition-all duration-300">
                    <span className="material-symbols-outlined text-neutral group-hover:text-primary transition-colors">mail</span>
                  </div>
                  <div>
                    <h4 className="text-primary text-xs font-bold tracking-widest uppercase mb-2">EMAIL ME</h4>
                    <p className="text-white text-xl font-medium mb-1">shibili.n@zohomail.in</p>
                    <p className="text-neutral text-sm opacity-80">I typically reply within 24 hours.</p>
                  </div>
                </div>
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
            </div>
            
            <div className="fade-up flex-1">
              <ContactPageClient />
            </div>
          </div>
        </section>

      </main>

      <footer className="bg-black text-primary font-label-mono w-full border-t border-outline-variant ">
        <div className="flex flex-col items-center gap-6 max-w-[1100px] mx-auto px-4 md:px-6 py-12 w-full text-xs md:text-sm">
          <div className="flex flex-wrap justify-center gap-8 mb-4">
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="https://github.com/shibilikds">Github <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="https://www.instagram.com/shib_ili_y/">Instagram <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-neutral hover:text-primary transition-colors flex items-center gap-1 group" href="https://www.facebook.com/profile.php?id=100082191128704">Facebook <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
            <a className="text-[#a78bfa] hover:text-primary transition-colors flex items-center gap-1 group" href="https://www.raihsoft.com">RaihSoft <span className="material-symbols-outlined text-[16px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span></a>
          </div>
          <p className="text-neutral text-center text-xs md:text-sm">
            Muhammed Shibili N &copy; 2026. Designed &amp; Developed by Muhammed Shibili N
          </p>
        </div>
      </footer>
    </div>
  );
}