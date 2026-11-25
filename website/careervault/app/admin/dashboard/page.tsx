"use client";

import { useState, useEffect } from "react";
import { Button } from "@/components/shared/button";

interface Stats {
  totalOrders: number;
  paidOrders: number;
  pendingOrders: number;
  grossAmount: number;
  netRevenue: number;
  refunds: number;
  recentOrders: Array<{
    id: string;
    customer: string;
    amount: number;
    status: string;
    date: string;
  }>;
}

export default function AdminDashboardPage() {
  const [stats, setStats] = useState<Stats | null>(null);
  const [loading, setLoading] = useState(true);
  const [timeRange, setTimeRange] = useState("7d");

  useEffect(() => {
    // In production, fetch from Supabase with service role
    // Simulate API call
    const fetchStats = async () => {
      await new Promise((resolve) => setTimeout(resolve, 500));
      setStats({
        totalOrders: 1247,
        paidOrders: 983,
        pendingOrders: 12,
        grossAmount: 495672,
        netRevenue: 385234,
        refunds: 24,
        recentOrders: [
          { id: "CV_A1B2C3", customer: "rahul.s@techcorp.com", amount: 3999, status: "paid", date: "2024-01-15" },
          { id: "CV_D4E5F6", customer: "priya.m@startup.io", amount: 3999, status: "paid", date: "2024-01-15" },
          { id: "CV_G7H8I9", customer: "amit.k@finance.co", amount: 3999, status: "pending", date: "2024-01-14" },
          { id: "CV_J0K1L2", customer: "sneha.r@growth.xyz", amount: 3999, status: "paid", date: "2024-01-14" },
          { id: "CV_M3N4O5", customer: "vikram.s@salesforce.com", amount: 3999, status: "paid", date: "2024-01-13" },
          { id: "CV_P6Q7R8", customer: "anjali.g@hdfcbank.com", amount: 3999, status: "refunded", date: "2024-01-13" },
          { id: "CV_S9T0U1", customer: "amit.k@zomato.com", amount: 3999, status: "paid", date: "2024-01-12" },
          { id: "CV_V2W3X4", customer: "sneha.r@swiggy.in", amount: 3999, status: "paid", date: "2024-01-12" },
          { id: "CV_Y5Z6A7", customer: "rahul.m@amazon.in", amount: 3999, status: "paid", date: "2024-01-11" },
          { id: "CV_B8C9D0", customer: "priya.s@flipkart.com", amount: 3999, status: "paid", date: "2024-01-11" },
        ],
      });
      setLoading(false);
    };
    fetchStats();
  }, []);

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat("en-IN", {
      style: "currency",
      currency: "INR",
      maximumFractionDigits: 0,
    }).format(amount);
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case "paid": return "text-green-400 bg-green-500/10";
      case "pending": return "text-amber-400 bg-amber-500/10";
      case "refunded": return "text-red-400 bg-red-500/10";
      default: return "text-white/60 bg-white/10";
    }
  };

  if (loading) {
    return (
      <main className="min-h-screen bg-navy-900 text-white flex items-center justify-center">
        <div className="text-center">
          <div className="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <p className="text-white/60">Loading dashboard...</p>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="section">
        <div className="container">
          <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-10">
            <div>
              <h1 className="heading-2 mb-1">Admin Dashboard</h1>
              <p className="text-white/60">Overview of orders, revenue & activity</p>
            </div>
            <div className="flex items-center gap-4">
              <select
                value={timeRange}
                onChange={(e) => setTimeRange(e.target.value)}
                className="input bg-white/5 border-white/10 text-white w-auto"
              >
                <option value="24h">Last 24 Hours</option>
                <option value="7d">Last 7 Days</option>
                <option value="30d">Last 30 Days</option>
                <option value="90d">Last 90 Days</option>
              </select>
              <Button variant="outline" asChild>
                <a href="/api/admin/export" target="_blank" rel="noopener noreferrer">Export CSV</a>
              </Button>
            </div>
          </div>

          {/* Key Metrics */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-10">
            <div className="card-elevated">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-white/60 text-sm mb-1">Total Orders</p>
                  <p className="text-3xl font-bold text-white">{stats?.totalOrders.toLocaleString("en-IN") || "—"}</p>
                </div>
                <div className="w-12 h-12 bg-blue-500/20 rounded-xl flex items-center justify-center text-blue-400">
                  <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                </div>
              </div>
            </div>
            <div className="card-elevated">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-white/60 text-sm mb-1">Verified Paid</p>
                  <p className="text-3xl font-bold text-green-400">{stats?.paidOrders.toLocaleString("en-IN") || "—"}</p>
                </div>
                <div className="w-12 h-12 bg-green-500/20 rounded-xl flex items-center justify-center text-green-400">
                  <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                </div>
              </div>
            </div>
            <div className="card-elevated">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-white/60 text-sm mb-1">Pending</p>
                  <p className="text-3xl font-bold text-amber-400">{stats?.pendingOrders.toLocaleString("en-IN") || "—"}</p>
                </div>
                <div className="w-12 h-12 bg-amber-500/20 rounded-xl flex items-center justify-center text-amber-400">
                  <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
              </div>
            </div>
          </div>

          {/* Revenue Metrics */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
            <div className="card-elevated">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-white/60 text-sm mb-1">Gross Amount</p>
                  <p className="text-3xl font-bold text-white">{stats?.grossAmount ? formatCurrency(stats.grossAmount) : "—"}</p>
                </div>
                <div className="w-12 h-12 bg-purple-500/20 rounded-xl flex items-center justify-center text-purple-400">
                  <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
              </div>
            </div>
            <div className="card-elevated">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-white/60 text-sm mb-1">Net Revenue</p>
                  <p className="text-3xl font-bold text-green-400">{stats?.netRevenue ? formatCurrency(stats.netRevenue) : "—"}</p>
                </div>
                <div className="w-12 h-12 bg-emerald-500/20 rounded-xl flex items-center justify-center text-emerald-400">
                  <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                  </svg>
                </div>
              </div>
            </div>
            <div className="card-elevated">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-white/60 text-sm mb-1">Refunds</p>
                  <p className="text-3xl font-bold text-red-400">{stats?.refunds.toLocaleString("en-IN") || "—"}</p>
                </div>
                <div className="w-12 h-12 bg-red-500/20 rounded-xl flex items-center justify-center text-red-400">
                  <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </div>
              </div>
            </div>
          </div>

          {/* Recent Orders */}
          <div className="card-elevated">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-bold">Recent Orders</h2>
              <span className="text-white/50 text-sm">{stats?.recentOrders.length} shown</span>
            </div>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead>
                  <tr className="border-b border-white/10">
                    <th className="text-left p-3 text-white/50 text-sm font-medium">Order ID</th>
                    <th className="text-left p-3 text-white/50 text-sm font-medium">Customer</th>
                    <th className="text-right p-3 text-white/50 text-sm font-medium">Amount</th>
                    <th className="text-center p-3 text-white/50 text-sm font-medium">Status</th>
                    <th className="text-left p-3 text-white/50 text-sm font-medium">Date</th>
                  </tr>
                </thead>
                <tbody>
                  {stats?.recentOrders.map((order) => (
                    <tr key={order.id} className="border-b border-white/5 hover:bg-white/5">
                      <td className="p-3 font-mono text-sm text-white">{order.id}</td>
                      <td className="p-3 text-white/70">{order.customer}</td>
                      <td className="p-3 text-right font-semibold text-white">{formatCurrency(order.amount)}</td>
                      <td className="p-3 text-center">
                        <span className={`px-3 py-1 rounded-full text-xs font-medium ${getStatusColor(order.status)}`}>
                          {order.status}
                        </span>
                      </td>
                      <td className="p-3 text-white/60 text-sm">{order.date}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          <div className="mt-10 pt-8 border-t border-white/10 flex flex-col md:flex-row justify-between items-center gap-4">
            <p className="text-white/40 text-sm">CareerVault Admin Panel • Version 1.0.0</p>
            <p className="text-white/40 text-sm">Data refreshed: {new Date().toLocaleString("en-IN")}</p>
          </div>
        </div>
      </section>
    </main>
  );
}