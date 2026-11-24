import Link from "next/link";
import { Button } from "@/components/shared/button";

export default function MarketingPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            CareerVault
          </h1>
          <p className="text-lg mb-8 max-w-2xl">
            Your complete system for landing a better job.
          </p>
          <div className="flex flex-col sm:flex-row gap-4">
            <Button asChild>
              <Link href="/product" className="flex items-center gap-2">
                <span>Explore What&rsquo;s Included</span>
              </Link>
            </Button>
            <Button asChild>
              <Link href="/checkout" className="flex items-center gap-2">
                <span>Get CareerVault &mdash; ₹3,999</span>
              </Link>
            </Button>
          </div>
        </div>
      </section>
    </main>
  );
}
