import Link from "next/link";
import { Button } from "@/components/shared/button";

export default function AccountLibraryPage() {
  return (
    <main className="min-h-screen bg-navy-900 text-white">
      <section className="px-4 py-12">
        <div className="max-w-6xl mx-auto">
          <div className="flex items-center justify-between mb-8">
            <div>
              <h1 className="text-3xl font-bold mb-2">CareerVault Library</h1>
              <p className="text-white/60">Purchased on: [Date]</p>
              <p className="text-white/60">Version: [Version]</p>
            </div>
            <Button asChild>
              <Link href="/account/settings" className="text-primary">
                <span>Account Settings</span>
              </Link>
            </Button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {/* Module cards */}
            <div className="group bg-white/5 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">01 Resume Mastery</h3>
              <p className="text-white/60 text-sm">Editable templates & ATS handbook</p>
              <Button asChild>
                <Link href="/account/download/01" className="text-primary mt-3 small">
                  <span>Download</span>
                </Link>
              </Button>
            </div>
            <div className="group bg-white/5 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">02 Professional Profile</h3>
              <p className="text-white/60 text-sm">LinkedIn & Naukri guides</p>
              <Button asChild>
                <Link href="/account/download/02" className="text-primary mt-3 small">
                  <span>Download</span>
                </Link>
              </Button>
            </div>
            <div className="group bg-white/5 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">03 Job Search System</h3>
              <p className="text-white/60 text-sm">Excel tracker & worksheets</p>
              <Button asChild>
                <Link href="/account/download/03" className="text-primary mt-3 small">
                  <span>Download</span>
                </Link>
              </Button>
            </div>
            <div className="group bg-white/5 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">04 Interview Preparation</h3>
              <p className="text-white/60 text-sm">Questions & frameworks</p>
              <Button asChild>
                <Link href="/account/download/04" className="text-primary mt-3 small">
                  <span>Download</span>
                </Link>
              </Button>
            </div>
            <div className="group bg-white/5 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">05 Salary & Negotiation</h3>
              <p className="text-white/60 text-sm">Calculator & scripts</p>
              <Button asChild>
                <Link href="/account/download/05" className="text-primary mt-3 small">
                  <span>Download</span>
                </Link>
              </Button>
            </div>
            <div className="group bg-white/5 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">06 AI Career Assistant</h3>
              <p className="text-white/60 text-sm">Prompt library</p>
              <Button asChild>
                <Link href="/account/download/06" className="text-primary mt-3 small">
                  <span>Download</span>
                </Link>
              </Button>
            </div>
            <div className="group bg-white/5 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">07 90-Day Programme</h3>
              <p className="text-white/60 text-sm">Roadmap & milestones</p>
              <Button asChild>
                <Link href="/account/download/07" className="text-primary mt-3 small">
                  <span>Download</span>
                </Link>
              </Button>
            </div>
            <div className="group bg-white/5 rounded-xl p-6 hover:bg-white/10 transition-colors">
              <h3 className="text-xl font-bold mb-2">08 Career Advancement</h3>
              <p className="text-white/60 text-sm">Portfolio & transition guide</p>
              <Button asChild>
                <Link href="/account/download/08" className="text-primary mt-3 small">
                  <span>Download</span>
                </Link>
              </Button>
            </div>
          </div>

          <div className="mt-12">
            <Button asChild>
              <Link href="/account/download-zip" className="w-full justify-center">
                <span>Download Complete ZIP Package</span>
              </Link>
            </Button>
          </div>
        </div>
      </section>
    </main>
  );
}