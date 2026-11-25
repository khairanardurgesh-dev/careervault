import Link from "next/link";
import { Button } from "@/components/shared/button";

export default function ProductPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            CareerVault Complete Job Switch System
          </h1>
          <p className="text-lg mb-8">
            Premium digital toolkit for working professionals with 1-5 years of experience
            who want to switch to better jobs, companies, roles, or salaries.
          </p>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
            {/* Module cards */}
            <div className="group bg-white/5 border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">01 Resume Mastery System</h3>
              <p className="text-sm text-white/60">
                15 editable resume templates, ATS optimisation handbook, achievement-writing frameworks,
                before-and-after examples, role-specific guidance.
              </p>
            </div>
            <div className="group bg-white/5 border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">02 Professional Profile Optimisation</h3>
              <p className="text-sm text-white/60">
                LinkedIn and Naukri optimisation, headlines, summaries, experience templates,
                recruiter visibility checklist, portfolio and professional branding.
              </p>
            </div>
            <div className="group bg-white/5 border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">03 Job Search Operating System</h3>
              <p className="text-sm text-white/60">
                Excel application tracker, company research worksheet, recruiter outreach templates,
                referral requests, weekly planner, job description analysis worksheet.
              </p>
            </div>
            <div className="group bg-white/5 border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">04 Interview Preparation Vault</h3>
              <p className="text-sm text-white/60">
                200 interview questions and answer frameworks, behavioural and HR preparation,
                STAR workbook, role-specific questions, mock interview scenarios, evaluation scorecards.
              </p>
            </div>
            <div className="group bg-white/5 border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">05 Salary & Offer Negotiation System</h3>
              <p className="text-sm text-white/60">
                Negotiation scripts, email templates, CTC versus take-home salary calculator,
                offer comparison spreadsheet, counteroffer decision framework, resignation communication.
              </p>
            </div>
            <div className="group bg-white/5 border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">06 AI Career Assistant Toolkit</h3>
              <p className="text-sm text-white/60">
                100 tested prompts, resume improvement workflows, job description matching,
                interview practice, recruiter communication, career research workflows.
              </p>
            </div>
            <div className="group bg-white/5 border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">07 90-Day Job Switch Programme</h3>
              <p className="text-sm text-white/60">
                Career assessment, skills-gap analysis, 30/60/90-day roadmap, weekly milestones,
                progress tracking, application and interview planning.
              </p>
            </div>
            <div className="group bg-white/5 border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">08 Career Advancement Toolkit</h3>
              <p className="text-sm text-white/60">
                Portfolio and project presentation, professional communication, networking frameworks,
                skills development, role-transition planning, first 90 days in a new job.
              </p>
            </div>
          </div>

          <div className="mt-12 pt-12 border-t border-white/10">
            <h2 className="text-2xl font-bold mb-6">Six Career Tracks</h2>
            <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
              <div className="bg-white/5 rounded-lg p-3">Technology & IT</div>
              <div className="bg-white/5 rounded-lg p-3">Business Analysis</div>
              <div className="bg-white/5 rounded-lg p-3">Product & Project Management</div>
              <div className="bg-white/5 rounded-lg p-3">Finance</div>
              <div className="bg-white/5 rounded-lg p-3">Sales & Marketing</div>
              <div className="bg-white/5 rounded-lg p-3">Management & Operations</div>
            </div>
          </div>

          <div className="mt-12">
            <h2 className="text-2xl font-bold mb-6">Price</h2>
            <p className="text-4xl font-bold mb-2">₹3,999</p>
            <p className="text-white/60">One-time payment — Lifetime access</p>
            <Button asChild>
              <Link href="/checkout" className="flex items-center gap-2">
                <span>Get Instant Access</span>
              </Link>
            </Button>
          </div>
        </div>
      </section>
    </main>
  );
}