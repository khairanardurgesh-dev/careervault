import os
import subprocess

base = r"C:\Users\Quick\Desktop\CareerVault\website\careervault"

# Create directory structure
dirs = [
    "app/(marketing)",
    "app/(marketing)/product",
    "app/(marketing)/how-it-works",
    "app/(marketing)/faq",
    "app/(marketing)/contact",
    "app/(marketing)/privacy",
    "app/(marketing)/terms",
    "app/(marketing)/refund-policy",
    "app/checkout",
    "app/payment",
    "app/payment/success",
    "app/payment/failed",
    "app/account",
    "app/account/login",
    "app/account/verify",
    "app/account/library",
    "app/api",
    "app/api/checkout",
    "app/api/razorpay",
    "app/api/account",
    "app/api/downloads",
    "app/api/webhooks",
    "components/marketing",
    "components/checkout",
    "components/portal",
    "components/shared",
    "lib",
    "lib/supabase",
    "lib/razorpay",
    "lib/email",
    "lib/storage",
    "lib/security",
    "lib/validation",
    "config",
    "types",
    "supabase/migrations",
]

for d in dirs:
    full = os.path.join(base, d)
    os.makedirs(full, exist_ok=True)

# Write package.json
package_json = {
    "name": "careervault",
    "version": "0.1.0",
    "private": True,
    "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start",
        "lint": "next lint"
    },
    "dependencies": {
        "next": "latest",
        "react": "latest",
        "react-dom": "latest",
        "typescript": "^5.0.0",
        "tailwindcss": "^3.0.0",
        "postcss": "^8.0.0",
        "autoprefixer": "^10.0.0",
        "supabase": "^2.0.0",
    },
    "devDependencies": {
        "daisyui": "^4.0.0",
    }
}

with open(os.path.join(base, "package.json"), "w") as f:
    import json
    json.dump(package_json, f, indent=2)

# Write tailwind.config.js
tailwind_config = """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,jsx}",
    "./src/**/*.{js,jsx}",
    "./src/components/**/*.{jsx}",
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
      },
    },
  },
  plugins: ["daisyui"],
}
"""

with open(os.path.join(base, "tailwind.config.js"), "w") as f:
    f.write(tailwind_config)

# Write next.config.js
next_config = """/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ["images.unsplash.com", "picsum.photos"],
  },
}

module.exports = nextConfig
"""

with open(os.path.join(base, "next.config.js"), "w") as f:
    f.write(next_config)

# Write tsconfig.json
tsconfig = {
    "compilerOptions": {
        "target": "ES2020",
        "lib": ["ES2020", "DOM", "DOM.Iterable"],
        "strict": True,
        "module": "ESNext",
        "moduleResolution": "bundler",
        "jsx": "react-jsx",
        "esModuleInterop": True,
        "skipLibCheck": True,
        "outDir": "./.next",
        "rootDir": ".",
    },
    "include": ["app", "components", "lib"],
    "exclude": ["node_modules"],
}

with open(os.path.join(base, "tsconfig.json"), "w") as f:
    import json
    json.dump(tsconfig, f, indent=2)

# Write app/layout.tsx
layout_tsx = """import "./globals.css";
import { children, Metadata } from "next";

export const metadata: Metadata = {
  title: "CareerVault - Your Complete Job Switch System",
  description: "Premium digital toolkit for working professionals switching jobs in India. Eight modules, six career tracks, organised career transition system.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
"""

with open(os.path.join(base, "app", "layout.tsx"), "w") as f:
    f.write(layout_tsx)

# Write app/page.tsx (homepage)
page_tsx = """import Image from "next/image";
import Link from "next/link";
import { Button } from "@/components/shared/button";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Your next career move deserves a better strategy.
          </h1>
          <p className="text-lg mb-8 max-w-2xl">
            CareerVault gives you a structured system to prepare your professional profile,
            find better opportunities, perform confidently in interviews, negotiate your offer
            and transition into your next role.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 mb-12">
            <Button asChild>
              <Link href="/checkout" className="flex items-center gap-2">
                <span>Get CareerVault — ₹3,999</span>
              </Link>
            </Button>
            <Button variant="outline" asChild>
              <Link href="/product" className="flex items-center gap-2">
                <span>Explore What's Included</span>
              </Link>
            </Button>
          </div>
        </div>
      </section>
    </main>
  );
}
"""

os.makedirs(os.path.join(base, "app/(marketing)"), exist_ok=True)
with open(os.path.join(base, "app/(marketing)/page.tsx"), "w") as f:
    f.write(page_tsx)

# Write globals.css
globals_css = """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: oklab(98% 0.01 0.01);
    --foreground: oklab(20% 0.02 0.02);
    --card: oklab(100% 0 0);
    --card-foreground: oklab(20% 0.02 0.02);
    --popover: oklab(100% 0 0);
    --popover-foreground: oklab(20% 0.02 0.02);
    --primary: oklab(27% 0.4 0.05);
    --primary-foreground: oklab(98% 0 0);
    --secondary: oklab(27% 0.2 0.02);
    --secondary-foreground: oklab(98% 0 0);
    --muted: oklab(70% 0.02 0.02);
    --muted-foreground: oklab(70% 0.01 0.01);
    --accent: oklab(268% 0.3 0.5);
    --accent-foreground: oklab(98% 0 0);
    --destructive: oklab(36% 0.65 0.45);
    --border: oklab(80% 0.01 0.01);
    --input: oklab(98% 0 0);
    --ring: oklab(27% 0.4 0.05);
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  html {
    font-family: Inter, system-ui, sans-serif;
    line-height: 1.5;
  }

  body {
    background: var(--background);
    color: var(--foreground);
  }

  img {
    max-width: 100%;
    display: block;
  }

  /* Custom electric blue accent */
  .electric-blue {
    color: #3b82f6;
  }
}

@layer components {
  .btn {
    @apply inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-2disabled:relative;
  }

  .btn-primary {
    @apply btn bg-primary text-primary-foreground hover:bg-primary/90;
  }

  .btn-outline {
    @apply btn border border-input hover:bg-accent hover:text-accent-foreground;
  }

  .nav-link {
    @apply relative after:absolute after:left-0 after:bottom-0 after:h-0.5 after:w-0 after-transition-w-0 after:duration-300 hover:after:w-full after:background-current;
  }
}
"""

with open(os.path.join(base, "app/globals.css"), "w") as f:
    f.write(globals_css)

print("Next.js project structure created successfully")
print(f"Base directory: {base}")