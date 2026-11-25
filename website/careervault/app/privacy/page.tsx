import { Hero } from "@/components/landing/hero";

export default function PrivacyPage() {
  return (
    <>
      <Hero variant="product" />
      <section className="section bg-navy-900">
        <div className="container">
          <div className="max-w-3xl mx-auto">
            <div className="text-center mb-12">
              <h1 className="heading-2 mb-4">Privacy Policy</h1>
              <p className="text-white/60">Last updated: November 2026</p>
            </div>

            <div className="space-y-8">
              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">1. Data We Collect</h2>
                <ul className="space-y-3 text-white/70 list-disc list-inside">
                  <li><strong>Account Data:</strong> Email address (from checkout/verification), name (optional), company name & GSTIN (optional, for invoice).</li>
                  <li><strong>Payment Data:</strong> Razorpay transaction IDs, order IDs, payment status. <strong>We never store card numbers, CVVs, UPI PINs, or net banking credentials.</strong> All sensitive payment processing is handled by Razorpay (PCI-DSS Level 1 certified).</li>
                  <li><strong>Usage Data:</strong> Download events (which module, when), email open/click events (for transactional emails only).</li>
                  <li><strong>Technical Data:</strong> IP address, browser/user agent, referral source (for fraud prevention & analytics).</li>
                </ul>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">2. How We Use Your Data</h2>
                <ul className="space-y-3 text-white/70 list-disc list-inside">
                  <li>Create and manage your customer account (login, library access).</li>
                  <li>Process payments and generate GST invoices via Razorpay.</li>
                  <li>Send transactional emails: order confirmation, magic links, download links, invoice, refund updates.</li>
                  <li>Prevent fraud (monitor suspicious login/download patterns).</li>
                  <li>Analytics: aggregate, anonymised usage stats (no personal identifiers).</li>
                  <li>Legal compliance: GST records, refund audit trail.</li>
                </ul>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">3. Data Sharing</h2>
                <p className="text-white/70 leading-relaxed mb-4">
                  We do <strong>not</strong> sell your personal data. We share data only with:
                </p>
                <ul className="space-y-3 text-white/70 list-disc list-inside">
                  <li><strong>Razorpay:</strong> Payment processing (PCI-DSS compliant). They process payments on our behalf.</li>
                  <li><strong>Supabase:</strong> Database & auth hosting (SOC 2 Type II, ISO 27001). Data stored in their infrastructure.</li>
                  <li><strong>Resend:</strong> Transactional email delivery. Only email address & name shared.</li>
                  <li><strong>Legal authorities:</strong> When required by Indian law (court order, government request).</li>
                </ul>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">4. Data Retention</h2>
                <ul className="space-y-3 text-white/70 list-disc list-inside">
                  <li>Account data: Retained while your account is active. Deleted within 30 days of account closure request.</li>
                  <li>Payment/order data: Retained for 7 years (GST/tax compliance under Indian law).</li>
                  <li>Download/email logs: Retained for 2 years (support audit trail).</li>
                  <li>Technical logs: Retained for 90 days.</li>
                </ul>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">5. Your Rights (Under DPDP Act, 2023)</h2>
                <ul className="space-y-3 text-white/70 list-disc list-inside">
                  <li><strong>Access:</strong> Request a copy of your personal data.</li>
                  <li><strong>Correction:</strong> Update inaccurate data (email, name, company).</li>
                  <li><strong>Deletion:</strong> Request account closure & data deletion (except payment records required by law).</li>
                  <li><strong>Portability:</strong> Receive your data in structured format (JSON/CSV).</li>
                  <li><strong>Objection:</strong> Opt out of non-essential processing (analytics).</li>
                </ul>
                <p className="text-white/60 mt-4">
                  To exercise these rights, email <a href="mailto:privacy@careervault.in" className="underline hover:text-blue-400">privacy@careervault.in</a> with "DPDP Request" in subject.
                </p>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">6. Cookies & Tracking</h2>
                <ul className="space-y-3 text-white/70 list-disc list-inside">
                  <li><strong>Essential cookies:</strong> Session management, CSRF protection, auth tokens. Cannot be disabled.</li>
                  <li><strong>Analytics cookies:</strong> Vercel Analytics (anonymous, no personal data). Opt-out via browser DNT.</li>
                  <li><strong>No marketing cookies:</strong> We don't use Facebook Pixel, Google Ads, or third-party trackers.</li>
                </ul>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">7. Security</h2>
                <ul className="space-y-3 text-white/70 list-disc list-inside">
                  <li>All data encrypted in transit (TLS 1.3) and at rest (AES-256 via Supabase).</li>
                  <li>Row Level Security (RLS) enforced on all database tables — customers only see their own data.</li>
                  <li>Service role keys (full DB access) never exposed to browser; used only in server-side API routes.</li>
                  <li>Magic links expire in 1 hour; single-use tokens.</li>
                  <li>Regular dependency updates & vulnerability scanning.</li>
                </ul>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">8. International Transfers</h2>
                <p className="text-white/70 leading-relaxed">
                  Supabase (database) and Resend (email) may process data on servers outside India. 
                  Both are GDPR-compliant and provide Standard Contractual Clauses (SCCs) for international transfers. 
                  Razorpay processes payments within India.
                </p>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">9. Children's Privacy</h2>
                <p className="text-white/70 leading-relaxed">
                  CareerVault is intended for working professionals aged 18+. We do not knowingly collect data from minors. 
                  If you believe a minor has provided data, contact us immediately for deletion.
                </p>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">10. Changes to This Policy</h2>
                <p className="text-white/70 leading-relaxed">
                  Updates will be posted here with a revised "Last updated" date. Material changes will be emailed to all customers. 
                  Continued use constitutes acceptance.
                </p>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">11. Contact</h2>
                <p className="text-white/70 leading-relaxed">
                  Data Protection Officer: <a href="mailto:privacy@careervault.in" className="underline hover:text-blue-400">privacy@careervault.in</a><br />
                  Grievance Officer (DPDP Act): <a href="mailto:grievance@careervault.in" className="underline hover:text-blue-400">grievance@careervault.in</a>
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}