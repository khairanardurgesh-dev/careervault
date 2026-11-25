import { Hero } from "@/components/landing/hero";

export default function TermsPage() {
  return (
    <>
      <Hero variant="product" />
      <section className="section bg-navy-900">
        <div className="container">
          <div className="max-w-3xl mx-auto">
            <div className="text-center mb-12">
              <h1 className="heading-2 mb-4">Terms and Conditions</h1>
              <p className="text-white/60">Last updated: November 2026</p>
            </div>

            <div className="space-y-8">
              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">1. Acceptance of Terms</h2>
                <p className="text-white/70 leading-relaxed">
                  By accessing and using CareerVault (the &quot;Product&quot;), you agree to be bound by these Terms and Conditions (&quot;Terms&quot;). 
                  If you do not agree with any part of these Terms, you may not use the Product.
                </p>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">2. Product Description</h2>
                <p className="text-white/70 leading-relaxed mb-4">
                  CareerVault is a premium downloadable digital toolkit for working professionals with 1–5 years of experience 
                  who want to switch to better jobs, companies, roles, or salaries. It consists of 8 modules, 6 career tracks, 
                  200+ interview frameworks, 100 AI prompts, and supporting templates — delivered as editable files (DOCX, XLSX, PDF, Markdown, Notion).
                </p>
                <p className="text-white/60">
                  <strong>This is not a video course, coaching programme, or job guarantee service.</strong> 
                  CareerVault provides self-guided resources. No employment, job placement, interview success, or salary increase guarantees are made or implied.
                </p>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">3. Purchase & License</h2>
                <ul className="space-y-3 text-white/70 list-disc list-inside">
                  <li><strong>Price:</strong> ₹3,999 (inclusive of 18% GST) — one-time payment.</li>
                  <li><strong>Access:</strong> Lifetime access to the purchased product version (v1.0.0).</li>
                  <li><strong>License:</strong> Personal, non-transferable, non-exclusive license to use the Product for your own career development.</li>
                  <li><strong>Updates:</strong> Free updates to the purchased version. Major version upgrades (v2.0+) may require separate purchase.</li>
                  <li><strong>GST Invoice:</strong> Automatically generated and emailed upon successful payment.</li>
                </ul>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">4. Refund Policy</h2>
                <p className="text-white/70 leading-relaxed mb-4">
                  CareerVault offers a 7-day no-questions-asked refund policy from the date of purchase. 
                  To request a refund, email <a href="mailto:refunds@careervault.in" className="underline hover:text-blue-400">refunds@careervault.in</a> 
                  with your order reference. Refunds are processed to the original payment method within 5–10 business days.
                </p>
                <p className="text-white/60">See the <a href="/refund-policy" className="underline hover:text-blue-400">Refund Policy page</a> for full details.</p>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">5. Intellectual Property</h2>
                <ul className="space-y-3 text-white/70 list-disc list-inside">
                  <li>All CareerVault content, templates, frameworks, prompts, and designs are owned by CareerVault and protected by Indian copyright law.</li>
                  <li>Unauthorised reproduction, distribution, sharing, reselling, or public posting of CareerVault content is strictly prohibited.</li>
                  <li>You may not share your download links, login credentials, or files with others. Team/business licences available separately.</li>
                  <li>Violation may result in immediate access revocation and legal action under the Copyright Act, 1957.</li>
                </ul>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">6. Disclaimer of Warranties</h2>
                <p className="text-white/70 leading-relaxed">
                  CareerVault is provided &quot;as is&quot; and &quot;as available&quot; without warranties of any kind, either express or implied, 
                  including but not limited to implied warranties of merchantability, fitness for a particular purpose, or non-infringement. 
                  We do not warrant that the Product will be uninterrupted, error-free, or that results will be achieved.
                </p>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">7. Limitation of Liability</h2>
                <p className="text-white/70 leading-relaxed">
                  In no event shall CareerVault be liable for any indirect, incidental, special, consequential, or punitive damages, 
                  including without limitation, loss of profits, data, use, goodwill, or other intangible losses, resulting from 
                  your use or inability to use the Product. Our total liability shall not exceed the amount paid by you for the Product.
                </p>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">8. Governing Law & Jurisdiction</h2>
                <p className="text-white/70 leading-relaxed">
                  These Terms shall be governed by and construed in accordance with the laws of India. 
                  Any disputes arising under these Terms shall be subject to the exclusive jurisdiction of the courts in Bangalore, Karnataka.
                </p>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">9. Changes to Terms</h2>
                <p className="text-white/70 leading-relaxed">
                  CareerVault reserves the right to modify these Terms at any time. Updated Terms will be posted on this page 
                  with a revised &quot;Last updated&quot; date. Continued use of the Product after changes constitutes acceptance of the new Terms.
                </p>
              </div>

              <div className="card-elevated">
                <h2 className="text-xl font-bold mb-4">10. Contact</h2>
                <p className="text-white/70 leading-relaxed">
                  For questions about these Terms, contact us at 
                  <a href="mailto:support@careervault.in" className="underline hover:text-blue-400">support@careervault.in</a>.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}