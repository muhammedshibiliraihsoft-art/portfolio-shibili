/* eslint-disable */
"use client";
import TitleHeader from "./TitleHeader";

const About = () => {
  return (
    <section id="about" className="flex-center section-padding">
      <div className="w-full h-full md:px-10 px-5">
        <TitleHeader
          title="About Me"
          sub="🧑‍💻 Who I am and what I do"
        />
        <div className="flex flex-col md:flex-row items-center gap-16 mt-16 max-w-5xl mx-auto">
          {/* Polaroid Image */}
          <div className="flex-shrink-0 group">
            <div className="bg-white p-4 pb-12 shadow-2xl rounded-sm transition-transform duration-300 transform -rotate-3 group-hover:rotate-0 w-64 h-auto mx-auto md:mx-0">
              <img
                src="/images/profile.webp"
                alt="Profile"
                className="w-full h-auto object-cover border border-gray-200"
              />
            </div>
          </div>

          {/* Text Content */}
          <div className="flex flex-col gap-6 text-white-50 text-lg leading-relaxed">
            <p>
              I am an aspiring software engineer passionate about building modern, intelligent, 
              and user-focused digital experiences. My journey in technology began with curiosity 
              and has grown into a continuous pursuit of learning software development, AI, and 
              agentic systems while strengthening my foundation in both frontend and backend 
              engineering.
            </p>
            <p>
              When I'm not coding, I enjoy exploring emerging technologies, experimenting with 
              AI-powered solutions, and turning ideas into practical projects. I believe in writing 
              clean, maintainable code and continuously improving my skills by learning, building, 
              and solving real-world problems.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
