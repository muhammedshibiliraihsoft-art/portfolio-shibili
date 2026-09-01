import re

with open('src/components/hero/AIGlobe.tsx', 'r') as f:
    code = f.read()

lines_svg = '''
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
'''

# Insert before {/* Floating Icons */}
code = code.replace('{/* Floating Icons */}', lines_svg + '\n        {/* Floating Icons */}')

with open('src/components/hero/AIGlobe.tsx', 'w') as f:
    f.write(code)

print("Added connecting lines")
