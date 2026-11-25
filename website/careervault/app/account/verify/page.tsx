import Link from "next/link";
import { Button } from "@/components/shared/button";

export default function AccountVerifyPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-md mx-auto">
          <div className="bg-white/5 rounded-xl p-8 text-center">
            <h1 className="text-3xl font-bold mb-4">
              Verify Your Email
            </h1>
            <p className="text-white/60 mb-6">
              A verification link has been sent to your email address. Please check your
              inbox and click the link to access your CareerVault library.
            </p>

            <Button asChild>
              <Link href="/" className="w-full justify-center">
                <span>Go to CareerVault</span>
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