import Link from "next/link";
import { Button } from "@/components/shared/button";

export default function PaymentFailedPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-xl mx-auto">
          <div className="bg-white/5 rounded-xl p-8 text-center">
            <h1 className="text-3xl font-bold mb-4">
              Your payment could not be completed.
            </h1>
            <p className="text-white/60 mb-6">
              Please try your payment again or contact support if the issue persists.
            </p>
          </div>

          <Button asChild>
            <Link href="/checkout" className="w-full justify-center">
              <span>Retry Payment</span>
            </Link>
          </Button>

          <Button variant="outline" asChild>
            <Link href="/product" className="w-full justify-center mt-4">
              <span>Return to Product</span>
            </Link>
          </Button>
        </div>
      </section>
    </main>
  );
}