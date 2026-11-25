const comparisons = [
  { feature: "Price", careervault: "₹3,999 (one-time)", courses: "Subscription-based (varies)", others: "Varies by provider" },
  { feature: "Format", careervault: "Downloadable toolkit (own forever)", courses: "Video lectures (platform-locked)", others: "Subscription access" },
  { feature: "Time to Value", careervault: "Immediate — apply templates today", courses: "50+ hours of videos first", others: "Ongoing monthly commitment" },
  { feature: "Career Tracks", careervault: "6 specialised tracks", courses: "Usually 1 generic track", others: "Generic or 1 track" },
  { feature: "Interview Prep", careervault: "200+ frameworks + STAR workbook", courses: "Basic tips, few examples", others: "Limited question banks" },
  { feature: "AI Prompts", careervault: "Track‑specific prompts (JD matching, resume, interview)", courses: "Rarely included", others: "Not included" },
  { feature: "Negotiation", careervault: "Scripts, CTC calculator (FY24‑25), offer comparison", courses: "Generic advice", others: "Not included" },
  { feature: "Job Search System", careervault: "Excel tracker, outreach templates", courses: "Not included", others: "Basic tracker" },
  { feature: "90‑Day Programme", careervault: "Structured roadmap with milestones", courses: "Not included", others: "Not included" },
  { feature: "Updates", careervault: "Lifetime free updates to v1.0.0", courses: "Varies by platform", others: "Varies" },
  { feature: "Refund", careervault: "7‑day no‑questions‑asked", courses: "Varies", others: "Varies" },
  { feature: "GST Invoice", careervault: "Automatic", courses: "Sometimes", others: "Sometimes" },
];

export function Comparison() {
  return (
    <section className="py-20 lg:py-28 bg-navy-900" aria-label="Comparison">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">Why CareerVault vs Alternatives</h2>
          <p className="text-white/60 max-w-2xl mx-auto">Compare the complete picture — not just price</p>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full min-w-[800px]">
            <thead>
              <tr className="border-b border-white/10">
                <th className="text-left p-4 font-semibold text-white sticky left-0 bg-navy-900 z-10">Feature</th>
                <th className="text-center p-4 font-semibold text-white bg-gradient-to-br from-blue-500/20 to-indigo-500/20">
                  <div className="flex items-center justify-center gap-2">
                    <div className="w-2 h-2 bg-blue-400 rounded-full" />
                    <span>CareerVault</span>
                  </div>
                </th>
                <th className="text-center p-4 font-semibold text-white/60">Typical Courses (₹20K+)</th>
                <th className="text-center p-4 font-semibold text-white/60">Subscription Platforms</th>
              </tr>
            </thead>
            <tbody>
              {comparisons.map((row, i) => (
                <tr key={i} className={`border-b border-white/5 ${i % 2 === 0 ? "bg-white/5" : ""}`}>
                  <td className="text-left p-4 font-medium text-white">{row.feature}</td>
                  <td className="text-center p-4 text-green-400 font-medium bg-blue-500/5">{row.careervault}</td>
                  <td className="text-center p-4 text-white/50">{row.courses}</td>
                  <td className="text-center p-4 text-white/50">{row.others}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div className="mt-12 text-center">
          <p className="text-white/60 mb-4">One-time ₹3,999 = Lifetime access to everything above</p>
          <p className="text-white/50 text-sm">vs ₹2,000+/month forever on subscription platforms</p>
        </div>
      </div>
    </section>
  );
}