import Link from "next/link";

export default function FaqPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Frequently Asked Questions
          </h1>

          <div className="space-y-4">
            <div>
              <details className="cursor-pointer">
                <summary className="text-lg font-medium text-white cursor-pointer">
                  What exactly is CareerVault?
                </summary>
                <p className="mt-4 text-white/60">
                  CareerVault is a premium downloadable digital toolkit for working professionals
                  with 1–5 years of experience who want to switch to better jobs, companies,
                  roles, or salaries. It is not a video course, coaching programme, or generic
                  collection of ebooks.
                </p>
              </details>
            </div>

            <div>
              <details className="cursor-pointer">
                <summary className="text-lg font-medium text-white cursor-pointer">
                  Who is it designed for?
                </summary>
                <p className="mt-4 text-white/60">
                  Working professionals with approximately 1–5 years of experience who want
                  to switch to better jobs, companies, roles, or salaries.
                </p>
              </details>
            </div>

            <div>
              <details className="cursor-pointer">
                <summary className="text-lg font-medium text-white cursor-pointer">
                  Which career tracks are covered?
                </summary>
                <p className="mt-4 text-white/60">
                  Technology and IT, Business Analysis, Product and Project Management,
                  Finance, Sales and Marketing, and Management and Operations.
                </p>
              </details>
            </div>

            <div>
              <details className="cursor-pointer">
                <summary className="text-lg font-medium text-white cursor-pointer">
                  Is this a video course?
                </summary>
                <p className="mt-4 text-white/60">
                  No. CareerVault is a downloadable digital toolkit consisting of editable
                  documents (DOCX, PDF), Excel workbooks, and structured resources. There are
                  no video lessons or live sessions.
                </p>
              </details>
            </div>

            <div>
              <details className="cursor-pointer">
                <summary className="text-lg font-medium text-white cursor-pointer">
                  What file formats are included?
                </summary>
                <p className="mt-4 text-white/60">
                  DOCX (editable resumes and handbooks), PDF (handbooks and workbooks),
                  XLSX (trackers and calculators), and JSON schemas for the content architecture.
                </p>
              </details>
            </div>

            <div>
              <details className="cursor-pointer">
                <summary className="text-lg font-medium text-white cursor-pointer">
                  Can I edit the templates?
                </summary>
                <p className="mt-4 text-white/60">
                  Yes. All resume templates and many other resources are provided as editable
                  DOCX files that you can customise with your own experience and achievements.
                </p>
              </details>
            </div>

            <div>
              <details className="cursor-pointer">
                <summary className="text-lg font-medium text-white cursor-pointer">
                  How do I access the purchase?
                </summary>
                <p className="mt-4 text-white/60">
                  After completing payment, you will receive a verification email. Click the
                  link to access your personal customer library where you can download all
                  resources or the complete ZIP package.
                </p>
              </details>
            </div>

            <div>
              <details className="cursor-pointer">
                <summary className="text-lg font-medium text-white cursor-pointer">
                  Can I download everything together?
                </summary>
                <p className="mt-4 text-white/60">
                  Yes. Your customer portal includes a &quot;Download Complete CareerVault Package&quot;
                  button that downloads the full ZIP package containing all eight modules.
                </p>
              </details>
            </div>

            <div>
              <details className="cursor-pointer">
                <summary className="text-lg font-medium text-white cursor-pointer">
                  Can I access the product again later?
                </summary>
                <p className="mt-4 text-white/60">
                  Yes. Log in to your customer portal using the email associated with your
                  purchase. You will have lifetime access to the product version you purchased.
                </p>
              </details>
            </div>

            <div>
              <details className="cursor-pointer">
                <summary className="text-lg font-medium text-white cursor-pointer">
                  Does CareerVault guarantee a job?
                </summary>
                <p className="mt-4 text-white/60">
                  No. CareerVault is a self-guided digital toolkit that provides the resources
                  and organisation system to help you manage your job search. It does not
                  guarantee employment, interview success, or salary increases.
                </p>
              </details>
            </div>

            <div>
              <details className="cursor-pointer">
                <summary className="text-lg font-medium text-white cursor-pointer">
                  What is the refund policy?
                </summary>
                <p className="mt-4 text-white/60">
                  CareerVault offers a refund within 7 days of purchase for customers who
                  confirm the product is not what they expected. Refunds are processed via
                  the original payment method. See the Refund Policy page for full details.
                </p>
              </details>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}