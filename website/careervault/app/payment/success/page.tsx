import Link from "next/link";
import { Button } from "@/components/shared/button";

export default function PaymentSuccessPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-8">
            <h1 className="text-5xl md:text-6xl font-bold mb-4">
              Your CareerVault purchase is confirmed.
            </h1>
            <p className="text-2xl text-white/60">
              Your payment has been verified and your access is ready.
            </p>
          </div>

          <div className="bg-white/5 rounded-xl p-8 max-w-md mx-auto">
            <p className="text-white/60 mb-6">Customer Name: <span className="font-medium">[Name]</span></p>
            <p className="text-white/60 mb-6">Order Reference: <span className="font-medium">[Order ID]</span></p>
            <p className="text-white/60 mb-6">Amount Paid: <span className="font-medium">₹3,999</span></p>
          </div>

          <Button asChild>
            <Link href="/account/library" className="w-full justify-center">
              <span>Access Your Library</span>
            </Link>
          </Button>

          <p className="mt-8 text-white/60">
            <Link href="/product">Return to product page</Link>
          </p>
        </div>
      </section>
    </main>
  );
}