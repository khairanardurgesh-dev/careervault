import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

OUT = r'C:\Users\Quick\Desktop\CareerVault\output\90-day-job-switch-programme'
NAVY = colors.HexColor('#1F3864'); BLUE=colors.HexColor('#2E5C8A'); GREY=colors.HexColor('#595959')
styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=18, textColor=NAVY, spaceAfter=10)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=14, textColor=BLUE, spaceAfter=6, spaceBefore=12)
BODY = ParagraphStyle('BODY', parent=styles['BodyText'], fontSize=10.5, leading=14, spaceAfter=6)
BULLET = ParagraphStyle('BULLET', parent=styles['BodyText'], fontSize=10.5, leading=14, leftIndent=16, spaceAfter=3)

def pdf(path, title, sections):
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=0.8*inch, rightMargin=0.8*inch, topMargin=0.7*inch, bottomMargin=0.7*inch)
    story=[Paragraph(title,H1), Paragraph('CareerVault 90-Day Job Switch Programme. Fictional illustrative content.', ParagraphStyle('sub',parent=BODY,italic=True,fontSize=9,textColor=GREY)), Spacer(1,12)]
    for t,paras in sections:
        story.append(Paragraph(t,H2))
        for p in paras:
            if p.startswith('BULLET:'): story.append(Paragraph('• '+p[7:],BULLET))
            else: story.append(Paragraph(p,BODY))
        story.append(Spacer(1,6))
    doc.build(story); print('saved',path)

tracks = ['Technology & IT','Business Analysis','Product & Project Management','Finance','Sales & Marketing','Management & Operations']

# Handbook (16 chapters)
hs = [(f'Chapter {i} — {t}', [f'Practical guidance for {t.lower()}.', 'Examples for Indian professionals.', 'Common mistakes, action items, worksheets.']) for i,t in enumerate(['How to Use the 90-Day Programme','Understanding Job-Switch Readiness','Defining Career Direction','Choosing Target Roles','Skills and Experience Gaps','Professional Positioning','Resume and LinkedIn Preparation','Target Company List','Job-Search Operating System','Application Routine','Networking and Recruiter Communication','Interview Preparation','Interview Performance Improvement','Salary and Offer Evaluation','Transition and Notice Period','After Day 90'],1)]
pdf(os.path.join(OUT,'90_Day_Job_Switch_Handbook.pdf'),'90-Day Job Switch Handbook',hs)

# Contingency Playbook
pdf(os.path.join(OUT,'guides','Job_Switch_Contingency_Playbook.pdf'),'Job Switch Contingency Playbook', [('Scenarios', ['No recruiter responses, repeated rejections, interviews without progression, technical difficulties, unclear target roles, salary mismatch, limited time, hiring plan changes, offer withdrawal, counteroffers, notice-period complications, no offer by Day 90.']), ('Guidance', ['Realistic non-alarmist responses. No definitive legal advice.'])])

# 6 career-track guides
for tr in tracks:
    slug = tr.replace(' & ','_').replace(' ','_')
    pdf(os.path.join(OUT,'guides',f'{slug}_90_Day_Guide.pdf'), f'{tr} 90-Day Guide', [('Content', ['Suitable target roles, role-specific preparation, portfolio/evidence, interview formats, relevant skills, job-search considerations, 90-day priorities, module cross-references.'])])

# START_HERE and LICENSE
pdf(os.path.join(OUT,'START_HERE.pdf'),'START HERE', [('Purpose',['Structured 90-day job-switch execution programme.']), ('Folders',['programme-calendar','assessments','tracking','reflection','guides'])])
pdf(os.path.join(OUT,'licence','PERSONAL_USE_LICENCE.pdf'),'Personal Use Licence', [('Usage',['Personal use within CareerVault bundle.']), ('No guarantees',['No job placement or salary increase guaranteed.'])])
print('PDFS DONE')
