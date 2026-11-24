import Link from "next/link";

export default function AccountSettingsPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-3xl font-bold mb-6">Account Settings</h1>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h3 className="text-xl font-medium mb-4">Purchase Details</h3>
              <ul className="space-y-3 text-white/60">
                <li>Order Reference: [Order ID]</li>
                <li>Purchase Date: [Date]</li>
                <li>Product Version: [Version]</li>
                <li>Access: Lifetime</li>
              </ul>
            </div>
            <div>
              <h3 className="text-xl font-medium mb-4">Support Options</h3>
              <ul className="space-y-3 text-white/60">
                <li>
                  <Link href="/contact" className="electric-blue underline">
                    Email support
                  </Link>
                </li>
                <li>Review download history</li>
                <li>Request product update</li>
              </ul>
            </div>
          </div>

          <div className="mt-12 pt-12 border-t border-white/10">
            <p className="text-white/60 mb-4">
              <Link href="/logout" className="electric-blue underline">
                Log Out
              </Link>
            </p>
          </div>
        </div>
      </section>
    </main>
  );
}