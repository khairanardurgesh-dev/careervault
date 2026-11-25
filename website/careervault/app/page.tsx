import Link from "next/link";
import { Button } from "@/components/shared/button";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Your next career move deserves a better strategy.
          </h1>
          <p className="text-lg mb-8 max-w-2xl">
            CareerVault gives you a structured system to prepare your professional profile,
            find better opportunities, perform confidently in interviews, negotiate your offer
            and transition into your next role.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 mb-12">
            <Button asChild>
              <Link href="/checkout" className="flex items-center gap-2">
                <span>Get CareerVault — ₹3,999</span>
              </Link>
            </Button>
            <Button variant="outline" asChild>
              <Link href="/product" className="flex items-center gap-2">
                <span>Explore What&apos;s Included</span>
              </Link>
            </Button>
          </div>
        </div>
      </section>
    </main>
  );
}