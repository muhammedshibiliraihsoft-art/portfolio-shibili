import re

with open('src/app/globals.css', 'r', encoding='utf-8') as f:
    content = f.read()

# First, strip everything from the first .projects-track down to the end of the file.
# We know the old injected CSS started with .projects-track or .projects-marquee.
# Let's find the first instance of .projects-track or .projects-marquee and cut there.

idx_track = content.find('.projects-track {')
idx_marquee = content.find('.projects-marquee {')

cut_idx = min(idx for idx in [idx_track, idx_marquee] if idx != -1)
if cut_idx != -1:
    content = content[:cut_idx].strip() + "\n\n"

new_css = '''
.projects-marquee {
  overflow: hidden;
  height: 600px;
  position: relative;
  -webkit-mask-image: linear-gradient(to bottom, transparent, black 12%, black 88%, transparent);
  mask-image: linear-gradient(to bottom, transparent, black 12%, black 88%, transparent);
}

.projects-track {
  display: flex;
  flex-direction: column;
  animation: scrollUp 25s linear infinite;
}

.project-card {
  margin-top: -80px; /* Overlap effect */
  position: relative;
}

.project-card:first-child {
  margin-top: 0;
}

/* Ensure later cards stack above earlier cards */
.project-card:nth-child(1) { z-index: 1; }
.project-card:nth-child(2) { z-index: 2; }
.project-card:nth-child(3) { z-index: 3; }
.project-card:nth-child(4) { z-index: 4; }
.project-card:nth-child(5) { z-index: 5; }
.project-card:nth-child(6) { z-index: 6; }

.projects-marquee:hover .projects-track {
  animation-play-state: paused;
}

@keyframes scrollUp {
  0% { transform: translateY(0); }
  100% { transform: translateY(-50%); }
}
'''

content += new_css

with open('src/app/globals.css', 'w', encoding='utf-8') as f:
    f.write(content)
