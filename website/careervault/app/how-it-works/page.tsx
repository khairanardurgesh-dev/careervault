import Link from "next/link";
import { Button } from "@/components/shared/button";

export default function HowItWorksPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            How It Works
          </h1>
          <p className="text-lg mb-12 max-w-2xl">
            Getting started with CareerVault is simple and straightforward.
          </p>

          <ol className="list-decimal list-inside space-y-6 text-white/60">
            <li>
              <h3 className="text-xl font-medium mb-2">Purchase CareerVault</h3>
              <p>Complete the one-time payment of ₹3,999 through our secure checkout.</p>
            </li>
            <li>
              <h3 className="text-xl font-medium mb-2">Verify Your Email</h3>
              <p>Check your inbox for a verification email and click the secure link.</p>
            </li>
            <li>
              <h3 className="text-xl font-medium mb-2">Open Your Library</h3>
              <p>Access your personal CareerVault customer portal with all eight modules.</p>
            </li>
            <li>
              <h3 className="text-xl font-medium mb-2">Explore Modules</h3>
              <p>Browse individual modules or download the complete ZIP package.</p>
            </li>
            <li>
              <h3 className="text-xl font-medium mb-2">Download Resources</h3>
              <p>Download individual files or the complete CareerVault ZIP package.</p>
            </li>
            <li>
              <h3 className="text-xl font-medium mb-2">Follow the Programme</h3>
              <p>Use the 90-day job-switch roadmap to organise your transition.</p>
            </li>
          </ol>

          <div className="mt-12">
            <Button asChild>
              <Link href="/checkout" className="flex items-center gap-2">
                <span>Get Started — ₹3,999</span>
              </Link>
            </Button>
          </div>
        </div>
      </section>
    </main>
  );
}