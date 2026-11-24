import Link from "next/link";

export default function AdminDashboardPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-7xl mx-auto">
          <h1 className="text-4xl font-bold mb-6">
            Admin Dashboard
          </h1>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-12">
            {/* Cards */}
            <div className="bg-white/5 rounded-xl p-6">
              <h3 className="text-xl font-medium mb-4">Total Orders</h3>
              <p className="text-3xl font-bold">1,247</p>
            </div>
            <div className="bg-white/5 rounded-xl p-6">
              <h3 className="text-xl font-medium mb-4">Verified Paid</h3>
              <p className="text-3xl font-bold">983</p>
            </div>
            <div className="bg-white/5 rounded-xl p-6">
              <h3 className="text-xl font-medium mb-4">Pending</h3>
              <p className="text-3xl font-bold">12</p>
            </div>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-12">
            <div className="bg-white/5 rounded-xl p-6">
              <h3 className="text-xl font-medium mb-4">Gross Amount</h3>
              <p className="text-2xl font-bold">₹4,95,672</p>
            </div>
            <div className="bg-white/5 rounded-xl p-6">
              <h3 className="text-xl font-medium mb-4">Net Revenue</h3>
              <p className="text-2xl font-bold">₹3,85,234</p>
            </div>
            <div className="bg-white/5 rounded-xl p-6">
              <h3 className="text-xl font-medium mb-4">Refunds</h3>
              <p className="text-2xl font-bold">24</p>
            </div>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-4 gap-6 mb-12">
            <div className="bg-white/5 rounded-xl p-6">
              <h3 className="text-xl font-medium mb-4">Recent Purchases</h3>
              <p className="text-white/60 text-sm">Last 10 orders</p>
            </div>
            <div className="bg-white/5 rounded-xl p-6">
              <h3 className="text-xl font-medium mb-4">Download Activity</h3>
              <p className="text-white/60 text-sm">Total downloads</p>
            </div>
            <div className="bg-white/5 rounded-xl p-6">
              <h3 className="text-xl font-medium mb-4">Webhook Status</h3>
              <p className="text-white/60 text-sm">Processing rate</p>
            </div>
            <div className="bg-white/5 rounded-xl p-6">
              <h3 className="text-xl font-medium mb-4">Support Tickets</h3>
              <p className="text-white/60 text-sm">Open tickets</p>
            </div>
          </div>

          <div className="mt-12 pt-12 border-t border-white/10 text-white/60">
            <p>CareerVault Admin Panel • Version 1.0</p>
          </div>
        </div>
      </section>
    </main>
  );
}