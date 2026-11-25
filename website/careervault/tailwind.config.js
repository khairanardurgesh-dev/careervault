/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
        serif: ["Merriweather", "serif"],
      },
      colors: {
        navy: {
          900: "#0f172a",
          800: "#1e293b",
          700: "#334155",
          600: "#475569",
        },
        electric: {
          500: "#3b82f6",
        },
        background: "#0f172a",
        foreground: "#f8fafc",
        card: {
          DEFAULT: "#1e293b",
          foreground: "#f8fafc",
        },
        popover: {
          DEFAULT: "#0f172a",
          foreground: "#f8fafc",
        },
        primary: {
          DEFAULT: "#3b82f6",
          foreground: "#f8fafc",
        },
        secondary: {
          DEFAULT: "#1e293b",
          foreground: "#f8fafc",
        },
        muted: {
          DEFAULT: "#64748b",
          foreground: "#94a3b8",
        },
        accent: {
          DEFAULT: "#3b82f6",
          foreground: "#f8fafc",
        },
        border: "#334155",
        input: "#1e293b",
        ring: "#3b82f6",
      },
    },
  },
  plugins: [],
};
