import os, sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\resume-mastery-system\03_Workbooks'
NAVY = RGBColor(0x1F,0x38,0x64); BLUE=RGBColor(0x2E,0x5C,0x8A); GREY=RGBColor(0x59,0x59,0x59)

doc = Document()
st = doc.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(10.5)
for s in doc.sections:
    s.top_margin=Inches(0.7); s.bottom_margin=Inches(0.7); s.left_margin=Inches(0.8); s.right_margin=Inches(0.8)

def h1(t): 
    p=doc.add_paragraph(); r=p.add_run(t); r.bold=True; r.font.size=Pt(18); r.font.color.rgb=NAVY; p.paragraph_format.space_after=Pt(6)
def h2(t):
    p=doc.add_paragraph(); r=p.add_run(t); r.bold=True; r.font.size=Pt(13); r.font.color.rgb=BLUE; p.paragraph_format.space_before=Pt(10); p.paragraph_format.space_after=Pt(4)
def para(t, italic=False, size=10.5):
    p=doc.add_paragraph(); r=p.add_run(t); r.italic=italic; r.font.size=Pt(size); p.paragraph_format.space_after=Pt(4)
def bullet(t):
    p=doc.add_paragraph(style='List Bullet'); r=p.add_run(t); r.font.size=Pt(10.5); p.paragraph_format.space_after=Pt(2)
def table(headers, rows, widths):
    t=doc.add_table(rows=1, cols=len(headers)); t.style='Table Grid'
    hdr=t.rows[0].cells
    for i,h in enumerate(headers):
        hdr[i].text=''
        r=hdr[i].paragraphs[0].add_run(h); r.bold=True; r.font.size=Pt(9.5)
    for row in rows:
        cells=t.add_row().cells
        for i,v in enumerate(row):
            cells[i].text=''
            r=cells[i].paragraphs[0].add_run(str(v)); r.font.size=Pt(9.5)
    for r_ in t.rows:
        for i,w in enumerate(widths):
            r_.cells[i].width=Inches(w)

h1('Achievement Writing Workbook')
para('CareerVault Resume Mastery System. Editable worksheets. Fictional illustrative examples — do not copy as personal achievements.', italic=True, size=9)

h2('1. Responsibility-to-Achievement Transformation')
para('List a responsibility, then rewrite it as an achievement using Action + Context + Method + Outcome.')
table(['Responsibility','Action','Context','Method','Outcome (verified)'], [
 ['Managed reports','Prepared','monthly MIS for leadership','automated data pulls','reduced cycle time by X days (if verified)'],
 ['Fixed bugs','Resolved','production defects','root-cause analysis','reduced customer-reported issues'],
], [1.4,0.9,1.6,1.4,1.8])

h2('2. Action Verb Selection')
para('Choose a precise verb. Avoid "responsible for".')
bullet('Built, designed, implemented, developed (creation)')
bullet('Improved, optimised, streamlined, reduced (improvement)')
bullet('Led, coordinated, facilitated, mentored (leadership)')
bullet('Analysed, evaluated, researched, assessed (analysis)')

h2('3. Context and Challenge Identification')
para('Answer: What was the situation? Who was affected? What constraints existed?')

h2('4. Method and Contribution Description')
para('Describe your specific approach and tools, not team activity.')

h2('5. Outcome Identification')
para('What changed? For whom? By how much (only if verified)?')

h2('6. Quantification When Evidence Exists')
para('Use numbers only from reliable sources: monitoring, reports, or verified records. Never invent percentages, revenue, or savings.')

h2('7. Achievement Verification')
para('Can you produce evidence if asked in an interview? If not, rephrase as scope/quality.')

h2('8. Rewriting Generic Bullet Points')
para('At least 30 before-and-after examples across all six career tracks.')

examples = [
 ('Technology & IT','Before: Worked on API development.','After: Designed and implemented REST APIs for order management supporting daily transaction volume.','Why stronger: specifies scope, action, and outcome.'),
 ('Technology & IT','Before: Fixed bugs.','After: Resolved production defects through root-cause analysis, reducing customer-reported issues.','Why stronger: method and outcome stated.'),
 ('Technology & IT','Before: Did testing.','After: Authored automated test suites covering core flows, improving release confidence.','Why stronger: contribution and value.'),
 ('Business Analysis','Before: Gathered requirements.','After: Elicited requirements from multiple stakeholders and documented functional specifications.','Why stronger: scope and deliverable.'),
 ('Business Analysis','Before: Made reports.','After: Built weekly KPI dashboards used by leadership for operational decisions.','Why stronger: audience and use.'),
 ('Business Analysis','Before: Analysed data.','After: Analysed sales data to identify trends and inform pricing discussions.','Why stronger: purpose and application.'),
 ('Product & PM','Before: Managed project.','After: Led delivery of customer portal with engineering team, meeting timeline and scope.','Why stronger: scale and outcome.'),
 ('Product & PM','Before: Prioritised backlog.','After: Prioritised backlog using customer feedback and usage data.','Why stronger: method and rationale.'),
 ('Product & PM','Before: Coordinated team.','After: Facilitated sprint ceremonies and removed blockers for cross-functional team.','Why stronger: specific activities.'),
 ('Finance','Before: Prepared reports.','After: Prepared monthly MIS reports for leadership within agreed timelines.','Why stronger: cadence and audience.'),
 ('Finance','Before: Did reconciliation.','After: Reconciled accounts monthly with documented accuracy checks.','Why stronger: frequency and quality.'),
 ('Finance','Before: Handled audit.','After: Supported internal audit by preparing schedules and responding to queries.','Why stronger: specific contribution.'),
 ('Sales & Marketing','Before: Handled sales.','After: Managed account portfolio and achieved agreed quarterly targets.','Why stronger: scope and result framing.'),
 ('Sales & Marketing','Before: Ran campaigns.','After: Executed digital campaigns and tracked lead generation metrics.','Why stronger: activity and measurement.'),
 ('Sales & Marketing','Before: Did marketing.','After: Created content and managed social channels supporting brand awareness.','Why stronger: concrete activities.'),
 ('Management & Ops','Before: Managed team.','After: Led team across shifts, coordinating schedules and performance reviews.','Why stronger: scope and activities.'),
 ('Management & Ops','Before: Improved process.','After: Redesigned workflow to reduce turnaround time (verified).','Why stronger: method and measurable outcome.'),
 ('Management & Ops','Before: Handled vendors.','After: Managed vendor relationships, tracking SLAs and resolving issues.','Why stronger: specific responsibilities.'),
]
# repeat to reach 30 with variations
more = [
 ('Technology & IT','Before: Wrote code.','After: Developed features in Python/Java following code review and testing standards.','Why stronger: standards and quality.'),
 ('Technology & IT','Before: Deployed app.','After: Deployed application updates using CI/CD pipelines with rollback plans.','Why stronger: method and reliability.'),
 ('Technology & IT','Before: Worked with database.','After: Designed database schema and optimised queries for reporting.','Why stronger: design and optimisation.'),
 ('Business Analysis','Before: Talked to clients.','After: Conducted stakeholder interviews to capture business needs.','Why stronger: method and purpose.'),
 ('Business Analysis','Before: Documented process.','After: Created process maps identifying bottlenecks and improvement areas.','Why stronger: analytical value.'),
 ('Business Analysis','Before: Supported testing.','After: Coordinated UAT, tracking defects and sign-off.','Why stronger: ownership.'),
 ('Product & PM','Before: Wrote user stories.','After: Wrote and refined user stories with acceptance criteria.','Why stronger: quality detail.'),
 ('Product & PM','Before: Did research.','After: Conducted user research and synthesised findings into roadmap inputs.','Why stronger: application.'),
 ('Product & PM','Before: Tracked metrics.','After: Defined and tracked product metrics for feature adoption.','Why stronger: specificity.'),
 ('Finance','Before: Did budgeting.','After: Prepared annual budget and tracked variance monthly.','Why stronger: cadence and ownership.'),
 ('Finance','Before: Calculated tax.','After: Computed tax provisions and supported compliance filings.','Why stronger: accuracy and support.'),
 ('Finance','Before: Used Excel.','After: Built financial models in Excel with documented assumptions.','Why stronger: deliverable and rigour.'),
]
all_ex = examples + more
for track, before, after, why in all_ex:
    h2(f'{track}')
    para(before, italic=True, size=9.5)
    para(after, size=9.5)
    para(why, italic=True, size=9)

doc.save(os.path.join(OUT, 'Achievement_Writing_Workbook.docx'))
print('saved workbook')
