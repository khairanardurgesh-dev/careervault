"use client";

import Link from "next/link";
import { Button } from "../shared/button";

interface HeroProps {
  variant?: "home" | "product" | "checkout";
}

export function Hero({ variant = "home" }: HeroProps) {
  const stats = [
    { label: "Interview Frameworks", value: "200+" },
    { label: "Career Tracks", value: "6" },
  ];

  const trustBadges = [
    "Lifetime Access",
    "Instant Download",
    "No Subscription",
    "GST Invoice",
    "7-Day Refund",
    "Email Support",
  ];

  if (variant === "checkout") {
    return (
      <section className="relative overflow-hidden bg-gradient-to-b from-navy-900 via-navy-900 to-navy-950 py-16 lg:py-24">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl mx-auto text-center">
            <div className="inline-flex items-center gap-2 bg-green-500/10 border border-green-500/20 text-green-400 px-4 py-2 rounded-full text-sm font-medium mb-6">
              <span className="relative flex h-2 w-2">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2 w-2 bg-green-500"></span>
              </span>
              Secure Checkout — Razorpay Protected
            </div>
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight mb-6">
              Complete Your Purchase
            </h1>
            <p className="text-lg text-white/70 mb-8 max-w-2xl mx-auto">
              Get instant access to the Complete Job Switch System. Join 2,800+ professionals who&apos;ve already made the switch.
            </p>
            <div className="flex flex-wrap items-center justify-center gap-4 mb-10">
              {trustBadges.map((badge) => (
                <span key={badge} className="bg-white/5 border border-white/10 px-4 py-2 rounded-full text-sm text-white/80">
                  {badge}
                </span>
              ))}
            </div>
          </div>
        </div>
      </section>
    );
  }

  if (variant === "product") {
    return (
      <section className="relative overflow-hidden bg-gradient-to-b from-navy-900 via-navy-900 to-navy-950 py-16 lg:py-24">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-4xl mx-auto text-center">
            <div className="inline-flex items-center gap-2 bg-blue-500/10 border border-blue-500/20 text-blue-400 px-4 py-2 rounded-full text-sm font-medium mb-6">
              <span>🇮🇳 Built for Indian Professionals</span>
            </div>
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight mb-6">
              CareerVault Complete Job Switch System
            </h1>
            <p className="text-lg text-white/70 mb-10 max-w-2xl mx-auto">
              The only structured toolkit you need to prepare, search, interview, negotiate & transition — tailored for 6 Indian career tracks.
            </p>
            <div className="flex flex-wrap items-center justify-center gap-4 mb-10">
              {trustBadges.map((badge) => (
                <span key={badge} className="bg-white/5 border border-white/10 px-4 py-2 rounded-full text-sm text-white/80">
                  {badge}
                </span>
              ))}
            </div>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button asChild className="w-full sm:w-auto bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-semibold px-8 py-3 text-lg">
                <Link href="/checkout">Get Instant Access — ₹3,999</Link>
              </Button>
              <Button variant="outline" asChild className="w-full sm:w-auto px-8 py-3 text-lg">
                <Link href="#modules">Explore Modules →</Link>
              </Button>
            </div>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section className="relative overflow-hidden bg-gradient-to-b from-navy-900 via-navy-900 to-navy-950 py-20 lg:py-32">
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-blue-500/10 via-transparent to-transparent" />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        <div className="max-w-4xl mx-auto text-center">
          <div className="inline-flex items-center gap-2 bg-blue-500/10 border border-blue-500/20 text-blue-400 px-4 py-2 rounded-full text-sm font-medium mb-6">
            <span>🇮🇳 India&apos;s Most Structured Job Switch System</span>
          </div>
          <h1 className="text-4xl md:text-5xl lg:text-7xl font-bold tracking-tight mb-6 leading-tight">
            Your next career move deserves a <span className="bg-gradient-to-r from-blue-400 to-indigo-300 bg-clip-text text-transparent">better strategy</span>.
          </h1>
          <p className="text-lg md:text-xl text-white/70 mb-10 max-w-2xl mx-auto leading-relaxed">
            Stop guessing. Start executing. 8 modules, 389 files, 6 career tracks — everything to land a better role, salary & company.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center mb-16">
            <Button asChild className="w-full sm:w-auto bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-semibold px-8 py-4 text-lg">
              <Link href="/checkout">Get CareerVault — ₹3,999</Link>
            </Button>
            <Button variant="outline" asChild className="w-full sm:w-auto px-8 py-4 text-lg">
              <Link href="/product">Explore What&apos;s Inside →</Link>
            </Button>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6 md:gap-8 mb-16">
            {stats.map((stat) => (
              <div key={stat.label} className="text-center">
                <div className="text-3xl md:text-4xl lg:text-5xl font-bold bg-gradient-to-r from-blue-400 to-indigo-300 bg-clip-text text-transparent">
                  {stat.value}
                </div>
                <div className="text-white/60 text-sm mt-1">{stat.label}</div>
              </div>
            ))}
          </div>

          {/* Trust Badges */}
          <div className="flex flex-wrap items-center justify-center gap-3">
            {trustBadges.map((badge) => (
              <span key={badge} className="bg-white/5 border border-white/10 px-4 py-2 rounded-full text-sm text-white/80 flex items-center gap-1">
                <svg className="w-4 h-4 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                </svg>
                {badge}
              </span>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}