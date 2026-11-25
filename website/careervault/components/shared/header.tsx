"use client";

import Link from "next/link";
import { Button } from "./button";

export function Header() {
  return (
    <header className="header sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center gap-8">
            <Link href="/" className="flex items-center gap-2">
              <div className="w-8 h-8 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-lg flex items-center justify-center">
                <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                </svg>
              </div>
              <span className="text-xl font-bold text-white">CareerVault</span>
            </Link>
            <nav className="hidden md:flex items-center gap-6">
              <Link href="/product" className="text-white/70 hover:text-white transition-colors text-sm font-medium">Product</Link>
              <Link href="/faq" className="text-white/70 hover:text-white transition-colors text-sm font-medium">FAQ</Link>
              <Link href="/contact" className="text-white/70 hover:text-white transition-colors text-sm font-medium">Contact</Link>
            </nav>
          </div>
          <div className="flex items-center gap-4">
            <Link href="/account/login">
              <Button variant="outline" className="hidden sm:inline-flex">Sign In</Button>
            </Link>
            <Link href="/checkout">
              <Button className="bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-semibold px-6 py-2">
                Get CareerVault — ₹3,999
              </Button>
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
}