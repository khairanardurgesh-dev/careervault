"use client";

import Link from "next/link";
import { Button } from "@/components/shared/button";
import { useEffect, useState } from "react";

export default function PaymentSuccessPage() {
  const [orderData, setOrderData] = useState<{
    name: string;
    orderId: string;
    amount: string;
    email: string;
  } | null>(null);

  useEffect(() => {
    // In production, this would come from the verified payment response
    // For now, we'll show placeholder data
    const params = new URLSearchParams(window.location.search);
    const name = params.get("name") || "Professional";
    const orderId = params.get("order_id") || "CV_" + Date.now().toString(36).toUpperCase();
    
    setOrderData({
      name,
      orderId,
      amount: "₹3,999",
      email: params.get("email") || "your@email.com",
    });
  }, []);

  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="section">
        <div className="container">
          <div className="max-w-2xl mx-auto text-center">
            <div className="w-20 h-20 bg-gradient-to-br from-green-500 to-emerald-600 rounded-full flex items-center justify-center mx-auto mb-8 animate-pulse-glow">
              <svg className="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
              </svg>
            </div>
            
            <h1 className="heading-1">Welcome to CareerVault! 🎉</h1>
            <p className="text-lg text-white/70 mb-10 max-w-xl mx-auto">
              Your payment has been verified. You now have lifetime access to the Complete Job Switch System.
            </p>

            {orderData && (
              <div className="bg-white/5 border border-white/10 rounded-2xl p-6 mb-8 text-left">
                <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
                  <svg className="w-5 h-5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                  Order Confirmed
                </h3>
                <div className="space-y-3 text-white/70">
                  <div className="flex justify-between">
                    <span>Customer</span>
                    <span className="font-semibold">{orderData.name}</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Order ID</span>
                    <span className="font-mono font-semibold">{orderData.orderId}</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Amount Paid</span>
                    <span className="font-semibold text-green-400">{orderData.amount}</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Email</span>
                    <span className="font-semibold">{orderData.email}</span>
                  </div>
                </div>
                <div className="mt-4 p-3 bg-green-500/10 border border-green-500/20 rounded-lg">
                  <p className="text-green-400 text-sm flex items-center gap-1">
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                    GST invoice sent to your email. Download link ready below.
                  </p>
                </div>
              </div>
            )}

            <div className="space-y-4">
              <Button asChild className="w-full py-4 text-lg">
                <Link href="/account/library">Access Your Library →</Link>
              </Button>
              <Button variant="outline" asChild className="w-full py-4">
                <Link href="/product">View Product Details</Link>
              </Button>
            </div>

            <div className="mt-10 pt-8 border-t border-white/10">
              <h3 className="text-lg font-semibold mb-4">What happens next?</h3>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-left">
                <div className="bg-white/5 border border-white/10 rounded-xl p-4">
                  <div className="w-10 h-10 bg-blue-500/20 rounded-lg flex items-center justify-center text-blue-400 mb-3">
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                    </svg>
                  </div>
                  <h4 className="font-semibold mb-1">1. Download</h4>
                  <p className="text-white/60 text-sm">Get all 389 files instantly from your library</p>
                </div>
                <div className="bg-white/5 border border-white/10 rounded-xl p-4">
                  <div className="w-10 h-10 bg-purple-500/20 rounded-lg flex items-center justify-center text-purple-400 mb-3">
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                    </svg>
                  </div>
                  <h4 className="font-semibold mb-1">2. Customise</h4>
                  <p className="text-white/60 text-sm">Edit templates with your details, target role, track</p>
                </div>
                <div className="bg-white/5 border border-white/10 rounded-xl p-4">
                  <div className="w-10 h-10 bg-green-500/20 rounded-lg flex items-center justify-center text-green-400 mb-3">
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                    </svg>
                  </div>
                  <h4 className="font-semibold mb-1">3. Apply</h4>
                  <p className="text-white/60 text-sm">Start applications, prep interviews, negotiate offers</p>
                </div>
              </div>
            </div>

            <p className="mt-8 text-white/50 text-sm">
              Need help? Email us at <a href="mailto:support@careervault.in" className="underline hover:text-white">support@careervault.in</a>
            </p>
          </div>
        </div>
      </section>
    </main>
  );
}