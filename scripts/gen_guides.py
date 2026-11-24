import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, ListFlowable, ListItem
from reportlab.lib.units import inch

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\resume-mastery-system\02_Handbooks'
NAVY = colors.HexColor('#1F3864')
BLUE = colors.HexColor('#2E5C8A')
GREY = colors.HexColor('#595959')

styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=18, textColor=NAVY, spaceAfter=10, spaceBefore=6)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=14, textColor=BLUE, spaceAfter=6, spaceBefore=12)
BODY = ParagraphStyle('BODY', parent=styles['BodyText'], fontSize=10.5, leading=14, spaceAfter=6)
BULLET = ParagraphStyle('BULLET', parent=styles['BodyText'], fontSize=10.5, leading=14, leftIndent=16, spaceAfter=3, bulletIndent=6)

def make_guide(filename, track, content_sections):
    path = os.path.join(OUT, filename)
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=0.8*inch, rightMargin=0.8*inch, topMargin=0.7*inch, bottomMargin=0.7*inch)
    story = []
    story.append(Paragraph(f'{track} Resume Guide', H1))
    story.append(Paragraph('CareerVault Resume Mastery System — Fictional educational content. Adapt to your own experience.', ParagraphStyle('sub', parent=BODY, italic=True, fontSize=9, textColor=GREY)))
    story.append(Spacer(1,12))
    for sec_title, paras in content_sections:
        story.append(Paragraph(sec_title, H2))
        for p in paras:
            if p.startswith('BULLET:'):
                story.append(Paragraph('• ' + p[7:], BULLET))
            else:
                story.append(Paragraph(p, BODY))
        story.append(Spacer(1,6))
    doc.build(story)
    print('saved', path)

# Content for each track
tracks = {
 'Technology_IT_Resume_Guide.pdf': ('Technology & IT', [
  ('Relevant Resume Sections', [
   'Contact information with professional email and LinkedIn profile.',
   'Professional summary tailored to the target role.',
   'Core technical skills grouped logically.',
   'Professional experience with measurable outcomes.',
   'Projects showcasing technical depth.',
   'Education and relevant certifications.',
   'BULLET:Optional sections: open-source contributions, publications, patents.',
  ]),
  ('Recommended Section Ordering', [
   'For 1-3 years: Summary, Skills, Experience, Projects, Education, Certifications.',
   'For 3-5 years: Summary, Experience, Skills, Projects, Education, Certifications.',
   'Place the section that best supports the target role first.',
  ]),
  ('Skills and Competencies', [
   'Programming languages, frameworks, and libraries relevant to the role.',
   'System design, debugging, testing, and code review practices.',
   'Cloud platforms, DevOps tools, and data stores.',
   'BULLET:Soft skills: cross-functional collaboration, technical communication, mentoring.',
  ]),
  ('Describing Responsibilities', [
   'Describe what you built, maintained, or improved and for whom.',
   'Mention scale: users, requests, data volume, or service criticality.',
   'Avoid listing tools without context.',
  ]),
  ('Measurable Achievements', [
   'Quantify when you have reliable data: latency reduction, error-rate drop, cost savings.',
   'When data is unavailable, describe scope, complexity, and ownership.',
   'BULLET:Example: "Reduced API response time by refactoring query patterns (verified via monitoring)."',
  ]),
  ('Tools and Technologies', [
   'List only technologies you can discuss confidently in an interview.',
   'Group by category: languages, frameworks, infrastructure, testing.',
  ]),
  ('Project Descriptions', [
   'Include problem, approach, technologies, and outcome.',
   'State your specific contribution in team projects.',
  ]),
  ('Common Mistakes', [
   'Listing every technology ever touched.',
   'Vague bullets like "worked on backend".',
   'Missing links to portfolio or GitHub where relevant.',
   'Inconsistent date formats.',
  ]),
  ('Customising for Job Descriptions', [
   'Map required skills to your experience bullets.',
   'Reorder skills to match the posting.',
   'Adjust summary to mirror role language without copying.',
  ]),
  ('Before-and-After Bullets', [
   'Before: "Worked on API development." After: "Designed and implemented REST APIs for order management, supporting 10k daily requests."',
   'Before: "Fixed bugs." After: "Resolved 30+ production defects, reducing customer-reported issues by a measurable margin."',
  ]),
  ('Role-Specific Example', [
   'Fictional example: Software Engineer with 3 years building web services, strong in Python and cloud deployment, seeking senior backend roles.',
  ]),
  ('Experience-Level Guidance', [
   'Entry-level: emphasise projects, internships, and coursework.',
   'Mid-level: emphasise ownership, impact, and technical leadership.',
   'Senior: emphasise architecture, mentoring, and business outcomes.',
  ]),
 ]),
 'Business_Analysis_Resume_Guide.pdf': ('Business Analysis', [
  ('Relevant Resume Sections', [
   'Summary highlighting analytical and stakeholder skills.',
   'Experience with requirements and process improvement.',
   'Skills: analysis, documentation, tools.',
   'Projects demonstrating business impact.',
   'Education and certifications (CBAP, CCBA where applicable).',
  ]),
  ('Recommended Section Ordering', [
   'Summary, Experience, Skills, Projects, Education, Certifications.',
  ]),
  ('Skills and Competencies', [
   'Requirements elicitation, process modelling, data analysis.',
   'Stakeholder management, documentation, UAT coordination.',
   'BULLET:Tools: Excel, SQL, Jira, Confluence, Visio, Tableau.',
  ]),
  ('Describing Responsibilities', [
   'Describe the business problem, stakeholders, and your analysis approach.',
   'Mention deliverables: BRDs, user stories, process maps.',
  ]),
  ('Measurable Achievements', [
   'Quantify process improvements, cost savings, or time reductions when verified.',
   'Describe decision support provided to leadership.',
  ]),
  ('Common Mistakes', [
   'Focusing on tools over business outcomes.',
   'Listing every document type without impact.',
   'Ignoring domain knowledge.',
  ]),
  ('Customising for Job Descriptions', [
   'Highlight domain expertise matching the posting.',
   'Mirror terminology from the job description.',
  ]),
  ('Before-and-After Bullets', [
   'Before: "Gathered requirements." After: "Elicited and documented requirements from 8 stakeholders, reducing rework cycles."',
   'Before: "Created reports." After: "Built weekly KPI dashboards used by leadership for operational decisions."',
  ]),
  ('Experience-Level Guidance', [
   'Entry-level: coursework, case studies, internships.',
   'Mid-level: end-to-end delivery ownership.',
   'Senior: strategy, mentoring, cross-functional leadership.',
  ]),
 ]),
 'Product_Project_Management_Resume_Guide.pdf': ('Product & Project Management', [
  ('Relevant Resume Sections', [
   'Summary positioning product/project focus.',
   'Experience with delivery, roadmap, and stakeholders.',
   'Skills: prioritisation, agile, metrics.',
   'Projects and outcomes.',
   'Education and certifications (PMP, CSM, PSPO).',
  ]),
  ('Recommended Section Ordering', [
   'Summary, Experience, Skills, Projects, Education, Certifications.',
  ]),
  ('Skills and Competencies', [
   'Roadmap planning, backlog management, sprint execution.',
   'Stakeholder alignment, risk management, metrics tracking.',
   'BULLET:Tools: Jira, Confluence, Figma, analytics platforms.',
  ]),
  ('Describing Responsibilities', [
   'Describe product/problem, users, and business goal.',
   'Mention team size and delivery cadence.',
  ]),
  ('Measurable Achievements', [
   'Quantify shipped features, adoption, or efficiency gains when verified.',
   'Describe experiments and learnings.',
  ]),
  ('Common Mistakes', [
   'Listing features without outcomes.',
   'Confusing project management with product management.',
   'No metrics on delivery performance.',
  ]),
  ('Customising for Job Descriptions', [
   'Align to product vs project focus of the role.',
   'Highlight relevant industry experience.',
  ]),
  ('Before-and-After Bullets', [
   'Before: "Managed project." After: "Led 6-month delivery of customer portal with 5 engineers, on time and within budget."',
   'Before: "Prioritised backlog." After: "Prioritised backlog using customer feedback, increasing feature adoption."',
  ]),
  ('Experience-Level Guidance', [
   'Entry-level: associate roles, internships, side projects.',
   'Mid-level: end-to-end product ownership.',
   'Senior: portfolio strategy, mentoring, org impact.',
  ]),
 ]),
 'Finance_Resume_Guide.pdf': ('Finance', [
  ('Relevant Resume Sections', [
   'Summary with domain and specialisation.',
   'Experience in reporting, analysis, compliance.',
   'Skills: accounting, financial modelling, tools.',
   'Education: CA, CFA, MBA, commerce degrees.',
   'Certifications.',
  ]),
  ('Recommended Section Ordering', [
   'Summary, Experience, Skills, Education, Certifications.',
  ]),
  ('Skills and Competencies', [
   'Financial reporting, analysis, budgeting, forecasting.',
   'Compliance, audit support, reconciliation.',
   'BULLET:Tools: Excel, Tally, SAP, Power BI, SQL.',
  ]),
  ('Describing Responsibilities', [
   'Describe scope: entities, volume, reporting cadence.',
   'Mention compliance frameworks and stakeholders.',
  ]),
  ('Measurable Achievements', [
   'Quantify cost savings, accuracy improvements, or cycle-time reductions when verified.',
   'Describe process improvements and automation.',
  ]),
  ('Common Mistakes', [
   'Listing software without accounting knowledge.',
   'No mention of compliance or accuracy.',
   'Unexplained employment gaps.',
  ]),
  ('Customising for Job Descriptions', [
   'Highlight relevant domain: banking, FMCG, startups.',
   'Match accounting standards and tools.',
  ]),
  ('Before-and-After Bullets', [
   'Before: "Prepared reports." After: "Prepared monthly MIS for leadership, improving reporting cycle time."',
   'Before: "Did reconciliation." After: "Reconciled 200+ accounts monthly with zero audit findings."',
  ]),
  ('Experience-Level Guidance', [
   'Entry-level: internships, articleship, coursework.',
   'Mid-level: ownership of reporting and analysis.',
   'Senior: strategy, team leadership, M&A support.',
  ]),
 ]),
 'Sales_Marketing_Resume_Guide.pdf': ('Sales & Marketing', [
  ('Relevant Resume Sections', [
   'Summary with revenue/growth focus.',
   'Experience in pipeline, campaigns, client management.',
   'Skills: selling, marketing channels, analytics.',
   'Achievements with metrics.',
   'Education.',
  ]),
  ('Recommended Section Ordering', [
   'Summary, Experience, Skills, Education, Certifications.',
  ]),
  ('Skills and Competencies', [
   'Prospecting, negotiation, account management.',
   'Campaign planning, content, digital marketing, analytics.',
   'BULLET:Tools: CRM (Salesforce, HubSpot), Google Analytics, ad platforms.',
  ]),
  ('Describing Responsibilities', [
   'Describe target segment, product, and sales cycle.',
   'Mention team structure and territory.',
  ]),
  ('Measurable Achievements', [
   'Quantify revenue, targets achieved, pipeline growth when verified.',
   'Describe campaign ROI and lead generation.',
  ]),
  ('Common Mistakes', [
   'Vague claims without numbers.',
   'Listing channels without results.',
   'Ignoring customer retention.',
  ]),
  ('Customising for Job Descriptions', [
   'Match B2B vs B2C focus.',
   'Highlight relevant industry and deal size.',
  ]),
  ('Before-and-After Bullets', [
   'Before: "Handled sales." After: "Managed 40+ accounts, achieving 110% of quarterly target."',
   'Before: "Ran campaigns." After: "Executed digital campaigns generating 500+ qualified leads."',
  ]),
  ('Experience-Level Guidance', [
   'Entry-level: SDR, marketing associate, internships.',
   'Mid-level: account ownership, campaign ownership.',
   'Senior: strategy, team leadership, P&L.',
  ]),
 ]),
 'Management_Operations_Resume_Guide.pdf': ('Management & Operations', [
  ('Relevant Resume Sections', [
   'Summary with operations/scale focus.',
   'Experience in process, team, and vendor management.',
   'Skills: operations, leadership, analytics.',
   'Education and certifications.',
  ]),
  ('Recommended Section Ordering', [
   'Summary, Experience, Skills, Education, Certifications.',
  ]),
  ('Skills and Competencies', [
   'Process design, SOPs, quality management.',
   'Team leadership, vendor management, budgeting.',
   'BULLET:Tools: Excel, ERP, BI tools, project management software.',
  ]),
  ('Describing Responsibilities', [
   'Describe scale: team size, volume, locations.',
   'Mention process improvements and compliance.',
  ]),
  ('Measurable Achievements', [
   'Quantify efficiency gains, cost reductions, quality improvements when verified.',
   'Describe transformation initiatives.',
  ]),
  ('Common Mistakes', [
   'Generic "managed operations" without scale.',
   'No mention of people leadership.',
   'Ignoring compliance and safety.',
  ]),
  ('Customising for Job Descriptions', [
   'Match industry and operational complexity.',
   'Highlight relevant certifications.',
  ]),
  ('Before-and-After Bullets', [
   'Before: "Managed team." After: "Led team of 12 across 2 shifts, improving throughput."',
   'Before: "Improved process." After: "Redesigned workflow reducing turnaround time."',
  ]),
  ('Experience-Level Guidance', [
   'Entry-level: coordinator, analyst roles.',
   'Mid-level: manager with P&L or team ownership.',
   'Senior: director-level strategy and transformation.',
  ]),
 ]),
}

for fname, (track, sections) in tracks.items():
    make_guide(fname, track, sections)

print('ALL GUIDES DONE')
