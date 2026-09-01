with open('src/app/globals.css', 'a', encoding='utf-8') as f:
    f.write("""

/* 3D PORTFOLIO STYLES MIGRATED */
body, html {
  background-color: black;
  color: white;
  scroll-behavior: smooth;
  font-family: var(--font-poppins), sans-serif;
}

/* NAVBAR */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  padding-left: 1.25rem;
  padding-right: 1.25rem;
  padding-top: 1rem;
  padding-bottom: 1rem;
  z-index: 50;
  transition: all 0.3s;
}
@media (min-width: 768px) {
  .navbar {
    padding-left: 2.5rem;
    padding-right: 2.5rem;
  }
}
.navbar.scrolled {
  background-color: rgba(14, 14, 16, 0.9); /* black-100 */
  backdrop-filter: blur(10px);
}
.navbar.not-scrolled {
  background-color: transparent;
}
.navbar .inner {
  margin-left: auto;
  margin-right: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.navbar .logo {
  color: #d9ecff; /* white-50 */
  font-size: 1.25rem;
  font-weight: 600;
  transition: transform 0.3s;
}
.navbar .logo:hover {
  transform: scale(1.05);
}
.navbar nav.desktop {
  display: none;
}
@media (min-width: 1024px) {
  .navbar nav.desktop {
    display: flex;
    align-items: center;
  }
}
.navbar nav.desktop ul {
  display: flex;
  column-gap: 2rem;
}
.navbar nav.desktop ul li {
  color: #d9ecff;
  position: relative;
}
.navbar nav.desktop ul li span {
  transition: color 0.3s;
}
.navbar nav.desktop ul li:hover span {
  color: white;
}
.navbar nav.desktop ul li .underline {
  position: absolute;
  bottom: -0.25rem;
  left: 0;
  width: 0;
  height: 0.125rem;
  background-color: white;
  transition: width 0.3s;
}
.navbar nav.desktop ul li:hover .underline {
  width: 100%;
}
.navbar .contact-btn {
  display: flex;
}
.navbar .contact-btn .inner {
  padding-left: 1.25rem;
  padding-right: 1.25rem;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  border-radius: 0.5rem;
  background-color: white;
  color: black;
  transition: background-color 0.3s;
}
.navbar .contact-btn:hover .inner {
  background-color: #1c1c21; /* black-50 */
  color: white;
}
.navbar .contact-btn .inner span {
  transition: color 0.3s;
}

/* HERO */
.hero-layout {
  position: relative;
  z-index: 10;
  margin-top: 8rem;
  height: 80vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}
@media (min-width: 1280px) {
  .hero-layout {
    margin-top: 5rem;
    height: 100vh;
    align-items: center;
  }
}
.hero-text {
  display: flex;
  flex-direction: column;
  justify-content: center;
  font-size: 30px;
  font-weight: 600;
  position: relative;
  z-index: 10;
  pointer-events: none;
  color: #d9ecff;
}
@media (min-width: 768px) {
  .hero-text {
    font-size: 60px;
  }
}
.hero-text h1 {
  display: flex;
  gap: 0.5rem;
}
@media (min-width: 768px) {
  .hero-text h1 {
    gap: 0.75rem;
  }
}
.hero-text img {
  width: 2rem;
  height: 2rem;
  object-fit: contain;
}
@media (min-width: 768px) {
  .hero-text img {
    width: 2.5rem;
    height: 2.5rem;
  }
}
.hero-text .slide {
  position: absolute;
  padding-top: 0;
  padding-left: 0.5rem;
  padding-right: 0.5rem;
  padding-bottom: 30px;
  height: 48px;
  transform: translateY(0);
  overflow: hidden;
  display: inline-flex;
  flex-direction: column;
  transition: all cubic-bezier(0.71, 0.03, 0.34, 1);
}
@media (min-width: 768px) {
  .hero-text .slide {
    padding-left: 1.25rem;
    padding-right: 1.25rem;
    height: 78px;
    transform: translateY(0.25rem);
  }
}
.hero-badge {
  background-color: #282732;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  padding-left: 1rem;
  padding-right: 1rem;
  border-radius: 9999px;
  width: fit-content;
  font-size: 0.875rem;
  white-space: nowrap;
}
@media (min-width: 768px) {
  .hero-badge {
    font-size: 1rem;
  }
}
.hero-3d-layout {
  width: 100%;
  height: 100%;
  min-height: 50vh;
  position: absolute;
  top: 6rem;
  right: 0;
}
@media (min-width: 1280px) {
  .hero-3d-layout {
    width: 70%;
    top: -5rem;
    right: -5rem;
  }
}

/* BUTTON */
.cta-button {
  padding-left: 1rem;
  padding-right: 1rem;
  padding-top: 1rem;
  padding-bottom: 1rem;
  border-radius: 0.5rem;
  background-color: #282732;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  cursor: pointer;
  overflow: hidden;
}
.cta-button .bg-circle {
  position: absolute;
  right: -2.5rem;
  transform-origin: center;
  top: 50%;
  transform: translateY(-50%);
  width: 120%;
  height: 120%;
  border-radius: 9999px;
  background-color: #d9ecff;
  transition: all 0.5s;
}
.cta-button:hover .bg-circle {
  width: 2.5rem;
  height: 2.5rem;
  right: 2.5rem;
}
.cta-button .text {
  text-transform: uppercase;
  color: black;
  transition: all 0.5s;
  transform: translateX(-1.25rem);
}
@media (min-width: 768px) {
  .cta-button .text {
    font-size: 1.125rem;
  }
}
@media (min-width: 1280px) {
  .cta-button .text {
    transform: translateX(0);
  }
}
.cta-button:hover .text {
  color: #d9ecff;
  transform: translateX(-1.25rem);
}
.cta-button .arrow-wrapper {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 9999px;
  position: absolute;
  right: 2.5rem;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}
.cta-button:hover .arrow-wrapper {
  background-color: #d9ecff;
}
.cta-button .arrow-wrapper img {
  width: 1.25rem;
  height: 1.25rem;
  transform: translateY(0);
  animation: bounce 1s infinite;
  transition: all 0.5s;
}
@media (min-width: 1280px) {
  .cta-button .arrow-wrapper img {
    transform: translateY(-8rem);
  }
}
.cta-button:hover .arrow-wrapper img {
  transform: translateY(0);
}

/* ANIMATIONS */
.wrapper {
  display: flex;
  flex-direction: column;
  animation: wordSlider 21s infinite cubic-bezier(0.9, 0.01, 0.3, 0.99);
}

@keyframes wordSlider {
  0% { transform: translateY(0.5%); }
  12.5% { transform: translateY(-12.5%); }
  25% { transform: translateY(-25%); }
  37.5% { transform: translateY(-37.5%); }
  50% { transform: translateY(-50%); }
  62.5% { transform: translateY(-62.5%); }
  75% { transform: translateY(-75%); }
  87.5% { transform: translateY(-87.5%); }
}

""")
