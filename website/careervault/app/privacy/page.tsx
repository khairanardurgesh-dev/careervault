import Link from "next/link";

export default function PrivacyPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Privacy Policy
          </h1>
          <div className="text-white/60 space-y-4">
            <p>
              <strong>Last updated: November 2026</strong>
            </p>
            <ol className="list-decimal list-inside space-y-2 text-white/60">
              <li>
                CareerVault collects the email address provided during checkout and
                verification to create and maintain your customer account.
              </li>
              <li>
                Payment information (e.g., Razorpay transaction IDs) is processed
                solely by Razorpay. CareerVault does not store card details, CVVs, or
                UPI PINs.
              </li>
              <li>
                Customer data is not sold or shared with third parties for marketing
                purposes.
              </li>
              <li>
                Customers can request data deletion or account closure by contacting
                support@careervault.in.
              </li>
              <li>
                Cookies are used solely for essential site functionality and analytics.
              </li>
              <li>
                The privacy policy may be updated periodically. Changes will be
                communicated via email.
              </li>
            </ol>
          </div>
        </div>
      </section>
    </main>
  );
}