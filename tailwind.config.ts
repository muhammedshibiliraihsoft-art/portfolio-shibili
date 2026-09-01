import type { Config } from 'tailwindcss';

const config: Config = {
  content: ['./src/**/*.{ts,tsx,js,jsx}'],
  darkMode: 'class',
  theme: {
    extend: {
  "colors": {
    "black-50": "#1c1c21",
    "black-100": "#0e0e10",
    "black-200": "#282732",
    "white-50": "#d9ecff",
    "blue-50": "#839cb5",
    "blue-100": "#2d2d38",

    "neutral": "#94a3b8",
    
    "brand": {
      "DEFAULT": "hsl(var(--color-brand) / <alpha-value>)",
      "light": "#5ab0ff",
      "dark": "#004a7f"
    },
    "on-primary": "#002a77",
    "inverse-primary": "rgb(97, 12, 159)",
    "on-secondary-container": "#a1b3ef",
    "secondary-fixed": "#dbe1ff",
    "on-tertiary": "#571f00",
    "surface-container-high": "#282a32",
    "primary-fixed": "#dbe1ff",
    "secondary": "#b4c5ff",
    "tertiary-fixed": "#ffdbcc",
    "background": "#0C1218",
    "on-error-container": "#ffdad6",
    "primary": "rgb(97, 12, 159)",
    "tertiary-fixed-dim": "#ffb695",
    "surface": "#11131b",
    "surface-bright": "#373941",
    "tertiary": "#ffb695",
    "on-tertiary-fixed-variant": "#7b2f00",
    "on-primary-container": "#eff0ff",
    "surface-container-highest": "#32343d",
    "surface-container-lowest": "#0c0e15",
    "on-primary-fixed-variant": "#003ea7",
    "inverse-on-surface": "#2e3039",
    "tertiary-container": "#ba4a00",
    "inverse-surface": "#e1e2ed",
    "on-secondary-fixed-variant": "#324479",
    "primary-fixed-dim": "#b4c5ff",
    "secondary-container": "#324479",
    "on-error": "#690005",
    "surface-container-low": "#191b23",
    "on-tertiary-container": "#ffede6",
    "surface-container": "#1d1f27",
    "error": "#ffb4ab",
    "on-secondary": "#192d61",
    "on-background": "#e1e2ed",
    "surface-tint": "#b4c5ff",
    "on-surface-variant": "#c3c6d7",
    "surface-variant": "#32343d",
    "on-secondary-fixed": "#00174a",
    "outline": "#8d90a0",
    "surface-dim": "#11131b",
    "error-container": "#93000a",
    "on-primary-fixed": "#00174a",
    "secondary-fixed-dim": "#b4c5ff",
    "on-tertiary-fixed": "#351000",
    "outline-variant": "#434654",
    "on-surface": "#f5f5f5",
    "primary-container": "#2864e8"
  },
  "borderRadius": {
    "DEFAULT": "1rem",
    "lg": "2rem",
    "xl": "3rem",
    "full": "9999px"
  },
  "spacing": {
    "content-gap": "64px",
    "container-padding": "24px",
    "gutter": "32px",
    "section-gap": "80px",
    "max-width": "1200px"
  },
  "fontFamily": {
    "sans": ["var(--font-be-vietnam-pro)", "sans-serif"],
      "serif": ["var(--font-gabarito)", "serif"],
    "poppins": ["var(--font-poppins)", "sans-serif"],
    "headline-md": [
      "var(--font-be-vietnam-pro)"
    ],
    "label-mono": [
      "var(--font-jetbrains-mono)"
    ],
    "display-xl": [
      "var(--font-be-vietnam-pro)"
    ],
    "display-lg": [
      "var(--font-be-vietnam-pro)"
    ],
    "body-lg": [
      "var(--font-be-vietnam-pro)"
    ],
    "display-lg-mobile": [
      "var(--font-be-vietnam-pro)"
    ],
    "body-md": [
      "var(--font-be-vietnam-pro)"
    ]
  },
  "fontSize": {
    "headline-md": [
      "48px",
      {
        "lineHeight": "52px",
        "letterSpacing": "-0.02em",
        "fontWeight": "700"
      }
    ],
    "label-mono": [
      "14px",
      {
        "lineHeight": "20px",
        "letterSpacing": "0.05em",
        "fontWeight": "500"
      }
    ],
    "display-xl": [
      "110px",
      {
        "lineHeight": "100px",
        "letterSpacing": "-0.04em",
        "fontWeight": "800"
      }
    ],
    "display-lg": [
      "80px",
      {
        "lineHeight": "76px",
        "letterSpacing": "-0.04em",
        "fontWeight": "800"
      }
    ],
    "body-lg": [
      "20px",
      {
        "lineHeight": "32px",
        "letterSpacing": "0em",
        "fontWeight": "400"
      }
    ],
    "display-lg-mobile": [
      "56px",
      {
        "lineHeight": "54px",
        "letterSpacing": "-0.03em",
        "fontWeight": "800"
      }
    ],
    "body-md": [
      "16px",
      {
        "lineHeight": "26px",
        "letterSpacing": "0em",
        "fontWeight": "400"
      }
    ]
  }
  }
},
  plugins: []
};

export default config;
