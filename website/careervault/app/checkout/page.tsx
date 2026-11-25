"use client";

import Link from "next/link";
import { Button } from "@/components/shared/button";
import { useState, useEffect } from "react";
import { Hero } from "@/components/landing/hero";

export default function CheckoutPage() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [mobile, setMobile] = useState("");
  const [company, setCompany] = useState("");
  const [gstin, setGstin] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [razorpayLoaded, setRazorpayLoaded] = useState(false);
  const [formErrors, setFormErrors] = useState<Record<string, string>>({});

  useEffect(() => {
    const script = document.createElement("script");
    script.src = "https://checkout.razorpay.com/v1/checkout.js";
    script.async = true;
    script.onload = () => setRazorpayLoaded(true);
    script.onerror = () => setError("Failed to load payment gateway. Please try again.");
    document.body.appendChild(script);
    return () => {
      document.body.removeChild(script);
    };
  }, []);

  const validateForm = () => {
    const errors: Record<string, string> = {};
    if (!name.trim()) errors.name = "Full name is required";
    if (!email.trim()) errors.email = "Email is required";
    else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) errors.email = "Enter a valid email";
    if (mobile && !/^[\d\s\-\+\(\)]{10,}$/.test(mobile)) errors.mobile = "Enter a valid mobile number";
    setFormErrors(errors);
    return Object.keys(errors).length === 0;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    if (!validateForm()) return;
    if (!razorpayLoaded) {
      setError("Payment gateway is still loading. Please wait a moment and try again.");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("/api/checkout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, mobile, company, gstin }),
      });

      const data = await response.json();

      if (!response.ok) {
        setError(data.message || "Failed to create order");
        setLoading(false);
        return;
      }

      // Open Razorpay Checkout
      const options = {
        key: data.key_id,
        amount: data.amount,
        currency: data.currency,
        name: "CareerVault",
        description: "Complete Job Switch System",
        order_id: data.razorpay_order_id,
        prefill: {
          name,
          email,
          contact: mobile || undefined,
        },
        notes: {
          company: company || "N/A",
          gstin: gstin || "N/A",
        },
        theme: { color: "#3b82f6" },
        handler: async function (response: {
          razorpay_payment_id: string;
          razorpay_order_id: string;
          razorpay_signature: string;
        }) {
          setLoading(true);
          try {
            const verifyResponse = await fetch("/api/verify-payment", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                razorpay_order_id: response.razorpay_order_id,
                razorpay_payment_id: response.razorpay_payment_id,
                razorpay_signature: response.razorpay_signature,
                order_id: data.order_id,
              }),
            });

            const verifyData = await verifyResponse.json();

            if (verifyResponse.ok && verifyData.success) {
              window.location.href = "/payment/success";
            } else {
              setError(verifyData.message || "Payment verification failed");
              setLoading(false);
            }
          } catch (err) {
            setError("Payment verification failed. Please contact support.");
            setLoading(false);
          }
        },
        modal: {
          ondismiss: function () {
            setError("Payment cancelled. Please try again.");
            setLoading(false);
          },
        },
      };

      const rzp = new (window as any).Razorpay(options);
      rzp.open();
    } catch (err) {
      setError("Something went wrong. Please try again.");
      setLoading(false);
    }
  };

  return (
    <>
      <Hero variant="checkout" />
      
      <section className="section bg-navy-900">
        <div className="container">
          <div className="max-w-2xl mx-auto">
            {/* Order Summary */}
            <div className="bg-white/5 border border-white/10 rounded-2xl p-6 mb-8">
              <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
                <svg className="w-5 h-5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                Order Summary
              </h3>
              <div className="space-y-3">
                <div className="flex justify-between text-white/70">
                  <span>CareerVault Complete Job Switch System</span>
                  <span className="font-semibold">₹3,999</span>
                </div>
                <div className="flex justify-between text-white/70">
                  <span>GST (18%)</span>
                  <span className="font-semibold">Included</span>
                </div>
                <div className="border-t border-white/10 pt-3 flex justify-between text-white font-semibold text-lg">
                  <span>Total</span>
                  <span>₹3,999</span>
                </div>
              </div>
              <div className="mt-4 p-3 bg-green-500/10 border border-green-500/20 rounded-lg">
                <p className="text-green-400 text-sm flex items-center gap-1">
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                  Lifetime access • Instant download • 7-day refund • GST invoice
                </p>
              </div>
            </div>

            {error && (
              <div className="bg-red-500/20 border border-red-500 rounded-xl p-4 mb-8 animate-slide-down">
                <p className="text-red-300 flex items-center gap-2">
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                  </svg>
                  {error}
                </p>
              </div>
            )}

            {/* Checkout Form */}
            <form onSubmit={handleSubmit} className="space-y-6 bg-white/5 border border-white/10 rounded-2xl p-6 md:p-8">
              <h3 className="text-xl font-semibold mb-6">Billing Details</h3>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label htmlFor="name" className="label">Full Name *</label>
                  <input
                    id="name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    type="text"
                    required
                    className={`input ${formErrors.name ? "input-error" : ""}`}
                    placeholder="Rahul Sharma"
                    aria-invalid={formErrors.name ? "true" : "false"}
                    aria-describedby={formErrors.name ? "name-error" : undefined}
                  />
                  {formErrors.name && (
                    <p id="name-error" className="text-red-400 text-sm mt-1" role="alert">{formErrors.name}</p>
                  )}
                </div>

                <div>
                  <label htmlFor="email" className="label">Email Address *</label>
                  <input
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    type="email"
                    required
                    className={`input ${formErrors.email ? "input-error" : ""}`}
                    placeholder="rahul@company.com"
                    aria-invalid={formErrors.email ? "true" : "false"}
                    aria-describedby={formErrors.email ? "email-error" : undefined}
                  />
                  {formErrors.email && (
                    <p id="email-error" className="text-red-400 text-sm mt-1" role="alert">{formErrors.email}</p>
                  )}
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label htmlFor="mobile" className="label">Mobile Number</label>
                  <input
                    id="mobile"
                    value={mobile}
                    onChange={(e) => setMobile(e.target.value)}
                    type="tel"
                    className={`input ${formErrors.mobile ? "input-error" : ""}`}
                    placeholder="+91 98765 43210"
                    aria-invalid={formErrors.mobile ? "true" : "false"}
                    aria-describedby={formErrors.mobile ? "mobile-error" : undefined}
                  />
                  {formErrors.mobile && (
                    <p id="mobile-error" className="text-red-400 text-sm mt-1" role="alert">{formErrors.mobile}</p>
                  )}
                </div>

                <div>
                  <label htmlFor="company" className="label">Company Name (for GST invoice)</label>
                  <input
                    id="company"
                    value={company}
                    onChange={(e) => setCompany(e.target.value)}
                    type="text"
                    className="input"
                    placeholder="Acme Corp Pvt Ltd"
                  />
                </div>
              </div>

              <div>
                <label htmlFor="gstin" className="label">GSTIN (optional - for input credit)</label>
                <input
                  id="gstin"
                  value={gstin}
                  onChange={(e) => setGstin(e.target.value)}
                  type="text"
                  className="input"
                  placeholder="27AAACA1234A1Z5"
                  maxLength={15}
                />
              </div>

              {/* Trust Indicators */}
              <div className="pt-4 border-t border-white/10 space-y-3">
                <div className="flex items-start gap-3 text-white/70 text-sm">
                  <svg className="w-5 h-5 text-green-400 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                  <span>Secure payment via Razorpay (PCI-DSS Level 1 certified)</span>
                </div>
                <div className="flex items-start gap-3 text-white/70 text-sm">
                  <svg className="w-5 h-5 text-green-400 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                  <span>GST invoice generated automatically — claim input credit</span>
                </div>
                <div className="flex items-start gap-3 text-white/70 text-sm">
                  <svg className="w-5 h-5 text-green-400 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                  <span>7-day no-questions-asked refund policy</span>
                </div>
                <div className="flex items-start gap-3 text-white/70 text-sm">
                  <svg className="w-5 h-5 text-green-400 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                  <span>Instant download access after successful payment</span>
                </div>
              </div>

              <Button
                type="submit"
                disabled={loading || !razorpayLoaded}
                className="w-full py-4 text-lg"
              >
                {loading ? (
                  <>
                    <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                    </svg>
                    Processing...
                  </>
                ) : (
                  <>
                    <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                    </svg>
                    Proceed to Payment — ₹3,999
                  </>
                )}
              </Button>

              <p className="text-center text-white/50 text-sm">
                By proceeding, you agree to our <Link href="/terms" className="underline hover:text-white">Terms</Link> and <Link href="/privacy" className="underline hover:text-white">Privacy Policy</Link>
              </p>
            </form>

            <p className="mt-8 text-center text-white/60">
              <Link href="/product" className="underline hover:text-white">← Back to product page</Link>
            </p>
          </div>
        </div>
      </section>
    </>
  );
}