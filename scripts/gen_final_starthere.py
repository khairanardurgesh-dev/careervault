import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch

OUT = r'C:\Users\Quick\Desktop\CareerVault\output'
NAVY = colors.HexColor('#1F3864'); BLUE=colors.HexColor('#2E5C8A'); GREY=colors.HexColor('#595959')
styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=20, textColor=NAVY, spaceAfter=12)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=14, textColor=BLUE, spaceAfter=6, spaceBefore=12)
BODY = ParagraphStyle('BODY', parent=styles['BodyText'], fontSize=10.5, leading=14, spaceAfter=6)
BULLET = ParagraphStyle('BULLET', parent=styles['BodyText'], fontSize=10.5, leading=14, leftIndent=16, spaceAfter=3)

def pdf(path, title, sections):
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=0.8*inch, rightMargin=0.8*inch, topMargin=0.7*inch, bottomMargin=0.7*inch)
    story=[Paragraph(title,H1), Paragraph('CareerVault Complete Job Switch System — Customer Onboarding Guide', ParagraphStyle('sub',parent=BODY,italic=True,fontSize=9,textColor=GREY)), Spacer(1,12)]
    for t,paras in sections:
        story.append(Paragraph(t,H2))
        for p in paras:
            if p.startswith('BULLET:'): story.append(Paragraph('• '+p[7:],BULLET))
            else: story.append(Paragraph(p,BODY))
        story.append(Spacer(1,6))
    doc.build(story); print('saved',path)

sections = [
 ('Welcome', [
  'CareerVault is a complete, self-guided career transition system for Indian working professionals.',
  'You have purchased the CareerVault Complete Job Switch System — a one-time digital product.',
  'This product helps you: define your career direction, build a stronger resume, optimise your professional profile, organise your job search, prepare for interviews, evaluate and negotiate offers, execute a structured 90-day plan, and continue long-term career advancement.',
  'This product does NOT guarantee a job, salary increase, recruiter responses, interviews, or placement. It is a toolkit — your outcomes depend on your effort, the market, and employer decisions.',
 ]),
 ('What You Received — Eight Modules', [
  'Module 01 — Resume Mastery System: 15 templates, 6 career-track guides, handbook, achievement workbook, summary library, matching worksheet, scorecard, checklists, before/after examples.',
  'Module 02 — Professional Profile Optimisation: Handbook, headline library (72), About section library (36), 12 LinkedIn templates, profile audit workbook, positioning workbook, networking messages (60), networking tracker, content toolkit (30 frameworks), 30-day plan, review checklist.',
  'Module 03 — Job Search Operating System: Handbook, platform directory, company research workbook, JD analysis toolkit, application tracker (XLSX), strategy planner, recruiter messages (72), weekly planner, scam prevention guide, screening prep (30 questions), performance review workbook, 6 career-track guides.',
  'Module 04 — Interview Preparation Vault: 200+ interview questions across 6 tracks, STAR workbook, mock scorecard, planner, self-assessment, day checklist, handbook, question library PDF.',
  'Module 05 — Salary & Offer Negotiation: Handbook (16 chapters), compensation structure guide, research guide, negotiation messages (72), expectation workbook, offer comparison calculator, CTC explainer, offer checklist (60+), strategy planner, benefits comparison, practice workbook (20 scenarios), decision framework, 6 career-track guides.',
  'Module 06 — AI Career Assistant Toolkit: Handbook (16 chapters), master prompt library (120), 6 track-specific libraries (90), prompt engineering workbook, 6 AI toolkits (resume, interview, job search, communication, salary, development), 6 workflow playbooks, fact-checking guide, privacy guide, tool directory, quick reference.',
  'Module 07 — 90-Day Job Switch Programme: Handbook (16 chapters), daily action calendar (90 days), weekly planner, dashboard, readiness assessment, target role workbook, skills gap planner, performance review, interview improvement, decision journal, Day 30/60/90 reviews, contingency playbook, 6 career-track guides, 3 workload pathways, 3 starting-point pathways.',
  'Module 08 — Career Advancement Toolkit: Handbook (18 chapters), growth strategy workbook, professional impact tracker, promotion readiness assessment, promotion prep workbook, communication library (60+), leadership workbook, first-time manager toolkit, skills planner, internal mobility guide, portfolio builder, reputation checklist, stagnation playbook, 12-month roadmap, quarterly/annual reviews, 6 career-track guides, 3 career pathways.',
 ]),
 ('Six Career Tracks', [
  'All modules cover these six CareerVault tracks: Technology & IT, Business Analysis, Product & Project Management, Finance, Sales & Marketing, Management & Operations.',
  'Select the track(s) relevant to your target roles. You may use multiple tracks.',
 ]),
 ('File Formats & How to Use Them', [
  'PDF — Guides, handbooks, checklists, libraries. Read on any device, print if needed.',
  'DOCX — Editable templates and workbooks. Open in Microsoft Word or Google Docs. Replace placeholder text (shown in brackets or grey italics) with your own information.',
  'XLSX — Interactive workbooks with formulas. Open in Excel or Google Sheets. Enter your data in input cells; calculated fields update automatically.',
 ]),
 ('Recommended Usage Sequence', [
  '1. Define career direction (Module 07 readiness assessment, Module 08 growth strategy).',
  '2. Improve resume (Module 01 templates, handbook, achievement workbook).',
  '3. Improve professional profile (Module 02 templates, headline/About libraries).',
  '4. Organise job search (Module 03 platform directory, company research, application tracker).',
  '5. Prepare for interviews (Module 04 questions, Module 06 AI interview toolkit).',
  '6. Evaluate and negotiate offers (Module 05 calculator, negotiation messages, CTC explainer).',
  '7. Execute 90-day plan (Module 07 daily calendar, weekly planner, reviews).',
  '8. Continue career advancement (Module 08 impact tracker, promotion prep, 12-month roadmap).',
  'Already applying? Skip to step 4. Already interviewing? Focus on steps 5-6.',
 ]),
 ('Usage Plans', [
  'Path A — Limited Time (~30 min/day): Focus on one daily action from Module 07 calendar. Prioritise resume, profile, and 1-2 applications per week.',
  'Path B — Standard (~60 min/day): Complete daily action + interview prep or networking. 3-5 applications per week.',
  'Path C — Intensive (~90-120 min/day): Full daily action + deep interview practice + skills development + networking. 5+ applications per week.',
  'More hours do not guarantee better outcomes. Consistency and quality matter more.',
 ]),
 ('Customer Portal & Downloads', [
  'Access your purchased product at the CareerVault customer portal after payment verification.',
  'Portal provides: complete ZIP download, individual module downloads, purchase history, entitlement status.',
  'Download links are short-lived signed URLs. If a link expires, return to the portal to generate a fresh one.',
  'All modules are also available as individual downloads if you prefer not to download the complete ZIP.',
 ]),
 ('Support', [
  'For technical issues with downloads or account access, contact support at the verified support email provided in your purchase confirmation.',
  'For product questions, refer to the module handbooks and START_HERE guides within each module.',
 ]),
 ('Limitations', [
  'No guaranteed job, interviews, recruiter responses, or salary increase.',
  'No direct recruiter access or placement service.',
  'No personal coaching unless separately offered.',
  'Content is educational — verify all financial, legal, and contractual information independently.',
  'AI-generated content (Module 06) must be reviewed and verified by you before use.',
 ]),
 ('Licence', [
  'Personal use only within the CareerVault bundle. See LICENCE/PERSONAL_USE_LICENCE.pdf.',
  'Do not redistribute templates or workbooks as standalone paid products.',
 ]),
 ('Product Version', [
  'CareerVault Complete Job Switch System v1.0.0',
  'Release date: November 24, 2026',
 ])
]

pdf(os.path.join(OUT, 'CAREERVAULT_START_HERE.pdf'), 'CAREERVAULT START HERE', sections)
print('START_HERE.pdf created')