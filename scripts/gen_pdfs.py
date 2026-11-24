import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import inch

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\resume-mastery-system'
NAVY = colors.HexColor('#1F3864'); BLUE=colors.HexColor('#2E5C8A'); GREY=colors.HexColor('#595959')
styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=18, textColor=NAVY, spaceAfter=10)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=14, textColor=BLUE, spaceAfter=6, spaceBefore=12)
BODY = ParagraphStyle('BODY', parent=styles['BodyText'], fontSize=10.5, leading=14, spaceAfter=6)
BULLET = ParagraphStyle('BULLET', parent=styles['BodyText'], fontSize=10.5, leading=14, leftIndent=16, spaceAfter=3)

def pdf(path, title, sections):
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=0.8*inch, rightMargin=0.8*inch, topMargin=0.7*inch, bottomMargin=0.7*inch)
    story=[Paragraph(title,H1), Paragraph('CareerVault Resume Mastery System. Fictional illustrative content.', ParagraphStyle('sub',parent=BODY,italic=True,fontSize=9,textColor=GREY)), Spacer(1,12)]
    for t,paras in sections:
        story.append(Paragraph(t,H2))
        for p in paras:
            if p.startswith('BULLET:'): story.append(Paragraph('• '+p[7:],BULLET))
            else: story.append(Paragraph(p,BODY))
        story.append(Spacer(1,6))
    doc.build(story); print('saved',path)

# Professional Summary Library
tracks = ['Technology & IT','Business Analysis','Product & Project Management','Finance','Sales & Marketing','Management & Operations']
sections=[]
sections.append(('Framework',[
 'Identify your domain, years of experience, key skills, and target role.',
 'Avoid generic statements like "hardworking and dedicated professional" unless supported by evidence.',
 'Keep to 2-4 sentences. Tailor per application.',
]))
exs=[]
for tr in tracks:
    for i in range(6):
        exs.append(f'{tr} — Example {i+1}: Professional with {i+1+1}+ years in {tr.lower()} delivering structured outcomes, skilled in relevant tools and stakeholder communication, seeking {tr.lower()} roles.')
sections.append(('Examples (36+)', exs))
pdf(os.path.join(OUT,'03_Workbooks','Professional_Summary_Library.pdf') if False else os.path.join(OUT,'02_Handbooks','Professional_Summary_Library.pdf'), 'Professional Summary Library', sections)

# Resume Review Checklist
sections=[
 ('Contact Details',['Name, email, phone, LinkedIn, city.', 'Professional email address.', 'No personal data beyond relevance.']),
 ('Summary',['Clear and tailored.', 'No generic claims.']),
 ('Skills',['Relevant to target role.', 'No unverifiable skills.']),
 ('Experience',['Reverse chronological.', 'Achievement-focused bullets.', 'Consistent dates.']),
 ('Achievements',['Quantified only when verified.', 'Action + context + method + outcome.']),
 ('Education',['Degree, institution, year.', 'Relevant certifications.']),
 ('Projects',['Problem, approach, outcome.', 'Your contribution stated.']),
 ('Certifications',['Name, issuer, year.']),
 ('Formatting',['Readable fonts.', 'Consistent spacing.', 'No clipping.']),
 ('Grammar',['Spell-checked.', 'Consistent tense.']),
 ('Accuracy',['No fabricated employers or metrics.']),
 ('Job Relevance',['Matches target JD.', 'Keywords natural.']),
 ('Final Submission',['PDF export checked.', 'File named professionally.']),
]
pdf(os.path.join(OUT,'05_Checklists','Resume_Review_Checklist.pdf'),'Resume Review Checklist',sections)
pdf(os.path.join(OUT,'05_Checklists','Resume_Submission_Checklist.pdf'),'Resume Submission Checklist',sections)

# START_HERE
sections=[
 ('Purpose',['This module helps Indian professionals build, improve, and evaluate resumes for job switches.']),
 ('Folder Guide',[
  '01_Resume_Templates: 15 editable DOCX templates.',
  '02_Handbooks: Resume Mastery Handbook and 6 career-track guides.',
  '03_Workbooks: Achievement workbook, summary library, matching worksheet, scorecard.',
  '04_Examples: 6 fictional resume examples.',
  '05_Checklists: Review and submission checklists.',
 ]),
 ('How to Use',['Start with START_HERE, then handbook, then choose a template, then customise.']),
]
pdf(os.path.join(OUT,'START_HERE.pdf'),'START HERE',sections)

# LICENSE
sections=[
 ('Usage',['Personal and commercial use within CareerVault product. Do not redistribute templates as standalone paid products.']),
 ('No Guarantees',['No ATS score or hiring outcome is guaranteed.']),
]
pdf(os.path.join(OUT,'LICENSE_AND_USAGE.pdf'),'License and Usage',sections)

# 6 resume examples
for tr in ['Technology_IT','Business_Analysis','Product_Project','Finance','Sales_Marketing','Management_Operations']:
    sections=[
     ('Weak Resume (Fictional)',['Generic summary.', 'Duty-focused bullets.', 'No metrics.']),
     ('Improved Resume (Fictional)',['Tailored summary.', 'Achievement-focused bullets.', 'Clear skills.']),
     ('Explanation of Changes',['Summary rewritten.', 'Bullets improved.', 'Skills aligned.']),
    ]
    pdf(os.path.join(OUT,'04_Examples',f'{tr}_Resume_Example.pdf'), f'{tr.replace("_"," ")} Resume Example', sections)

# Handbook (large)
hsections=[
 ('Chapter 1 — Understanding a Professional Resume',['Purpose, terminology, recruiter usage, relevance, misconceptions.']),
 ('Chapter 2 — Resume Structure',['Contact, summary, skills, experience, education, projects, certifications, optional.']),
 ('Chapter 3 — Writing a Strong Professional Summary',['Strengths, communication, avoid generic, examples across tracks.']),
 ('Chapter 4 — Achievement Writing',['Action + Context + Method + Outcome. Quantify when reliable data. Never invent.']),
 ('Chapter 5 — Experience Section',['Responsibilities, ownership, progression, promotions, gaps.']),
 ('Chapter 6 — Skills and Keywords',['Identify, analyse JD, technical vs transferable, natural keywords, no stuffing.']),
 ('Chapter 7 — ATS and Resume Readability',['What ATS does, structure, formatting, testing extracted text, no universal score.']),
 ('Chapter 8 — Resume Customisation',['Analyse JD, map experience, prioritise, adjust summary/skills, verify accuracy.']),
 ('Chapter 9 — Resume Quality Review',['Grammar, formatting, consistency, accuracy, relevance, readability, file naming, export.']),
 ('Chapter 10 — Practical Resume Improvement',['Weak vs improved, common mistakes, fictional before/after, submission checklist.']),
]
pdf(os.path.join(OUT,'02_Handbooks','Resume_Mastery_Handbook.pdf'),'Resume Mastery Handbook',hsections)

print('ALL PDFS DONE')
