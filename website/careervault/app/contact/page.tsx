import Link from "next/link";

export default function ContactPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Contact & Support
          </h1>
          <p className="text-lg mb-8 text-white/60">
            Have a question? We're here to help.
          </p>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div>
              <h3 className="text-xl font-bold mb-4">Support</h3>
              <ul className="space-y-3 text-white/60">
                <li>Payment completed but no access</li>
                <li>Magic link not received</li>
                <li>Unable to download ZIP</li>
                <li>Product file compatibility</li>
                <li>Refund request</li>
              </ul>
            </div>
            <div>
              <h3 className="text-xl font-bold mb-4">Company</h3>
              <ul className="space-y-3 text-white/60">
                <li><Link href="/product">Product Details</Link></li>
                <li><Link href="/how-it-works">How It Works</Link></li>
                <li><Link href="/faq">FAQ</Link></li>
              </ul>
            </div>
            <div>
              <h3 className="text-xl font-bold mb-4">Legal</h3>
              <ul className="space-y-3 text-white/60">
                <li><Link href="/terms">Terms and Conditions</Link></li>
                <li><Link href="/privacy">Privacy Policy</Link></li>
                <li><Link href="/refund-policy">Refund Policy</Link></li>
              </ul>
            </div>
          </div>

          <div className="mt-12 pt-12 border-t border-white/10">
            <p className="text-white/60 mb-4">
              If you cannot find the answer to your question, please email us at
              <a href="mailto:support@careervault.in" className="electric-blue underline">
                support@careervault.in
              </a>
            </p>
            <p className="text-white/60">
              We respond within 2 business days.
            </p>
          </div>
        </div>
      </section>
    </main>
  );
}