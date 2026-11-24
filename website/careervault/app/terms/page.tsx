import Link from "next/link";

export default function TermsPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Terms and Conditions
          </h1>
          <div className="text-white/60 space-y-4">
            <p>
              <strong>Last updated: November 2026</strong>
            </p>
            <ol className="list-decimal list-inside space-y-2 text-white/60">
              <li>
                By visiting this website, you agree to comply with these Terms and
                Conditions.
              </li>
              <li>
                CareerVault is a premium digital product sold for ₹3,999 one-time payment.
                Payment grants lifetime access to the purchased product version.
              </li>
              <li>
                CareerVault is a self-guided digital toolkit. No employment, job placement,
                or interview success guarantees are made or implied.
              </li>
              <li>
                Refunds are available within 7 days of purchase. See the Refund Policy
                page for full details.
              </li>
              <li>
                Unauthorised reproduction, distribution, or sharing of CareerVault content
                is prohibited and subject to legal action.
              </li>
              <li>
                CareerVault reserves the right to update the product and its contents.
                Update policy will be communicated to customers via email.
              </li>
            </ol>
          </div>
        </div>
      </section>
    </main>
  );
}