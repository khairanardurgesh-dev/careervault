import { Hero } from "@/components/landing/hero";
import { ModuleCard } from "@/components/landing/module-card";
import { TrustBadges } from "@/components/landing/trust-badges";
import { Testimonials } from "@/components/landing/testimonials";
import { Comparison } from "@/components/landing/comparison";
import { FAQ } from "@/components/landing/faq";
import { CTA } from "@/components/landing/cta";

const modules = [
  {
    number: "01",
    title: "Resume Mastery System",
    description: "15 editable resume templates, ATS optimisation handbook, achievement-writing frameworks, before-and-after examples, role-specific guidance.",
    icon: (
      <svg className="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
      </svg>
    ),
  },
  {
    number: "02",
    title: "Professional Profile Optimisation",
    description: "LinkedIn and Naukri optimisation, headlines, summaries, experience templates, recruiter visibility checklist, portfolio and professional branding.",
    icon: (
      <svg className="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
      </svg>
    ),
  },
  {
    number: "03",
    title: "Job Search Operating System",
    description: "Excel application tracker, company research worksheet, recruiter outreach templates, referral requests, weekly planner, job description analysis worksheet.",
    icon: (
      <svg className="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
      </svg>
    ),
  },
  {
    number: "04",
    title: "Interview Preparation Vault",
    description: "200 interview questions and answer frameworks, behavioural and HR preparation, STAR workbook, role-specific questions, mock interview scenarios, evaluation scorecards.",
    icon: (
      <svg className="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
      </svg>
    ),
  },
  {
    number: "05",
    title: "Salary & Offer Negotiation System",
    description: "Negotiation scripts, email templates, CTC versus take-home salary calculator, offer comparison spreadsheet, counteroffer decision framework, resignation communication.",
    icon: (
      <svg className="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
    ),
  },
  {
    number: "06",
    title: "AI Career Assistant Toolkit",
    description: "100 tested prompts, resume improvement workflows, job description matching, interview practice, recruiter communication, career research workflows.",
    icon: (
      <svg className="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
      </svg>
    ),
  },
  {
    number: "07",
    title: "90-Day Job Switch Programme",
    description: "Career assessment, skills-gap analysis, 30/60/90-day roadmap, weekly milestones, progress tracking, application and interview planning.",
    icon: (
      <svg className="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
      </svg>
    ),
  },
  {
    number: "08",
    title: "Career Advancement Toolkit",
    description: "Portfolio and project presentation, professional communication, networking frameworks, skills development, role-transition planning, first 90 days in a new job.",
    icon: (
      <svg className="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
      </svg>
    ),
  },
];

const tracks = [
  { name: "Technology & IT", icon: "code", roles: ["SDE", "Senior SDE", "Tech Lead", "Engineering Manager"] },
  { name: "Product & Project Management", icon: "cube", roles: ["APM", "PM", "Senior PM", "Group PM"] },
  { name: "Business Analysis", icon: "search", roles: ["BA", "Senior BA", "Lead BA", "Product Owner"] },
  { name: "Finance", icon: "rupee", roles: ["Analyst", "Senior Analyst", "Manager", "Finance Lead"] },
  { name: "Sales & Marketing", icon: "trending-up", roles: ["SDR", "AE", "Enterprise AE", "Sales Manager"] },
  { name: "Management & Operations", icon: "users", roles: ["Ops Analyst", "Ops Manager", "Program Manager", "COO Track"] },
];

const trackIcons: Record<string, React.ReactNode> = {
  code: <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" /></svg>,
  cube: <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" /></svg>,
  search: <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>,
  rupee: <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>,
  "trending-up": <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" /></svg>,
  users: <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" /></svg>,
};

export default function ProductPage() {
  return (
    <>
      <Hero variant="product" />
      
      {/* Modules Section */}
      <section id="modules" className="section bg-navy-900">
        <div className="container">
          <div className="text-center mb-16">
            <h2 className="heading-2">8 Modules — Everything You Need to Switch</h2>
            <p className="text-white/60 max-w-2xl mx-auto">Each module is a complete toolkit with templates, frameworks, trackers & track-specific bonuses. Download → Customise → Apply.</p>
          </div>
          <div className="feature-grid">
            {modules.map((module) => (
              <ModuleCard key={module.number} {...module} />
            ))}
          </div>
        </div>
      </section>

      {/* Career Tracks */}
      <section className="section bg-navy-950/50 border-y border-white/10">
        <div className="container">
          <div className="text-center mb-16">
            <h2 className="heading-2">6 Career Tracks — Tailored for Your Target Role</h2>
            <p className="text-white/60 max-w-2xl mx-auto">Every module includes track-specific bonuses. You get all 6 tracks — pick your path.</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {tracks.map((track) => (
              <div key={track.name} className="card-elevated group">
                <div className="flex items-center gap-3 mb-4">
                  <div className="w-12 h-12 bg-gradient-to-br from-blue-500/20 to-indigo-500/20 rounded-xl flex items-center justify-center text-blue-400 group-hover:from-blue-500/40 group-hover:to-indigo-500/40 transition-all">
                    {trackIcons[track.icon]}
                  </div>
                  <h3 className="text-xl font-bold text-white">{track.name}</h3>
                </div>
                <ul className="space-y-2">
                  {track.roles.map((role) => (
                    <li key={role} className="flex items-center gap-2 text-white/70 text-sm">
                      <svg className="w-4 h-4 text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                      </svg>
                      {role}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* What You Get Summary */}
      <section className="section bg-navy-900">
        <div className="container">
          <div className="text-center mb-16">
            <h2 className="heading-2">What You Actually Get</h2>
            <p className="text-white/60 max-w-2xl mx-auto">No fluff. Just files you can open, edit, and use today.</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="card-elevated text-center">
              <div className="text-4xl font-bold gradient-text mb-2">389</div>
              <div className="text-white/60">Files in Complete Package</div>
            </div>
            <div className="card-elevated text-center">
              <div className="text-4xl font-bold gradient-text mb-2">200+</div>
              <div className="text-white/60">Interview Frameworks</div>
            </div>
            <div className="card-elevated text-center">
              <div className="text-4xl font-bold gradient-text mb-2">100</div>
              <div className="text-white/60">AI Prompts (Tested)</div>
            </div>
          </div>
        </div>
      </section>

      <TrustBadges />
      <Testimonials />
      <Comparison />
      <FAQ />
      <CTA />
    </>
  );
}