"use client";

import { useEffect, useRef, useCallback } from "react";

export default function AIGlobe() {
  const containerRef = useRef<HTMLDivElement>(null);
  const animFrameRef = useRef<number>(0);
  const mouseRef = useRef({ x: 0, y: 0 });
  const currentOffsetRef = useRef({ x: 0, y: 0 });

  const handleMouseMove = useCallback((e: MouseEvent) => {
    const cx = window.innerWidth / 2;
    const cy = window.innerHeight / 2;
    mouseRef.current = {
      x: ((e.clientX - cx) / cx) * 8,
      y: ((e.clientY - cy) / cy) * 8,
    };
  }, []);

  useEffect(() => {
    window.addEventListener("mousemove", handleMouseMove, { passive: true });

    let raf = 0;
    const lerp = (a: number, b: number, t: number) => a + (b - a) * t;

    function tick() {
      const el = containerRef.current;
      if (el) {
        currentOffsetRef.current.x = lerp(currentOffsetRef.current.x, mouseRef.current.x, 0.06);
        currentOffsetRef.current.y = lerp(currentOffsetRef.current.y, mouseRef.current.y, 0.06);
        el.style.transform = `translate(${currentOffsetRef.current.x}px, ${currentOffsetRef.current.y}px)`;
      }
      raf = requestAnimationFrame(tick);
      animFrameRef.current = raf;
    }
    raf = requestAnimationFrame(tick);

    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
      cancelAnimationFrame(animFrameRef.current);
    };
  }, [handleMouseMove]);

  return (
    <div
      ref={containerRef}
      className="pointer-events-none will-change-transform"
      style={{ width: "100%", height: "100%", position: "relative" }}
      aria-hidden="true"
    >
      <svg
        viewBox="0 0 520 520"
        xmlns="http://www.w3.org/2000/svg"
        style={{ width: "100%", height: "100%", overflow: "visible" }}
      >
        <defs>
          {/* Globe radial gradient */}
          <radialGradient id="globeGrad" cx="42%" cy="38%" r="60%">
            <stop offset="0%" stopColor="#0d1c33" stopOpacity="0.95" />
            <stop offset="60%" stopColor="#060d1a" stopOpacity="0.98" />
            <stop offset="100%" stopColor="#020810" stopOpacity="1" />
          </radialGradient>

          {/* Outer glow */}
          <radialGradient id="glowGrad" cx="50%" cy="50%" r="50%">
            <stop offset="55%" stopColor="#1e40af" stopOpacity="0" />
            <stop offset="80%" stopColor="#1d4ed8" stopOpacity="0.12" />
            <stop offset="100%" stopColor="#3b82f6" stopOpacity="0.22" />
          </radialGradient>

          {/* Edge rim gradient */}
          <radialGradient id="rimGrad" cx="50%" cy="50%" r="50%">
            <stop offset="82%" stopColor="#1d4ed8" stopOpacity="0" />
            <stop offset="96%" stopColor="#3b82f6" stopOpacity="0.55" />
            <stop offset="100%" stopColor="#60a5fa" stopOpacity="0.15" />
          </radialGradient>

          {/* Core pulse glow */}
          <radialGradient id="coreGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="#93c5fd" stopOpacity="0.9" />
            <stop offset="40%" stopColor="#3b82f6" stopOpacity="0.6" />
            <stop offset="100%" stopColor="#1d4ed8" stopOpacity="0" />
          </radialGradient>

          {/* Filters */}
          <filter id="softGlow" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur in="SourceGraphic" stdDeviation="8" result="blur" />
            <feMerge>
              <feMergeNode in="blur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>

          <filter id="coreGlow" x="-60%" y="-60%" width="220%" height="220%">
            <feGaussianBlur in="SourceGraphic" stdDeviation="5" result="blur" />
            <feMerge>
              <feMergeNode in="blur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>

          <filter id="particleGlow" x="-200%" y="-200%" width="500%" height="500%">
            <feGaussianBlur in="SourceGraphic" stdDeviation="2.5" result="blur" />
            <feMerge>
              <feMergeNode in="blur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>

          {/* Clip globe */}
          <clipPath id="globeClip">
            <circle cx="260" cy="260" r="178" />
          </clipPath>
        </defs>

        {/* ── Ambient outer glow ── */}
        <circle cx="260" cy="260" r="230" fill="url(#glowGrad)" />

        {/* ── Pulsing outer ring (breathing) ── */}
        <circle cx="260" cy="260" r="188" fill="none" stroke="#3b82f6" strokeWidth="0.5" strokeOpacity="0.25">
          <animate attributeName="r" values="188;198;188" dur="4s" repeatCount="indefinite" />
          <animate attributeName="stroke-opacity" values="0.25;0.08;0.25" dur="4s" repeatCount="indefinite" />
        </circle>
        <circle cx="260" cy="260" r="198" fill="none" stroke="#60a5fa" strokeWidth="0.3" strokeOpacity="0.12">
          <animate attributeName="r" values="198;210;198" dur="4s" repeatCount="indefinite" />
          <animate attributeName="stroke-opacity" values="0.12;0.04;0.12" dur="4s" repeatCount="indefinite" />
        </circle>

        {/* ── Globe body ── */}
        <circle cx="260" cy="260" r="178" fill="url(#globeGrad)" />

        {/* ── Latitude lines (clipped) ── */}
        <g clipPath="url(#globeClip)" stroke="#1e40af" strokeWidth="0.6" strokeOpacity="0.35" fill="none">
          {[-120, -80, -40, 0, 40, 80, 120].map((offset, i) => (
            <ellipse key={i} cx="260" cy={260 + offset} rx="178" ry={Math.abs(offset) < 10 ? 12 : Math.sqrt(178 * 178 - offset * offset) * 0.28} />
          ))}
        </g>

        {/* ── Longitude lines (clipped) ── */}
        <g clipPath="url(#globeClip)" stroke="#1e40af" strokeWidth="0.6" strokeOpacity="0.3" fill="none">
          <ellipse cx="260" cy="260" rx="50" ry="178" />
          <ellipse cx="260" cy="260" rx="110" ry="178" />
          <ellipse cx="260" cy="260" rx="160" ry="178" />
        </g>

        {/* ── Surface data nodes ── */}
        <g clipPath="url(#globeClip)" filter="url(#particleGlow)">
          {[
            [210, 200], [300, 220], [180, 280], [330, 300],
            [240, 330], [290, 170], [220, 240], [310, 260]
          ].map(([x, y], i) => (
            <circle key={i} cx={x} cy={y} r="2.5" fill="#60a5fa" fillOpacity="0.55">
              <animate
                attributeName="fill-opacity"
                values="0.55;0.2;0.55"
                dur={`${2.5 + i * 0.4}s`}
                repeatCount="indefinite"
                begin={`${i * 0.3}s`}
              />
            </circle>
          ))}
        </g>

        {/* ── Rim glow ── */}
        <circle cx="260" cy="260" r="178" fill="url(#rimGrad)" />

        {/* ── Specular highlight ── */}
        <ellipse cx="218" cy="208" rx="48" ry="32" fill="white" fillOpacity="0.03" transform="rotate(-20, 218, 208)" />

        {/* ── Orbital ring 1 (wide, slow, tilted) ── */}
        <g transform="rotate(-20, 260, 260)">
          <ellipse cx="260" cy="260" rx="218" ry="62" fill="none" stroke="#3b82f6" strokeWidth="0.8" strokeOpacity="0.3" strokeDasharray="4 8">
            <animateTransform attributeName="transform" type="rotate" from="0 260 260" to="360 260 260" dur="18s" repeatCount="indefinite" />
          </ellipse>
          {/* Particle on ring 1 */}
          <circle r="4" fill="#60a5fa" filter="url(#particleGlow)" fillOpacity="0.9">
            <animateMotion
              dur="18s"
              repeatCount="indefinite"
              path="M478,260 a218,62 0 1,0 -436,0 a218,62 0 1,0 436,0"
            />
          </circle>
        </g>

        {/* ── Orbital ring 2 (narrower, faster, opposite tilt) ── */}
        <g transform="rotate(55, 260, 260)">
          <ellipse cx="260" cy="260" rx="200" ry="50" fill="none" stroke="#818cf8" strokeWidth="0.7" strokeOpacity="0.25" strokeDasharray="3 10">
            <animateTransform attributeName="transform" type="rotate" from="360 260 260" to="0 260 260" dur="13s" repeatCount="indefinite" />
          </ellipse>
          {/* Particle on ring 2 */}
          <circle r="3" fill="#a5b4fc" filter="url(#particleGlow)" fillOpacity="0.85">
            <animateMotion
              dur="13s"
              repeatCount="indefinite"
              path="M460,260 a200,50 0 1,1 -400,0 a200,50 0 1,1 400,0"
            />
          </circle>
        </g>

        {/* ── Orbital ring 3 (vertical-ish, slowest) ── */}
        <g transform="rotate(90, 260, 260)">
          <ellipse cx="260" cy="260" rx="185" ry="42" fill="none" stroke="#38bdf8" strokeWidth="0.6" strokeOpacity="0.2" strokeDasharray="2 12">
            <animateTransform attributeName="transform" type="rotate" from="0 260 260" to="360 260 260" dur="24s" repeatCount="indefinite" />
          </ellipse>
          {/* Particle on ring 3 */}
          <circle r="2.5" fill="#7dd3fc" filter="url(#particleGlow)" fillOpacity="0.8">
            <animateMotion
              dur="24s"
              repeatCount="indefinite"
              path="M445,260 a185,42 0 1,0 -370,0 a185,42 0 1,0 370,0"
            />
          </circle>
        </g>

        {/* ── AI core ── */}
        <g filter="url(#coreGlow)">
          {/* Core pulse bg */}
          <circle cx="260" cy="260" r="36" fill="#0d1c33">
            <animate attributeName="r" values="36;42;36" dur="3.5s" repeatCount="indefinite" />
          </circle>
          <circle cx="260" cy="260" r="36" fill="url(#coreGrad)" fillOpacity="0.25">
            <animate attributeName="r" values="36;42;36" dur="3.5s" repeatCount="indefinite" />
            <animate attributeName="fill-opacity" values="0.25;0.08;0.25" dur="3.5s" repeatCount="indefinite" />
          </circle>
          {/* Core ring */}
          <circle cx="260" cy="260" r="30" fill="#060d1a" stroke="#3b82f6" strokeWidth="1" strokeOpacity="0.7" />
          {/* AI label */}
          <text
            x="260" y="265"
            textAnchor="middle"
            dominantBaseline="middle"
            fill="#93c5fd"
            fontSize="18"
            fontWeight="700"
            fontFamily="monospace"
            letterSpacing="2"
            style={{ userSelect: "none" }}
          >
            AI
          </text>
        </g>

        {/* ── Corner tick marks ── */}
        {[
          [88, 260, 64, 260],   // left
          [432, 260, 456, 260], // right
          [260, 88, 260, 64],   // top
          [260, 432, 260, 456], // bottom
        ].map(([x1, y1, x2, y2], i) => (
          <line key={i} x1={x1} y1={y1} x2={x2} y2={y2} stroke="#3b82f6" strokeWidth="1" strokeOpacity="0.25" />
        ))}
      
        
        {/* Connecting Lines to Icons */}
        <g stroke="#3b82f6" strokeWidth="0.8" strokeOpacity="0.4" fill="none">
          {/* To Code Box */}
          <path d="M 330 150 Q 380 150 420 100" strokeDasharray="3 4">
            <animate attributeName="stroke-dashoffset" from="14" to="0" dur="2s" repeatCount="indefinite" />
          </path>
          {/* To DB Box */}
          <path d="M 180 250 Q 120 230 60 250" strokeDasharray="3 4">
            <animate attributeName="stroke-dashoffset" from="14" to="0" dur="2s" repeatCount="indefinite" />
          </path>
          {/* To Atom Box */}
          <path d="M 210 330 Q 160 380 130 410" strokeDasharray="3 4">
            <animate attributeName="stroke-dashoffset" from="14" to="0" dur="2s" repeatCount="indefinite" />
          </path>
          {/* To Server Box */}
          <path d="M 320 330 Q 380 350 400 390" strokeDasharray="3 4">
            <animate attributeName="stroke-dashoffset" from="14" to="0" dur="2s" repeatCount="indefinite" />
          </path>
        </g>

        {/* Floating Icons */}
        {/* 1. Code (Top Right) */}
        <g transform="translate(420, 100)">
          <animateTransform attributeName="transform" type="translate" values="420,100; 420,92; 420,100" dur="5s" repeatCount="indefinite" />
          <rect x="-22" y="-22" width="44" height="44" rx="10" fill="#020810" stroke="#1d4ed8" strokeWidth="1.5" strokeOpacity="0.6" filter="url(#coreGlow)" />
          <text x="0" y="2" textAnchor="middle" dominantBaseline="middle" fill="#60a5fa" fontSize="16" fontWeight="bold" fontFamily="monospace">
            &lt;/&gt;
          </text>
        </g>

        {/* 2. Database (Mid Left) */}
        <g transform="translate(60, 250)">
          <animateTransform attributeName="transform" type="translate" values="60,250; 60,258; 60,250" dur="6s" repeatCount="indefinite" />
          <rect x="-22" y="-22" width="44" height="44" rx="10" fill="#020810" stroke="#1d4ed8" strokeWidth="1.5" strokeOpacity="0.6" filter="url(#coreGlow)" />
          <g stroke="#60a5fa" strokeWidth="1.5" fill="none">
            <ellipse cx="0" cy="-6" rx="9" ry="3" />
            <path d="M -9 -6 v 12 a 9 3 0 0 0 18 0 v -12" />
            <path d="M -9 0 a 9 3 0 0 0 18 0" />
          </g>
        </g>

        {/* 3. Atom (Bottom Left) */}
        <g transform="translate(130, 410)">
          <animateTransform attributeName="transform" type="translate" values="130,410; 130,402; 130,410" dur="4.5s" repeatCount="indefinite" />
          <rect x="-22" y="-22" width="44" height="44" rx="10" fill="#020810" stroke="#1d4ed8" strokeWidth="1.5" strokeOpacity="0.6" filter="url(#coreGlow)" />
          <g stroke="#60a5fa" strokeWidth="1.2" fill="none">
            <ellipse cx="0" cy="0" rx="4" ry="11" transform="rotate(30)" />
            <ellipse cx="0" cy="0" rx="4" ry="11" transform="rotate(-30)" />
            <ellipse cx="0" cy="0" rx="4" ry="11" transform="rotate(90)" />
            <circle cx="0" cy="0" r="1.5" fill="#60a5fa" />
          </g>
        </g>

        {/* 4. Server (Bottom Right) */}
        <g transform="translate(400, 390)">
          <animateTransform attributeName="transform" type="translate" values="400,390; 400,398; 400,390" dur="5.5s" repeatCount="indefinite" />
          <rect x="-22" y="-22" width="44" height="44" rx="10" fill="#020810" stroke="#1d4ed8" strokeWidth="1.5" strokeOpacity="0.6" filter="url(#coreGlow)" />
          <g stroke="#60a5fa" strokeWidth="1.5" fill="none">
            <rect x="-9" y="-9" width="18" height="18" rx="2" />
            <line x1="-9" y1="0" x2="9" y2="0" />
            <circle cx="-5" cy="-4.5" r="1" fill="#60a5fa" stroke="none" />
            <circle cx="-5" cy="4.5" r="1" fill="#60a5fa" stroke="none" />
          </g>
        </g>

      </svg>
    </div>
  );
}
