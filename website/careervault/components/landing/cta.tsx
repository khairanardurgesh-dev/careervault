import Link from "next/link";
import { Button } from "../shared/button";

export function CTA() {
  return (
    <section className="py-20 lg:py-28 relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-r from-blue-500/10 via-transparent to-indigo-500/10" />
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-blue-500/20 via-transparent to-transparent" />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        <div className="bg-white/5 border border-white/10 rounded-3xl p-8 md:p-16 text-center">
          <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold mb-6">
            Ready to Make Your Move?
          </h2>
          <p className="text-lg md:text-xl text-white/70 mb-10 max-w-2xl mx-auto">
            Your structured system for switching roles, companies, or salaries is ready. Your toolkit is waiting.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button asChild className="w-full sm:w-auto bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-semibold px-8 py-4 text-lg">
              <Link href="/checkout">Get CareerVault — ₹3,999</Link>
            </Button>
            <Button variant="outline" asChild className="w-full sm:w-auto px-8 py-4 text-lg">
              <Link href="/product">Explore Modules First →</Link>
            </Button>
          </div>
          <p className="mt-6 text-white/50 text-sm">
            Secure checkout via Razorpay • Instant download • 7-day refund • GST invoice
          </p>
        </div>
      </div>
    </section>
  );
}