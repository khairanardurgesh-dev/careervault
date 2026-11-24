import Link from "next/link";
import { Button } from "@/components/shared/button";
import { useState } from "react";

export default function CheckoutPage() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [mobile, setMobile] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const response = await fetch("/api/checkout", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name, email, mobile }),
      });

      const data = await response.json();

      if (response.ok) {
        // Redirect to Razorpay Checkout
        window.location.href = data.payment_url;
      } else {
        setError(data.message || "Failed to create order");
      }
    } catch (err) {
      setError("Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Your CareerVault Purchase
          </h1>
          <p className="text-lg mb-8 text-white/60">
            Get instant access to the Complete Job Switch System.
          </p>

          {error && (
            <div className="bg-red-500/20 border border-red-500 rounded-xl p-6 mb-8">
              <p className="text-red-300">{error}</p>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label className="block text-white/60 mb-2">Full Name</label>
              <input
                value={name}
                onChange={(e) => setName(e.target.value)}
                type="text"
                required
                className="w-full bg-white/10 border border-white/20 rounded-md px-4 py-3 text-white placeholder-white/40 focus:outline-none focus:border-white/30"
              />
            </div>

            <div>
              <label className="block text-white/60 mb-2">Email Address</label>
              <input
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                type="email"
                required
                className="w-full bg-white/10 border border-white/20 rounded-md px-4 py-3 text-white placeholder-white/40 focus:outline-none focus:border-white/30"
              />
            </div>

            {mobile !== "" && (
              <div>
                <label className="block text-white/60 mb-2">Mobile Number (optional)</label>
                <input
                  value={mobile}
                  onChange={(e) => setMobile(e.target.value)}
                  type="tel"
                  className="w-full bg-white/10 border border-white/20 rounded-md px-4 py-3 text-white placeholder-white/40 focus:outline-none focus:border-white/30"
                />
              </div>
            )}

            <Button type="submit" disabled={loading}>
              {loading ? "Processing..." : "Proceed to Payment — ₹3,999"}
            </Button>
          </form>

          <p className="mt-8 text-white/60">
            <Link href="/product">Back to product page</Link>
          </p>
        </div>
      </section>
    </main>
  );
}