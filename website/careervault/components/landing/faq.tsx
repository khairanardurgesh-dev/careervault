"use client";

import { useState } from "react";

const faqs = [
  {
    q: "Is this a course or a downloadable toolkit?",
    a: "This is a downloadable toolkit — not a video course. You get 8 modules as editable files (Word, Excel, Notion, PDF, Markdown) that you own forever. No videos to watch, no login to a platform. Download once, use anytime. This is intentional: Indian professionals prefer actionable templates over passive learning.",
  },
  {
    q: "Which career tracks are covered?",
    a: "Six tracks: Technology & IT, Business Analysis, Product & Project Management, Finance, Sales & Marketing, and Management & Operations. Each module has track-specific bonuses (e.g., Tech gets system design cheat sheet, PM gets CIRCLES framework, Finance gets CTC calculator with FY24-25 tax).",
  },
  {
    q: "What file formats are included?",
    a: "Word (.docx) for resumes/letters, Excel (.xlsx) for trackers/calculators, Notion templates (duplicate links), PDF for guides/frameworks, Markdown for prompt libraries. All editable. No proprietary formats.",
  },
  {
    q: "Is there a refund policy?",
    a: "Yes — 7-day no-questions-asked refund. If you don't find value, email us within 7 days of purchase for a full refund. We trust Indian professionals — this isn't a 'course' with hidden upsells. The toolkit speaks for itself.",
  },
  {
    q: "Do I get updates?",
    a: "Yes — lifetime access includes all future updates. When we add new templates, update tax calculators for new FY, or add interview questions, you get them free. No subscription, no renewal fees.",
  },
  {
    q: "Can I use this if I have 0 years experience (fresher)?",
    a: "CareerVault is designed for 1-5 years experience. Freshers may find some modules advanced (negotiation, role transition). However, Modules 1, 2, 3, 4, 6 are highly relevant for freshers too. We recommend 6+ months work experience for maximum ROI.",
  },
  {
    q: "How is this different from ₹20,000+ courses?",
    a: "Courses sell information. CareerVault sells implementation. You get the exact templates, frameworks, and trackers used by professionals who switched to Amazon, Flipkart, HDFC, Salesforce, Swiggy, Zomato. No fluff, no 50-hour videos. Download → Customise → Apply.",
  },
  {
    q: "Is GST invoice provided?",
    a: "Yes — automatic GST invoice generated on purchase (via Razorpay). You can claim input credit if your employer reimburses learning expenses. Company name/GSTIN captured at checkout.",
  },
  {
    q: "What if I need help using the templates?",
    a: "Email support included (support@careervault.in). Typical response: <24 hours on weekdays. We also include 'how-to' guides inside each module. The toolkit is self-explanatory — most users need zero support.",
  },
  {
    q: "Can I share this with my friends/colleagues?",
    a: "Licence is per individual. Sharing login/download links violates terms. However, we offer team discounts (5+ licences) — email us for bulk pricing. Your purchase supports future updates for everyone.",
  },
];

export function FAQ() {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  return (
    <section className="py-20 lg:py-28 bg-navy-900" aria-label="FAQ">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">Questions? We've Got Answers</h2>
          <p className="text-white/60 max-w-2xl mx-auto">Everything you need to know before investing in your career switch</p>
        </div>

        <div className="max-w-3xl mx-auto space-y-4">
          {faqs.map((faq, index) => (
            <details
              key={index}
              className="group bg-white/5 border border-white/10 rounded-xl overflow-hidden transition-all"
              open={openIndex === index}
              onToggle={() => setOpenIndex(openIndex === index ? null : index)}
            >
              <summary className="flex items-center justify-between p-6 cursor-pointer list-none">
                <h3 className="text-white font-semibold text-lg pr-8">{faq.q}</h3>
                <svg
                  className={`w-5 h-5 text-white/50 transition-transform duration-200 flex-shrink-0 ${
                    openIndex === index ? "rotate-180" : ""
                  }`}
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </summary>
              <div className="px-6 pb-6 text-white/70 leading-relaxed animate-slide-down">
                {faq.a}
              </div>
            </details>
          ))}
        </div>
      </div>
    </section>
  );
}