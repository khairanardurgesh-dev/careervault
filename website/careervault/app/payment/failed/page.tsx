"use client";

import Link from "next/link";
import { Button } from "@/components/shared/button";

export default function PaymentFailedPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="section">
        <div className="container">
          <div className="max-w-xl mx-auto text-center">
            <div className="w-20 h-20 bg-red-500/20 rounded-full flex items-center justify-center mx-auto mb-8 border border-red-500/30">
              <svg className="w-10 h-10 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </div>
            
            <h1 className="heading-1">Payment Couldn't Be Completed</h1>
            <p className="text-lg text-white/70 mb-10 max-w-xl mx-auto">
              Don't worry — this happens sometimes. Your order hasn't been charged. Let's get you sorted.
            </p>

            <div className="bg-white/5 border border-white/10 rounded-2xl p-6 mb-8 text-left">
              <h3 className="text-lg font-semibold mb-4 flex items-center gap-2 text-amber-400">
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                </svg>
                Common Reasons
              </h3>
              <ul className="space-y-3 text-white/70">
                <li className="flex items-start gap-3">
                  <svg className="w-5 h-5 text-amber-400 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                  <span>Insufficient funds or daily limit reached</span>
                </li>
                <li className="flex items-start gap-3">
                  <svg className="w-5 h-5 text-amber-400 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                  <span>Card expired or invalid details entered</span>
                </li>
                <li className="flex items-start gap-3">
                  <svg className="w-5 h-5 text-amber-400 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                  <span>Bank declined (3D Secure / OTP timeout)</span>
                </li>
                <li className="flex items-start gap-3">
                  <svg className="w-5 h-5 text-amber-400 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                  <span>Network issue or payment gateway timeout</span>
                </li>
              </ul>
            </div>

            <div className="space-y-4">
              <Button asChild className="w-full py-4 text-lg bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700">
                <Link href="/checkout">Retry Payment →</Link>
              </Button>
              <Button variant="outline" asChild className="w-full py-4">
                <Link href="/product">Back to Product Page</Link>
              </Button>
            </div>

            <div className="mt-10 pt-8 border-t border-white/10">
              <p className="text-white/60 mb-2">Still having issues?</p>
              <div className="flex flex-col sm:flex-row gap-3 justify-center">
                <a href="mailto:support@careervault.in" className="text-blue-400 hover:text-blue-300 text-sm font-medium">
                  Email Support →
                </a>
                <a href="https://wa.me/91XXXXXXXXXX" target="_blank" rel="noopener noreferrer" className="text-green-400 hover:text-green-300 text-sm font-medium">
                  WhatsApp Us →
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}