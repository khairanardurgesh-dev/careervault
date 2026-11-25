import { Hero } from "@/components/landing/hero";

export default function RefundPolicyPage() {
  return (
    <>
      <Hero variant="product" />
      <section className="section bg-navy-900">
        <div className="container">
          <div className="max-w-3xl mx-auto">
            <div className="text-center mb-12">
              <h1 className="heading-2 mb-4">Refund Policy</h1>
              <p className="text-white/60">Effective date: November 2026</p>
            </div>

            <div className="space-y-8">
              <div className="card-elevated border-green-500/20">
                <h2 className="text-xl font-bold mb-4 text-green-400">✅ You Are Eligible for a Full Refund If:</h2>
                <ul className="space-y-3 text-white/70 list-disc list-inside">
                  <li>You request a refund within <strong>7 calendar days</strong> of verified successful payment.</li>
                  <li>The product is <strong>not as described</strong> on our sales pages (modules missing, files corrupted, features not matching).</li>
                  <li>You experienced a <strong>technical failure</strong> on our side (download links broken, ZIP incomplete, email not delivered) within the 7-day window.</li>
                </ul>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">📋 How to Request a Refund</h2>
                <ol className="space-y-4 text-white/70 list-decimal list-inside">
                  <li>Email <a href="mailto:refunds@careervault.in" className="underline hover:text-blue-400">refunds@careervault.in</a> with subject: "Refund Request — [Your Order ID]".</li>
                  <li>Include: Order reference, purchase email, brief reason (optional but helpful).</li>
                  <li>Our team reviews within <strong>24 hours</strong> (weekdays).</li>
                  <li>If approved, refund is initiated to the <strong>original payment method</strong>.</li>
                  <li>Refund processing time: <strong>5–10 business days</strong> (depends on Razorpay/bank/UPI).</li>
                </ol>
              </div>

              <div className="card-elevated border-amber-500/20">
                <h2 className="text-xl font-bold mb-4 text-amber-400">⚠️ Refunds Are NOT Available For:</h2>
                <ul className="space-y-3 text-white/70 list-disc list-inside">
                  <li>Change of mind after <strong>7 days</strong> from purchase.</li>
                  <li>Not using the product / not finding time to apply it.</li>
                  <li>Not getting a job / interview / salary hike (CareerVault is a toolkit, not a guarantee).</li>
                  <li>Already downloaded and extracted the complete ZIP package <strong>without technical issues</strong>.</li>
                  <li>Sharing/login credentials with others (violates license — access revoked, no refund).</li>
                  <li>Disputing via bank/chargeback instead of contacting us first (delays resolution).</li>
                </ul>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">🔄 Partial Refunds / Exceptions</h2>
                <ul className="space-y-3 text-white/70 list-disc list-inside">
                  <li><strong>Significant mismatch:</strong> If CareerVault is materially different from the product page description (missing modules, advertised features absent), full refund regardless of 7-day window.</li>
                  <li><strong>Duplicate charge:</strong> If you were charged twice for the same order, the duplicate is refunded immediately.</li>
                  <li><strong>Technical failure on our end:</strong> If download/email systems were down false during your 7-day window, we extend eligibility.</li>
                </ul>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">💳 Refund Processing Details</h2>
                <ul className="space-y-3 text-white/70 list-disc list-inside">
                  <li>Refunds are issued to the <strong>original payment method only</strong> (card, UPI, net banking, wallet).</li>
                  <li>Razorpay processes refunds; we cannot redirect to a different account/card.</li>
                  <li>GST invoice is cancelled/credited automatically upon refund.</li>
                  <li>Your CareerVault access is <strong>revoked immediately</strong> upon refund approval (entitlements marked "revoked" in database).</li>
                  <li>You will receive email confirmation at each stage: request received, approved, processed.</li>
                </ul>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">📞 Contact for Refund Issues</h2>
                <p className="text-white/70 leading-relaxed mb-4">
                  If you face any issues with your refund request, escalate to:
                </p>
                <ul className="space-y-2 text-white/70">
                  <li>Email: <a href="mailto:refunds@careervault.in" className="underline hover:text-blue-400">refunds@careervault.in</a></li>
                  <li>Escalation: <a href="mailto:support@careervault.in" className="underline hover:text-blue-400">support@careervault.in</a> (subject: "Refund Escalation")</li>
                  <li>Grievance Officer (DPDP Act): <a href="mailto:grievance@careervault.in" className="underline hover:text-blue-400">grievance@careervault.in</a></li>
                </ul>
              </div>

              <div className="card-elevated bg-blue-500/5 border-blue-500/20">
                <h2 className="text-xl font-bold mb-4">🤝 Our Commitment</h2>
                <p className="text-white/70 leading-relaxed">
                  We trust Indian professionals. The 7-day no-questions policy exists because we believe CareerVault delivers real value. 
                  If it doesn't work for you, we want to know why — your feedback makes the product better for everyone. 
                  No hoops, no runaround, no "retention specialists." Just email us.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}