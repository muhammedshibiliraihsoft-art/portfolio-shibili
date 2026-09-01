import re

with open('src/components/hero/AIGlobe.tsx', 'r') as f:
    code = f.read()

boxes_svg = '''
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
'''

# Insert before </svg>
code = code.replace('</svg>', boxes_svg + '\n      </svg>')

with open('src/components/hero/AIGlobe.tsx', 'w') as f:
    f.write(code)

print("Added floating icons")
