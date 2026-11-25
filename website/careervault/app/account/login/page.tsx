import Link from "next/link";
import { Button } from "@/components/shared/button";

export default function AccountLoginPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-md mx-auto">
          <div className="bg-white/5 rounded-xl p-8 text-center">
            <h1 className="text-3xl font-bold mb-4">
              Welcome Back
            </h1>
            <p className="text-white/60 mb-6">
              Enter your purchase email to access your CareerVault library.
            </p>

            <div className="mb-6">
              <input
                type="email"
                placeholder="your.email@example.com"
                className="w-full bg-white/10 border border-white/20 rounded-md px-4 py-3 text-white placeholder-white/40 focus:outline-none focus:border-white/30"
                required
              />
            </div>

            <Button asChild>
              <Link href="/account/verify" className="w-full justify-center">
                <span>Continue</span>
              </Link>
            </Button>
          </div>

          <p className="mt-8 text-white/60">
            <Link href="/">Return to CareerVault</Link>
          </p>
        </div>
      </section>
    </main>
  );
}