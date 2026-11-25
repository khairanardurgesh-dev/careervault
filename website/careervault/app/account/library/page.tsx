"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { Button } from "@/components/shared/button";

const modules = [
  { id: "01", title: "Resume Mastery System", desc: "15 ATS‑optimised .docx templates + 8 role‑specific handbooks + achievement workbooks + interview examples + checklists", icon: "📄" },
  { id: "02", title: "Professional Profile Optimisation", desc: "12 editable .docx profiles + LinkedIn About/Headline libraries + profiling workbook + networking tracker", icon: "👤" },
  { id: "03", title: "Job Search Operating System", desc: "Excel tracker + company research workbook + JD analysis + recruiter outreach + scam prevention + 6 track‑specific guides", icon: "📊" },
  { id: "04", title: "Interview Preparation Vault", desc: "200+ commercial interview questions + STAR workbook + planner + self‑assessment + scorecard + mock interview scenarios", icon: "🎯" },
  { id: "05", title: "Salary & Offer Negotiation", desc: "CTC calculator (FY24‑25) + negotiation scripts + offer comparison workbook + 6 track‑specific salary guides", icon: "💰" },
  { id: "06", title: "AI Career Assistant Toolkit", desc: "Master prompt library + 6 track‑specific prompt collections + prompt engineering workbook + 6 toolkits + 6 playbooks + quality‑safety guide", icon: "🤖" },
  { id: "07", title: "90‑Day Job Switch Programme", desc: "Handbook + 3 assessments (readiness, skills‑gap, target role) + 7 track‑specific guides + daily/weekly calendars + review templates + decision journal + performance trackers", icon: "📅" },
  { id: "08", title: "Career Advancement Toolkit", desc: "Advancement handbook + 12‑month roadmap + recovery playbook + 6 track‑specific guides + integration map + leadership workbook + impact tracker + portfolio templates + reputation checklist + strategy planner", icon: "🚀" },
];

export default function AccountLibraryPage() {
  const [downloading, setDownloading] = useState<string | null>(null);
  const [zipDownloading, setZipDownloading] = useState(false);

  const handleDownload = async (moduleId: string) => {
    setDownloading(moduleId);
    try {
      const response = await fetch(`/api/download/${moduleId}`);
      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `CareerVault_Module_${moduleId}.zip`;
        a.click();
        window.URL.revokeObjectURL(url);
      }
    } catch (error) {
      console.error("Download failed:", error);
    } finally {
      setDownloading(null);
    }
  };

  const handleZipDownload = async () => {
    setZipDownloading(true);
    try {
      const response = await fetch("/api/download/complete");
      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "CareerVault_Complete_Job_Switch_System.zip";
        a.click();
        window.URL.revokeObjectURL(url);
      }
    } catch (error) {
      console.error("ZIP download failed:", error);
    } finally {
      setZipDownloading(false);
    }
  };

  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="section">
        <div className="container">
          <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-6 mb-12">
            <div>
              <Link href="/" className="inline-flex items-center gap-2 mb-6">
                <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-xl flex items-center justify-center">
                  <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                  </svg>
                </div>
                <span className="text-2xl font-bold text-white">CareerVault</span>
              </Link>
              <h1 className="text-3xl md:text-4xl font-bold mb-2">Your Library</h1>
              <p className="text-white/60">8 modules • 389 files • Lifetime access • Version 1.0.0</p>
            </div>
            <Link href="/account/settings">
              <Button variant="outline">Account Settings</Button>
            </Link>
          </div>

          {/* Complete ZIP Download */}
          <div className="bg-gradient-to-r from-blue-500/10 to-indigo-500/10 border border-blue-500/20 rounded-2xl p-6 md:p-8 mb-12">
            <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-6">
              <div className="flex items-center gap-4">
                <div className="w-16 h-16 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center text-3xl">
                  📦
                </div>
                <div>
                  <h3 className="text-xl font-bold text-white">Complete CareerVault Package</h3>
                  <p className="text-white/70">All 8 modules, 6 career tracks, 389 files in one ZIP (2.49 MB)</p>
                </div>
              </div>
              <Button 
                onClick={handleZipDownload} 
                disabled={zipDownloading}
                className="w-full md:w-auto bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-semibold px-8 py-3"
              >
                {zipDownloading ? (
                  <>
                    <svg className="animate-spin -ml-1 mr-2 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                    </svg>
                    Downloading ZIP...
                  </>
                ) : (
                  <>
                    <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                    </svg>
                    Download Complete ZIP (2.49 MB)
                  </>
                )}
              </Button>
            </div>
          </div>

          {/* Module Cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {modules.map((module) => (
              <div
                key={module.id}
                className="card-elevated group relative overflow-hidden"
              >
                <div className="absolute top-4 right-4 text-3xl">{module.icon}</div>
                <div className="mb-4">
                  <span className="text-blue-400 text-sm font-semibold">Module {module.id}</span>
                  <h3 className="text-xl font-bold mt-1 text-white">{module.title}</h3>
                </div>
                <p className="text-white/60 text-sm mb-4">{module.desc}</p>
                <div className="flex items-center justify-between text-white/50 text-sm mb-6">
                  <span>{module.id} files</span>
                  <span className="text-blue-400 font-medium">Ready to download</span>
                </div>
                <Button
                  onClick={() => handleDownload(module.id)}
                  disabled={downloading === module.id}
                  className="w-full"
                  variant={downloading === module.id ? "outline" : "primary"}
                >
                  {downloading === module.id ? (
                    <>
                      <svg className="animate-spin -ml-1 mr-2 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                      </svg>
                      Downloading...
                    </>
                  ) : (
                    <>
                      <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                      </svg>
                      Download Module {module.id}
                    </>
                  )}
                </Button>
              </div>
            ))}
          </div>

          {/* Quick Stats */}
          <div className="mt-16 grid grid-cols-2 md:grid-cols-4 gap-6">
            <div className="card text-center">
              <div className="text-3xl font-bold gradient-text">389</div>
              <div className="text-white/60 text-sm">Total Files</div>
            </div>
            <div className="card text-center">
              <div className="text-3xl font-bold gradient-text">8</div>
              <div className="text-white/60 text-sm">Modules</div>
            </div>
            <div className="card text-center">
              <div className="text-3xl font-bold gradient-text">6</div>
              <div className="text-white/60 text-sm">Career Tracks</div>
            </div>
            <div className="card text-center">
              <div className="text-3xl font-bold gradient-text">∞</div>
              <div className="text-white/60 text-sm">Lifetime Access</div>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}