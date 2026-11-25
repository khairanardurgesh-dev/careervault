import Link from "next/link";

interface ModuleCardProps {
  number: string;
  title: string;
  description: string;
  files?: string[];
  trackSpecific?: string[];
  icon: React.ReactNode;
}

const moduleDetails: Record<string, { files: string[]; trackSpecific?: string[] }> = {
  "01": {
    files: [
      "15 ATS-optimised resume templates (Word + LaTeX)",
      "Achievement-writing framework (CAR method)",
      "Before/after resume transformations (12 examples)",
      "Role-specific bullet banks (Tech, BA, PM, Finance, Sales, Ops)",
      "ATS keyword optimisation handbook",
      "Cover letter templates (5 variants)",
      "Resume review checklist (50-point)",
    ],
    trackSpecific: ["Tech: GitHub/portfolio integration guide", "PM: Product sense showcase template", "Finance: Quant achievement templates"],
  },
  "02": {
    files: [
      "LinkedIn headline formula (30+ examples)",
      "About section templates (StoryBrand framework)",
      "Experience description templates (STAR-based)",
      "Skills & endorsements strategy guide",
      "Naukri.com profile optimisation checklist",
      "Recruiter visibility audit worksheet",
      "Personal branding content calendar",
      "Portfolio website template (Notion + Framer)",
    ],
    trackSpecific: ["Tech: GitHub/README showcase guide", "PM: Product portfolio case study template", "Sales: Revenue dashboard screenshots guide"],
  },
  "03": {
    files: [
      "Excel application tracker (auto-filtering, status, follow-ups)",
      "Company research worksheet (20-point framework)",
      "Recruiter outreach templates (cold email + LinkedIn DM)",
      "Referral request scripts (weak/strong ties)",
      "Weekly job search planner (KPIs + time blocks)",
      "JD analysis worksheet (requirements mapping)",
      "Application batching system (50 apps/week)",
      "Interview scheduling & prep tracker",
    ],
    trackSpecific: ["Tech: Stack-specific company targeting", "Finance: CFA/FRM relevant firm lists", "Sales: Quota attainment research method"],
  },
  "04": {
    files: [
      "200 interview questions with answer frameworks",
      "Behavioural: STAR workbook (30 scenarios)",
      "HR questions: Culture fit & salary scripts",
      "Technical: Role-specific question banks (6 tracks)",
      "Mock interview scenarios (video + evaluation)",
      "Interview evaluation scorecards (self + peer)",
      "Follow-up email templates (post-interview)",
      "Panel/group interview strategies",
    ],
    trackSpecific: ["Tech: System design cheat sheet", "PM: Product sense frameworks (CIRCLES)", "BA: SQL/requirements elicitation questions"],
  },
  "05": {
    files: [
      "Negotiation scripts (phone + email + in-person)",
      "CTC vs take-home calculator (Excel, FY24-25 tax)",
      "Offer comparison spreadsheet (total rewards view)",
      "Counteroffer decision framework (money vs growth)",
      "Resignation communication templates",
      "Notice period negotiation guide",
      "Equity/ESOP evaluation checklist",
      "Relocation & joining bonus scripts",
    ],
    trackSpecific: ["Tech: RSU/ESOP valuation models", "Sales: Variable pay negotiation", "Finance: Bonus structure analysis"],
  },
  "06": {
    files: [
      "100 tested ChatGPT/Claude prompts (categorised)",
      "Resume improvement workflow (JD → tailored resume)",
      "JD matching & gap analysis prompt chain",
      "Interview practice simulator (role-specific)",
      "Recruiter communication automation",
      "Career research workflows (company + role)",
      "LinkedIn content generation prompts",
      "Salary benchmarking prompt templates",
    ],
    trackSpecific: ["Tech: LeetCode explanation prompts", "PM: PRD generation from rough notes", "BA: User story writing from requirements"],
  },
  "07": {
    files: [
      "Career assessment diagnostic (skills + values + goals)",
      "Skills-gap analysis matrix (current vs target role)",
      "30/60/90-day roadmap template",
      "Weekly milestone tracker (Notion + Excel)",
      "Progress dashboard (applications, interviews, skills)",
      "Application planning calendar (seasonal hiring)",
      "Interview prep scheduling system",
      "Pivot vs progress decision framework",
    ],
    trackSpecific: ["Tech: DSA/System design prep calendar", "PM: Portfolio building sprint plan", "Finance: Certification timeline (CFA/FRM)"],
  },
  "08": {
    files: [
      "Portfolio & project presentation templates",
      "Professional communication frameworks (email/Slack/meetings)",
      "Networking frameworks (cold → warm → referral)",
      "Skills development roadmap (quarterly)",
      "Role-transition planning (IC → Lead → Manager)",
      "First 90 days in new job success plan",
      "Performance review preparation kit",
      "Personal board of advisors template",
    ],
    trackSpecific: ["Tech: Staff+ engineer archetype guide", "PM: Product leadership competency map", "Ops: Process improvement portfolio"],
  },
};

export function ModuleCard({ number, title, description, files, trackSpecific, icon }: ModuleCardProps) {
  const details = moduleDetails[number] || { files: [], trackSpecific: [] };
  const allFiles = [...(files || []), ...(details.files || [])];
  const allTracks = [...(trackSpecific || []), ...(details.trackSpecific || [])];
  const isOpen = false; // We'll handle with CSS-only or simple state

  return (
    <div className="group bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 hover:border-white/20 transition-all duration-300 relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-br from-blue-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
      <div className="relative flex gap-4">
        <div className="w-12 h-12 bg-gradient-to-br from-blue-500/20 to-indigo-500/20 rounded-xl flex items-center justify-center flex-shrink-0 group-hover:from-blue-500/40 group-hover:to-indigo-500/40 transition-all">
          {icon}
        </div>
        <div className="flex-1 min-w-0">
          <div className="flex items-start justify-between gap-4">
            <div>
              <span className="text-blue-400 text-sm font-semibold">Module {number}</span>
              <h3 className="text-xl font-bold mt-1 text-white">{title}</h3>
            </div>
            <svg className="w-5 h-5 text-white/40 group-hover:text-blue-400 transition-colors flex-shrink-0 mt-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </div>
          <p className="text-white/60 text-sm mt-2 line-clamp-2">{description}</p>
          
          {/* File preview */}
          <div className="mt-4 pt-4 border-t border-white/10">
            <p className="text-xs text-white/40 mb-2">Includes {allFiles.length} files & templates:</p>
            <ul className="space-y-1 max-h-40 overflow-hidden">
              {allFiles.slice(0, 4).map((file, i) => (
                <li key={i} className="flex items-center gap-2 text-white/50 text-xs">
                  <svg className="w-3.5 h-3.5 text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                  <span className="truncate">{file}</span>
                </li>
              ))}
              {allFiles.length > 4 && (
                <li className="flex items-center gap-2 text-blue-400 text-xs font-medium cursor-pointer hover:underline">
                  <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                  </svg>
                  +{allFiles.length - 4} more files
                </li>
              )}
            </ul>
          </div>

          {/* Track-specific */}
          {allTracks.length > 0 && (
            <div className="mt-3 pt-3 border-t border-white/10">
              <p className="text-xs text-white/40 mb-2">Track-specific bonuses:</p>
              <div className="flex flex-wrap gap-1.5">
                {allTracks.slice(0, 3).map((track, i) => (
                  <span key={i} className="bg-blue-500/10 text-blue-300 text-xs px-2 py-0.5 rounded-full">
                    {track}
                  </span>
                ))}
                {allTracks.length > 3 && (
                  <span className="bg-white/10 text-white/50 text-xs px-2 py-0.5 rounded-full">
                    +{allTracks.length - 3} more
                  </span>
                )}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}