"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { Button } from "@/components/shared/button";

export function Testimonials() {
  const highlights = [
    "15 Resume Templates — ATS‑optimised, industry‑specific .docx files",
    "200+ Interview Questions — Commercial JSON bank with answer frameworks",
    "389 Total Files — Lifetime access to all 8 modules and 6 career tracks",
    "6 Career Tracks — Technology, PM, Finance, Sales, BA, Operations with specific resources",
    "AI Prompt Library — Track‑specific prompts for JD matching, interview practice, resume improvement",
    "90‑Day Programme — Daily action calendar, assessments, milestone tracker and review templates",
  ];

  const [index, setIndex] = useState(0);

  useEffect(() => {
    const timeout = setTimeout(() => {
      setIndex((i) => (i + 1) % highlights.length);
    }, 4000);
    return () => clearTimeout(timeout);
  }, []);

  return (
    <section className="py-20 lg:py-28 bg-navy-900" aria-label="Product Highlights">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">What You'll Get</h2>
          <p className="text-white/60 max-w-2xl mx-auto">A breakdown of the complete CareerVault system.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {highlights.map((h, i) => (
            <div key={i} className="bg-white/5 border border-white/10 rounded-xl p-6 text-center">
              <h3 className="text-white font-semibold mb-2">{i + 1}. {highlights[i]}</h3>
            </div>
          ))}
        </div>
        <Button asChild>
          <Link href="/product" className="w-full py-3">
            <span>Explore CareerVault →</span>
          </Link>
        </Button>
      </div>
    </section>
  );
}