import Link from "next/link";

export default function RefundPolicyPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Refund Policy
          </h1>
          <div className="text-white/60 space-y-4">
            <p><strong>Effective date: November 2026</strong></p>
            <ol className="list-decimal list-inside space-y-2 text-white/60">
              <li>
                Customers may request a refund within 7 days of purchase. The 7-day
                period begins at the time of verified successful payment.
              </li>
              <li>
                To request a refund, email support@careervault.in with your order
                reference and the reason for the refund request.
              </li>
              <li>
                Refunds are processed via the original payment method. The processing
                time depends on the payment provider (typically 5-10 business days).
              </li>
              <li>
                Refunds are not available for the ZIP download package after extraction,
                unless the files are corrupted or incomplete due to a download error
                on our side.
              </li>
              <li>
                If CareerVault is found to be significantly different from the
                description on the sales pages, a full refund may be granted regardless
                of the 7-day window.
              </li>
            </ol>
            <p className="mt-6 text-white/60">
              For any refund-related questions, please email support@careervault.in.
            </p>
          </div>
        </div>
      </section>
    </main>
  );
}